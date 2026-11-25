# 局部卷积格拉斯曼流形

> `grassmann/concept/local-convolution-grassmannian` · 轨道 5 · BD Grassmannian 与辛纽结同调 · 状态 draft

> **先自测**：为什么这条链的终点纤维 $m_{\underline{\lambda}}^{-1}(L_0)$ 恰好只有整个卷积积的一半维数？

## 一句话

把仿射格拉斯曼流形中若干相邻的 Hecke 轨道串成一条链，得到带忘点映射 $m_{\underline{\lambda}}$ 的簇；它的顶维纤维就是张量积的不变量空间。

## 定义

设 $\underline{\lambda}=(\lambda_1,\dots,\lambda_k)$ 是 $G$ 的 $k$-元组支配权。局部卷积格拉斯曼流形定义为 $$\widetilde{\Gr}^{\underline{\lambda}}=\bigl\{(L_1,\dots,L_k)\in\Gr^k :\ L_0\xrightarrow{\lambda_1}L_1\xrightarrow{\lambda_2}\dots\xrightarrow{\lambda_{k-1}}L_{k-1}\xrightarrow{\lambda_k}L_k\bigr\},$$ 其中 $L_1\xrightarrow{\lambda}L_2$ 表示 $(L_1,L_2)$ 与 $(L_0,t^\lambda)$ 落在 $G^\vee(\mathcal{K})$ 在 $\Gr\times\Gr$ 上的同一轨道中。忘掉中间点得到 $m_{\underline{\lambda}}:\widetilde{\Gr}^{\underline{\lambda}}\to\Gr$，$(L_1,\dots,L_k)\mapsto L_k$，其像为 $\overline{\Gr^{\lambda_1+\dots+\lambda_k}}$。

**记号约定**：$L_0=t^0$ 是单位陪集；$\xrightarrow{\lambda}$ 只依赖两点的相对位置，因此是 $\Gr\times\Gr$ 中的局部闭条件；$m_{\underline{\lambda}}^{-1}(L_0)$ 称半维数纤维。

## 要点（为什么需要它）

- 卷积积是「相邻对的轨道条件」之交，链上每一步只约束相邻两点，所以中间点仍可自由滑动。
- $\lambda_i$ 全为微小时每个 $\Gr^{\lambda_i}$ 闭且射影，卷积积因此紧；这也是定理 2.1 能对它用反常层的前提。
- $m_{\underline{\lambda}}$ 是半小映射：$\dim m_{\underline{\lambda}}^{-1}(L_0)=\tfrac12\dim m_{\underline{\lambda}}^{-1}({}_0\Gr)$，于是顶维上同调落在中间维数上。
- 忘点映射的像不是单个轨道而是闭轨道 $\overline{\Gr^{\lambda_1+\dots+\lambda_k}}$：链的终点可以是任何 $\mu\le\sum\lambda_i$ 的轨道。

## 关键公式

$$
\widetilde{\Gr}^{\underline{\lambda}}=\bigl\{(L_1,\dots,L_k)\in\Gr^k :\ L_0\xrightarrow{\lambda_1}L_1\xrightarrow{\lambda_2}\dots\xrightarrow{\lambda_k}L_k\bigr\}
$$

$$
m_{\underline{\lambda}}:\widetilde{\Gr}^{\underline{\lambda}}\to\Gr,\qquad (L_1,\dots,L_k)\mapsto L_k,\qquad \operatorname{Im}m_{\underline{\lambda}}=\overline{\Gr^{\lambda_1+\dots+\lambda_k}}
$$

$$
\dim m_{\underline{\lambda}}^{-1}(L_0)=\tfrac12\dim m_{\underline{\lambda}}^{-1}({}_0\Gr)
$$

## 定理与证明（或缺口）

### 卷积积的像与半小性

$m_{\underline{\lambda}}$ 的像是闭轨道 $\overline{\Gr^{\lambda_1+\dots+\lambda_k}}$；并且 $m_{\underline{\lambda}}$ 是半小映射，故 $\dim m_{\underline{\lambda}}^{-1}(L_0)=\tfrac12\dim m_{\underline{\lambda}}^{-1}({}_0\Gr)$。

**证明状态：只引出处，原书不重证**


出处：中译 p.84、p.87（§2.1 的像的断言；半小性引 [MVi] 引理 4.4 的证明）

## 易错点

- 容易把 $\widetilde{\Gr}^{\underline{\lambda}}$ 当成 $G^\vee(\mathcal{K})$ 的单个轨道：$\Gr\times\Gr$ 的轨道才由 $\Lambda_+$ 标号，卷积积是若干相邻轨道条件的交，本身不是轨道。
- 容易把 $L_1\xrightarrow{\lambda}L_2$ 读成「$L_1\subset L_2$」这种包含关系：它是相对位置条件（落在同一条 $G^\vee(\mathcal{K})$-轨道里），不是格中的包含。

## 相关卡

- [几何 Satake 对应](../concepts/geometric-satake-correspondence.md)
- [整体卷积格拉斯曼流形](../concepts/global-convolution-grassmannian.md)
- [因子分解性质](../concepts/factorization-property.md)
- [仿射格拉斯曼流形](../concepts/affine-grassmannian.md)

## 出处

- ch5 §2.1 局部卷积格拉斯曼流形；中译 p.84（英文 PDF p.92），源码 `chapters/ch05.tex:68`
