# GL₂ 的四类表示如何对应到 Weil–Deligne 表示

> `yao17/deriv/gl2-llc-cases` · 轨道 分类与不变量 · 状态 dev · 5 步

> **要回答的问题**：GL₂ 的四类不可约容许表示分别对应哪一类 Weil–Deligne 表示？Sp₂(χ) 里的那个 N 作用在哪个向量上？

## 一句话

超尖点↦不可约 (ρ,0)；主序列↦(χ₁⊕χ₂,0)；triv⊗χ↦(χ⊕χ(1),0)；St₂(χ)↦(χ⊕χ(1),N)。

## 目标

在 $n=2$ 时把定理 2.13 的对应写全，验证四类 $\pi$ 恰好覆盖 $\WD_2$ 的四类对象。

## 前提

- $K$ 是 $p$ 进局部域，$\chi,\chi_1,\chi_2$ 是 $K^\times$ 的特征标（经 $\Art$ 也看成 $W_K$ 的特征标）。
- $\rec_2\colon\mathcal G_2^{\mathrm{irr}}\to\WD_2$ 是 LLC 的逆；$\WD_2$ 是 $\dim=2$ 的 Weil–Deligne 表示类。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 第一类：$\pi$ 不可约超尖点 $\iff$ $\rec_2(\pi)=(\rho,0)$ 且 $\rho$ 不可约。 | 超尖点对应「不可约的 $\rho$ 配 $N=0$」，这是 LLC 在 $n=2$ 时最干净的一半。 | `A p.25` | A·原文明确写了 |
| 2 | 第二类：$\pi=\chi_1\times\chi_2$（主序列，$\chi_1/\chi_2\neq\|\cdot\|^{\pm1}$）$\iff$ $\rec_2(\pi)=(\chi_1\oplus\chi_2,0)$，两个特征标都不可约。 | 主序列不可约时 $N=0$，而 $\rho$ 可约（两个特征标直和）；这给出「可约 $\rho$、$N=0$」的一类。 | `A p.25` | A·原文明确写了 |
| 3 | 第三类：$\pi=\mathrm{triv}\otimes\chi=Q(\chi\|\cdot\|^{1/2},\chi\|\cdot\|^{-1/2})$（特殊表示，主序列的不可约商）$\iff$ $\rec_2(\pi)=(\chi\oplus\chi(1),0)$，即 Frobenius 半单、$N=0$ 但 $\rho$ 是同一个特征标的两个不同扭转直和。 | 这是「$\rho$ 不可分解但 $N=0$」的情形：$\chi$ 与 $\chi(1)$ 在 $W_K$ 作用下不能分开，却都在 $\rho$ 里出现一次。 | `A p.25` | A·原文明确写了 |
| 4 | 第四类：$\pi=\St_2(\chi)=Q([\chi\|\cdot\|^{-1/2},\chi\|\cdot\|^{1/2}])$（Steinberg 扭转）$\iff$ $\rec_2(\pi)=\Sp_2(\chi)=(\chi\oplus\chi(1),N)$，其中 $N\colon\chi\to\chi(1)$ 是唯一非零的 $W_K$-映射，$N^2=0$。 | $N\neq0$ 正是「平方可积但非超尖点」在 Galois 侧的标志：$\Sp_2$ 的 $N$ 把 $\chi$ 打到 $\chi(1)$，两端各出现一次。 | `A p.26` | A·原文明确写了 |
| 5 | 核对覆盖：四类 $\pi$ 的 $\rec_2(\pi)$ 分别落在「$\rho$ 不可约」「$\rho$ 半单可约」「$\rho$ 不可分、$N=0$」「$N\neq0$」四格，穷尽 $\dim=2$ 的 Weil–Deligne 表示；且脚注 10 提醒更准确的写法是 $(\Art^{-1}\chi_1\oplus\Art^{-1}\chi_2,0)$。 | 这一步把「四类」与「$\WD_2$ 的全部分类」对齐，说明定理 2.13 在 $n=2$ 时确实是双射而不是单射。 | `A p.26` | A·原文明确写了 |

## 结论

四类 $\GL_2$ 的不可约容许表示与 $\WD_2$ 的四类对象一一对应；$\Sp_2(\chi)$ 的 $N$ 把 $\chi$ 送到 $\chi(1)$，是「平方可积非超尖点」的 Galois 侧标志。

## 缺口

- 第三、四类的「$\iff$」底本只写括号说明，未逐个验证双向；核对覆盖一步是我们补的。
- $Q([\chi|\cdot|^{-1/2},\chi|\cdot|^{1/2}])$ 作为唯一不可约商的论证底本略去，引 Zelevinsky。

## 最容易讲错的地方

- $\mathrm{triv}\otimes\chi$ 与 $\St_2(\chi)$ 都来自同一段 $[\chi|\cdot|^{-1/2},\chi|\cdot|^{1/2}]$，区别只在取子还是取商；对应到 WD 侧则是 $N=0$（子）与 $N\neq0$（商）。
- 写 $\chi$ 还是 $\Art^{-1}\chi$ 要看把 $\chi$ 放在 $K^\times$ 侧还是 $W_K$ 侧；底本脚注 10 专门纠正这一点，混用会让 $\rho$ 少一个扭转。
- $\Sp_2(\chi)$ 里 $N$ 的定义依赖 $\chi(1)$ 与 $\chi$ 的同构选取；换生成元只改标量，故 $\Sp_2(\chi)$ 作为同构类良定。

## 相关卡

[局部 Langlands 对应：定理 2.13 的五条性质](../concepts/llc-statement.md) · [Weil–Deligne 表示 (ρ, N) 及其基本性质](../concepts/wd-representation.md) · [本质 L^r、平方可积、缓增：定理 3.2、3.3 与推论 3.4](../concepts/square-integrable-tempered.md) · [把 LLC 从超尖点归纳到一般表示：rec_n = ⊕ Sp_{m_i} ∘ rec_{n_i}](../derivations/induction-to-supercuspidal.md)

## 出处（印刷页）

- A p.25–26（A p.26）

> 说明：四类对应与脚注 10 取自 p.25–p.26；「覆盖四格」的核对表是我们据 $\WD_2$ 分类补的。
