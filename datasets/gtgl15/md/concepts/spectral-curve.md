# 谱曲线

> `gtgl15/concept/spectral-curve` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev

> **先自测**：为什么把 $y$ 当成典范丛上的坐标、而不当成普通数值，就能把希格斯丛编码成一条曲线？

## 一句话

谱曲线 $D\subset K$ 由 $\det(y-\varphi)=0$ 定义，是 $C$ 上的 $N$ 重覆盖；它把希格斯丛的几何翻译成 $D$ 上线丛的几何。

## 定义

对 $SU(N)$ 希格斯丛 $(E,\varphi)$，令 $y$ 为 $K$ 的纤维坐标，则 $\det(y-\varphi)=0$ 定义 $K$ 的全空间中的曲线 $D$，$\psi:D\to C$ 是 $N$ 重覆盖。$D$ 的点是 $\varphi$ 在 $p\in C$ 上的本征值；$N=2$ 时方程化为 $y^2-\frac12\operatorname{Tr}\varphi^2=0$。$D$ 上自然有 $1$-形式 $\lambda=y\,dz$。

**记号**：$D$；$\psi:D\to C$；$y$；$\lambda=y\,dz$；$g_D$。

## 要点（为什么需要它）

1. $y$ 是 $K$ 的纤维坐标：$y\,dz$ 是 $C$ 上的 $1$-形式，Seiberg–Witten 微分 $\lambda=y\,dz$ 只在 $D$ 上有意义。
2. $\varphi$ 的本征值在分支点处重合，故 $\psi$ 的分歧点对应 $\varphi(p)$ 有重本征值。
3. 给定 $D$ 与 $D$ 上线丛 $\mathcal L$，$E=\psi_*(\mathcal L)$、$\varphi=\psi_*(y)$ 重建希格斯丛（$\S2.6.2$）。
4. $D$ 的亏格 $g_D=g_C+(N^2-1)(g_C-1)$；阶为 $N$ 的覆盖，其分歧点数为 $2N(N-1)(g-1)$。
5. $D$ 的 Jacobian（或其 Prym 子簇）就是 Hitchin 纤维；这是 §3 对偶环面的来源。

## 核心公式

$$
$$D=\{\det(y-\varphi)=0\}\subset K,\qquad \psi:D\to C$$$$g_D=g_C+(N^2-1)(g_C-1),\qquad \lambda=y\,dz$$
$$

$$
$$g_D=g_C+(N^2-1)(g_C-1),\qquad \lambda=y\,dz$$
$$

## 定理与证明（或缺口）

### 谱曲线的亏格

$g_D=g_C+(N^2-1)(g_C-1)=g_C+\dim\mathcal V$。

1. $\psi:D\to C$ 是 $N$ 重覆盖，Riemann–Hurwitz 给 $2g_D-2=N(2g-2)+\deg R$。
   - *为什么*：覆盖的 Riemann–Hurwitz 公式。
2. 分歧除子 $R$ 的次数是 $2N(N-1)(g-1)$，代入得 $2g_D-2=2N^2(g-1)-2$。
   - *为什么*：整理即得 $g_D=1+N^2(g-1)$，与所给公式一致。

出处：`A p.11`

## 常见误解

- $D$ 在 $K$（一次形式丛）的全空间里，不在 $T^*C$ 里；虽然两者都有 $y$ 坐标，但 $K\cong T^*C$ 的选取要小心。
- $y$ 是坐标值，$\lambda=y\,dz$ 才是微分；把 $y$ 当全局函数是错的。
- $D$ 可以奇异或可约：判别式为零时谱曲线退化，不能套用光滑曲线上的 Jacobian。
- $N=2$ 的公式 (2.10) 带 $\frac12$：$y^2=\frac12\operatorname{Tr}\varphi^2$，别漏系数。

## 相关卡

[谱覆盖、判别式与分歧除子](../concepts/spectral-cover.md) · [核线丛与余核线丛](../concepts/kernel-cokernel.md) · [希钦纤维化](../concepts/hitchin-fibration.md) · [阿贝尔化与 Prym 簇](../concepts/abelianization-prym.md) · [谱曲线亏格与分歧点计数](../derivations/spectral-genus.md)

## 出处（印刷页）

- A p.10–13（A p.10 eq (2.9)）
- A p.10–11（A p.10 eq (2.10)）

> 说明：A=原文 $\S2.6.1$ 的谱曲线定义、eq (2.9)(2.10) 与亏格公式；B=把 Riemann–Hurwitz 的两步补全为证明；C=谱曲线与 Hitchin 纤维 Jacobian 的联系按 $\S2.6.2$ 与 §3 整理。最没把握处：$K\cong T^*C$ 的选取在原文只顺带提到。
