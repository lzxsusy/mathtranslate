# 格罗嫩沃尔德–范霍夫定理（Groenewold–Van Hove）

> `geoq/concept/groenewold-van-hove` · 轨道 D · 几何量子化机器 · 状态 draft

> **先自测**：为什么「满足 Q2 与 Q4、且在低次多项式上取标准值」这两件事在四次多项式上就打架？矛盾具体出在哪个恒等式？

## 一句话

不存在把四次以下多项式都变成自伴算子、保单位、在低次上与标准实现一致、又满足括号关系的映射。证明把 $x^2p^2$ 写成两种泊松括号，两条路给出的算子相差 $\hbar^2/3$。

## 定义

这是量子化的不可行（no-go）型结果：狄拉克原理的 Q2 与 Q4 并不像看起来那样温和，只要再加上「低次多项式取标准实现」这一条，它们在四次多项式范围内就自相矛盾，因此必须放弃其中一条。定理的定义域取 $\mathbb{R}^{2n}$ 上的多项式空间 $P^{\le k}=\{f\in\mathbb{R}[x^i,p_i]\mid\deg f\le k\}$，并要求 $Q$ 在 $P^{\le1}$ 上与薛定谔表示一致：$Q(1)=\mathbf{1}$，$Q(x^i)=x^i$，$Q(p_i)=-i\hbar\partial_{x^i}$。

**记号约定**：$P^{\le k}$：次数不超过 $k$ 的实多项式空间；$\mathcal{W}_\hbar$：外尔量子化；$\hat x^i=x^i$，$\hat p_i=-i\hbar\partial_{x^i}$；$[f,g]_*$：Moyal 交换子；$\Lambda=\overleftarrow{\partial_{x^i}}\overrightarrow{\partial_{p_i}}-\overleftarrow{\partial_{p_i}}\overrightarrow{\partial_{x^i}}$ 是作用在两个因子上的双微分算子。

## 要点

- 定理只用到 Q2、Q4 与「低次取标准值」，完全没有用到 Q5：障碍来自括号关系本身，不是来自「要求不可约」。
- 证明是逐步升级的：先证 $P^{\le2}$ 上 $Q=\mathcal{W}_\hbar$，再证 $P^{\le3}$ 上同样，最后在 $x^2p^2$ 处让两种括号写法相撞。
- 每一步升级的关键引理是：若 $Q(f)-\mathcal{W}_\hbar(f)$ 与 $\hat x,\hat p$ 全部对易，则它是常数倍恒等算子（与 $\hat x$ 对易杀掉导数项，再与 $\hat p$ 对易杀掉非常数系数）。
- 常数被逐个消灭靠的是把 $f$ 写成泊松括号，例如 $x^2=\frac12\{x^2,xp\}$：Q4 把括号变成交换子，而常数在交换子里消失。
- 矛盾的量级是 $\hbar^2$（两侧相差 $\hbar^2/3$），不是可以靠 $\hbar\to0$ 忽略的高阶小量：定理对每个固定的 $\hbar\ne0$ 都成立。

## 关键公式

$$
$P^{\le k}=\{f\in\mathbb{R}[x^i,p_i]\mid\deg f\le k\}$
$$

$$
$[\hat x^i,\hat p_j]=i\hbar\delta^i_j$
$$

$$
$x^2p^2=\frac19\{x^3,p^3\}=\frac13\{x^2p,xp^2\}$
$$

$$
$[x^3,p^3]_*=9i\hbar\,x^2p^2+\frac32(i\hbar)^3$
$$

$$
$[x^2p,xp^2]_*=3i\hbar\,x^2p^2-\frac12(i\hbar)^3$
$$

## 定理与证明

### 定理 5.4.1（Groenewold）

