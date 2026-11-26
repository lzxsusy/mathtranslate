# 希伯特定理 90（Tate 上同调版）

> `raskin_lcft/concept/hilbert-theorem-90` ｜ track B ｜ reviewed

**一句话**：循环扩张上 Ĥ¹(G,L^×)=0；等价形式是「范数 1 的元素都是 y/σy」。它是 lcft 里唯一无条件成立的消没。

**自测**：为什么「N(x)=1 ⟹ x=y/σy」在循环扩张上总成立，而它的 n 次推广（H¹=0）却是 lcft 的内容？

## 定义

希伯特定理 90：若 $L/K$ 是循环扩张、$G=\mathrm{Gal}(L/K)$，则 $\widehat H^1(G,L^\times)=0$。展开即：$x\in L^\times$ 满足 $N_{L/K}(x)=1$ 时，存在 $y\in L^\times$ 使 $x=y/\sigma y$；更一般地 $H^1(G,L^\times)=0$ 对任意有限 Galois 扩张成立（命题 18.13 给出无限版本）。

记号：$N(x)=1\iff x=y/\sigma y$；$\widehat H^1(G,L^\times)=0$。

## 要点

- 证明只用线性代数：把 $x$ 看成 $L$ 上的线性变换，取合适的基向量 $y$，由 $N(x)=1$ 解出 $x=y/\sigma y$。
- 它是「消没」的原型：$\widehat H^1$ 的控制来自范数映射满射，而 lcft 里是 $\widehat H^0$ 与 $\widehat H^1$ 同时受控。
- $\chi(L^\times)=n$（定理 9.1）+ $\widehat H^1=0$（定理 9.2）合起来给出 $\#\widehat H^0(L^\times)=n$，这正是 lcft 想要的数。
- 无限 Galois 版本（命题 18.13）不是免费的：要用投射有限上同调把 $L=\bigcup L_i$ 的各层拼起来。

## 公式

\widehat H^1(G,L^\times)=0
N_{L/K}(x)=1\iff x=y/\sigma y

## 定理与证明

### 定理 9.2（Hilbert 90）

设 $L/K$ 是局部域的次数 $n$ Galois（循环）扩张，$G=\mathrm{Gal}(L/K)$，则 $\widehat H^1(G,L^\times)=0$。

（complete；来源：原书 p.38）

1. 取 $x\in L^\times$ 满足 $N(x)=1$，把 $x$ 看作 $L$ 上的 $K$-线性变换。  
   为什么：范数条件是「行列式为 1」的乘法版。
2. 由 $\sum_i \sigma_i(x)=1$（$n$ 个共轭的和除以 $n$）取 $y$ 使 $\sum_i\sigma_i(xy)\neq0$。  
   为什么：要构造 $y$ 使 $xy$ 与 $\sigma(xy)$ 差出 $y$。
3. 令 $y$ 为上述向量，则 $x=y/\sigma y$；代入即得 $1$-上边缘。  
   为什么：直接展开 $\sigma y=\sigma(x)y$。

缺口：第 9 讲用「上链复形 + 范数」的写法重做一遍，与上同调定义对齐。

### 命题 18.13（无限 Galois 版本）

设 $L/K$ 是（可能无限的）Galois 扩张、$G=\mathrm{Gal}(L/K)$ 投射有限，则 $H^1(G,L^\times)=0$。

（sketch；来源：原书 p.79）


缺口：把 $L=igcup_i L_i$ 写成有限层，对每层用 90，再取逆向极限；原文在 18.13 处把变元误印成 $K_i^	imes$（见勘误）。

## 易错点

- 把 90 当成「H¹(G,L^×)=0 对一切 G」：只对循环/伽罗瓦情形成立，无限群版本要 18.13
- 忘记 Ê¹ 与通常 H¹ 的差别：有限群时两者只差一个 Tate 修正
- 把 y/σy 写成 y·σy（乘而不是除）

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 9 讲 希尔伯特定理 90 与上链复形，p.38–41（原书 p.38）
- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 18 讲 范数群与 Kummer 理论，p.76–80（原书 p.76）

关联：`raskin_lcft/concept/herbrand-quotient`、`raskin_lcft/concept/tate-cohomology`、`raskin_lcft/concept/lcft-main-theorem`

来源说明：卡由中译本的数学内容改写，不含底本原文；页码为底本印刷页。
