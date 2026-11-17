---
id: csw/concept/conformal-blocks
type: concept
track: E
---

# 共形块

> 带标记点 $(\Sigma;P_i,R_i)$ 的共形块空间 $\mathcal{H}_\Sigma$ 是 WZW 的手征态空间；在 CS 里它就是 $H^0(\mathcal{M}_J,\mathcal{L}^{\otimes k})$。

**问题**：共形块与 CS 的量子 Hilbert 空间是什么关系？为什么说它们“是同一个空间”？

## 定义

固定复结构 $J$，带标记点 $(P_i,R_i)$ 的 WZW 共形块空间是 $z_i$ 处插入表示 $R_i$ 的手征场的多点函数空间（模去零模态）。Segal 的模函子把“曲面+标记+表示”映到有限维向量空间。CS 在 $\Sigma\times\mathbb{R}$ 上的量子 Hilbert 空间按 $\mathcal{H}_\Sigma=H^0(\mathcal{M}_J,\mathcal{L}^{\otimes k})$ 计算，两者作为向量空间典范同构。

*记号*：$\mathcal{H}_\Sigma$ 随 $J$ 是射影平坦丛；不带标记点时 $\mathcal{H}_\Sigma$ 是一维（空曲面）。

## 要点

- 共形块的维数是有限的（可积表示与紧曲面）。
- CS 的 $\mathcal{H}_\Sigma$ 与 WZW 的共形块空间是“对象级同构”：都是 $H^0(\mathcal{M}_J,\mathcal{L}^{\otimes k})$。
- 这个同构的证明不是本文给的：Witten 只给物理论证，严格处理由 Segal 与 TUY 给出。
- 函子性（缝合）只在原文 §5 用一句“It is obvious at this point”带过，没有证明。
- 共形块随复结构变化构成射影平坦丛；联络即 Hitchin/KZ，单值性给出映射类群表示。

## 关键公式

- $\mathcal{H}_\Sigma=H^0(\mathcal{M}_J,\mathcal{L}^{\otimes k})$
- $\dim\mathcal{H}_{S^2;R_1,R_2,R_3}=N_{R_1R_2R_3}$

## CS/WZW 的对象级等同

在固定复结构 $J$ 下，CS 的量子 Hilbert 空间 $\mathcal{H}_\Sigma$ 与 WZW 共形块空间作为向量空间同构；两边都等于 $H^0(\mathcal{M}_J,\mathcal{L}^{\otimes k})$。

**证明要点**（sketch）：

1. CS 侧：正则量子化给出 $H^0(\mathcal{M}_J,\mathcal{L}^{\otimes k})$（§3.1）。 *（全纯截面是量子态。）*
2. WZW 侧：共形块由 Ward 恒等式与 KZ 方程刻画，其解空间也是 $H^0$。 *（共形块是手征场的相关函数，KZ 把它们与全纯截面联系起来。）*
3. 两边维数一致且都由模空间上的同一线丛给出，故同构。 *（本文把这一步当作物理论证，未严格证明。）*

> **缺口**：本文只说“can be interpreted as”与“It is obvious at this point”；严格性由 Segal/TUY 补。

## 陷阱

- 不要把“同构”升级成“范畴等价”：函子性与缝合要额外证明。
- 共形块依赖复结构（$J$），但射影化后不依赖；别把 $J$ 依赖性说成物理依赖性。
- 标记点表示必须可积，否则维数为零。

## 相关卡片

- [holomorphic-sections](../concepts/holomorphic-sections.md)
- [cs-wzw-duality](../concepts/cs-wzw-duality.md)
- [knizhnik-zamolodchikov](../concepts/knizhnik-zamolodchikov.md)
- [fusion-rules](../concepts/fusion-rules.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.4 与 §5（共形块），印刷页 [373, 397] / PDF 页 [23, 47]（witten1989/sections/s05-hilbert.tex（§3.4）与 s09-applications.tex（§5））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
