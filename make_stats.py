# -*- coding: utf-8 -*-
r"""生成全仓统计：README 的统计块 + `_meta/stats.json`（唯一事实源）。

用法：
    python make_stats.py            # 打印统计块（不改文件）
    python make_stats.py --write    # 写回 README.md 的 STATS 块，并写 _meta/stats.json
    python make_stats.py --check    # 校验 README 的统计块是否与实测一致（CI 用，不一致 exit 1）
    python make_stats.py --json     # 只打印 stats.json（管道给别的脚本用）

口径约定：所有数字都从**工作区的 git 索引与语料文件**实测，禁止手写。
其它 Markdown 里的数字若与 stats.json 冲突，由 `tools/check_numbers.py` 拦截。
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys
from collections import Counter, OrderedDict

sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.dirname(os.path.abspath(__file__))
BEGIN = "<!-- STATS:BEGIN -->"
END = "<!-- STATS:END -->"
STATS_JSON = os.path.join(REPO, "_meta", "stats.json")

THEMES = OrderedDict([
    ("SY01", "镜像对称与同调镜像对称"),
    ("SY02", "几何朗兰兹与电磁对偶"),
    ("SY03", "量子场论与规范理论"),
    ("SY04", "弦论与紧致化"),
    ("SY05", "辛几何·拓扑·纽结·指标定理"),
    ("SY07", "其他几何（热带/范畴/量子力学与几何）"),
    ("SY08", "双有理几何"),
    ("SY99", "拓扑学与专题"),
])


def mb(n):
    return "%.1f MB" % (n / 1048576.0)


def git(*args):
    try:
        return subprocess.run(["git", "-C", REPO] + list(args),
                              capture_output=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return b""


def tracked_files():
    out = git("ls-files", "-z")
    return [p for p in out.decode("utf-8", "replace").split("\0") if p]


def count_tree(path):
    n = b = 0
    for dp, dn, fn in os.walk(path):
        if ".git" in dp.split(os.sep):
            continue
        for f in fn:
            try:
                b += os.path.getsize(os.path.join(dp, f))
            except OSError:
                continue
            n += 1
    return n, b


def project_stats(files):
    """按 08_source_code 的工程目录统计：部数、带源码、缺工程文件、空源码。"""
    tset = [p for p in files if p.startswith("08_source_code/") and p.count("/") >= 2]
    projs = sorted({p.split("/")[1] for p in tset})
    per = {d: {"tex": 0, "figures": 0, "gongcheng": 0, "src_files": 0} for d in projs}
    for p in tset:
        parts = p.split("/")
        d = parts[1]
        low = p.lower()
        if low.endswith(".tex"):
            per[d]["tex"] += 1
        elif low.endswith((".png", ".jpg", ".jpeg", ".pdf")) and "figures" in low:
            per[d]["figures"] += 1
        if len(parts) > 2 and parts[2] == "工程文件":
            per[d]["gongcheng"] += 1
        if len(parts) > 2 and parts[2] == "源码":
            per[d]["src_files"] += 1
    tex = sum(v["tex"] for v in per.values())
    figs = sum(v["figures"] for v in per.values())
    with_tex = [d for d, v in per.items() if v["tex"] > 0]
    no_tex = [d for d, v in per.items() if v["tex"] == 0]
    no_gc = [d for d, v in per.items() if v["gongcheng"] == 0]
    empty_src = [d for d, v in per.items() if v["src_files"] == 0
                 and os.path.isdir(os.path.join(REPO, "08_source_code", d, "源码"))]
    themes = OrderedDict()
    for code, name in THEMES.items():
        ds = [d for d in projs if d.startswith(code + "-")]
        themes[code] = {
            "name": name,
            "projects": len(ds),
            "with_tex": len([d for d in ds if per[d]["tex"] > 0]),
        }
    return {
        "total": len(projs),
        "with_tex": len(with_tex),
        "tex_files": tex,
        "figures": figs,
        "without_tex": sorted(no_tex),
        "without_gongcheng": sorted(no_gc),
        "empty_src": sorted(empty_src),
        "by_theme": themes,
    }


def source_stats():
    """底本类型分布，只认 RELEASE_REGISTER.csv（逐部台账）。"""
    p = os.path.join(REPO, "RELEASE_REGISTER.csv")
    if not os.path.isfile(p):
        return {"rows": 0, "by_type": {}}
    with io.open(p, encoding="utf-8-sig") as f:
        head = f.readline().rstrip("\n").split(",")
        i_type = head.index("底本类型")
        c = Counter()
        rows = 0
        for line in f:
            cells = line.rstrip("\n").split(",")
            if len(cells) <= i_type:
                continue
            rows += 1
            c[cells[i_type].strip()] += 1
    return {"rows": rows, "by_type": OrderedDict(c.most_common())}


def pdf_stats():
    """成品 PDF：只数有公网直链（http）的行；页数同样只数这些行。"""
    p = os.path.join(REPO, "03_translations_meta", "_PDF清单.tsv")
    rows = nbytes = pages = 0
    if os.path.isfile(p):
        with io.open(p, encoding="utf-8-sig") as f:
            head = f.readline().rstrip("\n").split("\t")
            i_file = head.index("成品文件")
            i_bytes = head.index("成品字节")
            i_pages = head.index("成品页数")
            i_link = next((i for i, h in enumerate(head) if h.startswith("成品直链")), None)
            for line in f:
                cells = line.rstrip("\n").split("\t")
                if len(cells) <= max(i_file, i_bytes):
                    continue
                ok = i_link is not None and len(cells) > i_link and cells[i_link].strip().startswith("http")
                if cells[i_file].strip() and ok:
                    rows += 1
                    nbytes += int(cells[i_bytes] or 0)
                    pages += int((cells[i_pages] if len(cells) > i_pages else "") or 0)
    return {"rows": rows, "bytes": nbytes, "pages": pages}


def corpus_stats():
    p = os.path.join(REPO, "01_corpus_zh", "zh_paragraphs.jsonl")
    paras = uniq = with_math = near = zhsum = page = 0
    pkgs = set()
    page_pkgs = Counter()
    if os.path.isfile(p):
        seen = set()
        for line in io.open(p, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            paras += 1
            pkgs.add(d.get("pkg"))
            t = d.get("text", "")
            if "$" in t or "\\begin{" in t:
                with_math += 1
            if d.get("near_dup_of"):
                near += 1
            zhsum += int(d.get("zh_chars") or 0)
            if d.get("page_orig"):
                page += 1
                page_pkgs[d.get("pkg")] += 1
            h = d.get("para_id")
            if h not in seen:
                seen.add(h)
                uniq += 1
    return {
        "paragraphs": paras,
        "unique": uniq,
        "with_math": with_math,
        "math_pct": round(100.0 * with_math / max(1, paras)),
        "zh_chars": zhsum,
        "packages": len(pkgs),
        "near_dup": near,
        "page_orig": page,
        "page_orig_top": page_pkgs.most_common(3),
    }


def termbase_stats():
    p = os.path.join(REPO, "01_corpus_zh", "termbase.jsonl")
    st, lang = Counter(), Counter()
    total = 0
    if os.path.isfile(p):
        for line in io.open(p, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            total += 1
            st[d.get("status") or "?"] += 1
            lang[d.get("lang") or "?"] += 1
    return {"total": total,
            "by_status": OrderedDict(st.most_common()),
            "by_lang": OrderedDict(lang.most_common())}


def dataset_stats():
    """资料卡：datasets/<集>/cards 下每个 JSON 一张卡；对齐语料单独记。"""
    root = os.path.join(REPO, "datasets")
    per = Counter()
    status = Counter()
    if os.path.isdir(root):
        for ds in sorted(os.listdir(root)):
            cdir = os.path.join(root, ds, "cards")
            if not os.path.isdir(cdir):
                continue
            for dp, dn, fn in os.walk(cdir):
                for f in fn:
                    if not f.endswith(".json"):
                        continue
                    per[ds] += 1
                    try:
                        with io.open(os.path.join(dp, f), encoding="utf-8") as fh:
                            status[json.load(fh).get("status") or "?"] += 1
                    except (ValueError, OSError):
                        status["unreadable"] += 1
    lean = {"cards": 0, "certified": 0, "gap": 0, "lean_files": 0, "sorry": 0}
    ldir = os.path.join(root, "leanstmt")
    if os.path.isdir(ldir):
        for dp, dn, fn in os.walk(os.path.join(ldir, "cards")):
            for f in fn:
                if not f.endswith(".json"):
                    continue
                lean["cards"] += 1
                with io.open(os.path.join(dp, f), encoding="utf-8") as fh:
                    v = (json.load(fh).get("verification") or {}).get("status")
                if v == "certified":
                    lean["certified"] += 1
                elif v in ("gap", "sketch"):
                    lean["gap"] += 1
        for dp, dn, fn in os.walk(os.path.join(ldir, "lean")):
            for f in fn:
                if f.endswith(".lean"):
                    lean["lean_files"] += 1
                    txt = io.open(os.path.join(dp, f), encoding="utf-8").read()
                    lean["sorry"] += len(re.findall(r"(?<![\w'])sorry(?![\w'])", txt))
    return {
        "cards_total": sum(per.values()),
        "by_dataset": OrderedDict(sorted(per.items(), key=lambda kv: -kv[1])),
        "by_status": OrderedDict(status.most_common()),
        "leanstmt": lean,
    }


def misc_stats():
    tj = os.path.join(REPO, "02_trajectories", "traj_selected.jsonl")
    traj = sum(1 for _ in io.open(tj, encoding="utf-8")) if os.path.isfile(tj) else 0
    att = os.path.join(REPO, "06_sessions_raw", "_attachments.json")
    shards = 0
    sbytes = 0
    if os.path.isfile(att):
        am = json.load(io.open(att, encoding="utf-8"))
        shards = sum(len(p.get("parts", [])) for p in am.get("packages", []))
        sbytes = int(am.get("total_bytes") or 0)
    return {"trajectories": traj,
            "session_shards": shards,
            "session_bytes": sbytes}


def compute():
    files = tracked_files()
    if files:
        n = len(files)
        b = 0
        for rel in files:
            try:
                b += os.path.getsize(os.path.join(REPO, rel))
            except OSError:
                continue
    else:  # 没有 git 时退回工作区
        n, b = count_tree(REPO)
    stats = OrderedDict()
    stats["generated_at"] = __import__("datetime").datetime.now().astimezone().isoformat(timespec="seconds")
    stats["repo"] = {"tracked_files": n, "tracked_bytes": b}
    stats["projects"] = project_stats(files)
    stats["sources"] = source_stats()
    stats["pdf"] = pdf_stats()
    stats["corpus"] = corpus_stats()
    stats["termbase"] = termbase_stats()
    stats["datasets"] = dataset_stats()
    stats.update(misc_stats())
    return stats


def render_block(s):
    p = s["projects"]
    c = s["corpus"]
    return "\n".join([
        BEGIN,
        "",
        "| 指标 | 数值 |",
        "|---|---|",
        "| 译注工程 | **%d** 部（其中 **%d** 部带完整 LaTeX 源码） |" % (p["total"], p["with_tex"]),
        "| 仓库文件（git 跟踪） | %s 个 / **%s** |" % ("{:,}".format(s["repo"]["tracked_files"]), mb(s["repo"]["tracked_bytes"])),
        "| LaTeX 源文件 / 插图 | %s 个 `.tex` / %s 张图 |" % ("{:,}".format(p["tex_files"]), "{:,}".format(p["figures"])),
        "| 成品 PDF（预印本类） | %s 部 / **%s**（Release 附件） |" % ("{:,}".format(s["pdf"]["rows"]), mb(s["pdf"]["bytes"])),
        "| 中文段落语料 | **%s** 段（唯一 %s），其中 **%s** 段含公式（%d%%）；汉字 %s 字 |"
        % ("{:,}".format(c["paragraphs"]), "{:,}".format(c["unique"]), "{:,}".format(c["with_math"]),
           c["math_pct"], format(c["zh_chars"], ",")),
        "| 语料覆盖 | **%d** 个工程有段落入库 |" % c["packages"],
        "| 近重复标注 | %s 段（保留，标 `near_dup_of`） |" % "{:,}".format(c["near_dup"]),
        "| 原书页码锚点 | %s 段（`page_orig`） |" % "{:,}".format(c["page_orig"]),
        "| 术语基 | %s 条 |" % "{:,}".format(s["termbase"]["total"]),
        "| 资料卡 | %s 张（%d 个数据集） |" % ("{:,}".format(s["datasets"]["cards_total"]), len(s["datasets"]["by_dataset"])),
        "| 形式化陈述对齐 | %d 条（%d certified + %d gap；%d 个 `.lean`，%d 处 sorry） |"
        % (s["datasets"]["leanstmt"]["cards"], s["datasets"]["leanstmt"]["certified"],
           s["datasets"]["leanstmt"]["gap"], s["datasets"]["leanstmt"]["lean_files"],
           s["datasets"]["leanstmt"]["sorry"]),
        "| 精选轨迹 | %s 条 |" % "{:,}".format(s["trajectories"]),
        "| 原始会话分片 | %d 片 / **%s**（Release 附件） |" % (s["session_shards"], mb(s["session_bytes"])),
        "",
        "> 口径：本表由 `python make_stats.py` 从仓库文件与语料实测生成，同一份数据写入 "
        "[`_meta/stats.json`](_meta/stats.json)（机器可读，供其它文档与站点取数），是唯一事实源；"
        "请勿手写或从他处抄数。定义见 [`_meta/口径.md`](_meta/口径.md)。",
        END,
    ])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="写回 README 并写 _meta/stats.json")
    ap.add_argument("--check", action="store_true", help="校验 README 统计块是否与实测一致")
    ap.add_argument("--json", action="store_true", help="只打印 stats.json")
    a = ap.parse_args()

    s = compute()
    block = render_block(s)
    if a.json:
        print(json.dumps(s, ensure_ascii=False, indent=2))
        return
    print(block)

    if a.write:
        os.makedirs(os.path.dirname(STATS_JSON), exist_ok=True)
        with io.open(STATS_JSON, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(s, ensure_ascii=False, indent=2) + "\n")
        p = os.path.join(REPO, "README.md")
        src = io.open(p, encoding="utf-8").read()
        src2 = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda m: block, src, flags=re.S)
        with io.open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(src2)
        print("\n[written] README.md STATS 块 + _meta/stats.json")

    if a.check:
        p = os.path.join(REPO, "README.md")
        src = io.open(p, encoding="utf-8").read()
        m = re.search(re.escape(BEGIN) + r"(.*?)" + re.escape(END), src, flags=re.S)
        cur = (BEGIN + m.group(1) + END) if m else None
        if cur is None:
            print("[FAIL] README.md 缺少 STATS 块")
            sys.exit(1)
        norm = lambda t: [ln.rstrip() for ln in t.strip().splitlines()]
        if norm(cur) != norm(block):
            print("[FAIL] README.md 的统计块与实测不一致，请跑 python make_stats.py --write")
            sys.exit(1)
        print("[OK] README.md 统计块与实测一致")


if __name__ == "__main__":
    main()
