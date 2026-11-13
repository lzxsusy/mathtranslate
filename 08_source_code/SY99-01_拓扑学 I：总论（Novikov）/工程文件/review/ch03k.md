# 核验报告 · ch03k（原书 p.134–141）

核验人：译者丙　　作者：译者丁　　日期：2026-11-09

## 结论
需改（3 处「必须改」：一处脱字、两处脚注体例/人名与译名错误。公式部分质量很高：逐页核对 8 页，(9.9)–(9.20) 共 12 个编号连续无缺，无漏译、无跳译；几处易错处——(9.15) 原书印 $\CP^2$、(9.18) 的 $\alpha_{n-k}$ 递推、(9.20) 的 $y^{l_j}$——均照原文且批注到位。）

## 必须改（影响正确性）
1. **第 87 行**：「（关于 $J$-同态的定参见上文 §8 与第 4 章 §3。）」——「的定参见」脱字，应为「的定义参见」（原文 For the definition of the J-homomorphism, see §8 above, and Chapter 4, §3）。虽属笔误，但落在正文、读者会读不通，必须改。

2. **脚注体例：第 87 行脚注（注 14）与第 156 行脚注（注 15）**：二者在原书中均印作 *Translator's note*（p.136、p.138 页底原文可证），是英译本的译者注，不是我们译注本的译注。现译文写作「译者注：……」，会被读者误认为本书译者的批注。
   改法：两处均改为「原书英译者注：……」（lead 早已明确此统一措辞；本书其余块的英译者注均已如此标记，此处不一致）。

3. **第 159 行脚注（注 16）**：人名拼写错误——「Nadirazde」应为「Nadiradze」（Buchstaber, Ivanovskii, Nadiradze, Vershinin；原书 p.139 脚注放大可辨）。同句「为**单形**上配边环的 Adams–Novikov 谱序列计算提供了强有力的工具」有误：原书印作 *simplectic cobordism ring*，系 *symplectic* 的拼写笔误，实指**辛**上配边环 $\Omega_*^{Sp}$（本块 p.139 正文正讨论 $\Omega_*^{Sp}$ 的两值形式群计算），译作「单形（simplicial）」与上下文不符。
   改法：译作「辛上配边环」，并在括注或 Tutor Note 说明原书拼作 simplectic（应为 symplectic），符合补充规则④「照排原印 + 批注给理由」的精神；人名按 Nadiradze 拼写。

## 建议改（可读性/文风/排版）
1. **第 213–214 行**：页标记 `% [原文 p.141]` 插在人名「Gusein-Zade」的连字符处（`Gusein-% [原文 p.141]` / `Zade（约 1970 年代）`），把一个专名劈成两行。页标记位置本身没错（p.141 确从该词中间开始），但可读性差。
   建议：把「Gusein-Zade」整词移到页标记之后，页标记单独占一行（`例如，` 后换行写页标记，再起 `Gusein-Zade（约 1970 年代）完全描述了……`），不改变文字内容。
2. **第 69 行**「\emph{注}. 对任意环 $A$……」：原书是 *Remark.*，建议改用 preamble 的 `remark` 环境（参数 `{}`），与全书其他块的 Remark 排版统一；现在只有本块用 `\emph{注}`，印出来样式会与别处不一致。
3. **第 194 行**：「把空间 $S_j^{2n+1}/\Z/p\subset S_j^\infty/\Z/p$ 看作配边类 $\alpha(\ldots)$ 的代表」——原文是 *Consider the spaces … as representatives of the bordism classes*，主语是「空间即代表」；现译成「把空间看作……的代表」稍绕。建议改为「空间 $S_j^{2n+1}/\Z/p\subset S_j^\infty/\Z/p$ 就是配边类 $\alpha(\ldots)$ 的代表」。

