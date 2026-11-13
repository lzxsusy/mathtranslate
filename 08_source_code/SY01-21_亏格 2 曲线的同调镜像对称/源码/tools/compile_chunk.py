#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""单块编译自检（EN48）。

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
    "c00": ("-1", "0", "i–v"),
    "c01": ("0", "0", "1–12"),
    "c02": ("1", "2", "13–22"),
    "c03": ("1", "3", "23–43"),
    "c04": ("1", "0", "44–69"),
    "c05": ("2", "0", "70–81"),
    "c06": ("3", "0", "82–90"),
    "c07": ("4", "1", "91–109"),
    "c08": ("4", "3", "110–113"),
    "c09": ("4", "0", "114–130"),
    "c10": ("5", "0", "131"),
    "c11": ("6", "0", "132–136"),
}


def wrap(cid):
    sec, subsec, _ = CHUNKS[cid]
    head = ("\\input{preamble}\n\\begin{document}\n"
            "\\setcounter{section}{%s}\n\\setcounter{subsection}{%s}\n" % (sec, subsec))
    body = "\\input{chunks/%s}\n\\end{document}\n" % cid
    return head + body


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
    undef = len(re.findall(r"undefined", txt, re.I))
    missing = len(re.findall(r"Missing character", txt))
    pdf = os.path.join(outdir, base + ".pdf")
    if os.path.exists(pdf):
        shutil.copyfile(pdf, os.path.join(outdir, "wrap.pdf"))
    print("chunk=%s  pages=原书 p.%s" % (cid, pages))
    print("errors=%d overfull=%d underfull=%d undefined=%d missing_char=%d"
          % (errors, over, under, undef, missing))
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
