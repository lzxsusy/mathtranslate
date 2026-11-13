# -*- coding: utf-8 -*-
"""一键构建（Lead 独占）：汇总 → xelatex ×2 → 生成 deliverable/。
用法: python build.py
"""
import os, shutil, subprocess, sys, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
XELATEX = r"<本地路径>"
PANDOC = r"<本地路径>"


def run(cmd, cwd=ROOT):
    env = dict(os.environ)
    env["TMP"] = os.path.join(ROOT, "tmp")
    env["TEMP"] = env["TMP"]
    env["PYTHONIOENCODING"] = "utf-8"
    p = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p


def main():
    print("== 1. aggregate ==")
    p = run([PY, "aggregate.py"])
    print(p.stdout.strip()[-2000:])

    print("== 2. xelatex x2 ==")
    for i in (1, 2):
        p = run([XELATEX, "-interaction=nonstopmode", "-file-line-error", "main.tex"])
        print("pass", i, "rc=", p.returncode)

    log = os.path.join(ROOT, "main.log")
    if os.path.exists(log):
        txt = open(log, encoding="utf-8", errors="replace").read()
        # 注意：-file-line-error 下错误行形如 "src/b03.tex:189: Undefined control sequence."，
        # 不以 "!" 开头，必须按关键字匹配。
        pats = ("Undefined control", "LaTeX Error", "Missing $", "Extra }",
                "Runaway", "Bad math environment", "ended by \\end")
        errs = [l for l in txt.split("\n")
                if l.startswith("!") or any(k in l for k in pats)]
        ovf = [l for l in txt.split("\n") if l.startswith("Overfull")]
        print("LaTeX errors:", len(errs), "Overfull:", len(ovf))
        for l in errs[:20]:
            print("  ", l)
        big = [l for l in ovf if "pt too wide" in l]
        for l in big[:10]:
            print("  ", l)

    pdf = os.path.join(ROOT, "main.pdf")
    if not os.path.exists(pdf):
        print("!! main.pdf 未生成"); return 1
    print("main.pdf pages/size:", os.path.getsize(pdf))

    print("== 3. deliverable ==")
    dd = os.path.join(ROOT, "deliverable")
    os.makedirs(os.path.join(dd, "src"), exist_ok=True)
    shutil.copy2(pdf, os.path.join(dd, "共形场论与规范对称性-中文译注本.pdf"))
    for f in glob.glob(os.path.join(ROOT, "src", "*.tex")) + [os.path.join(ROOT, "main.tex")]:
        shutil.copy2(f, os.path.join(dd, "src", os.path.basename(f)))
    for f in ("ENGINEERING.md", "译注汇总.md", "ERRATA.md", "脉络梳理.md", "glossary.tsv",
              "BRIEF.md", "STYLE_GUIDE.md", "TIMELINE.md", "BLOCK_TASKS.md", "ROADMAP_SPEC.md"):
        src = os.path.join(ROOT, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dd, f))

    # Markdown -> PDF（中文）
    md2pdf = [("译注汇总.md", "译注汇总.pdf"), ("脉络梳理.md", "脉络梳理.pdf"),
              ("ENGINEERING.md", "工程文档.pdf"), ("ERRATA.md", "ERRATA.pdf")]
    for m, p_ in md2pdf:
        src = os.path.join(dd, m)
        if not os.path.exists(src):
            continue
        out = os.path.join(dd, p_)
        r = run([PANDOC, src, "-o", out, "--pdf-engine=xelatex",
                 "-V", "CJKmainfont=SimSun", "-V", "geometry:margin=2.4cm",
                 "--wrap=none", "-V", "linkcolor=black"])
        print("pandoc", m, "->", p_, "rc=", r.returncode)
        if r.returncode != 0:
            print(r.stderr[-800:])
    print("== done ==")
    return 0


if __name__ == "__main__":
    sys.exit(main())
