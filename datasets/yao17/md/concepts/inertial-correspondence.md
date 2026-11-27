# 惯性对应：Bernstein 中心 ↔ Weil–Deligne 惯性类型（引理 4.3–4.5）

> `yao17/concept/inertial-correspondence` · 轨道 惯性 Langlands 与类型 · 状态 dev

> **先自测**：为什么 Bernstein 中心能被 Weil–Deligne 惯性类型索引？引理 4.5 里 generic 这个条件为什么删不掉？

## 一句话

π 与 π′ 同 Bernstein 分量 ⇔ rec(π)|I_K ≅ rec(π′)|I_K；generic 时更强：同一 Galois 惯性类型 ⇒ π|K ≅ π′|K。

## 定义

引理 4.3：$H\triangleleft G$、$G/H$ 交换，$\rho_1,\rho_2$ 不可约有限维且 $\rho_1|_H\cong\rho_2|_H$，则存在特征标 $\psi\colon G/H\to\mathbb C^\times$ 使 $\rho_2\cong\rho_1\otimes\psi$；注：只需 $\Hom_H(\rho_1,\rho_2)\neq0$。引理 4.4：$\pi,\pi'$ 在同一个 Bernstein 分量 $R(L,\sigma)(G)$ 中 $\iff$ 其 LLC 像的底层 $W_K$ 表示满足 $\rec_n(\pi)|_{I_K}\cong\rec_n(\pi')|_{I_K}$——即 Bernstein 中心 $\mathcal B(\GL_n)$ 由 Weil–Deligne 惯性类型索引。引理 4.5：$\pi,\pi'$ 一般不可约且 $r_n(\pi)|_{I_K}\cong r_n(\pi')|_{I_K}$（$r_n=\WD^{-1}\circ\rec_n$），则 $\pi|_K\cong\pi'|_K$。

**记号**：$K$ 在此指 $\GL_n(\mathcal O_K)$（底本用同一字母，译本改用 $\mathcal K$ 区分）；$\WD$ 是推论 1.7 的函子；引理 4.5 的证明用 Iwasawa 分解与 Mackey 分解 $ (\Ind_P^{\GL_n(K)}\sigma)|_K=\Ind_{P\cap K}^{K}(\sigma|_{P\cap K})$。

## 要点（为什么需要它）

1. 引理 4.4 的证明把 BZ 分类代进去：$\pi=Q(\Delta_1,\dots,\Delta_r)$ 给出 $L=\prod\GL_{n_i}(K)^{m_i}$、$\sigma=\bigotimes_{i,j}\pi_i|\cdot|^j$，而 $\rec_n(\pi)=\bigoplus\Sp_{m_i}(\rec_{n_i}(\pi_i))$，限制到 $I_K$ 得 $\bigoplus\rec_{n_i}(\pi_i)^{m_i}|_{I_K}$——于是只剩超尖点情形，而那正由引理 4.3（取 $H=I_K$、$G=W_K$、$G/H\cong\mathbb Z$ 交换）给出。
2. 引理 4.3 的注（只需 $\Hom_H(\rho_1,\rho_2)\neq0$）在这里是关键：$\bigoplus\rec_{n_i}(\pi_i)^{m_i}$ 与另一侧同构是「和」层面的，要逐个分量分离就得反复用这条注，底本在证明末尾明确点了这一步。
3. 引理 4.5 用 Iwasawa 与 Mackey 把「$\pi|_K$」化成「$P\cap K$ 上的诱导」，再比较 $\Sp_{m_i}$ 的类型；它说的比 4.4 强：不只同分量，而是限制到 $K$ 后完全同构。
4. generic 条件不能删（底本 Remark）：$\GL_2$ 中 $\mathrm{triv}$ 与 $\St_2$ 同属一个 Bernstein 分量（都来自 $\{\chi,\chi\}$ 型支撑），但 $\mathrm{triv}|_K$ 与 $\St_2|_K$ 不同构——非 generic 的那些表示在 $K$ 上的型会把它们区分开。

## 核心公式

$$
$\rho_1|_H\cong\rho_2|_H,\ G/H\ \text{交换}\ \Longrightarrow\ \rho_2\cong\rho_1\otimes\psi$$\pi,\pi'\ \text{同 Bernstein 分量}\iff \rec_n(\pi)|_{I_K}\cong\rec_n(\pi')|_{I_K}$$\pi,\pi'\ \text{generic},\ r_n(\pi)|_{I_K}\cong r_n(\pi')|_{I_K}\ \Longrightarrow\ \pi|_K\cong\pi'|_K$$(\Ind_P^{\GL_n(K)}\sigma)|_K=\Ind_{P\cap K}^{K}(\sigma|_{P\cap K})$
$$

