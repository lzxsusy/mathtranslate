# $\phi^t$ 连续延拓到完备化的态射空间

`kshms/concept/prp-12-continuous-extension` · track F（同调镜像猜想） · 原文 命题 12

**问题**　只在指数有限和上定义的 $\phi^t$，凭什么能连续延拓到全部态射？

**摘要**　因为 $\psi^t$ 使滤过下降，只在指数有限和上定义的 $\phi^t$ 可连续延拓到整个态射空间 $\mathrm{Hom}_{C(Y)}(E_1,E_2)$，即延拓到滤过的完备化上。

**别名**　Proposition 12；continuous extension of $\phi^t$；半群 $\phi^t$ 在 $\mathrm{Hom}_{C(Y)}$ 上的作用

## 陈述

$\phi^t$ 的作用连续地从 $\mathrm{Hom}^{alg}_{C(Y)}(E_1,E_2)$ 延拓到 $\mathrm{Hom}_{C(Y)}(E_1,E_2)$。

## 记号

$\mathrm{Hom}^{alg}_{C(Y)}(E_1,E_2)$：由对 $z_i$ 与 $e^{-\lambda/\varepsilon}$ 都是有限和的代数态射构成的子空间，在 $\mathrm{Hom}_{C(Y)}(E_1,E_2)$ 中稠密；$\mathrm{Hom}_{C(Y)}(E_1,E_2)$：关于 $\mathbb{R}$-滤过的完备化；$\psi^t$：$P(L_1,L_2)$ 上的半群，其在 $\Gamma_c(P(L_1,L_2),\underline{\mathrm{Hom}}^{alg})$ 上的作用对应 $\phi^t$。

## 要点

- 两个前提缺一不可：$\mathrm{Hom}^{alg}_{C(Y)}$ 在 $\mathrm{Hom}_{C(Y)}$ 中稠密（解析函数可用 Laurent 多项式逼近），且两者的滤过完备化重合。
- 延拓的机制是命题 11：$\psi^t$ 使滤过只下降不上升，故关于滤过连续，可以穿过完备化。
- $\pi_!$ 与 $\underline{\mathrm{Hom}}^{alg}_{C(Y)}$、$\underline{\mathrm{Hom}}^{alg}$ 的茎上滤过相容，且前者茎的完备化恰是 $\mathrm{Hom}_{C(Y)}(E_1,E_2)$，$\psi^t$ 的延拓于是下降为 $\phi^t$ 的延拓。
- 结论只是「连续延拓」：既没有断言 $\phi^t$ 是单参数群，也没有断言 $t\to+\infty$ 收敛，后者的存在性是命题 13 的内容。

## 公式

$$\phi^t:\mathrm{Hom}^{alg}_{C(Y)}(E_1,E_2)\longrightarrow\mathrm{Hom}_{C(Y)}(E_1,E_2)$$

## 证明（complete）

1. $\pi_!$ 与 $\underline{\mathrm{Hom}}^{alg}_{C(Y)}$、$\underline{\mathrm{Hom}}^{alg}$ 的茎上滤过相容；前者茎关于诱导滤过的完备化与 $\mathrm{Hom}_{C(Y)}(E_1,E_2)$ 重合。

   *为什么*：原文明确给出这一重合，它是把层上的讨论搬到态射空间的依据。

2. 由命题 11，$\psi^t$ 在不属于 $L_1\cap L_2$ 的点上使滤过下降，故 $\psi^t$ 关于滤过连续。

   *为什么*：滤过指标只下移有限的 $\int_0^t\mu$，映射不放大任何一层，故在滤过拓扑下连续。

3. 连续映射穿过完备化：$\phi^t$ 由 $\mathrm{Hom}^{alg}_{C(Y)}(E_1,E_2)$ 连续延拓到其完备化 $\mathrm{Hom}_{C(Y)}(E_1,E_2)$。

   *为什么*：稠密子空间上的连续映射在完备化上的延拓唯一存在，这是完备化的泛性质；稠密性由 Laurent 多项式逼近保证。

## 易错点

- 别把延拓读成「$\phi^t$ 在新空间上仍由原来的有限和公式给出」：完备化后的元素是无穷级数，$\phi^t$ 只作为连续映射存在。
- 连续性是对 $\mathbb{R}$-滤过的拓扑而言，不是对某个范数拓扑；说「$\phi^t$ 连续」时必须点明这层滤过。
- 命题 11 的下降性质不可省：若 $\psi^t$ 使滤过上升，同样的论证给不出连续延拓。

## 相关卡

- `kshms/concept/prp-11-spectrum-semigroup`
- `kshms/concept/prp-13-psi-infinity-limit`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §8.2（原文 p.56）；锚点 `源码/chunks/ch09.tex:208-211（命题 12）`

> 原文 p56 §8.2；译本 ch09.tex 第 202–211 行（第 202–206 行为论证，第 208–211 行为命题）。
