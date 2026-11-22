# 第 7 章 通读笔记

Stephen S. Kudla, *From Modular Forms to Automorphic Representations*
原书印刷页 133–151（PDF 137–155；页图 `c07_p137.png`–`c07_p154.png` 覆盖印刷页 133–150，参考文献后半在 `work/en/ch08_raw.txt` 开头，印刷页 151）。

## 三句话主旨

1. 经典全纯尖点形式 $f\in S_k(\Gamma_0(N),\chi_N)$ 可以提升为 $G(\mathbb A)=GL_2(\mathbb A)$ 上的函数 $\phi_f$，它生成一个不可约容许 $(\mathfrak g,K_\infty)\times G(\mathbb A_f)$-模，即自守表示 $\pi=\pi(f)$。
2. 自守表示可以做局部–整体分解 $\pi=\otimes_v\pi_v$，而 Jacquet–Langlands 理论保证尖点谱是离散的、重数为 1，从而可以在表示论层面重新叙述新形式/老形式理论。
3. 由此得到 Langlands $L$ 函数 $L(s,\pi,r)$ 的欧拉乘积；对标准表示，Hecke 的经典理论就是它的一个特例。

## 逐节内容地图

**引言（印刷页 133）** 与 Tate 论文的 $GL_1$ 情形类比：局部–整体分解、本原特征对应新形式；指出 $GL_2$ 的表示是无限维的，需要非交换调和分析；交代参考文献（Jacquet–Langlands 1970 为基础）。

