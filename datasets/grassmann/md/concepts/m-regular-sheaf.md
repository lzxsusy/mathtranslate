# $M$-正则层

> `grassmann/concept/m-regular-sheaf` · 轨道 8 · 阿贝尔簇上的正则性 · 状态 draft

> **先自测**：为什么只把 $\operatorname{codim}V^i\ge i$ 一律加严成 $>i$，就足以让一个层在阿贝尔簇上整体生成？

## 一句话

把一般消没的余维下界 $\operatorname{codim}V^i\ge i$ 逐条加严成 $>i$，得到的层叫 $M$-正则层；它是 GV 条件的一阶强化，却足以推出生成性、nef 性与多典范的非常充裕性。

## 定义

设 $X$ 是 $g$ 维阿贝尔簇，$\widehat X=\operatorname{Pic}^0(X)$ 为其对偶，$\mathcal P$ 是 $X\times\widehat X$ 上的正规化 Poincaré 丛。对凝聚层 $\mathcal F$ 记 $$V^i(\mathcal F):=\{\alpha\in\widehat X\mid h^i(X,\mathcal F\otimes\alpha)>0\},\qquad \mathbf R\widehat{\mathcal S}(\mathcal F):=\mathbf R p_{\widehat X*}\bigl(p_X^*\mathcal F\otimes\mathcal P\bigr).$$ 若对一切 $i>0$ 都有 $$\operatorname{codim}_{\widehat X}\operatorname{Supp}\bigl(R^i\widehat{\mathcal S}(\mathcal F)\bigr)>i,$$ 等价地 $\operatorname{codim}V^i(\mathcal F)>i$（空集按 $+\infty$ 计），就称 $\mathcal F$ 是 **$M$-正则层**。作为对照：把严格不等号换成 $\ge$ 得到的是 $GV$-层（命题与定义 2.1）。

**记号约定**：$g=\dim X$；$\mathbf R\Delta\mathcal F:=\mathbf R\mathcal H om(\mathcal F,\mathcal O_X)$ 是 Grothendieck 对偶；$R^i\widehat{\mathcal S}$ 是 Fourier–Mukai 变换的高次直像；$IT_0$ 指所有 $i>0$ 的 $V^i$ 为空且 $R^0\widehat{\mathcal S}$ 局部自由。

## 要点（为什么需要它）

- $M$-正则 = $GV$ 的严格化：同样只查 $i>0$，但每条从 $\ge$ 收紧为 $>$；效果是每个支集分支的维数至多 $g-i-1$，比 $GV$ 的 $g-i$ 少一维。
- $i=0$ 一条必须排除：$V^0(\mathcal F)=\widehat X$ 恒成立，若也要 $\operatorname{codim}>0$，则一个 $M$-正则层都不剩（椭圆曲线例 7.14 正是靠 $i=1$ 才成立）。
- 由定理 2.3，$GV$ 等价于 $\mathbf R\Delta\mathcal F$ 满足 $WIT_g$ 且其变换是层；$M$-正则再要求该层无挠（命题 2.8），这就是整章的技术入口。
- 反例：$\mathcal O_X$ 的 $h^i=\wedge^iH^1(X,\mathcal O)\ne0\ (1\le i\le g)$，故 $V^i(\mathcal O_X)=\widehat X$ 对每个 $i$，连 $GV$ 都不是——不加扭转的结构层没有任何正则性。
- 『强一阶』是准确的说法：定义没有引入任何高阶消没假设，力量全来自那一格 $>$，它让 $\alpha$ 在开集里连续变动时截面能扫过参数方向（§5）。

## 关键公式

$$
V^i(\mathcal F)=\{\alpha\in\widehat X\mid h^i(X,\mathcal F\otimes\alpha)>0\}
$$

$$
\operatorname{codim}_{\widehat X}\operatorname{Supp}\bigl(R^i\widehat{\mathcal S}\mathcal F\bigr)>i\qquad(i>0)
$$

$$
\mathcal F\ \text{是 }M\text{-正则}\iff \mathbf R\widehat{\mathcal S}\bigl(\mathbf R\Delta\mathcal F\bigr)[g]\ \text{是无挠层}
$$

## 定理与证明（或缺口）

### $M$-正则性的两条基本性质

(1) 若 $\mathcal F$ 是 $M$-正则的，则 $\mathcal F$ 是 $GV$-层；(2) 对任意 $\alpha_0\in\operatorname{Pic}^0(X)$，$\mathcal F$ 是 $M$-正则的当且仅当 $\mathcal F\otimes\alpha_0$ 是 $M$-正则的。

**证明状态：完整**

1. 对每个 $i>0$，$M$-正则给 $\operatorname{codim}V^i(\mathcal F)>i$，特别地 $\ge i$，这正是 $GV$ 的余维条件。
   - *为什么*：$GV$ 与 $M$-正则只差不等号是否严格（命题与定义 2.1 对 2.7），严格条件逐条蕴含弱条件。
2. 把 $h^i(X,\mathcal F\otimes\alpha\otimes\beta)$ 里的 $\alpha\otimes\beta$ 记作 $\beta'$，得 $V^i(\mathcal F\otimes\alpha)=V^i(\mathcal F)-\alpha$，即 $\widehat X$ 中的一次平移。
   - *为什么*：线丛张量积的结合律与 $\operatorname{Pic}^0$ 的群结构；$\alpha\mapsto\alpha\otimes\beta$ 是 $\widehat X$ 的自同构。
3. 平移是同构，保维数与余维，故 $\operatorname{codim}V^i(\mathcal F\otimes\alpha)=\operatorname{codim}V^i(\mathcal F)>i$，$M$-正则性在 $\operatorname{Pic}^0$ 平移下不变（反向同理由取 $\alpha^{-1}$）。
   - *为什么*：判据只依赖余维，而余维在自同构下不变。


出处：中译 p.138，§2 定义 2.7 及其后的讨论（chapters/ch08.tex:101）

## 易错点

- 容易把定义 2.7 的两条都读成从 $i=0$ 起：那样 $\operatorname{codim}V^0=\operatorname{codim}\widehat X=0$，任何层都不合格，定义会空掉；原文的条件从 $i>0$ 起，读时别把编号看丢。
- 中译 p.138 定义 2.7 的第二条有一处把 $\operatorname{codim}V^i>i$ 的大于号排掉了（印成 $\operatorname{codim}V^i\ i$）；这是掉字，不是新条件，按大于号读。
- 别把余维的空集当成 $g$：若按 $\operatorname{codim}\varnothing=\dim\widehat X$ 算，$g=1$ 时 $\operatorname{codim}V^1>1$ 永不成立，椭圆曲线上就没有 $M$-正则层了；正确约定是空集余维 $+\infty$（等价写法 $\dim V^i\le g-i-1$）。

## 相关卡

- [$GV$-层](../concepts/gv-sheaf.md)
- [$M$-正则性的无挠判别](../concepts/torsion-freeness-criterion.md)
- [$GV$-层的 nef 性](../concepts/nefness-of-gv-sheaves.md)
- [椭圆曲线上的指标计算](../examples/elliptic-curve-regularity.md)

## 出处

- ch8 §2 一般消没与 $M$-正则性；中译 p.138（英文 PDF p.154），源码 `chapters/ch08.tex:101`
