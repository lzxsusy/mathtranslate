import sys
sys.stdout.reconfigure(encoding="utf-8")
p = r"<本地路径>"
rows = [
    r"| p7（图 1 图注） | \"colliding labels adds dimensions\" | \"add dimensions\"（主谓一致） | 复数主语加 adds 不通。 |",
    r"| p12 | \"the image of (17) are the topological field theories\" | \"is\" | 主语 image 为单数。 |",
    r"| p10（式 (11) 末两处） | $E(\cup^{+})$、$E(\cup^{+})$（无下标 $t$） | 依生成元记号应为 $E(\cup^{\pm}_t)$；同行 $E(\cap^{+}_t)$ 带下标 | 同式内记号不对称，照原文排。 |",
    r"| p13（式 (20) 第四行） | 第二个 $E(\cup^{+}_t)$ | 应为 $E(\cup^{-}_t)$（与式 (19) 同型） | 同一行第一个已用 $\cup^{+}_t$，第二列应配 $\cup^{-}_t$。 |",
    r"| p13（式 (20) 的 2-胞图） | 扭标作 $\alpha_n$ | 按本节正文应为 $\alpha_A$（同页写「$\alpha_A$-扭场论」） | 页面图确认图中下标为 $n$；照原文排 + 批注。 |",
    r"| p13（例 2.24） | \"a twisted spin field theory theory\" | 去掉重复的 theory | 连写两个 theory。 |",
    r"| p9（命题 2.7 的证明） | 先写 $\mathrm{BPU}(H)$（斜体 $H$）、后写 $\mathrm{BPU}(\cH)$ | 同一对象两种写法 | 非笔误，照原文排；统一用 $\cH$ 读。 |",
]
s = open(p, encoding="utf-8").read().rstrip("\n")
s = s + "\n" + "\n".join(rows) + "\n"
open(p, "w", encoding="utf-8", newline="\n").write(s)
print("appended", len(rows), "rows; total lines", s.count("\n"))
