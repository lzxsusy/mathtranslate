# 辛流形（symplectic manifold）

> `geoq/concept/symplectic-manifold` · 轨道 A · 相空间的辛几何 · 状态 draft

> **先自测**：为什么辛形式要同时要求「闭」与「非退化」，只留一条会丢掉什么？

## 一句话

光滑流形配上闭的、逐点非退化的 $2$-形式；非退化把切空间与余切空间等同，闭性让哈密顿流保辛，$\omega^n/n!$ 给出刘维尔体积。

## 定义

辛流形指带有一份额外结构的流形：$(M,\omega)$ 中 $M$ 光滑，$\omega$ 是 $M$ 上的光滑 2-形式，并且满足两条公理。其一，$d\omega=0$，即 $\omega$ 闭；其二，每个切空间上的双线性形式 $\omega_p$ 都非退化——若 $\omega_p(u,v)$ 对一切 $v$ 为零，则 $u=0$。满足这两条时，$\omega$ 称为辛形式。

**记号约定**：$x^i$ 是局部坐标，$\omega=\frac12\sum_{i,j}\omega_{ij}(x)\,dx^i\wedge dx^j$，其中 $\omega_{ij}=-\omega_{ji}$；$\omega^{ij}$ 是矩阵 $(\omega_{ij})$ 的逆矩阵元素，满足 $\sum_k\omega^{ik}\omega_{kj}=\delta^i_j$；$\dim M=2n$；$\mathrm{Vect}(M)$ 是光滑向量场空间。

## 要点

- 非退化等价于逐点矩阵 $(\omega_{ij})$ 可逆，线性代数随即给出 $\dim M=2n$ 为偶数，且 $\omega^n$ 处处非零。
- 闭性 $d\omega=0$ 在坐标下是三个指标的循环求和为零；只有下标互异时才需要检查，含重复下标的分量自动消失。
- 两条条件分工明确：非退化让每一点都有辛配对（从而有哈密顿向量场），闭性把不同点的辛形式绑在一起（从而哈密顿流保辛）；去掉闭性得到的是近辛流形，理论立刻散架。
- 由 $\frac{1}{n!}\omega^n$ 是无处零的最高次形式，$M$ 必可定向；但辛结构记住的是逐点的面积配对，信息远比一个体积形式多。
- 局部没有不变量：达布定理保证每点附近可取坐标 $q^i,p_i$ 使 $\omega=\sum_i dp_i\wedge dq^i$（本书未证，只作背景），所以辛几何的全部内容都在整体。
- 标准例子有两个：$\mathbb{R}^{2n}$ 配上常系数形式 $\omega_n$；任意光滑流形 $X$ 的余切丛 $T^*X$ 配上 $d\lambda$。

## 关键公式

$$
$\omega=\frac12\sum_{i,j}\omega_{ij}(x)\,dx^i\wedge dx^j,\qquad \omega_{ij}=-\omega_{ji}$
$$

$$
$d\omega=0\iff \partial_i\omega_{jk}+\partial_j\omega_{ki}+\partial_k\omega_{ij}=0$
$$

$$
$\det(\omega_{ij}(x))\neq0,\qquad \forall x$
$$

$$
$\flat_\omega:TM\to T^*M,\qquad X\mapsto\iota_X\omega$ 是丛同构
$$

$$
$\frac{1}{n!}\omega^n$ 是 $M$ 的体积形式，$2n=\dim M$
$$

## 定理与证明

### 非退化性 $\iff$ $\flat_\omega$ 是丛同构；辛流形为偶数维且可定向

设 $(M,\omega)$ 是辛流形，$\dim M=m$。则 $\flat_\omega:TM\to T^*M$，$X\mapsto\iota_X\omega$ 是向量丛同构；由此 $m=2n$ 为偶数，$\omega^n$ 处处非零，$\frac{1}{n!}\omega^n$ 是 $M$ 的体积形式，特别地 $M$ 可定向。

**完整证明**

1. 逐点看：$(\flat_\omega)_p:T_pM\to T_p^*M$ 的核是 $\{X\in T_pM\mid \omega_p(X,Y)=0,\ \forall Y\}$，非退化说的正是这个核为零，故 $(\flat_\omega)_p$ 单射。
   - *为什么*：非退化的定义就是零空间平凡，这一步只是把定义翻译成线性映射的语言。
2. 取基 $c_1,\dots,c_m$，$(\flat_\omega)_p$ 在这组基与其对偶基下的矩阵恰为 $(\omega_{ij})$，故单射等价于 $\det(\omega_{ij})\neq0$，此时 $T_pM$ 与 $T_p^*M$ 同维，单射即同构。
   - *为什么*：把「同构」化成「矩阵可逆」，才能在局部一次算完。
3. 对斜对称矩阵 $A=(\omega_{ij})$ 有 $\det A=\det(-A^T)=(-1)^m\det A$；若 $m$ 为奇数则 $\det A=-\det A$，只能 $\det A=0$，与可逆矛盾，故 $m=2n$。
   - *为什么*：维数必须为偶数这件事完全来自行列式的符号，不需要任何几何输入。
