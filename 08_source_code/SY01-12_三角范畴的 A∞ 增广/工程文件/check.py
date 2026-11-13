# -*- coding: utf-8 -*-
r"""check.py —— 交付前自检（内容 / 语言 / 工程三组）。

用法（工程根目录）：
    python check.py            # 先编译整书两遍，再自检
    python check.py --nocompile  # 只做源码自检（用已有 main.log）

输出全英文，避免控制台中日文乱码。退出码 0 = 全通过。
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
CHUNKS = os.path.join(SRC, "chunks")
OUTDIR = os.path.join(ROOT, "work", "main_build")

# 每块应有的编号公式条数（\begin{equation} 个数）
EQ_EXPECT = {"c00": 1, "c01": 2, "c02": 3, "c03": 2, "c04": 0,
             "c05": 0, "c06": 2, "c07": 0}

# 禁用句式（STYLE_GUIDE §1）
BANNED = [
    "被…所", "被……所",
    "进行…的", "进行……的",
    "对于…而言", "对于……而言",
    "关于…的讨论", "关于……的讨论",
    "使得…得以", "使得……得以",
    "众所周知", "不难发现", "值得注意的是",
    "起到了…作用", "起到了……作用",
    "有着…意义", "有着……意义",
]

KANA = re.compile(u"[\u3041-\u309f\u30a0-\u30ff]")
THEOREM_ENVS = ["definition", "theorem", "proposition", "lemma",
                "corollary", "example", "remark", "problem"]


def read(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()


def compile_main():
    os.makedirs(OUTDIR, exist_ok=True)
    for run in (1, 2):
        p = subprocess.run(["xelatex", "-interaction=nonstopmode",
                            "-output-directory=" + OUTDIR, "main.tex"],
                           cwd=SRC, capture_output=True)
        if p.returncode not in (0, 1):
            print("xelatex run", run, "returncode", p.returncode)
    log = os.path.join(OUTDIR, "main.log")
    if not os.path.exists(log):
        print("FATAL: main.log not found")
        return None
    with io.open(log, encoding="utf-8", errors="replace") as f:
        return f.read()


def main():
    ok = True
    do_compile = "--nocompile" not in sys.argv
    log = compile_main() if do_compile else None
    if log is None and not do_compile:
        lp = os.path.join(OUTDIR, "main.log")
        log = read(lp) if os.path.exists(lp) else ""
    if log:
        errs = [l for l in log.splitlines() if l.startswith("!")]
        over = len(re.findall(r"Overfull \\hbox", log))
        overv = len(re.findall(r"Overfull \\vbox", log))
        undef = len(re.findall(r"Reference .* undefined", log)) \
            + len(re.findall(r"Citation .* undefined", log))
        misschar = len(re.findall(r"Missing character", log))
        dup_bookmark = len(re.findall(r"destination with the same identifier", log))
        print("[ENGINE] errors=%d overfull_hbox=%d overfull_vbox=%d undefined=%d "
              "missing_char=%d dup_bookmark=%d" % (errs, over, overv, undef, misschar, dup_bookmark))
        for e in errs[:8]:
            print("   ", e)
        ok &= (not errs) and over == 0 and undef == 0 and misschar == 0
        pdf = os.path.join(OUTDIR, "main.pdf")
        if os.path.exists(pdf):
            import pymupdf
            d = pymupdf.open(pdf)
            print("[ENGINE] pages=%d" % d.page_count)

    files = sorted(f for f in os.listdir(CHUNKS) if re.fullmatch(r"c\d\d\.tex", f))
    total_eq = total_thm = total_note = 0
    print("[SRC] chunks:", ", ".join(f[:3] for f in files))
    for f in files:
        cid = f[:3]
        t = read(os.path.join(CHUNKS, f))
        eq = len(re.findall(r"<本地路径>", t))
        eq_star = len(re.findall(r"<本地路径>*\}", t))
        thm = sum(len(re.findall(r"<本地路径>" % e, t)) for e in THEOREM_ENVS)
        note = len(re.findall(r"<本地路径>*\{", t))
        # prose = source without comment lines and without bibliography block,
        # so that Japanese reference titles and %-comments do not trigger checks
        prose_lines = []
        in_bib = False
        for ln in t.splitlines():
            if ln.strip().startswith("%"):
                continue
            if "\\begin{thebibliography}" in ln:
                in_bib = True
            if not in_bib:
                prose_lines.append(ln)
            if "\\end{thebibliography}" in ln:
                in_bib = False
        prose = "\n".join(prose_lines)
        kana = KANA.findall(prose)
        banned = [b for b in BANNED if b in prose]
        bad_env = "\\begin{transnote}" in t
        tags = len(re.findall(r"\\tag", prose))
        cites = len(re.findall(r"\\cite", prose))
        total_eq += eq
        total_thm += thm
        total_note += note
        exp = EQ_EXPECT.get(cid)
        flag = ""
        if exp is not None and eq != exp:
            flag += " EQ_MISMATCH(expect %d)" % exp
            ok = False
        if eq_star:
            flag += " EQSTAR(%d)" % eq_star
        if kana:
            flag += " KANA(%d: %s)" % (len(kana), "".join(kana[:6]))
            ok = False
        if banned:
            flag += " BANNED(%s)" % ",".join(banned)
            ok = False
        if bad_env:
            flag += " TRANSNOTE_ENV"
            ok = False
        if tags:
            flag += " TAG(%d)" % tags
            ok = False
        if cites:
            flag += " CITE(%d)" % cites
        print("  %s eq=%d thm=%d note=%d%s" % (cid, eq, thm, note, flag))

    bib = read(os.path.join(CHUNKS, "c07.tex")) if os.path.exists(os.path.join(CHUNKS, "c07.tex")) else ""
    nbib = len(re.findall(r"\\bibitem", bib))
    print("[SRC] bibitems=%d (expect 22)" % nbib)
    if nbib != 22:
        ok = False
    print("[SRC] equations total=%d (expect 10), theorem-envs total=%d (expect 18), "
          "notes total=%d" % (total_eq, total_thm, total_note))
    if total_eq != 10 or total_thm != 18:
        ok = False

    print("VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
