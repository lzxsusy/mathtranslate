#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""单块编译自检（EN49）。

用法（任意目录）：
  python src/tools/compile_chunk.py c01

在 src/ 下生成 _wrap_cNN.tex（导言区 + section/subsection 计数器设定 + 本块），
用 -output-directory 把编译产物放到 work/tmp_cNN/，跑两遍 xelatex，输出
work/tmp_cNN/_wrap_cNN.pdf（同时复制为 wrap.pdf），并统计 errors / overfull /
underfull / undefined / missing character，打印首个错误与 overfull 行。
"""
import os, re, subprocess, sys, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, ".."))          # src/
ROOT = os.path.abspath(os.path.join(SRC, ".."))          # 工程根

# (编译前 section 计数, 编译前 subsection 计数, 原书页范围说明)
# 规则：块首行若是 \section，则 section 取「目标章号 − 1」；若是 \subsection，
# section 取所在章号、subsection 取「目标小节号 − 1」。c11 用 \section*，计数无关。
CHUNKS = {
    "c00": ("-1", "0", "i–ix"),
    "c01": ("0", "0", "1–11"),
    "c02": ("1", "3", "12–21"),
    "c03": ("1", "5", "22–28"),
    "c04": ("1", "0", "29–47"),
    "c05": ("2", "0", "48–57"),
    "c06": ("3", "0", "58–64"),
    "c07": ("4", "1", "65–75"),
    "c08": ("4", "0", "76–86"),
    "c09": ("5", "0", "87–97"),
    "c10": ("6", "0", "98–111"),
    "c11": ("7", "0", "112–127"),
    "c12": ("8", "0", "128–134"),
    "c13": ("9", "0", "135–145"),
}


def wrap(cid):
    sec, subsec, _ = CHUNKS[cid]
    head = ("\\input{preamble}\n\\input{chunks/_envs}\n\\begin{document}\n"
            "\\setcounter{section}{%s}\n\\setcounter{subsection}{%s}\n" % (sec, subsec))
    body = "\\input{chunks/%s}\n\\end{document}\n" % cid
    return head + body


def all_labels(except_cid):
    """收集其他块（以及本块）里定义过的 \\label，用于判定未解析引用是否只是跨块引用。"""
    seen = {}
    cdir = os.path.join(SRC, "chunks")
    for fn in sorted(os.listdir(cdir)):
        if not fn.endswith(".tex"):
            continue
        cid = fn[:-4]
        txt = open(os.path.join(cdir, fn), encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"\\label\{([^}]+)\}", txt):
            seen.setdefault(m.group(1), cid)
    return seen


def unresolved(txt):
    """从 log 中取出未解析的 \ref 键（LaTeX 写作 Reference `xx' on page N undefined）。"""
    keys = []
    for m in re.finditer(r"Reference `([^']+)' on page \d+ undefined", txt):
        keys.append(m.group(1))
    return keys


def run(cid):
    sec, subsec, pages = CHUNKS[cid]
    outdir = os.path.join(ROOT, "work", "tmp_%s" % cid)
    os.makedirs(outdir, exist_ok=True)
    base = "_wrap_%s" % cid
    texpath = os.path.join(SRC, base + ".tex")
    with open(texpath, "w", encoding="utf-8") as f:
        f.write(wrap(cid))
    cmd = ["xelatex", "-interaction=nonstopmode",
           "-output-directory=" + outdir, base + ".tex"]
    last = ""
    for _ in range(2):
        p = subprocess.run(cmd, cwd=SRC, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
        last = p.stdout.decode("utf-8", "replace")
    log = os.path.join(outdir, base + ".log")
    txt = open(log, encoding="utf-8", errors="replace").read() if os.path.exists(log) else last
    errors = len(re.findall(r"^!", txt, re.M))
    over = len(re.findall(r"^Overfull", txt, re.M))
    under = len(re.findall(r"^Underfull", txt, re.M))
    undef = len(re.findall(r"Reference `[^']+' on page \d+ undefined", txt))
    missing = len(re.findall(r"Missing character", txt))
    pdf = os.path.join(outdir, base + ".pdf")
    if os.path.exists(pdf):
        shutil.copyfile(pdf, os.path.join(outdir, "wrap.pdf"))
    print("chunk=%s  pages=原书 p.%s" % (cid, pages))
    print("errors=%d overfull=%d underfull=%d undefined=%d missing_char=%d"
          % (errors, over, under, undef, missing))
    # 未解析引用的分类：跨块引用（label 在别的块里定义）与真悬空引用
    if undef:
        labels = all_labels(cid)
        keys = unresolved(txt)
        cross = [(k, labels[k]) for k in keys if k in labels and labels[k] != cid]
        unknown = [k for k in keys if k not in labels]
        print("  -> 跨块引用 %d 条（%s）" % (len(cross), ", ".join("%s@%s" % kv for kv in cross[:12])))
        if unknown:
            print("  -> **悬空引用（任何块都未定义）**: %s" % ", ".join(unknown))
        else:
            print("  -> 跨块引用均可在其他块中找到 \\label；整书编译后为 0")
    print("pdf: %s" % os.path.join(outdir, "wrap.pdf"))
    if errors:
        m = re.search(r"^!.*(?:\n.*){0,8}", txt, re.M)
        print("\n--- first error ---\n" + (m.group(0) if m else ""))
    for m in re.finditer(r"^Overfull.*$", txt, re.M):
        print(m.group(0)[:160])
    return errors


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    sys.exit(1 if run(sys.argv[1]) else 0)