**§1 与经典尖点形式相联系的 $G(\mathbb Q)\backslash G(\mathbb A)$ 上的函数（pp.133–138）**
- 记号：$G_v$、限制乘积 $G(\mathbb A)=G(\mathbb R)G(\mathbb A_f)$、$K=\prod_p K_p$、对角嵌入的离散性；$SL_2$ 的强逼近定理。
- Lemma 1.1：若 $\det(K')=\widehat{\mathbb Z}^\times$，则 $G(\mathbb A)=G(\mathbb Q)G(\mathbb R)^+K'$，故 $G(\mathbb Q)\backslash G(\mathbb A)/K'\simeq\Gamma'\backslash G(\mathbb R)^+$；取 $K'=K_0(N)$ 得 $\Gamma'=\Gamma_0(N)$。
- (1.5) 自守因子 $j(g,\tau)=\det(g)^{-1/2}(c\tau+d)$；(1.6) $K_\infty^+$；(1.7) $j(zk_\theta,i)=\operatorname{sgn}(z)e^{-i\theta}$。
- (1.8)–(1.10) 由 $f$ 造 $\phi=\phi_f$，再用双陪集分解延拓到 $G(\mathbb A)$；Lemma 1.2 给出 $\Gamma_0(N)$-变换律与 $Z_\infty K_\infty$-变换律。
- 全纯性 $\Leftrightarrow$ $X_-\phi=0$：Lie 代数作用 (1.11)，$X_\pm$ (1.12)，$\operatorname{Ad}(k_\theta)X_\pm=e^{\pm2i\theta}X_\pm$ (1.13)，Maass 算子 $M_\pm$；Lemma 1.3。
- Proposition 1.4：$S_k(\Gamma_0(N),\chi_N)\simeq\mathcal A_0(G)(\mathrm{hol},k,N,\chi)$，三条公理 (i)(ii)(iii)，其中 (iii) 是尖点条件 (2.6) 的原型；(1.15) 把它化为 $f$ 在无穷远尖点常数项为零。
- Remark 1.5：中心特征 $\omega$，$\phi(zg)=\omega(z)\phi(g)$。Remark 1.6：用 $I=\operatorname{diag}(1,-1)$ 造 $\tilde\phi$、$\tilde f(\tau)=v^kf(-\bar\tau)$，把 $X_-$ 条件换成 $X_+$ 条件。

**§2 $\mathcal A_0(G)$ 上的表示（pp.138–143）**
- Definition 2.1：自守形式空间 $\mathcal A(G)=\mathcal A(G,\omega)$ 的六条公理（中心特征、光滑、$K_\infty$-有限、$K'$-不变、$\mathcal Z(\mathfrak g)$-有限、缓增）。
- Casimir 算子 (2.1)；范数 (2.2)–(2.4)；缓增条件 (2.5)。
- Definition 2.2：尖点条件 (2.6) 定义 $\mathcal A_0(G)$；由 (2.7) $C\phi=k(k-2)\phi$ 验证 $\mathcal A_0(G)(\mathrm{hol},k,N,\chi)\subset\mathcal A_0(G)$；指出 Eisenstein 级数给出非尖点的缓增元素。
- Definition 2.3：$(\mathfrak g,K_\infty)$-模、$(\mathfrak g,K_\infty)\times G(\mathbb A_f)$-模（光滑性）；Definition 2.4：容许、不可约；局部版本（实位与 $p$ 进位的定义）。
- Theorem 2.5：限制张量积的分解与还原（局部–整体原则）。
- Theorem 2.6：$\mathcal A_0(G)=\bigoplus_\pi\mathcal A_0(\pi)$；重数一（Jacquet–Langlands）；强重数一（Miyake、Casselman）；超强重数一（Ramakrishnan，密度 $<1/8$）。
- 讨论：$SL_n$（$n\ge3$）重数可以大于 1；证明 (i) 用 Fourier 展开与整体 Whittaker 函数。

**§3 局部表示论（pp.143–147）**
- $G=GL_2(F)$，$B=NM$，诱导表示 $I(\mu)$，模函数 $\delta(b)=|a_1/a_2|$；$I(\mu)\simeq I^K_{K\cap B}(\mu)$，中心特征 $\mu_1\mu_2$。
- Theorem 3.1：$I(\mu)$ 的不可约性判据 $\mu_1\mu_2^{-1}\ne\omega_{\pm1}$，以及 $\omega_{\pm1}$ 时的子/商表示 $\sigma(\mu)$；等价关系。
- Theorem 3.2：超尖点表示的两个等价刻画（$\operatorname{Hom}_G(\pi,I(\mu))=0$；矩阵系数模中心紧支）。
- 无分歧表示：$\mu_j(x)=t_j^{\operatorname{ord}(x)}$，$I(\mu)\simeq C^\infty(B\cap K\backslash K)$，$\dim I(\mu)^K=1$。
- Theorem 3.3：$\pi(t_1,t_2)$ 分类，唯一等价 $\pi(t_2,t_1)\simeq\pi(t_1,t_2)$。
- Iwahori 子群 $I$ 的注记；Corollary 3.4：Satake 参数 $t(\pi)$ 与 $G^\vee=GL_2(\mathbb C)$ 的半单共轭类。
- 球 Hecke 代数 $\mathcal H=\mathcal H(G,K)$，$\pi(\xi)v=\lambda_\pi(\xi)v$，$\mathcal H=\mathbb C[\xi_1,\xi_2]\simeq\mathbb C[t_1+t_2,t_1t_2]$。
- $K_0(r)$、$c(\omega)\le r$；Theorem 3.5（Casselman）：导子 $c(\pi)$ 与一维新向量空间 $V^{K_0(c(\pi)),\omega_\pi}$。
- 实位例子：离散序列模 $\mathrm{DS}_k$，$V=\bigoplus_{\ell\ge k,\ \ell\equiv k(2)}\mathbb C v_\ell$，$K_\infty$-作用、$X_\pm$ 作用 $\frac12(k\pm\ell)v_{\ell\pm2}$，$\pi_k(C)=k(k-2)$。

**§4 经典新形式（pp.147–149）**
- (4.1) 回到 $k=\mathbb Q$ 的同构；$p\nmid N$ 时 $\mathcal H_p$ 作用；与经典 $T_p,R_p$ 的关系 (4.2)，$\mathcal H^N=\otimes'_{p\nmid N}\mathcal H_p$ (4.3)。
- (4.4) $N(\pi)=\prod p^{c(\pi_p)}$；(4.5) 一维空间 $\mathcal A_0(\pi)^{\mathrm{new}}_{\mathrm{hol}}=\mathbb C\phi_0$，对应唯一的 $f_0$。
- (4.6) 特征值 $a_p=p^{(k-1)/2}(t_{p,1}+t_{p,2})$，$f_0|R_p=\chi(p)f_0$；(4.7) Hecke 多项式 $1-a_pp^{-(k-1)/2}X+\chi(p)X^2=\det(1_2-t(\pi_p)X)$。
- Theorem 4.1：$f_0(\pi)$ 是新形式；$S_k(\Gamma_0(N),\chi)^{\mathrm{new}}\simeq\bigoplus_{\omega_\pi=\omega,\pi_\infty\simeq\mathrm{DS}_k,N(\pi)=N}\mathcal A_0(\pi)^{\mathrm{new}}_{\mathrm{hol}}$；更一般 $N(\pi)\mid N$ 的版本 (iii)。
- 两条 Remarks：该定理可当作新形式的定义；Hecke 作用只涉及 $G(\mathbb A_f)$，故 Maass 形式同理。
- 收尾：$\phi$ 按 (iii) 分解即 $f$ 的新形式/老形式分解；$V(\phi)$ 不可约当且仅当 $f$ 是新形式。

**§5 自守尖点表示的 $L$ 函数（pp.149–150）**
- 有限位集 $S$，Satake 参数 $\{t(\pi_v)\}_{v\notin S}$；与 Galois 扩张的 Frobenius 共轭类类比。
- $L^S(s,\pi,r)=\prod_{v\notin S}\det(1-r(t(\pi_v))q_v^{-s})^{-1}$；两个基本问题：补全局部因子、建立解析性质与函数方程；标准表示由 Jacquet–Langlands 完成。
- Hecke 情形：$L^S(s,\pi,r)=\prod_{p\nmid N}(1-a_pp^{-s-\frac{k-1}{2}}+p^{-2s})^{-1}=L^N(s+\frac{k-1}{2},f)=\sum_{(n,N)=1}a_nn^{-s}$。

**参考文献** [1]–[19]（pp.150–151）。

## 体裁

综述性讲义章节：定义–定理–注记体，夹大量"读者可参阅"式文献指引；公式密集但证明全部省略（作者明说"sketches"）。译注应补足被跳过的计算（如 (1.15)、(2.7)、(4.7) 的验证），并说明归一化约定，不宜展开完整证明。

## 公式/记号风险点

1. **编号跳号**：原书从 (1.13) 直接到 (1.15)，(1.14) 号缺；中间 $X_\pm\phi(g_\infty k_\theta)=\phi(g_\infty)(e^{i\theta})^{k\pm2}$ 一行无编号。译文照旧，不加 (1.14)。
2. **(1.15) 的积分限**：第二个积分写作 $\int_{\mathbb Z\backslash\mathbb R}$，不是 $\int_{\mathbb Q\backslash\mathbb A}$；因 $\phi$ 对 $(1\ n;0\ 1)$（$n\in\mathbb Z$）不变，这一步合法，不是排印错误。
3. **(2.1) 的 $H$**：$H=-i\begin{pmatrix}0&1\\-1&0\end{pmatrix}$（右上 $1$、左下 $-1$、对角为空格）。若误读为 $-i\operatorname{diag}(1,-1)$，则 (2.9) 与 $\pi_k(H)v_\ell=\ell v_\ell$、$[X_+,X_-]=H$ 全部对不上。
4. **(2.5) 的 $f$**：原书作 $|f(g)|\le C\|g\|^n$，按上下文应为 $\phi$；译文照排并出注。
5. **定理 3.2 (ii) "module Z"**：应为 "modulo Z"（模中心），排印掉了字母 o。
6. **(1.5) 的 $\det^{-1/2}$ 与 (1.8) 的 $j^{-k}$**：只对 $\Gamma_0(N)\subset SL_2(\mathbb Z)$（$\det=1$）相消；换成 $GL_2^+$ 的一般元素会多出 $\det$ 因子。
7. **$\omega_\infty$ 在 $\mathbb R^\times_+$ 上平凡**（定义 2.1 前）：与 Lemma 1.2(ii) 的 $\operatorname{sgn}(z)^k$ 只在 $k$ 为偶数时相容；原书此处默认偶权，§1 却允许任意 $k$，需出注。
8. **$j(g,\tau)$ 的取值**：$g\in GL_2(\mathbb R)^+$，$c\tau+d$ 取主值分支；$j(zg,\tau)=\operatorname{sgn}(z)j(g,\tau)$ 依赖 $z\in\mathbb R^\times$ 的符号。
9. **$X_\pm$ 的矩阵**：$X_\pm=\frac12\begin{pmatrix}1&\pm i\\ \pm i&-1\end{pmatrix}$，两个 $\pm$ 同号；由此 $X_++X_-=\operatorname{diag}(1,-1)$。
10. **$q_v$**：$L$ 函数中 $q_v$ 是剩余域大小；$\mathbb Q$ 情形 $q_p=p$，故 (5) 末式指数 $p^{-s-\frac{k-1}{2}}$ 与 (4.7) 中 $p^{-\frac{k-1}{2}}$ 的配合要核对：$a_p$ 已是 $q$ 展开系数，故 $L$ 的局部因子写成 $1-a_pp^{-s-\frac{k-1}{2}}+p^{-2s}$。
11. **$L^N(s+\frac{k-1}{2},f)$**：这是"平移后"的 $L$ 函数记号，与 $L(s,f)$ 差一个平移；不要与 $L^S$ 的 $S$（位集）混淆，此处 $N$ 是级。
12. **$\mathrm{DS}_k$ 的权**：$V=\bigoplus_{\ell\ge k,\ \ell\equiv k(2)}\mathbb C v_\ell$ 是单侧（全纯）离散序列；$v_{-k}$ 也出现（由 $I$ 作用），故 $\ell$ 取绝对值 $\ge k$ 且与 $k$ 同奇偶。
13. **定理 4.1 (ii)(iii) 的下标条件**：$\omega_\pi=\omega$、$\pi_\infty\simeq\mathrm{DS}_k$、$N(\pi)=N$（或 $N(\pi)\mid N$）；(iii) 中上标 $K_0(N),\omega$ 指把 $N(\pi)$ 换成 $N$。
14. **$R_p$**：与 $\xi_{p,2}$ 对应的经典算子，特征值 $\chi(p)=t_{p,1}t_{p,2}$，即 $\det(p,p)$ 型双陪集算子；不要与 $T_p$ 混淆。
