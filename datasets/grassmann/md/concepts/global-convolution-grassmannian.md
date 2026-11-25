# 整体卷积格拉斯曼流形

> `grassmann/concept/global-convolution-grassmannian` · 轨道 5 · BD Grassmannian 与辛纽结同调 · 状态 draft

> **先自测**：既然纤维只在正则点与对角点上被描述清楚，为什么还要造整个 $X^n$ 上的族？

## 一句话

把权 $\lambda_i$ 换成曲线上的点 $x_i$、把相邻 Hecke 型写成链条件，得到 $X^n$ 上记录全部中间丛的族；它是对角点处卷积积的整体版本。

## 定义

固定 $G$ 的 $n$-元组微小支配权 $\underline{\lambda}=(\lambda_1,\dots,\lambda_n)$。整体卷积格拉斯曼流形是簇 $$\widetilde{\Gr}_{X^n}^{\underline{\lambda}}:=\bigl\{((x_1,\dots,x_n),(P_1,\dots,P_n),(\phi_1,\dots,\phi_n)):\ x_i\in X,\ P_i\text{ 是 }X\text{ 上的主 }G^\vee\text{-丛},\ \phi_i:P_{i-1}|_{X\setminus x_i}\to P_i|_{X\setminus x_i}\text{ 在 }x_i\text{ 处具有 Hecke 型 }\lambda_i\bigr\},$$ 配投影 $\tilde{p}:\widetilde{\Gr}_{X^n}^{\underline{\lambda}}\to X^n$，并对 $A\subset X^n$ 记 $\widetilde{\Gr}_A^{\underline{\lambda}}=\tilde{p}^{-1}(A)$。正则点上方纤维同构于 $\Gr^{\lambda_1}\times\dots\times\Gr^{\lambda_n}$，小对角线上方纤维是局部卷积积 $\Gr^{\lambda_1}\widetilde{\times}\dots\widetilde{\times}\Gr^{\lambda_n}$。

**记号约定**：$P_0$ 是 $X$ 上的平凡 $G^\vee$-丛；$X_{\mathrm{reg}}^n=\{(x_1,\dots,x_n):x_i\neq x_j\ (i\neq j)\}$；小对角线是 $X=\{(x,\dots,x)\}\subset X^n$。

## 要点（为什么需要它）

- 它记住全部中间丛 $(P_1,\dots,P_n)$，这是与奇异版的唯一实质差别：奇异版只留最后的 $(P,\phi)$。
- 正则点上方是乘积、小对角线上方是卷积积；两种纤维由同一个定义在不同点处自动给出，不需要分别定义。
- 命题 2.3 说前推 $R^k\tilde{p}_*\mathbb{C}$ 是常值层，因此沿 $X_{\mathrm{reg}}^n$ 的单值性作用平凡——这是「辫群作用只通过 $\Sigma_{\underline{\lambda}}$ 分解」的技术来源。
- 把 $P_n$ 钉成平凡丛得到开版本 ${}_0\widetilde{\Gr}$，它才可能形变收缩到半维数纤维 $m_{\underline{\lambda}}^{-1}(L_0)$。

## 关键公式

$$
\widetilde{\Gr}_{X^n}^{\underline{\lambda}}:=\bigl\{((x_i),(P_i),(\phi_i)):\ \phi_i:P_{i-1}|_{X\setminus x_i}\to P_i|_{X\setminus x_i}\text{ 在 }x_i\text{ 处具有 Hecke 型 }\lambda_i\bigr\}
$$

$$
\tilde{p}:\widetilde{\Gr}_{X^n}^{\underline{\lambda}}\longrightarrow X^n,\qquad \widetilde{\Gr}_A^{\underline{\lambda}}=\tilde{p}^{-1}(A)
$$

## 定理与证明（或缺口）

### 命题 2.3（前推是常值层）

前推 $R^k\tilde{p}_*\mathbb{C}_{\widetilde{\Gr}_{X^n}^{\underline{\lambda}}}$ 是 $X^n$ 上的常值层。

**证明状态：只引出处，原书不重证**


出处：中译 p.86（§2.3 命题 2.3；证明见 [MVi] 引理 6.1 的证明）

## 易错点

- 容易把正则点上的纤维也算成卷积积：只有小对角线（所有 $x_i$ 相等）上纤维才是 $\Gr^{\lambda_1}\widetilde{\times}\dots\widetilde{\times}\Gr^{\lambda_n}$，正则点上它是普通乘积。
- 容易把 $\widetilde{\Gr}_{X^n}^{\underline{\lambda}}$ 与开版本 ${}_0\widetilde{\Gr}$ 混用：前者对 $P_n$ 不加条件，纤维一般不是仿射的；后者把 $P_n$ 钉成平凡丛，代价是当 $\sum\lambda_i$ 不在根格时整族为空。

## 相关卡

- [整体奇异格拉斯曼流形](../concepts/global-singular-grassmannian.md)
- [局部卷积格拉斯曼流形](../concepts/local-convolution-grassmannian.md)
- [因子分解性质](../concepts/factorization-property.md)
- [沿曲线的因子化：SU(2) 能级 1 的维数核对](../examples/factorization-along-a-curve.md)

## 出处

- ch5 §2.3 整体卷积格拉斯曼流形；中译 p.85（英文 PDF p.94），源码 `chapters/ch05.tex:132`
