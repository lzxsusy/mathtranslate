# Reider 定理

> `grassmann/concept/reiders-theorem` · 轨道 3 · Reider 与 Thaddeus 再探 · 状态 draft

> **先自测**：Reider 定理的数值条件为什么写成 $(d+1)^2$，而不是更自然的 $4d$？

## 一句话

Reider 定理用 $c_1^2(L)>(d+1)^2$ 与所有 $C^2\le0$ 有效除子的数值条件，保证 $K_S+L$ 分离长度 $d$ 的子概形。

## 定义

设 $L$ 是光滑射影曲面 $S$ 上的充裕线丛，$Z\subset S$ 是长度 $d$ 的零维子概形。**Reider 定理**断言：若 $c_1^2(L)>(d+1)^2$，且对 $S$ 上所有满足 $C^2\le0$ 的有效除子 $C$ 都有 $C\cdot c_1(L)>C^2+d$，则 $K_S+L$ 分离长度 $d$ 的子概形，即对所有长度 $\le d$ 的 $Z$ 有 $\operatorname H^1(S,K_S\otimes L\otimes\mathcal I_Z)=0$。

**记号约定**：$d=\deg Z$ 是子概形长度；$C^2$ 是除子自交数；$K_S$ 是典范丛；$L$ 充裕。

## 要点（为什么需要它）

- 条件分成两支：$c_1^2$ 的下界排除稳定扩张，$C\cdot c_1$ 的下界排除不稳定扩张，两支缺一不可。
- $(d+1)^2$ 比 $4d$ 强，来自「$C^2\le d$ 且 $C^2\le0$」的整数性：稳定情形只给 $c_1^2\le4d$。
- $d=1$ 时结论是 $K_S+L$ 无基点，$d=2$ 时是非常充裕，这是定理的几何含义。
- 推论 $K_S+(d+2)L$ 分离长度 $d$ 的子概形，即 Fujita 猜想的曲面情形。

## 关键公式

$$
c_1^2(L)>(d+1)^2,\qquad C^2\le0\ \Longrightarrow\ C\cdot c_1(L)>C^2+d
$$

$$
\operatorname H^1(S,K_S\otimes L\otimes\mathcal I_Z)=0
$$

## 定理与证明（或缺口）

### Reider 定理

设 $L$ 是光滑射影曲面 $S$ 上的充裕线丛，$c_1^2(L)>(d+1)^2$，且对所有满足 $C^2\le0$ 的有效除子 $C$ 有 $C\cdot c_1(L)>C^2+d$。则对所有长度 $\le d$ 的零维子概形 $Z\subset S$，$\operatorname H^1(S,K_S\otimes L\otimes\mathcal I_Z)=0$。

**证明状态：完整**

1. 反设存在长度 $d$ 的 $Z$ 使 $\operatorname H^1(S,K_S\otimes L\otimes\mathcal I_Z)\ne0$；由 Serre 对偶得非零 $\epsilon\in\Ext^1(L\otimes\mathcal I_Z,\mathcal O_S)$，对应扩张 $0\to\mathcal O_S\to E\to L\otimes\mathcal I_Z\to0$。
   - *为什么*：Serre 对偶与一阶扩张的分类。
2. 若 $E$ 是 $H$-Mumford 稳定的，应用 2.1 给 $c_1^2(L)\le4d$，与 $c_1^2(L)>(d+1)^2\ge4d$ 矛盾。
   - *为什么*：应用 2.1；$d\ge1$ 时 $(d+1)^2>4d$。
3. 故 $E$ 不稳定。应用 2.2：要么 $\epsilon=0$（与 $\epsilon\ne0$ 矛盾），要么存在有效曲线 $C$ 使 $C\cdot c_1(L)\le\frac12c_1^2(L)$ 且 $C\cdot c_1(L)\le C^2+d$。
   - *为什么*：应用 2.2 的二分法。
4. 结合 $c_1^2(L)>(d+1)^2$ 得 $C^2\le0$，于是题设的 $C\cdot c_1(L)>C^2+d$ 与第 3 步矛盾。
   - *为什么*：应用 2.2 的结论 (d) 与定理假设。


出处：中译 p.58（§2 Reider 定理）

### 推论（曲面的 Fujita 猜想）

若 $L$ 是光滑射影曲面 $S$ 上的充裕线丛，则 $K_S+(d+2)L$ 分离长度 $d$ 的子概形。

**证明状态：只引出处，原书不重证**


出处：中译 p.58（§2 推论）

## 易错点

- 条件只对满足 $C^2\le0$ 的**有效**除子提出，漏掉「有效」会把任意负自交曲线都算进来。
- $(d+1)^2$ 不能弱化成 $4d$：后者只够排除稳定扩张，非稳定支需要额外的 $C\cdot c_1$ 条件。
- 「分离长度 $d$ 的子概形」等价于对所有长度 $\le d$ 的 $Z$ 有 $H^1=0$，不是只对某一个 $Z$。

## 相关卡

- [Bogomolov 不等式](../concepts/bogomolov-inequality.md)
- [Bridgeland 稳定性条件](../concepts/bridgeland-stability-condition.md)
- [Clifford 指标](../concepts/clifford-index.md)

## 出处

- ch3 §2 Reider 定理；中译 p.58（英文 PDF p.63），源码 `chapters/ch03.tex:175`
