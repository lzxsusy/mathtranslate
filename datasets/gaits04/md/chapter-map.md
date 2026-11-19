# 第 12 章论证地图：从阿代尔到层

> `gaits04/concept/chapter-map` · 轨 O 总览 · 状态 reviewed · 核验 source-only

**问题：** 这一章为什么先讲函数域上的 $\mathrm{GL}_n$，再讲向量丛，最后才过渡到层？

**一句话：** 全章三步：把自守形式写成阿代尔双商上的函数，把 Hecke 算子写成向量丛上的对应，再把函数换成 $\ell$-进层，以陈述几何 Langlands 猜想。

**别名：** `Informal Introduction to Geometric Langlands`、`全章结构`

## 定义

本章分四节。§1 在函数域 $K=\mathbb{F}_q(X)$ 上重述 $\mathrm{GL}_n$ 的自守形式：光滑函数、Hecke 代数、球表示与 Satake 参数、尖点性，末了给出 Langlands 对应（现为 Lafforgue 定理）。§2 把双商 $\mathrm{GL}_n(K)\backslash\mathrm{GL}_n(\mathbb A)/\mathrm{GL}_n(\mathbb O)$ 解释为 $X$ 上秩 $n$ 向量丛的同构类，把 Hecke 算子解释为 Hecke 对应上的「拉回再推前」。§3 把 $\mathrm{Bun}_n$ 升级为模叠 $\mathfrak{B}\mathrm{un}_n$，把 Hecke 算子升级为导出范畴上的函子，从而定义 Hecke 本征层并陈述几何 Langlands 猜想。§4 附录回顾层-函数对应，说明层何以是函数的「几何化」。

**记号：** $K$：函数域；$\mathbb A$：阿代尔环；$\mathbb O$：整阿代尔环；$\mathrm{Bun}_n$：秩 $n$ 向量丛的同构类集合；$\mathfrak{B}\mathrm{un}_n$：相应的模叠；$D^b$：导出范畴。

## 要点

- §1 只做 $\mathrm{GL}_n$，不做一般约化群；作者明言这是为了省去定义，而不是因为 $\mathrm{GL}_n$ 特殊。
- §2 与 §3 是同一件事的两层：§2 在集合层面写 Hecke 算子，§3 在叠与层的层面重写一遍。
- §4 是工具节：不读它也能读懂猜想的陈述，但读不懂「为什么这叫几何化」。

## 公式

$$
\operatorname{Funct}(\mathrm{GL}_n(K)\backslash\mathrm{GL}_n(\mathbb A)/\mathrm{GL}_n(\mathbb O))
$$

$$
T_x^i:\ D^b(\mathfrak{B}\mathrm{un}_n)\to D^b(\mathfrak{B}\mathrm{un}_n)
$$

## 易错点

- 把 §2 的 $\mathrm{Bun}_n$（集合）与 §3 的 $\mathfrak{B}\mathrm{un}_n$（叠）混为一谈：前者只记同构类，后者记整个范畴。

## 批注

**〔背景直觉〕为什么先函数域**　函数域上「曲线 $X$」与「域 $K$」是同一件事的两面：域的算术（Frobenius、分歧）可以用 $X$ 的几何（点、层、上同调）来读。整章的翻译就是把左边的词逐个换成右边的词。

## 相关

[[adeles]]、[[bun-bijection]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§1–§4 总览，原书 pp. 269–281（PDF pp. 271–283）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec1.tex:7-17（§1.1）`
