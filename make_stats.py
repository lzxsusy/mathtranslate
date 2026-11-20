# -*- coding: utf-8 -*-
r"""生成 README 里的统计块（单一事实源，避免手写数字漂移）。

用法：python make_stats.py            # 只打印
      python make_stats.py --write    # 写回 README.md 的 <!-- STATS:BEGIN/END --> 之间
"""
import argparse
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.dirname(os.path.abspath(__file__))
BEGIN = "<!-- STATS:BEGIN -->"
END = "<!-- STATS:END -->"


def mb(n):
    return "%.1f MB" % (n / 1048576.0)


def count_tree(path):
    n = b = 0
    for dp, dn, fn in os.walk(path):
        if ".git" in dp.split(os.sep):
            continue
        for f in fn:
            fp = os.path.join(dp, f)
            try:
                b += os.path.getsize(fp)
            except OSError:
                continue
            n += 1
    return n, b


def count_tracked(path):
    """只数 git 跟踪的文件——这才是别人 clone 下来真正拿到的东西。

    以前用 os.walk 数工作区，会把 .gitignore 掉的缓存/本地 PDF 也算进去，
    于是同一个仓库在不同机器上给出不同数字（口径漂移的根源之一）。
    """
    import subprocess

    try:
        out = subprocess.run(
            ["git", "-C", path, "ls-files", "-z"],
            capture_output=True, check=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return count_tree(path)
    n = b = 0
    for rel in out.split(b"\0"):
        if not rel:
            continue
        fp = os.path.join(path, rel.decode("utf-8", "replace"))
        try:
            b += os.path.getsize(fp)
        except OSError:
            continue
        n += 1
    return n, b


def main():
    write = "--write" in sys.argv
    d08 = os.path.join(REPO, "08_source_code")
    d03 = os.path.join(REPO, "03_translations_meta")
    # 只统计仓库里真的入库的工程（git 跟踪），本机草稿目录不算数
    import subprocess
    try:
        tracked = subprocess.run(["git", "-C", REPO, "ls-files", "08_source_code"],
                                 capture_output=True, check=True).stdout.decode("utf-8", "replace")
    except Exception:
        tracked = ""
    tset = [ln for ln in tracked.splitlines() if ln.count("/") >= 2]
    projs = sorted({ln.split("/")[1] for ln in tset}) if tset else \
        ([d for d in os.listdir(d08) if os.path.isdir(os.path.join(d08, d))] if os.path.isdir(d08) else [])
    tex = img = 0
    with_src = 0
    for d in projs:
        t = 0
        for ln in tset:
            if ln.split("/")[1] != d:
                continue
            lf = ln.lower()
            if lf.endswith(".tex"):
                tex += 1
                t += 1
            elif lf.endswith((".png", ".jpg", ".jpeg", ".pdf")) and "figures" in os.path.dirname(lf):
                img += 1
        if t:
            with_src += 1

    # 成品 PDF（2026-11-14 起在 Release 附件，字节数从 _PDF清单.tsv 读取）
    # 2026-11-16 起仓库内不留成品 PDF：只统计有 Release 外链的行。
    pdf_rows = 0
    pdf_bytes = 0
    tsv = os.path.join(d03, "_PDF清单.tsv")
    if os.path.isfile(tsv):
        with io.open(tsv, encoding="utf-8-sig") as f:
            head = f.readline().rstrip("\n").split("\t")
            i_file, i_bytes = head.index("成品文件"), head.index("成品字节")
            i_link = next((i for i, h in enumerate(head) if h.startswith("成品直链")), None)
            for line in f:
                cells = line.rstrip("\n").split("\t")
                if len(cells) <= max(i_file, i_bytes):
                    continue
                link_ok = i_link is not None and len(cells) > i_link and cells[i_link].strip().startswith("http")
                if cells[i_file].strip() and link_ok:
                    pdf_rows += 1
                    pdf_bytes += int(cells[i_bytes] or 0)

    # 语料
    zp = os.path.join(REPO, "01_corpus_zh", "zh_paragraphs.jsonl")
    paras = uniq = with_math = near = zhsum = 0
    pkgs = set()
    if os.path.isfile(zp):
        seen = set()
        for line in io.open(zp, encoding="utf-8"):
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
            h = d.get("para_id")
            if h not in seen:
                seen.add(h)
                uniq += 1
    tb = os.path.join(REPO, "01_corpus_zh", "termbase.jsonl")
    terms = sum(1 for _ in io.open(tb, encoding="utf-8")) if os.path.isfile(tb) else 0

    # 轨迹
    tj = os.path.join(REPO, "02_trajectories", "traj_selected.jsonl")
    traj = sum(1 for _ in io.open(tj, encoding="utf-8")) if os.path.isfile(tj) else 0

    # 会话分片（2026-11-14 起在 Release 附件，元数据见 _attachments.json）
    att = os.path.join(REPO, "06_sessions_raw", "_attachments.json")
    shards_n = 0
    sbytes = 0
    if os.path.isfile(att):
        am = json.load(io.open(att, encoding="utf-8"))
        shards_n = sum(len(p.get("parts", [])) for p in am.get("packages", []))
        sbytes = int(am.get("total_bytes") or 0)

    nfiles, nbytes = count_tracked(REPO)

    lines = [
        BEGIN,
        "",
        "| 指标 | 数值 |",
        "|---|---|",
        "| 译注工程 | **%d** 部（其中 **%d** 部带完整 LaTeX 源码） |" % (len(projs), with_src),
        "| 仓库文件（git 跟踪） | %s 个 / **%s** |" % ("{:,}".format(nfiles), mb(nbytes)),
        "| LaTeX 源文件 / 插图 | %s 个 `.tex` / %s 张图 |" % ("{:,}".format(tex), "{:,}".format(img)),
        "| 成品 PDF（预印本类） | %s 部 / **%s**（Release 附件） |" % ("{:,}".format(pdf_rows), mb(pdf_bytes)),
        "| 中文段落语料 | **%s** 段（唯一 %s），其中 **%s** 段含公式（%.0f%%）；汉字 %s 字 |"
        % ("{:,}".format(paras), "{:,}".format(uniq), "{:,}".format(with_math),
           100.0 * with_math / max(1, paras), format(zhsum, ",")),
        "| 语料覆盖 | **%d** 个工程有段落入库（其余为仅成品 PDF / 无正文的工程） |" % len(pkgs),
        "| 近重复标注 | %s 段（保留，标 `near_dup_of`） |" % "{:,}".format(near),
        "| 术语基 | %s 条 |" % "{:,}".format(terms),
        "| 精选轨迹 | %s 条 |" % "{:,}".format(traj),
        "| 原始会话分片 | %d 片 / **%s**（Release 附件） |" % (shards_n, mb(sbytes)),
        "",
        "> 口径：本表由 `python make_stats.py` 从仓库文件与语料实测生成，是唯一事实源；请勿手写或从他处抄数。",
        END,
    ]
    block = "\n".join(lines)
    print(block)
    if write:
        p = os.path.join(REPO, "README.md")
        s = io.open(p, encoding="utf-8").read()
        s2 = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda m: block, s, flags=re.S)
        io.open(p, "w", encoding="utf-8", newline="\n").write(s2)
        print("\n[written to README.md]")


if __name__ == "__main__":
    main()
