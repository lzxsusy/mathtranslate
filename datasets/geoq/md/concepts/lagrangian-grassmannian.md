# 拉格朗日子空间与格拉斯曼流形

> `geoq/concept/lagrangian-grassmannian` · 轨道 A · 相空间的辛几何 · 状态 draft

> **先自测**：为什么迷向子空间的维数最多是一半，而达到一半的那些子空间恰好满足 $L=L^\perp$？

## 一句话

辛形式在子空间上消失、且维数恰为全空间一半者称拉格朗日；全体这样的子空间构成紧齐性流形，酉群在其上可迁。

## 定义

在辛向量空间 $(V,\omega)$ 中，若子空间 $L$ 上 $\omega$ 恒取零值（任意 $u,v\in L$ 都有 $\omega(u,v)=0$），则 $L$ 称为迷向子空间。迷向子空间一旦把维数撑到 $\frac12\dim V$，就称为拉格朗日子空间；所有这类子空间组成的集合记作 $\mathcal L(V)$，即拉格朗日格拉斯曼流形。对任意子空间 $N$，用 $N^\perp$ 表示与 $N$ 中每个向量都 $\omega$-正交的向量全体。

**记号约定**：$\dim V=2n$，$\dim L=n$；$N^\perp$ 是 $\omega$-正交补，与内积 $g_J$ 的正交补 $N^*$ 不同，后者只需 $g_J(u,n)=0$。$\operatorname{O}(L)$ 表示 $L$ 上关于 $g_J|_L$ 的正交群，$\operatorname{U}(V)=\operatorname{Sp}(V)\cap\operatorname{O}(V)$。

## 要点

- 迷向的维数上界来自一个单射 $L\to(V/L)^*$：把 $u$ 送到 $\omega(u,-)$ 在商上的泛函；证明只用非退化，不需要任何正定性。
- 拉格朗日条件有三条等价说法：迷向且 $\dim L=\frac12\dim V$；$L$ 迷向且 $L=L^\perp$；$L=L^\perp$ 本身。核心是 $\dim N^\perp=\dim V-\dim N$。
- $\mathcal L(V)$ 是紧流形，$\dim_{\mathbb R}\mathcal L(V)=\frac{n(n+1)}2$；$n=1$ 时退化为 $\mathbb{RP}^1\cong S^1$，这就是「所有直线」的例子。
- $\operatorname{U}(V)$（于是 $\operatorname{Sp}(V)$）在 $\mathcal L(V)$ 上可迁，稳定化子为 $\operatorname{O}(L)$，故 $\mathcal L(V)=\operatorname{U}(V)/\operatorname{O}(L)\cong \operatorname{U}(n)/\operatorname{O}(n)$。
- 每个 $L$ 都给出 $g_J$-正交分解 $V=L\oplus J(L)$，$J(L)$ 也是拉格朗日；因此「$V$ 写成两个拉格朗日之和」不需要任何额外选择。
- 迷向严格弱于拉格朗日：$n\ge2$ 时 $\operatorname{span}\{e_1\}$ 在 $(\mathbb R^{2n},\omega_n)$ 中迷向但维数只有 $1$，不是拉格朗日。

## 关键公式

$$
$\omega|_{L\times L}=0\ \iff\ \omega(u,v)=0\ \ \forall u,v\in L,\qquad \dim L\le\tfrac12\dim V$
$$

$$
$L\ \text{拉格朗日}\iff L\ \text{迷向且}\ \dim L=\tfrac12\dim V\iff L=L^\perp$
$$

$$
$N^\perp=\{u\in V\mid\omega(u,N)=0\},\qquad \dim N^\perp=\dim V-\dim N$
$$

$$
$\mathcal L(V)=\operatorname{U}(V)/\operatorname{O}(L)\cong \operatorname{U}(n)/\operatorname{O}(n),\qquad \dim\mathcal L(V)=\tfrac{n(n+1)}2$
$$

$$
$V=L\oplus J(L),\qquad L^*=J(L)\ (g_J\text{-正交补})$
$$

## 定理与证明

### 命题 5.1.12（迷向子空间的维数上界）

若 $L$ 是辛向量空间 $(V,\omega)$ 的迷向子空间，则 $\dim L\le\frac12\dim V$。

**完整证明**

1. 由 $\omega$ 非退化，$\tilde\omega:V\to V^*$，$v\mapsto\omega(v,-)$ 是线性同构。
   - *为什么*：$\tilde\omega$ 的核恰是零空间 $N$，非退化即 $N=0$。
2. 设 $L$ 迷向。对 $u\in L$，泛函 $\omega(u,-)$ 在 $L$ 上为零，故它在商 $V/L$ 上下良定义：$\tilde\omega_L:L\to(V/L)^*$，$u\mapsto\bigl([v]\mapsto\omega(u,v)\bigr)$。
   - *为什么*：「在 $L$ 上为零」正是下降（well-defined）所需条件，这一步用到迷向性。
3. $\tilde\omega_L$ 是单射：若 $\tilde\omega_L(u)=0$，则 $\omega(u,v)=0$ 对一切 $v\in V$ 成立（因 $[v]$ 跑遍 $V/L$，而 $L$ 上已知为零），由非退化得 $u=0$。
   - *为什么*：把「对商为零」拆回「对 $V$ 为零」，再交给非退化性；这里 $u\in L$ 只是为了保证 $u$ 落在映射的定义域里。
