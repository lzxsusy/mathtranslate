# -*- coding: utf-8 -*-
"""单独编译某一讲的 chunk，用于译手自检。

用法（工程根目录下）：
    python 工程文件/tools/compile_chunk.py 07
退出码 0 表示零 error。编译产物在临时目录，不污染 源码/。
"""
import os, sys, subprocess, tempfile, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "源码")


def main(nn):
    nn = f"{int(nn):02d}"
    chunk = os.path.join(SRC, "chunks", f"lec{nn}.tex")
    if not os.path.exists(chunk):
        print(f"[FAIL] 找不到 {chunk}")
        return 2
    test = os.path.join(SRC, f"_test_lec{nn}.tex")
    with open(test, "w", encoding="utf-8") as f:
        f.write("\\input{preamble}\n\\begin{document}\n")
        f.write(f"\\input{{chunks/lec{nn}}}\n")
        f.write("\\end{document}\n")
    outdir = tempfile.mkdtemp(prefix=f"lec{nn}_")
    cmd = ["xelatex", "-interaction=nonstopmode", "-halt-on-error",
           f"-output-directory={outdir}", f"_test_lec{nn}.tex"]
    try:
        r = subprocess.run(cmd, cwd=SRC, capture_output=True, text=True,
                           errors="replace", timeout=300)
        log = r.stdout + r.stderr
        errs = re.findall(r"^! .*(?:\n.*){0,4}", log, re.M)
        if r.returncode == 0 and not errs:
            print(f"[OK] lec{nn} 编译通过（零 error）")
            return 0
        print(f"[FAIL] lec{nn} 编译失败，returncode={r.returncode}")
        for e in errs[:12]:
            print("  " + e.replace("\n", "\n  "))
        m = re.search(r"^l\.(\d+)", log, re.M)
        if m:
            print(f"  首个错误位置：第 {m.group(1)} 行")
        return 1
    finally:
        try:
            os.remove(test)
        except OSError:
            pass


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
