---
id: csw/concept/polarization
type: concept
track: C
---

# 极化

> 在复化切丛里选一个拉格朗日、可积且维数为 $n$ 的子丛 $P$，把“沿 $P$ 协变常数”的截面当作量子态；它把 $2n$ 个变量砍成 $n$ 个。

**问题**：预量子化的 Hilbert 空间为什么太大？极化的三条条件各自排除什么？

## 定义

辛流形 $(M,\omega)$ 的极化是复化切丛 $T_{\mathbb{C}}M$ 的一个子丛 $P$，满足：①拉格朗日性 $\omega|_P=0$；②可积性（$P$ 的截面在 Lie 括号下封闭）；③$\dim_{\mathbb{C}}P=\frac12\dim M$。量子态定义为沿 $P$ 协变常数的截面：$\nabla_Xs=0$ 对所有 $X\in\Gamma(P)$。Kähler 情形取 $P=T^{0,1}M$，条件是“全纯”，量子态即全纯截面。

*记号*：$P$ 常记作 $\mathcal{P}$；$\Gamma_P(M,\cL)$ 表示 $P$-极化截面空间，$\cH_P=\Gamma_P(M,\cL)$。

## 要点

- 三条条件缺一不可：拉格朗日性保证沿 $P$ 的协变导数是“半截”的；可积性保证有足够多的解；维数条件保证砍掉恰好一半。
- 实极化对应“位置空间或动量空间”，解只依赖一半坐标；Kähler 极化对应“全纯”，解是全纯截面。
- 极化不是规范选择，它是量子化方案的一部分：不同的极化给出同构的 Hilbert 空间（BKS 配对），但计算难度不同。
- 在紧相空间上不能用“$q$ 与 $p$ 分离”的实极化（$q$ 或 $p$ 无界），Kähler 极化是自然选择。
- 半形式修正把截面从 $\cL$ 换成 $\cL\otimes K^{1/2}$，这一步与极化独立。

## 关键公式

- $\omega|_P=0,\quad[P,P]\subset P,\quad\dim_{\mathbb{C}}P=\tfrac12\dim M$
- $\nabla_Xs=0\ (X\in P)$
- $P=T^{0,1}M\Longrightarrow s$ 全纯

## Kähler 极化的量子态空间

在紧 Kähler 流形 $(M,\omega)$ 上取 $P=T^{0,1}M$，则 $P$-极化截面就是 $\cL$ 的全纯截面，$\cH_P=H^0(M,\cL)$，且 $\dim_{\mathbb{C}}\cH_P<\infty$。

**证明**：

1. $P=T^{0,1}M$ 时，$\nabla_Xs=0$ 对 $X=\bar\partial/\partial\bar z^k$ 即 $\bar\partial s=0$（用联络的 $(0,1)$ 部分刻画）。 *（Kähler 情形下相容联络的 $(0,1)$ 部分就是 $\bar\partial$ 加上线丛的联络。）*
2. $\bar\partial s=0$ 的解正是全纯截面；$\cL$ 正（$c_1(\cL)$ 为 Kähler 类）时 $H^0$ 有限维。 *（椭圆算子的核有限维（Hodge 理论）。）*
3. 故 $\cH_P=H^0(M,\cL)$，维数有限。 *（紧性给出有限维。）*

## 陷阱

- 不要以为“任意复结构都给极化”：$P$ 必须可积，$T^{0,1}$ 只在复结构可积时才对。
- 实极化在紧流形上常常不存在（叶空间非 Hausdorff），这是必须用 Kähler 极化的原因。
- 极化的选择影响“哪个空间与 $J$ 无关”的表述：严格说只有射影化后的空间典范。

## 相关卡片

- [prequantization-determinant-line](../concepts/prequantization-determinant-line.md)
- [holomorphic-sections](../concepts/holomorphic-sections.md)
- [half-form-correction](../concepts/half-form-correction.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.1 The Holomorphic Viewpoint（极化），印刷页 [367, 368] / PDF 页 [17, 18]（witten1989/sections/s04-canonical.tex（§3.1））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
