# 整体奇异格拉斯曼流形

> `grassmann/concept/global-singular-grassmannian` · 轨道 5 · BD Grassmannian 与辛纽结同调 · 状态 draft

> **先自测**：把「每点 Hecke 型不超过该点 $\lambda$ 之和」写成逐点条件，为什么就足以让对角点纤维恰好是整条闭轨道？

## 一句话

只记录最终的主丛与整体同构 $\phi$、把每点的 Hecke 型放宽为不超过该点权之和，得到 $X^n$ 上的族；对角点纤维因此奇异，是本章的主要研究对象。

## 定义

整体奇异格拉斯曼流形定义为 $$\Gr_{X^n}^{\underline{\lambda}}:=\bigl\{((x_1,\dots,x_n),P,\phi):\ x_i\in X,\ P\text{ 是 }X\text{ 上的主 }G^\vee\text{-丛},\ \phi:P_0|_{X\setminus\{x_1,\dots,x_n\}}\to P|_{X\setminus\{x_1,\dots,x_n\}}\text{ 是同构},\ \text{且对每个 }x\in X,\ \phi\text{ 在 }x\text{ 处具有 Hecke 型 }\le\textstyle\sum_{i:x_i=x}\lambda_i\bigr\}.$$ 它同样是 $X^n$ 上的族：正则点上纤维是 $\Gr^{\lambda_1}\times\dots\times\Gr^{\lambda_n}$ 且 $\widetilde{\Gr}_{X_{\mathrm{reg}}^n}^{\underline{\lambda}}\cong\Gr_{X_{\mathrm{reg}}^n}^{\underline{\lambda}}$；小对角线上纤维是（通常奇异的）$\overline{\Gr^{\lambda_1+\dots+\lambda_n}}$。

**记号约定**：$\le\sum_{i:x_i=x}\lambda_i$ 是支配序意义下的不等式，等价于落在闭轨道 $\overline{\Gr^{\nu}}$ 中（$\nu$ 为该和）；$\supp(D)$ 是染色除子 $D$ 的支撑。

## 要点（为什么需要它）

- 它只有一份整体同构 $\phi$，没有中间丛，所以对角点处无法拆成两个独立因子——这正是 §3 要处理的「不分解」。
- 定义里的型条件是 $\le$ 而不是 $=$：$\le\nu$ 对应整条闭轨道 $\overline{\Gr^\nu}=\bigcup_{\mu\le\nu}\Gr^\mu$，奇异性就是被这些更小的轨道层造出来的。
- 存在显然的映射 $\widetilde{\Gr}_{X^n}^{\underline{\lambda}}\to\Gr_{X^n}^{\underline{\lambda}}$：在正则点上是一一对应，在小对角线上就是 $m_{\underline{\lambda}}$。
- 把点按 $\Sigma_{\underline{\lambda}}$ 商掉后得到 $\Gr_{X^{\underline{\lambda}}}^{\underline{\lambda}}\to X^{\underline{\lambda}}$，其点可写成 $(D,P,\phi)$，$D$ 是总权为 $\sum\lambda_i$ 的 $\Lambda_+$-染色除子。

## 关键公式

$$
\Gr_{X^n}^{\underline{\lambda}}:=\bigl\{((x_i),P,\phi):\ \phi:P_0|_{X\setminus\{x_1,\dots,x_n\}}\to P|_{X\setminus\{x_1,\dots,x_n\}},\ \text{每点 Hecke 型}\le\textstyle\sum_{i:x_i=x}\lambda_i\bigr\}
$$

$$
\Gr_{X^{\underline{\lambda}}}^{\underline{\lambda}}=\{(D,P,\phi):\ \textstyle\sum_{x}D(x)=\sum_i\lambda_i,\ \phi\text{ 在 }x\text{ 处型}\le D(x)\}
$$

$$
\widetilde{\Gr}_{X_{\mathrm{reg}}^n}^{\underline{\lambda}}\cong\Gr_{X_{\mathrm{reg}}^n}^{\underline{\lambda}}
$$

## 定理与证明（或缺口）

### 命题 2.4（整体奇异族的纤维）

(i) 正则点上方的纤维仍是 $\Gr^{\lambda_1}\times\dots\times\Gr^{\lambda_n}$，且 $\widetilde{\Gr}_{X_{\mathrm{reg}}^n}^{\underline{\lambda}}\cong\Gr_{X_{\mathrm{reg}}^n}^{\underline{\lambda}}$；(ii) 小对角线上点上方的纤维是（通常奇异的）簇 $\overline{\Gr^{\lambda_1+\dots+\lambda_n}}$。

**证明状态：提纲（有缺口）**

1. 正则点：各 $x_i$ 互异，逐点条件 $\le\sum_{i:x_i=x}\lambda_i$ 退化为「在 $x_i$ 处型 $\le\lambda_i$」这一组互不干扰的局部条件，于是族按 $J_i=\{i\}$ 因子分解成乘积。
   - *为什么*：因子分解性质（定理 3.1）在跨组点互不重合时给出族同构，而正则点恰好满足该前提。
2. 对角点：所有 $x_i=y$，型条件变成单点上的 $\le\lambda_1+\dots+\lambda_n$，即 $\phi$ 落在 $\overline{\Gr^{\lambda_1+\dots+\lambda_n}}$ 中。
   - *为什么*：$\Gr$ 中「型 $\le\nu$」的轨迹按定义就是闭轨道 $\overline{\Gr^\nu}$。

> **缺口**：命题 2.4 在章内没有证明。第 (i) 步可由因子分解性质补出；第 (ii) 步我写不下去：要断言纤维「恰好」是整条 $\overline{\Gr^{\nu}}$，需说明从平凡丛到平凡丛、在 $y$ 外同构、型 $\le\nu$ 的每个 $\phi$ 都能实现，这要用命题 2.2 的向量丛夹逼判据去构造，我没有完成该构造。


出处：中译 p.86（§2.4 命题 2.4）

## 易错点

- 容易把整体奇异版当成整体卷积版的另一种写法：前者只记 $(P,\phi)$，后者记 $(P_1,\dots,P_n)$，两族只在正则点上同构，小对角线上一个是闭包、一个是卷积积，不能互相替代。
- 容易把型条件里的 $\le$ 写成 $=$：取等号会把闭轨道 $\overline{\Gr^\nu}$ 换成单个轨道 $\Gr^\nu$，低维层被丢掉，奇异性与「不分解」现象一起消失。

## 相关卡

- [整体卷积格拉斯曼流形](../concepts/global-convolution-grassmannian.md)
- [因子分解性质](../concepts/factorization-property.md)
- [部分 Grothendieck 解消与幂零切片](../concepts/partial-grothendieck-resolution-and-nilpotent-slice.md)
- [$SL_2$ 两点碰撞的最小例子](../examples/sl2-two-point-collision.md)
- [仿射格拉斯曼流形](../concepts/affine-grassmannian.md)
- [沿曲线的因子化：SU(2) 能级 1 的维数核对](../examples/factorization-along-a-curve.md)

## 出处

- ch5 §2.4 整体奇异格拉斯曼流形；中译 p.86（英文 PDF p.95），源码 `chapters/ch05.tex:151`
