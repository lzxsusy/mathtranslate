# 哈密顿向量场与泊松括号

> `geoq/concept/hamiltonian-vector-field` · 轨道 A · 相空间的辛几何 · 状态 draft

> **先自测**：$\{f,g\}=V_f(g)$ 为什么自动满足雅可比恒等式，而 $f\mapsto V_f$ 的核又是什么？

## 一句话

由 $\iota_{V_f}\omega=df$ 定义的向量场 $V_f$ 与 $\{f,g\}=V_f(g)$ 构成李代数同态；$V_f$ 保辛形式与体积，且 $V_{\{f,g\}}=[V_f,V_g]$。

## 定义

在辛流形 $(M,\omega)$ 上取光滑函数 $f$。因为 $\flat_\omega$ 是丛同构，方程 $\iota_{V_f}\omega=df$ 有且只有一个解 $V_f$，即 $f$ 的哈密顿向量场。对两个函数 $f,g$，其泊松括号定义为 $\{f,g\}:=\iota_{V_f}\iota_{V_g}\omega$；利用 $\iota_{V_g}\omega=dg$ 可把它写成 $\{f,g\}=\iota_{V_f}dg=V_f(g)$。

**记号约定**：$\iota_X$ 是内乘、$\mathcal{L}_X$ 是李导数；$[\cdot,\cdot]$ 是向量场的李括号；$\omega^{ij}$ 是 $(\omega_{ij})$ 的逆矩阵元素；$\mathrm{Vect}(M)$ 为光滑向量场空间；$\mathrm{Ham}(M,\omega)$ 记哈密顿向量场全体。

## 要点

- $V_f$ 的存在唯一性完全来自非退化性：$\flat_\omega$ 可逆，$df$ 才有唯一原像；没有非退化就谈不上哈密顿向量场。
- 坐标公式 $V_f=\sum_{i,j}\omega^{ij}\partial_if\,\partial_j$ 说明 $V_f$ 是 $f$ 的一阶算子；$f\mapsto V_f$ 线性但不 $C^\infty(M)$-线性，正确的关系是 $V_{fh}=fV_h+hV_f$。
- 符号约定要钉住：$\{f,g\}=\omega(V_g,V_f)=-\omega(V_f,V_g)$，且 $\{f,g\}=V_f(g)=-V_g(f)$；写成 $+\omega(V_f,V_g)$ 会把所有括号整体反号。
- 命题 5.1.21 给出 $\mathcal{L}_{V_f}\omega=0$，推论是刘维尔定理 $\mathcal{L}_{V_f}(\omega^n/n!)=0$：哈密顿流保体积，这是自伴性与遍历性质的几何来源。
- 命题 5.1.22 与 5.1.23 合起来说：$f\mapsto V_f$ 是李代数同态，核是局部常值函数，故哈密顿向量场空间是 $C^\infty(M)$ 的商。
- $V_f$ 的流是辛同胚（见辛同胚卡），因此泊松括号可以读成「沿 $f$ 的流对 $g$ 求导」，这与量子力学里 $[\hat f,\hat g]$ 的对应就是狄拉克原理的起点。

## 关键公式

$$
$\iota_{V_f}\omega=df$
$$

$$
$V_f=\sum_{i,j}\omega^{ij}\partial_if\,\partial_j$
$$

$$
$\{f,g\}=\iota_{V_f}\iota_{V_g}\omega=V_f(g)=\sum_{i,j}\omega^{ij}\partial_if\,\partial_jg$
$$

$$
$\mathcal{L}_{V_f}\omega=0,\qquad \mathcal{L}_{V_f}\left(\frac{1}{n!}\omega^n\right)=0$
$$

$$
$V_{\{f,g\}}=[V_f,V_g],\qquad V_{fh}=fV_h+hV_f$
$$

## 定理与证明

### 命题 5.1.21：哈密顿向量场保辛形式

