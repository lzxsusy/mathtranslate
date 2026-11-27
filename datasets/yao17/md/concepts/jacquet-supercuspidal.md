# 超尖点表示：J_P(π)=0 与矩阵系数的紧支性

> `yao17/concept/jacquet-supercuspidal` · 轨道 自守侧 · 状态 dev

> **先自测**：为什么「所有真抛物上的 Jacquet 函子为零」能刻画超尖点？它与「矩阵系数紧支」的等价是怎么来的？

## 一句话

π 超尖点指对所有真抛物 P 有 J_P(π)=0；等价地所有矩阵系数在 G⁰ 上紧支（模中心紧支）。它们是容许表示的积木。

## 定义

设 $(\pi,V)\in\Rep^{\mathrm{adm}}_G$ 不可约。$\pi$ 称超尖点（supercuspidal），若对任一真抛物 $P<G$ 有 $J_P^G(\pi)=0$。引理 2.10：任一不可约 $\pi$ 或超尖点，或是某个 $I_P^G(\sigma)$ 的子表示，$P$ 真抛物、$\sigma$ 为 $L$ 的不可约超尖点表示。引理 2.11：$\pi$ 不可约容许，则 TFAE：(1) $\pi$ 超尖点；(2) 每个矩阵系数 $C_{v,\lambda}(g)=\lambda(\pi(g)v)$ 在 $G^0=\{g:\det g\in\mathcal O_K^\times\}$ 上紧支；(3) 每个矩阵系数模中心 $Z$ 紧支。若 $\pi^\vee$ 也不可约，还可加 (4) 存在一个模中心紧支的矩阵系数。

**记号**：$G^0=\{g\in\GL_n(K):\det g\in\mathcal O_K^\times\}$，$ZG^0$ 在 $G$ 中有限指数（$\GL_n$ 时为 $n$）；引理 2.12：对紧开 $K_0$，带 $K_0$-固定向量的不可约超尖点表示只有有限多个同构类。

## 要点（为什么需要它）

1. 引理 2.10 的证明就是一个伴随：$\pi$ 非超尖点 $\Rightarrow$ 存在极小抛物 $P$ 使 $J_P\pi\neq0$；取不可约商 $\sigma$，则 $0\neq\Hom_L(J_P\pi,\sigma)=\Hom_G(\pi,I_P\sigma)$，即 $\pi\hookrightarrow I_P\sigma$，且可证 $\sigma$ 超尖点。
2. 于是「超尖点」= 不为任何真抛物诱导的子表示，这正是「积木」的意思：所有不可约表示都由超尖点经诱导（以及取子商）搭出来（§3 的 BZ 分类把这个直觉变成定理）。
3. 矩阵系数刻画（引理 2.11）把「超尖点」变成可检验的分析条件：$\pi$ 超尖点 $\iff$ 其矩阵系数模中心紧支。底本脚注说这「也许就是超尖点性最初的定义」。
4. 引理 2.12（带 $K_0$-固定向量的超尖点表示只有有限多个）是把超尖点侧「局部有限」的关鍵：它保证了 §3.3 的 BZ 参数化在每一层都是有限集。

## 核心公式

$$
$\pi\ \text{超尖点}\iff J_P^G(\pi)=0\ \ \forall P\lneq G$$0\neq\Hom_L(J_P\pi,\sigma)=\Hom_G(\pi,I_P\sigma)\quad\Longrightarrow\quad \pi\hookrightarrow I_P^G\sigma$$\pi\ \text{超尖点}\iff C_{v,\lambda}\ \text{在}\ G^0\ \text{上紧支}\iff C_{v,\lambda}\ \text{模}\ Z\ \text{紧支}$
$$

$$
$0\neq\Hom_L(J_P\pi,\sigma)=\Hom_G(\pi,I_P\sigma)\quad\Longrightarrow\quad \pi\hookrightarrow I_P^G\sigma$
$$

$$
$\pi\ \text{超尖点}\iff C_{v,\lambda}\ \text{在}\ G^0\ \text{上紧支}\iff C_{v,\lambda}\ \text{模}\ Z\ \text{紧支}$
$$

## 定理与证明（或缺口）

### 引理 2.10（不可约表示或超尖点或嵌入抛物诱导）

不可约 $\pi$ 或超尖点，或是某真抛物 $P$ 上某不可约超尖点 $\sigma$ 的 $I_P^G(\sigma)$ 的子表示。

1. 若 $\pi$ 非超尖点，取极小抛物 $P$ 使 $J_P\pi\neq0$；$J_P\pi$ 有限长，取不可约商 $\sigma$。
   - *为什么*：非超尖点的定义保证这样的 $P$ 存在；$J_P$ 保有限长（§2.2.2 Remark (3)）。
2. 由伴随 $\tilde J\dashv\tilde I$ 得 $0\neq\Hom_L(J_P\pi,\sigma)=\Hom_G(\pi,I_P\sigma)$，故 $\pi$ 嵌入 $I_P\sigma$。
   - *为什么*：同构的左边非零推出右边非零，而不为零的 $G$-同态在不可约 $\pi$ 上必单。
3. 由 $P$ 极小可证 $\sigma$ 超尖点。
   - *为什么*：底本只写「由构造可证」（By construction one can show），未展开；这是本引理唯一的缺口。

出处：`A §2.2.4 p.19–p.20`

## 常见误解

- 定义里要求「所有真抛物」，而引理 2.11 的紧支性是在 $G^0$（或模中心）上；这两个条件等价需要 $ZG^0$ 有限指数这一结构事实，不能逐字推广到任意约化群。
- 引理 2.11 的第 (4) 条（存在一个模中心紧支的矩阵系数）额外要求 $\pi^\vee$ 不可约，底本明确标了这个条件，不能省。

## 相关卡

[抛物诱导、Jacquet 函子与模特征标 δ 的正规化](../concepts/parabolic-induction.md) · [定理 2.5（光滑不可约 ⇒ 容许）、引理 2.6 与 Harish-Chandra 特征标](../concepts/harish-chandra-character.md) · [超尖点判据：π 非超尖点 ⇒ 可嵌入某真抛物诱导（引理 2.10 的证明链）](../derivations/supercuspidal-criterion.md) · [超尖点支撑与 Steinberg 表示 St_n](../concepts/supercuspidal-support.md)

## 出处（印刷页）

- A p.19–20（A p.19）

> 说明：超尖点定义、引理 2.10 的证明、引理 2.11 的 (1)–(4)、引理 2.12 与 2.2.4 末的注记取自 p.19–p.20；「积木」的解读依据同一页的 Supercuspidal representations form building blocks。
