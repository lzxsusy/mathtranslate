# Hecke 对应与 Grassmann 纤维

> `gaits04/concept/hecke-correspondence` · 轨 C 向量丛与 Hecke · 状态 reviewed · 核验 source-only

**问题：** 为什么 $h^\leftarrow$ 的纤维是 $i$ 维子空间，而 $h^\rightarrow$ 的纤维是 $n-i$ 维子空间？

**一句话：** $H_x^i$ 是三元组 $(M,M',\beta)$ 的同构类集合，其中 $\beta:M\hookrightarrow M'$ 的商在 $x$ 处概形论地支撑且长度为 $i$；两个投影 $h^\leftarrow,h^\rightarrow$ 的纤维分别是 Grassmann 簇 $\mathrm{Gr}^i(M_x)$ 与 $\mathrm{Gr}^{n-i}(M'_x)$ 的 $k_x$-点。

**别名：** `Hecke correspondence`、`H_x^i`、`Grassmannian`、`Lemma 2.4`

## 定义

固定 $x\in X$ 与整数 $i$，$1\le i\le n$。记 $H_x^i$ 为下述数据的同构类集合：$(M,M',\beta)$，其中 $M,M'$ 是 $X$ 上秩 $n$ 向量丛，$\beta$ 是 $M$ 到 $M'$ 的单射（视二者为 $X$ 上的凝聚层），使得商 $M'/M$ 长度为 $i$，且概形论地支撑在 $x$ 处。有两个自然映射，记为 $h^\leftarrow$ 与 $h^\rightarrow$，从 $H_x^i$ 到 $\mathrm{Bun}_n$，分别把上述三元组送到 $M$ 与 $M'$。引理 2.4：给定 $M\in\mathrm{Bun}_n$，$h^\leftarrow$ 在其上的纤维可典范地等同于 $k_x$ 上向量空间 $M_x$ 中 $i$ 维子空间的集合；换言之，$(h^\leftarrow)^{-1}(M)$ 是 Grassmann 簇 $\mathrm{Gr}^i(M_x)$ 的 $k_x$-点集。对 $h^\rightarrow$ 同样成立：$(h^\rightarrow)^{-1}(M')$ 是 $\mathrm{Gr}^{n-i}(M'_x)$ 的 $k_x$-点集。

**记号：** $H_x^i$：Hecke 对应的 $k_x$-点集；$\beta|_x$：$\beta$ 在 $x$ 处纤维上的映射；$\mathrm{Gr}^i(V)$：$V$ 的 $i$ 维子空间构成的 Grassmann 簇；$M(x)=M\otimes_{\mathcal O_X}\mathcal O_X(x)$。

## 要点

- 「概形论地支撑在 $x$ 处」等价于 $M'/M$ 非典范地同构于 $k_x^i$，故长度 $i$ 就是 $k_x$ 上的维数 $i$。
- 证明用纤维上的正合列 $0\to\ker(\beta|_x)\to M_x\to M'_x\to(M'/M)_x\to0$：$\ker(\beta|_x)$ 是 $M_x$ 的 $i$ 维子空间。
- 反向构造：给定 $V\subset M_x$，令 $M'$ 为 $M(x)$ 中局部截面形如 $t^{-1}m$（$m$ 在 $x$ 处取值属于 $V$）的子层，于是 $\ker(\beta|_x)=V$。

## 公式

$$
0\to\ker(\beta|_x)\to M_x\to M'_x\to(M'/M)_x\to0
$$

$$
(h^{\leftarrow})^{-1}(M)=\mathrm{Gr}^i(M_x)(k_x)
$$

## 定理与证明

**引理 2.4**　给定 $M\in\mathrm{Bun}_n$，$(h^{\leftarrow})^{-1}(M)$ 可典范等同于 $\mathrm{Gr}^i(M_x)$ 的 $k_x$-点集；$(h^{\rightarrow})^{-1}(M')$ 可典范等同于 $\mathrm{Gr}^{n-i}(M'_x)$ 的 $k_x$-点集。

> 跳步说明：原书给出正合列与 $t^{-1}m$ 构造，未验证两个构造互逆的细节。

*出处：§2.4，原书 p.275*

## 易错点

- 把 $H_x^i$ 的纤维当成「$i$ 维子空间」而不区分 $h^\leftarrow$ 与 $h^\rightarrow$：两者维数互补（$i$ 与 $n-i$），混用会让 §3.2 的平移 $[i(n-i)]$ 也写错。

## 批注

**〔含糊点拨〕原书的 $M(x)$ 简写**　$M(x)$ 指把 $M$ 沿 $x$ 扭转一次，即 $M\otimes_{\mathcal O_X}\mathcal O_X(x)$。它比 $M$ 多出允许在 $x$ 处有一阶极点的截面，正是形如 $t^{-1}m$ 的那些；要求 $m(x)\in V$ 就限定了 $M'$ 在 $x$ 处纤维的大小。

## 相关

[[bun-bijection]]、[[hecke-operator]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§2.3–2.4，原书 pp. 274–275（PDF pp. 276–277）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec2.tex:24-50（§2.3–§2.4）`
