# α-稳定凝聚系

> `grassmann/concept/alpha-stable-coherent-system` · 轨道 7 · α-稳定凝聚系 · 状态 draft

> **先自测**：α 变大时为什么更难稳定？稳定性的翻转点由什么决定？

## 一句话

凝聚系按 α-斜率 μ_α=d/n+αk/n 判稳；α 控制「截面多少算多」，稳定性只在有限个 α 区间内不变。

## 定义

设 $(E,V)$ 是 $C$ 上型为 $(n,d,k)$ 的凝聚系，$\alpha\in\mathbb{R}$。定义 $\alpha$-斜率 $$\mu_\alpha(E,V)=\frac{d}{n}+\alpha\frac{k}{n}.$$ 若对 $(E,V)$ 的每个真凝聚子系 $(F,W)$（$0<\operatorname{rk}F<\operatorname{rk}E$，$W\subseteq V\cap H^0(F)$）都有 $\mu_\alpha(F,W)<\mu_\alpha(E,V)$，称 $(E,V)$ 为 **$\alpha$-稳定**；把 $<$ 换成 $\le$ 得 **$\alpha$-半稳定**。

**记号约定**：$n,d,k$ 为型；$\mu_\alpha$ 是 $\mathbb{R}$-值的斜率函数；$\alpha$ 不是斜率参数而是「权重」。

## 要点（为什么需要它）

- $\alpha=0$ 时退回向量丛的斜率稳定性，$V$ 完全不参与判据。
- $\alpha>0$ 时 $k$ 越大 $\mu_\alpha$ 越大，越容易被 $(F,0)$ 判掉——所以「截面多」在 $\alpha>0$ 时是不利因素。
- $\alpha\le 0$ 且 $k\ge 1$ 时不存在稳定凝聚系：$(E,0)$ 的斜率不低于 $(E,V)$。
- 对固定 $(n,d,k)$，稳定性的变化只发生在有限多个 $\alpha$ 临界值上，区间内部模空间不变。

## 关键公式

$$
\mu_\alpha(E,V)=\frac{d}{n}+\alpha\frac{k}{n}
$$

$$
\mu_\alpha(F,W)<\mu_\alpha(E,V)\quad\text{对所有真子系}
$$

## 定理与证明（或缺口）

### Jordan–Hölder 滤过与 S-等价

每个 $\alpha$-半稳定凝聚系都有滤过 $0=(E_0,V_0)\subset\cdots\subset(E_m,V_m)=(E,V)$，各子商 $\alpha$-稳定且斜率相同；相伴分次对象 $\gr(E,V)$ 唯一，$(E,V)$ 与 $(E',V')$ S-等价当且仅当 $\gr$ 同构。

**证明状态：提纲（有缺口）**


> **缺口**：本章只陈述不证明：存在性用半稳定对象的有限性（Quot 有界）+ 斜率极大子系逐步剥离；唯一性用两个滤过的公共细分。完整证明见 Le Potier 或 King–Newstead。


出处：中译 p.116–117（§1，定义之后）

## 易错点

- 把 $\mu_\alpha$ 写成 $d/n+\alpha k$：第二项漏了除秩，比较不同秩子系时符号会翻。
- 判稳时只查 $(F,V\cap H^0(F))$，漏掉 $(F,0)$——$\alpha\le0$ 的反例正是被 $(E,0)$ 判掉的。
- 以为 $\alpha$ 连续变化时模空间也连续变化：实际在临界值处会发生 flip（本章 §3–§8 的主题）。

## 相关卡

- [凝聚系](../concepts/coherent-system.md)
- [Jordan–Hölder 滤过与 S-等价](../concepts/jordan-holder-filtration.md)

## 出处

- ch7 §1 定义（定义 1.2）；中译 p.116（英文 PDF p.130），源码 `chapters/ch07.tex:27`
