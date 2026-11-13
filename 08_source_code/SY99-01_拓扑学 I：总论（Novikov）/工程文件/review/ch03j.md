# 核验报告 · ch03j（原书 p.125–133）

核验人：译者丙　　作者：译者丁　　日期：2026-11-09

## 结论
需改（3 处「必须改」：两处静默改正原书笔误、一处符号照抄错。数学内容本身无误：逐页核对 9 页，编号 (9.1)–(9.8) 连续无缺，例 1–5 与原文对应，无漏译、无跳译。）

本块的问题集中在一类：**原书明显印错的地方，译文直接改成了正确写法而未保留原印**。这违反 STYLE_GUIDE 补充规则④（笔误正文照排 + Tutor Note 给理由）。此类改动看似「更好」，但会让读者对照原书时找不到来源，也失去了译注本「记录底本状况」的价值。

## 必须改（影响正确性）
1. **第 96 行，(9.3) 第一行**：原书 p.127 印作
   $\Omega_G^{m_1}(X)\cdot\Omega_G^{m_1}(X)\subset\Omega_G^{m_1+m_2}(X)$
   （第二个因子的上标确实是 $m_1$，已用 `python work\tools\crop.py 134 0.20 0.56 0.90 0.68 500` 放大页图确认，非扫描模糊）；现译文写作 $\Omega_G^{m_2}(X)$，属静默改正。
   改法：照印 $m_1$，并加 Tutor Note 说明判据——由下一行 $z_1\cdot z_2=(-1)^{m_1m_2}z_2\cdot z_1$ 与乘积次数 $m_1+m_2$ 可知第二个因子应为 $m_2$，故原书此处系笔误。

2. **第 157 行（例 3 末句）**：原书 p.129 印作「the adjoint ring $G\Omega_U^*(X)$ need not be isomorphic to $\Omega_U^*(X)$」，即下标是 $U$；现译文写作 $G\Omega_G^*(X)$。这是符号照抄错（本例通篇 $G=U$，$G\Omega_G^*$ 与上下文记号不符）。
   改法：改为 $G\Omega_U^*(X)$。

3. **第 300 行**：原书 p.133 印作 $\Lambda\subset X^*,\quad \Lambda\otimes\Q=S^*\otimes\Q$（已用 `crop.py 140 0.20 0.62 0.85 0.72 450` 放大确认，确为 $X^*$）；现译文静默改成 $\Lambda\subset S^*$。
   改法：照印 $X^*$，Tutor Note 给理由——本段讲 Landweber–Novikov 代数 $S$ 的对偶 Hopf 代数 $S^*$，「自然对偶 Hopf 代数……包含复配边环 $\Lambda$」指 $\Lambda\subset S^*$；$X^*$ 在本书记号中无定义，故系 $S^*$ 之误。批注中宜顺带点明「读作 $S^*$」，以免读者误以为 $X$ 是某个空间。

## 建议改（可读性/文风/排版）
1. **第 157 行「相伴环」**：adjoint ring 的译名建议与全书其余块核对一次（若别处作「伴随环」，统一其一；glossary 若无此条，报 lead 入库）。
2. **第 300 行修正为 $X^*$ 后**，该 display 是独立公式，建议在批注里补半句「此处 $X^*$ 应读作 $S^*$，见下段 $R_y^*$ 的定义」，与本块后文 $\Lambda\subset S^*$ 的用法呼应，避免读者以为是笔误之外的另一种结构。
3. **p.129 例 3 与例 1 的 □**：本块例 1–5 均按「原书有 □ → 无星 example」处理，抽查无误；建议作者复核例 3 的 □ 是否在 p.129 行末（若实际在 p.128 页末，页标记与 □ 的相对位置需再对一次）。

