# -*- coding: utf-8 -*-
"""Gate 4 落改 patch：ch01c 的 M1–M3 批注修正 + ch01b 尾注清理。exact-match，命中数须等于预期。"""
import os

CH = r"<本地路径>"
log = []


def sub(fname, old, new, why, expect=1):
    p = os.path.join(CH, fname)
    t = open(p, encoding="utf-8").read()
    n = t.count(old)
    if n != expect:
        log.append(f"SKIP {fname}: {why} (命中 {n}, 预期 {expect})")
        return
    open(p, "w", encoding="utf-8").write(t.replace(old, new))
    log.append(f"OK   {fname}: {why}")


# M1
OLD1 = r"""% [Tutor Note: 这里 $\fg(\bm p)$ 的元素取值为亚纯函数，故它在 $p_i$ 处只有有限阶极点；$\iota$ 把它们逐个展开到各点、再直和起来。要点是“同一点的不同展开彼此相容”------当 $f$ 是多项式（无极点）时各 $\iota_j(f)$ 都是零次项，$\iota$ 仍为单射，靠的正是解析延拓的唯一性。]"""
NEW1 = r"""% [Tutor Note: 这里 $\fg(\bm p)$ 的元素取值为亚纯函数，故它在 $p_i$ 处只有有限阶极点；$\iota$ 把同一个 $f$ 在各点 $p_j$ 处分别展开、再直和起来。当 $f$ 无极点时，各 $\iota_j(f)$ 只有非负次项；若对每个 $j$ 都有 $\iota_j(f)=0$，则 $f$ 在各 $p_j$ 附近恒为 $0$，由解析延拓的唯一性得 $f\equiv0$，故 $\iota$ 为单射。]"""
sub("ch01c.tex", OLD1, NEW1, "M1 iota 批注修正")

# M2
OLD2 = r"""$-2(k+1)$ 来自 $V_1$ 与 $d_1$ 的搭配，等价于 $d_1-\lambda_1=k+1$。"""
NEW2 = r"""$+2(k+1)$ 来自 $V_{\lambda_1}$ 与 $d_1$ 的搭配，即 $d_1+\lambda_1=k+1$。"""
sub("ch01c.tex", OLD2, NEW2, "M2 符号与下标修正")

# M3
OLD3 = r"""% [Tutor Note: 图中箭头只标出“外侧 $n+1$ 条边”的指向，并不表示最高权的大小，真正约束每条边权的是三价顶点处的 level $k$ Clebsch--Gordan 条件"""
NEW3 = r"""% [Tutor Note: 图中每条边上的箭头只标出该边的定向（相对顶点的指向），并不表示最高权的大小，真正约束每条边权的是三价顶点处的 level $k$ Clebsch--Gordan 条件"""
sub("ch01c.tex", OLD3, NEW3, "M3 箭头批注修正")

# O1
sub("ch01c.tex", r"若 $\lambda_1+\lambda_2+\lambda_3\le2k$，上述不等号恒成立",
    r"若 $\lambda_1+\lambda_2+\lambda_3\le2k$，上述不等式（即 $2(k+1)-(\lambda_1+\lambda_2+\lambda_3)+2(n_2+n_3)\ne0$）恒成立",
    "O1 不等号→不等式")

# O2
sub("ch01c.tex", r"亚纯函数空间 $\fg(\bm p)$ 在", r"$\fg(\bm p)$ 在", "O2 删「亚纯函数空间」")

# L1 ch01b 尾注
OLD_L1 = r"""% --- 命题 1.11 的证明起于 p.24 末行、续于 p.25 开头（原书 p.25 属 ch01c 页段）。为保证 proof 环境完整，以下译出该跨块句及其收尾，tr03 自「これと，(1.14) の形の Polyakov--Wiegmann の等式をあわせて」一句起接续，勿重复 ---"""
NEW_L1 = r"""% --- 命题 1.11 的证明起于 p.24 末行、续于 p.25 开头；为保证 proof 环境完整，本块已译至 p.25 的 ■ 处（ch01c 从 p.25「Wess--Zumino--Witten 模型本来の目的は…」接续，勿重复）---"""
sub("ch01b.tex", OLD_L1, NEW_L1, "L1 ch01b 尾注清理")

print("\n".join(log))
