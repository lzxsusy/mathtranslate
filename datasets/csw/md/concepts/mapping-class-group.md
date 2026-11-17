---
id: csw/concept/mapping-class-group
type: concept
track: F
---

# 映射类群与模函子

> $\operatorname{MCG}(\Sigma)$ 通过“剪开-扭转-粘回”作用于 $\Sigma$，得到 $\cH_\Sigma$ 上的射影表示；Segal 的模函子把这套结构公理化。

**问题**：为什么映射类群的作用只到射影？它与三维手术有什么关系？

## 定义

映射类群 $\operatorname{MCG}(\Sigma)=\pi_0\operatorname{Diff}^+(\Sigma)$ 作用在 $\Sigma$ 上；把它看成 $\Sigma\times[0,1]$ 的边界粘合，得到三维流形 $M_\phi$。CS 的量子化给出 $\operatorname{MCG}(\Sigma)$ 在 $\cH_\Sigma$ 上的射影表示（因为 $\cH_\Sigma$ 只是射影平坦丛的纤维）。Segal 的模函子把“曲面→向量空间、粘合→配对、映射类→射影自同构”公理化。

*记号*：$\phi\in\operatorname{MCG}(\Sigma)$；$M_\phi=\Sigma\times[0,1]/(x,1)\sim(\phi(x),0)$；$\rho:\operatorname{MCG}\to\mathrm{PGL}(\cH_\Sigma)$。

## 要点

- 映射类群的作用是射影的：整体相位不可消除（共形反常）。
- 三维手术 = 沿环面粘合，其“粘合映射”就是 $\operatorname{MCG}(T^2)=SL(2,\mathbb{Z})$ 的元素。
- 把 $\Sigma$ 剪开再粘回得到 $M_\phi$，其配分函数 $Z(M_\phi)=\operatorname{Tr}_{\cH_\Sigma}\rho(\phi)$（TQFT 的迹公式）。
- 模函子（Segal）是“共形场论 = 函子”的严格版本；CS 给出它的构造。
- 单值性 = 映射类群表示；这正是“共形块为什么是三维的”的答案。

## 关键公式

- $\rho:\operatorname{MCG}(\Sigma)\to\mathrm{PGL}(\cH_\Sigma)$
- $Z(M_\phi)=\operatorname{Tr}_{\cH_\Sigma}\rho(\phi)$
- $\operatorname{MCG}(T^2)=SL(2,\mathbb{Z})$

## 映射类群表示与手术

CS 量子化给出 $\operatorname{MCG}(\Sigma)$ 在 $\cH_\Sigma$ 上的射影表示；对 $\phi\in\operatorname{MCG}$，$Z(M_\phi)=\operatorname{Tr}\rho(\phi)$ 且与手术描述一致。

**证明要点**（sketch）：

1. $\operatorname{MCG}$ 作用在 $\Sigma$ 上，逐点作用在态空间上，得射影表示。 *（射影性来自 $\cH_\Sigma$ 的射影平坦性。）*
2. 把 $\phi$ 看成 $\Sigma\times[0,1]$ 的边界粘合，得 $M_\phi$。 *（这是映射环面的构造。）*
3. 沿边界收缩给出迹公式 $Z(M_\phi)=\operatorname{Tr}\rho(\phi)$。 *（这是 TQFT 的“态-配分函数”对应。）*

> **缺口**：本文只说“模函子可在三维量子化中得到”，未系统展开；Segal 的严格版见其 1988/2004 讲义。

## 陷阱

- 射影表示不是线性表示：不要忽略相位，它影响手术不变量。
- $\operatorname{MCG}(T^2)=SL(2,\mathbb{Z})$ 作用在 $\cH(T^2)$ 上就是 $S,T$ 矩阵；这是 Verlinde 公式的几何来源。
- 不同亏格的映射类群差别很大；别把环面的结论直接搬到高亏格。

## 相关卡片

- [cs-wzw-duality](../concepts/cs-wzw-duality.md)
- [projective-flat-connection](../concepts/projective-flat-connection.md)
- [s-matrix](../concepts/s-matrix.md)
- [surgery-formula](../concepts/surgery-formula.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.2 与 §5（模函子），印刷页 [369, 397] / PDF 页 [19, 47]（witten1989/sections/s04-canonical.tex（§3.2）与 s09-applications.tex（§5））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
