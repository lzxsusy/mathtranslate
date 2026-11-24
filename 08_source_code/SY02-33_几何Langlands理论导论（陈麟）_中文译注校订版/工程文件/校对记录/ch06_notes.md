# ch06《洁净性》待注点（原 PDF p37–p40）

## 待注 ch06.tex:27（原 PDF p36）

- 原文：The functor F_{C̄′k/Ck} is the Fourier–Deligne transform between the dual vector bundles over Ck.
- 概念：相对 Fourier–Deligne 变换：在 $C_k$ 上的一对对偶向量丛（$\mathcal E_{k+1}\to C_k$ 与 $\overline C'_k\to C_k$）之间逐纤维做 §5.2 的变换，并与底空间拉回相容；归一化沿用 $[r](r/2)$。
- 读者缺什么：§5.2 只对单个向量丛 $V\to S$ 定义了绝对变换，读者不知道"相对"版本的函子性如何给出、为何先 $j_{k,!}$ 延拓再变换，也不知道为何只保留 $\mathcal E^{\ne0}_{k+1}$（去掉零截面）。
- 建议来源：原书文献 [KL85]

## 待注 ch06.tex:51（原 PDF p37）

- 原文：The sheaf is monodromic for the dilation action on the fibers. ... The contraction principle gives i!jk,!Fk ≃ q!jk,!Fk.
- 概念：monodromic 指沿 $\Gm$ 在纤维上的伸缩作用是"轨道局部常值"的；收缩原理把向量丛沿该 $\Gm$-作用缩到零截面，于是 $i^!j_{k,!}\simeq q_!j_{k,!}$。
- 读者缺什么：只给结论；读者不知道 monodromic 正是 contraction principle 的适用前提，也不知道这里为何用 $!$-拉回（要的是紧支撑边界项，Verdier 对偶后才换成检验 $i^*j_{k,*}F_k=0$）。
- 建议来源：原书文献 [Gai04]

## 待注 ch06.tex:59（原 PDF p37）

- 原文：Let Wk be the base Whittaker sheaf, i.e. the direct image of expψ from BunNk to Bunk with the same shift and twist.
- 概念：$\Bun_{N_k}$ 上的 Whittaker 层（指数层，依赖加法特征 $\psi$，记作 $\cL_\psi$ 或 $\exp_\psi$）沿 $\pi:\Bun_{N_k}\to\Bun_k$ 的直像，配以与 $F_k$ 相同的移位与 Tate 扭转；它是归纳中"基础层"的模型。
- 读者缺什么：$\exp_\psi$ 与 $\cL_\psi$ 是同一对象的不同记法，读者易当作两个层；也不知道为何取直像而非 $!$-直像（Whittaker 层在 $\Bun_{N_k}$ 上非紧支撑）。
- 建议来源：原书文献 [Gai18]

## 待注 ch06.tex:76（原 PDF p38）

- 原文：Without the section, this is the usual presentation of the torsion-ℓ stratum of Cohk by modifications of vector bundles; the relative tangent is Hom(M˚, T)
- 概念：用向量丛的修改（modification）表现挠层：取 $\mathring M\in\Bun_k$、$\mathcal T\in\Tor^\ell$ 与扩张 $0\to\mathring M\to M\to\mathcal T\to0$ 后忘去典范截面；$\widetilde Y\to Y_\ell$ 在挠长度 $\ell$ 的层上光滑，相对切空间为 $\Hom(\mathring M,\mathcal T)$，相对维数局部常值。
- 读者缺什么："presentation by modifications"未定义；读者不知道它与 §6.3 的 $C'_k$（带截面）如何相容，也不知道光滑性为何只要求在这一分层上。
- 建议来源：nLab "affine Grassmannian"

## 待注 ch06.tex:122（原 PDF p40）

- 原文：The needed proposition is the factorization identity, in the quotient-stack normalization used for Tor, (s, q)!m∗LE ≃ LE ⊠ LE, which is proved in Section 7.
- 概念：Laumon 因子化恒等式：$\cL_E$ 在 $\Tor$ 上对"粘合"$(s,q)$ 的乘性，配以 $\Tor$ 所用的商叠归一化；它把挠商拆成 $M'/M_k$ 与 $\mathcal T/\mathcal T'$ 两部分，从而把非满射情形归约到满射情形。
- 读者缺什么：只报名并推到第 7 章；读者不知道 $(s,q)$ 与 $m$ 的定义（粘合映射与外乘法），也不知道"商叠归一化"指 $\Tor$ 的哪个群约化，因而看不出它为何正好给出这一拆解。
- 建议来源：原书文献 [Gai04]
