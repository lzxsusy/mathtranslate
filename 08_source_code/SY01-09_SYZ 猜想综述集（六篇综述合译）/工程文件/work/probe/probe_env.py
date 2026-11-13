# -*- coding: utf-8 -*-
"""环境探测（本机实测）→ work/probe/probe_env.md"""
import os, sys, subprocess, io, platform, tempfile, shutil

OUT = r"<本地路径>"
TEX = r"<本地路径>"
PY = r"<本地路径>"
BUILD = r"<本地路径>"

lines = ["# 环境探测（实测）", ""]

lines.append("## TeX")
lines.append(f"- lualatex exists: {os.path.exists(os.path.join(TEX, 'lualatex.exe'))}")
try:
    r = subprocess.run([os.path.join(TEX, "lualatex.exe"), "--version"], capture_output=True, text=True, timeout=60)
    lines.append("- " + r.stdout.splitlines()[0])
except Exception as e:
    lines.append(f"- lualatex version ERROR: {e!r}")
lines.append(f"- build dir writable: {os.path.isdir(BUILD)} / {os.access(BUILD, os.W_OK)}")
lines.append(f"- work dir writable: {os.access(r'<本地路径>', os.W_OK)}")
lines.append(f"- deliverable writable: {os.access(r'<本地路径>', os.W_OK)}")
lines.append("")

lines.append("## Python / PDF libs")
lines.append(f"- python: {sys.version.split()[0]} @ {sys.executable}")
try:
    import pymupdf
    lines.append(f"- pymupdf: {pymupdf.__version__ if hasattr(pymupdf,'__version__') else pymupdf.VersionBind}")
except Exception as e:
    lines.append(f"- pymupdf ERROR {e!r}")
for mod in ("pypdf", "pikepdf", "pdfplumber"):
    try:
        __import__(mod); lines.append(f"- {mod}: ok")
    except Exception as e:
        lines.append(f"- {mod}: MISSING ({e.__class__.__name__})")
lines.append("")

lines.append("## ctex / fonts 冒烟（3 行文档，由 build.ps1 落实验证）")
lines.append("")

lines.append("## 已知本机硬约束（手册 M1/M2）")
lines.append("- lualatex 不能写非 ASCII 路径的 .log；子进程不能写 Desktop")
lines.append("- 编译必须在 default-workspace\\syzbuild 镜像目录进行，PDF 拷回")
lines.append("- TMP/TEMP 显式指向 syzbuild\\tmp")
lines.append("- 日志用 Out-Null，不重定向到 <jobname>.out")

# smoke test
os.makedirs(BUILD, exist_ok=True)
os.makedirs(os.path.join(BUILD, "tmp"), exist_ok=True)
smoke = os.path.join(BUILD, "smoke.tex")
with open(smoke, "w", encoding="utf-8") as fh:
    fh.write(r"""\documentclass[UTF8]{ctexart}
\usepackage{amsmath,amssymb}
\begin{document}
中文冒烟测试：$E=mc^2$，$\int_0^1 x\,dx=\tfrac12$。
\begin{equation}\label{eq:1} a^2+b^2=c^2 \end{equation}
\end{document}
""")
env = dict(os.environ)
env["PATH"] = TEX + ";" + env.get("PATH", "")
env["TMP"] = os.path.join(BUILD, "tmp")
env["TEMP"] = env["TMP"]
log = []
for i in range(1, 4):
    r = subprocess.run([os.path.join(TEX, "lualatex.exe"), "-interaction=nonstopmode", "-file-line-error", "smoke.tex"],
                       cwd=BUILD, env=env, capture_output=True, text=True, timeout=600)
    log.append(f"pass {i}: exit={r.returncode}")
pdf = os.path.join(BUILD, "smoke.pdf")
lines.append("## 冒烟编译")
lines.extend("- " + x for x in log)
lines.append(f"- smoke.pdf: {os.path.exists(pdf)} size={os.path.getsize(pdf) if os.path.exists(pdf) else 0}")
if os.path.exists(os.path.join(BUILD, "smoke.log")):
    lg = open(os.path.join(BUILD, "smoke.log"), encoding="utf-8", errors="replace").read()
    import re
    lines.append(f"- log errors: file:line={len(re.findall(r'(?m)^[^<本地路径>]*?\\:\\d+: ', lg))} fatal={len(re.findall(r'(?m)^! ', lg))}")
    lines.append(f"- missing char={len(re.findall(r'Missing character', lg))}")

with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(lines) + "\n")
print("\n".join(lines))
