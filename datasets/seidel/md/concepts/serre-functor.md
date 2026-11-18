# Serre 函子

> `seidel/concept/serre-functor` ｜ track B ｜ draft

**一句话**：三角范畴上实现 Hom(X,Y)≅Hom(Y,SX)^∨ 的精确函子；Fukaya 范畴因 Poincaré 对偶带扭，只能以弱 Calabi–Yau 方式实现它。

**自测**：Fukaya 范畴为什么不是 Frobenius 范畴，而要用一个非恒等的 Serre 函子来补对偶？

## 定义

设 $\mathcal A$ 是 $k$-线性三角范畴，$\Hom$ 有限维。$\mathcal A$ 上的 Serre 函子是精确函子 $S:\mathcal A\to\mathcal A$ 连同自然同构
$$\varphi_{X,Y}:\Hom_{\mathcal A}(X,Y)\;\xrightarrow{\ \sim\ }\;\Hom_{\mathcal A}(Y,SX)^\vee,$$
且与复合相容：对 $g:W\to X$、$f:X\to Y$ 有 $\varphi_{W,Y}(f\circ g)=\varphi_{X,Y}(f)\circ Sg$。Serre 函子若存在，则在分次自然同构意义下唯一。
$A_\infty$ 情形：Seidel 用典范 $A_\infty$ 函子 $D:\mathcal A\to\mathrm{mod}.\mathcal A$，$D(Y)=Y^\vee$，$Y^\vee(X)=\hom_{\mathcal A}(Y,X)^\vee$，称 abstract Serre functor；若 Yoneda 嵌入 $I$ 到 $D$ 有 $-n$ 次同构，则称 $\mathcal A$ 为 $n$ 维弱 Calabi–Yau 范畴。

记号：$S$ 与平移 $[1]$ 交换；$\vee$ 表对偶空间；弱 CY 的「$-n$ 次」是相对 Yoneda 嵌入 $I\to D$ 而言。Donaldson–Fukaya 范畴 $\mathcal H F(M)$ 中 $S(X)=X\otimes\Lambda^{\mathrm{top}}TX\,[n]$，$n=\dim X$；$\xi_M$ 平凡时即 $[n]$。

## 要点

- Frobenius 范畴要求 $\Hom(X,Y)\cong\Hom(Y,X)^\vee$ 与复合相容；Serre 函子把右端的 $X$ 换成 $SX$，允许「对偶 $+$ 平移/扭」的缺陷，这正是非 Frobenius 情形需要的。
- 唯一性：两个 Serre 函子相差分次自然同构；故「Serre 函子」是范畴的内在数据，不是额外选择。
- CY 情形：$S=[n]$（$n=\dim X$）。光滑射影簇的 $D^b\mathrm{Coh}(X)$ 上 $S=(\cdot\otimes\omega_X)[n]$，$\omega_X\cong\mathcal O$ 时即 $[n]$。
- $\mathcal H F(M)$ 一般不是 Frobenius：Poincaré 对偶配对落在 $\Lambda^{\mathrm{top}}TL_0$ 的规范化上，只在 $\xi_M$ 平凡时可去掉 twist（p.180–181）。
- 弱 CY：不要求 $S$ 就是 $[n]$，只要求 Yoneda 嵌入到 abstract Serre 函子有 $-n$ 次同构；$\mathcal F(M)$ 的这个同构由带一个内部标记点的尖圆盘给出的自然变换实现（p.190）。

## 公式

