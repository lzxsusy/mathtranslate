import io, sys, glob, os, re
sys.stdout.reconfigure(encoding="utf-8")
CH = r"<本地路径>"
files = [f for f in sorted(glob.glob(os.path.join(CH, "*.tex"))) if not os.path.basename(f).startswith("_")]
CJK = r"\u4e00-\u9fff"
TERMS = "扇区|和乐|离壳|后代|鬼数"

pat1 = re.compile(rf"(?<=[{CJK}])[ \t]+(?=({TERMS}))")
pat2 = re.compile(rf"(({TERMS}))[ \t]+(?=[{CJK}])")
total1 = total2 = 0
for f in files:
    s = io.open(f, encoding="utf-8").read()
    s2, n1 = pat1.subn(r"\1", s)
    s2, n2 = pat2.subn(r"\1", s2)
    total1 += n1
    total2 += n2
    if s2 != s:
        io.open(f, "w", encoding="utf-8", newline="\n").write(s2)
print("space-before-term fixed:", total1, " space-after-term fixed:", total2)

# 复查残留
alltxt = "".join(io.open(f, encoding="utf-8").read() for f in files)
for pat, name in ((rf"[{CJK}] (扇区|和乐|离壳|后代|鬼数)", "CJK+space+term"),
                  (rf"(扇区|和乐|离壳|后代|鬼数) [{CJK}]", "term+space+CJK")):
    m = re.findall(pat, alltxt)
    print(name, "residual:", len(m))
