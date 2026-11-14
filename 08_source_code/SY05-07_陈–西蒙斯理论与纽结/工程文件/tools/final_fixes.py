import io
import re

# 1) s01: strip trailing ASCII period inside \paragraph{...}
p = "sections/s01-intro.tex"
t = open(p, encoding="utf-8").read()
t2 = re.sub(r"\\paragraph\{([^}]*?)。?\}", r"\\paragraph{\1}", t)
t2 = re.sub(r"\\paragraph\{([^}]*?)\.\}", r"\\paragraph{\1}", t2)
open(p, "w", encoding="utf-8").write(t2)
print("s01 paragraphs:", len(re.findall(r"\\paragraph\{", t2)))

# 2) s02b: figure reference for fig:torus
p = "sections/s02b-abelian2.tex"
t = open(p, encoding="utf-8").read()
assert "如图 2 所示" in t
t = t.replace("如图 2 所示", "如图 \\ref{fig:torus} 所示")
open(p, "w", encoding="utf-8").write(t)
print("s02b fig ref added")

# 3) s03a: add a note on the "2 pi k w(g) integer" slip
p = "sections/s03a-framing.tex"
t = open(p, encoding="utf-8").read()
anchor = "这就要求 $2\\pi k\\,w(g)$ 为整数，从而 $k\\in\\Z$。"
assert anchor in t
note = anchor + """

% [Tutor Note: 原文疑误] 「2πkw(g) 为整数」字面不成立：单值性要求 e^{2πikw}=1，即 k w(g)∈Z；结论 k∈Z 不变
\\begin{yizhu}[原文疑误]
原文此句作 “This forces $2\\pi k\\,w(g)$ to be an integer”，字面读不通：$e^{i\\SCS}$ 单值只要求 $e^{2\\pi ik\\,w(g)}=1$，即 $k\\,w(g)\\in\\Z$，等价于说 $2\\pi k\\,w(g)$ 是 $2\\pi$ 的整数倍，而不是它本身为整数（后者对一般的 $k$ 无解）。取 $w(g)=1$ 即得 $k\\in\\Z$，故结论不受影响。中译本照录原文措辞，读者按 $e^{2\\pi ik\\,w}=1$ 理解即可。
\\end{yizhu}"""
t = t.replace(anchor, note)
open(p, "w", encoding="utf-8").write(t)
print("s03a note inserted")
