# 定理 3.1：Bernstein–Zelevinsky 对 GL_n 容许表示的七条分类

> `yao17/concept/bz-classification` · 轨道 总览与主陈述 · 状态 dev

> **先自测**：定理 3.1 的七条各说了什么？为什么它可以被读成「GL_n 的不可约表示由段的有序组唯一决定」？

## 一句话

用段 Δ 造出 Q(Δ) 与 Z(Δ)，任何不可约表示唯一地是 Q(Δ_1,…,Δ_r)，且 Q 侧对 (∗)-置换不变。

## 定义

$\Delta=\Delta(\pi,m)=[\pi,\pi(1),\dots,\pi(m-1)]$ 是段，$\pi(\Delta)=\pi_1\times\dots\times\pi_m$ 是抛物诱导。定理 3.1：(1) $\pi(\Delta)$ 的长度为 $2^{m-1}$；(2) 有限长段 $\Delta$ 的 $\pi(\Delta)$ 有唯一不可约子表示 $Z(\Delta)$ 与唯一不可约商 $Q(\Delta)$；(3) 满足 $(\ast)$ 的 $\Delta_1,\dots,\Delta_r$，$Q(\Delta_1)\times\dots\times Q(\Delta_r)$ 有唯一不可约商 $Q(\Delta_1,\dots,\Delta_r)$，且在 $(\ast)$-置换下不变；(4) 任一不可约 $\pi\cong Q(\Delta_1,\dots,\Delta_r)$，$n=\sum n_im_i$，且该段组在 $(\ast)$-置换下唯一；(5) $Q(\Delta_1)\times\dots\times Q(\Delta_r)$ 不可约当且仅当任两段不 linked；(6) $Q(\Delta^\vee)=Q(\Delta)^\vee$；(7) $Z$ 侧有对偶的 (3)–(6)。

**记号**：$\pi(s)$ 是 $\pi$ 用 $|\det|^s$ 的扭转；$\Asc_n$ 是超尖点表示按「$\pi\le\pi(s)$，$s\in\mathbb Z_{\ge 0}$」排序的偏序集；(∗) 条件：对 $i<j$，$\Delta_i$ 不 precede $\Delta_j$。

## 要点（为什么需要它）

1. 整条定理的枢纽是 (2)：$\pi(\Delta)$ 有唯一不可约商 $Q(\Delta)$，这才是可乘的「原子」；(1) 的长度 $2^{m-1}$ 说明一个段诱导出来的是 $2^{m-1}$ 个 Jordan–Hölder 因子，故 (5) 的不可约判据（无 linked）是极强条件。
2. (3)(4) 合起来说：不可约表示与「满足 $(\ast)$ 的段组”一一对应，而 $(\ast)$-置换不改变 $Q$——所以真正的不变量是无序段组，注记里正是这么说的。
3. (6)(7) 是对偶性：取反变对偶把 $Q$ 侧换成 $Q$ 侧（$\Delta^\vee=[\pi(m-1)^\vee,\dots,\pi^\vee]$），而 $Z$ 侧的自反性给出 Buchsbaum 型对偶陈述。
4. Grothendieck 群 $R_K=\oplus_nR_n(K)$ 用 $[\pi_1]\cdot[\pi_2]=[\pi_1\times\pi_2]$ 成为分次交换环，$Q(\Delta)\mapsto Z(\Delta)$ 在其上给出对合——这是底本注记里的第二条结构性结论。

## 核心公式

$$
$\Delta(\pi,m)=[\pi,\pi(1),\dots,\pi(m-1)],\qquad \pi(\Delta)=\pi_1\times\dots\times\pi_m=I_{\GL_{mn}}^{P(n,\dots,n)}(\pi_1\otimes\dots\otimes\pi_m)$$\operatorname{length}\pi(\Delta)=2^{m-1}$$\pi\cong Q(\Delta_1,\dots,\Delta_r)\iff \text{段组在 }(\ast)\text{-置换下唯一}$$\Delta^\vee=[\pi(m-1)^\vee,\dots,\pi^\vee],\qquad Q(\Delta_1^\vee,\dots,\Delta_r^\vee)=Q(\Delta_1,\dots,\Delta_r)^\vee$
$$

$$
$\operatorname{length}\pi(\Delta)=2^{m-1}$
$$

$$
$\pi\cong Q(\Delta_1,\dots,\Delta_r)\iff \text{段组在 }(\ast)\text{-置换下唯一}$
$$

$$
$\Delta^\vee=[\pi(m-1)^\vee,\dots,\pi^\vee],\qquad Q(\Delta_1^\vee,\dots,\Delta_r^\vee)=Q(\Delta_1,\dots,\Delta_r)^\vee$
$$

## 定理与证明（或缺口）

### 定理 3.1（Bernstein–Zelevinsky）

上述 (1)–(7) 全部成立。

> 证明状态：**cited**。底本只陈述；(1) 来自 BZ 的「长度 = 段长减一的 2 的幂」，(2)–(7) 来自 BZ 的 Langlands 型分类与几何引理，底本未给证明。

出处：`A §3.1.3 p.24`

## 常见误解

- $(\ast)$ 条件只对 $n_i=n_j$ 的段对起作用（段不 linked 时该条为空），所以它看起来「宽松」，但 (3) 的商 $Q(\Delta_1,\dots,\Delta_r)$ 仍依赖顺序给出唯一的不可约商，不能把顺序随便换。
- $Q(\Delta)$ 是商、$Z(\Delta)$ 是子表示，二者一般不同构；只有当 $\Delta$ 长度为 1（即 $\pi$ 本身超尖点）时 $Q=Z=\pi$。
- (5) 的「不可约」是在问 $Q(\Delta_1)\times\dots\times Q(\Delta_r)$ 这个抛物诱导本身，而不是它的某个商。

## 相关卡

[Zelevinsky 段 Δ(π,m)、linked/precedes 与 (∗) 条件](../concepts/zelevinsky-segment.md) · [超尖点支撑与 Steinberg 表示 St_n](../concepts/supercuspidal-support.md) · [局部 Langlands 对应：定理 2.13 的五条性质](../concepts/llc-statement.md) · [把 LLC 从超尖点归纳到一般表示：rec_n = ⊕ Sp_{m_i} ∘ rec_{n_i}](../derivations/induction-to-supercuspidal.md)

## 出处（印刷页）

- A p.24–25（A p.24）

> 说明：(1)–(7) 逐条照抄 p.24 定理 3.1；$R_K$ 的环结构与对合见 p.24 第二条 Remark；key_points 中「枢纽是 (2)」「(∗) 只对同维段对起作用」是我们的判断。
