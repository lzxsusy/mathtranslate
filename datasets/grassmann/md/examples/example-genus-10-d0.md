# $g=10$、$(2,12,4)$ 的 $d_0$（例 7.5）

> `grassmann/example/example-genus-10-d0` · 轨道 7 · α-稳定凝聚系 · 状态 draft

> **这张卡练什么**：为什么 $g=10$、$(2,4)$ 时 $d_0$ 会随曲线在 $12$ 与 $13$ 之间跳动？

## 一句话

例 7.5 在 $g=10$、$(n,k)=(2,4)$、$d=12$ 上算出 $d_0$ 只能是 $12$ 或 $13$：一般曲线上 $d_0=13$，而 $K3$ 上的某些 Petri 曲线上 $d_0=12$。

## 背景定义

例 7.5 考察 $g=10$、$(n,k)=(2,4)$、$d=12$ 时 $d_0$ 的取值：定理 7.2 的两个临界值 $\frac{4g}{5}+4$ 与 $d_2-1$ 同时等于 $12$，于是 $d_0$ 只能为 $12$ 或 $13$，而一般曲线上为 $13$。

## 设定

设 $C$ 是亏格 $g=10$ 的光滑射影曲线，取 $n=2$、$k=4$，考察 $d=12$ 的秩 $2$ 凝聚系 $G(\alpha;2,12,4)$。定理 7.2 的临界值是 $d_2=13$，而 $\frac{4g}{5}+4=12=g+2=d_2-1$，故 $d_0$ 只能是 $12$ 或 $13$。整段论证的关键是：任意 $(E,V)\in G(\alpha;2,12,4)$ 都被迫给出一个「截面太少」的线丛，从而与 Voisin 的一般曲线结果冲突。

## 计算

先算预期维数：$\beta(2,12,4)\big|_{g=10}=4\cdot9+1-4(4-12+18)=36+1-40=-3$，为负，说明引理 1.6 的维数下界在此是空话。设 $(E,V)\in G(\alpha;2,12,4)$，记 $L=\det E$。定理 7.2(ii)/(iii) 的论证给出 $E$、$D(E)$ 稳定且 $h^0(L)\ge5$；由经典 Brill–Noether 理论 $\deg L\ge12$，但 $\deg L=\deg E=12$，故 $h^0(L)=5$。取 $H^0(L)$ 的 $3$ 维子空间 $W$ 使 $0\to E^*\to W\otimes\mathcal{O}\to L\to0$，得 $0\to H^0(L\otimes E^*)\to W\otimes H^0(L)\xrightarrow{\psi}H^0(L^{\otimes2})$。因 $L\otimes E^*\cong E$，$h^0(L\otimes E^*)=h^0(E)\ge k=4$，故 $\dim\ker\psi\ge4$。而 $\dim W\otimes H^0(L)=3\cdot5=15$，又与 $h^0(L^{\otimes2})=2\cdot12-10+1=15$ 相等，于是 $\psi$ 既不单射也不满射。把 $\psi$ 换成 $S^2H^0(L)\to H^0(L^{\otimes2})$（两者维数同为 $15$），同样不满射；而 Voisin 证明一般曲线上它是满射。故一般 $C$ 上 $G(\alpha;2,12,4)=\emptyset$，$d_0=13$。反过来，若该映射不满射，$L$ 的截面给出 $C\hookrightarrow\mathbb{P}^4$ 落在生成其核的二次超曲面 $q$ 上；$q$ 秩为 $5$ 时 $(E,V)$ 确实存在（$K3$ 曲面上的 Petri 曲线），此时 $d_0=12$。

## 要点

