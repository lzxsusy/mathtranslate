# 't Hooft 算符 $\leftrightarrow$ $p$ 处赫克修正（$U(1)$）

> `gtgl15/deriv/thooft-hecke-u1` · 轨道 D · 't Hooft 算符与赫克修正 · 状态 dev · 5 步

> **要回答的问题**：为什么插入一个 't Hooft 算符等价于在 $p$ 处做一次赫克修正，而不是改变整个丛？

## 一句话

以 $U(1)$ 显式单极子解为边界条件，把 3d 超对称方程化成复方程；$[D_1,D_2]=0$ 使全纯结构只在 $p$ 处跳变，故 't Hooft 算符 $=$ 赫克修正 $\mathcal O\mapsto\mathcal O(mp)$。

## 目标

在 $U(1)$ 情形下把 't Hooft 算符的插入翻译成 $p$ 处的赫克修正，并用显式单极子解说明边界条件。

## 前提

- $U(1)$ 规范理论，'t Hooft 算符带磁荷 $m\in\mathbb Z$，在 $\mathbb R^3$ 中的经典解由 Dirac 单极子奇点给出。
- 紧致化到 $\Sigma\times C$：线算符沿 $\Sigma$、在 $p\in C$ 插入；3d 有效理论在 $I\times C$ 上（$I$ 是 $\Sigma$ 中的线段）。
- $C$ 是亏格 $g\ge2$ 的 Riemann 面，$\varphi$ 是 $K$ 值的 Higgs 场。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | $U(1)$ 电荷 1 的解：$F=\frac{i}{2}\star_3\frac{1}{\|\vec x\|}$、$\varphi=\frac{i}{2\|\vec x\|}ds$（eq (4.9)）；磁荷靠 $F$ 与 $\varphi$ 同时奇异。 | 只有 $F$ 奇异不满足超对称，$\varphi$ 的奇点由 BPS 条件决定。 | `A p.40 eq (4.9)` | A·原文明确写了 |
| 2 | 在 3d 有效理论（$I\times C$）中，超对称方程化为 Bogomolny 型 $F=\star D\varphi_s$（eq (4.11)），一般 $t=1$ 时 $0=F-\varphi\wedge\varphi+\star D_A\star\varphi=D_A\star\varphi$（eq (4.12)）。 | 这是 4d 方程的 3d 约化。 | `A p.41 eq (4.12)` | A·原文明确写了 |
| 3 | 定义 $D_1=\bar D_z$、$D_2=D_y-i[\varphi_s,\cdot]$、$D_3=[\varphi_z,\cdot]$，矩映射 $\mu=\sum_i[D_i,D_i^\dagger]$（eq (4.13)(4.14)）；超对称方程 $=$ 复方程 $[D_i,D_j]=0$（eq (4.15)）与 $\mu=0$（eq (4.16)）。 | 复方程形式便于用全纯丛语言。 | `A p.41 eq (4.13)` | A·原文明确写了 |
| 4 | 由 $[D_1,D_2]=0$ 得 $\bar D_z$ 与 $y$ 无关（eq (4.17)）；等价地 $\bar\partial$ 在 $C\setminus\{p\}$ 上良定义，故去掉 $p$ 后是平凡丛。 | 这说明唯一的不平凡性集中在 $p$。 | `A p.42 eq (4.17)` | A·原文明确写了 |
| 5 | $p$ 处的全纯型跳变正是赫克修正；$U(1)$ 情形为 $\mathcal O\mapsto\mathcal O(mp)$（eq (4.19) 的 $U(2)$ 例子在 $U(1)$ 的对应）。 | 赫克修正的定义就是单点处的全纯结构变化。 | `A p.44 eq (4.19)` | B·原文暗示、我们补的中间步 |

## 结论

$U(1)$ 情形：$p$ 处的磁荷 $m$ 't Hooft 算符 $T(m;p)$ 使 $\mathcal O\to\mathcal O(mp)$，即赫克修正。

## 缺口

- 第 5 步在 $U(1)$ 与 $U(2)$ 例子之间是类比：$U(1)$ 的 $\mathcal O(mp)$ 原文在 §4.4.1，而 eq (4.19) 是 $U(2)$ 的。
- 非 minuscule 权与分歧点 $p$ 的情形需要 monopole bubbling，原文未处理。

## 最容易讲错的地方

- 't Hooft 算符的奇点同时含 $F$ 与 $\varphi$；只考虑 $F$ 的 Dirac 弦会漏掉超对称条件。
- $U(1)$ 的 $\mathcal O(mp)$ 对 $m$ 的正负号有约定：$m<0$ 给 $\mathcal O(-p)$，不要照抄符号。
- $p$ 必须非分歧且 $\varphi(p)$ 非零/正则，否则赫克修正的局部结构复杂化。

## 相关卡

['t Hooft 算符](../concepts/thooft-operator.md) · [赫克修正与赫克变换](../concepts/hecke-modification.md) · [线算符](../concepts/line-operators.md) · [磁本征膜](../concepts/magnetic-eigenbranes.md) · [磁本征膜的赫克本征值（$U(1)$ 与 $SU(N)$）](../derivations/magnetic-hecke-eigenvalue.md)

## 出处（印刷页）

- A p.39–43（A p.40 eq (4.9)）
- A p.41–42（A p.42 eq (4.17)）
- A p.43–44（A p.43）

> 说明：A4：eq (4.9)(4.11)–(4.17) 与 $U(2)$ 例子 eq (4.19) 均在原文；B1：第 5 步把 $U(1)$ 的 $\mathcal O(mp)$ 与 eq (4.19) 对应起来。最没把握处：$U(1)$ 的 $\mathcal O(mp)$ 原文在 §4.4.1（p.43），与 eq (4.19) 不同页。
