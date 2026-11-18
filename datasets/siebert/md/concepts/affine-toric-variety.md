# 仿射环面簇

> `siebert/concept/affine-toric-variety` ｜ track D ｜ draft

**一句话**：有理多面尖锥给出的 $\Spec k[\sigma^{\vee}\cap M]$：正规、$d$ 维、含环面为开稠密子概形，其定义理想是二项式生成的环面理想。

**自测**：为什么每个仿射环面簇都正规，而它的环面理想总能由二项式生成？

## 定义

$d$ 维仿射环面簇是形如 $\Spec k[\sigma^{\vee}\cap M]$ 的概形，其中 $\sigma\subset N_{\RR}$ 是有理多面尖锥。$k[M]$ 是 $k[\sigma^{\vee}\cap M]$ 的局部化，故 $T_N=\Spec k[M]$ 经开嵌入 $T_N\subset\Spec k[\sigma^{\vee}\cap M]$ 成为稠密环面轨道。$\sigma$ 换成其面 $\tau$ 就得到开子簇 $U_\tau$，$U_\sigma=U_{\{0\}}$ 的整点正是 $k[\sigma^{\vee}\cap M]$ 的单单项式。

记号：$U_\sigma=\Spec k[\sigma^{\vee}\cap M]$；$T_N=(\mathbb G_m)^{d}$；$m_1,\ldots,m_s$ 是 $\sigma^{\vee}\cap M$ 的幺半群生成元；$I=\ker q$ 是环面理想。

## 要点

