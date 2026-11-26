# 中心层的 IW 像是倾斜层（定理 4.5.1）

> `sandvik25/concept/central-tilting` · 轨道 C · Iwahori–Whittaker 侧 · 状态 dev

> **先自测**：为什么中心层经平均之后变成倾斜层，重数公式又是怎么被证明的？

## 一句话

复合 $Z^{\mathrm{IW}}\colon\mathrm{Rep}(G^\vee)\xrightarrow{Z}\mathcal P_I\xrightarrow{\mathrm{Av}^{\mathrm{IW}}}\mathcal P_{\mathrm{IW}}$ 把每个 $V$ 送到倾斜层，且 $\Delta^{\mathrm{IW}}_\lambda$ 与 $\nabla^{\mathrm{IW}}_\lambda$ 的重数都等于 $\dim V_\lambda$。

## 定义

定义 $Z^{\mathrm{IW}}\colon\mathrm{Rep}(G^\vee)\xrightarrow{Z}\mathcal P_I\xrightarrow{\mathrm{Av}^{\mathrm{IW}}}\mathcal P_{\mathrm{IW}}$。定理 4.5.1（[ArBe]）：对一切 $V\in\mathrm{Rep}(G^\vee)$，$Z^{\mathrm{IW}}(V)$ 是倾斜层，且对一切 $\lambda\in X^\vee$ 有 $(Z^{\mathrm{IW}}(V):\Delta^{\mathrm{IW}}_\lambda)=(Z^{\mathrm{IW}}(V):\nabla^{\mathrm{IW}}_\lambda)=\dim V_\lambda$。

**记号**：$(X:\Delta)$ 表示 $\Delta$ 在滤链中的重数；倾斜层的标准重数与余标准重数相等。

## 要点（为什么需要它）

1. 倾斜 = 同时有标准滤链与余标准滤链；定理给出两侧重数相等，这正是倾斜性的等价刻画（在最高权范畴中）。
2. 重数公式与定理 2.5.3 的 Wakimoto 重数公式形式一致：都是「几何侧的重数 = 表示侧的权空间维数」，一个在 $\mathcal P_I$、一个在 $\mathcal P_{\mathrm{IW}}$。
3. 证明策略是「化归到极小情形」：先证张量封闭，再约到半单，最后只剩极小与拟极小的单模。
4. 拟极小情形是全文承认最难的一步，需要研究 $\mathcal P_I$ 的某些商；原文只写一句，没有细节。
5. 这条定理是 §5 整篇文章的动机：$F^{\mathrm{IW}}$ 把线丛 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)$ 送到 $\mathrm{Av}^{\mathrm{IW}}(\mathbb W_\lambda)$、把 $L_\lambda\otimes\mathcal O_{\widetilde{\mathcal N}}$ 送到倾斜层 $T^{\mathrm{IW}}(L_\lambda)$。

## 核心公式

$$
$Z^{\mathrm{IW}}(V):=\mathrm{Av}^{\mathrm{IW}}(Z(\mathrm{Sat}(V)))$$(Z^{\mathrm{IW}}(V):\Delta^{\mathrm{IW}}_\lambda)=(Z^{\mathrm{IW}}(V):\nabla^{\mathrm{IW}}_\lambda)=\dim V_\lambda$
$$

$$
$(Z^{\mathrm{IW}}(V):\Delta^{\mathrm{IW}}_\lambda)=(Z^{\mathrm{IW}}(V):\nabla^{\mathrm{IW}}_\lambda)=\dim V_\lambda$
$$

## 定理与证明（或缺口）

### 定理 4.5.1（Arkhipov–Bezrukavnikov）

$Z^{\mathrm{IW}}(V)$ 是倾斜层，且标准/余标准重数均为 $\dim V_\lambda$。

> 证明状态：**sketch**。第 3 步的拟极小情形原文只说「much more difficult」，未给论证；这是本卡标注的主要空白。

出处：`A p.11`

## 常见误解

- 把 $Z^{\mathrm{IW}}(V)$ 与 $Z(\mathrm{Sat}(V))$ 混同：前者是后者的平均像，一般不再是中心层（等变性被换成 IW）。
- 重数公式两边都用 $\dim V_\lambda$，但下标 $\lambda\in X^\vee$ 是余根格权重；若把 $V$ 理解为 $G$（而非 $G^\vee$）的表示，下标要对偶化。

## 相关卡

[IW 平均函子 $\mathrm{Av}^{\mathrm{IW}}$（定理 4.4.1）](../concepts/iw-averaging.md) · [中心层的 Wakimoto 滤链（定理 2.5.3）](../concepts/wakimoto-filtration.md) · [Wakimoto 滤链的重数如何变成 $\dim V_\lambda$](../derivations/wakimoto-multiplicity.md)

## 出处（印刷页）

- A p.11（A p.11）

> 说明：§4.5 与定理 4.5.1 的三步证明梗概全在 p.11。
