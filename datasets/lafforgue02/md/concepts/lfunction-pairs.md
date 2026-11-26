# 配对 $L$-函数（fonction $L$ de paires）

> `lafforgue02/concept/lfunction-pairs` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：为什么「边界上同调 $r$-可忽略」这样一条纯几何命题，要用配对 $L$-函数的收敛性来证？

## 一句话

可忽略部分的排除靠对数导数在 $|Z|<q^{-2+2\varepsilon}$ 内绝对收敛；这恰是配对 $L$-函数（自守侧与 Galois 侧各一对）的收敛性估计。

## 定义

配对 $L$-函数指 $L(\pi\times\tilde\pi',Z)$ 一类由两个自守表示（或两个 Galois 表示）配对得到的 $L$-函数。第 II 章用它们的对数导数 $L'/L$ 的级数展开，把「本质部分的权」与「是否存在可忽略分量」联系起来。

**记号**：$L_{X-N}(\pi\times\tilde\pi',Z)$；$Z$ 为形式变量，收敛域 $|Z|<q^{-1+\varepsilon}$ 与 $|Z|<q^{-2+2\varepsilon}$。

## 要点（为什么需要它）

1. 论证结构是反证：若最大权块含可忽略分量 $q'^*\sigma'\otimes q''^*\sigma''$，则某个配对 $L$-函数的对数导数在指定圆盘内不绝对收敛。
2. 收敛性来自 Jacquet–Shalika 的估计：$L(\pi\times\tilde\pi',Z)$ 在 $|Z|<q^{-1+\varepsilon}$ 内无极点。
3. 把两个方向的 $L'/L$ 相乘（「逐项乘积」），得到对 $H\otimes(\tilde\sigma'\otimes\tilde\sigma'')$ 的配对 $L$-函数，其收敛半径 $q^{-2+2\varepsilon}$ 恰好对应权 $2$。
4. 这一步同时给出「本质部分纯权 $0$」与「无 $r$-可忽略分量」两个结论。

## 核心公式

$$
$\dfrac{L'_{X-N}(\pi\times\tilde\pi',Z)}{L_{X-N}(\pi\times\tilde\pi',Z)}=\sum_{\infty\in(X-N)}\deg(\infty)\sum_{k\ge1}\big(\sum_i z_i(\pi_\infty)^{-k}\big)\big(\sum_i z_i(\pi'_\infty)^{k}\big)Z^{k\deg(\infty)-1}$$\dfrac{L'_{(X-N)\times(X-N)}(H\otimes(\tilde\sigma'\otimes\tilde\sigma''),Z)}{L_{\cdots}(\cdots,Z)}$ 在 $|Z|<q^{-2+2\varepsilon}$ 内绝对收敛
$$

$$
$\dfrac{L'_{(X-N)\times(X-N)}(H\otimes(\tilde\sigma'\otimes\tilde\sigma''),Z)}{L_{\cdots}(\cdots,Z)}$ 在 $|Z|<q^{-2+2\varepsilon}$ 内绝对收敛
$$

## 定理与证明（或缺口）

### 可忽略性的 $L$-函数判据

若本质部分的最大权块含 $r$-可忽略分量，则对应配对 $L$-函数的对数导数在某圆盘内不绝对收敛；而该收敛性成立，故无此分量。

> 证明状态：**sketch**。收敛性估计本身（Jacquet–Shalika）在讲义中只作引用，未给证明。

出处：`A p.15`

## 常见误解

- 这里的 $L$-函数不是 Langlands 对应的 $L(\pi,s)$，而是两个表示**配对**后的 $L$-函数；混淆两者会看不出权 $2$ 的来源。
- 收敛性的阈值 $q^{-2+2\varepsilon}$ 与「权 $2$」对应，不是任意取的常数。

## 相关卡

[$r$-可忽略表示与本质上同调](../concepts/r-negligible-representation.md) · [为什么本质部分集中在中间次数 $2r-2$](../derivations/essential-part-in-middle-degree.md) · [函数域上的 Langlands 对应（$\mathrm{GL}_r$）](../concepts/langlands-correspondence-function-field.md)

## 出处（印刷页）

- A p.15–16（A p.15）

> 说明：配对 $L$-函数的级数展开取讲义 p.15 的两个展示式（A 级）；收敛性估计引自 Jacquet–Shalika（讲义的引用，B 级）；「权 $2$ 对应」一句是本卡对阈值的解读（B 级）。
