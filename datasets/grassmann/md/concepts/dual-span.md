# 对偶张成

> `grassmann/concept/dual-span` · 轨道 7 · α-稳定凝聚系 · 状态 draft

> **先自测**：为什么对偶张成能把秩 $n$ 的问题变成秩 $k-n$ 的问题？

## 一句话

把 $(E,V)$ 换成 $(D_V(E),V')$，其中 $D_V(E)^*$ 是求值映射 $V\otimes\mathcal{O}\to E$ 的核；这个对合运算把高秩问题化归为线丛问题，是 §6 处理 $k=n+1$ 的主力工具。

## 定义

设 $(E,V)$ 是凝聚系。定义**对偶张成** $D(E,V)=(D_V(E),V')$，其中 $D_V(E)^*$ 是求值映射 $V\otimes\mathcal{O}\to E$ 的核，$V'$ 是 $V^*$ 在 $H^0(D_V(E))$ 中的像。当 $(E,V)$ 生成且 $H^0(E^*)=0$ 时，有对偶正合列 $0\to D_V(E)^*\to V\otimes\mathcal{O}\to E\to0$ 与 $0\to E^*\to V^*\otimes\mathcal{O}\to D_V(E)\to0$，且 $D(D(E,V))=(E,V)$。由此 $D_V(E)$ 的秩为 $k-n$、次数为 $d$。

**记号约定**：$D_V(E)^*$ 为求值映射的核（与核丛同一构造，只是用 $V$ 替代 $H^0(E)$）。

## 要点（为什么需要它）

- $D_V(E)^*=\ker(V\otimes\mathcal{O}\to E)$ 与核丛 $M_L=\ker(H^0(L)\otimes\mathcal{O}\to L)$ 是同一构造；区别是用 $k$ 维的 $V$ 代替整个 $H^0(E)$。
- 由正合列算次数：$0=\deg(D_V(E)^*)+d$，故 $\deg D_V(E)=d$；秩由 $0\to D_V(E)^*\to V\otimes\mathcal{O}\to E\to0$ 得 $k-n$。
- $k=n+1$ 时 $D_V(E)$ 是秩 $1$、次数 $d$ 的层，于是 $G_L(n,d,n+1)$ 双有理于 $G(1,d,n+1)=G^n_d$（定理 6.2）。
- 稳定性在 $D$ 下保持：引理 6.1 说对大 $\alpha$，$D(L,V)$ 是 $\alpha$-稳定的；这是 §6 能用线丛的经典 Brill–Noether 理论反推高秩结论的原因。

## 关键公式

$$
D(E,V)=(D_V(E),V'),\qquad D_V(E)^*=\ker(V\otimes\mathcal{O}\to E)
$$

$$
0\to D_V(E)^*\to V\otimes\mathcal{O}\to E\to0
$$

$$
0\to E^*\to V^*\otimes\mathcal{O}\to D_V(E)\to0
$$

## 定理与证明（或缺口）

### 引理 6.1（对偶张成的稳定性）

设 $C$ 是 Petri 曲线，$(L,V)$ 是生成凝聚系，$\dim V=n+1$。则对大 $\alpha$，$D(L,V)$ 是 $\alpha$-稳定的。

**证明状态：提纲（有缺口）**


> **缺口**：原文只引 [12] 的细节，没有写出证明。缺的是对 $D(L,V)$ 的每个真凝聚子系验证 $\mu_\alpha$ 不等式：用两条对偶正合列把子系的斜率翻译成 $L$ 上子空间的斜率，再用 $\alpha$ 足够大时 $\alpha$ 项占优来结论。


出处：中译 p.121（引理 6.1）

### 定理 6.2（$k=n+1$ 的双有理化）

设 $C$ 是 Petri 曲线，$L$ 次数 $d>0$，$(L,V)$ 生成且 $\dim V=n+1$。则 $G_L(n,d,n+1)$ 双有理于 $G(1,d,n+1)=G^n_d$。

**证明状态：只引出处，原书不重证**


出处：中译 p.121（定理 6.2）

## 易错点

- 把 $D_V(E)^*$ 写成 $D_V(E)$：星号是核丛本身，$D_V(E)$ 是它的对偶，两者的秩与次数都差一个符号。
- 以为 $D$ 总是秩 $k-n$：这需要 $(E,V)$ 生成且 $H^0(E^*)=0$，否则求值映射不满射，正合列右端要加余核。
- 把对偶张成与 Serre 对偶混为一谈：$D$ 是「用 $V$ 重写 $E$」的初等变换，与 $K_X$ 无关；Serre 对偶是另一套操作。

## 相关卡

- [模型定理](../concepts/model-theorem.md)
- [Petri 映射](../concepts/petri-map.md)
- [核丛](../concepts/kernel-bundle.md)
- [大 $\alpha$ 下不半稳定的例子（例 5.3）](../examples/example-non-stability-large-alpha.md)

## 出处

- ch7 §3 对偶张成；中译 p.120（英文 PDF p.134），源码 `chapters/ch07.tex:212`
- ch7 §6 引理 6.1；中译 p.121（英文 PDF p.135），源码 `chapters/ch07.tex:294`
