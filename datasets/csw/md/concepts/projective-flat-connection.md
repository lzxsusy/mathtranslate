---
id: csw/concept/projective-flat-connection
type: concept
track: C
---

# 射影平坦丛与“与 $J$ 无关”

> $H^0(\cM_J,\cL^{\otimes k})$ 随 $J$ 构成 Teichmüller 空间上的向量丛，只带射影平坦联络：平行移动在整体相位上有歧义，单值性给出映射类群的射影表示。

**问题**：为什么“Hilbert 空间与 $J$ 无关”只在射影意义下成立？单值性为什么与纽结不变量有关？

## 定义

设 $\mathcal{T}$ 是 $\Sigma$ 的 Teichmüller 空间。$\cH_\Sigma^{(J)}=H^0(\cM_J,\cL^{\otimes k})$ 在 $\mathcal{T}$ 上构成向量丛，带一个联络 $\nabla$。该联络不是平坦的，而是射影平坦：$[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}=\omega(X,Y)\cdot\mathrm{id}$，其中 $\omega$ 是 $\mathcal{T}$ 上的 Kähler 形式（Hitchin 联络）。沿闭环平行移动给出射影变换，即映射类群 $\operatorname{MCG}(\Sigma)$ 的射影表示。

*记号*：$\mathcal{T}$ 是 Teichmüller 空间；$\operatorname{MCG}(\Sigma)=\pi_0\operatorname{Diff}^+(\Sigma)$；射影平坦 = 平坦到中心扩张。

## 要点

- “与 $J$ 无关”的准确含义：向量空间之间没有典范同构，只有射影同构。
- 射影因子是规范（anomaly）：它来自共形反常，不是坐标选择。
- 单值性给出映射类群的射影表示；在三维里这就是“沿边界粘合”的运算，模函子由此而来。
- 带标记点时联络变成 KZ 联络（在 $g=0$ 时显式可写）。
- Witten 只给出物理论证（$\cH_\Sigma$ 应当与 $J$ 无关），严格证明由 Hitchin 与 Segal 给出。

## 关键公式

- $[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}=\omega(X,Y)\,\mathrm{id}$
- $\operatorname{MCG}(\Sigma)\curvearrowright\mathbb{P}\cH_\Sigma$

## 射影平坦性（Hitchin）

$\mathcal{T}$ 上由 $H^0(\cM_J,\cL^{\otimes k})$ 构成的向量丛带自然的射影平坦联络；其单值化为 $\operatorname{MCG}(\Sigma)$ 的射影表示。

**证明要点**（sketch）：

1. 用 $\bar\partial$ 族的行列式线丛与 Quillen 联络构造 $\nabla$。 *（联络来自“把 $J$ 变一点”时全纯截面空间的移动。）*
2. 曲率计算给出 $[\nabla,\nabla]=\omega\cdot\mathrm{id}$，即曲率是纯迹的。 *（迹部分由 Kähler 形式给出，其余为零——这就是射影平坦。）*
3. 沿闭环的平行移动定义射影变换，给出 $\operatorname{MCG}$ 的作用。 *（单值性只由拓扑决定。）*

> **缺口**：本文自认是物理推导（p.370 说 heuristic）；Hitchin 的严格证明与 KZ 在带标记点的显式形式不在本文范围。

## 陷阱

- 不要说“Hilbert 空间不依赖 $J$”：只能说射影化后不依赖；射影因子是物理的（共形反常）。
- 射影平坦不等于平坦：曲率不为零，只是纯迹；把它当平坦会丢掉单值性。
- 单值性是射影表示，不是线性表示；相位不是总能整体消掉。

## 相关卡片

- [holomorphic-sections](../concepts/holomorphic-sections.md)
- [hitchin-connection](../concepts/hitchin-connection.md)
- [conformal-blocks](../concepts/conformal-blocks.md)
- [mapping-class-group](../concepts/mapping-class-group.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.2 模空间上的平坦向量丛，印刷页 [369, 371] / PDF 页 [19, 21]（witten1989/sections/s04-canonical.tex §3.2）

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