设 $(M,\omega)$ 是辛流形，$f\in C^\infty(M)$，$V_f$ 由 $\iota_{V_f}\omega=df$ 定义。则 $\mathcal{L}_{V_f}\omega=0$；进而 $\mathcal{L}_{V_f}(\omega^n/n!)=0$，即哈密顿流保持刘维尔体积。

**完整证明**

1. 写嘉当公式 $\mathcal{L}_{V_f}\omega=d\iota_{V_f}\omega+\iota_{V_f}d\omega$。
   - *为什么*：李导数作用在微分形式上的标准分解；它把「沿流的变化率」拆成两项分别处理。
2. 第一项：$\iota_{V_f}\omega=df$，故 $d\iota_{V_f}\omega=ddf=0$。第二项：$d\omega=0$。
   - *为什么*：两项分别死于 $d^2=0$ 与辛形式的闭性，这就是「闭」这条公理的唯一用处。
3. 相加得 $\mathcal{L}_{V_f}\omega=0$。
   - *为什么*：两条通道都归零，结论成立。
4. 对体积形式用李导数的莱布尼茨律：$\mathcal{L}_{V_f}(\omega^n)=n\omega^{n-1}\wedge\mathcal{L}_{V_f}\omega=0$，故 $\mathcal{L}_{V_f}(\omega^n/n!)=0$。
   - *为什么*：把 $\omega^n$ 看成 $n$ 重外积，只有一项被求导；该项已为零，于是体积不变。

来源：ch05a.tex:628-646（原书 p.260）

### 命题 5.1.22：$V_{\{f,g\}}=[V_f,V_g]$

对任意 $f,g\in C^\infty(M)$ 有 $V_{\{f,g\}}=[V_f,V_g]$，即「先取泊松括号再取哈密顿向量场」与「先取哈密顿向量场再取李括号」一致。

**完整证明**

1. 待证等式两边都形如「某个向量场的内乘 $\omega$」，先算左边：$\iota_{V_{\{f,g\}}}\omega=d\{f,g\}=d\iota_{V_f}\iota_{V_g}\omega$。
   - *为什么*：把等式化为 $\iota_\bullet\omega$ 的等式，最后才能用非退化性「约掉」$\omega$。
2. 用 $\iota_{V_g}\omega=dg$ 与 $d\iota_{V_f}=\mathcal{L}_{V_f}-\iota_{V_f}d$，得 $d\iota_{V_f}\iota_{V_g}\omega=\mathcal{L}_{V_f}\iota_{V_g}\omega-\iota_{V_f}d\iota_{V_g}\omega$。
   - *为什么*：把外微分换成李导数，好让 $\mathcal{L}_{V_f}$ 直接作用在 $\iota_{V_g}\omega$ 上。
3. 由命题 5.1.21，$\mathcal{L}_{V_f}\omega=0$，故 $\mathcal{L}_{V_f}\iota_{V_g}\omega=\iota_{V_g}\mathcal{L}_{V_f}\omega+\iota_{[V_f,V_g]}\omega=\iota_{[V_f,V_g]}\omega$；又 $d\iota_{V_g}\omega=ddg=0$，第二项消失。
   - *为什么*：这一步同时用到「保辛」与 $d^2=0$，两个条件缺一不可；也是出现李括号的地方。
4. 于是 $\iota_{V_{\{f,g\}}}\omega=\iota_{[V_f,V_g]}\omega$，即 $\iota_{V_{\{f,g\}}-[V_f,V_g]}\omega=0$，由 $\omega$ 非退化得 $V_{\{f,g\}}=[V_f,V_g]$。
   - *为什么*：内乘同一个非退化形式是单射，这正是非退化性在此处的用处。

来源：ch05a.tex:648-666（原书 p.260）

### 命题 5.1.23：$(C^\infty(M),\{\cdot,\cdot\})$ 是李代数，$f\mapsto V_f$ 是同态

