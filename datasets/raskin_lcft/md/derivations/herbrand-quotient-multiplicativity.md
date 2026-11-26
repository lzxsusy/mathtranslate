# Herbrand 商的乘性：从正合列乘性到 χ(L^×)=n

> `raskin_lcft/deriv/herbrand-quotient-multiplicativity` ｜ track B ｜ reviewed

**目标**：证明 Herbrand 商对短正合列乘性，并据此求 χ(L^×)=[L:K]。

**自测**：为什么一个关于「群阶乘积」的初等事实，最后能算出局部域范数商的阶？

## 前提

- $G$ 是有限循环群，$M$ 是 $G$-模，$\widehat H^0,\widehat H^1$ 均有限（否则 $\chi$ 无定义）。
- 对局部域情形取 $M=L^\times$、$G=\mathrm{Gal}(L/K)$ 循环。

## 步骤

1. **先证有限阿贝尔群的乘性：正合列 $0\to X_0\to\cdots\to X_n\to0$ 满足 $\#X_0\cdots\#X_n=\#X_1\cdots\#X_{n-1}$。**  
   为什么：这是「逐项相消」的源头，后面所有乘性都由它推出。  
   锚点：原书 p.25（证据 A）

2. **由 1 得 Euler 特征 $\chi(M)=\#M/n\,/\,\#M[n]$ 对短正合列乘性（引理 6.7）。**  
   为什么：$\chi$ 把「两个群的阶」编码成一个乘法不变量。  
   锚点：原书 p.25（证据 A）

3. **把 Tate 长正合列（断言 6.16）在 $i=-1,0,1$ 处拆成两个六项正合列，对每个套用 1，得到 $\chi(M)=\chi(M')\chi(M'')$（引理 7.6）。**  
   为什么：长正合列的两端正好是 $\widehat H^0$ 与 $\widehat H^1$，相消后只剩它们的阶之比。  
   锚点：原书 p.30（证据 A）

4. **有限 $G$-模上 $\widehat H^0$ 与 $\widehat H^1$ 同阶，故 $\chi(M)=1$（引理 7.9）。**  
   为什么：有限模是「基准点」：所有计算都归结到把一般模夹在有限模之间。  
   锚点：原书 p.31（证据 A）

5. **对 $L^\times$ 用单位群滤过 $U^0\supseteq U^1\supseteq\cdots$：每层商是 $k$ 的加法群（或 $\mu$），$\chi=1$；只留 $\mathbb Z$ 层贡献 $n$。**  
   为什么：滤过的商都是有限模或平凡模，逐层乘性后只剩赋值层。  
   锚点：原书 p.38（证据 A）

6. **得 $\chi(L^\times)=n=[L:K]$；配合 $\widehat H^1(L^\times)=0$（定理 9.2）得 $\#\widehat H^0(L^\times)=n$。**  
   为什么：这正是 lcft 需要的数：$\#(K^\times/NL^\times)=[L:K]$。  
   锚点：原书 p.38（证据 B）

## 结果

$\chi(L^\times)=[L:K]$，且 $\#\widehat H^0(G,L^\times)=[L:K]$、$\#\widehat H^1(G,L^\times)=0$。

## 缺口

- 第 5 步的滤过细节原文只给概要：$U^i/U^{i+1}$ 上与 $G$ 作用的关系需逐层核对（驯分歧/不驯分歧不同）。
- 若 $L/K$ 不循环，$\chi$ 无定义，这条路线必须改成「对每个循环子群算、再用 16.3 的 Sylow 归约」。
- 引理 6.4 在底本里印出的指标链自相矛盾（见勘误卡 exactness-index），本卡用的是订正后的标准归纳。

## 易错点

- $\chi$ 只在循环群上有定义；把 7.6 直接用在非循环扩张上会得到无意义的式子。
- 把 $\#\widehat H^0=\#\widehat H^1$ 当普遍事实：只在有限模上成立。
- 忘记第 5 步里 $\mathbb Z$ 层的贡献是 $n$ 而不是 1。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 6 讲 正合列与 Tate 上同调，p.24–28（原书 p.24）
- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 7 讲 链复形与 Herbrand 商，p.29–33（原书 p.29）
- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 9 讲 希尔伯特定理 90 与上链复形，p.38–41（原书 p.38）

关联：`raskin_lcft/concept/herbrand-quotient`、`raskin_lcft/concept/tate-cohomology`、`raskin_lcft/concept/hilbert-theorem-90`

来源说明：步骤按底本论证顺序重写；provenance 见 SCHEMA（A 原文显式 / B 原文略写由邻页补 / C 译者补证）。
