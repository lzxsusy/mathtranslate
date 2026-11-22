# 整体 Langlands 猜想（函数域）：Satake 参数与特征值

> `lbook04/concept/ch10-global-function-field` · 轨 G GL_n 的 Langlands 纲领 · 状态 reviewed · 核验 source-only

**问题：** 为什么整体对应只需比较几乎所有点的特征值，而不必逐点指定？

**一句话：** 函数域上整体对应由「几乎所有点的 Hecke 特征值 = Frobenius 特征值」唯一确定；Lafforgue 用 shtuka 上同调实现，$L$ 函数相等与特征值相等等价。

**别名：** `整体对应`、`Satake 参数`、`shtuka`、`Lafforgue`、`Ramanujan–Petersson`

## 定义

函数域上，整体对应是一个双射 $\mathcal{A}_n^0(k;\overline{\mathbb{Q}}_\ell)_f\to\mathrm{Rep}_n^0(\mathcal{G}_k;\overline{\mathbb{Q}}_\ell)_f$，性质 (i)–(vi) 中最关键的是与局部对应的相容性。给定 $\pi$，几乎所有点 $x$ 处 $\pi_x$ 无分歧，有 Satake 类 $A_{\pi_x}$（共轭类）与 Hecke 特征值 $z_1(\pi_x),\dots,z_n(\pi_x)$；给定 $\rho$，同样有 Frobenius 共轭类 $\rho(\Phi_x)$ 与特征值 $z_i(\rho_x)$。整体猜想断言这两组数几乎处处相等；Chebotarev 保证 Frobenius 共轭类决定 $\rho$，强重数一保证 Hecke 特征值决定 $\pi$。定理 4.1 把这件事凝成「存在唯一双射使 $\{z_i(\pi_x)\}=\{z_i(\rho_{\pi,x})\}$ 对几乎所有 $x$ 成立」，等价于 $L^S(s,\pi)=L^S(s,\rho_\pi)$；定理 4.2（Piatetski-Shapiro–Deligne 归纳）说明只需几乎所有 $x$ 即可。Lafforgue 的证明用 shtuka：双陪集 $\mathrm{GL}_n(k)\backslash\mathrm{GL}_n(\mathbb{A})/\mathrm{GL}_n(\mathcal{O})$ 只参数化秩 $n$ 向量丛，而 shtuka 叠 $\mathcal{V}$ 的 Frobenius 两腿让 Hecke 对应几何化；在 $H^*_c(\bar k\otimes_k\mathcal{V};\overline{\mathbb{Q}}_\ell)$ 上，几何 Grothendieck–Lefschetz 与 Arthur–Selberg 迹公式给出 $\pi\otimes\rho_\pi\otimes\widetilde{\rho}_\pi$。

**记号：** $x$：$k$ 的位点；$A_{\pi_x}$：Satake 类；$z_i(\pi_x)$：Hecke 特征值；$\Phi_x$：$x$ 处的几何 Frobenius；$z_i(\rho_x)$：Frobenius 特征值；$S(\pi)$、$S(\rho)$：分歧位点集；$\mathcal{V}$：shtuka 叠。

## 要点

- Satake 参数是局部–整体的接口：$A_{\pi_x}$ 的特征值是 Hecke 算子 $T_x$ 的特征值，$\rho(\Phi_x)$ 的特征值是 Frobenius 的特征值，猜想说二者相等。
- 定理 4.1 的等价形式是 $L^S(s,\pi)=L^S(s,\rho_\pi)$；由局部因子决定特征值，函数方程与 $\varepsilon$ 的局部分解再把分歧集 $S(\pi)=S(\rho_\pi)$ 升级。
- 定理 4.3 是 Ramanujan–Petersson：$|z_i(\pi_x)|=1$；定理 4.4 是 Deligne 的权 $0$ 纯性，二者都由几何/上同调方法给出，是「纯性 ⇒ Ramanujan」的现代形式。
- 特征 $p$ 的证明不经过模空间，而经过 shtuka 的上同调；这是几何 Langlands 的起点。

## 公式

$$
\{z_i(\pi_x)\}=\{z_i(\rho_{\pi,x})\}\quad\text{对几乎所有 }x
$$

$$
L^S(s,\pi)=L^S(s,\rho_\pi)
$$

$$
\det\bigl(1-t\rho_\pi(\Phi_x)\bigr)^{-1}=\prod_{i=1}^{n}(1-z_i(\pi_x)t)^{-1}
$$

## 定理与证明

**定理 4.1（整体对应）**　存在唯一双射使 $\{z_i(\pi_x)\}=\{z_i(\rho_{\pi,x})\}$ 对几乎所有 $x$ 成立，等价于 $L^S(s,\pi)=L^S(s,\rho_\pi)$。

*出处：译文 §4.1*

**定理 4.2（只需几乎所有点）**　Piatetski-Shapiro–Deligne 归纳：只需几乎所有 $x$ 的特征值相等即可。

*出处：译文 §4.1*

## 易错点

- 把双陪集当成本质：$\mathrm{GL}_n(k)\backslash\mathrm{GL}_n(\mathbb{A})/\mathrm{GL}_n(\mathcal{O})$ 只给出向量丛的同构类，Hecke 算子的几何化需要 shtuka 的 Frobenius 结构。
- 以为需要「所有 $x$」：定理 4.2 说明几乎所有即可，剩下的由函数方程与 $\varepsilon$ 的局部分解补上。
- 把 $z_i(\pi_x)$ 与 $z_i(\rho_x)$ 逐一下标对齐：它们只在集合意义下相等，单个特征值的配对依赖 Satake 参数的选择。

## 批注

**〔背景直觉〕为什么是 shtuka 而不是模空间**　数域上用 Shimura 簇，因为 $\mathrm{GL}_n$ 在数域上没有自然模空间（原书 §4.2 明说）；函数域上向量丛的模叠给出几何对象，shtuka 的 Frobenius 把 Hecke 算子变成对应上的推前，于是迹公式可以在上同调上算。

## 相关

[[ch10-local-langlands]]、[[ch10-global-number-field]]、[[ch10-weil-deligne]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§4.1，原书 pp. 241–244（PDF pp. 244–247）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch10.tex:566-740`