## 抽查记录（逐页）
- **p.125**（`pages\p132.png`）：§9 节标题与 `\takeaway` 由本块写（正确，节标题在 p.125）；配边论的几何定义——奇异 $n$-闭链 $(M^n,f)$、配边等价 $\sim$、$\Omega_n^O(X)$ 及其不交并群结构、相对群 $\Omega_n^O(X,Y)$；稳定群序列 $G=(G_n)$ 与基本例子 $G=O,SO,U,SU,Sp,e$、表示 $\rho:G\to O$、$Spin$ 二重覆叠——逐句一致。
- **p.126**（`p133.png`）：$G$-流形与「稳定法丛带 $G$-结构」；广义同调公理（同伦不变性、函子性、切除 $\Omega_n^G(X,Y)=\Omega_n^G(X/Y,*)$、正合列）；悬挂同构 $\Sigma:\Omega_n^G(X,Y)\cong\Omega_{n+1}^G(\Sigma X,\Sigma Y)$；上配边群 $\Omega_*^G$、上配边环、Thom 定理 $\Omega_m^G(*)\cong\pi_m^s(MG)$；(9.1) 一致。
- **p.127**（`p134.png`）：乘积 $M\Phi_{n_1,n_2}$ 的定义与 (9.2)；双线性、结合乘性两行 (9.3)——**第二行 $z_1z_2=(-1)^{m_1m_2}z_2z_1$ 与原书一致，第一行见必须改 1**；基本类 $[M^n]\in\Omega_n^G(M^n)$；卡积 $\Omega_G^m(X)\cap\Omega_k^G(X)\to\Omega_k^{G-m}(X)$ 一致。
- **p.128**（`p135.png`）：Poincaré 对偶 $D:\Omega_G^m(X)\cong\Omega_{N-m}^G(X)$、(9.4) 上配边环的交换性与乘性、例 1（上配边群作为同伦群的计算）、例 2、例 3 开头（$U$-上配边论、$G\Omega_U^*$ 记号）——一致。
- **p.129**（`p136.png`）：例 3 末句（Atiyah–Hirzebruch 谱序列何时退化，$G\Omega_U^*\ne\Omega_U^*$）——**见必须改 2**；例 4、例 5（$\Omega_*^U\otimes\Z_{(p)}$ 的 Novikov 结果、Conner–Floyd 的 $2$-挠结构）；辛上配边环 $\Omega_*^{Sp}$ 的挠为 $2$-挠、Ray 元 $\phi_j\in\Omega_{2j-5}^{Sp}$、Kochman/Vershinin/Botvinnik 的计算——一致。
- **p.130**（`p137.png`）：配边示性类——$W(X)$ 与几何上配边类 $[z]$、$f_z:X\to M(U_2)=\CP^\infty$、除子 $\{D[z]\}\subset\Omega_{2n-2}^U(M^{2n})$；(9.5) $\sigma(\eta_1\oplus\eta_2)=\sigma(\eta_1)\sigma(\eta_2)$、$\sigma(\eta)=1+\sigma_1(\eta)+\sigma_2(\eta)+\cdots$；(9.6) $s_\omega:\Omega_U^j(X)\to\Omega_U^{j+2|\omega|}(X)$、$\deg s_\omega=2|\omega|$、$|\omega|=\sum\omega_i$ 与乘积公式、$s_0=1$、$s_\omega a$ 的分段式——逐符号一致。
- **p.131**（`p138.png`）：$u_1\cdots u_n\in\Omega_U^{2n}(\CP_1^\infty\times\cdots\times\CP_n^\infty)$、复合公式 $s_{\omega'}\circ s_{\omega''}(u)=\sum\lambda_\omega(\omega',\omega'')s_\omega$、$s_\omega(u)=(\sum u_{i_1}^{\omega_1}\cdots u_{i_n}^{\omega_n})u_1\cdots u_n$；Landweber–Novikov 代数 $S$ 是 Hopf 代数、Milnor 模；$A^U=\{\sum_j\lambda_js_{\omega(j)}\}$、$\lambda_j\in\Omega_U^{-2q_j}=\Lambda^{-2q_j}$、分次 $A^U=\sum_{-\infty}^{\infty}A_{2n}^U$——一致。
- **p.132**（`p139.png`）：$s_\omega$ 在 $\Omega_U^*=\Lambda$ 上的显式作用——$\tau(\CP^n)+\varepsilon_\C^1=(n+1)\eta$、$\sigma_1(\eta)=u\in\Omega_U^2(\CP^n)$、$D(u)=[\CP^{n-1}]$、$\nu(\CP^n)=-(n+1)\eta$、$\sigma_j(-\eta)=(-1)^ju^j$、$Du^j=[\CP^{n-j}]$；对称多项式 $Q^\omega$、$P^\omega$ 与 $\sigma_\omega=P^\omega(\sigma_1,\sigma_2,\ldots)$；$\bar\sigma(-(n+1)\eta)=1/(1+u)^{n+1}$；(9.7) $s_\omega(\CP^n)=\lambda(\omega)[\CP^{n-|\omega|}]$——一致。
- **p.133**（`p140.png`）：(9.8) 两条 Novikov 公式（$s_\omega(\mu)$ 与 $s_\omega\circ\mu$ 的分裂求和，$\mu\in\Lambda$）、$s_0=1$、表示忠实性（$a$ 在 $\Lambda$ 上平凡作用则 $a=0$）；$A^U=(\Lambda\otimes S)^T$ 与「算子双」、Milnor 模、形式微分同胚上的微分算子实现；Buchstaber–Shokurov 的 $\Lambda\subset X^*$——**见必须改 3**；$R_b(a)=L_a(b)=ab$、$(R_y^*(z),x)=(z,R_y(x))=(z,xy)$ 一致。

## 体例抽查
- 页标记：`% [原文 p.125]` … `% [原文 p.133]` 共 9 个，递增、无重复 ✓（跨页句 1 处，整句归起始页处理得当）。
- 编号：`\tag` (9.1)–(9.8) 共 8 个，与原书逐个对应、连续无缺、无自造 ✓。
- 陈述环境：例 1–5 共 5 个，均为 `example`（无星，原书均带 □）✓；编号 1–5 连续，未出现重号。
- 结构：§9 节标题与 `\takeaway` 只在本块 p.125 写一次 ✓；本块无章标题（正确）。
- Tutor Note：4 条（要求 ≥ 9/3 = 3）✓；均为单行、无 `%` 字符。
- `% CHUNK ch03j DONE` 在末行 ✓。
- check_chunk：`python work\check_chunk.py src\chunks\ch03j.tex` 复跑 **0 error**（输出「OK」）。
