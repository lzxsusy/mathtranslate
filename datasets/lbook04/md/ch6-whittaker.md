# Whittaker 模型（GL(1) 情形）

> `lbook04/concept/ch6-whittaker` · 轨 T Tate 与迹公式 · 状态 reviewed · 核验 source-only

**问题：** 为什么 $\operatorname{GL}(1)$ 的 Whittaker 模型只有一维，而 $\operatorname{GL}(2)$ 的 Whittaker 空间却能承载整个尖点表示？

**一句话：** $\operatorname{GL}(1)$ 的 Whittaker 模型退化为一维本征分布空间 $S'(\omega)$：其上「Fourier 系数」只有一个，就是 $\omega$ 本身；$\operatorname{GL}(2)$ 的 Whittaker 函数是这一结构的非交换升级。

**别名：** `Whittaker model`、`Whittaker 函数`、`Fourier 展开`

## 定义

群 $G=\operatorname{GL}(1)$ 的幂零子群 $N$ 平凡，故 Whittaker 模型就是 $\mathbb A^\times$ 上满足 $r'(a)\lambda=\omega(a)\lambda$ 的分布空间 $S'(\omega)$。定理 3.4：$\dim S'(\omega)=1$，故「Whittaker 函数」只有一个自由度 $z_o$。$\operatorname{GL}(2)$ 时 $N=U$ 非平凡，Whittaker 空间 $W(\pi,\psi)$ 与 $\pi$ 同构（重数一），这才是第 7 章 §2 的 Fourier 展开。

**记号：** $N$：幂零子群（$\operatorname{GL}(1)$ 时平凡）；$\psi$：加法特征；$W(\pi,\psi)$：Whittaker 空间；$S'(\omega)$：本征分布空间。

## 要点

- $\operatorname{GL}(1)$：Whittaker 泛函就是 zeta 积分 $z(s,\omega;\cdot)$ 给出的分布；一维性 $=$ 定理 3.4。
- 「Fourier 展开」在 $\operatorname{GL}(1)$ 就是 Poisson 求和/局部 Fourier 变换，不产生新的系数。
- $\operatorname{GL}(2)$：$W(\pi,\psi)\cong\pi$（重数一），整体 Whittaker 函数由局部成分唯一决定，这是定理 2.6(i) 的证明工具。
- 本章正文不出现 “Whittaker” 一词；此卡按 $\operatorname{GL}(1)$ 结构补足，并指向第 7 章。

## 公式

$$
W(\pi,\psi)=\bigl\{W:G(\mathbb A)\to\mathbb C\ \text{光滑}\mid W(ng)=\psi(n)W(g)\bigr\}
$$

$$
\dim S'(\omega)=1\quad(\operatorname{GL}(1)\ \text{的 Whittaker 空间})
$$

## 易错点

- 不要把 $S'(\omega)$ 与 $\operatorname{GL}(2)$ 的 Whittaker 空间混同：前者是一维分布空间，后者与 $\pi$ 同构、通常无限维；本卡标题的「$\operatorname{GL}(1)$」限定不能省。
- 本章 grep 不到 Whittaker（已核）；引用时必须说明这是按第 7 章结构回填的导读，不是 ch06.tex 的原文。

## 批注

**〔易错预警〕本章无此词**　ch06.tex 全文没有 Whittaker；Tate 论文只处理 $\operatorname{GL}(1)$，$N$ 平凡使 Whittaker 条件空洞。真正的 Whittaker 模型定义与重数一定理在第 7 章 §2（ch07.tex:393–429）。

**〔背景直觉〕为什么一维**　$\operatorname{GL}(1)$ 的表示是一维的，故其 Whittaker 空间也只能一维；到 $\operatorname{GL}(2)$，不可约表示无限维，Whittaker 泛函把 $\pi$ 嵌入 $\mathbb A$ 上的函数空间，Fourier 系数 $a_n$ 才出现。

## 相关

[[ch6-local-zeta]]、[[ch6-global-tate]]、[[ch7-cuspidal-whittaker]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§3 本征分布，原书 pp. 114–116（PDF pp. 119–121）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch06.tex:173-312`
