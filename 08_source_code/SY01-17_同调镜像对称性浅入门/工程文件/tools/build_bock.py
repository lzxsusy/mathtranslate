# -*- coding: utf-8 -*-
"""Build the book: xelatex -> makeindex -> xelatex x2.

Usage:  python tools/build_bock.py [--dir bock/book] [--out main] [--quiet]
"""
import os, re, sys, subprocess, argparse

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TL = os.path.join(WS, ".texlive", "2026")
BIN = os.path.join(TL, "bin", "windows")
DEPS = os.path.join(WS, "texdeps")


def env():
    e = dict(os.environ)
    e["PATH"] = BIN + os.pathsep + e.get("PATH", "")
    d = DEPS.replace("\\", "/")
    e["TEXINPUTS"] = d + "//;" + e.get("TEXINPUTS", "")
    e["OPENTYPEFONTS"] = d + "/fonts/opentype//;" + e.get("OPENTYPEFONTS", "")
    e["TTFONTS"] = d + "/fonts/truetype//;" + e.get("TTFONTS", "")
    e["TEXMFHOME"] = DEPS
    return e


def run(cmd, cwd):
    r = subprocess.run(cmd, cwd=cwd, env=env(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="bock/book")
    ap.add_argument("--out", default="main")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    d = os.path.join(WS, a.dir)
    os.makedirs(os.path.join(d, "build"), exist_ok=True)
    xelatex = os.path.join(BIN, "xelatex.exe")
    args = ["-interaction=nonstopmode", "-halt-on-error", "-output-directory=build", a.out + ".tex"]
    logs = []
    rc, out = run([xelatex] + args, d)
    logs.append(("pass1", rc))
    if rc != 0:
        open(os.path.join(d, "build", "err.log"), "w", encoding="utf-8").write(out)
        print("PASS1 FAILED rc=", rc)
        for line in out.splitlines():
            if line.startswith("!") or "Error" in line or line.startswith("l."):
                print(line)
        return 1
    idx = os.path.join(d, "build", a.out + ".idx")
    if os.path.exists(idx):
        rc2, out2 = run([os.path.join(BIN, "makeindex.exe"), "-o",
                         os.path.join("build", a.out + ".ind"), os.path.join("build", a.out + ".idx")], d)
        logs.append(("makeindex", rc2))
        if rc2 != 0:
            print("MAKEINDEX rc=", rc2, out2[-800:])
    for i in range(2):
        rc, out = run([xelatex] + args, d)
        logs.append((f"pass{i+2}", rc))
        if rc != 0:
            open(os.path.join(d, "build", "err.log"), "w", encoding="utf-8").write(out)
            print(f"PASS{i+2} FAILED rc=", rc)
            for line in out.splitlines():
                if line.startswith("!") or "Error" in line:
                    print(line)
            return 1
    pdf = os.path.join(d, "build", a.out + ".pdf")
    logtxt = ""
    logf = os.path.join(d, "build", a.out + ".log")
    if os.path.exists(logf):
        logtxt = open(logf, encoding="utf-8", errors="replace").read()
    warn = [l for l in logtxt.splitlines() if l.startswith("LaTeX Warning") or "Overfull" in l]
    print("RESULT", logs, "pdf", os.path.getsize(pdf) if os.path.exists(pdf) else None)
    print("warnings:", len(warn))
    if not a.quiet:
        for w in warn[:20]:
            print("  ", w[:160])
    try:
        import pymupdf
        doc = pymupdf.open(pdf)
        print("pages:", doc.page_count)
    except Exception as ex:
        print("page count unavailable", ex)
    return 0


if __name__ == "__main__":
    sys.exit(main())
