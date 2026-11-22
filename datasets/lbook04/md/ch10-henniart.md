# 局部对应的四步约化与 Henniart 的结果

> `lbook04/concept/ch10-henniart` · 轨 G GL_n 的 Langlands 纲领 · 状态 reviewed · 核验 source-only

**问题：** 为什么「数值局部 Langlands」与「$\varepsilon$ 因子逆定理」两步合起来就能把对应逼成唯一的？

**一句话：** 证明局部 LL 分四步：$L$ 函数在 $s=0$ 的极点给单射，导子指数做数值比对，$\varepsilon$ 因子逆定理给唯一性，LRS、Harris–Taylor 或 Henniart 给存在性。

**别名：** `局部逆定理`、`数值局部 Langlands`、`Henniart`、`Harris–Taylor`、`LRS`

## 定义

局部对应的证明被拆成四步。(1) 单射：由 $L(s,\rho\otimes\rho')$ 在 $s=0$ 有极点当且仅当 $\rho'\cong\widetilde{\rho}$，以及 $\pi$ 侧对应的极点判据，任何满足猜想 II (ii) 的对应自动单射。(2) 数值：Artin 导子指数 $a(\rho)$ 与 JPSS 导子 $f(\pi)$ 相等，且每个 $(m,\mu)$ 层的表示个数相等，$|\mathrm{Rep}_n^0(\mathcal{G}_k)_{m,\mu}|=|\mathcal{A}_n^0(k)_{m,\mu}|$（Henniart 1988）；这一步只给「数个数」，不给映射。(3) 唯一性：$\varepsilon$ 因子逆定理——若对一切 $1\le m\le n-1$ 与 $\tau\in\mathcal{A}_m^0(k)$ 有 $\varepsilon(s,\pi\times\tau,\psi)=\varepsilon(s,\pi'\times\tau,\psi)$，则 $\pi\cong\pi'$；此时相应扭 $L$ 函数恒 $1$，故只需比对 $\varepsilon$。(4) 存在性：LRS 在正特征用 $\mathcal{D}$-椭圆模空间的上同调；Harris–Taylor 在特征零用 Kottwitz 酉群的简单 Shimura 簇，得到 $\pi\otimes JL(\pi)\otimes\rho_\pi$ 作用于 $\mathrm{GL}_n(k)\times D_n^\times(k)\times W_k$；Henniart 用 Brauer 归纳把 $\rho$ 写成单项表示之和，经局部类域论提升与整体自守诱导，证明更短但无几何实现。

**记号：** $a(\rho)$：Artin 导子指数；$f(\pi)$：JPSS 导子指数；$\mathcal{A}_n^0(k)$：超尖点表示集；$\mathcal{D}$：$\mathrm{GL}_n$ 上的中心除代数；$JL$：局部 Jacquet–Langlands 对应；$\iota$：$\overline{\mathbb{Q}}_\ell\to\mathbb{C}$。

## 要点

- 四步分工：单射与唯一性把「已知的 $L/\varepsilon$」用足，数值步把「未知的对应」数清楚，存在性才是真正的构造。
- 数值 LL 的计数按 $(m,\mu)$ 分层，$m$ 是导子指数、$\mu$ 与中心特征的幂零部分有关；层的划分必须与两边各自的定义一致。
- Harris–Taylor 的构造同时给出局部 LL 与局部 Jacquet–Langlands：$\pi$、$JL(\pi)$、$\rho_\pi$ 出现在同一个上同调里。
- Henniart 的 Brauer 归纳路线依赖 $n=1$（局部类域论）与整体自守诱导的弱情形，是「解析化」的证明，不含几何实现。

## 公式

$$
L(s,\rho\otimes\rho')\ \text{在}\ s=0\ \text{有极点}\iff\rho'\cong\widetilde{\rho}
$$

$$
a(\rho)=f(\pi)
$$

$$
\varepsilon(s,\pi\times\tau,\psi)=\varepsilon(s,\pi'\times\tau,\psi)\ \ (\forall\,1\le m\le n-1,\ \tau\in\mathcal{A}_m^0(k))\ \Longrightarrow\ \pi\cong\pi'
$$

## 定理与证明

**定理 3.2（正特征）**　存在双射 $\mathcal{A}_n^0(k)_f\to\mathrm{Rep}_n^0(\mathcal{G}_k)$，$\pi\mapsto\rho_\pi$，满足 (i)–(v)（LRS）。

*出处：译文 §3.2*

**定理 3.3（特征零）**　同一双射在特征零成立（Harris–Taylor；Henniart）。

*出处：译文 §3.2*

## 易错点

- 把数值相等当成对应存在：它只保证两边计数相同，不给出映射。
- 把「扭 $L$ 恒 $1$」误解为「所有扭都消失」：消失的是 $L$，$\varepsilon$ 仍在，且其单项式性使逐位点比对成为可能。
- 原书 p. 237 两处 Henniart 引文编号 $[28]$ 与 $[30]$ 互换：1988 数值 LL 是 $[28]$，2000 简化证明是 $[30]$。

## 批注

**〔含糊点拨〕为什么 $arepsilon$ 逆定理够用**　对应若存在，扭 $L$ 函数 $L(s,\pi\times\tau)$ 对一切 $\tau$ 都由第 9 章的解析理论已知，比对 $\varepsilon$ 就等价于比对整个局部因子。Piatetski-Shapiro 的逆定理正是这个逻辑的局部版。

## 相关

[[ch10-local-langlands]]、[[ch9-functional-equation]]、[[ch10-global-function-field]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§3.2，原书 pp. 237–240（PDF pp. 240–243）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch10.tex:395-539`
