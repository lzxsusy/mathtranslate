# 定理 2.14：超尖点、本质平方可积、一般表示在对应下的像

> `yao17/concept/llc-finer-properties` · 轨道 总览与主陈述 · 状态 dev

> **先自测**：除了定理 2.13 的五条公理，底本还给 LLC 补了哪三条更细的性质？它们各对应自守侧的哪一类表示？

## 一句话

rec_n 把超尖点送成不可约、把本质平方可积送成不可分解、把一般表示送成 ad 的 L 因子在 s=1 无极点。

## 定义

在定理 2.13 的 $\rec_n$ 之下：(1) $\pi\in\Repadm_G$ 不可约且超尖点，当且仅当 $\rec_n(\pi)$ 不可约；(2) $\pi$ 本质平方可积，当且仅当 $\rec_n(\pi)$ 不可分解；(3) $\pi$ 一般（generic），当且仅当 $L(\ad\circ\rec_n(\pi),s)$ 在 $s=1$ 处无极点。

**记号**：$\ad$ 指 $\GL_n$ 的伴随表示 $\mathfrak{gl}_n$，故 $\ad\circ\rec_n(\pi)$ 是 $W_K\times\SL_2$ 表示在 $\mathfrak{gl}_n$ 上的作用；底本记 $\rec$ 为 $r_n$（同为 $\rec_n$）。

## 要点（为什么需要它）

1. 这三条不是用来保证唯一性的公理（底本明说定理 2.13 的五条才是），而是「更精细的信息」：它们把自守侧的三类表示与 $\rec_n(\pi)$ 的三个结构性质（不可约、不可分解、$\ad$ 的 $L$ 因子无极点）一一对上。
2. (1) 与 (2) 的区别就是「不可约」与「不可分解」的区别：$\rec_n(\pi)$ 可以分解成若干块而仍不可约化；$\Sp_m(r)$ 正是这种块的模型。
3. (3) 的 $\ad$ 是 $\GL_n$ 的 Lie 代数，$L(\ad\circ\rho,s)$ 的极点位置读出 $\rho$ 里有没有「单值块」；$s=1$ 处的极点恰对应一般的自守侧失败（无 Whittaker 模型）。
4. 三条都能用 $N$ 的幂零性直接检验：$N=0$ 且 $\rho'$ 不可约给 (1)，$N$ 非零给 (2) 的「可分解」，$\mathfrak{gl}_n^{\rho'}$ 中不变向量的重数给 (3)。

## 核心公式

$$
$\pi\ \text{超尖点}\iff \rec_n(\pi)\ \text{不可约}$$\pi\ \text{本质平方可积}\iff \rec_n(\pi)\ \text{不可分解}$$\pi\ \text{一般}\iff L(\ad\circ\rec_n(\pi),s)\|_{s=1}\ \text{无极点}$
$$

$$
$\pi\ \text{本质平方可积}\iff \rec_n(\pi)\ \text{不可分解}$
$$

$$
$\pi\ \text{一般}\iff L(\ad\circ\rec_n(\pi),s)\|_{s=1}\ \text{无极点}$
$$

## 定理与证明（或缺口）

### 定理 2.14

在 $\rec_n$ 为 LLC 下，(1) 超尖点 $\leftrightarrow$ 不可约；(2) 本质平方可积 $\leftrightarrow$ 不可分解；(3) 一般 $\leftrightarrow$ $L(\ad\circ\rec_n(\pi),s)$ 在 $s=1$ 无极点。

> 证明状态：**cited**。底本不证，且把这三条「视为额外性质」；它们分别需要超尖点判据（§2.2）、本质平方可积的定义（§3.2）与 Whittaker 模型理论（§3.2.2）。

出处：`A §2.3.2 p.22`

## 常见误解

- 「不可分解」不等同于「不可约」：定理 2.14(2) 说的是 $\rec_n(\pi)$ 作为 $W_K\times\SL_2$ 表示不可分解，允许它有可约的 Jordan–Hölder 因子链。
- 定理 2.13 已把目标范畴限制在 Frobenius 半单对象上，所以 (1)(2) 的差别全落在 $N$ 上，而不是落在 $\rho'$ 的半单性上。

## 相关卡

[局部 Langlands 对应：定理 2.13 的五条性质](../concepts/llc-statement.md) · [本质 L^r、平方可积、缓增：定理 3.2、3.3 与推论 3.4](../concepts/square-integrable-tempered.md) · [一般（generic）表示、Whittaker 模型与定理 3.6](../concepts/generic-whittaker.md) · [超尖点表示：J_P(π)=0 与矩阵系数的紧支性](../concepts/jacquet-supercuspidal.md)

## 出处（印刷页）

- A p.22（A p.22）

> 说明：三条性质逐条取自 p.22 定理 2.14；key_points 中对「不可约 vs 不可分解」「$\ad$ 的极点读什么」的解释是我们的判断，底本未展开。