4. 由 $\det(\omega_{ij})\neq0$ 知 $\omega_p^n\neq0$；在 $2n$ 维空间里 $n$ 次外积只剩一个方向，故 $\frac{1}{n!}\omega^n$ 是无处零的 $2n$-形式，它给出一致的定向。
   - *为什么*：体积形式就是无处零的最高次形式，可定向就是存在这样的形式。

来源：ch05a.tex:563-627（原书 p.259–260）；维数论证同书 ch05a.tex:53

### 局部坐标下的闭性与非退化（定义 5.1.18 的坐标翻译）

在局部坐标 $x^i$ 下写 $\omega=\frac12\sum_{i,j}\omega_{ij}(x)\,dx^i\wedge dx^j$。则 $d\omega=0$ 等价于对一切 $i,j,k$ 有 $\partial_i\omega_{jk}+\partial_j\omega_{ki}+\partial_k\omega_{ij}=0$；非退化等价于 $\det(\omega_{ij}(x))\neq0$ 对一切 $x$ 成立。

**完整证明**

1. 按外微分的定义展开：$d\omega=\frac12\sum_{i,j,k}\partial_k\omega_{ij}\,dx^k\wedge dx^i\wedge dx^j$，只需按 $dx^i\wedge dx^j\wedge dx^k$ 重新归并系数。
   - *为什么*：外微分没有额外结构，纯粹是逐项求导再外乘。
2. 因为 $dx^k\wedge dx^i\wedge dx^j$ 在指标置换下按符号变化，而 $\omega_{ij}$ 斜对称，三组置换后的项合并后系数正比于 $\partial_i\omega_{jk}+\partial_j\omega_{ki}+\partial_k\omega_{ij}$；三个下标互异时这一项才可能不为零。
   - *为什么*：这解释了为什么「闭」是一个三指标循环方程，只有 $\binom{m}{3}$ 个独立分量。
3. 若三个下标有重复，例如 $i=j$，则方程化为 $\partial_i\omega_{ik}+\partial_i\omega_{ki}=0$，由斜对称自动成立。于是 $d\omega=0$ 只剩下标互异的情形要验证。
   - *为什么*：排除自动成立的方程，才知道真正要检查什么、也不会误以为条件比实际更强。
4. 非退化那条：$(\omega_{ij}(x))$ 是 $\omega|_x$ 在坐标基下的矩阵，由第 1 条定理的步骤 2 即知可逆 $\iff$ 非退化。
   - *为什么*：逐点条件与矩阵条件是一回事，坐标只提供了一张逐点的图。

来源：ch05a.tex:575-586（原书 p.259）

## 易错点

- 只有非退化（近辛）时 $\omega^n$ 照样是体积形式，但没有 $d\omega=0$ 就推不出 $\mathcal{L}_{V_f}\omega=0$，哈密顿流不再保辛，命题 5.1.21 与 5.1.22 全部失效。两条条件不能只留一条。
- $d\omega=0$ 不等于 $\omega$ 恰当。$\mathbb{R}^{2n}$ 上 $\omega_n=d(\sum p_idq^i)$ 确实恰当，但紧致辛流形（如 $S^2$ 的面积形式）上 $[\omega]\neq0$，不能整体写成 $d\theta$——这与预量子化能否取平凡线丛直接相关。
- 坐标公式里的 $\frac12$ 与 $\omega_{ij}$ 的斜对称是配套约定：$\omega=\frac12\sum_{i,j}\omega_{ij}dx^i\wedge dx^j=\sum_{i<j}\omega_{ij}dx^i\wedge dx^j$，两种写法是同一个形式、同一个矩阵 $(\omega_{ij})$；换了写法又把系数整体乘 $2$，才会把行列式算错。
- 记号坑：$\omega^{ij}$ 是 $(\omega_{ij})$ 的逆矩阵元素，不是 $\omega_{ij}$ 逐项取倒数；$\omega_{ij}\omega^{ij}$ 一般也不等于 $2n$ 以外的简单数。
- 「非退化」是逐点条件，不要求 $\omega$ 是常系数形式；把它当成「$\omega$ 与坐标无关」会错误地只承认 $\mathbb{R}^{2n}$ 上的线性辛结构。

## 相关卡

- [辛向量空间与辛基](../concepts/symplectic-vector-space.md)
- [哈密顿向量场与泊松括号](../concepts/hamiltonian-vector-field.md)
- [余切丛的典范辛结构与刘维尔形式](../concepts/cotangent-bundle.md)
- [辛同胚与哈密顿流](../concepts/symplectomorphism.md)
- [余切丛 $T^*X$ 的典范辛形式（$X=\mathbb{R}^2$）](../examples/cotangent-bundle-symplectic.md)

## 出处

- §5.1.4 辛流形（定义 5.1.18 与局部坐标刻画），p.259–260（PDF p.260–261），源码 `ch05a.tex:563-627`
