import sys
sys.stdout.reconfigure(encoding="utf-8")
p = r"<本地路径>"
L = open(p, encoding="utf-8").read().split("\n")
row = ("| p12（式 (19) 第四行） | 第二个 " + r"$\alpha_A(\cup^{+}_t)$" +
       " | 按同一行第一个及对称性，应为 " + r"$\alpha_A(\cup^{-}_t)$" +
       " | 同行已有 " + r"$\cup^{+}_t\mapsto{}_{A\otimes\ol{A}}A$" +
       "，第二个应配 " + r"$\cup^{-}_t$" + "；照原样排 + 批注。 |")
assert L[25].startswith("| p12"), L[25][:30]
L[25] = row
open(p, "w", encoding="utf-8", newline="\n").write("\n".join(L))
print("fixed:", row)
