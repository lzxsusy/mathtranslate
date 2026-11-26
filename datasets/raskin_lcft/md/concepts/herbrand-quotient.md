# Herbrand 商

> `raskin_lcft/concept/herbrand-quotient` ｜ track B ｜ reviewed

**一句话**：循环群上 Tate 上同调的阶之比 χ(M)=#Ĥ⁰/#Ĥ¹；它对短正合列乘性，且有限模上恒为 1，于是把无限模的问题化成有限模。

**自测**：为什么 Herbrand 商对短正合列是乘性的，而「有限模上 χ=1」这条又能用来算无穷阶的同调？

## 定义

设 $G$ 是有限循环群，$M$ 是 $G$-模，且 $\widehat H^0(G,M)$、$\widehat H^1(G,M)$ 都有限。定义 Herbrand 商 $\chi(M)=\#\widehat H^0(G,M)/\#\widehat H^1(G,M)$。它把「同调群的阶」压成一个数，且对短正合列乘性（引理 7.6）。

记号：$\chi(M)=\dfrac{\#\widehat H^0(G,M)}{\#\widehat H^1(G,M)}$。

## 要点

- 乘性（引理 7.6）来自 Tate 上同调的长正合列：把三个模的群排成六项，逐项取阶即得乘积关系。
- 有限 $G$-模上 $\chi(M)=1$（引理 7.9）：$\widehat H^0$ 与 $\widehat H^1$ 同阶，这是所有计算的基准点。
- 典型用法：若 $M$ 含有限指数子模 $M'$，则 $\chi(M)=\chi(M')$——于是无限模的 $\chi$ 可归到有限商上算。
- 第 9 讲的 $\chi(L^\times)=[L:K]$ 就是本卡技术的第一个大用途，也是 lcft 的「数值半边」。

## 公式

\chi(M)=\frac{\#\widehat H^0(G,M)}{\#\widehat H^1(G,M)}
\chi(M)=\chi(M')\ \text{若}\ M'\subseteq M\ \text{指数有限}

## 定理与证明

### 引理 7.6（对短正合列的乘性）

若 $0\to M'\to M\to M''\to 0$ 是 $G$-模短正合列且三者的 Herbrand 商都有定义，则 $\chi(M)=\chi(M')\chi(M'')$。

（sketch；来源：原书 p.30）


缺口：把 Tate 长正合列拆成两个六项正合列，逐项取阶相消。

### 定理 9.1（χ(L^×) = n）

设 $L/K$ 是局部域的次数 $n$ 循环扩张，则 $\chi(L^\times)=n$。

（sketch；来源：原书 p.38）


缺口：用单位群滤过把 $\chi$ 归到有限层上，逐层算得 1，只留赋值 $\mathbb Z$ 层的贡献 $n$。

## 易错点

- 把 χ(M) 当成有理数配不上整数：它是两个有限群阶之比，本身可非整
- 在无限模上直接算 #Ĥ^i（阶无穷）；必须先证明两个上同调群都有限
- 忘记 χ 只在循环群上有定义：一般群的 Tate 上同调没有这种「阶之比」

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 7 讲 链复形与 Herbrand 商，p.29–33（原书 p.29）
- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 9 讲 希尔伯特定理 90 与上链复形，p.38–41（原书 p.38）

关联：`raskin_lcft/concept/tate-cohomology`、`raskin_lcft/concept/hilbert-theorem-90`、`raskin_lcft/concept/lcft-main-theorem`

来源说明：卡由中译本的数学内容改写，不含底本原文；页码为底本印刷页。
