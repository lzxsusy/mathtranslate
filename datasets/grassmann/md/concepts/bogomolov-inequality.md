# Bogomolov 不等式

> `grassmann/concept/bogomolov-inequality` · 轨道 3 · Reider 与 Thaddeus 再探 · 状态 draft

> **先自测**：Bogomolov 不等式为什么在曲面上与 $H$ 无关，而在高维必须固定 $H$？

## 一句话

Bogomolov 不等式用第二 Chern 特征给出斜率稳定无挠层的 $c_1^2$ 上界，是 Reider 论证与 Bridgeland 稳定性构造中反复使用的数值工具。

## 定义

设 $X$ 是 $n\ge2$ 维光滑射影簇，$H$ 是充裕除子，$E$ 是 $X$ 上 $H$-Mumford 稳定的无挠凝聚层。**Bogomolov 不等式**断言 $\operatorname{ch}_2(E)\cdot H^{n-2}\le\frac{c_1^2(E)\cdot H^{n-2}}{2\operatorname{rk}(E)}$。当 $X=S$ 是曲面时 $H^{n-2}=1$，不等式退化为 $\operatorname{ch}_2(E)\le\frac{c_1^2(E)}{2\operatorname{rk}(E)}$，与 $H$ 的选取无关。

**记号约定**：$\operatorname{ch}_2=\frac{c_1^2}{2}-c_2$；$H^{n-2}$ 表示与 $n-2$ 次上同调类配对；$\mu_H(E)=\frac{c_1(E)\cdot H^{n-1}}{\operatorname{rk}(E)H^n}$。

## 要点（为什么需要它）

- 稳定性（或半稳定性）是前提：对不稳定的无挠层，$\operatorname{ch}_2$ 没有这种上界。
- 曲面上 $H^{n-2}=H^0=1$，不等式变成纯数值的 $\operatorname{ch}_2(E)\le c_1^2(E)/(2\operatorname{rk}E)$，所以第 2 节的阈值只含 $d$ 而不含 $H$。
- 高维时两侧都要与 $H^{n-2}$ 配对，稳定性本身也依赖 $H$，因此「$H$-稳定」不能省略。
- 本章把它用在两个方向：稳定时用它排除扩张（应用 2.1），Bridgeland 一节用它估计 $d_{(s,t)}$ 的上界（命题 3.3、4.1）。

## 关键公式

$$
\operatorname{ch}_2(E)\cdot H^{n-2}\le\frac{c_1^2(E)\cdot H^{n-2}}{2\operatorname{rk}(E)}
$$

$$
\operatorname{ch}_2(E)=\frac{c_1^2(L)}{2}-d\ \Longrightarrow\ c_1^2(L)\le 4d
$$

## 定理与证明（或缺口）

### 应用 2.1（稳定扩张的次数上界）

若扩张 $\epsilon:0\to\mathcal O_S\to E\to L\otimes\mathcal I_Z\to0$ 中的 $E$ 是 $H$-Mumford 稳定的，则 $c_1^2(L)\le4d$，其中 $d$ 是零维子概形 $Z$ 的长度。

**证明状态：完整**

1. 计算 $\operatorname{ch}_2(E)=\frac{c_1^2(L)}{2}-d$，并注意 $E$ 的秩为 $2$、$c_1(E)=c_1(L)$。
   - *为什么*：扩张的 Chern 特征可加，且 $Z$ 的长度为 $d$。
2. 把 Bogomolov 不等式用于稳定层 $E$，得 $\frac{c_1^2(L)}{2}-d\le\frac{c_1^2(E)}{2\cdot 2}=\frac{c_1^2(L)}{4}$。
   - *为什么*：曲面情形 $H^{n-2}=1$，右边只含 $c_1^2(E)$ 与秩。
3. 移项即得 $c_1^2(L)\le4d$。
   - *为什么*：代数整理。


出处：中译 p.57（§2 应用 2.1）

### Bogomolov 不等式（经典形式）

$E$ 为 $n\ge2$ 维光滑射影簇上 $H$-Mumford 稳定的无挠凝聚层，则 $\operatorname{ch}_2(E)\cdot H^{n-2}\le\frac{c_1^2(E)\cdot H^{n-2}}{2\operatorname{rk}(E)}$。

**证明状态：只引出处，原书不重证**


出处：中译 p.57（§2 引述，Reider 1988 使用）

## 易错点

- 曲面上成立的 $\operatorname{ch}_2(E)\le c_1^2(E)/(2\operatorname{rk}E)$ 与 $H$ 无关，但高维形式必须保留 $H^{n-2}$ 配对；把两者混用会写出不含 $H$ 的错误阈值。
- 不等式对 $H$-半稳定层仍成立，但对任意无挠层一般不成立，引用时必须核对稳定性假设。
- $\operatorname{ch}_2=\frac{c_1^2}{2}-c_2$ 的符号要与「$c_2-\frac{c_1^2}{2}\ge0$」的写法区分，符号反了会得到相反方向的界。

## 相关卡

- [Reider 定理](../concepts/reiders-theorem.md)
- [有效除子的斜率](../concepts/slope-of-effective-divisor.md)
- [Clifford 指标](../concepts/clifford-index.md)

## 出处

- ch3 §2 Bogomolov 不等式；中译 p.57（英文 PDF p.62），源码 `chapters/ch03.tex:110`
