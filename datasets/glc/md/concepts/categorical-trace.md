---
id: glc/concept/categorical-trace
type: concept
track: G
---

# 范畴迹

> 对可对偶 DG 范畴与自函子，仿向量空间迹的公式定义、落在 $\operatorname{Vect}$ 中的对象。

**问题**：为什么范畴迹 $\operatorname{Tr}(F;\mathcal C)$ 落在 $\operatorname{Vect}$ 里，而不是落在 $\mathcal C$ 里？

## 定义

对于可对偶 DG 范畴 $\mathcal C$ 和自函子 $F:\mathcal C\to\mathcal C$，用与向量空间迹相同的公式定义
$$\operatorname{Tr}(F;\mathcal C):=\bigl[\operatorname{Vect}\xrightarrow{\operatorname{coev}}\mathcal C\otimes\mathcal C^\vee\xrightarrow{F\otimes\operatorname{Id}}\mathcal C\otimes\mathcal C^\vee\xrightarrow{\operatorname{ev}}\operatorname{Vect}\bigr].$$
对照地，对有限维向量空间 $V$ 与自同态 $f:V\to V$，通常的迹是复合 $\bigl[k\xrightarrow{\operatorname{coev}}V\otimes V^*\xrightarrow{f\otimes\operatorname{Id}}V\otimes V^*\xrightarrow{\operatorname{ev}}k\bigr]$ 得到的标量。

*记号*：$\mathcal C^\vee$ 为 $\mathcal C$ 的对偶范畴；$\operatorname{coev}=\eta$ 为单位、$\operatorname{ev}=\varepsilon$ 为余单位（满足 zig-zag 恒等式）；$\operatorname{Vect}$ 为 DG 范畴。

## 要点

- 对有限维向量空间，同样的复合给出通常的迹（一个标量）。
- 对可对偶 DG 范畴，复合的两端都落在 $\operatorname{Vect}$ 上，因此 $\operatorname{Tr}(F;\mathcal C)$ 是 $\operatorname{Vect}$ 中的对象（一个复形），而不是 $\mathcal C$ 中的对象。
- 范畴 $\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)$ 预期是可对偶的；在受限理论中这一点已在所需的意义下成立 [AGK20b]，所以这个迹有意义。
- 取 $F=\operatorname{Fr}$ 时它对应 $\operatorname{Bun}_G(\mathbb F_q)$ 上的函数空间。

## 关键公式

- $$\operatorname{Tr}(F;\mathcal C):=\bigl[\operatorname{Vect}\xrightarrow{\operatorname{coev}}\mathcal C\otimes\mathcal C^\vee\xrightarrow{F\otimes\operatorname{Id}}\mathcal C\otimes\mathcal C^\vee\xrightarrow{\operatorname{ev}}\operatorname{Vect}\bigr]$$
- $$\bigl[k\xrightarrow{\operatorname{coev}}V\otimes V^*\xrightarrow{f\otimes\operatorname{Id}}V\otimes V^*\xrightarrow{\operatorname{ev}}k\bigr]$$

## 定理与证明

### 范畴迹的层-函数恒等式（要点（有缺口））

预期有 $\operatorname{Tr}(\operatorname{Fr};\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G))\simeq C^{\infty}_{\mathrm{stk}}(\operatorname{Bun}_G(\mathbb F_q))$，它在通常的完备化选择、有限性条件以及自守函数上来自叠自同构的权重的意义下成立。

1. 取 $k=\mathbb F_q$ 并使用 $\ell$-进层，Frobenius 作用在自守范畴上。  
   *为什么*：有限域上才有 Frobenius 自同构。
2. 把范畴迹按定义展开为 $\operatorname{coev}$、$\operatorname{Fr}\otimes\operatorname{Id}$、$\operatorname{ev}$ 的复合。  
   *为什么*：可对偶性使该复合有定义。
3. 把所得对象识别为 $\operatorname{Bun}_G(\mathbb F_q)$ 上的叠函数空间。  
   *为什么*：这是层-函数对应的预期内容。

> 缺口：讲义称之为「预期的层与函数对应陈述」，未给证明；且只在通常的完备化选择、有限性条件与叠自同构权重的意义下成立。

*出处*：定义与预期（§12.7，讲义无编号） / 原书 p.63


## 易错点

- 范畴迹不是数：$\operatorname{Tr}(F;\mathcal C)$ 是 $\operatorname{Vect}$ 中的对象（复形）。只有在层-函数对应下取 $F=\operatorname{Fr}$，才得到 $\operatorname{Bun}_G(\mathbb F_q)$ 上的函数。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§12.7 范畴迹与有限域上的函数，p.63（PDF p.63），`源码/chapters/ch12.tex:125-146（范畴迹的定义与预期恒等式，§12.7）`

## 核验

状态：`external-confirmed`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/trace — C=Vect_k 时 tr(f) 为 k→η V⊗V*→f⊗id V⊗V*→ε k，ε 为标准 evaluation pairing；tr(f)(λ)=λΣa_ii。
- arXiv:2010.01906 (AGK20a)：https://arxiv.org/abs/2010.01906 — Tr((Frob_BunG)_*,Shv_Nilp(Bun_G)) 同构于 Autom:=Funct_c(Bun_G(F_q))。
- arXiv:2012.07665 (AGK20b)：https://arxiv.org/abs/2012.07665 — Shv_Nilp(Bun_G) 与其自身对偶等同，从而范畴迹有意义。

## 关联

- `glc/concept/frobenius-twisted-trace`
- `glc/concept/restricted-categorical-langlands`
