# 定理 2.5（光滑不可约 ⇒ 容许）、引理 2.6 与 Harish-Chandra 特征标

> `yao17/concept/harish-chandra-character` · 轨道 自守侧 · 状态 dev

> **先自测**：「光滑 + 不可约 ⇒ 容许」这条定理为什么只能用 Jacquet 函子证？Harish-Chandra 特征标 χ_π 在什么集合上局部常值，椭圆表示又怎么定义？

## 一句话

光滑不可约必容许；GL_n 的光滑不可约表示或一维或无穷维，一维者必为 χ∘det；Θ_π(f)=Tr π(f) 由正则半单处的局部常值函数 χ_π 表示。

## 定义

定理 2.5：$G$ 的光滑不可约表示必容许（证明用 Jacquet 函子把 $\pi$ 嵌入容许（超尖点）表示的抛物诱导，底本略）。引理 2.6：$G=\GL_n(K)$ 的光滑不可约表示或一维或无穷维；一维者必形如 $\chi\circ\det$。引理 2.7：两两不同构的不可约容许表示的特征标 $\Theta_{\pi_i}$ 线性无关。定理 2.8（Harish-Chandra；正特征时属 Lemaire）：存在局部可积函数 $\chi_\pi$，在正则半单集 $G^{\mathrm{r.s.}}$ 上局部常值、在补集上为 0，使 $\Theta_\pi(f)=\int_Gf(g)\chi_\pi(g)dg$。定义：$\pi$ 椭圆，若 $\chi_\pi$ 在正则椭圆集 $G^{\mathrm{r.e.}}$ 上不恒为 0。

**记号**：$\Theta_\pi\colon H(G)\to\mathbb C$，$f\mapsto\Tr\pi(f)$；$g$ 正则半单指特征多项式 $P_g$ 在 $K$ 上可分；正则椭圆指 $P_g$ 不可约。每本质平方可积表示都是椭圆的。

## 要点（为什么需要它）

1. 定理 2.5 的证明被底本整段略去，理由很实在：它需要 Jacquet 函子 + 超尖点表示的存在性（§2.2），而这两样在 §2.1 还没讲；底本还特意在脚注里提醒「不能反过来用定理 2.5 去证 Schur 引理，因为定理 2.5 的证明本身用 Schur 引理」。
2. 引理 2.6 的论证只用了 $G$ 的结构：$\ker\pi$ 开，含 $1+\varpi^m\GL_n(\mathcal O_K)$，共轭后含上三角幂幺群 $U$，正规性给出 $\SL_n(K)\subset\ker\pi$，故 $\pi$ 过 $\det$。
3. 引理 2.7（特征标线性无关）是 Harish-Chandra 特征标理论的基本引理，配合定理 2.8 就把「表示」变成「正则半单集上的函数」，这是 Jacquet–Langlands 与迹公式的出发点。
4. 椭圆表示的定义刻意用「$\chi_\pi$ 在 $G^{\mathrm{r.e.}}$ 上不恒为 0」而不是「矩阵系数紧支」，因为后者只在超尖点时成立（引理 2.11）；椭圆是比超尖点更宽、比一般更窄的类。

## 核心公式

$$
$\Theta_\pi(f)=\Tr\pi(f)=\int_Gf(g)\chi_\pi(g)\,dg,\qquad \chi_\pi\ \text{在}\ G^{\mathrm{r.s.}}\ \text{上局部常值}$$\pi\ \text{光滑不可约}\ \Longrightarrow\ \pi\ \text{容许}$$\pi\ \text{一维}\ \Longleftrightarrow\ \pi\cong\chi\circ\det$
$$

$$
$\pi\ \text{光滑不可约}\ \Longrightarrow\ \pi\ \text{容许}$
$$

$$
$\pi\ \text{一维}\ \Longleftrightarrow\ \pi\cong\chi\circ\det$
$$

## 定理与证明（或缺口）

### 定理 2.5（光滑不可约表示容许）

$G$ 的任一光滑不可约表示都是容许的。

> 证明状态：**cited**。底本整段略去，只说证明用 Jacquet 函子把 $\pi$ 嵌入容许（超尖点）表示的抛物诱导，并引 Jacquet 的处理或 Bernstein–Zelevinsky。

出处：`A §2.1.8 p.15`

### 定理 2.8（Harish-Chandra 特征标）

存在局部可积的 $\chi_\pi$，在 $G^{\mathrm{r.s.}}$ 上局部常值、补集为 0，且 $\Theta_\pi(f)=\int_Gf\chi_\pi$。

> 证明状态：**cited**。底本只陈述（称 $K$ 特征 0 时属 Harish-Chandra、正特征属 Lemaire），未给证明；前一段只给了 $\Theta_\pi$ 的显式计算式。

出处：`A §2.1.9 p.16`

## 常见误解

- 定理 2.8 里的 $\chi_\pi$ 只在正则半单集上局部常值，在奇异元素上可以爆掉；把它当成 $G$ 上的连续函数会出错。
- 「椭圆」不等于「超尖点」：超尖点 $\Rightarrow$ 椭圆，反之不成立；底本只说「每本质平方可积表示是椭圆的」。

## 相关卡

[光滑表示、容许表示与反变对偶](../concepts/smooth-admissible.md) · [Hecke 代数 H(G)、双陪集子代数与 「光滑表示 ≃ 非退化 Hecke 模」](../concepts/hecke-modules.md) · [超尖点表示：J_P(π)=0 与矩阵系数的紧支性](../concepts/jacquet-supercuspidal.md)

## 出处（印刷页）

- A p.15–16（A p.16）

> 说明：定理 2.5、引理 2.6/2.7、定理 2.8 与椭圆定义照 p.15–p.16；「椭圆比超尖点宽」一句依据 p.16 的 Remark (2)。
