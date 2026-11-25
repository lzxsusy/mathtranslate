# 凝聚系

> `grassmann/concept/coherent-system` · 轨道 7 · α-稳定凝聚系 · 状态 draft

> **先自测**：为什么模空间要模 (E,V) 而不只模 E？V 的大小如何改变几何？

## 一句话

曲线上「向量丛连同其截面空间的一个子空间」组成的对，是经典线性系在高秩情形的推广；稳定性与模空间都定义在它上面。

## 定义

设 $C$ 是光滑射影曲线。$C$ 上型为 $(n,d,k)$ 的**凝聚系**是一对 $(E,V)$：$E$ 是秩 $n$、次数 $d$ 的向量丛，$V\subseteq H^0(E)$ 是 $k$ 维线性子空间。**凝聚子系**是一对 $(F,W)$，$F\subseteq E$ 是子丛，$W\subseteq V\cap H^0(F)$。若典范映射 $V\otimes\mathcal{O}_C\to E$ 满射（余核为挠层），称 $(E,V)$ **生成**；只要求在一般点满射则称**一般生成**。

**记号约定**：$n=\operatorname{rk}E$，$d=\deg E$，$k=\dim V$；$H^0(E)$ 为整体截面空间。

## 要点（为什么需要它）

- $V$ 是数据的一部分，不是 $E$ 的函数：同一个 $E$ 配不同的 $V$ 得到不同的凝聚系和不同的稳定性。
- $W$ 只要求含于 $V\cap H^0(F)$，可以取 $0$——取 $W=0$ 的子系在判稳时经常是决定性的。
- $k=1$ 时凝聚系就是「带一个截面的丛」，与经典线性系 $|V|$ 的直观对应。
- 生成的凝聚系才有到射影空间的映射：$V\otimes\mathcal{O}\twoheadrightarrow E$ 给出 $\mathbb{P}(V^*)$ 上的框架，这是几何侧的入口。

## 关键公式

$$
(E,V),\quad V\subseteq H^0(E),\ \dim V=k
$$

$$
V\otimes\mathcal{O}_C\longrightarrow E\longrightarrow 0\quad(\text{生成})
$$

## 定理与证明（或缺口）

### 凝聚系模空间的存在性

对固定的 $(n,d,k)$ 与使 $\alpha$-稳定性非空的 $\alpha$，$\alpha$-稳定凝聚系的模空间 $G(\alpha;n,d,k)$ 存在，且是拟射影簇。

**证明状态：只引出处，原书不重证**


出处：中译 p.117（§1 末，引 \cite{ch07:29, ch07:36, ch07:43, ch07:17}）

## 易错点

- 把凝聚系当成「$E$ 加上 $V=H^0(E)$」的特例：这样 $k=h^0(E)$ 会随 $E$ 跳动，模空间就不存在了，$k$ 必须固定。
- 写子系时要求 $W=V\cap H^0(F)$（等号）：定义里是包含，等号只是判稳时最不利的那个选择。

## 相关卡

- [α-稳定凝聚系](../concepts/alpha-stable-coherent-system.md)
- [Jordan–Hölder 滤过与 S-等价](../concepts/jordan-holder-filtration.md)

## 出处

- ch7 §1 定义；中译 p.116（英文 PDF p.130），源码 `chapters/ch07.tex:18`
