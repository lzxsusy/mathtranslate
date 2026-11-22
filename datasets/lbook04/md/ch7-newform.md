# 从模形式到 GL2 自守表示的对应

> `lbook04/concept/ch7-newform` · 轨 M 模形式与自守表示 · 状态 reviewed · 核验 source-only

**问题：** 为什么「新形式」恰好对应导子等于 $N$ 的表示，而旧形式对应的是导子更小的表示？

**一句话：** 每个经典新形式 $f\in S_k(\Gamma_0(N),\chi)$ 对应唯一的尖点自守表示 $\pi$，满足 $\pi_\infty\cong DS_k$、$\omega_\pi=\chi$、$N(\pi)=N$；反之由 $\pi$ 的球向量可还原 $f$。

**别名：** `新形式`、`newform`、`$S_k(\Gamma_0(N))$ 分解`

## 定义

定理 4.1：$\mathcal A_0(\pi)^{\mathrm{new}}_{\mathrm{hol}}=\{\varphi:X_-\varphi=0,\ \varphi(gk)=\omega(k)\varphi(g)\ \forall k\in K_0(N(\pi))\}$ 是一维的，由唯一的新形式 $f_0$ 张成；$S_k^{\mathrm{new}}(\Gamma_0(N),\chi)\cong\bigoplus_{\omega_\pi=\omega,\ \pi_\infty\cong DS_k,\ N(\pi)=N}\mathcal A_0(\pi)^{\mathrm{new}}_{\mathrm{hol}}$；一般 $S_k(\Gamma_0(N),\chi)\cong\bigoplus_{N(\pi)\mid N}\mathcal A_0(\pi)^{K_0(N),\omega}_{\mathrm{hol}}$。Hecke 特征值由 $(4.6)(4.7)$ 给出。

**记号：** $S_k(\Gamma_0(N),\chi)$：经典尖点形式；$DS_k$：离散系列；$K_0(N)$；$N(\pi)$：导子；$f_0$：新形式；$t(\pi_p)$：Satake 参数。

## 要点

- 对应是双射：$\{$新形式$\}\leftrightarrow\{\pi:\pi_\infty\cong DS_k,\ \omega_\pi=\chi,\ N(\pi)=N\}$；旧形式来自 $N(\pi)\mid N$ 的嵌入。
- Hecke 特征值与 Satake 参数的关系 $(4.7)$：$1-a_p p^{-(k-1)/2}X+\chi(p)X^2=\det(1-t(\pi_p)X)$。
- Ramanujan–Petersson $|a_p|\le2p^{(k-1)/2}\iff|t_{p,i}|=p^{1/2}$（Deligne 1974）；$p\|N$ 时参数为 $p^{1/2},p^{-1/2}$，坏位必失效。
- 本章 $\pi_\infty$ 是离散系列 $DS_k$；Maass 形式把 $DS_k$ 换成主系列，对应同样成立。

## 公式

$$
a_p=p^{(k-1)/2}(t_{p,1}+t_{p,2}),\qquad \chi(p)=t_{p,1}t_{p,2}
$$

$$
1-a_p p^{-(k-1)/2}X+\chi(p)X^2=\det\bigl(1-t(\pi_p)X\bigr)
$$

$$
S_k^{\mathrm{new}}(\Gamma_0(N),\chi)\cong\bigoplus_{\omega_\pi=\omega,\ \pi_\infty\cong DS_k,\ N(\pi)=N}\mathcal A_0(\pi)^{\mathrm{new}}_{\mathrm{hol}}
$$

## 易错点

- 权 $k$ 与中心平移：经典 $L(f,s)=\sum a_n n^{-s}$ 的中心在 $s=k/2$，而自守 $L$ 用 $q^{-s}$ 归一化；比较时差 $(k-1)/2$。
- $p\|N$ 时 $a_p=\pm p^{(k-1)/2}$，仍满足 $|a_p|\le2p^{(k-1)/2}$，但对应 Satake 参数有一个是 $p^{-1/2}$，不是两个都取 $p^{1/2}$。

## 批注

**〔背景直觉〕新形式 $=$ 导子恰好**　新形式 $f$ 的 Mellin 变换给出 $\pi$，且 $N(\pi)=N$；旧形式是某个更低水平新形式的像，故导子严格小于 $N$。这解释了分解中为何用 $N(\pi)\mid N$ 而非等号。

**〔易错预警〕$DS_k$ 的归一化**　本章 $DS_k$ 的 Casimir 特征值是 $k(k-2)$（$(2.7)$），与通常的权 $k$ 一致；若用 $H=\operatorname{diag}(1,-1)$ 的旧归一化，会得到 $k(k-1)$ 之类的值，导致 $(4.6)$ 的指数错位（见 annote 329–338）。

## 相关

[[ch7-restricted-tensor]]、[[ch7-automorphic-rep]]、[[ch5-hecke-eigenform]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§4，原书 pp. 147–149（PDF pp. 151–153）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch07.tex:594-671`
