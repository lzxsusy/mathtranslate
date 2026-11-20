# -*- coding: utf-8 -*-
r"""把仓库里的条目渲染成静态站点 `site/`——不克隆也能看。

用法：
    python tools/build_site.py            # 生成到 site/
    python tools/build_site.py --out site

产物：
    site/index.html        落地页：规模、主线、样例语料、样例卡片、术语抽样
    site/p/index.html      106 部工程总表（可搜索）
    site/p/<id>.html       单部工程详情（底本、作者、台账、语料段数、入口）
    site/cards/index.html  900 张资料卡统一入口（按系列/类型/状态筛选）
    site/corpus.html       语料样例（按包/环境抽样，带 flags）
    site/terms.html        术语基全表（1,820 条，可搜索）
    site/compliance.html   许可与合规口径（LIKE LICENSE §0–§1）
    site/catalog.json      机器可读目录（106 条）
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
    every = max(1, 49035 // n)
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


def page(title, body, depth=0, extra_head=""):
    up = "../" * depth
    nav = NAV.replace('href="', 'href="%s' % up).replace('%s%s' % (up, up), up)
    return """<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t} · 数译 mathtranslate</title>
<link rel="stylesheet" href="{up}assets/style.css">{eh}</head><body>
<div class="wrap"><header class="top"><div class="brand">
<div class="logo">数</div><div><h1>数译 · 中文数学译注文献库</h1>
<div class="sub">mathtranslate · 106 部译注工程 · 49,035 段中文语料 · 900 张资料卡</div></div>{nav}</div></header>
{body}
<footer>许可：自产层 CC BY 4.0；译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制
（检索、研究、教学、训练均可），权利人通知即撤 · 见 <a href="{up}compliance.html">许可与合规</a> 与仓内 LICENSE</footer>
</div></body></html>""".format(t=esc(title), body=body, up=up, nav=nav, mj=MATHJAX, eh=extra_head)


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
    total_files = len(tracked())

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
<div class="stat"><b>%d</b><span>个仓库文件</span></div>
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
<li><b>想拿语料训练</b>：<code>01_corpus_zh/zh_paragraphs.jsonl</code>（49,035 段，字段见
<a href="compliance.html">DATASHEET.md</a>）；训练前建议按 <code>flags</code> 过滤
<code>orphan_number / empty_ref</code>，按 <code>para_id</code> 去重。</li>
<li><b>想接管术语</b>：<code>01_corpus_zh/termbase.jsonl</code>（1,820 条，1,411 条 candidate 待裁决）。</li>
</ul></div>
""" % (len(projs), n_src, "{:,}".format(total_paras), "{:,}".format(formulas), len(cards),
       "{:,}".format(len(terms)), total_files, "".join(theme_cards), len(cards), "".join(card_html),
       "{:,}".format(total_paras), para_html, "{:,}".format(len(terms)), term_html)
    io.open(os.path.join(out, "index.html"), "w", encoding="utf-8", newline="\n").write(page("总览", body))

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
    io.open(os.path.join(out, "p", "index.html"), "w", encoding="utf-8", newline="\n").write(
        page("工程总表", pidx, depth=1))

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
        io.open(os.path.join(out, "p", p["id"] + ".html"), "w", encoding="utf-8", newline="\n").write(
            page("%s %s" % (p["id"], p["cn"]), rel, depth=1))

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
    io.open(os.path.join(out, "cards", "index.html"), "w", encoding="utf-8", newline="\n").write(
        page("资料卡", cidx, depth=1))

    # ---------- 语料 ----------
    crow = "".join(
        '<div class="quote"><span class="k">%s · para %s · env=%s · tier=%s%s</span><br>%s</div>'
        % (esc(r.get("pkg")), esc(r.get("para_id", r.get("para"))), esc(r.get("env")), esc(r.get("tier")),
           (" · flags=" + ",".join(r.get("flags") or [])) if r.get("flags") else "",
           fmt(r.get("text") or ""))
        for r in corpus_samples(400))
    cpage = """<h2 class="sec">语料样例</h2>
<p class="lead">全库 <b>%s</b> 段（唯一 47,469），其中含公式 <b>%s</b> 段（86%%）；
正文字段 <code>text</code>，段落键 <code>para_id</code>，环境 <code>env</code>，评级 <code>tier</code>，
质检标记 <code>flags</code>。下面是均匀抽样 400 段（MathJax 在线渲染，离线时为原始 LaTeX）。</p>
%s
<p class="lead">全量：<code>01_corpus_zh/zh_paragraphs.jsonl</code>（49,035 行，字段表见 DATASHEET §3）。</p>
""" % ("{:,}".format(total_paras), "{:,}".format(formulas), crow)
    io.open(os.path.join(out, "corpus.html"), "w", encoding="utf-8", newline="\n").write(page("语料", cpage))

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
    io.open(os.path.join(out, "terms.html"), "w", encoding="utf-8", newline="\n").write(page("术语基", tpage))

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
    io.open(os.path.join(out, "compliance.html"), "w", encoding="utf-8", newline="\n").write(
        page("许可与合规", comp))

    print("built: %d projects, %d cards, %d terms, %d files -> %s"
          % (len(projs), len(cards), len(terms), total_files, out))


if __name__ == "__main__":
    build()
