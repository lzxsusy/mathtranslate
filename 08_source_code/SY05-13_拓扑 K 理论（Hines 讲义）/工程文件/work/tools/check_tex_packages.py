# -*- coding: utf-8 -*-
"""盘点 TeX Live 里缺哪些宏包（用 kpsewhich 逐项探测）。"""
import subprocess, sys, os
sys.stdout.reconfigure(encoding="utf-8")

BIN = r"<本地路径>"
KPSE = os.path.join(BIN, "kpsewhich.exe")

# 候选：数学物理翻译/排版最常用的宏包（按用途分组）
groups = {
    "数学/记号": ["amsmath", "amssymb", "amsthm", "mathtools", "mathrsfs", "bm", "bbm", "dsfont",
                  "esint", "extarrows", "cancel", "braket", "physics", "siunitx", "tensor",
                  "upgreek", "stmaryrd", "mathabx", "txfonts", "newtx", "newpx", "pxfonts",
                  "mathpazo", "fourier", "eulervm", "bbold", "unicode-math", "lualatex-math",
                  "mathspec", "cases", "extpfeil", "xymatrix", "amscd"],
    "定理/排版": ["thmtools", "ntheorem", "mdframed", "framed", "fancybox", "tcolorbox",
                  "titlesec", "titletoc", "tocloft", "sectsty", "titlesec", "appendix",
                  "etoc", "minitoc", "enumitem", "caption", "subcaption", "subfig", "float",
                  "placeins", "wrapfig", "adjustbox", "rotating", "pdflscape", "lscape",
                  "setspace", "parskip", "ragged2e", "microtype", "csquotes", "lineno"],
    "表格": ["longtable", "booktabs", "multirow", "tabularx", "tabulary", "makecell",
             "threeparttable", "colortbl", "xltabular", "diagbox", "slashbox", "bigdelim",
             "dcolumn", "siunitx", "tabu", "supertabular", "ltablex"],
    "图/TikZ": ["tikz", "pgf", "pgfplots", "tikz-cd", "tikz-feynman", "tikz-3dplot",
                "tikz-dependency", "pgfopts", "circuitikz", "chemfig", "tikzmark",
                "graphicx", "standalone", "pdfpages", "preview", "overpic", "eso-pic",
                "background", "textpos", "fancyhdr", "geometry", "xcolor", "transparent"],
    "文献/索引": ["biblatex", "natbib", "cite", "glossaries", "imakeidx", "makeidx",
                  "xindy", "biber", "notes2bib", "doi", "url", "xurl", "hyperref",
                  "bookmark", "hypcap", "cleveref", "autonum"],
    "中文/字体": ["ctex", "xeCJK", "luatexja", "fontspec", "zhnumber", "lmodern", "cm-super",
                  "fandol", "arphic", "uming", "ukai"],
    "代码/算法": ["listings", "minted", "algorithm2e", "algorithmicx", "algpseudocode",
                  "algorithm", "clrscode3e", "program"],
    "幻灯片/其他": ["beamer", "beamerposter", "pgfpages", "handout", "pdfpc", "multimedia",
                    "notes", "xmpincl", "datetime", "xstring", "etoolbox", "xpatch",
                    "etex", "ifthen", "calc", "suffix", "refcount", "kvoptions", "oberdiek"],
}


def has(style):
    r = subprocess.run([KPSE, style + ".sty"], capture_output=True, text=True)
    if r.stdout.strip():
        return True
    r = subprocess.run([KPSE, style + ".cls"], capture_output=True, text=True)
    return bool(r.stdout.strip())


missing = {}
present = 0
for g, pkgs in groups.items():
    miss = []
    for p in pkgs:
        if has(p):
            present += 1
        else:
            miss.append(p)
    if miss:
        missing[g] = sorted(set(miss))

print(f"已安装（探测项中）: {present}")
print("缺失分组：")
for g, miss in missing.items():
    print(f"  [{g}] {len(miss)} 个: {', '.join(miss)}")

allmiss = sorted({p for v in missing.values() for p in v})
print("\n合计缺失:", len(allmiss))
print(" ".join(allmiss))
