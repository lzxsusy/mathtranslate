# 局部 Hecke 函子 $T_x^i$

> `gaits04/concept/hecke-functor` · 轨 D 层化与猜想 · 状态 reviewed · 核验 source-only

**问题：** 那个平移 $[i(n-i)]$ 从哪来？

**一句话：** $T_x^i(\mathcal F)=(h^{\rightarrow})_!((h^{\leftarrow})^*\mathcal F)[i(n-i)]$ 是 $D^b(\mathfrak{B}\mathrm{un}_n)$ 到自身的函子，比函数侧多一个上同调平移。

**别名：** `Hecke functor`、`Hecke stack`、`cohomological shift`

## 定义

先固定 $x\in|X|$。考虑 Hecke 叠 $\mathcal H_x^i$，使 $\operatorname{Hom}(S,\mathcal H_x^i)$ 是三元组 $(M,M',\beta)$ 的范畴，其中 $M$ 与 $M'$ 是 $X\times S$ 上秩 $n$ 向量丛，$\beta$ 是凝聚层的嵌入 $M\hookrightarrow M'$，使 $M'/M$ 概形论地支撑在 $x\times S\subset X\times S$ 上，且是该子概形上秩 $i$ 的向量丛。$\mathcal H_x^i$ 的 $\mathbb{F}_q$-点同构类集合就是原来的 $H_x^i$。和前面一样，有映射 $h^{\leftarrow},h^{\rightarrow}:\mathcal H_x^i\to\mathfrak{B}\mathrm{un}_n$。但现在对 $\mathfrak{B}\mathrm{un}_n$ 的给定点（即向量丛 $M$），原像 $(h^{\leftarrow})^{-1}\subset\mathcal H_x^i$ 不再是集合，而是同构于 $\mathrm{Gr}^i(M_x)$ 的概形。引入 Hecke 函子 $T_x^i:D^b(\mathfrak{B}\mathrm{un}_n)\to D^b(\mathfrak{B}\mathrm{un}_n)$，定义为 $\mathcal F\mapsto(h^{\rightarrow})_!((h^{\leftarrow})^*\mathcal F)[i(n-i)]$，括号内的表达式表示上同调平移。

**记号：** $\mathcal H_x^i$：Hecke 叠；$\mathrm{Gr}^i$：Grassmann 簇；$[d]$：上同调平移 $d$ 步；$i(n-i)=\dim\mathrm{Gr}^i$。

## 要点

- 平移 $[i(n-i)]$ 的指数正是 Grassmann 簇 $\mathrm{Gr}^i$ 的维数，它把层的次数拉回与函数同权。
- 与 §1.6 脚注的归一化因子 $(-|k_x|^{1/2})^{i(n-i)}$ 配套：$[1]$ 对应 Tate 扭 $\mathbb{Q}_\ell(1/2)$，故 $[i(n-i)]$ 对应 $|k_x|^{i(n-i)/2}$。
- 叠层面的函子与函数侧算子 $T_x^i$ 通过层-函数对应（§4.2）相容，这是几何 Langlands 的出发点。

## 公式

$$
T_x^i(\mathcal F)=(h^{\rightarrow})_!((h^{\leftarrow})^*\mathcal F)[i(n-i)]
$$

## 易错点

- 漏掉 $[i(n-i)]$：不写平移，函子与函数侧算子差一个 $q_x^{i(n-i)/2}$ 的权，本征值随之错位。

## 批注

**〔易错预警〕同一符号，两个世界**　$T_x^i$ 在 §1.6 是双陪集特征函数，在 §3.2 是导出范畴的函子；原书用同一符号，靠上下文区分。写卡片时务必标明是函数侧还是层侧。

## 相关

[[hecke-operator]]、[[big-hecke]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§3.2，原书 pp. 277（PDF pp. 279）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec3.tex:22-34（§3.2）`
