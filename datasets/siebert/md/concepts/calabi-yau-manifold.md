# Calabi–Yau 流形

> `siebert/concept/calabi-yau-manifold` ｜ track O ｜ draft

**一句话**：紧 Kähler 流形且典范丛全纯平凡（K_X≅O_X，等价于 c₁=0）；加上 b₁=0 与不可约，其和乐群落在 SU(n) 内。

**自测**：为什么『典范丛全纯平凡』这一个条件就足以成为镜像对称的几何前提？

## 定义

$n$ 维紧 Kähler 流形 $X$ 称为 Calabi–Yau，若其典范丛全纯平凡：\n$$K_X=\det T^*_X\simeq\mathcal O_X,$$\n等价地 $c_1(X)=0$。讲义还要求 $b_1=0$ 与不可约（万有覆盖不分解为乘积）。进一步称严格 Calabi–Yau，若 $H^{k,0}(X)=0$ 对 $0<k<n$ 成立（p.13）。

记号：$K_X=\det T^*_X=\Omega^n_X$；$h^{p,q}=\dim H^{p,q}$；$\Theta_X=T_X$ 为切丛；Hodge 数满足 $h^{p,q}=h^{q,p}=h^{n-p,n-q}$。

## 要点

- $K_X\simeq\mathcal O_X$ 等价于 $c_1(X)=0$，于是存在处处非零的全纯 $n$ 形式 $\Omega\in H^0(X,\Omega^n_X)$，$h^{n,0}=1$。
- 在 Kähler 情形，$c_1=0$ 由 Yau 定理可实现为 Ricci 平坦度量，其和乐群落在 $SU(n)$ 内；反之和乐 $\subseteq SU(n)$ 给出平凡典范丛。这一等价是标准事实，讲义 p.7 只用 $K_X\simeq\mathcal O_X$ 作定义。
- 五次超曲面：$N_{X/\PP^4}\cong\mathcal O_X(5)$、$\mathcal O_{\PP^4}(5)|_X\cong\mathcal O_X(5)$，由 II/II² 与伴随公式得 $K_X\simeq\mathcal O_X$（p.7）。
- 不可约这一条不能省：$K3	imes K3$ 的典范丛平凡，但万有覆盖分解成两个因子，按讲义术语不『不可约』（p.13）。
- 镜像对称的几何前提：B 模型是 Hodge 结构变分，需要 $\Omega$ 存在且 $H^3$ 上是秩 4 的局部系统；A 模型需要辛结构，$c_1=0$ 才能让 GW 不变量与虚拟类干净地定义。

## 公式

$$K_X=\det T^*_X\simeq\mathcal O_X\iff c_1(X)=0$$
$$h^{n,0}=h^{0,n}=1,\qquad h^{p,q}=h^{q,p}=h^{n-p,n-q}$$
$$\mathrm{Hol}(\nabla^{LC})\subseteq SU(n)\quad(\text{取 Ricci 平坦度量时})$$

## 定理与证明

### Calabi–Yau 的 Hodge 数约束

$n$ 维紧 Calabi–Yau 流形满足 $h^{n,0}=h^{0,n}=1$、$h^{1,0}=h^{0,1}=0$，且 $h^{p,q}=h^{q,p}=h^{n-p,n-q}$。

（complete；来源：原书 p.13）

1. $K_X\simeq\mathcal O_X$ 给出 $H^0(X,\Omega^n_X)\cong H^0(X,\mathcal O_X)=\CC$，故 $h^{n,0}=1$，且可取处处非零的 $\Omega$。  
   为什么：典范丛的截面就是全纯 $n$ 形式，平凡丛的截面空间一维。
2. 讲义要求 $b_1=0$，由 Hodge 分解 $b_1=h^{1,0}+h^{0,1}$ 与 $h^{1,0}=h^{0,1}$ 得 $h^{1,0}=0$。  
   为什么：$b_1=0$ 是讲义定义的一部分；没有它 $h^{1,0}$ 未必为零。
3. 对 $p+q=n$ 用 Serre 对偶 $H^{p,q}\cong H^{n-p,n-q}$ 的共轭得到 $h^{p,q}=h^{n-p,n-q}$，再配合 Dolbeault 的共轭对称 $h^{p,q}=h^{q,p}$。  
   为什么：这两条对称性是 Kähler 流形的一般事实，与 $K_X$ 是否平凡无关，但决定了 Hodge 菱形的形状。

### 五次超曲面的典范丛平凡

设 $X=Z(\sum x_i^5)\subset\PP^4$ 光滑，则 $K_X\simeq\mathcal O_X$。

（complete；来源：原书 p.7）

1. 由伴随公式 $K_X\cong (K_{\PP^4}\otimes\mathcal O_{\PP^4}(5))|_X$。  
   为什么：超曲面 $X$ 是 $\PP^4$ 中次数 5 的除子，其典范丛由伴随公式给出。
2. $K_{\PP^4}\cong\mathcal O_{\PP^4}(-5)$，故 $K_X\cong\mathcal O_{\PP^4}(-5)|_X\otimes\mathcal O_{\PP^4}(5)|_X\cong\mathcal O_X$。  
   为什么：$-5+5=0$，两份超平面线丛的限制相互抵消。

## 易错点

- 『$K_X\simeq\mathcal O_X$』本身不够：$K3	imes K3$ 也满足，但万有覆盖可分解，讲义因此额外要求不可约（p.13）。
- 严格 Calabi–Yau 比 Calabi–Yau 多一条：中间 Hodge 数 $h^{k,0}=0$（$0<k<n$）。复环面 $T^6$ 的典范丛平凡，但 $b_1=6$，按讲义定义根本不算 Calabi–Yau。
- $SU(n)$ 和乐 $\Leftrightarrow$ 平凡典范丛的等价依赖 Kähler 与 Yau 定理；在非 Kähler 或没有 Ricci 平坦度量的情形不要直接套用。
- p.13 的反例针对的是『不可约』这一条，而不是『$K$ 平凡』——别把 $K3	imes K3$ 说成典范丛不平凡。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，概览 §1 计数镜像对称，p.7–7（原书 p.7）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 1 章 §3 Hodge 菱形，p.13–13（原书 p.13）

关联：`siebert/concept/quintic-threefold`、`siebert/concept/mirror-symmetry`、`siebert/concept/homological-mirror-symmetry`

来源说明：原书 p.7（$K_X\simeq\mathcal O_X$ 的定义、$b_1=0$、不可约、五次超曲面例）、p.13（严格 CY、$K3	imes K3$ 反例、Hodge 对称）。$SU(n)$ 和乐等价是 Yau 定理的标准推论，讲义未展开，卡中已标为『外部标准事实』而非讲义结论。nLab「Calabi-Yau variety」（Calabi-Yau+manifold 重定向到此页，last revised 2026-01-06）核过术语。
