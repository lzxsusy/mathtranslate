# 仿射格拉斯曼流形

> `grassmann/concept/affine-grassmannian` · 轨道 A · 跨章基础 · 状态 draft

> **先自测**：为什么只有微小权的轨道才闭，而这一点恰好是几何 Satake 对应能用的前提？

## 一句话

仿射格拉斯曼流形是 $G^\vee(\mathcal K)/G^\vee(\mathcal O)$，其轨道由支配权标号；只有微小权的轨道闭且射影，闭包由支配序给出，几何 Satake 由此把卷积翻译成张量积。

## 定义

设 $G$ 是复约化群、$G^\vee$ 是其 Langlands 对偶群，$\mathcal K=\mathbb C((t))$、$\mathcal O=\mathbb C[[t]]$。$G^\vee$ 的**仿射格拉斯曼流形**定义为 $\mathrm{Gr}=G^\vee(\mathcal K)/G^\vee(\mathcal O)$。对支配权 $\lambda\in\Lambda_+$，记 $\mathrm{Gr}^\lambda$ 为经过 $t^\lambda$ 的 $G^\vee(\mathcal O)$-轨道，$L_0=t^0$ 为单位陪集。轨道 $\mathrm{Gr}^\lambda$ 闭（因而射影）当且仅当 $\lambda$ 是**微小权**（minuscule weight）。

**记号约定**：$\Lambda$ 是 $G$ 的权格，等同于 $G^\vee$ 的余权格；$\Lambda_+$ 为支配权；$\mu\le\lambda$ 指 $\lambda-\mu$ 是正根之和。$\mathrm{Gr}$ 是 ind-概形，每个 $\mathrm{Gr}^\lambda$ 有限维。

## 要点（为什么需要它）

- $\mathrm{Gr}$ 是 ind-概形而不是概形，$L_0$ 只是单位陪集，$\mathrm{Gr}$ 本身没有群结构。
- 轨道闭、射影、$\lambda$ 微小三件事等价；微小权都是基本权，所以互异的微小权线性无关。
- 闭包公式 $\overline{\mathrm{Gr}^\lambda}=\bigcup_{\mu\le\lambda}\mathrm{Gr}^\mu$ 说明闭包的边界正是低维轨道，光滑轨迹恰为 $\mathrm{Gr}^\lambda$。
- $\mathrm{Gr}\times\mathrm{Gr}$ 的 $G^\vee(\mathcal K)$-轨道同样由 $\Lambda_+$ 标号，记作 $L_1\xrightarrow{\lambda}L_2$，这是卷积格拉斯曼的字母表。

## 关键公式

$$
\mathrm{Gr}=G^\vee(\mathcal K)/G^\vee(\mathcal O)
$$

$$
\overline{\mathrm{Gr}^\lambda}=\bigcup_{\mu\le\lambda}\mathrm{Gr}^\mu
$$

$$
H^*(\mathrm{Gr}^\lambda)\cong V_\lambda
$$

## 定理与证明（或缺口）

### 定理 2.1（几何 Satake 的 BD 版本）

设 $\lambda_1,\dots,\lambda_n$ 都是微小权。则存在典范同构 (i) $H^*(\mathrm{Gr}^\lambda)\cong V_\lambda$；(ii) $H^*(\widetilde{\mathrm{Gr}}^{\underline\lambda})\cong V_{\lambda_1}\otimes\cdots\otimes V_{\lambda_n}$；(iii) $H^{\mathrm{top}}(m_{\underline\lambda}^{-1}(L_0))\cong(V_{\lambda_1}\otimes\cdots\otimes V_{\lambda_n})^G$，且 (ii)(iii) 与包含映射诱导的拉回构成交换图表。

**证明状态：提纲（有缺口）**

1. 几何 Satake 对应给出 $G^\vee(\mathcal O)$-等变反常层范畴与 $\mathrm{Rep}(G)$ 的张量等价，并与导出整体截面（纤维函子）相容。
   - *为什么*：这是本章唯一的输入，见 [MVi] 定理 7.3。
2. $\lambda$ 微小时 $\mathbb C_{\mathrm{Gr}^\lambda}[\dim\mathrm{Gr}^\lambda]$ 是反常层，该等价把它送到 $V_\lambda$，得到 (i)。
   - *为什么*：轨道闭且光滑，常数层的移位才是反常层。
3. 卷积层 $(m_{\underline\lambda})_*\mathbb C_{\widetilde{\mathrm{Gr}}^{\underline\lambda}}[\dim]$ 送到 $V_{\lambda_1}\otimes\cdots\otimes V_{\lambda_n}$，再取 $m_{\underline\lambda}^{-1}(L_0)$ 的顶维上同调即得 (ii)(iii)。
   - *为什么*：球 Hecke 范畴中张量积的定义，加上半小映射的分解定理。

> **缺口**：本章的证明只有三行，实质输入是 [MVi] 定理 7.3 的几何 Satake 等价；等价本身的证明、$m_{\underline\lambda}$ 的半小性与分解定理都未展开，故记为 sketch。


出处：中译 p.84（§2.1 定理 2.1）

## 易错点

- 把 $\mathrm{Gr}$ 当成概形或群：它是 ind-概形，$L_0$ 只是单位陪集，$\mathrm{Gr}$ 没有群结构。
- 对任意支配权都断言 $\overline{\mathrm{Gr}^\lambda}$ 光滑：只有微小权才光滑；$SL_2$ 的 $2\omega$ 就是反例（闭包含低维轨道）。
- 把 $G$ 与 $G^\vee$ 混写：几何全在 $G^\vee$ 一侧，$\lambda$ 是 $G$ 的权、$G^\vee$ 的余权；写成 $G(\mathcal K)/G(\mathcal O)$ 整段失效。
- 把「支配」当成「闭」的判据：支配只保证轨道存在，闭不闭只看微小性。

## 相关卡

- [几何 Satake 对应](../concepts/geometric-satake-correspondence.md)
- [局部卷积格拉斯曼流形](../concepts/local-convolution-grassmannian.md)
- [因子分解性质](../concepts/factorization-property.md)

## 出处

- ch5 §2.1 仿射格拉斯曼流形的定义；中译 p.84（英文 PDF p.92），源码 `chapters/ch05.tex:62`
