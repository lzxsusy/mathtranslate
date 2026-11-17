---
id: csw/concept/gauss-law-constraint
type: concept
track: B
---

# 高斯定律作为第一类约束

> $A_0$ 是拉格朗日乘子，对它的变分给出 $\varepsilon^{ij}F_{ij}=0$；这条约束是第一类约束，生成规范变换。

**问题**：为什么 $A_0=0$ 不是规范选择而是约束？约束为什么是第一类？

## 定义

在 $M=\Sigma\times\mathbb{R}$ 上取 $A=A_0dt+A_i dx^i$。作用量对 $A_0$ 不含时间导数，$A_0$ 是拉格朗日乘子；对 $A_0$ 变分得约束 $\varepsilon^{ij}F^a_{ij}=0$，即 $F=0$。约束函数的泊松括号（在约束面上）正比于约束本身，故为第一类。

*记号*：$i,j=1,2$ 是 $\Sigma$ 上的指标；$\varepsilon^{ij}$ 是 $\Sigma$ 的面积形式；$a$ 是 Lie 代数指标。

## 要点

- 作用量对 $A_0$ 线性：$\int A_0\,\varepsilon^{ij}F_{ij}$，所以 $A_0$ 是乘子，不是动力学变量。
- 约束 $F=0$ 在二维曲面 $\Sigma$ 上只有一个独立分量（$\varepsilon^{ij}F_{ij}$），不是三个。
- 约束是第一类：它的泊松括号生成规范变换，因此不能直接当方程解，而要做辛商。
- 经典处理分两步：先限制到 $F=0$（约束面），再按规范群取商。
- 量子化时不能先解约束再量子化，也不能先量子化再解约束——两种顺序给出同构的 Hilbert 空间（Dirac 方案与辛商等价），但技术难度不同。

## 关键公式

- $S=\frac{k}{8\pi}\int dt\int_\Sigma\varepsilon^{ij}\operatorname{Tr}A_i\partial_tA_j+\int A_0\,\varepsilon^{ij}F_{ij}$
- $\varepsilon^{ij}F^a_{ij}=0$
- $\{G(\epsilon),G(\epsilon')\}=G([\epsilon,\epsilon'])$

## 约束生成规范变换

令 $G(\epsilon)=\int_\Sigma\varepsilon^{ij}\operatorname{Tr}(\epsilon F_{ij})$。在泊松括号下，$\{G(\epsilon),A_i\}=D_i\epsilon$，即约束生成无穷小规范变换；约束之间闭合，故为第一类。

**证明**：

1. 由泊松括号 $\{A_i^a(x),A_j^b(y)\}=\frac{4\pi}{k}\varepsilon_{ij}\delta^{ab}\delta^2(x-y)$ 计算 $\{G(\epsilon),A_k\}$。 *（辛形式给出基本括号，见 symplectic-quotient 卡。）*
2. 用 $\delta F_{ij}=D_i\delta A_j-D_j\delta A_i$ 与反对称性 $\varepsilon^{ij}$，只剩一项 $\varepsilon^{ij}D_i\epsilon$，即 $D_i\epsilon$（二维）。 *（$\varepsilon^{ij}$ 把 $D_i\delta A_j$ 的对称部分杀掉。）*
3. 两个约束的括号给出 $\{G(\epsilon),G(\eta)\}=G([\epsilon,\eta])$，仍是约束，故第一类。 *（结构常数反对称，闭合在约束理想内。）*

## 陷阱

- 不要写 $F_{ij}=0$ 三个分量：二维只有一个独立分量；写成三维会多出两个虚假约束。
- 约束是第一类意味着规范不是物理自由度，必须商掉；第二类约束才用 Dirac 括号。
- $A_0=0$ 只是把乘子固定，不是解掉约束；固定 $A_0$ 后约束仍在。

## 相关卡片

- [symplectic-quotient](../concepts/symplectic-quotient.md)
- [flat-connection-moduli](../concepts/flat-connection-moduli.md)
- [cs-action](../concepts/cs-action.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.1 The Holomorphic Viewpoint（正则形式），印刷页 [366, 367] / PDF 页 [16, 17]（witten1989/sections/s04-canonical.tex（式 3.1–3.3））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
