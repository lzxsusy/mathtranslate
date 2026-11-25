# 大 $\alpha$ 下不半稳定的例子（例 5.3）

> `grassmann/example/example-non-stability-large-alpha` · 轨道 7 · α-稳定凝聚系 · 状态 draft

> **这张卡练什么**：为什么 $k$ 偏大时，把稳定性参数 $\alpha$ 调大反而使半稳定性必然失败？

## 一句话

例 5.3 指出：$k$ 落在 $n+\frac{1}{g}(d-n)$ 与 $\frac{ng}{g-1}$ 之间时，任何凝聚系对大 $\alpha$ 都不半稳定；而这个区间又确由型 $(rg-r+1,2rg-2r+3,rg+1)$ 的稳定例子取到。

## 背景定义

例 5.3 给出参数区间（式 (3)）$n+\frac{1}{g}(d-n)<k<\frac{ng}{g-1}$：落在其中的任何型 $(n,d,k)$ 的凝聚系对大 $\alpha$ 都不 $\alpha$-半稳定；例子同时给出该区间非空的构造，型为 $(rg-r+1,2rg-2r+3,rg+1)$ 且 $E$ 稳定。

## 设定

设 $C$ 是亏格 $g\ge2$ 的光滑射影曲线，$(E,V)$ 是型 $(n,d,k)$ 的凝聚系，$\alpha$-斜率 $\mu_\alpha(E,V)=\frac{d}{n}+\alpha\frac{k}{n}$。大 $\alpha$ 时 $\mu_\alpha$ 由 $\frac{k}{n}$ 主导，因此「$V$ 太大」会直接破坏半稳定性——这正是式 (3) 区间的含义：$k>n+\frac{1}{g}(d-n)$ 说明 $h^0$ 相对次数偏高，$k<\frac{ng}{g-1}$ 说明还没高到不可能存在。

## 计算

取 $n=r(g-1)+1$、$k=rg+1$、$d=2n+1=2rg-2r+3$（$3\le r\le g-1$）。左不等式：$n+\frac{d-n}{g}=rg-r+1+\frac{rg-r+2}{g}$，与 $k=rg+1$ 相差 $\frac{r-2}{g}>0$（因 $r\ge3$），故式 (3) 左端成立；右不等式：$\frac{ng}{g-1}=rg+\frac{g}{g-1}>rg+1=k$，恒成立。数值核验取 $g=5$、$r=3$：$n=13$、$k=16$、$d=27$，左端 $13+\frac{27-13}{5}=15.8<16$，右端 $16<\frac{13\cdot5}{4}=16.25$，两边都紧。于是由例 5.3 的前半，这对 $(E,V)$ 对大 $\alpha$ 不半稳定；而同一个例子断言存在型 $(rg-r+1,2rg-2r+3,rg+1)$、$E$ 稳定的 $(E,V)$（$C$ 非超椭圆时），即区间非空且与「$E$ 稳定」并不冲突。

## 要点

- 式 (3) 是「大 $\alpha$ 必不半稳定」的区域，方向与 §4/§5 的存在性条件式 (1)(2) 相反：后者要求 $k$ 不太大，前者描述 $k$ 太大时会发生什么。
- 机制是斜率的 $\alpha$ 项：$\mu_\alpha=\frac{d}{n}+\alpha\frac{k}{n}$，$k/n$ 越大的子系在大 $\alpha$ 时越占优，于是 $(E,V)$ 自己被真子系压过。
- $E$ 稳定与 $(E,V)$ 半稳定是两件事：例 5.3 后半构造的 $(E,V)$ 满足 $E$ 稳定，但仍落在式 (3) 区间内，故对大 $\alpha$ 不半稳定。
- 参数代入后 $r>2$ 是唯一实质条件：左端差恰为 $\frac{r-2}{g}$，$r=2$ 时不等式退化，$r=1$ 时反向；右端则对一切 $g>1$ 自动成立。

## 关键公式

$$
n+\frac{1}{g}(d-n)<k<\frac{ng}{g-1}
$$

$$
\mu_\alpha(E,V)=\frac{d}{n}+\alpha\frac{k}{n}
$$

$$
rg+1-\left[n+\frac{d-n}{g}\right]=\frac{r-2}{g}
$$

## 相关定理

- **例 5.3（大 $\alpha$ 下的不半稳定性）**：设 $(E,V)$ 是型 $(n,d,k)$ 的凝聚系，满足式 (3) $n+\frac{1}{g}(d-n)<k<\frac{ng}{g-1}$。则对大 $\alpha$，$(E,V)$ 不是 $\alpha$-半稳定的。
- **例 5.3 后半（区间非空）**：设 $C$ 非超椭圆、$3\le r\le g-1$。则存在型 $(rg-r+1,\ 2rg-2r+3,\ rg+1)$、$E$ 稳定的 $(E,V)$，且该型满足式 (3)。
- **式 (3) 在 $n=r(g-1)+1$ 时的算术核验**：取 $n=r(g-1)+1$、$k=rg+1$、$d=2n+1$。则式 (3) 左端等价于 $r>2$，右端对一切 $g>1$ 恒成立。

## 易错点

- 把式 (3) 当存在性判据：它是「大 $\alpha$ 必不半稳定」的禁区，与定理 4.1 的式 (2)（$k\le n+\frac{1}{g}(d-n)$）方向相反。
- 漏掉 $3\le r$：$r=2$ 时左端差为 $0$，不等式退化成等式，构造不出严格不半稳定的例子。
- 以为 $E$ 稳定就自动有 $(E,V)$ 半稳定：例 5.3 后半的 $(E,V)$ 正是 $E$ 稳定但 $(E,V)$ 对大 $\alpha$ 不半稳定的情形。
- 把「大 $\alpha$」当成「任意 $\alpha$」：结论只对充分大的 $\alpha$ 成立，当 $\alpha$ 小到使 $d/n$ 项占优时稳定性可能恢复。

## 用到哪些概念

- [α-稳定凝聚系](../concepts/alpha-stable-coherent-system.md)
- [模型定理](../concepts/model-theorem.md)
- [$d_0$ 与存在域 $U(n,d,k)$](../concepts/existence-region-d0.md)

## 相关卡

- [α-稳定凝聚系](../concepts/alpha-stable-coherent-system.md)
- [模型定理](../concepts/model-theorem.md)
- [$d_0$ 与存在域 $U(n,d,k)$](../concepts/existence-region-d0.md)
- [$g=10$、$(2,12,4)$ 的 $d_0$（例 7.5）](../examples/example-genus-10-d0.md)
- [性质 (N_p)](../concepts/property-np.md)

## 出处

- ch7 §5 例 5.3（大 $\alpha$ 下不半稳定）；中译 p.122（英文 PDF p.136），源码 `chapters/ch07.tex:281`
