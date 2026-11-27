# -*- coding: utf-8 -*-
r"""把仓库里的条目渲染成静态站点 `site/`——不克隆也能看。

用法：
    python tools/build_site.py            # 生成到 site/
    python tools/build_site.py --out site

产物：
    site/index.html        落地页：规模、主线、样例语料、样例卡片、术语抽样
    site/p/index.html      全部译注工程总表（可搜索）
    site/p/<id>.html       单部工程详情（底本、作者、台账、语料段数、入口）
    site/cards/index.html  全部资料卡统一入口（按系列/类型/状态筛选）
    site/corpus.html       语料样例（按包/环境抽样，带 flags）
    site/terms.html        术语基全表（可搜索）
    site/compliance.html   许可与合规口径（LIKE LICENSE §0–§1）
    site/catalog.json      机器可读目录
    site/assets/style.css  共享样式

数据全部来自本仓：git 索引、RELEASE_REGISTER.csv、03_translations_meta/、
datasets/**/cards/、01_corpus_zh/。改完数据重跑本脚本即可，不要手改 site/。
"""
import csv
import html
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

THEMES = {
    "01": ("镜像对称与同调镜像对称", "Mirror Symmetry & HMS"),
    "02": ("几何朗兰兹与电磁对偶", "Geometric Langlands & EM Duality"),
    "03": ("量子场论与规范理论", "QFT & Gauge Theory"),
    "04": ("弦论与紧致化", "Strings & Compactification"),
    "05": ("辛几何 · 拓扑 · 纽结 · 指标定理", "Symplectic, Topology, Knots & Index"),
    "07": ("其他几何（热带 / 范畴 / 量子力学）", "Misc. Geometry"),
    "08": ("双有理几何与教材", "Birational Geometry & Textbooks"),
    "99": ("拓扑学与专题", "Topology & Misc."),
}
TYPES = ["concept", "derivation", "correction", "example", "statement", "remark"]
STATUS_ZH = {"published": "已发布", "reviewed": "已复核", "draft": "草稿", "dev": "开发中"}


def load_stats():
    """站点上的规模数字只从 `_meta/stats.json` 取，不在这里手写。"""
    try:
        return json.load(io.open(os.path.join(ROOT, "_meta", "stats.json"), encoding="utf-8"))
    except Exception:
        return {}


ST = load_stats()


def stnum(path, default=0):
    cur = ST
    for key in path.split("."):
        if isinstance(cur, dict) and key in cur:
            cur = cur[key]
        else:
            return default
    return cur if isinstance(cur, (int, float)) else default


def fmtn(n):
    return "{:,}".format(int(n))


def esc(s):
    return html.escape(str(s if s is not None else ""), quote=True)


MATH = re.compile(r"\$([^$\n]{1,300})\$")


def fmt(s):
    """转义 + 把行内公式包成 <code>，离线也能读（不依赖 CDN 渲染）。"""
    e = esc(s)
    return MATH.sub(lambda m: '<code class="m">$%s$</code>' % m.group(1), e)


def tracked(prefix=None):
    args = ["git", "-C", ROOT, "ls-files"] + ([prefix] if prefix else [])
    out = subprocess.run(args, capture_output=True)
    return out.stdout.decode("utf-8", "replace").splitlines()