4. 于是 $\dim L\le\dim(V/L)^*=\dim V-\dim L$，移项得 $\dim L\le\frac12\dim V$。
   - *为什么*：单射给出维数不等式，$\dim(V/L)=\dim V-\dim L$ 是商空间的维数公式。

来源：ch05a.tex:306-329（原书 pp.254-255）

### 命题 5.1.16（$\operatorname{U}(V)$ 作用的可迁性与稳定化子）

$\operatorname{U}(V)$ 在 $\mathcal L(V)$ 上的作用可迁，且 $L$ 处的稳定化子为 $\operatorname{O}(L)$。因此 $\mathcal L(V)=\operatorname{U}(V)/\operatorname{O}(L)\cong \operatorname{U}(n)/\operatorname{O}(n)$。

**完整证明**

1. 取 $L_1,L_2\in\mathcal L(V)$，及 $g_J$-正交同构 $\varphi:L_1\to L_2$（等维欧氏空间之间总存在）。
   - *为什么*：限制在 $L_i$ 上的 $g_J$ 都是正定内积，维数相同故可取正交同构。
2. 定义 $\tilde\varphi:L_1\oplus JL_1\to L_2\oplus JL_2$ 为 $\tilde\varphi=\varphi\oplus J\circ\varphi\circ J^{-1}$，即 $\tilde\varphi(u)=\varphi(u)$、$\tilde\varphi(Ju)=J\varphi(u)$。由 $V=L_i\oplus JL_i$，$\tilde\varphi$ 延拓为 $V$ 上的线性同构。
   - *为什么*：两部分各自定义在互补的直和项上，故拼起来是 $V$ 上的同构；第二块的写法保证它与 $J$ 交换。
3. $\tilde\varphi$ 与 $J$ 交换，且保 $g_J$：两个直和块上 $\varphi$ 与 $J\varphi J^{-1}$ 都正交，交叉项由直和正交性为零。故 $\tilde\varphi\in\operatorname{GL}(V,J)\cap\operatorname{O}(V)=\operatorname{U}(V)$，且 $\tilde\varphi(L_1)=L_2$。
   - *为什么*：命题 5.1.7 说明保 $J$ 又保 $g_J$ 就是酉的；可迁性由 $\tilde\varphi(L_1)=L_2$ 得到。
4. 稳定化子：若 $\tilde\varphi\in\operatorname{U}(V)$ 且 $\tilde\varphi(L)=L$，则 $\varphi=\tilde\varphi|_L$ 保 $g_J|_L$，故 $\varphi\in\operatorname{O}(L)$；反之任给 $\varphi\in\operatorname{O}(L)$，按步骤 2 的公式延拓即得稳定化子中的元素。
   - *为什么*：两个方向都用了「$L$ 与其 $J$-像的直和」这一分解，限制与延拓互为逆过程。
5. 由轨道–稳定化子定理，$\mathcal L(V)\cong\operatorname{U}(V)/\operatorname{O}(L)$；取定 $J$ 后 $\operatorname{U}(V)\cong\operatorname{U}(n)$、$\operatorname{O}(L)\cong\operatorname{O}(n)$。维数 $\dim\operatorname{U}(n)-\dim\operatorname{O}(n)=n^2-\frac{n(n-1)}2=\frac{n(n+1)}2$。
   - *为什么*：齐性空间的维数等于群维数减稳定化子维数，这同时给出 $\mathcal L(V)$ 的维数公式。

来源：ch05a.tex:394-429（原书 p.256）

## 易错点

- $L^\perp$ 是 $\omega$-正交补，不是 $g_J$-正交补：对拉格朗日 $L$，$L^\perp=L$ 而 $L^*=J(L)$，两者一般不同，混用会把「$L=L^\perp$」误判成「$L=J(L)$」。
- $\dim N^\perp=\dim V-\dim N$ 依赖 $\omega$ 非退化；若 $\omega$ 退化（例如只给斜对称形式），维数公式失效，迷向的维数上界也不再成立。
- 「迷向」不是「全迷向」：迷向只要求 $\omega$ 在 $L$ 上为零，$L$ 中可以有非零向量；在辛空间里这恰恰是常态，因为 $\omega(u,u)=0$ 恒成立。
- $\dim\mathcal L(V)=\frac{n(n+1)}2$ 是实维数；不要与复维数或 $\operatorname{Gr}(n,2n)$ 的维数 $n^2$ 混淆，后者是全体 $n$ 维子空间，比 $\mathcal L(V)$ 大。

## 相关卡

- [辛向量空间与辛基](../concepts/symplectic-vector-space.md)
- [相容复结构与可缩性](../concepts/compatible-complex-structure.md)
- [马斯洛夫指标与 $\mathcal L(V)$ 的基本群](../concepts/maslov-index.md)
- [标准辛基给出的两张拉格朗日子空间](../examples/standard-lagrangian-subspaces.md)
- [$\mathcal L(\mathbb R^2)=\mathbb{RP}^1$ 上的马斯洛夫指标](../examples/maslov-index-rp1.md)
- [拉格朗日子流形、可投影与相函数](../concepts/lagrangian-submanifold.md)
- [极化：实极化与凯勒极化](../concepts/polarization.md)

## 出处

- §5.1.2 迷向、拉格朗日与命题 5.1.12，p.254–255（PDF p.255–256），源码 `ch05a.tex:299-368`
- §5.1.2 命题 5.1.16 与齐性空间，p.256（PDF p.257），源码 `ch05a.tex:370-429`