$$\Hom_{\mathcal A}(X,Y)\cong\Hom_{\mathcal A}(Y,SX)^\vee$$
$$\int_{L^\#}:HF^n(L^\#,L^\#\otimes\Lambda^{\mathrm{top}}TL)\cong H^0(L;K)\longrightarrow K$$
$$HF^\bullet(L_1^\#,L_0^\#\otimes\Lambda^{\mathrm{top}}TL_0)\otimes HF^\bullet(L_0^\#,L_1^\#)\to K,\qquad \langle a_2,a_1\rangle=\int_{L_0^\#}a_2a_1$$
$$S_{D^b\mathrm{Coh}(X)}=(\cdot\otimes\omega_X)[n]$$

## 定理与证明

### Donaldson–Fukaya 范畴的对偶由 twist 实现

对 $\mathcal H F(M)$ 中任意 brane $L^\#$，配对
$$\langle a_2,a_1\rangle=\int_{L_0^\#}a_2a_1:HF^\bullet(L_1^\#,L_0^\#\otimes\Lambda^{\mathrm{top}}TL_0)\otimes HF^\bullet(L_0^\#,L_1^\#)\to K$$
非退化且分次对称：$\langle a_1,a_2\rangle=(-1)^{|a_1||a_2|}\langle a_2,a_1\rangle$。因此 $S(L_0^\#)=L_0^\#\otimes\Lambda^{\mathrm{top}}TL_0\,[n]$（$n=\dim L_0$）扮演 Serre 函子；当 $\xi_M$ 平凡时它约化为 $[n]$，$\mathcal H F(M)$ 退化为 Frobenius 范畴。

（sketch；来源：原书 p.180 (12.15)）

1. PSS 同构给 $HF^\bullet(L^\#,L^\#)\cong H^\bullet(L;K)$；Poincaré 对偶给 (12.15)：$HF^n(L^\#,L^\#\otimes\Lambda^{\mathrm{top}}TL)\cong H^0(L;K)\to K$。  
   为什么：twist 上 $\Lambda^{\mathrm{top}}TL$ 后 $n$ 次 Floer 上同调对偶到 $H^0$，积分即增广映射。
2. 三角积 $HF^\bullet(L_1^\#,L_0^\#\otimes\Lambda)\otimes HF^\bullet(L_0^\#,L_1^\#)\to HF^n(L_0^\#,L_0^\#\otimes\Lambda)\to K$ 与复合相容。  
   为什么：复合的结合性 (12.11) 与第 1 步的增广映射给出配对，且对第二个因子的复合自然。
3. 非退化：若 $a_2\ne0$，存在 $a_1$ 使 $\langle a_2,a_1\rangle\ne0$。  
   为什么：第 1 步把配对化为 $H^\bullet(L;K)$ 上的杯积配对，后者由 Poincaré 对偶非退化。
4. 分次对称性：交换 $a_1,a_2$ 时把 $\Lambda^{\mathrm{top}}TL_k\cong\xi_M|_{L_k}$ 的扭转移到另一侧，得符号 $(-1)^{|a_1||a_2|}$。  
   为什么：Floer 乘积的分次交换性加上 twist 线丛的交换（次数 $0$）给出该符号。

缺口：原书 p.180–181 只陈述 (12.15) 与「非退化、分次对称」，非退化性的分析细节（横截性、PSS、定向）散在 §12a–§12d，此处为骨架。

### abstract Serre 函子与弱 Calabi–Yau 性质

对任意 $A_\infty$ 范畴 $\mathcal A$，$D(Y)=Y^\vee$（$Y^\vee(X)=\hom_{\mathcal A}(Y,X)^\vee$）是 $A_\infty$ 函子 $D:\mathcal A\to\mathrm{mod}.\mathcal A$，称 abstract Serre functor；若 Yoneda 嵌入 $I\to D$ 有 $-n$ 次同构，则称 $\mathcal A$ 为 $n$ 维弱 CY 范畴。当 $\mathcal A=\mathcal F(M)$ 且 $\xi_M$ 平凡时该同构存在。

（sketch；来源：原书 p.189–190 §12j）

1. 对每个 $Y$，$Y^\vee(X)=\hom_{\mathcal A}(Y,X)^\vee$ 带 $A_\infty$ 右模结构：结构映射由 $\hom$ 的 $A_\infty$ 运算对偶化得到。  
   为什么：对偶化把 $A_\infty$ 运算的顺序反转，正是一个右模所需的相容性。
2. Yoneda 嵌入 $I(Y)(X)=\hom(X,Y)$ 与 $Y^\vee$ 之间的自然变换对应 $\HH(\mathcal A,\mathcal A^\vee)$ 中的一个类。  
   为什么：双边模之间的态射就是 Hochschild 上链，$I$ 与 $D$ 都是 $\mathcal A$-双边模。
3. $\mathcal A=\mathcal F(M)$ 时该类由「带一个内部标记点的尖圆盘」给出（§10c 风格）；同构性由 Lemma 1.6 与 Floer 上同调的 Poincaré 对偶得到。  
   为什么：内部标记点给出开弦真空的自然变换，逐对象上由 Poincaré 对偶保证可逆。

缺口：原书 §12j（p.189–190）只勾画该论证；Hochschild 类与圆盘模空间的对应细节在 §10c，本卡未展开。

## 易错点

- Serre 函子不是「对偶函子」：$S$ 是范畴到自身的精确函子，对偶只是 $\Hom$ 的同构；把 $S$ 与 $\vee$ 混同会丢掉平移与 twist。
- $n$ 的次数约定不统一：Serre 函子与 $[1]$ 交换，弱 CY 的「$-n$ 次」是相对 Yoneda 嵌入而言；不同文献用 $[n]$ 或 $[-n]$，相差一个平移。
- $\mathcal H F(M)$ 的 twist 是 $\Lambda^{\mathrm{top}}TL$ 而非 $\Lambda^{\mathrm{top}}TM$，次数是 $n=\dim L$ 而非 $\dim M$；$\xi_M$ 平凡时才可去掉 twist。
- 非退化配对的存在不自动给 Frobenius 结构：还要与复合严格相容；$\mathcal H F(M)$ 一般只在弱 CY 意义下满足，且原书只断言 $\xi_M$ 平凡时退化为 Frobenius，未断言反之。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§12e，p.180–181（原书 p.180 §12e）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§12j，p.189–190（原书 p.189 §12j）

关联：`seidel/concept/fukaya-category`、`seidel/concept/brane-structure`、`seidel/concept/determinant-line`、`seidel/concept/exact-triangle`

来源说明：据原书 §12e（p.180–181）与 §12j（p.189–190）转述；译者注 A07-04。外部：nLab「Serre functor」https://ncatlab.org/nlab/show/Serre+functor，支持句「A Serre functor on a triangulated category A is an exact functor such that for any pair of objects there is a natural isomorphism Hom(A,B) ≃ Hom(B,S(A))^*」；例「on the derived category of coherent sheaves … (·⊗ω_X)[n]」，CY 时 $\omega_X\cong\mathcal O$ 即 $[n]$。
