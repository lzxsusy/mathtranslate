# 有效除子的斜率

> `grassmann/concept/slope-of-effective-divisor` · 轨道 2 · Koszul 上同调 · 状态 draft

> **先自测**：为什么 $\mathcal{K}_{10}$ 的斜率 $7$ 低于 $78/11$，就足以推翻斜率猜想？

## 一句话

把 $\overline{\mathcal{M}}_g$ 上的有效除子写成 $a\lambda$ 与边界除子的组合，取最小的比值 $a/b$；斜率猜想预言它不小于 $6+12/(g+1)$，而 Koszul 闭链正是造反例的机器。

## 定义

$\overline{\mathcal{M}}_g$ 上有效除子 $D$ 的**斜率** $s(D)$ 定义为：使类 $a\lambda-b(\delta_0+\dots+\delta_{[g/2]})-[D]\in\Pic(\overline{\mathcal{M}}_g)$ 成为边界除子的有效 $\mathbb{Q}$-线性组合的最小有理数 $a/b$（其中 $a,b\ge0$）。斜率猜想预言 $s(\overline{\mathcal{M}}_g):=\inf_{D\in\mathrm{Eff}(\overline{\mathcal{M}}_g)}s(D)\ge6+\frac{12}{g+1}$，等号成立当且仅当 $g+1$ 是合数。

**记号约定**：$\lambda$ 为 Hodge 除子，$\delta_i$ 为边界除子；$\mathrm{Eff}(\overline{\mathcal{M}}_g)$ 为有效除子锥。

## 要点（为什么需要它）

- 斜率越小，除子越「负」：$s(D)<6+12/(g+1)$ 就直接违反猜想，因为下界是对所有有效除子取的。
- 量 $6+12/(g+1)$ 正是 Brill–Noether 除子（存在时）的斜率：$\mathcal{M}^r_{g,d}$ 的类为 $c((g+3)\lambda-\frac{g+1}{6}\delta_0-\sum i(g-i)\delta_i)$，比值即 $6(g+3)/(g+1)$。
- $g=10$ 时下界为 $6+12/11=78/11\approx7.0909$，而 $s(\overline{\mathcal{K}}_{10})=7$，差约 $0.09$，是猜想的第一个反例。
- Koszul 刻画把 $\mathcal{K}_{10}$ 写成「存在 $L\in W^4_{12}$ 使 $K_{0,2}(C,L)\neq0$」，于是可以搬到 $\overline{\mathcal{M}}_{10}$ 上算虚类，完全绕开 $K3$ 曲面。

## 关键公式

$$
s(D)=a/b,\qquad a\lambda-b(\delta_0+\dots+\delta_{[g/2]})-[D]\ \text{有效}
$$

$$
s(\overline{\mathcal{M}}_g)\ge 6+\frac{12}{g+1}
$$

$$
s(\overline{\mathcal{K}}_{10})=7<\frac{78}{11}
$$

## 定理与证明（或缺口）

### 定理 3.1（Brill–Noether 除子的类与斜率）

设 $\rho(g,r,d)=-1$。则 $\mathcal{M}^r_{g,d}:=\sigma_*(\mathfrak{G}^r_d)$ 是 $\mathcal{M}_g$ 上的不可约除子，其类为 $c_{g,d,r}\bigl((g+3)\lambda-\frac{g+1}{6}\delta_0-\sum_{i=1}^{[g/2]}i(g-i)\delta_i\bigr)$，斜率为 $6+\frac{12}{g+1}$。

**证明状态：只引出处，原书不重证**


出处：中译 p.38（定理 3.1，引 Harris–Mumford）

### $\mathcal{K}_{10}$ 是斜率猜想的反例

$\mathcal{K}_{10}=\{[C]\in\mathcal{M}_{10}:C\ \text{位于某个 }K3\text{ 曲面上}\}$，等价地 $\mathcal{K}_{10}=\{[C]:\exists L\in W^4_{12}(C),\ K_{0,2}(C,L)\neq0\}$。则 $s(\overline{\mathcal{K}}_{10})=7<78/11$，故 $\overline{\mathcal{K}}_{10}$ 是 $\overline{\mathcal{M}}_{10}$ 上违背斜率猜想的有效除子。

**证明状态：提纲（有缺口）**


> **缺口**：原文只引用 [FaPo05] 的类计算，没有在正文推导 $\overline{\mathcal{K}}_{10}$ 的类；这里能核对的只有数值 $7$ 与下界 $78/11=7.\overline{09}$ 的比较，以及「$K3$ 曲面上的曲线带 $g^4_{12}$」这一步。


出处：中译 p.32（§1，引 Farkas–Popa）

## 易错点

- 斜率定义要求余项 $a\lambda-b\delta-[D]$ 是**边界**除子的有效组合，不是任意有效组合；放宽成任意除子会把所有斜率都算成 $0$。
- 把 $s(D)$ 与 $D$ 的次数混为一谈：只有 $\lambda$ 与 $\delta$ 的系数比才是斜率，绝对大小无关。
- $6+12/(g+1)$ 是 Brill–Noether 除子的斜率，不是「所有除子的最小斜率」；猜想说它是下界，且 $g+1$ 合数时取等。
- 反例的存在不推翻「下界」的全部内容：$s(\overline{\mathcal{K}}_{10})=7$ 说明下界至少要下调，但斜率猜想的一般形式是否对每个 $g$ 都失败仍是开放问题。

## 相关卡

- [Koszul 闭链与退化轨迹](../concepts/koszul-cycle.md)
- [Brill–Noether 数 $\beta$](../concepts/brill-noether-number.md)
- [极小合冲猜想](../concepts/minimal-syzygy-conjecture.md)
- [$g=10$、$(2,12,4)$ 的 $d_0$（例 7.5）](../examples/example-genus-10-d0.md)

## 出处

- ch2 §1 斜率与斜率猜想；中译 p.32（英文 PDF p.36），源码 `chapters/ch02.tex:77`
- ch2 §1 $\mathcal{K}_{10}$ 反例；中译 p.33（英文 PDF p.37），源码 `chapters/ch02.tex:85`