- 维数与正规性（命题 4.6）：$C=\sigma^{\vee}$ 时 $\dim\Spec k[C\cap M]=\dim_{\RR}\RR C$。把 $C$ 写成半空间交 $C=\bigcap_i v_i^{\vee}$，每个 $k[M\cap v_i^{\vee}]\simeq k[x_1^{\pm1},\ldots,x_{d-1}^{\pm1},x_d]$ 是多项式环的局部化，整闭环的交仍整闭，故 $k[C\cap M]$ 正规。
- 环面理想（命题 4.3）：取生成元 $m_1,\ldots,m_s$ 得满射 $q:k[x_1,\ldots,x_s]\twoheadrightarrow k[\sigma^{\vee}\cap M]$，$q(x^{a})=\chi^{\sum a_im_i}$；$\ker q$ 由二项式 $x^{a}-x^{b}$（$\sum a_im_i=\sum b_im_i$）生成。证明用 $\deg x_i=m_i$ 的 $M$-分次：$f=\sum_A\alpha_Ax^{A}\in I$ 时 $f\in I\iff\sum_A\alpha_A=0$，再用 $x^{A}-x^{A'}\in G$ 作递减归纳。
- $k$ 值点（命题 4.4）：$X(k)=\Hom_{\Mon}(\sigma^{\vee}\cap M,(k,\cdot))$，右边是乘法幺半群。$\sigma=M_{\RR}$ 时得 $\Hom(M,k^{\times})\simeq(k^{\times})^{d}$；$\sigma=\RR_{\ge0}^{d}$ 时得 $k^{d}$。
- 基本开集（命题 4.5）：若面 $\tau=\sigma\cap m^{\perp}$，则 $\tau^{\vee}\cap M=(\sigma^{\vee}\cap M)+\NN(-m)$，故 $k[\tau^{\vee}\cap M]=k[\sigma^{\vee}\cap M]_{\chi^{m}}$，$U_\tau\hookrightarrow U_\sigma$ 是基本开嵌入。
- 环面分层（引理 4.7）：取面 $\tau\subseteq\sigma$、$L=\RR\tau$，$T_L$ 不变环是 $k[(\tau^{\perp}\cap\sigma^{\vee})\cap M]=k[\sigma^{\vee}\cap M]^{T_L}$；占优态射 $\pi:U_\sigma\to U_{\sigma/L}$ 是范畴商，截面由理想 $I_\tau=(\chi^{m})_{m\in(\sigma^{\vee}\cap M)\setminus\tau^{\perp}}$ 的商给出。

## 公式

$U_\sigma=\Spec k[\sigma^{\vee}\cap M],\qquad k[\tau^{\vee}\cap M]=k[\sigma^{\vee}\cap M]_{\chi^{m}}\ \ (\tau=\sigma\cap m^{\perp})$
$I=\ker\bigl(q:k[x_1,\ldots,x_s]\to k[\sigma^{\vee}\cap M]\bigr)=\bigl(x^{a}-x^{b}:\textstyle\sum_i a_im_i=\sum_i b_im_i\bigr)$
$X(k)=\Hom_{\Mon}(\sigma^{\vee}\cap M,(k,\cdot))$

## 定理与证明

### 命题 4.3：环面理想的二项式生成

若 $m_1,\ldots,m_s\in M$ 作为幺半群生成 $\sigma^{\vee}\cap M$，则 $q:k[x_1,\ldots,x_s]\twoheadrightarrow k[\sigma^{\vee}\cap M]$ 的核由所有差 $x^{a}-x^{b}$（$\sum a_im_i=\sum b_im_i$）生成。

（complete；来源：原书 p.62）

1. 给 $k[x_1,\ldots,x_s]$ 装 $M$-分次：$\deg x_i=m_i$、$\deg\chi^{m}=m$，则 $q$ 是分次映射，$I=\ker q$ 是齐次理想。  
   为什么：齐次性保证 $I$ 只需由齐次元生成，也就能逐次做归纳。
2. 对齐次 $f=\sum_A\alpha_Ax^{A}\in I$，各非零项的权都等于同一个 $m$：$\sum_iA_im_i=m$，且 $q(f)=(\sum_A\alpha_A)\chi^{m}$。  
   为什么：于是 $f\in I$ 当且仅当系数和 $\sum_A\alpha_A=0$，把问题变成纯组合的系数消去。
3. 对非零项数递减归纳：取两项 $A,A'$，$x^{A}-x^{A'}\in G\subset I$，把 $x^{A}$ 替换成 $x^{A'}$，项数减一。  
   为什么：每次替换都保持 $\chi^{m}$ 与系数和，故最终化到零，说明 $G$ 生成 $I$。

### 命题 4.6：有理函数、维数与正规性

设 $C\subset M_{\RR}$ 是有理多面锥，$L=\RR C=C+(-C)$。则 (a) $\operatorname{Quot}k[C\cap M]=k(L\cap M)$；(b) 每个仿射环面簇正规；(c) $\dim\Spec k[C\cap M]=\dim_{\RR}L$。

（sketch；来源：原书 p.63–64）

1. (a) 由 $C\cap M$ 生成 $L\cap M$ 的群，故分式域就是 $k[L\cap M]=k(M\cap L)$。  
   为什么：环面 $\Spec k[L\cap M]\simeq\mathbb G_m^{\dim L}$ 在 $U_\sigma$ 里开稠密。
2. (b) 写 $C=\bigcap_i v_i^{\vee}$，则 $k[C\cap M]=\bigcap_i k[M\cap v_i^{\vee}]$；在共同分式域里整闭环的交整闭，而每个 $k[M\cap v_i^{\vee}]$ 是多项式环的局部化，正规。  
   为什么：正规性是逐半空间验证再取交，避免了直接处理一般的锥。
3. (c) 用 $\Spec k[L\cap M]\simeq\mathbb G_m^{\dim_{\RR}L}$ 是开稠密子概形，维数由开稠密子集读出。  
   为什么：概形的维数在开稠密子概形上不变，环面部分的维数给出答案。

缺口：讲义给出 (a)(b)(c) 的证明骨架，(a) 中「$C\cap M$ 生成 $L\cap M$ 的群」一步未展开，需要 Gordan 引理先保证有限生成再用整点论证。

## 易错点

- 仿射环面簇不是「$\mathbb A^{d}$ 的某个开集」那么简单：$\sigma$ 取 $\RR_{\ge0}^{d}$ 得 $\mathbb A^{d}$，但一般的锥给的是带奇点的仿射簇，例如 $\sigma$ 由 $(1,0),(1,2)$ 生成时得 $A_1$ 奇点。
- 环面理想里不要漏掉 $M$-分次：$I$ 由二项式生成这一结论依赖 $\deg x_i=m_i$，把 $k[x_1,\ldots,x_s]$ 当普通多项式环处理会看不到齐次结构。
- $k$ 值点用乘法幺半群 $(k,\cdot)$，不是加法群：$\Hom_{\Mon}(\sigma^{\vee}\cap M,(k,\cdot))$ 与 $\Hom(M,k)$ 不是一回事，后者是切空间。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §5 仿射环面簇，p.61–62（原书 p.61–62）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §6 k 有理点，p.62–62（原书 p.62）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §7 环面开子概形，p.63–63（原书 p.63）

关联：`siebert/concept/rational-polyhedral-cone`、`siebert/concept/monoid`、`siebert/concept/fan`、`siebert/concept/toric-variety`

来源说明：原书 p.61–64（Def 4.4、命题 4.3 环面理想、命题 4.4 k 值点、命题 4.5 基本开集、命题 4.6 正规性、引理 4.7 环面分层）。核过 nLab「toric variety」（2024-07-29：Idea 段把环面簇说成环面及其群概形结构的紧化）；nLab 无「affine toric variety」条目（实测 404），正规性与环面理想依原文。Stacks tag/033H（正规 ⇔ 各局部环为正规整环）用于核对「正规」的用法。
