# 惯性对应怎么从 Bernstein 分量推出来：BZ 分类 → 超尖点 → 引理 4.3

> `yao17/deriv/inertia-from-bernstein` · 轨道 惯性 Langlands 与类型 · 状态 dev · 5 步

> **要回答的问题**：引理 4.4 的「同分量 ⇔ rec(π)|I_K 同构」是怎么从 BZ 分类与引理 4.3 一步步得到的？

## 一句话

把 π 写成 Q(Δ₁..Δ_r) 后限制到 I_K，只剩各段超尖点的 rec，再用引理 4.3 逐个分离分量。

## 目标

复现引理 4.4 的证明：把 $\rec_n(\pi)|_{I_K}$ 化成各超尖点块的直和，再用引理 4.3 的注分离。

## 前提

- $\pi=Q(\Delta_1,\dots,\Delta_r)$，$\Delta_i=\Delta_i(\pi_i,m_i)$，$\pi_i$ 超尖点，$n=\sum n_i m_i$；对应 Levi $L=\prod_i\GL_{n_i}(K)^{m_i}$。
- 引理 4.3：$H\triangleleft G$、$G/H$ 交换、$\rho_1|_H\cong\rho_2|_H$ $\Rightarrow$ $\rho_2\cong\rho_1\otimes\psi$；注：只需 $\Hom_H(\rho_1,\rho_2)\neq0$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 由 BZ 分类，$\pi=Q(\Delta_1,\dots,\Delta_r)$ 给出 $L=\prod_i\GL_{n_i}(K)^{m_i}$ 与 $\sigma=\bigotimes_{i,j}\pi_i\|\cdot\|^j$（$j=0,\dots,m_i-1$），使 $\pi$ 是 $I_L^{\GL_n}(\sigma)=I_P^{\GL_n}(\sigma)$ 的子商。 | 这一步把「$\pi$ 在哪个 Bernstein 分量」翻译成「$\sigma$ 的超尖点块 $\pi_i$ 与段长 $m_i$」的显式数据。 | `A p.33` | A·原文明确写了 |
| 2 | 由引理 1.9 与 3.1.7，$\rec_n(\pi)\|_{I_K}=\bigoplus_i\rec_{n_i}(\pi_i)^{m_i}\|_{I_K}$：$\SL_2$ 部分 $\Sp_{m_i}$ 在 $I_K$ 上平凡，只剩各 $\rec_{n_i}(\pi_i)$ 重复 $m_i$ 次。 | $P_K\subset I_K$ 上 $\Sp_m$ 平凡是这里的关键——惯性群看不到段长，只看到「哪些超尖点块、各几次」。 | `A p.33` | A·原文明确写了 |
| 3 | 于是问题归到超尖点情形：$\pi_i$ 超尖点时 $\rec_{n_i}(\pi_i)\|_{I_K}$ 不可约（若 $\pi_i$ 非超尖点则其 $\rec$ 在 $I_K$ 上可约），两个超尖点的 $I_K$-限制同构 $\iff$ 二者惯性等价。 | 超尖点 $\Leftrightarrow$ $I_K$ 上不可约，这使「同构」变成「逐块配对」，避免了不可约分解的歧义。 | `A p.33` | A·原文明确写了 |
| 4 | 对两个分量 $\pi=Q(\Delta_1..\Delta_r)$、$\pi'=Q(\Delta'_1..\Delta'_{r'})$，若 $\rec_n(\pi)\|_{I_K}\cong\rec_n(\pi')\|_{I_K}$，则第 2–3 步给出块的多重集相同，即 $(L,\sigma)$ 与 $(L',\sigma')$ 惯性等价。 | 多重集相同正是惯性等价的定义（允许非分歧扭转与共轭），这一步完成「$\Rightarrow$」。 | `A p.34` | A·原文明确写了 |
| 5 | 反向：若惯性等价，取 $H=I_K$、$G=W_K$（$G/H\cong\mathbb Z$ 交换），引理 4.3 给出 $\rec_n(\pi')\|_{I_K}\cong\rec_n(\pi)\|_{I_K}\otimes\psi$（$\psi$ 为 $W_K/I_K$ 的特征标）；对每个块反复用「只需 $\Hom_H(\rho_1,\rho_2)\neq0$」的注把 $\psi$ 吸收掉，得同构。 | 这是证明中最技术的一步：$\psi$ 是非分歧扭转，在 $I_K$ 上平凡，故「吸收」不改变 $I_K$-限制——但也正因为如此，引理 4.4 才只能给出 $I_K$ 上的同构，而不能给出 $W_K$ 上的同构。 | `A p.34` | A·原文明确写了 |

## 结论

$\pi,\pi'$ 同 Bernstein 分量 $\iff$ $\rec_n(\pi)|_{I_K}\cong\rec_n(\pi')|_{I_K}$。Bernstein 中心 $\mathcal B(\GL_n)$ 因此被 Weil–Deligne 惯性类型（$\rho|_{I_K}$ 连同各块的重复数）索引。

## 缺口

- 第 3 步「超尖点 $\Leftrightarrow$ $I_K$ 上不可约」底本未证，只引用。
- 第 5 步「反复用注分离分量」底本写作一句断言，未给逐块的归纳。

## 最容易讲错的地方

- 第 2 步 $\Sp_{m_i}$ 在 $I_K$ 上平凡，故 $m_i$ 只以「重复次数」出现；若把 $\rec_n(\pi)|_{I_K}$ 误算成含 $\SL_2$ 结构就会多出 $m_i$ 的信息，与「Bernstein 中心不含段长」矛盾。
- 第 5 步用引理 4.3 需要 $G/H$ 交换；$W_K/I_K\cong\widehat{\mathbb Z}$ 确实交换，但 $W_K/P_K$ 不交换，换成野惯性群就不成立。
- $gL_1g^{-1}=L_2$ 中的 $g$ 是 $\GL_n(K)$ 的元素（共轭），不是 $W_K$ 的元素；两个并存的「共轭」层次容易混。

## 相关卡

[惯性对应：Bernstein 中心 ↔ Weil–Deligne 惯性类型（引理 4.3–4.5）](../concepts/inertial-correspondence.md) · [Bernstein 分量、惯性等价与定理 4.2 的直积分解](../concepts/bernstein-decomposition.md) · [定理 3.1：Bernstein–Zelevinsky 对 GL_n 容许表示的七条分类](../concepts/bz-classification.md) · [把 LLC 从超尖点归纳到一般表示：rec_n = ⊕ Sp_{m_i} ∘ rec_{n_i}](../derivations/induction-to-supercuspidal.md)

## 出处（印刷页）

- A p.33–34（A p.33）

> 说明：证明链依 p.33–p.34 的引理 4.4 整理；第 3 步的等价与第 5 步的逐块归纳是我们补的，已在 gaps 标出。
