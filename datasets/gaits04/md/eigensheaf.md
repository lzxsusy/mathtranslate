# Hecke 本征层与几何 Langlands 猜想

> `gaits04/concept/eigensheaf` · 轨 D 层化与猜想 · 状态 reviewed · 核验 source-only

**问题：** 这个猜想与 §1.9 的 Langlands 对应是什么关系？

**一句话：** $\mathcal F_\sigma$ 称为关于 $\sigma$ 的 Hecke 本征层，若对所有 $i$ 有 $T^i(\mathcal F_\sigma)\simeq\Lambda^i(E_\sigma)\boxtimes\mathcal F_\sigma$；几何 Langlands 猜想断言每个不可约 $\sigma$ 都有这样的尖点本征层。

**别名：** `Hecke eigensheaf`、`geometric Langlands conjecture`、`Laumon`、`Drinfeld`

## 定义

现在可以给出 Hecke 本征层的定义（定义稍嫌粗糙，对任意群都适用的更好定义见 [BD]）。设 $\sigma:\pi_1(X)\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$ 是表示；回忆 $E_\sigma$ 是相应的 $X$ 上 $n$ 维局部系统。若对每个 $i=1,\dots,n$ 都存在同构 $T^i(\mathcal F_\sigma)\simeq\Lambda^i(E_\sigma)\boxtimes\mathcal F_\sigma$，则称对象 $\mathcal F_\sigma\in D^b(\mathfrak{B}\mathrm{un}_n)$ 为关于 $\sigma$ 的 Hecke 本征层；其中 $\Lambda^i$ 表示 $i$ 次外幂。若基域 $k=\mathbb{F}_q$，且 $\mathcal F_\sigma$ 是关于 $\sigma$ 的 Hecke 本征层，则其对应的 $\mathrm{GL}_n(K)\backslash\mathrm{GL}_n(\mathbb A)/\mathrm{GL}_n(\mathbb O)$ 上的函数，是 Hecke 算子的公共特征函数，特征值由 $\sigma$ 给出，如 §1.9 所述。几何 Langlands 猜想（由 [L] 在 Drinfeld 原始论文之后提出；[Dr] 完整处理了 $\mathrm{GL}_2$ 的情形）预测：对每个如上所述的不可约 $\sigma$，确实存在 Hecke 本征层 $\mathcal F_\sigma$，而且它是尖点的（即 §2.8 所定义的函子 $r^n_{n_1,n_2}$ 在 $\mathcal F_\sigma$ 上为零）。

**记号：** $\Lambda^i$：外幂；$\boxtimes$：外张量积（$X$ 上因子与 $\mathfrak{B}\mathrm{un}_n$ 上因子）；$\sigma$：$\pi_1(X)$ 的 $n$ 维表示。

## 要点

- 本征条件是「每个 $i$ 一个同构」，$i=1$ 不够：外幂 $\Lambda^i$ 记录的是 $\sigma$ 的全部特征值，等价于 §1.9 中 $n$ 个 Satake 参数的逐点相等。
- $k=\mathbb{F}_q$ 时取函数，本征层退化为 Hecke 算子的公共特征函数——这正是 §1.9 对应的几何版本。
- 猜想要求 $\mathcal F_\sigma$ 尖点（$r^n_{n_1,n_2}=0$），与 §1.9 中 $\pi$ 尖点相对应。

## 公式

$$
T^i(\mathcal F_\sigma)\simeq\Lambda^i(E_\sigma)\boxtimes\mathcal F_\sigma,\qquad i=1,\dots,n
$$

## 易错点

- 把 $\Lambda^i(E_\sigma)$ 写成 $E_\sigma^{\otimes i}$：外幂与张量幂不同，外幂才是 $\mathrm{GL}_n$ 标准表示的第 $i$ 个外幂。

## 批注

**〔含糊点拨〕「稍嫌粗糙」何指**　原书自称定义粗糙，并在 [BD] 中指出对任意群都适用的更好定义。差别在于：这里只对 $\mathrm{GL}_n$ 陈述，把本征性直接写成外幂的显式同构；对一般约化群 $G$，本征层的「特征值」应取对偶群 $\check G$ 的局部系统，外幂只是 $G=\mathrm{GL}_n$ 时标准表示的外幂。

## 相关

[[big-hecke]]、[[langlands-lafforgue]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§3.4，原书 pp. 277–278（PDF pp. 279–280）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec3.tex:47-65（§3.4）`
