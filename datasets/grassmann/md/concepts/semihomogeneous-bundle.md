# 半齐次向量丛

> `grassmann/concept/semihomogeneous-bundle` · 轨道 8 · 阿贝尔簇上的正则性 · 状态 draft

> **先自测**：为什么半齐次丛在同源拉回下会变成线丛的直和，从而让 $m$-$\Theta$-正则性退化成可检验的 $IT_0$ 消没？

## 一句话

沿平移只差一个 $\operatorname{Pic}^0$ 扭动的向量丛叫半齐次丛；Mukai 的分解与 Jordan–Hölder 定理把它化成若干个同 $\delta$ 的单半齐次丛，从而使 $m$-$\Theta$-正则性可算。

## 定义

设 $X$ 是阿贝尔簇。$X$ 上的向量丛 $E$ 称**半齐次**，如果对每个 $x\in X$，存在 $\alpha\in\operatorname{Pic}^0(X)$ 使 $$t_x^*E\cong E\otimes\alpha,$$ 其中 $t_x$ 是平移 $y\mapsto y+x$。等价地：对每个 $x$，$t_x^*E$ 与 $E$ 只差一个次数零的线丛因子。

**记号约定**：$t_x\colon X\to X$ 是平移；$\delta(E)=[c_1(E)/\operatorname{rk}E]\in NS(X)\otimes\mathbb Q$ 是约化斜率；『单』指 $\operatorname{End}(E)=k$（自同态只有标量）。

## 要点（为什么需要它）

- Mukai：半齐次丛是 Gieseker 半稳定的（单的实为稳定），并且有强意义的 Jordan–Hölder 滤过——各因子是同构的单半齐次丛。
- 命题 7.26：$E\cong\bigoplus E_i$，每个 $E_i$ 有滤过，其因子全同构于 $F_i$，而各 $F_i$ 是同一个 $\delta\in NS(X)\otimes\mathbb Q$ 的单半齐次丛。
- 引理 7.27 是『拆成线丛』的关键：(1) 存在同源 $\pi\colon Y\to X$ 与线丛 $M$ 使 $\pi^*E\cong\bigoplus_rM$；(2) 存在同源 $\varphi\colon Z\to X$ 与线丛 $L$ 使 $\varphi_*L=E$。
- 引理 7.28：非退化（$\chi(E)\ne0$）单半齐次丛恰有一个上同调群非零；引理 7.29：半齐次 $E$ 是 $m$-$\Theta$-正则的 $\iff E((m-1)\Theta)$ 满足 $IT_0$。
- 这正对上 ch7、ch9 的稳定性话题：本章用半齐次性 + Jordan–Hölder 归约代替 Harder–Narasimhan，与 α-稳定凝聚系那条路互为参照。

## 关键公式

$$
t_x^*E\cong E\otimes\alpha,\qquad \alpha\in\operatorname{Pic}^0(X)
$$

$$
\pi^*E\cong M^{\oplus r},\qquad \varphi_*L\cong E
$$

$$
c_1(\widehat E(-\Theta))=-\operatorname{PD}_{2g-2}\bigl(\operatorname{ch}_{g-1}(E(-\Theta))\bigr),\qquad \operatorname{rk}\widehat E(-\Theta)=h^0(E(-\Theta))=\frac{c_1(E(-\Theta))^g}{r^{g-1}g!}
$$

## 定理与证明（或缺口）

### 命题 7.26（半齐次丛的分解与 Jordan–Hölder 滤过）

设 $E$ 是 $X$ 上的半齐次向量丛。则 $E\cong\bigoplus E_i$，每个 $E_i$ 带一个滤过，其因子全部同构于 $F_i$，其中 $F_i$ 是同一个 $\delta\in NS(X)\otimes\mathbb Q$ 的单半齐次丛。

**证明状态：只引出处，原书不重证**


出处：中译 p.154，命题 7.26，出自 [Muk3] Prop 6.18（章内未重证）

### 引理 7.29（半齐次丛的 $m$-$\Theta$-正则性即 $IT_0$）

设 $E$ 是 $X$ 上的半齐次向量丛、$\Theta$ 是主极化，则 $E$ 是 $m$-$\Theta$-正则的当且仅当 $E((m-1)\Theta)$ 满足 $IT_0$。

**证明状态：完整**

1. 由引理 7.27(1) 取同源 $\pi\colon Y\to X$ 使 $\pi^*E\cong\bigoplus_rM$；$M$-正则性与 $IT_0$ 都在有限同源拉回下保持（支集轨迹的原像维数不变），故可逐线丛判断。
   - *为什么*：$E$ 的 $V^i$ 与 $\pi^*E$ 的 $V^i$ 只差 $\pi^*$ 的有限纤维，维数不变。
2. 对线丛 $M$，$\dim V^i(M)\le g-i-1$ 与 $V^i(M)=\varnothing$ 等价：Mumford 指数定理说 $h^i(M\otimes\beta)$ 在 $\operatorname{Pic}^0$ 的连通分支上为常数，故 $V^i(M)$ 是若干分支的并，而分支维数只能是 $0$ 或 $g$。
   - *为什么*：线丛的支集轨迹没有中间维数，所以严格余维条件退化成空集。
3. 把两条合起来：$E((m-1)\Theta)$ 是 $M$-正则的 $\iff$ 其同源拉回是线丛直和且每个直和项 $IT_0$ $\iff E((m-1)\Theta)$ 满足 $IT_0$。
   - *为什么*：直和项逐项 $IT_0$ 等价于整体 $IT_0$，而同源拉回不改变 $IT_0$。


出处：中译 p.154，引理 7.28 与引理 7.29（chapters/ch08.tex:798 起的 §7.3）

## 易错点

- 中译 p.154 把『单的半齐次丛』解释成『没有非平凡自同构的』，这是错的：标量自同构 $c\cdot\operatorname{id}$ 永远存在。单指 $\operatorname{End}(E)=k$，即自同态只有标量；英文原书同样错，命题 7.26 与引理 7.27 用的正是后者。
- 别把半齐次理解成『平移下不变』：$t_x^*E\cong E\otimes\alpha$ 里的 $\alpha$ 一般依赖 $x$，只有 $\delta(E)$ 是不变量；$\alpha$ 那部分正是 $\operatorname{Pic}^0$ 的自由度。
- 命题 7.26 的分解不是把 $E$ 直接拆成单丛的直和，而是『直和 + 每个直和项的滤过』；滤过因子才是单半齐次丛，且所有 $F_i$ 共享同一个 $\delta$。

## 相关卡

- [$m$-$\Theta$-正则性](../concepts/m-theta-regular.md)
- [Jordan–Hölder 滤过与 S-等价](../concepts/jordan-holder-filtration.md)
- [α-稳定凝聚系](../concepts/alpha-stable-coherent-system.md)
- [Picard 丛](../concepts/picard-bundle.md)

## 出处

- ch8 §7.3 半齐次向量丛（定义 7.25）；中译 p.154（英文 PDF p.170），源码 `chapters/ch08.tex:798`
