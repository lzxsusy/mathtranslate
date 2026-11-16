# $\mathbb{C}^n$ 的凯勒极化与全纯截面

> `geoq/example/kahler-polarization-cn` · 轨道 D · 几何量子化机器 · 状态 draft

> **这张卡练什么**：为什么凯勒流形上的极化自动选出全纯截面，而不必额外指定复结构的用法？

## 一句话

用凯勒势定义辛形式与联络，取反全纯方向的极化后极化截面恰为全纯函数，内积带权 $e^{-K/\hbar}$。

## 设定

取 $M=\mathbb{C}^n$，复坐标 $z^1,\dots,z^n$，$K$ 为实值凯勒势。定义 $\omega=i\partial\bar\partial K$，在平凡线丛上取联络 $\nabla=d-\frac{1}{\hbar}\partial K$，内积 $\langle f_1,f_2\rangle=\bar f_1f_2e^{-K/\hbar}$，极化取 $P=\operatorname{Span}\{\partial_{\bar z^1},\dots,\partial_{\bar z^n}\}$。

## 计算

**第 1 步**：验证 $\omega$ 闭、$P$ 迷向：$d\omega=i(\partial+\bar\partial)\partial\bar\partial K=0$，因为 $\partial^2=\bar\partial^2=0$ 且交叉项相消。$\omega$ 是 $(1,1)$ 型，对两个反全纯向量缩并必为零，故 $P$ 是拉格朗日极化。

> 为什么：$(1,1)$ 形式的 $(0,2)$ 分量为零，缩并两个 $(0,1)$ 向量自然得零。

**第 2 步**：写出极化条件。$\partial K$ 是 $(1,0)$ 形式，故 $(\partial K)(\partial_{\bar z^i})=0$，于是 $\nabla_{\partial_{\bar z^i}}f=\partial_{\bar z^i}f=0$，即 $f$ 全纯。

> 为什么：仍然是形式类型起作用：$(1,0)$ 形式作用在 $(0,1)$ 向量上为零。

**第 3 步**：算曲率以确认预量子化：$F_\nabla=d\left(-\frac{1}{\hbar}\partial K\right)=-\frac{1}{\hbar}\bar\partial\partial K$；由 $\omega=i\partial\bar\partial K=-i\bar\partial\partial K$ 得 $\bar\partial\partial K=i\omega$，故 $F_\nabla=-\frac{i}{\hbar}\omega$。

> 为什么：利用 $\partial\bar\partial+\bar\partial\partial=0$（即 $d^2=0$）把 $\bar\partial\partial K$ 换成 $-\partial\bar\partial K$。

**第 4 步**：检验内积与联络相容：把 $d\langle f_1,f_2\rangle=d(\bar f_1f_2e^{-K/\hbar})$ 与 $\langle\nabla f_1,f_2\rangle+\langle f_1,\nabla f_2\rangle$ 作为 1-形式比较，两者相等当且仅当 $\partial K+\bar\partial K=dK$，而 $K$ 实值恰好保证这一点。

> 为什么：相容性要求内积的微分等于两边协变导数之和，$K$ 实值使权的微分拆成 $(1,0)+(0,1)$ 两部分。

**第 5 步**：希尔伯特空间取全纯且范数有限者：$\mathbb{H}=\{f\text{ 全纯}\mid\int|f|^2e^{-K/\hbar}\,\omega^n/n!<\infty\}$。

> 为什么：极化只筛截面，取内积完备化还要加上可积性，否则连常函数都进不来。

## 结果

凯勒极化把预量子化截面化为全纯函数，权为 $e^{-K/\hbar}$；取 $K=|\mathbf{z}|^2$ 即 Segal–Bargmann 空间。

## 复核

(i) 代回 $n=1$，$K=|z|^2$：$\partial K=\bar z\,dz$，$\partial\bar\partial K=dz\wedge d\bar z$，故 $\omega=i\,dz\wedge d\bar z$，而 $F_\nabla=-\frac{1}{\hbar}d\bar z\wedge dz=\frac{1}{\hbar}dz\wedge d\bar z=-\frac{i}{\hbar}\omega$ ✓。(ii) 特例检验：$f=z$ 全纯，$\partial_{\bar z}z=0$；$f=\bar z$ 不是极化截面。(iii) 数值：$n=1$，$K=|z|^2$ 时 $\int_{\mathbb{C}}|z|^{2m}e^{-|z|^2/\hbar}\,dz\,d\bar z$ 对每个 $m\ge0$ 有限，故所有全纯单项式都落在 $\mathbb{H}$ 中。

## 易错点

- 全纯与反全纯方向选错：取 $\{\partial_{\bar z^i}\}$ 得全纯截面，取 $\{\partial_{z^i}\}$ 得反全纯截面；两者给出互为共轭的空间，混用时权会变成 $e^{+K/\hbar}$ 并破坏可积性。
- 相容性必须整体核对：只对单个 $\partial_{z^i}$ 检验会漏掉 $e^{-K/\hbar}$ 求导产生的项，出现因子 2 的假象；正确做法是把两个 1-形式逐项比较。
- 凯勒势不是函数而是势：$K$ 加上一个全纯项与一个反全纯项不改变 $\omega$，却改变权 $e^{-K/\hbar}$，此时要同时做规范变换 $f\mapsto e^{\varphi/\hbar}f$ 才能保持内积，只说「截面全纯」不够。

## 用到哪些概念

- [极化：实极化与凯勒极化](../concepts/polarization.md)
- [预量子化线丛](../concepts/prequantization.md)

## 相关卡

- [$\mathbb{R}^{2n}$ 的实极化与位置波函数](../examples/real-polarization-r2n.md)
- [全纯线丛上的凯勒极化](../examples/holomorphic-line-bundle-polarization.md)
- [Segal–Bargmann 空间](../concepts/segal-bargmann-space.md)

## 出处

- §5.4.4 例 5.4.9，p.289–290（PDF p.290–291），源码 `ch05b.tex:1125-1163`
