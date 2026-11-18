---
id: dmod/concept/graded-dz-on-smooth
type: concept
track: C
---

# 光滑簇上的分次层 $\operatorname{Gr}\mathcal D_X$

> 光滑簇上主符号给出分次代数层同构 $\operatorname{Gr}\mathcal D_X\cong\pi_*\mathcal O_{T^*(X)}$，故 $\mathcal D_X$ 是局部自由层。

**问题**：为什么只有在光滑簇上才可以把 $\operatorname{Gr}\mathcal D_X$ 等同于余切丛上的多项式函数层，并由此得到 $\mathcal D_X$ 的局部自由性？

## 定义

设 $X$ 是特征零代数闭域 $k$ 上的光滑代数簇，$F\mathcal D_X$ 是阶数滤过。对 $T\in D_p(U)$ 定义 $\sigma_p(T)(f_1,\dots,f_p)=[[\cdots[[T,f_1],f_2],\dots],f_p]$，再令 $\operatorname{Symb}_p(T)(x,\omega)=\frac{1}{p!}\sigma_p(T)(f,\dots,f)(x)$，其中 $f$ 满足 $\mathrm df(x)=\omega$。这给出层同态 $\operatorname{Symb}:\operatorname{Gr}\mathcal D_X\to\pi_*(\mathcal O_{T^*(X)})$，$\pi:T^*(X)\to X$ 是余切丛投射；$\operatorname{Symb}$ 是分次 $\mathcal O_X$-代数层同构（定理 3.2）。

*记号*：$\pi:T^*(X)\to X$：余切丛投射；$\operatorname{Symb}_p$：$p$ 次主符号；$T^*(U)$：$U$ 的余切丛；$(x,\omega)$：余切向量。

## 要点

- $\operatorname{Symb}_p(T)$ 在 $T^*(U)$ 上正则，且在纤维 $T^*_x(X)$ 上是 $p$ 次齐次多项式（引理 3.1）。
- $\operatorname{Symb}:\operatorname{Gr}\mathcal D_X\to\pi_*\mathcal O_{T^*(X)}$ 是分次 $\mathcal O_X$-代数层同构（定理 3.2），乘性即 $\operatorname{Symb}_{p+q}(TS)=\operatorname{Symb}_p(T)\operatorname{Symb}_q(S)$（引理 3.3）。
- $\operatorname{Symb}_p(T)=0$ 当且仅当 $T$ 的阶数 $\le p-1$（引理 3.4），故主符号恰好编码最高阶项。
- $\mathcal D_X$ 是局部自由 $\mathcal O_X$-模，且在坐标卡上 $(D^I,|I|\le p)$ 是 $F_p\mathcal D_X(U)$ 的基（命题 3.5）。
- 光滑仿射 $X$ 上 $D(X)$ 左、右诺特，由 $R(X)$ 与整体向量场生成（定理 3.7），这是第三章凝聚性论证的前提。

## 关键公式

- $\operatorname{Symb}_p(T)(x,\omega)=\frac{1}{p!}\sigma_p(T)(f,\dots,f)(x)$
- $\operatorname{Gr}\mathcal D_X\cong\pi_*(\mathcal O_{T^*(X)})$
- $\operatorname{Symb}_p(T)=0\iff T\in F_{p-1}\mathcal D_X$
- $D^I\circ D^J=D^{I+J}$

## 定理与证明

### 引理 3.1（主符号的正则性与齐次性）（完整）

设 $T\in D_p(U)$。则 (i) 函数 $\operatorname{Symb}_p(T)$ 在 $T^*(U)$ 上正则；(ii) 对固定的 $x\in U$，它是 $T^*_x(X)$ 上的 $p$ 次齐次多项式。

1. 断言是局部的，由定理 2.10 可取 $U$ 充分小，使 $U$ 上存在坐标系 $(f_1,\dots,f_n;D_1,\dots,D_n)$，且 $(x,\xi_1,\dots,\xi_n)\mapsto(x,\sum_i\xi_i\mathrm df_i(x))$ 是 $U\times k^n\to T^*(U)$ 的同构。  
   *为什么*：坐标向量场给出余切丛的平凡化，把余切向量写成 $\sum_i\xi_i\mathrm df_i(x)$，才能在 $U\times k^n$ 上做计算。
2. 在该同构下 $\operatorname{Symb}_p(T)$ 等于 $(x,\xi)\mapsto\frac{1}{p!}\sigma_p(T)(\sum_i\xi_if_i,\dots,\sum_i\xi_if_i)(x)$，这是 $U\times k^n$ 上的正则函数。  
   *为什么*：$\sigma_p(T)$ 对 $R(U)$ 中元素是多重线性的，代入 $\xi$ 的线性组合后成为 $\xi$ 的多项式，系数是 $x$ 的正则函数。
