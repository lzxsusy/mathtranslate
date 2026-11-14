"""Assemble sections/*.tex into a single self-contained .tex file.

Usage: python tools/assemble.py  -> writes "../CS and Knots.tex" (project root: cs_knots/CS and Knots.tex)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(ROOT, "main.tex")
OUT = os.path.join(ROOT, "CS and Knots.tex")


def main():
    src = open(MAIN, encoding="utf-8-sig").read().replace("\ufeff", "")
    banner = (
        "% =============================================================================\n"
        "%  单文件版：由 tools/assemble.py 从 main.tex + sections/*.tex 自动装配，\n"
        "%  手改请改 sections/ 分片后重新装配，否则下次装配会被覆盖。\n"
        "% =============================================================================\n"
    )

    def repl(m):
        name = m.group(1).strip()
        path = os.path.join(ROOT, name + ".tex")
        if not os.path.exists(path):
            sys.exit(f"missing section file: {path}")
        body = open(path, encoding="utf-8-sig").read().replace("\ufeff", "").rstrip() + "\n"
        return f"% >>>>>>>>>>>>>>>> {name}.tex <<<<<<<<<<<<<<<<\n{body}% >>>>>>>>>>>>>>>> end {name}.tex <<<<<<<<<<<<<<<<\n"

    out = re.sub(r"\\input\{([^}]+)\}", repl, src)
    out = (banner + out).replace("\ufeff", "")
    open(OUT, "w", encoding="utf-8").write(out)
    n = out.count("\n")
    print(f"wrote {OUT}  ({n} lines, {len(out)} bytes)")


if __name__ == "__main__":
    main()