def load_register():
    p = os.path.join(ROOT, "RELEASE_REGISTER.csv")
    rows = {}
    with io.open(p, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            rows[r["id"]] = r
    return rows


def parse_meta(pid):
    """从 03_translations_meta/<id>/投稿信息.md 取题名/作者/等级。"""
    p = os.path.join(ROOT, "03_translations_meta", pid, "投稿信息.md")
    info = {"orig": "", "author": "", "level": "", "kind": "", "pub": ""}
    if not os.path.isfile(p):
        return info
    txt = io.open(p, encoding="utf-8", errors="replace").read()
    for key, pat in (("orig", r"^-\s*原文题名：\s*(.+)$"), ("author", r"^-\s*原作者：\s*(.+)$"),
                     ("kind", r"^-\s*类型：\s*(.+)$"), ("pub", r"^-\s*出版/底本信息：\s*(.+)$")):
        m = re.search(pat, txt, re.M)
        if m:
            info[key] = m.group(1).strip()
    m = re.search(r"^-\s*推荐等级：\s*([ABC])", txt, re.M)
    if m:
        info["level"] = m.group(1)
    return info


def load_cards():
    cards = []
    for rel in tracked("datasets"):
        if "/cards/" not in rel or not rel.endswith(".json"):
            continue
        try:
            c = json.load(io.open(os.path.join(ROOT, rel), encoding="utf-8"))
        except Exception:
            continue
        c["_series"] = rel.split("/")[1]
        cards.append(c)
    return cards


def corpus_counts():
    p = os.path.join(ROOT, "01_corpus_zh", "zh_paragraphs.jsonl")
    per, total, formulas = {}, 0, 0
    if not os.path.isfile(p):
        return per, 0, 0
    for line in io.open(p, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        total += 1
        per[r.get("pkg", "")] = per.get(r.get("pkg", ""), 0) + 1
        t = r.get("text") or ""
        if "$" in t or "\\begin{" in t:
            formulas += 1
    return per, total, formulas


def corpus_samples(n=240):
    p = os.path.join(ROOT, "01_corpus_zh", "zh_paragraphs.jsonl")
    rows = []
    if not os.path.isfile(p):
        return rows
    every = max(1, (stnum("corpus.paragraphs") or 49322) // n)
    for i, line in enumerate(io.open(p, encoding="utf-8")):
        if i % every:
            continue
        try:
            r = json.loads(line)
        except Exception:
            continue
        rows.append(r)
    return rows[:n]


def load_terms():
    p = os.path.join(ROOT, "01_corpus_zh", "termbase.jsonl")
    rows = []
    if not os.path.isfile(p):
        return rows
    for line in io.open(p, encoding="utf-8"):
        try:
            rows.append(json.loads(line))
        except Exception:
            pass
    return rows


CSS = """
:root{--bg:#0b0f15;--panel:#111823;--panel2:#151e2b;--line:rgba(255,255,255,.09);
--txt:#e8eef8;--txt2:#a6b6cc;--txt3:#7d8ea6;--brand:#4d7cfe;--brand2:#6f97ff;--accent:#3ddad0}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1100px 600px at 12% -8%,rgba(77,124,254,.16),transparent 60%),
radial-gradient(900px 500px at 92% 4%,rgba(61,218,208,.10),transparent 62%),var(--bg);
color:var(--txt);font-family:"Noto Sans SC","Microsoft YaHei","PingFang SC",system-ui,sans-serif;
font-size:15px;line-height:1.7;-webkit-font-smoothing:antialiased}
a{color:var(--brand2);text-decoration:none}a:hover{color:#9ab8ff}
.wrap{max-width:1180px;margin:0 auto;padding:0 26px}
header.top{padding:38px 0 22px;border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:14px}
.logo{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,#2f55cc,#4d7cfe 60%,#5f8dff);
box-shadow:0 8px 26px rgba(77,124,254,.42);display:grid;place-items:center;font-weight:700;color:#fff}
.brand h1{font-size:21px;margin:0}.brand .sub{color:var(--txt3);font-size:13px}
nav.meta{margin-left:auto;color:var(--txt3);font-size:13px;text-align:right;line-height:1.9}
nav.meta a{margin-left:14px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:13px;margin:24px 0 6px}
.stat{background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.015));
border:1px solid var(--line);border-radius:15px;padding:15px 17px}
.stat b{display:block;font-size:25px;color:#fff}.stat span{color:var(--txt3);font-size:12.5px}
.themes{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:13px;margin:22px 0}
.tcard{display:block;background:var(--panel);border:1px solid var(--line);border-radius:15px;padding:16px 18px;transition:.18s}
.tcard:hover{border-color:rgba(77,124,254,.55);transform:translateY(-2px)}
.tcard h3{margin:0 0 4px;font-size:15.5px}.tcard .en{color:var(--txt3);font-size:12px}
.tcard .cnt{margin-top:10px;color:var(--accent);font-size:12.5px}
h2.sec{font-size:17px;margin:36px 0 10px;padding-left:11px;border-left:3px solid var(--brand)}
p.lead{color:var(--txt2);margin:6px 0 14px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:15px;padding:16px 20px;margin:12px 0}
.card .meta{color:var(--txt3);font-size:12.5px;margin-bottom:8px}
.card h3{margin:2px 0 8px;font-size:16.5px}
.quote{background:var(--panel2);border:1px solid var(--line);border-radius:12px;padding:12px 15px;margin:9px 0;
color:var(--txt2);font-size:14px}
.quote .k{color:var(--txt3);font-size:11.5px;font-family:ui-monospace,Consolas,monospace}
input.search{width:100%;background:var(--panel2);border:1px solid var(--line);border-radius:12px;
padding:11px 15px;color:var(--txt);font-size:14px;outline:none;margin:14px 0}
input.search:focus{border-color:rgba(77,124,254,.7);box-shadow:0 0 0 3px rgba(77,124,254,.16)}
table{width:100%;border-collapse:collapse;font-size:14px;margin:10px 0}
th,td{text-align:left;padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--txt3);font-weight:600;font-size:12.5px;white-space:nowrap}
.pill{font-size:11.5px;padding:2px 9px;border-radius:999px;border:1px solid var(--line);color:var(--txt2);white-space:nowrap}
.pill.a{border-color:rgba(61,218,208,.5);color:#7ee9e2}.pill.b{border-color:rgba(77,124,254,.5);color:#a9c1ff}
.pill.c{border-color:rgba(155,140,255,.5);color:#c3b6ff}
footer{border-top:1px solid var(--line);margin-top:52px;padding:22px 0 44px;color:var(--txt3);font-size:12.5px}
code{font-family:ui-monospace,Consolas,monospace;font-size:13px;background:rgba(255,255,255,.05);
padding:1px 6px;border-radius:6px}
code.m{color:#cfe0ff;background:rgba(77,124,254,.12);border:1px solid rgba(77,124,254,.18)}
details{background:var(--panel);border:1px solid var(--line);border-radius:13px;padding:12px 16px;margin:9px 0}
summary{cursor:pointer;font-size:15px}
"""

MATHJAX = ""

NAV = ('<nav class="meta"><a href="index.html">总览</a><a href="p/index.html">工程</a>'
       '<a href="cards/index.html">资料卡</a><a href="corpus.html">语料</a>'
       '<a href="terms.html">术语</a><a href="compliance.html">许可</a></nav>')


SITE_BASE = os.environ.get("SITE_BASE", "https://lzxsusy.github.io/mathtranslate").rstrip("/")
SITE_NAME = "数译 · 中文数学译注文献库"
SITE_DESC = ("数译（Shuyi）是面向中文数学的开源语料库：数学讲义与专著的中文译注本、"
             "段落级中文语料、术语基与资料卡，以及自然语言与 Lean 4 的对齐。"
             "自产层 CC BY 4.0；译文层不代原作者授权。")
SITE_KEYWORDS = ("中文数学,数学译注,几何朗兰兹,镜像对称,辛几何,量子场论,"
                 "Lean 4,mathlib,形式化,数据集,语料库,Chinese mathematics,"
                 "geometric Langlands,formalization,dataset,corpus")


def seo_head(title, path, desc, up=""):
    """面向搜索引擎与 LLM 爬虫的 head：description/canonical/OG/JSON-LD/llms.txt。"""
    url = SITE_BASE + "/" + str(path).lstrip("/")
    ld = {"@context": "https://schema.org", "@type": "WebPage",
          "name": title, "description": desc, "url": url, "inLanguage": "zh-CN",
          "isPartOf": {"@type": "WebSite", "name": "数译 Shuyi", "url": SITE_BASE + "/"}}
    return ('<meta name="description" content="%s">'
            '<meta name="keywords" content="%s">'
            '<meta name="author" content="数译 Shuyi contributors">'
            '<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">'
            '<link rel="canonical" href="%s">'
            '<meta property="og:type" content="website">'
            '<meta property="og:site_name" content="%s">'
            '<meta property="og:title" content="%s">'
            '<meta property="og:description" content="%s">'
            '<meta property="og:url" content="%s">'
            '<meta property="og:locale" content="zh_CN">'
            '<meta name="twitter:card" content="summary">'
            '<meta name="twitter:title" content="%s">'
            '<meta name="twitter:description" content="%s">'
            '<link rel="alternate" type="text/plain" href="%sllms.txt" title="llms.txt">'
            '<link rel="alternate" type="text/plain" href="%sllms-full.txt" title="llms-full.txt">'
            '<script type="application/ld+json">%s</script>'
            ) % (esc(desc), SITE_KEYWORDS, url, esc(SITE_NAME), esc(title), esc(desc), url,
                 esc(title), esc(desc), up, up, json.dumps(ld, ensure_ascii=False))


def page(title, body, depth=0, extra_head="", path="index.html", desc=None):
    up = "../" * depth
    nav = NAV.replace('href="', 'href="%s' % up).replace('%s%s' % (up, up), up)
    seo = seo_head(title, path, desc or SITE_DESC, up)
    return """<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t} · 数译 mathtranslate</title>
<link rel="stylesheet" href="{up}assets/style.css">{seo}{eh}</head><body>
<div class="wrap"><header class="top"><div class="brand">
<div class="logo">数</div><div><h1>数译 · 中文数学译注文献库</h1>
<div class="sub">mathtranslate · {n_proj} 部译注工程 · {n_para} 段中文语料 · {n_card} 张资料卡</div></div>{nav}</div></header>
{body}
<footer>许可：自产层 CC BY 4.0；译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制
（检索、研究、教学、训练均可），权利人通知即撤 · 见 <a href="{up}compliance.html">许可与合规</a> 与仓内 LICENSE</footer>
</div></body></html>""".format(t=esc(title), body=body, up=up, nav=nav, mj=MATHJAX, eh=extra_head, seo=seo,
                              n_proj=fmtn(stnum("projects.total", 113)),
                              n_para=fmtn(stnum("corpus.paragraphs", 49322)),
                              n_card=fmtn(stnum("datasets.cards_total", 1034)))


def write_page(out, path, title, body, depth=0, desc=None, extra_head=""):
    full = os.path.join(out, path)
    os.makedirs(os.path.dirname(full) or out, exist_ok=True)
    io.open(full, "w", encoding="utf-8", newline="\n").write(
        page(title, body, depth=depth, desc=desc, extra_head=extra_head, path=path))


def build():
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else os.path.join(ROOT, "site")
    for sub in ("p", "cards", "assets"):
        os.makedirs(os.path.join(out, sub), exist_ok=True)
    io.open(os.path.join(out, "assets", "style.css"), "w", encoding="utf-8", newline="\n").write(CSS)

    reg = load_register()
    per_pkg, total_paras, formulas = corpus_counts()
    dirs = sorted({ln.split("/")[1] for ln in tracked("08_source_code") if ln.count("/") >= 2})
    projs = []
    for d in dirs:
        pid = d.split("_", 1)[0]
        cn = d.split("_", 1)[1] if "_" in d else d
        tset = [ln for ln in tracked("08_source_code") if ln.split("/")[1] == d]
        meta = parse_meta(pid)
        r = reg.get(pid, {})
        projs.append({
            "id": pid, "dir": d, "cn": cn, "orig": meta["orig"], "author": meta["author"],
            "level": meta["level"] or "B", "kind": r.get("底本类型", ""),
            "release": r.get("成品级别", ""), "risk": r.get("风险", ""),
            "tex": sum(1 for ln in tset if ln.lower().endswith(".tex")),
            "figs": sum(1 for ln in tset if "/figures/" in ln.lower()
                        and ln.lower().endswith((".png", ".jpg", ".jpeg", ".svg", ".pdf"))),
            "files": len(tset), "paras": per_pkg.get(pid, 0),
        })
    cards = load_cards()
    terms = load_terms()
    n_src = sum(1 for p in projs if p["tex"])
    # 与 make_stats.py 的口径一致：排除 MANIFEST.json / _build_summary.json 两个自指文件
    total_files = stnum("repo.tracked_files", 0) or len(tracked())

    # ---------- catalog.json ----------
    cat = [{k: p[k] for k in ("id", "cn", "orig", "author", "level", "kind", "release", "tex", "figs", "paras")}
           for p in projs]
    io.open(os.path.join(out, "catalog.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(cat, ensure_ascii=False, indent=1))

    # ---------- 总览 ----------
    by_theme = {}
    for p in projs:
        key = p["id"][2:4]
        by_theme.setdefault(key, []).append(p)
    theme_cards = []
    for key in sorted(by_theme):
        name, en = THEMES.get(key, ("其他", "Other"))
        items = by_theme[key]
        theme_cards.append(
            '<a class="tcard" href="p/index.html#SY%s"><h3>%s</h3><div class="en">%s</div>'
            '<div class="cnt">%d 部 · %d 部带源码</div></a>'
            % (key, esc(name), esc(en), len(items), sum(1 for x in items if x["tex"])))

    sample_cards = [c for c in cards if c.get("type") == "concept" and c.get("status") in ("published", "reviewed")][:2]
    card_html = []
    for c in sample_cards:
        card_html.append(
            '<div class="card"><div class="meta">%s · %s · %s</div><h3>%s</h3>'
            '<div>%s</div><div class="quote"><span class="k">key_points</span><br>%s</div></div>'
            % (esc(c.get("_series")), esc(c.get("type")), esc(c.get("status")),
               fmt(c.get("title")), fmt((c.get("summary") or "")[:300]),
               fmt(" · ".join(c.get("key_points") or [])[:400])))

    paras = corpus_samples(3)
    para_html = "".join('<div class="quote"><span class="k">%s · para %s · env=%s · tier=%s</span><br>%s</div>'
                        % (esc(r.get("pkg")), esc(r.get("para_id", r.get("para"))),
                           esc(r.get("env")), esc(r.get("tier")), fmt((r.get("text") or "")[:400]))
                        for r in paras)
    term_html = "".join("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
                        % (esc(t.get("foreign")), esc(t.get("lang")), esc(t.get("zh")), esc(t.get("status")))
                        for t in terms[:8])

    body = """
<div class="stats">
<div class="stat"><b>%d</b><span>部译注工程</span></div>
<div class="stat"><b>%d</b><span>部带 LaTeX 源码</span></div>
<div class="stat"><b>%s</b><span>段中文语料（含公式 %s）</span></div>
<div class="stat"><b>%d</b><span>张资料卡</span></div>
<div class="stat"><b>%s</b><span>条术语</span></div>
<div class="stat"><b>%s</b><span>个仓库文件</span></div>
</div>
<p class="lead">这是一个中文数学译注库：把镜像对称、几何朗兰兹、量子场论、辛几何等方向的讲义与专著
逐段译成中文，并附术语表、资料卡与可编译 LaTeX 源码。<b>不用克隆</b>——本页与下列页面直接给出内容样例；
要全文/全量数据时再取仓库。</p>

<h2 class="sec">按主线浏览</h2>
<div class="themes">%s</div>

<h2 class="sec">资料卡样例（共 %d 张，<a href="cards/index.html">全部入口</a>）</h2>
%s

<h2 class="sec">语料样例（共 %s 段，<a href="corpus.html">更多</a>）</h2>
%s

<h2 class="sec">术语抽样（共 %s 条，<a href="terms.html">全表</a>）</h2>
<table><tr><th>外文</th><th>语种</th><th>中文</th><th>状态</th></tr>%s</table>

<h2 class="sec">怎么用</h2>
<div class="card"><div class="meta">三条路，按需要选</div>
<ul>
<li><b>只想读</b>：<a href="p/index.html">工程总表</a> → 选一部 → 详情页给出底本、作者、语料段数与入口；
成品 PDF 按台账分级（随仓公开 / Release 外链 / 按 §4 申请 / 不公开）。</li>
<li><b>想拿语料训练</b>：<code>01_corpus_zh/zh_paragraphs.jsonl</code>（{n_para} 段，字段见
<a href="compliance.html">DATASHEET.md</a>）；训练前建议按 <code>flags</code> 过滤
<code>orphan_number / empty_ref</code>，按 <code>para_id</code> 去重。</li>
<li><b>想接管术语</b>：<code>01_corpus_zh/termbase.jsonl</code>（{n_term} 条，{n_cand} 条 candidate 待裁决）。</li>
</ul></div>
""" % (len(projs), n_src, "{:,}".format(total_paras), "{:,}".format(formulas), len(cards),
       "{:,}".format(len(terms)), "{:,}".format(total_files), "".join(theme_cards), len(cards), "".join(card_html),
       "{:,}".format(total_paras), para_html, "{:,}".format(len(terms)), term_html)
    body = (body.replace("{n_para}", fmtn(total_paras))
                .replace("{n_term}", fmtn(len(terms)))
                .replace("{n_cand}", fmtn(sum(1 for t in terms if t.get("status") == "candidate"))))
    ds_ld = {"@context": "https://schema.org", "@type": "Dataset",
             "name": "数译 Shuyi · 中文数学译注语料与资料卡",
             "alternateName": "Shuyi Chinese mathematical corpus",
             "description": SITE_DESC,
             "url": SITE_BASE + "/",
             "sameAs": ["https://github.com/lzxsusy/mathtranslate",
                        "https://atomgit.com/lzxSUSUY/mathtranslate"],
             "inLanguage": "zh-CN",
             "license": "https://creativecommons.org/licenses/by/4.0/",
             "creator": {"@type": "Organization", "name": "数译 Shuyi contributors"},
             "keywords": ["中文数学", "数学译注", "几何朗兰兹", "Lean 4", "mathlib",
                          "形式化", "中文语料", "dataset", "geometric Langlands"],
             "size": "%d 段中文语料 / %d 张资料卡 / %d 部译注工程" % (total_paras, len(cards), len(projs)),
             "distribution": [
                 {"@type": "DataDownload", "name": "zh_paragraphs.jsonl",
                  "contentUrl": "https://github.com/lzxsusy/mathtranslate/raw/master/01_corpus_zh/zh_paragraphs.jsonl",
                  "encodingFormat": "application/x-ndjson"},
                 {"@type": "DataDownload", "name": "termbase.jsonl",
                  "contentUrl": "https://github.com/lzxsusy/mathtranslate/raw/master/01_corpus_zh/termbase.jsonl",
                  "encodingFormat": "application/x-ndjson"},
                 {"@type": "DataDownload", "name": "cards (JSON)",
                  "contentUrl": "https://github.com/lzxsusy/mathtranslate/tree/master/datasets",
                  "encodingFormat": "application/json"}]}
    ds_head = '<script type="application/ld+json">%s</script>' % json.dumps(ds_ld, ensure_ascii=False)
    write_page(out, "index.html", "总览", body, desc=(
        "数译（Shuyi）：%d 部数学文献的中文译注工程、%s 段段落级中文语料、%s 条术语、%s 张资料卡。"
        "自产层 CC BY 4.0，面向检索、研究与训练。"
        % (len(projs), fmtn(total_paras), fmtn(len(terms)), fmtn(len(cards)))), extra_head=ds_head)

    # ---------- 工程总表 ----------
    rows = []
    last_theme = None
    for p in sorted(projs, key=lambda x: (x["id"][:4], x["id"])):
        th = p["id"][2:4]
        if th != last_theme:
            if last_theme is not None:
                rows.append("</tbody>")
            rows.append('<tbody id="SY%s"><tr><th colspan="7" style="color:var(--accent);padding-top:22px">%s</th></tr>'
                        % (th, esc(THEMES.get(th, ("其他", ""))[0])))
            last_theme = th
        rows.append(
            '<tr class="prow" data-k="%s %s %s"><td><a href="%s.html">%s</a></td>'
            '<td>%s<div class="meta" style="color:var(--txt3);font-size:12px">%s</div></td>'
            '<td>%s</td><td><span class="pill %s">%s 级</span></td><td>%s</td><td>%s</td><td>%d</td></tr>'
            % (esc(p["id"]), esc(p["cn"]), esc(p["orig"]), esc(p["id"]), esc(p["id"]),
               esc(p["cn"]), esc(p["orig"]), esc(p["author"]),
               p["level"].lower(), p["level"], esc(p["kind"]), esc(p["release"]), p["paras"]))
    rows.append("</tbody>")
    pidx = ("""<h2 class="sec">全部工程（%d 部，其中 %d 部带 LaTeX 源码）</h2>
<input class="search" id="q" placeholder="搜索编号 / 中文题名 / 原文题名 / 作者…">
<table id="tbl"><tr><th>编号</th><th>工程</th><th>原作者</th><th>等级</th><th>底本类型</th><th>成品</th><th>语料段</th></tr>%s</table>
<script>const q=document.getElementById('q'),rows=[...document.querySelectorAll('.prow')];
q.oninput=()=>{const v=q.value.toLowerCase();rows.forEach(r=>r.style.display=r.dataset.k.toLowerCase().includes(v)?'':'none')};</script>
""" % (len(projs), n_src, "".join(rows)))
    write_page(out, "p/index.html", "工程总表", pidx, depth=1, desc=(
        "%d 部数学文献的中文译注工程总表：底本、作者、源码、段落数与许可分级。" % len(projs)))

    # ---------- 单部详情 ----------
    for p in projs:
        rel = """
<h2 class="sec">%s · %s</h2>
<div class="stats">
<div class="stat"><b>%s</b><span>语料段</span></div>
<div class="stat"><b>%d</b><span>.tex 源文件</span></div>
<div class="stat"><b>%d</b><span>插图</span></div>
<div class="stat"><b>%d</b><span>仓库文件</span></div>
</div>
<table>
<tr><th>原文题名</th><td>%s</td></tr>
<tr><th>原作者</th><td>%s</td></tr>
<tr><th>底本类型</th><td>%s</td></tr>
<tr><th>成品级别</th><td>%s</td></tr>
<tr><th>权利风险</th><td>%s</td></tr>
<tr><th>推荐等级</th><td>%s</td></tr>
<tr><th>源码目录</th><td><code>08_source_code/%s/</code></td></tr>
<tr><th>元数据</th><td><code>03_translations_meta/%s/</code></td></tr>
</table>
<h2 class="sec">这部工程里有什么</h2>
<ul>
<li>语料：<code>01_corpus_zh/zh_paragraphs.jsonl</code> 中 <code>pkg=%s</code> 的 %s 段。</li>
<li>资料卡：见 <a href="../cards/index.html">卡片统一入口</a>（按系列/类型/状态筛选）。</li>
<li>工程文档：BRIEF / 编译说明 / 校对标准 / 术语表在 <code>08_source_code/%s/工程文件/</code>。</li>
</ul>
""" % (esc(p["id"]), esc(p["cn"]), "{:,}".format(p["paras"]), p["tex"], p["figs"], p["files"],
       esc(p["orig"]) or "（未登记，见元数据）", esc(p["author"]), esc(p["kind"]), esc(p["release"]),
       esc(p["risk"]), p["level"], esc(p["dir"]), esc(p["id"]), esc(p["id"]),
       "{:,}".format(p["paras"]), esc(p["dir"]))
        write_page(out, "p/%s.html" % p["id"], "%s %s" % (p["id"], p["cn"]), rel, depth=1, desc=(
            "%s %s 的中文译注工程页：底本、作者、%s 段语料、LaTeX 源码与资料卡入口。"
            % (p["cn"], p["orig"], fmtn(p["paras"]))))

    # ---------- 资料卡入口 ----------
    chunks = []
    for c in sorted(cards, key=lambda x: (x.get("_series", ""), x.get("type", ""), x.get("id", ""))):
        title = c.get("title") or c.get("id")
        summ = (c.get("summary") or c.get("definition") or "")[:220]
        kp = " · ".join(c.get("key_points") or [])[:220]
        chunks.append(
            '<details class="ccard" data-k="%s"><summary><span class="pill">%s</span> '
            '<span class="pill">%s</span> %s</summary>'
            '<div class="meta" style="color:var(--txt3);font-size:12px;margin:6px 0">%s</div>'
            '<div>%s</div>%s</details>'
            % (esc("%s %s %s %s" % (c.get("_series"), c.get("type"), c.get("status"), title)),
               esc(c.get("_series")), esc(STATUS_ZH.get(c.get("status", ""), c.get("status"))),
               fmt(title), esc(c.get("id")), fmt(summ),
               ('<div class="quote">%s</div>' % fmt(kp)) if kp else ""))
    cidx = """<h2 class="sec">资料卡 %d 张 · 统一入口</h2>
<p class="lead">按系列、类型、状态筛选；点开看摘要与要点。卡片是"概念—定义—要点—易错点—来源"的结构化笔记，
与语料段落互补：语料是逐段译文，卡片是可检索的论证单元。</p>
<input class="search" id="q" placeholder="搜索系列 / 类型 / 状态 / 标题…">
<div id="list">%s</div>
<script>const q=document.getElementById('q'),items=[...document.querySelectorAll('.ccard')];
q.oninput=()=>{const v=q.value.toLowerCase();items.forEach(r=>r.style.display=r.dataset.k.toLowerCase().includes(v)?'':'none')};</script>
""" % (len(cards), "".join(chunks))
    write_page(out, "cards/index.html", "资料卡", cidx, depth=1, desc=(
        "%s 张中文数学资料卡：定义、定理、证明思路与出处页码；可按系列、类型、状态筛选。" % fmtn(len(cards))))

    # ---------- 语料 ----------
    crow = "".join(
        '<div class="quote"><span class="k">%s · para %s · env=%s · tier=%s%s</span><br>%s</div>'
        % (esc(r.get("pkg")), esc(r.get("para_id", r.get("para"))), esc(r.get("env")), esc(r.get("tier")),
           (" · flags=" + ",".join(r.get("flags") or [])) if r.get("flags") else "",
           fmt(r.get("text") or ""))
        for r in corpus_samples(400))
    cpage = """<h2 class="sec">语料样例</h2>
<p class="lead">全库 <b>%s</b> 段（唯一 {n_uniq}），其中含公式 <b>%s</b> 段（86%%）；
正文字段 <code>text</code>，段落键 <code>para_id</code>，环境 <code>env</code>，评级 <code>tier</code>，
质检标记 <code>flags</code>。下面是均匀抽样 400 段（MathJax 在线渲染，离线时为原始 LaTeX）。</p>
%s
<p class="lead">全量：<code>01_corpus_zh/zh_paragraphs.jsonl</code>（{n_para} 行，字段表见 DATASHEET §3）。</p>
""" % ("{:,}".format(total_paras), "{:,}".format(formulas), crow)
    cpage = cpage.replace("{n_uniq}", fmtn(stnum("corpus.unique", total_paras)))
    write_page(out, "corpus.html", "语料", cpage, desc=(
        "段落级中文数学语料样例：%s 段，含公式、环境类型与质量 flags。" % fmtn(total_paras)))

    # ---------- 术语 ----------
    trows = "".join(
        '<tr class="trow" data-k="%s %s %s"><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
        % (esc(t.get("foreign")), esc(t.get("zh")), esc(t.get("pkg")),
           esc(t.get("foreign")), esc(t.get("lang")), esc(t.get("zh")),
           esc(t.get("status")), esc(t.get("pkg")))
        for t in terms)
    tpage = """<h2 class="sec">术语基 %s 条</h2>
<p class="lead">外文 / 中文 / 语种 / 状态 / 来源工程。<code>confirmed</code> 为已定稿，
<code>candidate</code>（%d 条）待裁决——裁决入口见 <code>01_corpus_zh/termbase.jsonl</code> 与
<code>04_playbook/</code> 的术语流程。</p>
<input class="search" id="q" placeholder="搜索外文 / 中文 / 工程编号…">
<table><tr><th>外文</th><th>语种</th><th>中文</th><th>状态</th><th>来源</th></tr><tbody id="tb">%s</tbody></table>
<script>const q=document.getElementById('q'),rows=[...document.querySelectorAll('.trow')];
q.oninput=()=>{const v=q.value.toLowerCase();rows.forEach(r=>r.style.display=r.dataset.k.toLowerCase().includes(v)?'':'none')};</script>
""" % ("{:,}".format(len(terms)), sum(1 for t in terms if t.get("status") == "candidate"), trows)
    write_page(out, "terms.html", "术语基", tpage, desc=(
        "中英日数学术语基 %s 条：外文、中文、语种、状态与来源工程。" % fmtn(len(terms))))

    # ---------- 许可 ----------
    comp = """<h2 class="sec">许可与合规口径</h2>
<p class="lead">分三层，别混：<b>自产层</b>（元数据、术语、方法、脚本、文档）→ CC BY 4.0；
<b>译文层</b>（译文、译注、语料、译文源码）→ 第三方底本的演绎作品，<b>本库不代原作者授权，也不另设限制</b>；
<b>原文本体</b>（底本 PDF、扫描件、页面图）→ 不入库、不发布。</p>
<table>
<tr><th>层</th><th>内容</th><th>许可</th><th>可否训练</th></tr>
<tr><td>自产层</td><td>元数据、术语表、工程文档、流水线脚本</td><td>CC BY 4.0</td><td>可以</td></tr>
<tr><td>译文层</td><td>译文、译注、语料正文、LaTeX 源码</td><td>不代原作者授权、不另设限制、48 小时可撤</td><td><b>可以</b>（检索、研究、教学、训练、蒸馏）</td></tr>
<tr><td>原文本体</td><td>底本 PDF、扫描件、页面图、OCR 全文</td><td>不发布</td><td>不适用（本库没有）</td></tr>
</table>
<h2 class="sec">五条红线</h2>
<ul>
<li>不发布原文 PDF / 扫描件 / 页面图 / OCR 全文（R1–R3）。</li>
<li>译文本体<b>不得</b>标 CC BY 4.0——本库无权替原作者授权；也<b>不得</b>写"仅限非商业""不得用于训练"这类本库无权施加的限制（R4）。</li>
<li>每条译注可追溯到 A/B/I 级来源；黑名单来源不看不引（R6–R7）。</li>
<li>授权表述必须有凭证，不得写"已获授权"（R9）。</li>
<li>权利人通知 → 48 小时内撤下对应内容（R10）。</li>
</ul>
<p class="lead">完整条款：仓内 <a href="../LICENSE">LICENSE</a>、<a href="../COMPLIANCE.md">COMPLIANCE.md</a>、
<a href="compliance.html">DATASHEET.md</a>；机器检查：<code>python tools/check_compliance.py</code>。</p>
"""
    write_page(out, "compliance.html", "许可与合规", comp, desc=(
        "数译的三层许可口径、五条红线与可训练范围（自产层 CC BY 4.0；译文层不代原作者授权）。"))

    # ---------- 爬虫/大模型发现层：robots、sitemap、llms.txt ----------
    pages_found = []
    for dirpath, _dirs, fnames in os.walk(out):
        for fn in fnames:
            if fn.endswith(".html"):
                rel = os.path.relpath(os.path.join(dirpath, fn), out).replace(os.sep, "/")
                pages_found.append(rel)
    pages_found.sort()
    robots = """# 数译 Shuyi — 中文数学译注语料库
# 检索、研究、教学与训练均可；原文 PDF/扫描件不入库。
User-agent: *
Allow: /

# 主要大模型/搜索爬虫：明确允许（不设抓取限制）
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-Web
Allow: /
User-agent: anthropic-ai
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Googlebot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: CCBot
Allow: /
User-agent: Bytespider
Allow: /
User-agent: Amazonbot
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: meta-externalagent
Allow: /
User-agent: cohere-ai
Allow: /
User-agent: YouBot
Allow: /
User-agent: Diffbot
Allow: /

# 机器可读入口
# llms.txt: %s/llms.txt
Sitemap: %s/sitemap.xml
""" % (SITE_BASE, SITE_BASE)
    io.open(os.path.join(out, "robots.txt"), "w", encoding="utf-8", newline="\n").write(robots)

    today = time.strftime("%Y-%m-%d")
    urls = "".join(
        '<url><loc>%s/%s</loc><lastmod>%s</lastmod><changefreq>weekly</changefreq>'
        '<priority>%s</priority></url>\n'
        % (SITE_BASE, pth, today, "1.0" if pth in ("index.html", "cards/index.html", "corpus.html", "terms.html") else "0.7")
        for pth in pages_found)
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    io.open(os.path.join(out, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write(sitemap)

    n_card = len(cards)
    n_term = len(terms)
    llms = """# 数译 Shuyi

> 数译（Shuyi）是面向中文数学的开源语料库：%d 部数学讲义与专著的中文译注工程、
> %s 段段落级中文语料、%s 条中英日术语、%s 张资料卡，以及自然语言与 Lean 4 的对齐卡。
> 自产层（元数据、术语、方法、脚本、文档）为 CC BY 4.0；译文层是第三方底本的演绎作品，
> 本库不代原作者授权、也不另设限制（检索、研究、教学、训练、蒸馏均可）。原文 PDF/扫描件不入库。

## 站点（可直接读，无需克隆）
- [总览](%s/index.html): 规模、主线、语料与卡片样例、三条使用路径
- [工程总表](%s/p/index.html): 全部译注工程（底本、作者、源码、段落数、许可分级）
- [资料卡](%s/cards/index.html): 定义/定理/校正/例子/陈述/注记，按系列与类型筛选
- [语料样例](%s/corpus.html): 段落级中文语料（带公式与环境类型）
- [术语基](%s/terms.html): 外文 / 中文 / 语种 / 状态 / 来源工程
- [许可与合规](%s/compliance.html): 三层许可、五条红线、可训练范围

## 数据（仓库内 JSONL / JSON）
- [zh_paragraphs.jsonl](https://github.com/lzxsusy/mathtranslate/raw/master/01_corpus_zh/zh_paragraphs.jsonl): 段落级中文语料，字段见 DATASHEET.md
- [termbase.jsonl](https://github.com/lzxsusy/mathtranslate/raw/master/01_corpus_zh/termbase.jsonl): 术语基（含 candidate/confirmed）
- [datasets/](https://github.com/lzxsusy/mathtranslate/tree/master/datasets): 资料卡与 Lean 对齐卡（每张卡一个 JSON）
- [site/catalog.json](%s/catalog.json): 全部工程的机器可读目录
- [站内全文入口](%s/llms-full.txt): 规模统计、schema 与引用方式

## 引用
- 仓库：https://github.com/lzxsusy/mathtranslate （Gitee/AtomGit 有镜像）
- 引用元数据：CITATION.cff；数据集 DOI：见 .zenodo.json（归档后回填）
""" % (len(projs), fmtn(total_paras), fmtn(n_term), fmtn(n_card),
       SITE_BASE, SITE_BASE, SITE_BASE, SITE_BASE, SITE_BASE, SITE_BASE, SITE_BASE, SITE_BASE)
    io.open(os.path.join(out, "llms.txt"), "w", encoding="utf-8", newline="\n").write(llms)

    llms_full = """# 数译 Shuyi — llms-full

## 规模（快照 %s）
- 译注工程：%d（%d 部带 LaTeX 源码）
- 中文语料：%s 段（含公式 %s 段）
- 术语：%s 条（candidate 待裁决 %s 条）
- 资料卡：%s 张（concept/derivation/correction/example/statement/remark）
- 仓库跟踪文件：%s

## 数据 schema
- zh_paragraphs.jsonl：字段 pkg, para_id, env, tier, flags, text（去 LaTeX 命令、保留行内公式）；按 para_id 去重，按 flags 过滤 orphan_number/empty_ref。
- termbase.jsonl：字段 source_term, lang, zh, status(confirmed|candidate), pkg, note。
- datasets/<set>/cards/**/*.json：字段 id,type,track,title,aliases,summary,question,definition{text,notation},key_points,formulas,theorems{name,statement,proof{status,steps,gap_note},source},pitfalls,related,sources{book,section,pages,pdf_pages,anchor},rights,status。
- leanstmt：中文陈述 ↔ Lean 4 对齐卡；lean/ 下有 lakefile.lean 与 lean-toolchain，`lake build` 可复现。

## 许可
- 自产层 CC BY 4.0；译文层：演绎作品，不代原作者授权、不另设限制；48 小时撤下机制。
- 原文 PDF/扫描件/OCR 全文不入库。

## 引用
- CITATION.cff；仓库 https://github.com/lzxsusy/mathtranslate
""" % (today, len(projs), n_src, fmtn(total_paras), fmtn(formulas), fmtn(n_term),
       fmtn(sum(1 for t in terms if t.get("status") == "candidate")), fmtn(n_card),
       fmtn(total_files))
    io.open(os.path.join(out, "llms-full.txt"), "w", encoding="utf-8", newline="\n").write(llms_full)

    print("built: %d projects, %d cards, %d terms, %s files -> %s"
          % (len(projs), len(cards), len(terms), "{:,}".format(total_files), out))


if __name__ == "__main__":
    build()
