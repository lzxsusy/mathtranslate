# Q-不变方程与消失定理

> `kw/deriv/vanishing-theorem` · 轨道 B · 扭化与拓扑 · 状态 dev · 4 步

> **要回答的问题**：为什么 $\int\mathrm{Tr}F\wedge F\neq0$ 时 $Q$-不变方程除 $t=0,\infty$ 外无解，而有解时又自动对所有 $t$ 有解？

## 一句话

从 eq (3.29) 出发，用恒等式 eq (3.32) 与 eq (3.33)、(3.34) 证明：紧致无边四维流形上若 $\int\mathrm{Tr}F\wedge F\neq0$，则除 $t=0,\infty$ 外无解；且在一个 $t$ 有解则对所有 $t$ 有解，解为平坦 $G_{\mathbb C}$ 联络。

## 目标

证明两个消失定理，并说明 $t=0,\infty$ 为何例外。

## 前提

- 记 $V^+(t)=(F-\varphi\wedge\varphi+tD\varphi)^+$、$V^-(t)=(F-\varphi\wedge\varphi-t^{-1}D\varphi)^-$、$V_0=D^*\varphi$，见 `B p.28`。
- 讨论范围是实 $t$，此时方程是椭圆方程，见 `B p.28`。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 第一恒等式 eq (3.32) 由分部积分证明：$\int_M\mathrm{Tr}F\wedge F=\int_M\mathrm{Tr}[V^+(t)\wedge V^+(-t^{-1})+V^-(t)\wedge V^-(-t^{-1})]$。若某 $t$ 处 $V^\pm(t)=0$，则积分必为零，即定理 1：$\int\mathrm{Tr}F\wedge F\neq0$ 时 $t\neq0,\infty$ 无解。 | 这条恒等式是全部论证的支点：它把拓扑荷写成两个方程左端的双线性式；跳过这一步，定理 1 只剩猜测。 | `B p.28 eq (3.32)` | A·原文明确写了 |
| 2 | $t=0,\infty$ 时 $V^\pm$ 有极点，eq (3.32) 的证明失效；这两个值确有 $\varphi=0$ 的瞬子或反瞬子解，故定理 1 必须把它们排除。 | 不说明例外，会把定理误读成「任何 $t$ 都无解」，并与后面的紧化应用矛盾。 | `B p.28` | A·原文明确写了 |
| 3 | 第二恒等式 eq (3.33) 把 $V$ 的平方和写成与 $t$ 无关的项加上 $f(t)\int\mathrm{Tr}F\wedge F$，其中 $f(t)=(t-t^{-1})/(t+t^{-1})$；由此得 eq (3.34)：$B(u)-B(t)=(f(u)-f(t))\int_M\mathrm{Tr}F\wedge F$。 | 定理 2 需要「一个 $t$ 有解则所有 $t$ 有解」，这只能由平方和恒等式提供；第一恒等式不够。 | `B p.29 eq (3.34)` | A·原文明确写了 |
| 4 | $B(t)$ 是平方和故半正定。若某 $t\neq0,\infty$ 有解，则 $B(t)=0$ 且 $\int\mathrm{Tr}F\wedge F=0$，由 eq (3.34) 得 $B(u)=0$ 对所有 $u$，即 $V^\pm(u)=V_0=0$ 对所有 $u$，等价于 $F(A+i\varphi)=0$（定理 2）。加强版定理 1′：$\int\mathrm{Tr}F\wedge F>0$ 只允许 $t=0$，$<0$ 只允许 $t=\infty$。 | 这一步把「解集不变」落成 $F(A+i\varphi)=0$，直接给出 §4 紧化所需的平坦 $G_{\mathbb C}$ 联络。 | `B p.30` | A·原文明确写了 |

## 结论

两个恒等式把 $\int\mathrm{Tr}F\wedge F$ 分别写成 $V$ 的双线性式与平方和加 $f(t)\int\mathrm{Tr}F\wedge F$，于是非零 Pontryagin 类排除所有 $t\neq0,\infty$ 的解，而一个解自动延拓为所有 $t$ 的解并给出平坦 $G_{\mathbb C}$ 联络。$t=0,\infty$ 因分母退化而例外，恰是瞬子或反瞬子所在；这一结论在 $\Sigma\times C$ 上把解化成 $\Sigma\to M_H$ 的映射，是 §4 的入口。

## 缺口

- 证明依赖 $B(t)$ 半正定与分部积分，原文未讨论带边界或 $M$ 非紧的情形；非紧版本只给断言。

## 最容易讲错的地方

- 把定理 2 理解成「所有 $t$ 的解空间相同」：原文说的是解集不变，配分函数的符号仍依赖 $t$。
- 忘记 $t=0,\infty$ 的例外来自 $V^\pm$ 的极点，而不是方程本身无解。

## 相关卡

[一族拓扑场论：t ∈ CP¹ 与 Q² = 0](../derivations/one-parameter-family.md) · [紧化到 Hitchin 方程：M = Σ×C](../derivations/compactify-to-hitchin.md) · [瞬子](../concepts/instanton.md) · [拓扑量子场论](../concepts/topological-qft.md)

## 出处（印刷页）

- B p.28–30（B p.28 eq (3.32)）

> 说明：A4：两条恒等式、两个定理与 $t=0,\infty$ 的例外均在 `B p.28–30` 明写；最没把握处是定理 1′ 的陈述位置（`B p.29`）与第 4 步把定理 2、1′ 合并在 `B p.30` 的证明中叙述。
