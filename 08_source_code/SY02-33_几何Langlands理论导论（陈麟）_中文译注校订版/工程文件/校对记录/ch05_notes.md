# ch05《Fourier 变换》待注点（原 PDF p32 下–p36）

## 待注 ch05.tex:8（原 PDF p32）

- 原文：Equivalently, this is the compactified global version of the positive Hecke correspondence fibered with the ρ-twisted Whittaker stack
- 概念：ρ 是半和正根；ρ-扭曲（ρ-shift）是把 Whittaker 层沿 $\Bun_N$ 的连通分支按 $2\rho$ 作 Tate 扭转，使 $p_2^*\cL_\psi$ 在 Hecke 对应下带正确的中心特征；"紧化后的整体版本"指把旗、挠商、Whittaker 三层数据捆在一起，而非 $\mathrm{Gr}\times\Bun_N$ 的直积。
- 读者缺什么：$\rho$ 在书中未定义；读者不知道 twist 是对 $\Bun_N$ 的哪个作用做的、为何不扭曲就与 $p_1,p_2$ 不相容，也不知道非紧化版本丢掉的正是挠缺陷。
- 建议来源：原书文献 [Gai18]

## 待注 ch05.tex:26（原 PDF p33）

- 原文：with this normalization it is t-exact for the perverse t-structure and preserves irreducibility on simple perverse sheaves
- 概念：$[r]$ 是相对维数 $r=\dim V-\dim S$ 的移位，$(r/2)$ 是 Tate 扭转；二者合起来把 $p^\vee_!$ 与 $p^\vee_*$ 的 Verdier 对偶拉平，故 $\mathsf F_{V/S}$ 对反常 t-结构 t-正合。
- 读者缺什么：为何恰好取 $r$ 与 $r/2$、$r/2$ 为半整数时 Tate 扭转如何定义（需系数含 $\sqrt q$，书中用 $\Qbar_\ell$），以及 t-正合为何就能保证单反常层的像仍单。
- 建议来源：nLab "Tate twist"

## 待注 ch05.tex:49（原 PDF p34）

- 原文：If j! = j!∗ = j∗, then j!q∗LE is a simple perverse sheaf.
- 概念：中间延拓 $j_{!*}$（IC 层）与单性判据：$j_!=j_{!*}=j_*$ 表示 $j$ 的两侧延拓重合，边界上无 $!$-或 $*$-亏损，"洁净延拓"于是就是中间延拓。
- 读者缺什么：$j_{!*}$ 在此首次出现，前文只说"洁净延拓"；读者不知道 $j_{!*}$ 的定义，也不知道单性还要靠 $q^*\cL_E$ 本身单（$q$ 光滑、$\cL_E$ 单）。
- 建议来源：nLab "intermediate extension"

## 待注 ch05.tex:63（原 PDF p34）

- 原文：for E geometrically irreducible of rank n > 1 (or nontrivial of rank 1), d > n(2g − 2) ⇒ AJ^d_!(E^(d)) = 0
- 概念：Deligne 的 Abel–Jacobi 消失定理。$X^{(d)}$ 是 $d$ 次对称积（维数 $d$），$E^{(d)}$ 是 $E^{\boxtimes d}$ 的 $S_d$-不变部分，$\AJ^d:X^{(d)}\to\Pic^d$；$d>n(2g-2)$ 时 $R\Gamma_c$ 消失。$n=1$ 非平凡即经典 AJ 消失。
- 读者缺什么：定理只报名；读者不知道界 $n(2g-2)$ 来自 $\deg E^{(d)}$ 与 $\AJ^d$ 纤维维数的比较，也不知道 $n>1$ 时必须"几何不可约"是为了排除来自子局部系统的分量。
- 建议来源：原书文献 [KL85]

## 待注 ch05.tex:98（原 PDF p35）

- 原文：The input for cleanness is Gaitsgory's vanishing theorem for averaging functors [Gai04, Gai16b].
- 概念：平均函子 $\Av_E^d=\overrightarrow h_!(\overleftarrow h^*(-)\otimes\pi^*\cL_E^d)[dk](dk/2)$ 的消失：$\rank E>k$、$d>(2g-2)k\rank E$ 时 $\Av_E^d=0$；$k=1$ 即 Deligne 的 AJ 消失。
- 读者缺什么：只说"输入"；读者看不出 5.7.2 的界 $d>nk(2g-2)$ 与一般界 $d>(2g-2)k\rank E$ 在 $\rank E=n$ 时正好一致，也不清楚该定理在证明链条中只负责"挠部分为零"。
- 建议来源：原书文献 [Gai04]