## 抽查记录（逐页）
- **p.134**（`pages\p141.png`）：Hopf 代数的 Leibniz 性质、$S^*$ 作为 $S$ 上左（右）Milnor 模、$\rho_{\pm,a\otimes b}(x)=R_a^*(L_{s^{\pm1}b}^*(x))$、对极 $s$ 与转置代数 $S^t$、ad-模、Drinfeld 量子双；Buchstaber–Shokurov 把 $A^U$ 实现为形式微分同胚群上的微分算子代数、算子双、「Heisenberg 双」（Semenov–Tyanshanskii、Faddeev、Alexeev）——一致。
- **p.135**（`p142.png`）：(9.9) 三阶谱序列 $E_m^{p,q}$、$d_m:E_m^{p,q}\to E_m^{p-m,q+m-1}$、$d_m^2=0$、$E_{m+1}^{*,*}=H(E_m^{*,*},d_m)$；$E_2^{p,q}=\Ext_{A^U}^{p,q}(N,M)$、$G[K,L]_n^s=\sum_{p-q=n}E_\infty^{p,q}$、$\Ext_{A^U}^{0,q}\cong\Hom_{A^U}^q$；自由无环分解、对偶复形 $C^*=\Hom_{A^U}(C,M)$ 与 $C_n^{*,q}$ 的三重等式——逐符号一致。
- **p.136**（`p143.png`）：$\Ext_A^q(\Z,M)\cong H^q(K(\pi,1);M)$（原书带 □，译文用 `\hfill$\square$`，位置正确）；$K=S^0$ 情形 $M=\Lambda$、$N=\Omega_U^*(L)$、$E_2^{p,q}=\Ext_{A^U}^{p,q}(N,\Lambda)$；稳定范畴上广义上同调论的讨论（非 Grothendieck 阿贝尔范畴、$K$-理论无此类谱序列）；$E_2^{*,*}=\Ext_{A^U}^{*,*}(\Lambda,\Lambda)$、$\Ext_{A^U}^{1,*}$ 含 Kervaire–Milnor 下界——一致；脚注 14 见必须改 2。
- **p.137**（`p144.png`）：(9.10) 形式群公理两行、$\bar u=-u+\sum_{i\ge2}\mu_iu^i$ 与 (9.11) $f(u,\bar u)=0$、$g(u)=\sum\CP^n\frac{u^{n+1}}{n+1}$ 与 (9.12) $f(u,v)=g^{-1}(g(u)+g(v))$、$\psi^k(u)=\frac1kg^{-1}(kg(u))$ 与 (9.13) 三行；$\psi^k$ 在 $\Omega_U^*\otimes\Z[1/k]$ 中良定义——一致。
- **p.138**（`p145.png`）：$g_Q(u)=\sum Q(\CP^n)\frac{u^{n+1}}{n+1}=Q(g(u))$、$Q(z)=z/g_Q^{-1}(z)$；(9.14) $ch_U:\Omega_U^*(K)\to H^*(K;\Lambda\otimes\Q)$、(9.15) $ch_U(g(u))=t\in H^2(\CP^2;\Z)$——**原书确印 $\CP^2$**，译文照排并加 Tutor Note 说明，处理正确；Quillen/Lazard、$A^U\otimes\Z_{(p)}$ 的投影算子、$BP^*(\cdot)$、$\Omega_U^*\otimes\Q_p$ 分解——一致；脚注 15 见必须改 2。
- **p.139**（`p146.png`）：(9.16) $f_j:S_j^{2n-1}/\Z/p\to S_j^\infty/\Z/p=K(\Z/p,1)$、$w_j^T=(S_j^{2n-1}/\Z/p,f_j)$；$w_j^T=w_j^T(\lambda_1,\ldots,\lambda_n)$、$\lambda_q(A_j)=\exp(2\pi ix_{jq}/p)$、$x_{jq}\in(\Z/p)^*$；挖去邻域得自由作用 $\Rightarrow\sum_jw_j^T=0$；$p=2$ 时 $\Omega_{2n-1}^U(S_j^\infty/\Z/2)=\Omega_{2n-1}^U(\RP^\infty)$、$w_j^T=a_n$、$2^{n-1}a_n\ne0$、$2^na_n=0$、不动点数被 $2^n$ 整除——一致；脚注 16 见必须改 3。
- **p.140**（`p147.png`）：(9.17) $\alpha(x_{j1},\ldots,x_{jn})=\prod_{q=1}^n\frac{u}{g^{-1}(x_{jq}g(u))}\cap\alpha(1,\ldots,1)$（逐符号与页图一致，含末尾的 $\cap\alpha(1,\ldots,1)$）；$\Omega_U^*$ 与 $\Omega_*^U$ 两记号与原书印法一致（原书此处确为 $\Omega_U^*$ 与 $\Omega_*^U$，已放大核对，非笔误）；(9.18) $u^{n+2}=0$、$g^{-1}(pg(u))=0$、$Du^k=\alpha(\underbrace{1,\ldots,1}_{n-k})= \alpha_{n-k}\in\Omega_U^{2(n-k)+1}$、$\alpha_{n-k}\circ\alpha_{n-l}=\alpha_{n-k-l}$；(9.19) $\sum_{j=1}^m\alpha(\ldots)=0$；关于 $p>2$ 与 $S^1$ 作用的过渡——一致。
- **p.141**（`p148.png`）：$A_{(k)}=\frac{kue^u}{e^{ku}-1}$、$k\mid c_1(M^{2n})\Rightarrow A_{(k)}(M^{2n})=0$、$k=2$ 时 $A_{(2)}$ 与符号差重合；$S^1$ 作用的线性化特征值 $\lambda_{1j},\ldots,\lambda_{n-k,j}$、$\lambda_{qj}=\exp(2\pi in_{qj})$、负权个数 $l_j$、Hirzebruch 级数 $T_y(u)=\frac{(y+1)u}{1-\exp(-u(y+1))}-yu$、(9.20) $\sum_jy^{l_j}T_y(N_j^k)=T_y(M^{2n})$；$y=1$ 给符号差、$y=-1$ 给 Euler–Poincaré 示性数——逐符号一致；脚注 17（Witten、Taubes；Oshanine、Landweber；Baker–Akhieser）内容完整。

## 体例抽查
- 页标记：`% [原文 p.134]` … `% [原文 p.141]` 共 8 个，递增、无重复 ✓；无跨页句断点问题（本块 0 处跨页）。
- 编号：`\tag` (9.9)–(9.20) 共 12 个，与原书逐个对应、连续无缺、无自造 ✓；多行公式 (9.10)(9.16)(9.18) 用 `gathered` 单 tag，与原书右侧单个编号一致 ✓。
- 陈述：本块无编号定理/引理（原书亦然），仅 1 处 Remark（见建议改 2）✓。
- 结构：本块为 §9 续页，未写 `\section`（正确，§9 标题在 p.125 由 ch03j 写）✓；本块末为第 3 章正文结束，未误写章末标记。
- Tutor Note：5 条（要求 ≥ 8/3 = 2.7）✓；均为单行、无 `%` 字符。
- `% CHUNK ch03k DONE` 在末行 ✓。
- check_chunk：`python work\check_chunk.py src\chunks\ch03k.tex` 复跑 **0 error**（输出「OK」）。