$C^\infty(M)$ 配上泊松括号是李代数：括号双线性、斜对称、满足雅可比恒等式；并且 $f\mapsto V_f$ 是李代数同态，即 $V_{\{f,g\}}=[V_f,V_g]$，其核为局部常值函数。

**完整证明**

1. 斜对称：$\{f,g\}=\omega(V_g,V_f)=-\omega(V_f,V_g)=-\{g,f\}$，双线性来自 $\omega$ 与 $df$ 的双线性。
   - *为什么*：反对称性直接继承自辛形式的斜对称，不需要额外假设。
2. 用命题 5.1.22 把 $\{\{f,g\},h\}$ 改写成 $V_{\{f,g\}}(h)=[V_f,V_g](h)=V_f(V_gh)-V_g(V_fh)=\{f,\{g,h\}\}-\{g,\{f,h\}\}$。
   - *为什么*：把泊松括号翻译成向量场作用，李括号的展开就变成一阶导数的结合律。
3. 将上式移项并用斜对称：$\{\{f,g\},h\}+\{\{g,h\},f\}+\{\{h,f\},g\}=0$，即雅可比恒等式。
   - *为什么*：这正是雅可比恒等式的循环形式，逐个移项即可核对。
4. 同态性就是命题 5.1.22；核为 $\{f\mid df=0\}$，即局部常值函数（$M$ 连通时就是常数）。
   - *为什么*：$V_f=0\iff df=0$，非退化性让这一等价成立；核的计算同时说明 $V_f$ 只记得 $f$ 的微分。

来源：ch05a.tex:668-687（原书 p.260）

## 易错点

- 符号：定义取 $\iota_{V_f}\omega=df$ 而不是 $-df$。若换成 $-df$，泊松括号、哈密顿方程与 $V_{\{f,g\}}=[V_f,V_g]$ 的相对符号会整体翻转；读别的教材前必须先确认这一条。
- $\{f,g\}=V_f(g)$，不是 $V_g(f)$：两者差一个负号。把括号读成「$g$ 沿 $f$ 的流的变化率」是对的，读成「$f$ 沿 $g$ 的流的变化率」就反了。
- 在余切丛上用 $\lambda=\sum p_idq^i$、$\omega=d\lambda=\sum dp_i\wedge dq^i$ 时，$V_f=\sum_i(\partial_{q^i}f\,\partial_{p_i}-\partial_{p_i}f\,\partial_{q^i})$，哈密顿方程读作 $\dot q^i=-\partial_{p_i}f$、$\dot p_i=\partial_{q^i}f$；物理教材常用 $\omega=\sum dq^i\wedge dp_i$，那里的方程是 $\dot q^i=+\partial_{p_i}f$，差一个整体符号。
- $f\mapsto V_f$ 不是 $C^\infty(M)$-线性的：$V_{fh}=fV_h+hV_f$。若按 $V_{fh}=fV_h$ 去算会漏掉一项，也会误以为 $V_f$ 决定 $f$（其实只决定 $df$）。
- 「保辛」比「保体积」强：命题 5.1.21 的推论只给出保体积，反过来不成立；$n\ge2$ 时存在保体积但不保辛的微分同胚。

## 相关卡

- [辛流形（symplectic manifold）](../concepts/symplectic-manifold.md)
- [辛同胚与哈密顿流](../concepts/symplectomorphism.md)
- [余切丛的典范辛结构与刘维尔形式](../concepts/cotangent-bundle.md)
- [拉格朗日子流形、可投影与相函数](../concepts/lagrangian-submanifold.md)
- [哈密顿流是辛同胚（$f=\tfrac12q^2$ 与 $f=q^1q^2$）](../examples/hamiltonian-flow-symplectomorphism.md)

## 出处

- §5.1.4 定义 5.1.19–5.1.20 与命题 5.1.21–5.1.23，p.259–261（PDF p.260–262），源码 `ch05a.tex:588-690`
