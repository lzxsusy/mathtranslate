# -*- coding: utf-8 -*-
"""build2.py — 真编译 + 日志验收（唯一验收标准）

用法： python build2.py [--clean]
验收四项：① file:line 错误数 = 0  ② Undefined control sequence = 0
          ③ Missing character = 0  ④ main.pdf 存在且 >0 字节
"""
import os, re, subprocess, sys, shutil

ROOT = r"<本地路径>"
TEXDIR = r"G:\texlive\2026\bin\windows"
XELATEX = os.path.join(TEXDIR, "xelatex.exe")
TMP = os.path.join(ROOT, "tmp")
os.makedirs(TMP, exist_ok=True)

env = dict(os.environ)
env["TMP"] = TMP
env["TEMP"] = TMP
env["TMPDIR"] = TMP
env["PYTHONIOENCODING"] = "utf-8"

if "--clean" in sys.argv:
    for f in ["main.aux", "main.toc", "main.out", "main.log", "main.pdf"]:
        p = os.path.join(ROOT, f)
        if os.path.exists(p):
            os.remove(p)

log_path = os.path.join(ROOT, "compile.log")
allout = []
for run in (1, 2):
    p = subprocess.run([XELATEX, "-interaction=nonstopmode", "-file-line-error", "main.tex"],
                       cwd=ROOT, env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=1800)
    allout.append("===== PASS %d (exit %d) =====\n" % (run, p.returncode))
    allout.append(p.stdout[-40000:])

with open(log_path, "w", encoding="utf-8", newline="\n") as f:
    f.write("".join(allout))

logfile = os.path.join(ROOT, "main.log")
log = open(logfile, encoding="utf-8", errors="replace").read() if os.path.exists(logfile) else ""

errs = re.findall(r"^([^\s:][^:]*):(\d+): (.*)$", log, re.M)
errs = [e for e in errs if not e[2].startswith("warning") and "Package" not in e[0]]
undef = re.findall(r"Undefined control sequence", log)
miss = re.findall(r"Missing character: There is no (\S+)", log)
overfull = len(re.findall(r"Overfull \\hbox", log))
# 追加：LaTeX 错误行与 Package Error（不能只看 file:line）
bang = re.findall(r"^! (.*)$", log, re.M)
pkg_err = re.findall(r"^Package (\w+) Error: (.*)$", log, re.M)
pdf = os.path.join(ROOT, "main.pdf")
pdfsize = os.path.getsize(pdf) if os.path.exists(pdf) else 0
pages = 0
try:
    import pymupdf
    pages = len(pymupdf.open(pdf))
except Exception:
    pass

print("PDF: exists=%s size=%d pages=%d" % (os.path.exists(pdf), pdfsize, pages))
print("file:line errors = %d" % len(errs))
for e in errs[:25]:
    print("   %s:%s: %s" % e)
print("Undefined control sequence = %d" % len(undef))
if undef:
    ctx = re.findall(r"(?:^|\n)(.{0,160}Undefined control sequence.{0,200})", log)
    for c in ctx[:8]:
        print("   ", c.replace("\n", " ")[:260])
print("Missing character = %d" % len(miss))
if miss:
    from collections import Counter
    print("   ", Counter(miss).most_common(15))
print("Overfull hbox = %d" % overfull)
print("LaTeX ! errors = %d | Package Error = %d" % (len(bang), len(pkg_err)))
for b in bang[:10]:
    print("   !", b[:160])
for p in pkg_err[:10]:
    print("   Package %s Error: %s" % p)

ok = (len(errs) == 0 and len(undef) == 0 and len(miss) == 0
      and len(bang) == 0 and len(pkg_err) == 0 and pdfsize > 0)
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