3. 故 $\operatorname{Symb}_p(T)$ 在 $T^*(U)$ 上正则；又它在 $\xi$ 中是 $p$ 次齐次的，得 (ii)。  
   *为什么*：同构拉回保持正则性，$\xi\mapsto\lambda\xi$ 下表达式乘以 $\lambda^p$ 即齐次性。

*出处*：引理 3.1 / chap2.tex:584-595

### 命题 3.5（$\mathcal D_X$ 的局部自由性）（完整）

光滑簇 $X$ 上 $\mathcal D_X$ 是局部自由 $\mathcal O_X$-模（左乘、右乘）。更精确地，每点 $x$ 有仿射开邻域 $U$ 与坐标系 $(f_1,\dots,f_n;D_1,\dots,D_n)$，使 (i) $D^I\circ D^J=D^{I+J}$；(ii) $(D^I,|I|\le p)$ 是 $F_p\mathcal D_X(U)$ 的基；(iii) $(D^I)$ 是 $\mathcal D_X(U)$ 的基。

1. 取 $x$ 的邻域 $U$ 与坐标系 $(f_1,\dots,f_n;D_1,\dots,D_n)$（定理 2.10），则 $[D_i,D_j]=0$，故 $D^I\circ D^J=D^{I+J}$，得 (i)。  
   *为什么*：坐标向量场两两交换，才能把多重指标写成算子的幂并与交换律相容。
2. 记 $\xi_i=\operatorname{Symb}_1(D_i)$，则 $\pi_*(\mathcal O_{T^*(X)})(U)$ 以 $(\xi^I)$ 为基、齐次分量自由；由 $0\to F_{p-1}\mathcal D_X\to F_p\mathcal D_X\to\operatorname{Gr}_p\mathcal D_X\to0$ 与定理 3.2 对 $p$ 归纳，$F_p\mathcal D_X(U)$ 自由且由 $(D^I,|I|\le p)$ 生成。  
   *为什么*：分次化把「生成」逐阶提升为「自由基」：每一阶的齐次分量自由，扩张仍自由。
3. 若 $\sum_{|I|\le p}f_ID^I=0$，取 $p$ 次主符号得 $|I|=p$ 时 $f_I=0$，再对 $p$ 递降归纳得所有 $f_I=0$，故 $(D^I,|I|\le p)$ 是基，得 (ii)(iii)。  
   *为什么*：主符号只看见最高阶项，从最高阶往下逐层剥离即可证线性无关。

*出处*：命题 3.5 / chap2.tex:646-663

### 定理 3.2（主符号给出分次代数层同构）（要点（有缺口））

$\operatorname{Symb}:\operatorname{Gr}\mathcal D_X\to\pi_*(\mathcal O_{T^*(X)})$ 是分次 $\mathcal O_X$-代数层同构。

1. $\operatorname{Symb}_p$ 在 $F_{p-1}\mathcal D_X$ 上为零，故诱导 $\operatorname{Gr}_p\mathcal D_X$ 到 $\pi_*\mathcal O_{T^*(X)}$ 第 $p$ 次齐次分量的同态。  
   *为什么*：主符号只依赖最高阶项，这正是分次化的定义方式。
2. 逐阶验证该同态在坐标卡上是同构，从而 $\operatorname{Symb}$ 是分次代数层同构。  
   *为什么*：局部自由性（命题 3.5）把问题化到自由模上的秩比较。

> 缺口：讲义在 chap2.tex:605-644 给出完整证明；本卡只记录陈述，并只在命题 3.5 的证明中引用它。

*出处*：定理 3.2 / chap2.tex:601-644


## 易错点

- $\operatorname{Symb}_p$ 依赖于对阶数的假设：只有 $\operatorname{ord}T\le p$ 时它才由 $\operatorname{Gr}_p$ 良定义，$p$ 取得过小时无意义（引理 3.4 给出零的判据）。
- 该同构只在光滑簇上成立：按译者注（chap2.tex:566-568），只有光滑点处才有 $\operatorname{Gr}\mathcal D_X$ 的这种多项式描述，一般点必须退回 $\mathcal O_X$-凝聚语言。
- $\operatorname{Symb}$ 是分次层之间的同构，不是 $\mathcal D_X$ 与 $\pi_*\mathcal O_{T^*(X)}$ 的同构：分次化丢掉了低阶项，不能据此断言算子环本身可交换。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本，第 II 章 §3 光滑簇上的微分算子层，p.73（PDF p.79），`源码/chapters/chap2.tex:576-663（主符号与命题 3.5）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本，第 II 章 §2 译者注，p.62（PDF p.68），`源码/chapters/chap2.tex:566-568（光滑点处的分次结构）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/dz-structure-sheaf`
- `dmod/concept/smooth-point`
- `dmod/concept/characteristic-variety-sheaf`
