---
id: dmod/concept/d-module-on-projective-space
type: concept
track: C
---

# 射影空间上的 $D$-模

> 用 $k^*$-纤维化 $\pi:Y^*\to P^n$ 与 Euler 算子 $E$，把射影空间上的模拉回到 $k^{n+1}-\{0\}$ 上按 $E$-特征值分解，证明 $\Gamma$ 与 $\Delta$ 仍互逆。

**问题**：射影空间非仿射，为什么整体截面函子 $\Gamma$ 仍与局部化 $\Delta$ 互逆，$k^*$-作用在其中起什么作用？

## 定义

设 $X=P^n$，$Y=k^{n+1}$，$Y^*=Y-\{0\}$，$\pi:Y^*\to X$ 是自然的 $k^*$-纤维化。对 $\mathcal D_X$-模 $V$ 记 $\pi^+V=\mathcal D_{Y^*}\otimes_{\pi^{-1}\mathcal D_X}\pi^{-1}V$ 为其拉回。Euler 算子 $E=\sum_{i=0}^ny_i\partial/\partial y_i$ 满足 $[E,y_i]=y_i$、$[E,\partial/\partial y_i]=-\partial/\partial y_i$，故 $\Gamma(Y^*,\pi^+V)$ 分解为 $E$-特征空间直和 $\bigoplus_{p\in\mathbb Z}\Gamma(Y^*,\pi^+V)_{(p)}$；整体截面与 $(0)$-特征空间通过 $\gamma:\Gamma(X,V)\cong\Gamma(Y^*,\pi^+V)_{(0)}$ 等同。

*记号*：$X=P^n$；$Y=k^{n+1}$；$Y^*=Y-\{0\}$；$\pi:Y^*\to X$；$E=\sum_iy_i\partial/\partial y_i$；$\pi^+V$：$\mathcal D_{Y^*}$-模拉回。

## 要点

- 引理 5.1：$\pi:Y^*\to X$ 是以 $k^*$ 为纤维的局部平凡纤维化，故 $\pi^+$ 有显式的纤维描述。
- 引理 5.2：$\pi^+$ 是正合函子——这是下面所有上同调计算的起点。
- 引理 5.4：$\Gamma(Y^*,\pi^+V)=\bigoplus_{p\in\mathbb Z}\Gamma(Y^*,\pi^+V)_{(p)}$ 按 $E$-特征值分解；引理 5.5：$\gamma$ 是到 $(0)$-特征空间的同构。
- 定理 5.8：$H^p(P^n,V)=0$ 对 $p>0$；引理 5.10：$\Gamma(X,V)=0\Rightarrow V=0$。
- 定理 5.12：$\Gamma:\mathcal M_{qc}(\mathcal D_{P^n})\to\mathcal M(D_{P^n})$ 是范畴等价，拟逆为 $\Delta$；推论 5.13：$P^n$ 上拟凝聚 $\mathcal D_X$-模由整体截面生成。

## 关键公式

- $E=\sum_{i=0}^ny_i\frac{\partial}{\partial y_i},\qquad [E,y_i]=y_i,\quad [E,\partial/\partial y_i]=-\partial/\partial y_i$
- $\Gamma(Y^*,\pi^+V)=\bigoplus_{p\in\mathbb Z}\Gamma(Y^*,\pi^+V)_{(p)}$
- $\gamma:\Gamma(X,V)\cong\Gamma(Y^*,\pi^+V)_{(0)}$
- $H^p(P^n,V)=0\quad(p>0)$

## 定理与证明

### 定理 5.8（射影空间上拟凝聚模的高阶上同调消失）（完整）

设 $V$ 是 $P^n$ 上拟凝聚 $\mathcal D_X$-模。则对 $p>0$ 有 $H^p(P^n,V)=0$。

1. 取 $V$ 在 $\mathcal M_{qc}(\mathcal D_X)$ 中的入射右分解 $I^\bullet$（命题 4.3 保证拟凝聚模有充足入射），则 $H^p(P^n,V)=H^p(\Gamma(X,I^\bullet))$。  
   *为什么*：上同调按定义就是入射消解取整体截面后的同调，且比其局部数据。
2. 入射拟凝聚 $\mathcal D_X$-模对 $\Gamma$ 无环：由引理 5.7 及随后 595-597 的论证，$\Gamma(Y,K)_{(0)}=0$，用 $0\to V_1\to V_2\to V_3\to0$ 与特征空间的分解得 $0\to\Gamma(X,V_1)\to\Gamma(X,V_2)\to\Gamma(X,V_3)\to0$ 正合。  
   *为什么*：$\Gamma$ 的正合性使它能直接作用在消解上而不改变同调。
3. 于是 $H^p(\Gamma(X,I^\bullet))=0$ 对 $p>0$，即 $H^p(P^n,V)=0$。  
   *为什么*：正合函子作用在消解上给出同调为零的复形，即所需消失。

*出处*：定理 5.8 / chap3.tex:599-605

### 定理 5.12（射影空间上的 Serre 型等价）（要点（有缺口））

设 $X=P^n$。则 $\Gamma:\mathcal M_{qc}(\mathcal D_X)\to\mathcal M(D_X)$ 是范畴等价，其拟逆为 $\Delta$。

1. 定理 5.8 与引理 5.10 给出 $\Gamma$ 的正合性与保守性（$\Gamma(X,V)=0\Rightarrow V=0$），故 $\Gamma$ 是忠实且反映同构的。  
   *为什么*：保守性把「图追踪中的零性」提升为「模的零性」，这是等价判据的关键一步。
2. 引理 5.9 与引理 5.11 分别给出 $\lambda:V\to\Gamma(X,\Delta(V))$ 与 $\mu:\Delta(\Gamma(X,V))\to V$ 的同构，故 $\Gamma$ 与 $\Delta$ 互为拟逆。  
   *为什么*：两个自然变换都是同构，按定义即范畴等价的拟逆关系。

> 缺口：讲义在 chap3.tex:607-652 用引理 5.9（$\lambda$ 同构）、引理 5.10（$\Gamma$-保守）、引理 5.11（$\mu$ 同构）三步完成证明；本卡合并为两条主线。

*出处*：定理 5.12 / chap3.tex:650-652


## 易错点

- $(0)$-特征空间的下标不能省：$\Gamma(Y^*,\pi^+V)$ 含有全部整数特征值，只有 $(0)$ 部分才同构于 $\Gamma(X,V)$。
- 定理 1.1（仿射情形）不能直接搬到 $P^n$：仿射性只提供 $\Gamma\circ\Delta$ 的一侧，射影情形需要定理 5.8 的上同调消失补齐另一侧。
- $H^p=0$（$p>0$）只对拟凝聚 $\mathcal D_X$-模成立；对一般 $\mathcal O_X$-模或非拟凝聚情形不能照搬。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本，第 III 章 §5 射影空间上的 $D$-模，p.90（PDF p.96），`源码/chapters/chap3.tex:545-605（引理 5.4、5.5 与定理 5.8）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本，第 III 章 §5 射影空间上的 $D$-模，p.95（PDF p.101），`源码/chapters/chap3.tex:624-652（引理 5.10、定理 5.12）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/quasi-coherent-d-module`
- `dmod/concept/coherent-d-module`
- `dmod/concept/coherator`
- `dmod/example/example-d-module-on-projective-space`
