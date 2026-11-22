# 全书地图：从 L 函数到几何朗兰兹

> `lbook04/concept/all-map` · 轨 O 总览 · 状态 reviewed · 核验 source-only

**问题：** 这本书的十二章应当按什么顺序读，各章之间靠什么概念相连？

**一句话：** 十二章沿一条主线：先把 L 函数从 Riemann zeta 推广到 Artin 与椭圆曲线，再把自守形式升到 adele 与 GL_n，最终在 Langlands 猜想与对偶群处收束，以几何朗兰兹作结。

**别名：** `chapter map`、`阅读路线`

## 定义

全书可分成四段：第 1–5 章讲 L 函数（Riemann、Dirichlet、Dedekind、Hecke、Artin、椭圆曲线）；第 3、7 章讲自守形式从经典模形式到 adele 表示的升级；第 6、8 章讲 Tate 论文与谱理论/迹公式这套解析机器；第 9–11 章把一切搬到 GL_n 并陈述 Langlands 猜想与函子性；第 12 章是几何版本。

**记号：** 章节编号沿用原书；第 12 章为 Gaitsgory 的几何朗兰兹导论。

## 要点

- 前五章是同一问题的五次推广：zeta → Dirichlet L → Dedekind zeta → Hecke L → Artin L。
- 第 6 章的 Tate 论文把 L 函数的函数方程化归为局部 zeta 积分的计算，是全书技术转折点。
- 第 9–11 章的三部曲（解析理论、Langlands 猜想、对偶群与函子性）构成纲领的现代陈述。
- 第 12 章把数域换成函数域、把 Galois 表示换成 lisse 层，得到几何朗兰兹。

## 公式

$$
L(s,\chi)=\sum_{n\ge 1}\chi(n)n^{-s}
$$

$$
\zeta_K(s)=\prod_{\mathfrak p}(1-N\mathfrak p^{-s})^{-1}
$$

## 易错点

- 把第 12 章当作全书的特例会误解它：几何朗兰兹是平行理论，不是第 9–11 章的推论。
- 各章作者不同，记号并不完全统一（如 GL_n 的 L 函数在 ch9 与 ch10 的归一化差一个移位），跨章引用时须回到该章定义。

## 批注

**〔背景直觉〕为什么按这个顺序读**　若只为几何朗兰兹，最短路径是 ch6（Tate 局部理论）→ ch9（GL_n 解析理论）→ ch12；ch1–5 提供动机，ch7–8 提供自守表示与迹公式的语言，ch10–11 是纲领的完整陈述。

## 相关

[[ch1-zeta-euler]]、[[ch6-local-zeta]]、[[ch9-godement-jacquet]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，导论，原书 pp. 1–281（PDF pp. 9–289）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch01.tex:1-40`
