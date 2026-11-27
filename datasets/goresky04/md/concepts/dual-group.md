# 对偶群与 $L$-群

> `goresky04/concept/dual-group` · 轨道 D · 几何侧与展望 · 状态 dev

> **先自测**：对偶群是怎么从 $G$ 造出来的，为什么它出现在猜想的左侧？

## 一句话

对偶群 $G^\vee$ 由 $G$ 的根数据（把根与余根互换）决定；加上 Galois 作用得到 $L$-群 ${}^{L}G$，它是朗兰兹对应里「左侧」的群。

## 定义

设 $G$ 为约化群，取极大环面 $T$ 与根系 $\Phi\subset X^*(T)$、余根系 $\Phi^\vee\subset X_*(T)$。把这两组数据互换（$X^*\leftrightarrow X_*$，$\Phi\leftrightarrow\Phi^\vee$），得到一个新的根数据，它对应的复约化群就是 $G^\vee$。例如 $\GL(n)^\vee=\GL(n)$，$\SL(n)^\vee=\PGL(n)$，$\mathrm{Sp}(2n)^\vee=\SO(2n+1)$。再加上 Galois 群在根数据上的作用，得到 $L$-群 ${}^{L}G=G^\vee\rtimes\Gal(\Qbar/\bbQ)$。

**记号**：$X^*(T)$ 特征标格；$X_*(T)$ 余特征标格；$W$ 外尔群；${}^{L}G$ 记 $L$-群。

## 要点（为什么需要它）

1. 对偶群的构造是**纯组合**的：只用到根数据，与 $G$ 的具体实现无关；这解释了为什么它可以出现在纯算术的猜想里。
2. 自对偶的例子（$\GL(n)$、$\SO(2n)$、$\mathrm{Sp}(2n)$ 的某些形式）让 $\GL(n)$ 的情形看起来「两边是同一个群」，但一般情形两边不同。
3. 对偶群把「群」与「表示」对偶起来：$G^\vee$ 的有限维表示正是构造 $L$ 函数所需的原料。
4. $L$-群里的半直积（$\rtimes$）不能省：Galois 作用编码了分歧与扭曲，去掉它就只能处理「无扭曲」的对应。

## 核心公式

$$
$\Phi\subset X^*(T)$ 与 $\Phi^\vee\subset X_*(T)$ 互换，得到 $G^\vee$ 的根数据${}^{L}G=G^\vee\rtimes\Gal(\Qbar/\bbQ)$
$$

$$
${}^{L}G=G^\vee\rtimes\Gal(\Qbar/\bbQ)$
$$

## 定理与证明（或缺口）

### 对偶群的组合构造（本文未陈述）

根数据的对偶仍是一个根数据，故对应一个复约化群 $G^\vee$；$G$ 与 $G^\vee$ 的根系互为对偶。

> 证明状态：**gap**。原文 §8.2 只有标题；本卡按根数据的标准理论补出，属 B 级译者按。

出处：`B p.15`

## 常见误解

- $\GL(n)^\vee=\GL(n)$ 会让人误以为对偶群总是自己：$\SL(n)^\vee=\PGL(n)$ 才是常态。
- 对偶群不是「Pontryagin 对偶」：这里是根数据的对偶，与局部紧群的字符群无关（名字撞车而已）。

## 相关卡

[函子性：换群的那条路](../concepts/functoriality.md) · [几何朗兰兹：把猜想搬到曲线上](../concepts/geometric-langlands.md) · [朗兰兹猜想（$\GL(n,\bbQ)$ 版）的陈述](../concepts/langlands-conjecture-statement.md)

## 出处（印刷页）

- A p.15–16（B p.15）

> 说明：原文 §8.2 只有标题；构造与例子按标准根数据理论补，属 B 级译者按。
