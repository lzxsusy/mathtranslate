# Weil 群 W_K、惯性群、野惯性群与驯特征标

> `yao17/concept/weil-group` · 轨道 Weil–Deligne 侧 · 状态 dev

> **先自测**：底本怎么定义 W_K？驯特征标 t 与 l 进分圆特征标 χ_l 之间是什么关系？

## 一句话

W_K 是 I_K 与 Frobenius 整数幂的半直积；t 把 I_K/P_K 同构到 ∏_{l≠p} Z_l，共轭作用即分圆特征标。

## 定义

设 $K$ 是非阿基米德局部域，剩余特征 $p$，$q=\#k=p^f$，$G_K=\Gal(K^s/K)$。$W_K$ 由短正合列 $0\to I_K\to W_K\to\operatorname{Frob}^{\mathbb Z}\to 0$ 刻画，拓扑取成 $I_K$ 为开子群、$\operatorname{Frob}^{\mathbb Z}\cong\mathbb Z$ 离散——注意这不是从 $G_K$ 继承的子空间拓扑。野惯性 $P_K=G(K^s/K^t)$ 是 $I_K$ 唯一的 pro-$p$ Sylow 子群；驯特征标是 $t\colon I_K/P_K\xrightarrow{\sim}\prod_{l\neq p}\mathbb Z_l$，$\sigma\mapsto t(\sigma)$ 由 $\sigma(\varpi_K^{1/n})/\varpi_K^{1/n}=\zeta_n^{t(\sigma)}$ 确定（依赖单位根系统的选取）。

**记号**：$\varpi_K$ 是素元，$K^{\mathrm{nr}}=\bigcup_{p\nmid n}K(\zeta_n)$，$K^t=\bigcup_{p\nmid n}K^{\mathrm{nr}}(\varpi_K^{1/n})$；$t_l$ 是 $t$ 投到 $\mathbb Z_l$ 的分量。

## 要点（为什么需要它）

1. W_K 的拓扑是「人为」的：$I_K$ 开、$\operatorname{Frob}^{\mathbb Z}$ 离散，因此 W_K 不紧而只是局部紧；这一点决定了 W_K 的连续表示一定是「$I_K$ 上有限像 + Frobenius 可无限阶」，与 $G_K$ 的连续表示完全不同。
2. $P_K$ 是 pro-$p$ 群，故任何 $l\neq p$ 的 $\mathbb Z_l$-模上 $P_K$ 的像都平凡——这就是驯特征标商掉 $P_K$ 的全部理由。
3. $G_K$ 共轭作用保持 $P_K$（唯一 pro-$p$ Sylow），在每个 $\mathbb Z_l$ 分量上给出 $l$ 进分圆特征标：$t_l(\sigma\tau\sigma^{-1})=\chi_l(\sigma)t_l(\tau)$，即 $I_{K,l}/P_K\cong\mathbb Z_l(1)$。
4. 底本 Remark 给了公理化定义：W_K 由三元组 $(W_K,\iota,\{r_E\})$ 刻画，$\iota$ 像稠密、$r_E\colon C_E\xrightarrow{\sim}W_E^{\mathrm{ab}}$，非阿局部情形下 $\iota$ 就是自然包含、$r_E$ 来自局部类域论。

## 核心公式

$$
$0\to I_K\to W_K\to\operatorname{Frob}^{\mathbb Z}\to 0$$t\colon I_K/P_K\xrightarrow{\ \sim\ }\prod_{l\neq p}\mathbb Z_l,\qquad t_l\colon I_{K,l}/P_K\xrightarrow{\ \sim\ }\mathbb Z_l$$t_l(\sigma\tau\sigma^{-1})=\chi_l(\sigma)\,t_l(\tau)\quad(\sigma\in G_K,\ \tau\in I_{K,l})$
$$

$$
$t\colon I_K/P_K\xrightarrow{\ \sim\ }\prod_{l\neq p}\mathbb Z_l,\qquad t_l\colon I_{K,l}/P_K\xrightarrow{\ \sim\ }\mathbb Z_l$
$$

$$
$t_l(\sigma\tau\sigma^{-1})=\chi_l(\sigma)\,t_l(\tau)\quad(\sigma\in G_K,\ \tau\in I_{K,l})$
$$

## 常见误解

- $W_K\to G_K$ 的像稠密但不闭，故 W_K 的连续表示不一定给出 $G_K$ 的连续表示；把两者混同会丢掉「$I_K$ 上有限像」这一条。
- 驯特征标依赖单位根系统 $\{\zeta_n\}_{p\nmid n}$ 的选取；换一套 $\zeta_n$ 相当于乘一个 $\widehat{\mathbb Z}^{(p)}$ 中的单位，底本在 §1.2.2 明确说不同选取给出自然同构的 WD 函子。

## 相关卡

[Weil–Deligne 表示 (ρ, N) 及其基本性质](../concepts/wd-representation.md) · [Grothendieck 单值化定理、WD 函子与惯性类型](../concepts/wd-functor.md) · [φ-半单（Frobenius 半单）与引理 1.2](../concepts/frobenius-semisimple.md)

## 出处（印刷页）

- A p.2（A p.2）

> 说明：正合列、拓扑、$K^{\mathrm{nr}}$/$K^t$ 与 $t$ 的定义照 p.2 的 1.1.1–1.1.2；「$W_K$ 的拓扑是人为的」这一句解释是我们的判断。
