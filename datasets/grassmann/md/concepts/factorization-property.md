# 因子分解性质

> `grassmann/concept/factorization-property` · 轨道 5 · BD Grassmannian 与辛纽结同调 · 状态 draft

> **先自测**：为什么因子分解只能用在不重合的开集上，而两点真正碰撞处必须另找局部模型？

## 一句话

当标号分成两组、且跨组的点互不重合时，Beilinson–Drinfeld 格拉斯曼族精确分解为两个子族的乘积，是两点碰撞局部化的基本工具。

## 定义

设 $X$ 是光滑曲线，$\underline{\lambda}=(\lambda_1,\dots,\lambda_n)$ 是支配权组，$J_1,J_2$ 是 $(1,\dots,n)$ 的一个不相交分解，$\underline{\lambda}^i$ 由满足 $j\in J_i$ 的那些 $\lambda_j$ 组成。令 $U$ 为 $X^{\underline{\lambda}}$ 中满足「若 $j_1\in J_1$ 且 $j_2\in J_2$，则 $x_{j_1}\neq x_{j_2}$」的点 $[x_1,\dots,x_n]$ 所成的开集。则存在同构 $$\Gr_U^{\underline{\lambda}}\cong\bigl(\Gr_{X^{J_1}}^{\underline{\lambda}^1}\times\Gr_{X^{J_2}}^{\underline{\lambda}^2}\bigr)\big|_U,$$ 且该同构与到 $U$ 的两个投影都相容，即它是 $U$ 上两个族的同构而非逐纤维的同构。

**记号约定**：$X^{\underline{\lambda}}=X^n/\Sigma_{\underline{\lambda}}$；$\Gr_{X^n}^{\underline{\lambda}}$ 是整体奇异格拉斯曼族；$d_i$ 表示删去列表第 $i$、$i+1$ 项的算子；组内允许重合，只禁止跨组重合。

## 要点（为什么需要它）

- 条件只管「跨组不等」，组内可以重合——正因如此才能取 $J_2=\{i,i+1\}$ 把一次两点碰撞单独切成一个因子，而不必要求整组点互异。
- 结论是 $U$ 上的族同构（与两个投影相容），所以它不只比较纤维，还能把族上的截面、前推、单值性一起拆开。
- 本章两次用到它：命题 2.4(i) 把正则点的纤维写成乘积，引理 3.2 把开版本 ${}_0\Gr$ 拉进乘积并保持为邻域。
- 它把「奇异性」全部压到 $\Gr_{(y,y)}^{(\mu,\mu^\vee)}\cong\overline{\Gr^{\mu+\mu^\vee}}$ 这一个因子上，于是半局部几何变成两点问题。

## 关键公式

$$
\Gr_U^{\underline{\lambda}}\cong\bigl(\Gr_{X^{J_1}}^{\underline{\lambda}^1}\times\Gr_{X^{J_2}}^{\underline{\lambda}^2}\bigr)\big|_U
$$

$$
U=\{[x_1,\dots,x_n]\in X^{\underline{\lambda}}:\ j_1\in J_1,\ j_2\in J_2\ \Rightarrow\ x_{j_1}\neq x_{j_2}\}
$$

## 定理与证明（或缺口）

### 因子分解性质（定理 3.1，Beilinson–Drinfeld）

设 $X$ 是任意光滑曲线，$J_1,J_2$ 是 $(1,\dots,n)$ 的不相交分解，$U$ 如上。则 $\Gr_U^{\underline{\lambda}}\cong\bigl(\Gr_{X^{J_1}}^{\underline{\lambda}^1}\times\Gr_{X^{J_2}}^{\underline{\lambda}^2}\bigr)\big|_U$，且同构与到 $U$ 的两个投影相容。

**证明状态：只引出处，原书不重证**


出处：中译 p.89（§3 定理 3.1，直接引 [BD] §5.3.10）

## 易错点

- 容易把「不相交分解」读成「两组点各自互不重合」：定理的字面条件只是跨组不等，$J_2=\{i,i+1\}$ 时 $x_i=x_{i+1}=y$ 完全允许，否则引理 3.2 的两点碰撞根本没有开集可用。
- 容易把同构当成逐纤维同构：少了「与两个投影相容」这一句，就无法把因子分解沿 $U$ 上的路径搬运（单值性、常值前推都要用它）。

## 相关卡

- [局部卷积格拉斯曼流形](../concepts/local-convolution-grassmannian.md)
- [整体奇异格拉斯曼流形](../concepts/global-singular-grassmannian.md)
- [整体卷积格拉斯曼流形](../concepts/global-convolution-grassmannian.md)
- [仿射格拉斯曼流形](../concepts/affine-grassmannian.md)

## 出处

- ch5 §3 定理 3.1（因子分解性质）；中译 p.89（英文 PDF p.98），源码 `chapters/ch05.tex:296`