不存在 $\mathbb{R}$-线性映射 $Q:P^{\le4}\to L^2(\mathbb{R}^n)$ 上的自伴算子，使得 (1) $Q(1)=1$，$Q(x^i)=\hat x^i$，$Q(p_i)=\hat p_i$；(2) $[Q(f),Q(g)]=i\hbar Q(\{f,g\})$ 对一切 $f,g\in P^{\le4}$ 成立。

**完整证明**

1. 反设这样的 $Q$ 存在。条件 (1) 与对称序一致，故 $f\in P^{\le1}$ 上 $Q(f)=\mathcal{W}_\hbar(f)$。取 $f\in P^{\le2}$、$g\in P^{\le1}$：此时 $\{f,g\}\in P^{\le1}$，且 Moyal 修正项 $\Lambda^3(fg)$ 需要总次数 $\ge6$ 而这里至多 $3$，故 $[\mathcal{W}_\hbar(f),\mathcal{W}_\hbar(g)]=i\hbar\mathcal{W}_\hbar(\{f,g\})$。于是 $[Q(f),\hat g]=i\hbar Q(\{f,g\})=i\hbar\widehat{\{f,g\}}=[\mathcal{W}_\hbar(f),\hat g]$，即 $R_f:=Q(f)-\mathcal{W}_\hbar(f)$ 与全部 $\hat x^i,\hat p_i$ 对易。
   - *为什么*：中间一步用的是 $Q$ 在 $P^{\le1}$ 上与 $\mathcal{W}_\hbar$ 相等，这正是条件 (1) 的内容。
2. 与全部 $\hat x^i$ 对易的算子不能含导数项，故 $R_f$ 是乘一个函数；再与 $\hat p_i=-i\hbar\partial_{x^i}$ 对易迫使该函数为常数。于是 $Q(f)=\mathcal{W}_\hbar(f)+c_f\mathbf{1}$，$f\in P^{\le2}$。
   - *为什么*：等价说法是 $\hat x,\hat p$ 的作用不可约（斯通–冯·诺依曼定理加 Schur 引理），这里用初等版本便于核对。
3. 常数在交换子里消失，所以这一步不必知道 $c_f$ 的值：由 $x^2=\frac12\{x^2,xp\}$ 与 Q4，$Q(x^2)=\frac{1}{2i\hbar}[Q(x^2),Q(xp)]=\frac{1}{2i\hbar}[\mathcal{W}_\hbar(x^2)+c_1,\mathcal{W}_\hbar(xp)+c_2]=\frac{1}{2i\hbar}[\mathcal{W}_\hbar(x^2),\mathcal{W}_\hbar(xp)]=\mathcal{W}_\hbar(x^2)$，末步用 $[x^2,xp]_*=2i\hbar\,x^2$；同理 $Q(p^2)=\mathcal{W}_\hbar(p^2)$、$Q(xp)=\mathcal{W}_\hbar(xp)$。
   - *为什么*：把函数写成括号，常数项自动被交换子杀掉，这是整段论证的关键技巧。
4. 升到三次：$\{P^{\le3},P^{\le1}\}\subset P^{\le2}$，总次数 $4<6$ 保证修正项仍为零，重复前两步得 $Q(f)=\mathcal{W}_\hbar(f)+c_f\mathbf 1$（$f\in P^{\le3}$）；再用 $x^3=\frac13\{x^3,xp\}$、$p^3=\frac13\{xp,p^3\}$、$x^2p=\frac16\{x^3,p^2\}$、$xp^2=\frac16\{x^2,p^3\}$ 逐个消灭常数。
   - *为什么*：每步都要求 $\{f,g\}$ 落在已解决的次数层；四个恒等式各管一个三次单项式，凑齐 $P^{\le3}$ 的基。
