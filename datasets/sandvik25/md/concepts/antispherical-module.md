# 反球模 $M^{\mathrm{asph}}$

> `sandvik25/concept/antispherical-module` · 轨道 A · 中心层与 Wakimoto 层 · 状态 dev

> **先自测**：反球模是怎么由符号表示诱导出来的，为什么叫「反球」？

## 一句话

把 $\mathbb Z$ 沿 $W$ 的符号表示诱导到延长仿射 Weyl 群：$M^{\mathrm{asph}}=\mathbb Z\otimes_{\mathbb Z[W]}\mathbb Z[W_{\mathrm{ext}}]$。它是整篇文章的「靶子」。

## 定义

$G$ 是 $\mathbb F_p$ 上的连通约化群，$B\subset G$ 为 Borel，$T$ 为极大环面，$W_{\mathrm{ext}}=W\ltimes X^\vee$ 为延长仿射 Weyl 群。令 $\mathbb Z[W]$ 通过符号表示作用在 $\mathbb Z$ 上，定义右 $\mathbb Z[W_{\mathrm{ext}}]$-模 $M^{\mathrm{asph}}:=\mathbb Z\otimes_{\mathbb Z[W]}\mathbb Z[W_{\mathrm{ext}}]$。

**记号**：$W$ 有限 Weyl 群，$X^\vee$ 余根格；$\ell$ 是 $W_{\mathrm{ext}}$ 上准 Coxeter 结构的长度函数。

## 要点（为什么需要它）

1. 「反球」指的是取符号表示（而非平凡表示）：球（spherical）情形用平凡表示，反球用符号表示，两者的 Hecke 模对偶。
2. 这个模的 $K_0$ 同时作用于三个几何对象（反球 Hecke 范畴、Springer 解消上的凝聚层、IW 层），所以它是三条范畴化路线的公共骨架。
3. 式 (2) 的 $[\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})]\cong M^{\mathrm{asph}}$ 不是显然的：它把「符号表示」翻成「$\wedge$-幂的符号」，再靠 Springer 解消的几何把它实现。
4. 模层面只有一个对象，范畴化之后变成「每个 $V\in\mathrm{Rep}(G^\vee)$ 一个对象」；从模到范畴的这一步正是 [ArBe] 的工作。

## 核心公式

$$
$M^{\mathrm{asph}}:=\mathbb Z\otimes_{\mathbb Z[W]}\mathbb Z[W_{\mathrm{ext}}]$$[\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})]\cong M^{\mathrm{asph}}$
$$

$$
$[\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})]\cong M^{\mathrm{asph}}$
$$

## 定理与证明（或缺口）

### 式 (2)：$K$ 群同构

$G^\vee$-等变 Springer 解消上凝聚层的 Grothendieck 群同构于 $M^{\mathrm{asph}}$。

> 证明状态：**gap**。原文只引用，不证；这是 [ArBe] 与几何表示论的既有结果，本译本未补。

出处：`A p.1`

## 常见误解

- 不要把 $M^{\mathrm{asph}}$ 与仿射 Hecke 代数混为一谈：前者是 $\mathbb Z[W_{\mathrm{ext}}]$ 上的模，后者是 $W_{\mathrm{ext}}$ 的群代数本身。
- $\mathbb Z$ 上的符号表示要求 $W$ 的生成元都作用为 $-1$，若误用平凡表示会得到球模而不是反球模。

## 相关卡

[反球模的三种描述与三种范畴化](../concepts/three-categorifications.md) · [Springer 解消 $\widetilde{\mathcal N}$ 与线丛 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)$](../concepts/springer-resolution.md) · [Wakimoto 层 $\mathbb W_\lambda$](../concepts/wakimoto-sheaves.md)

## 出处（印刷页）

- A p.1（A p.1）

> 说明：定义与式 (2) 出自 p.1；「反球=符号诱导」的解读见原文 §2.6 反球商的构造。
