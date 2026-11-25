# Green 维数公式

> `grassmann/concept/greens-dimension-formula` · 轨道 2 · Koszul 上同调 · 状态 draft

> **先自测**：为什么这个公式只在非特殊线丛上成立，特殊线丛要加哪些修正项？

## 一句话

非特殊线丛 $L$ 上 $K_{p,1}$ 与 $K_{p-1,2}$ 的维数差有闭形式，只依赖 $g,d,p$；它给出 $K_{p,1}$ 非消没的数值阈值，是 Green 猜想最优性的计算基础。

## 定义

设 $C$ 是亏格 $g\ge2$ 的光滑曲线，$L$ 是次数 $d$、非特殊且整体生成的线丛，$r=h^0(C,L)-1$。对 $1\le p\le r$，**Green 维数公式**（定理 2.8）为 $\dim K_{p,1}(C,L)-\dim K_{p-1,2}(C,L)=p\binom{d-g}{p}\left(\frac{d+1-g}{p+1}-\frac{d}{d-g}\right)$。

**记号约定**：$d=\deg L$，$r=h^0(C,L)-1$；非特殊即 $h^1(C,L)=0$，于是 $r=d-g$。

## 要点（为什么需要它）

- 证明只有五行：先用对偶把两个群换成 $K_{r-p-1,1}(C,K_C,L)^{\vee}$ 与 $K_{r-p,0}(C,K_C,L)^{\vee}$，再用核丛 $M_L$ 的 Koszul 复形算 Euler 示性数。
- 关键同构 $\wedge^{r-p-1}M_L\otimes L\cong\wedge^{p+1}M_L^{\vee}$（因 $\det M_L=L^{-1}$）把 $h^0$ 换成 $-\chi$，之后 Riemann–Roch 直接给出闭式。
- $p<\frac{(d+1-g)(d-g)}{d}-1$ 时 $K_{p,1}\neq0$；$\frac{(d+1-g)(d-g)}{d}\le p\le d-g$ 时 $K_{p-1,2}\neq0$。
- $p=d-g$ 是分界点：$p>d-g$ 时 $\binom{d-g}{p}=0$，公式退化为 $\dim K_{p,1}=\dim K_{p-1,2}$，不再给非消没信息。

## 关键公式

$$
\dim K_{p,1}-\dim K_{p-1,2}=p\binom{d-g}{p}\left(\frac{d+1-g}{p+1}-\frac{d}{d-g}\right)
$$

$$
h^0(C,\wedge^{r-p-1}M_L\otimes K_C\otimes L)=-\chi(C,\wedge^{p+1}M_L)
$$

$$
-\chi(C,\wedge^{p+1}M_L)=d\binom{r-1}{p}+(g-1)\binom{r}{p+1}
$$

## 定理与证明（或缺口）

### 定理 2.8（Green 维数公式）

设 $L$ 是亏格 $g\ge2$ 的光滑曲线 $C$ 上非特殊整体生成的线丛，$d=\deg L$，$r=h^0(C,L)-1$，$1\le p\le r$。则 $\dim K_{p,1}(C,L)-\dim K_{p-1,2}(C,L)=p\binom{d-g}{p}\left(\frac{d+1-g}{p+1}-\frac{d}{d-g}\right)$。

**证明状态：完整**

1. 由定理 2.7 取 $n=1$、$q=1,2$，得 $K_{p,1}(C,L)\cong K_{r-p-1,1}(C,K_C,L)^{\vee}$ 与 $K_{p-1,2}(C,L)\cong K_{r-p,0}(C,K_C,L)^{\vee}$。
   - *为什么*：$n=1$ 时定理 2.7 的假设是对 $i=1,\dots,0$ 的空条件，故对任何整体生成线丛成立。
2. 考虑 Koszul 复形 $0\to\wedge^{r-p}H^0(L)\otimes H^0(K_C)\to H^0(\wedge^{r-p-1}M_L\otimes K_C\otimes L)\to0$：$K_{r-p,0}$ 是它的核，故所求差等于该复形的 Euler 示性数减去 $g\binom{r+1}{p+1}$。
   - *为什么*：复形只有两项，核的维数等于右端项维数减去左端项维数，而左端项维数是 $g\dim\wedge^{r-p}H^0(L)=g\binom{r+1}{p+1}$。
3. 由 $\det M_L=L^{-1}$ 得 $\wedge^{r-p-1}M_L\otimes L\cong\wedge^{p+1}M_L^{\vee}$，又 $h^0(\wedge^{p+1}M_L)=K_{p+1,0}(C,L)=0$，故 $h^0(\wedge^{r-p-1}M_L\otimes K_C\otimes L)=h^1(\wedge^{p+1}M_L)=-\chi(\wedge^{p+1}M_L)$。
   - *为什么*：Serre 对偶把 $h^0(\wedge^{p+1}M_L^{\vee}\otimes K_C)$ 换成 $h^1(\wedge^{p+1}M_L)$；而 $q=0$ 时 $L^{-1}$ 无截面，故 $h^0(\wedge^{p+1}M_L)=0$。
4. $\deg(\wedge^{p+1}M_L)=\deg(M_L)\binom{r-1}{p}=-d\binom{r-1}{p}$，$\mathrm{rk}(\wedge^{p+1}M_L)=\binom{r}{p+1}$，Riemann–Roch 给 $-\chi(\wedge^{p+1}M_L)=d\binom{r-1}{p}+(g-1)\binom{r}{p+1}$。
   - *为什么*：外幂的次数是 $\deg(M_L)\cdot\binom{r-1}{p}$，秩是 $\binom{r}{p+1}$，再用 $\chi=\deg+\mathrm{rk}(1-g)$。
5. 代回得 $\dim K_{p,1}-\dim K_{p-1,2}=d\binom{r-1}{p}+(g-1)\binom{r}{p+1}-g\binom{r+1}{p+1}$；把 $r=d-g$ 代入并整理二项式恒等式，即得所述闭式。
   - *为什么*：非特殊给 $h^0(L)=d+1-g$，即 $r=d-g$；这一步是原文唯一的「将 $r$ 替换为 $d-g$」，漏掉它公式就与 $g$ 的形式不符。


出处：中译 p.36（定理 2.8，证明在中译 p.36–37）

## 易错点

- 别把 $r$ 当成 $d$：非特殊时 $r=d-g$，证明最后一步就是代换 $r\mapsto d-g$，漏掉会与闭式差整整一个 $g$。
- $p=d-g$ 之后公式右端为 $0$ 或负，不能读成「$K_{p,1}$ 的维数」；原文只声明 $1\le p\le r$，非消没结论只在 $p\le d-g$ 一侧。
- 特殊线丛要加 $K_{p-i,i+1}$ 的交错项（注 2.9），直接套定理 2.8 会漏掉 $\dim K_{p-2,3}$ 等项。
- 数值自检 $(g,d)=(5,10)$：$p=1$ 两边为 $5$，$p=2$ 为 $0$，$p=3$ 右端为 $-15/2$——出现分数说明已经越过 $d-g=5$ 分界。

## 相关卡

- [Koszul 对偶](../concepts/koszul-duality.md)
- [核丛](../concepts/kernel-bundle.md)
- [Brill–Noether 数 $\beta$](../concepts/brill-noether-number.md)

## 出处

- ch2 §2.4 Green 维数公式；中译 p.36（英文 PDF p.40），源码 `chapters/ch02.tex:248`
- ch2 §2.4 定理 2.8 的证明；中译 p.37（英文 PDF p.41），源码 `chapters/ch02.tex:279`