5. 在 $P^{\le4}$ 上出现矛盾。两条路线都算 $Q(x^2p^2)$：由 $\{x^3,p^3\}=9x^2p^2$ 与 $[x^3,p^3]_*=9i\hbar\,x^2p^2+\frac32(i\hbar)^3$，得 $Q(x^2p^2)=\frac{1}{9i\hbar}[\mathcal{W}_\hbar(x^3),\mathcal{W}_\hbar(p^3)]=\frac{1}{9i\hbar}\mathcal{W}_\hbar([x^3,p^3]_*)=\mathcal{W}_\hbar(x^2p^2)-\frac16\hbar^2$；由 $\{x^2p,xp^2\}=3x^2p^2$ 与 $[x^2p,xp^2]_*=3i\hbar\,x^2p^2-\frac12(i\hbar)^3$ 同法得 $Q(x^2p^2)=\mathcal{W}_\hbar(x^2p^2)+\frac16\hbar^2$。两者相差 $\frac13\hbar^2\ne0$，矛盾。
   - *为什么*：两个系数分别是 $\frac{1}{9i\hbar}\cdot\frac32i^3\hbar^3=-\frac16\hbar^2$ 与 $\frac{1}{3i\hbar}\cdot(-\frac12i^3\hbar^3)=+\frac16\hbar^2$，符号相反正是障碍所在。

来源：ch05b.tex:686-815（原书 p.282–284）

### 推论：不存在满足 Q1–Q4 的量子化

设 $n\ge1$、$\hbar\ne0$。不存在 $\mathbb{R}$-线性映射 $Q:C^\infty(\mathbb{R}^{2n})\to$ 算子，使得它在 $P^{\le1}$ 上取标准值（$Q(1)=1$，$Q(x^i)=\hat x^i$，$Q(p_i)=\hat p_i$）并且满足 Q4 对一切 $f,g$。

**完整证明**

1. 若这样的 $Q$ 存在，把它限制到 $P^{\le4}\subset C^\infty(\mathbb{R}^{2n})$，就得到定理 5.4.1 所禁止的映射。
   - *为什么*：限制不改变线性性与括号关系；标准值条件也原样保留。
2. 定理 5.4.1 的证明只用到 Q2、Q4 与低次取值，因此 Q5 是否成立与矛盾无关：即使不要求 Q5，Q1–Q4 也已经不可能实现。
   - *为什么*：这条推论把「不可行」的责任精确地归给 Q4，而不是归给 Q5。

来源：ch05b.tex:686-699、815（原书 p.282、p.284）

## 易错点

- 定理的前提 (2) 要求 Q4 对一切 $f,g\in P^{\le4}$ 成立；若只要求低次多项式之间的 Q4（例如 $f,g\in P^{\le2}$），矛盾不出现——外尔量子化本身就是这样的例子。别把定理读成「任何量子化都不可能」。
- $[x^3,p^3]_*$ 与 $[x^2p,xp^2]_*$ 里的 $\Lambda^3$ 是双微分算子，导数分别落在左右两个因子上。若把 $\Lambda^3$ 当成单个微分算子作用在乘积 $x^3p^3$ 上，会得到 $36$ 而不是 $-12$，$\pm\frac16\hbar^2$ 就被错算成 $-\frac12\hbar^2$，矛盾的数值随之出错。
- 两侧之差是 $\frac13\hbar^2$，单侧的偏移才是 $\frac16\hbar^2$；报数时说清楚是哪一个。另外这不是「$\hbar$ 的高阶修正可以忽略」的问题：$Q$ 是固定 $\hbar$ 的映射，定理对每个 $\hbar\ne0$ 都成立。

## 相关卡

- [狄拉克量子化原理 Q1–Q5](../concepts/dirac-quantization.md)
- [预量子化线丛](../concepts/prequantization.md)
- [斯通–冯·诺依曼定理](../concepts/stone-von-neumann.md)
- [量子算子与 P-保持条件](../concepts/quantum-operator.md)

## 出处

- §5.4.2 定理 5.4.1 与证明的前半（$P^{\le3}$），p.282–283（PDF p.283–284），源码 `ch05b.tex:686-760`
- §5.4.2 四次多项式的矛盾，p.283–284（PDF p.284–285），源码 `ch05b.tex:761-816`
