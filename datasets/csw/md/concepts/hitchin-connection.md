---
id: csw/concept/hitchin-connection
type: concept
track: C
---

# Hitchin 联络与 KZ 联络

> 在 Teichmüller 空间上，把全纯截面空间沿“复结构改变”的方向求导，得到 Hitchin 联络；在 $g=0$ 带标记点时它显式化为 KZ 方程。

**问题**：Hitchin 联络的曲率为什么只有迹部分？KZ 方程是它的哪个特例？

## 定义

设 $\mathcal{H}_J=H^0(\mathcal{M}_J,\mathcal{L}^{\otimes k})$。Hitchin 联络 $\nabla$ 在向量场 $\partial/\partial t$（$t$ 是 Teichmüller 坐标）上的作用由“把截面沿 $J$ 的变化平行移动”给出，其曲率纯迹：$[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}=\omega_{\mathcal{T}}(X,Y)\mathrm{id}$。当 $g=0$ 带 $n$ 个标记点且取 $\mathcal{M}_J$ 为带标记点的模空间时，全纯截面满足 KZ 方程 $\kappa\partial_{z_i}\Psi=\sum_{j\ne i}\frac{\Omega_{ij}}{z_i-z_j}\Psi$，$\kappa=k+h^\vee$。

*记号*：$\Omega_{ij}=\sum_aT^a_{(i)}T^a_{(j)}$；$\kappa=k+h^\vee$ 是“有效 level”。

## 要点

- Hitchin 联络的曲率纯迹，是因为全纯截面空间的维数在变形下不变，只有整体相位可以变。
- 在 $g=0$ 时模空间的复结构由标记点位置 $z_i$ 给出，Hitchin 联络就是 KZ 方程。
- KZ 的分母是 $z_i-z_j$，说明它是“两点函数”的推广；单极点结构来自算子积展开。
- 有效 level 是 $k+h^\vee$，不是 $k$：半形式修正已经把 $h^\vee$ 加进去了。
- KZ 的单值性给出共形块的表示，这是“共形块 = 物理态空间”的最具体实现。

## 关键公式

- $[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}=\omega_{\mathcal{T}}(X,Y)\,\mathrm{id}$
- $\kappa\partial_{z_i}\Psi=\sum_{j\ne i}\frac{\Omega_{ij}}{z_i-z_j}\Psi$
- $\kappa=k+h^\vee$

## Hitchin 联络的平坦性（射影）

$\mathcal{T}$ 上的 Hitchin 联络 $\nabla$ 的曲率是纯迹的，因此给出射影平坦结构；其单值性为 $\operatorname{MCG}(\Sigma)$ 的射影表示。

**证明要点**（sketch）：

1. 计算 $\nabla$ 的曲率：$[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}$ 的迹部分由 $\partial\bar\partial$ 的 Quillen 曲率给出。 *（这是 Hitchin 1990 的计算；本文只引用结论。）*
2. 无迹部分为零，来自全纯截面空间的维数在变形下不变。 *（维数局部常数意味着平行移动只差整体相位。）*
3. 故曲率 $=\omega\cdot\mathrm{id}$，射影平坦。 *（纯迹曲率就是射影平坦的定义。）*

> **缺口**：本文只说“should be”；严格证明由 Hitchin 给出，KZ 显式形式见 Knizhnik–Zamolodchikov 与河野 §1.5。

## 陷阱

- 把 $\kappa$ 写成 $k$ 是常见错误：分母必须是 $k+h^\vee$，否则 $SU(2)$、$k=1$ 的数值全错。
- KZ 只在 $g=0$ 有显式的 $\sum\Omega_{ij}/(z_i-z_j)$ 形式；高亏格要加更多项。
- Hitchin 联络与 Berry 联络不是一回事，但都描述“参数变化时的平行移动”。

## 相关卡片

- [projective-flat-connection](../concepts/projective-flat-connection.md)
- [knizhnik-zamolodchikov](../concepts/knizhnik-zamolodchikov.md)
- [conformal-blocks](../concepts/conformal-blocks.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.2 射影平坦联络（Hitchin），印刷页 [369, 370] / PDF 页 [19, 20]（witten1989/sections/s04-canonical.tex §3.2）

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
