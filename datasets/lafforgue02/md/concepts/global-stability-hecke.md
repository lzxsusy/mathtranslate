# Hecke 对应的全局稳定性定理

> `lafforgue02/concept/global-stability-hecke` · 轨道 B · 拓扑镜像对称与 Hodge 数 · 状态 dev

> **先自测**：全局稳定性定理说的「只差 Frob 的幂」到底允许了什么、禁止了什么？

## 一句话

若两个截断 chtouca 在 Hecke 意义下相互对应且都延拓到整族，则它们特殊化后的极点、零点与退化子只相差 Frob 的一个幂。

## 定义

设 $\tilde{\mathcal E},\tilde{\mathcal F}$ 是 $\Cht^{r,\overline p\le p}(K_A)$ 的两个点，它们在 Hecke 意义下相互对应，并延拓为 $\Cht^{r,\overline p\le p}(A)$ 的点。定理断言：$\tilde{\mathcal E}$ 与 $\tilde{\mathcal F}$ 的特殊化所给出的极点、零点与退化子构成的集合，彼此只相差 Frob 的一个幂。

**记号**：$x_s=x(\mathcal E_s^M)$ 为退化子；$\mathrm{Frob}$ 是相对 Frobenius。

## 要点（为什么需要它）

1. 「只差 Frob 的幂」是最弱的可能结论：它允许坐标整体差一个 Frobenius 平移，但不允许退化位置真正不同。
2. 证明拆两步：Hecke 对应只在有限多个位作用（故一般纤维相同）；再由命题把问题化到两个迭代 $\varphi$-格由初等变换相联系。
3. 关键计算是 $${}^\tau\det(\mathcal E_s^M)\cong\det(\mathcal E_s^M)(\oo-x_s)$$，退化子 $x_s$ 由这个同构里的除子读出。
4. 它正是第 II 章「Hecke 对应在不动点附近保持 chtouca 开集」的来源。

## 核心公式

$$
$\Cht^{r,\overline p\le p}(K_A)\rightsquigarrow\Cht^{r,\overline p\le p}(A)$，特殊化$\deg{}^{\tau}\mathcal E/\overline{\mathcal E}_s=\deg\mathcal E_s+1$$\mathrm{div}(\oo-x_s)=\deg(\text{退化})$
$$

$$
$\deg{}^{\tau}\mathcal E/\overline{\mathcal E}_s=\deg\mathcal E_s+1$
$$

$$
$\mathrm{div}(\oo-x_s)=\deg(\text{退化})$
$$

## 定理与证明（或缺口）

### Hecke 对应的全局稳定性

两个在 Hecke 意义下对应且可延拓的截断 chtouca，其特殊化的极点、零点、退化子集合只相差 Frob 的幂。

> 证明状态：**sketch**。讲义给出证明骨架与关键同构，中间对逐一初等变换的归纳细节从略。

出处：`A p.41`

## 常见误解

- 定理的结论是「集合只相差 Frob 的幂」，不是「两个 chtouca 同构」；把结论读强是常见错误。
- 「延拓为 $A$-点的点」这一前提不能省：不延拓时退化子无从谈起。

## 相关卡

[Hecke 对应与 Hecke 代数](../concepts/hecke-correspondence.md) · [退化子（dégénérateur）](../concepts/degenerator.md) · [用赋值判据把紧合性化归为构造一个 $\varphi$-格](../derivations/properness-by-valuative-criterion.md)

## 出处（印刷页）

- A p.41–45（A p.41）

> 说明：定理与证明取第 V 章 p.41–45。原文两处笔误（$M,M'=2$ 应为 $M,M'$ 两个；夹注把 $M'$ 换成 $M$）已加译注，本卡按修正后的读法陈述，并在《疑点清单》登记。
