# 几何 Satake 对应

> `grassmann/concept/geometric-satake-correspondence` · 轨道 5 · BD Grassmannian 与辛纽结同调 · 状态 draft

> **先自测**：为什么偏偏是「等变反常层」这一层范畴，而不是所有构造层，才与表示范畴等价？

## 一句话

把仿射格拉斯曼流形上等变反常层构成的球 Hecke 范畴与 Langlands 对偶群的表示范畴作张量等价，并保持纤维函子；本章的同调—表示对照全靠它。

## 定义

设 $G$ 是复约化群、$G^\vee$ 是其 Langlands 对偶，$\Gr=G^\vee(\mathcal{K})/G^\vee(\mathcal{O})$。考虑 $\Gr$ 上 $G^\vee(\mathcal{O})$-等变反常层（即球 Hecke 范畴，spherical Hecke category）及其上的卷积张量积。**几何 Satake 对应**断言：存在该张量范畴与 $G$ 的有限维表示范畴之间的张量范畴等价，且与「取纤维」的函子相容——后者在几何一侧就是导出整体截面。微小时它把 $\mathbb{C}_{\Gr^\lambda}[\dim\Gr^\lambda]$ 送到 $V_\lambda$。

**记号约定**：$\mathcal{K}=\mathbb{C}((t))$，$\mathcal{O}=\mathbb{C}[[t]]$；$[\dim\Gr^\lambda]$ 是反常层意义下的移位；「与纤维函子相容」指下图与取整体截面交换。

## 要点（为什么需要它）

- 等变条件（$G^\vee(\mathcal{O})$-等变）不可省：它把巨大的层范畴压到刚好对应有限维表示的那一片。
- 对应是张量的，所以「几何的卷积积」翻译成「表示的张量积」，「取纤维」翻译成「取 $G$-不变量」，两件事一次翻译完。
- 只有微小的 $\lambda$ 才能用 $\mathbb{C}_{\Gr^\lambda}[\dim]$：此时 $\Gr^\lambda$ 闭且光滑，移位常数层才是反常层。
- 它给出定理 2.1 的全部三条同构，而定理 2.1 又是 §2.5 中间上同调结论的唯一入口。

## 关键公式

$$
H^*(\Gr^\lambda)\cong V_\lambda
$$

$$
H^*(\widetilde{\Gr}^{\underline{\lambda}})\cong V_{\lambda_1}\otimes\dots\otimes V_{\lambda_n}
$$

$$
H^{\mathrm{top}}\bigl(m_{\underline{\lambda}}^{-1}(L_0)\bigr)\cong(V_{\lambda_1}\otimes\dots\otimes V_{\lambda_n})^G
$$

## 定理与证明（或缺口）

### 定理 2.1（几何 Satake 的 BD 版）

设所有 $\lambda_i$ 均为微小权。则存在典范同构 (i) $H^*(\Gr^\lambda)\cong V_\lambda$；(ii) $H^*(\widetilde{\Gr}^{\underline{\lambda}})\cong V_{\lambda_1}\otimes\dots\otimes V_{\lambda_n}$；(iii) $H^{\mathrm{top}}(m_{\underline{\lambda}}^{-1}(L_0))\cong(V_{\lambda_1}\otimes\dots\otimes V_{\lambda_n})^G$。并且 (ii)(iii) 的同构与包含 $m_{\underline{\lambda}}^{-1}(L_0)\hookrightarrow\widetilde{\Gr}^{\underline{\lambda}}$ 诱导的拉回构成交换图表。

**证明状态：完整**

1. 把几何 Satake 对应用在单个轨道上：$\lambda$ 微小时 $\mathbb{C}_{\Gr^\lambda}[\dim\Gr^\lambda]$ 是反常层，对应把它送到 $V_\lambda$，取整体截面上同调即得 (i)。
   - *为什么*：几何 Satake 是张量范畴等价，必然把每个对象送到某个表示；微小的 $\lambda$ 使 $\Gr^\lambda$ 闭、光滑、射影，移位常数层才落在反常层范畴内并对应最高权表示。
2. 把对应用在卷积积上：由球 Hecke 范畴上张量积的定义，$(m_{\underline{\lambda}})_*\mathbb{C}_{\widetilde{\Gr}^{\underline{\lambda}}}[\dim\widetilde{\Gr}^{\underline{\lambda}}]$ 被送到 $V_{\lambda_1}\otimes\dots\otimes V_{\lambda_n}$，取上同调得 (ii)。
   - *为什么*：卷积积在层一侧的定义正是「外积再沿 $m_{\underline{\lambda}}$ 前推」，而对应是张量的，外积对应张量积、前推对应取不变量前的张量积。
3. 把 (ii) 限制到纤维 $m_{\underline{\lambda}}^{-1}(L_0)$：它的顶维上同调对应张量积中的 $G$-不变量，得 (iii)；交换性由构造（拉回—前推的相容）显然。
   - *为什么*：纤维函子在几何一侧是导出整体截面，在表示一侧是 $G$-不变量函子；$m_{\underline{\lambda}}^{-1}(L_0)$ 是半维数纤维，其顶维恰好承担全部不变量部分。


出处：中译 p.84（§2.1 定理 2.1 及其证明，引 [MVi] 定理 7.3、§4、§5）

## 易错点

- 容易把「球 Hecke 范畴」记成 $\Gr$ 上的全反常层范畴：丢掉 $G^\vee(\mathcal{O})$-等变条件后，对应的不再是 $G$ 的表示范畴，定理 2.1 的三条同构全部失效。
- 容易忽略「微小」这个前提：$\lambda$ 不微小时 $\Gr^\lambda$ 不闭，$\mathbb{C}_{\Gr^\lambda}[\dim]$ 根本不是反常层，谈不上被送到 $V_\lambda$。

## 相关卡

- [局部卷积格拉斯曼流形](../concepts/local-convolution-grassmannian.md)
- [因子分解性质](../concepts/factorization-property.md)
- [仿射格拉斯曼流形](../concepts/affine-grassmannian.md)
- [曲线算子](../concepts/curve-operator.md)

## 出处

- ch5 §2.1 定理 2.1；中译 p.84（英文 PDF p.93），源码 `chapters/ch05.tex:92`
