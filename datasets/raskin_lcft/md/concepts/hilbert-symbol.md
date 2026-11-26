# 希尔伯特符号

> `raskin_lcft/concept/hilbert-symbol` ｜ track A ｜ reviewed

**一句话**：K^×/(K^×)^2 上的双乘配对：若 b 是 K(√a)/K 的范数则取 1，否则取 −1。n=2 的 lcft 全部内容都装在这个符号里。

**自测**：为什么「b 是 K(√a)/K 的范数」这件事能用一个 ±1 的双乘性符号来记录？

## 定义

对 $a,b\in K^\times$，定义 $(a,b)_K=1$ 当且仅当 $b$ 属于 $K(\sqrt a)/K$ 的范数群，否则 $(a,b)_K=-1$。它诱导 $K^\times/(K^\times)^2\times K^\times/(K^\times)^2\to\{\pm1\}$，双乘（命题 2.3）、非退化，且完备刻画二次扩张的范数群（定理 2.12）。

记号：$(\ ,\ )_K$；$b\in N_{K(\sqrt a)/K}K(\sqrt a)^\times\iff(a,b)_K=1$。

## 要点

- 定义是「存在范数」的编码：符号只记 1/−1，却等价于一个范数条件，所以能承载群论信息。
- 双乘性使 $(,)_K$ 下降为 $K^\times/(K^\times)^2$ 上的配对，非退化性于是说「正交补 = 范数群」。
- n=2 时定理 1.5 变成：$K^\times/NL^\times$ 的阶为 2 且同构于 $\mathrm{Gal}(L/K)$，符号恰好给出这个同构。
- 显式公式（第 5 讲）把 $(,)_K$ 算成幂次，从而把二次互反律化为乘积公式。

## 公式

(a,b)_K=1\iff b\in N_{K(\sqrt a)/K}\,K(\sqrt a)^\times
(\ ,\ )_K:\ \frac{K^\times}{(K^\times)^2}\times\frac{K^\times}{(K^\times)^2}\to\{\pm1\}

## 定理与证明

### 命题 2.3（良定义与双乘性）

$(a,b)_K$ 只依赖 $a,b$ 的平方类，且对每个变元都是同态：$(a_1a_2,b)=(a_1,b)(a_2,b)$，$(a,b_1b_2)=(a,b_1)(a,b_2)$，$(a,b)=(b,a)$。

（sketch；来源：原书 p.6）


缺口：原文用范数群与 Hilbert 90 给出，双乘性的解释句在底本里印重了（见勘误卡）。

### 定理 2.12（二次扩张的范数群）

若 $L=K(\sqrt a)$ 是二次扩张，则 $NL^\times$ 是 $K^\times$ 中指数 2 的开子群，且由 $(a,\ )_K$ 的核给出。

（sketch；来源：原书 p.9）


缺口：证明依赖 $L$ 的局部结构（第 3 讲的驯分歧计算是同一技术的加强版）。

## 易错点

- 把 (,)_K 的取值域记成分数或 Z（实际只有 ±1）
- 在 a 是平方时仍去讨论 K(√a)（此时扩张平凡，符号恒为 1）
- 把「非退化」当成「双乘」：两者是不同方向的性质
- 把 $(a,b)=1$ 理解为「$a$ 与 $b$ 互素」：这是域上的符号，与素性无关。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 2 讲 希尔伯特符号，p.6–9（原书 p.6）
- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 3 讲 带驯分歧的范数群，p.10–12（原书 p.10）

关联：`raskin_lcft/concept/lcft-main-theorem`、`raskin_lcft/concept/norm-group`、`raskin_lcft/concept/tame-ramification`

来源说明：卡由中译本的数学内容改写，不含底本原文；页码为底本印刷页。
