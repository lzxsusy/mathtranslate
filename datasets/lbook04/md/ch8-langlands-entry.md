# 自守表示的 L 函数与 Langlands 纲领入口

> `lbook04/concept/ch8-langlands-entry` · 轨 T Tate 与迹公式 · 状态 reviewed · 核验 source-only

**问题：** 为什么说 Jacquet–Langlands 对应是 Langlands 函子性的「第一个实例」，它对应的对偶群同态是什么？

**一句话：** 第 8 章末把 $D^\times$ 的迹公式与 $\operatorname{GL}(2)$ 比较，得 Jacquet–Langlands 提升与 $L$ 函数、$\varepsilon$ 因子的保持；这正是 Langlands 函子性的第一个非交换实例。

**别名：** `Godement–Jacquet L 函数`、`函子性提升`、`Langlands 纲领`

## 定义

定理 54–55 的比较给出 $\pi\leftrightarrow\pi'$ 的对应，且保持 $L$ 函数与 $\varepsilon$ 因子（annote 2008–2014）。1991–1993 年 Jacquet–Langlands 用 Godement–Jacquet 构造证明 $D^\times$ 上 $L$ 函数的函数方程——因为 $D^\times$ 上没有 Hecke 积分可用。书中 1950 行明确写出：$\pi\to\pi'$ 是 Langlands 意义上的自守形式函子性提升。对偶群侧：$\operatorname{GL}(2)$ 与 $D^\times$ 的内形式共享 $L$-群，对应由 ${}^LG$ 的恒等映射诱导。

**记号：** $L(s,\pi)$、$\varepsilon(s,\pi,\psi)$；Godement–Jacquet $L$ 函数；${}^LG$：$L$-群；内形式（inner form）。

## 要点

- Jacquet–Langlands 是「内形式」之间的对应：$\operatorname{GL}(2)$ 与 $D^\times$ 有相同的 $L$-群，故函子性由恒等同态诱导。
- $L$ 函数与 $\varepsilon$ 因子的保持是定理 55 的核心；没有它，$D^\times$ 侧的迹公式无法转回 $\operatorname{GL}(2)$。
- Godement–Jacquet 用「表示空间上的积分」构造 $L$ 函数，绕开 Whittaker/Hecke 积分，适用于 $D^\times$。
- 这是全书的入口：第 8 章的迹公式比较 $=$ Langlands 函子性的一个具体案例，后续章节把它推广到 $\operatorname{GL}(n)$。

## 公式

$$
L(s,\pi)=L(s,\pi'),\qquad \varepsilon(s,\pi,\psi)=\varepsilon(s,\pi',\psi)
$$

$$
\pi\ \text{是}\ D_{\mathbb A}^\times\ \text{自守表示}\iff\forall v\in S,\ \pi_v\ \text{平方可积}
$$

## 易错点

- 不要把 Jacquet–Langlands 说成「$\operatorname{GL}(2)$ 表示都来自 $D^\times$」：定理 55 的条件是 $\pi$ 在 $S$ 的每个位平方可积，否则对应不存在。
- $L$-群的同态是恒等，但「内形式」改变的是群本身而不是 $L$-群；把内形式对应误作函子性的一般情形（如 $\operatorname{Sym}^2$）会搞错对偶侧。

## 批注

**〔背景直觉〕全书的收束**　第 5–8 章从椭圆曲线 $L$ 函数走到 Tate 论文、自守表示与迹公式；第 8 章末的 Jacquet–Langlands 提升把「表示论比较」与「$L$ 函数保持」绑在一起，正是 Langlands 函子性的原型。

**〔含糊点拨〕$L$ 函数的两条路**　$\operatorname{GL}(2)$ 侧用 Whittaker/Hecke 积分（第 7 章 §5），$D^\times$ 侧只能用 Godement–Jacquet（无 Whittaker）；两条构造在对应下相等，这是 1991–1993 年工作的技术核心。

## 相关

[[ch8-arthur-selberg]]、[[ch8-eisenstein]]、[[ch7-newform]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§10 末段，原书 pp. 190–191（PDF pp. 193–194）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch08.tex:1950-2016`