$$
$\pi,\pi'\ \text{同 Bernstein 分量}\iff \rec_n(\pi)|_{I_K}\cong\rec_n(\pi')|_{I_K}$
$$

$$
$\pi,\pi'\ \text{generic},\ r_n(\pi)|_{I_K}\cong r_n(\pi')|_{I_K}\ \Longrightarrow\ \pi|_K\cong\pi'|_K$
$$

$$
$(\Ind_P^{\GL_n(K)}\sigma)|_K=\Ind_{P\cap K}^{K}(\sigma|_{P\cap K})$
$$

## 定理与证明（或缺口）

### 引理 4.4（Bernstein 分量 ↔ WD 惯性类型）

$\pi,\pi'$ 同 Bernstein 分量 $\iff$ $\rec_n(\pi)|_{I_K}\cong\rec_n(\pi')|_{I_K}$。

> 证明状态：**sketch**。底本给了完整思路（BZ 分类 + 归纳到超尖点 + 引理 4.3 及其注），但最后一步「反复用注逐个分离分量」只作断言。

出处：`A §4.2.1 p.33–p.34`

### 引理 4.5（generic 时 Galois 惯性类型决定 K-限制）

一般的 $\pi,\pi'$ 若 $r_n(\pi)|_{I_K}\cong r_n(\pi')|_{I_K}$，则 $\pi|_K\cong\pi'|_K$。

1. 用 Iwasawa $\GL_n(K)=B\cdot\GL_n(\mathcal O_K)$ 与 Mackey，把 $\Ind_P^{\GL_n(K)}$ 限制到 $K$ 化成 $\Ind_{P\cap K}^{K}$。
   - *为什么*：这一步把 $G$ 上的诱导换成紧子群上的诱导，使泛性（generic ⇒ $\pi=Q(\Delta_1)\times\dots$）可以直接逐项比较。
2. 由定理 3.6，generic 给出 $\pi=Q(\Delta_1)\times\dots\times Q(\Delta_r)$，故 $\rec_n(\pi)=\bigoplus\rec_{n_i m_i}(Q(\Delta_i))$。
   - *为什么*：generic 保证 $\pi$ 是诱导的（无 linked），从而 $\rec_n$ 按块分解。
3. 由引理 1.9，两侧 Galois 惯性类型相同 $\iff$ 块数、块长 $m_i$ 与 $\rho_i|_{I_K}$ 逐项相同。
   - *为什么*：引理 1.9 正是「惯性类型相同」的判据。
4. 归到 $\pi=Q(\Delta(\lambda,m))$、$\pi'=Q(\Delta(\lambda',m))$，$\lambda'=\lambda\otimes\eta$（$\eta=\chi\circ\det$ 非分歧），故 $\rec_n(\pi')=\rec_n(\pi)\otimes\rec_1(\chi)$，即 $\pi'=\pi\chi$。
   - *为什么*：非分歧扭转在 $K$ 上平凡，故 $\pi|_K\cong\pi'|_K$ 成立。

出处：`A §4.2.2 p.34–p.35`

## 常见误解

- 引理 4.5 的结论是 $\pi|_K\cong\pi'|_K$（限制到 $\GL_n(\mathcal O_K)$ 同构），不是 $\pi\cong\pi'$；非分歧扭转在 $K$ 上不可见，这正是差别所在。
- 引理 4.4 用的是 $\rec_n(\pi)|_{I_K}$（Weil–Deligne 表示的底层 $W_K$ 表示限制到 $I_K$），引理 4.5 用的是 $r_n(\pi)|_{I_K}$（$\ell$ 进表示）；两者经 $\WD$ 对应，但记号不能混。

## 相关卡

[Bernstein 分量、惯性等价与定理 4.2 的直积分解](../concepts/bernstein-decomposition.md) · [Grothendieck 单值化定理、WD 函子与惯性类型](../concepts/wd-functor.md) · [一般（generic）表示、Whittaker 模型与定理 3.6](../concepts/generic-whittaker.md) · [惯性对应怎么从 Bernstein 分量推出来：BZ 分类 → 超尖点 → 引理 4.3](../derivations/inertia-from-bernstein.md)

## 出处（印刷页）

- A p.33–35（A p.33）

> 说明：引理 4.3 及其注、引理 4.4 的证明、引理 4.5 与 generic 反例取自 p.33–p.35；引理 4.5 的四步拆解是我们的整理，底本证明较简。
