# 行列式线丛与配对 $\langle\mathcal L,\mathcal M\rangle$

> `gtgl15/concept/determinant-line-pairing` · 轨道 E · 行列式线丛与本征值 · 状态 dev

> **先自测**：为什么仅用上同调的行列式线丛就能造出纤维对偶所需的 Poincaré 线丛？

## 一句话

对 $D$ 上度数 0 的线丛，行列式线丛给出典范配对 $\langle\mathcal L,\mathcal M\rangle=\det H^*(\mathcal L)\otimes\det H^*(\mathcal M)/\det H^*(\mathcal L\otimes\mathcal M)\otimes\det H^*(\mathcal O)$，它是 Poincaré 线丛的 twisted 版本。

## 定义

定义 $\det H^*(L)=\det H^0(L)^{-1}\otimes\det H^1(L)$（eq (6.1)；注意与代数几何常用约定相反，本文随 Quillen [41] 的物理约定）。对 $D$ 上线丛 $L,M$ 定义配对 eq (6.2)。由局部化到 $\mathcal O(q)$：eq (6.9) 给 $\det H^*(L(-q))\cong\det H^*(L)\otimes L|_q$，归纳得 eq (6.17) $\langle L,M\rangle=\otimes_i L|_{q_i}^{n_i}$（$M=\otimes_i\mathcal O(q_i)^{n_i}$）。当 $\deg M\ne0$ 时配对依赖 $M$ 的平凡化，需万有线丛并给出 twisted line bundle；$\deg M=0$ 时 eq (6.19) 给出典范定义。

**记号**：$\det H^*$；$\langle L,M\rangle$；$\mathcal O(q)$；twisted line bundle；$c=\deg L$、$d=\deg M$。

## 要点（为什么需要它）

1. 配对是双线性的（eq (6.4)）且对称（eq (6.3)），$\langle L,\mathcal O\rangle\cong\mathbb C$。
2. 核心恒等式 (6.9)：$\det H^*(L(-q))\cong\det H^*(L)\otimes L|_q$，它把配对归结为在点上的取值。
3. 于是对 $M=\otimes\mathcal O(q_i)^{n_i}$ 有 (6.17)：$\langle L,M\rangle=\otimes_i L|_{q_i}^{n_i}$。
4. $\deg M\ne0$ 时 $N$ 只是 twisted line bundle（twisted by gerbe），这正是 §6.3–§6.4 的技术的来源。
5. 曲率计算（eq (6.23)(6.25)）说明 $\langle L,M\rangle$ 就是 Poincaré 线丛的曲率形式。

## 核心公式

$$
$$\det H^*(L)=\det H^0(L)^{-1}\otimes\det H^1(L)$$$$\langle L,M\rangle=\frac{\det H^*(L)\otimes\det H^*(M)}{\det H^*(L\otimes M)\otimes\det H^*(\mathcal O)},\qquad \langle L,\mathcal O(q)\rangle\cong L|_q^{-1}$$
$$

$$
$$\langle L,M\rangle=\frac{\det H^*(L)\otimes\det H^*(M)}{\det H^*(L\otimes M)\otimes\det H^*(\mathcal O)},\qquad \langle L,\mathcal O(q)\rangle\cong L|_q^{-1}$$
$$

## 定理与证明（或缺口）

### 配对的基本性质

$\langle L,M\rangle$ 双线性、对称，且只在 $\deg M=0$ 时典范定义；一般情形是 twisted line bundle。

> 证明状态：**sketch**。立方定理 (6.16) 的完备处理原文引用 [40] Deligne，未在本篇证明。

出处：`A p.60`

## 常见误解

- 约定陷阱：本文的 $\det H^*(L)$ 与代数几何通常的（$\det H^0\otimes\det H^1{}^*$）相反，符号差一个对偶。
- 配对不是数，也不是线丛的同构类：它是一条线丛，只有在 $\deg M=0$ 且平凡化后才给出元素。
- $\langle L,\mathcal O(q)\rangle\cong L|_q^{-1}$ 有负号（inverse），别写成 $L|_q$。
- $\deg M\ne0$ 时不要用普通线丛的语言：必须引入 twisted line bundle（gerbe）。

## 相关卡

[Gerbe 与 $B$-场（离散电/磁荷）](../concepts/gerbe-bfield.md) · ['t Hooft flux 与 $PSU(N)$ 分量](../concepts/thooft-flux-psu.md) · [磁本征膜](../concepts/magnetic-eigenbranes.md) · [阿贝尔化与 Prym 簇](../concepts/abelianization-prym.md) · [磁本征膜的赫克本征值（$U(1)$ 与 $SU(N)$）](../derivations/magnetic-hecke-eigenvalue.md)

## 出处（印刷页）

- A p.59–61（A p.60 eq (6.2)）
- A p.61–62（A p.61 eq (6.17)）
- A p.64–66（A p.65 eq (6.25)）

> 说明：A=原文 $\S6.1$ 的 eq (6.1)–(6.17)、$\S6.2$ 的 twisted line bundle、$\S6.4$ 的曲率计算；B=把性质整理成三步；C=Quillen 度规的背景按脚注 18 补。最没把握处：立方定理的证明原文完全外包给 [40]。
