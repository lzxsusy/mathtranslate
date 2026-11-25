# $SL_2$ 两点碰撞的最小例子

> `grassmann/example/sl2-two-point-collision` · 轨道 5 · BD Grassmannian 与辛纽结同调 · 状态 draft

> **这张卡练什么**：两点相撞时卷积版纤维只有 $\mathbb{P}^1$，奇异版纤维却是二维的，这个维数差究竟是被丢掉的哪个自由度？

## 一句话

取 $G=SL_2$、$\underline{\lambda}=(\omega,\omega)$、两点相撞，逐步算出卷积纤维 $\mathbb{P}^1$、奇异纤维 $\overline{\Gr^{2\omega}}$ 与半维数等式，是全章唯一能完整验算的碰撞模型。

## 背景定义

**半局部几何**：设 $\mu=\lambda_i=\lambda_{i+1}^\vee$，$x=[x_1,\dots,x_n]$ 满足 $y=x_i=x_{i+1}$ 而其余点互异。由因子分解性质，$\Gr_x^{\underline{\lambda}}\cong\Gr_{d_i(x)}^{d_i(\underline{\lambda})}\times\Gr_{(y,y)}^{(\mu,\mu^\vee)}$，其中第二个因子同构于闭轨道 $\overline{\Gr^{\mu+\mu^\vee}}$，它是奇异的；$\Gr^{d_i(\underline{\lambda})}_{d_i(x)}$ 则以「$\phi$ 在 $y$ 处可延拓（型 $0$）」的轨迹嵌入其中。

## 设定

取 $G=SL_2$（自对偶，$G^\vee=SL_2$ 亦可），$\underline{\lambda}=(\omega,\omega)$，$n=2$，$\mu=\lambda_1=\omega=\omega^\vee=\lambda_2^\vee$；取 $x=[x_1,x_2]\in\mathbb{P}^{1^{\underline{\lambda}}}$ 使 $x_1=x_2=y$、其余点条件空洞。此时 $d_i(x)$ 与 $d_i(\underline{\lambda})$ 都删空，因子分解性质给出 $$\Gr_x^{(\omega,\omega)}\cong\Gr_{(y,y)}^{(\omega,\omega)}\cong\overline{\Gr^{2\omega}}.$$ 同时 $\Gr^\omega\cong\mathbb{P}^1$，$\dim\Gr^\omega=\langle\omega,2\rho^\vee\rangle=1$，$\dim\Gr^{2\omega}=2$。

## 计算

第一步（卷积纤维）：$\omega^\vee=\omega$，故 $L_0\xrightarrow{\omega}L_1$ 与 $L_1\xrightarrow{\omega}L_0$ 是同一个对称条件，$$m_{(\omega,\omega)}^{-1}(L_0)=\{L_1:L_0\xrightarrow{\omega}L_1\xrightarrow{\omega}L_0\}=\Gr^{\omega}\cong\mathbb{P}^1,$$ 维数 $1$。第二步（整个卷积积的维数）：在正则点 $(y+u,y-u)$ 上纤维是 $\Gr^\omega\times\Gr^\omega$，维数 $1+1=2$，而族在 $u\to0$ 时维数不跳，故 $\dim\widetilde{\Gr}^{(\omega,\omega)}=2$，于是 $\dim m^{-1}(L_0)=1=\tfrac12\cdot2$，半小性等式成立。第三步（取顶维上同调）：$H^{\mathrm{top}}(m^{-1}(L_0))=H^2(\mathbb{P}^1)=\mathbb{C}$；表示一侧 $(V^\omega\otimes V^\omega)^{SL_2}=\mathbb{C}$（由 $SL_2$ 的不变辛形式给出），两边都是 $1$ 维，与定理 2.1(iii) 吻合。第四步（奇异纤维）：由命题 2.4(ii)，$(y,y)$ 上的奇异纤维是 $\overline{\Gr^{2\omega}}$，维数 $2$，它比卷积纤维多出的那一维正是被忘掉的中间丛 $L_1$ 的自由度——卷积版把 $L_1$ 记下来，奇异版只留下 $\phi$。

## 要点

- $SL_2$、$\lambda=(\omega,\omega)$ 是所有构造都退化成 $\mathbb{P}^1$ 的最小情形：$\Gr^\omega=\mathbb{P}^1$，卷积积是两条 $\mathbb{P}^1$ 的链，维数 $2$。
- 取 $\lambda_{i+1}=\lambda_i^\vee$ 是必要的：否则 $L_0\xrightarrow{\lambda_1}L_1\xrightarrow{\lambda_2}L_0$ 无解，半维数纤维是空的，整个半局部图像不成立。
- 维数核对 $1=\tfrac12\cdot2$ 是全章唯一能一行验算的半小性实例，也是理解「顶维上同调 = 中间上同调」的最短路径。
- 奇异纤维 $\overline{\Gr^{2\omega}}$ 比卷积纤维多一维，多出的正是中间丛：这解释了为什么卷积版是解消、奇异版只留结果。

## 关键公式

$$
\Gr_{(y,y)}^{(\omega,\omega)}\cong\overline{\Gr^{2\omega}},\qquad \dim\overline{\Gr^{2\omega}}=2
$$

$$
m_{(\omega,\omega)}^{-1}(L_0)=\{L_1:L_0\xrightarrow{\omega}L_1\xrightarrow{\omega}L_0\}\cong\mathbb{P}^1,\qquad \dim=1=\tfrac12\cdot2
$$

$$
H^{\mathrm{top}}\bigl(m^{-1}(L_0)\bigr)=H^2(\mathbb{P}^1)=\mathbb{C}=(V^\omega\otimes V^\omega)^{SL_2}
$$

## 相关定理

- **半维数等式在 $SL_2$ 最小情形下的验证**：对 $G=SL_2$、$\underline{\lambda}=(\omega,\omega)$，有 $\dim m_{\underline{\lambda}}^{-1}(L_0)=\tfrac12\dim\widetilde{\Gr}^{(\omega,\omega)}$，且 $H^{\mathrm{top}}(m_{\underline{\lambda}}^{-1}(L_0))\cong(V^\omega\otimes V^\omega)^{SL_2}$。

## 易错点

- 容易把中译 p.89 的「特异点」读成「奇点」：原文是 distinguished point，指纤维中对应「平凡丛 + 平凡同构」、即 Hecke 型 $0$ 的那一点，它是光滑点、是嵌入 $\Gr^{d_i(\underline{\lambda})}_{d_i(x)}$ 的基点；当成奇点会把 §3.2 的图像整个搞反。
- 容易把奇异纤维写成开轨道 $\Gr^{2\omega}$ 而忘了闭包：型条件是 $\le2\omega$，型为 $\omega$ 的层也在纤维里，少了它维数从 $2$ 掉到 $2$ 虽看不出，但奇异性与「不分解」现象全部消失。

## 用到哪些概念

- [因子分解性质](../concepts/factorization-property.md)
- [整体奇异格拉斯曼流形](../concepts/global-singular-grassmannian.md)
- [局部卷积格拉斯曼流形](../concepts/local-convolution-grassmannian.md)

## 相关卡

- [因子分解性质](../concepts/factorization-property.md)
- [局部卷积格拉斯曼流形](../concepts/local-convolution-grassmannian.md)
- [整体奇异格拉斯曼流形](../concepts/global-singular-grassmannian.md)
- [沿曲线的因子化：SU(2) 能级 1 的维数核对](../examples/factorization-along-a-curve.md)

## 出处

- ch5 §3.1–3.2 两点碰撞的半局部几何；中译 p.89（英文 PDF p.98），源码 `chapters/ch05.tex:310`
