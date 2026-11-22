# L 函数的零点与显式公式

> `lbook04/concept/ch2-explicit-formula` · 轨 L L 函数 · 状态 reviewed · 核验 source-only

**问题：** 显式公式为什么能把「素数的分布」与「L 函数零点的位置」精确地等同起来？

**一句话：** 显式公式把素数幂上的 von Mangoldt 和写成极点主项、零点求和与阿基米德积分三项；零点计数 $N(\chi;T)$ 的主项来自 $\Gamma$ 因子。

**别名：** `显式公式`、`零点计数`、`Hadamard 乘积`

## 定义

命题 3.1 给出零点计数：$N(\chi;T)=\frac{T}{2\pi}\log\frac{T^d|D|N\mathfrak m}{(2\pi e)^d}+O(\log(T^d|D|N\mathfrak m))$，且 $\sum_\rho|\rho|^{-1-\varepsilon}$ 绝对收敛。证明用 Cauchy 定理在矩形上积分 $\Lambda'/\Lambda$，主要贡献来自 $\Gamma$ 因子，其余由 Hadamard 乘积控制。$\operatorname{Re}(s)=1$ 上无零点（1896 年 Hadamard 与 de la Vallée Poussin）是无零点区域与素理想定理的关键。命题 3.5 的显式公式 (3.6) 把 $\sum_{\mathfrak a}\Lambda(\mathfrak a)(\chi(\mathfrak a)\varphi(N\mathfrak a)+\overline\chi(\mathfrak a)\psi(N\mathfrak a))$ 写成 $(\log|D|N\mathfrak m)\varphi(1)+\delta(\chi)\int\varphi-\sum_{L(\chi,\rho)=0}\hat\varphi(\rho)$ 再加阿基米德积分与 $s=0$ 的留数；检验函数取光滑紧支集时各项绝对收敛，公式是恒等式而非极限。

**记号：** $N(\chi;T)$：虚部在 $[-T,T]$ 内的零点数；$\Lambda(\mathfrak a)$：von Mangoldt 函数；$\varphi,\hat\varphi$：检验函数与其 Mellin 变换；$\psi(x)=\varphi(x^{-1})/x$；$\delta(\chi)$：$\chi$ 平凡时为 $1$，否则为 $0$。

## 要点

- 显式公式是「素数 $\leftrightarrow$ 零点」的精确字典：左边是素数幂上的和，右边是极点主项、零点项与阿基米德项。
- 主项来自 $s=1$ 的极点（仅 $\chi$ 平凡时）与 $\log|D|N\mathfrak m$；零点项逐项对应非平凡零点；阿基米德项吸收 $\Gamma'/\Gamma$。
- 零点计数的主项 $\frac{T}{2\pi}\log(T^d|D|N\mathfrak m)$ 中 $1/2\pi$ 与 $d\log T$ 都来自 $\Gamma$ 因子——「零点密度由无穷处的局部因子控制」。

## 公式

$$
N(\chi;T)=\frac{T}{2\pi}\log\frac{T^d|D|N\mathfrak m}{(2\pi e)^d}+O\bigl(\log(T^d|D|N\mathfrak m)\bigr)
$$

$$
\sum_{\mathfrak a}\Lambda(\mathfrak a)\bigl(\chi(\mathfrak a)\varphi(N\mathfrak a)+\overline\chi(\mathfrak a)\psi(N\mathfrak a)\bigr)=(\log|D|N\mathfrak m)\varphi(1)+\delta(\chi)\int_0^{\infty}\varphi-\sum_{L(\chi,\rho)=0}\hat\varphi(\rho)+\cdots
$$

$$
\Lambda(\chi,s)=e^{a+bs}\prod_{\rho}\bigl(1-\frac{s}{\rho}\bigr)e^{s/\rho}\qquad(\chi\ne1)
$$

## 易错点

- 照抄书中 (3.6) 的下标 $\zeta(\rho)=0$：应为 $L(\chi,\rho)=0$，否则会漏掉全部 $L(\chi,s)$ 的零点（中译注本已出译注）。
- 忽略 $\delta(\chi)$ 项：只有 $\chi$ 平凡时才有 $\int\varphi$ 项（对应 $\zeta$ 在 $s=1$ 的极点）；非平凡时该项为零。

## 批注

**〔易错预警〕ζ(ρ) 是笔误**　中译注本在 (3.6) 后出注：影印作 $\zeta(\rho)=0$，是照抄第 1 章 (2.5) 未改符号；一般情形必须写 $L(\chi,\rho)=0$。同一段的伽马项与 $-L'/L$ 都写明取自 $L(\chi,\cdot)$，可见下标确是排印疏漏。

**〔背景直觉〕为什么零点计数主项来自 Γ**　用 Cauchy 定理在矩形上积分 $\Lambda'/\Lambda$，主要贡献来自 $\Gamma'/\Gamma$（Stirling 公式给 $T\log T$），而 $L'/L$ 的贡献被 Hadamard 乘积控制为 $O(\log)$。这就是「零点密度由阿基米德因子决定」的机制，也是显式公式里 $\log|D|N\mathfrak m$ 出现的原因。

## 相关

[[ch2-nonvanishing]]、[[ch1-gamma-factor]]、[[ch2-goldfeld]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§3，原书 pp. 26–27（PDF pp. 34–35）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch02.tex:231-261`
- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§3，原书 pp. 30–32（PDF pp. 38–40）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch02.tex:332-360`