- 两条界夹住 $d_0$：定理 7.2(iii) 给 $d<\min\{\frac{4g}{5}+4,d_2-1\}$ 时 $G=\emptyset$，而 $g=10$ 时 $\frac{4g}{5}+4=12=d_2-1$，故 $d_0\ge12$；一般曲线上又证出 $d=12$ 空，故 $d_0=13$。
- 反例来自 $K3$ 上的 Petri 曲线：二次超曲面 $q$ 秩为 $5$ 时 $(E,V)$ 存在，说明 $d_0$ 在 $k>n+1$ 时可能依赖曲线，模型定理不能照搬。
- 维数 $15$ 的两次出现是全部算术：$\dim W\otimes H^0(L)=3\cdot5$ 与 $h^0(L^{\otimes2})=2d-g+1$、以及 $\dim S^2H^0(L)=\binom{6}{2}$ 三者相等，才使「$\psi$ 不单射」升级为「$\psi$ 不满射」。
- 若 $q$ 秩为 $4$，$(E,V)$ 可能对所有 $\alpha>0$ 严格半稳定，原文明确说此时对 $d_0$ 无法下结论；$q$ 的秩不可能小于 $4$。

## 关键公式

$$
\beta(2,12,4)\big|_{g=10}=36+1-40=-3
$$

$$
\dim W\otimes H^0(L)=3\cdot5=15=h^0(L^{\otimes2})=2\cdot12-10+1
$$

$$
0\to H^0(L\otimes E^*)\to W\otimes H^0(L)\to H^0(L^{\otimes2})
$$

## 相关定理

- **例 7.5 的判定（$g=10$ 时 $d_0=12$ 或 $13$）**：设 $g=10$，$n=2$，$k=4$，$d=12$。则对一般曲线 $G(\alpha;2,12,4)=\emptyset$，从而 $d_0(2,4)=13$；而 $K3$ 曲面上的某些 Petri 曲线上 $G(\alpha;2,12,4)\neq\emptyset$，对这些曲线 $d_0=12$。
- **定理 7.2（$k=n+2$ 的临界值）**：设 $k=n+2$，$d_2$ 为定理 7.1 给出的临界值。则 (ii) 若 $d<d_2-1$ 且 $(E,V)$ 对某个 $\alpha$ 半稳定，则 $(E,V)\in U$；(iii) 若 $d<\min\{\frac{4g}{5}+4,\ d_2-1\}$，则 $G(\alpha;n,d,k)=\emptyset$。

## 易错点

- 把 $d_0$ 当成只依赖 $(n,k)$ 的数：本例正是它在 $k=n+2$ 时依赖曲线的证据，模型定理在 $k\ge n+2$ 不能照搬。
- 由 $\beta=-3<0$ 直接断言空间为空：$K3$ 上的 Petri 曲线给出非空反例，$\beta<0$ 只是维数下界失效，不是消没定理。
- 把「$q$ 秩为 $4$」当成 $d_0=12$ 的证明：原文只说此情形可能对所有 $\alpha>0$ 严格半稳定，推不出结论；能下结论的只有秩 $5$ 与秩 $<4$（后者不可能）。
- 把 $\psi$ 与 $S^2H^0(L)\to H^0(L^{\otimes2})$ 混为一谈：前者定义域是 $W\otimes H^0(L)$（$3\times5$），后者是 $S^2H^0(L)$（$\binom{6}{2}$），两者维数都是 $15$ 但映射不同。

## 用到哪些概念

- [$d_0$ 与存在域 $U(n,d,k)$](../concepts/existence-region-d0.md)
- [Brill–Noether 数 $\beta$](../concepts/brill-noether-number.md)
- [Petri 曲线](../concepts/petri-curve.md)
- [极大秩猜想](../concepts/maximal-rank-conjecture.md)

## 相关卡

- [$d_0$ 与存在域 $U(n,d,k)$](../concepts/existence-region-d0.md)
- [Brill–Noether 数 $\beta$](../concepts/brill-noether-number.md)
- [Petri 曲线](../concepts/petri-curve.md)
- [极大秩猜想](../concepts/maximal-rank-conjecture.md)
- [$(6,3,3)$ 上二次曲面上的曲线](../examples/degree-6-genus-3-quadric.md)

## 出处

- ch7 §7 例 7.5（$g=10$ 的 $d_0$）；中译 p.126（英文 PDF p.140），源码 `chapters/ch07.tex:508`
