# 阿代尔环与限制积

> `gaits04/concept/adeles` · 轨 A 阿代尔与球表示 · 状态 reviewed · 核验 source-only

**问题：** 阿代尔环为什么取限制积，而不是直积？

**一句话：** 取 $X$ 的闭点、局部域与剩余域，把各局部域按「几乎处处取整数」粘成限制积，得到 $K$ 的阿代尔环 $\mathbb A$。

**别名：** `adele ring`、`restricted product`、`函数域的整体域`

## 定义

设 $K$ 为正特征的整体域，即有限域 $\mathbb{F}_q$ 上光滑、射影、几何不可约曲线 $X$ 的有理函数域。记 $|X|$ 为 $X$ 的闭点集，它与 $K$ 的赋值一一对应。对 $x\in|X|$，记 $K_x$ 为相应的局部域，$\mathcal O_x$ 为其整数环，$k_x$ 为剩余域。$K$ 的阿代尔环定义为限制积 $\mathbb A:=\prod'_{x\in|X|}K_x$。

**记号：** $|X|$：闭点集；$K_x$：$x$ 处完备化；$\mathcal O_x$：$K_x$ 的整数环；$k_x=\mathcal O_x/\mathfrak m_x$：剩余域；$\prod'$：限制积（几乎处处落在 $\mathcal O_x$ 内）。

## 要点

- 限制积是 $\mathbb A$ 上能定义 Haar 测度、又能让 $\mathrm{GL}_n(\mathbb O)$ 成为紧群的关键：直积太大，商空间上没有有限测度。
- 对函数域，$|X|$ 就是曲线的闭点，$K_x$ 是 $x$ 处的完备化，故「数论」与「曲线几何」字面同构。
- 正特征使 $k_x$ 有限，后文所有纤维都是有限集（§2.5），迹公式才有意义。

## 公式

$$
\mathbb A:=\prod'_{x\in|X|}K_x
$$

## 易错点

- 把 $\mathbb A$ 写成直积：直积里 $\mathrm{GL}_n(\mathbb O)$ 不紧，Haar 测度也不是局部有限的。

## 批注

**〔易错预警〕$\mathcal K$ 与 $K$**　原书用花体 $\mathcal K$ 记全局域、$K_x$ 记局部域；译文照此。读公式时不要把 $\mathcal K$ 误作基域 $k$。

## 相关

[[integral-adeles]]、[[smooth-funct]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§1.1，原书 pp. 269（PDF pp. 271）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec1.tex:9-18（§1.1）`
