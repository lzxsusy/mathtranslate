# 大 Hecke 叠 $\mathcal H^i$ 与整体函子

> `gaits04/concept/big-hecke` · 轨 D 层化与猜想 · 状态 reviewed · 核验 source-only

**问题：** 为什么要把 $x$ 变成变量？

**一句话：** 让 $x$ 沿曲线移动，得到带映射 $s:\mathcal H^i\to X$ 的大 Hecke 叠；相应的函子 $T^i:D^b(\mathfrak{B}\mathrm{un}_n)\to D^b(X\times\mathfrak{B}\mathrm{un}_n)$ 把第 $i$ 个 Hecke 本征条件写成一个等式。

**别名：** `big Hecke stack`、`Hecke functor over X`

## 定义

可以做得更好：让点 $x$ 沿曲线移动。引入「大」Hecke 叠 $\mathcal H^i$ 如下：$\operatorname{Hom}(S,\mathcal H^i)$ 是四元组 $(\phi,M,M',\beta)$ 的范畴，其中 $M,M'$ 同前，$\phi$ 是映射 $S\to X$，$\beta$ 仍是凝聚层的嵌入 $M\hookrightarrow M'$，使得商支撑在图像 $\Gamma_\phi\subset X\times S$ 上，且其上秩 $i$ 的向量丛。除原有的投影 $h^{\leftarrow},h^{\rightarrow}:\mathcal H^i\to\mathfrak{B}\mathrm{un}_n$ 外，现在还有自然映射 $s:\mathcal H^i\to X$，把四元组 $(\phi,M,M',\beta)$ 送到 $\phi$。对固定 $x\in X$，有 $s^{-1}(x)\simeq\mathcal H_x^i$。定义 Hecke 函子 $T^i:D^b(\mathfrak{B}\mathrm{un}_n)\to D^b(X\times\mathfrak{B}\mathrm{un}_n)$ 为 $\mathcal F\mapsto(s\times h^{\rightarrow})_!((h^{\leftarrow})^*\mathcal F)[i(n-i)]$。

**记号：** $\mathcal H^i$：大 Hecke 叠；$s:\mathcal H^i\to X$：记录 $x$ 的映射；$s\times h^{\rightarrow}:\mathcal H^i\to X\times\mathfrak{B}\mathrm{un}_n$。

## 要点

- $s$ 的出现使「对所有 $x$ 的 Hecke 条件」可以写成一个对象：$T^i(\mathcal F)$ 是 $X\times\mathfrak{B}\mathrm{un}_n$ 上的层。
- 固定 $x$ 时 $s^{-1}(x)\simeq\mathcal H_x^i$，故大函子在每个纤维上退化为 §3.2 的局部函子。
- 本征条件 $T^i(\mathcal F)\simeq E\boxtimes\mathcal F$ 里的 $E$ 正是 $X$ 上的局部系统——把「每个 $x$ 一个特征值」打包成「$X$ 上一个层」。

## 公式

$$
s:\mathcal H^i\to X,\qquad s^{-1}(x)\simeq\mathcal H_x^i
$$

$$
T^i(\mathcal F)=(s\times h^{\rightarrow})_!((h^{\leftarrow})^*\mathcal F)[i(n-i)]
$$

## 易错点

- 把 $T^i$ 的值域写成 $D^b(\mathfrak{B}\mathrm{un}_n)$：大函子的值域是 $D^b(X\times\mathfrak{B}\mathrm{un}_n)$，多出的 $X$ 因子不能省。

## 批注

**〔背景直觉〕为什么要「大」**　局部条件「$\forall x$」在几何上不好写；把 $x$ 变成变量后，逐点条件变成一个整体同构 $T^i(\mathcal F)\simeq E\boxtimes\mathcal F$，$E$ 就是那个「随 $x$ 变化的特征值」。这是几何 Langlands 陈述的标准写法。

## 相关

[[hecke-functor]]、[[eigensheaf]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§3.3，原书 pp. 277（PDF pp. 279）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec3.tex:35-46（§3.3）`
