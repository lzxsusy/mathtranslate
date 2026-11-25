# $(6,3,3)$ 上二次曲面上的曲线

> `grassmann/example/degree-6-genus-3-quadric` · 轨道 2 · Koszul 上同调 · 状态 draft

> **这张卡练什么**：为什么 $\mathfrak{I}_{6,3,3}$ 中「$\nu_2$ 不同构」恰好等于「曲线位于某个二次曲面上」？

## 一句话

在 $\mathfrak{I}_{6,3,3}$ 里，$\nu_2$ 失效当且仅当曲线落在某个二次曲面上；二次曲面上的曲线必为 $(2,4)$ 型、从而是超椭圆曲线，这是一个真除子条件。

## 背景定义

考虑 $\deg(C)=6$、$g(C)=3$ 的光滑曲线 $C\subset\mathbb{P}^3$，即 Hilbert 概形分支 $\mathfrak{I}_{6,3,3}$ 中的点。**例 5.2** 考察 $C$ 位于某个二次曲面 $Q\subset\mathbb{P}^3$ 上的轨迹，并断言这恰好是 $\nu_2(C)$ 不同构的轨迹：它是 $\mathfrak{I}_{6,3,3}$ 上的一个除子条件，而对一般的 $[C\hookrightarrow\mathbb{P}^3]\in\mathfrak{I}_{6,3,3}$，$\nu_2(C)$ 是同构。

## 设定

$C\subset\mathbb{P}^3$ 光滑，$\deg C=6$、$g(C)=3$，$\mathcal{O}_C(1)$ 次数 $6$、非特殊；比较 $C$ 是否落在某个二次曲面上与 $\nu_2(C)$ 的秩。

## 计算

若 $C\subset Q$，在 $Q\cong\mathbb{P}^1\times\mathbb{P}^1$ 上记 $C$ 为 $(a,b)$ 型，则 $a+b=6$、$(a-1)(b-1)=3$，解得 $\{a,b\}=\{2,4\}$。此时 $\dim\mathrm{Sym}^2H^0(C,\mathcal{O}_C(1))=\binom{5}{2}=10$，而 $h^0(C,\mathcal{O}_C(2))=12-3+1=10$，两端同维；$Q$ 的二次方程在 $C$ 上为零，给出 $\nu_2$ 的非零核，故 $\nu_2$ 不同构。

## 要点

- 双次数解唯一：$a+b=6$ 与 $ab-(a+b)+1=3$ 联立得 $ab=8$，故 $\{a,b\}=\{2,4\}$。
- $(2,4)$ 型曲线被 $Q$ 的一族直线以 $2:1$ 覆盖，带 $g^1_2$，是超椭圆曲线；这与 $\mathrm{Cliff}(C)=0$ 一致。
- 维数巧合是本题的关键：$\dim\mathrm{Sym}^2H^0(\mathcal{O}_C(1))=\binom{5}{2}=10=h^0(\mathcal{O}_C(2))$，所以「极大秩」在这里只能是同构。
- 「位于二次曲面上」是 Hilbert 概形中的真闭条件（$h^0(\mathbb{P}^3,\mathcal{I}_C(2))\neq0$），故它对一般曲线不成立。

## 关键公式

$$
\deg C=a+b=6,\qquad g(C)=(a-1)(b-1)=3\ \Longrightarrow\ \{a,b\}=\{2,4\}
$$

$$
\dim\mathrm{Sym}^2H^0(C,\mathcal{O}_C(1))=\binom{5}{2}=10=h^0(C,\mathcal{O}_C(2))
$$

$$
q\in H^0(\mathbb{P}^3,\mathcal{O}(2)),\ q|_C=0\ \Longrightarrow\ q\in\ker\nu_2(C)
$$

## 相关定理

- **例 5.2（$(6,3,3)$ 的极大秩）**：设 $C\subset\mathbb{P}^3$ 光滑、$\deg C=6$、$g(C)=3$。则 $\nu_2(C)$ 不同构当且仅当 $C$ 位于某个二次曲面上；这样的曲线在 $Q$ 上必为 $(2,4)$ 型、特别地是超椭圆曲线。对一般的 $[C\hookrightarrow\mathbb{P}^3]\in\mathfrak{I}_{6,3,3}$，$\nu_2(C)$ 是同构。
- **猜想 5.1 在此分支的解读**：对一般 $[C\hookrightarrow\mathbb{P}^3]\in\mathfrak{I}_{6,3,3}$ 与 $n=2$，极大秩猜想预言 $\nu_2(C)$ 是单射或满射；由 $\binom{2+3}{2}=10=2\cdot6+1-3$ 两端同维，即预言它是同构——这正是例 5.2 的结论。

## 易错点

- 把 $(a,b)$ 型当成「$a$ 次曲线」：双次数 $(2,4)$ 的总次数是 $a+b=6$，不是 $2$ 或 $4$。
- 忽略维数巧合：一般 $(d,g,r)$ 下 $\nu_2$ 两端维数不同，「极大秩」不等于「同构」；例 5.2 恰好 $\binom{5}{2}=10=h^0(\mathcal{O}_C(2))$，才能把「不同构」与「不满射」互换。
- 以为二次曲面上的曲线都超椭圆：只有 $g=3$、$\deg 6$ 的特殊参数下 $(a,b)=(2,4)$ 才自动带 $g^1_2$；一般双次数曲线的棱性不是 $2$。
- 忘记 $\mathcal{O}_C(1)$ 的非特殊性：$h^0(\mathcal{O}_C(2))=10$ 用到 $\deg=12>2g-2=4$。

## 用到哪些概念

- [极大秩猜想](../concepts/maximal-rank-conjecture.md)
- [Koszul 对偶](../concepts/koszul-duality.md)
- [Green 猜想](../concepts/greens-conjecture.md)

## 相关卡

- [极大秩猜想](../concepts/maximal-rank-conjecture.md)
- [$g=10$、$(2,12,4)$ 的 $d_0$（例 7.5）](../examples/example-genus-10-d0.md)
- [核丛](../concepts/kernel-bundle.md)

## 出处

- ch2 §5.1 例 5.2；中译 p.49（英文 PDF p.53），源码 `chapters/ch02.tex:813`
- ch2 §5.1 极大秩猜想；中译 p.49（英文 PDF p.53），源码 `chapters/ch02.tex:803`
