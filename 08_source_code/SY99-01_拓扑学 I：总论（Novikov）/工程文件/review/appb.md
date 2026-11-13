# 核验报告 · appb（原书 p.283–291，附录 §2 续、§3 Vassiliev 不变量、§4 开头）

核验人：译者戊　　作者：译者辛　　日期：2026-11-10

## 结论
通过。逐页核对 9 页（`pages\p290.png`–`p298.png`）：§2 末段、§3 与 §4 两个节标题、2 条本节重点、9 条 Tutor Note、4 张裁图（图 A.8–A.12）与全部公式均与原书逐个符号对得上，**没有必须改的条目**。只有 2 条建议（一处人名拼写照原加注、一处节标题分行）。

## 必须改（影响正确性）
无。

## 建议改（可读性/忠实度）
1. **第 205 行附近（原书 p.288）**：Tait 段把 "Thompson (Lord Kelvin)" 照原书写作「Thomson（开尔文勋爵）」；原书确实排作 Thompson（通行为 Thomson）。与 Calaby--Yau、Dijgraaf 的处理保持一致，建议在段末 Tutor Note 里补一句「原书把 Thomson 排作 Thompson」，或照原印 Thompson 并在注里说明。
2. **第 312 行（§4 标题）**：原书标题分两行排印（"New topological invariants for 3-manifolds." 换行 "Topological Quantum Field Theories"），`\section` 里现写作「3 维流形的新拓扑不变量与拓扑量子场论」；建议改为「3 维流形的新拓扑不变量。拓扑量子场论」，与 §2 标题用「。」分句的做法一致（`\section` 内可用「。」断句，不必用换行）。

## 抽查记录（逐页）
- **p.283**（`pages\p290.png`）：Markov 性质 $\Tr[\rho_n(a)]A=\Tr[\rho_{n+1}(a\sigma_{n+1})]$ 与 $A^{-w(a)}\Tr[\rho_n(a)]$（$a=\sigma_{i_1}^{j_1}\cdots\sigma_{i_m}^{j_m}$，$w(a)=\sum_{k=1}^m j_k$）；标架 $R_{cd}^{ab}$、$\bar R_{kl}^{ij}$、总张量缩并 $\langle D\|R,\bar R\rangle$；通道/交叉通道幺正性 $\bar R_{ij}^{ab}R_{cd}^{ij}=\delta_c^a\delta_d^b$、$R_{jb}^{ia}\bar R_{ic}^{jd}=\delta_c^a\delta_d^b$；$R_{ad}^{ab}=A\delta_d^b$、$\bar R_{ad}^{ab}=A^{-1}\delta_d^b$；Yang–Zamolodchikov 解释与「谱参数」段——一致（本页后半已与 p.284 合并，页标记合规）。
- **p.284**（`p291.png`）：杯/帽矩阵 $M^{ai}M_{ib}=\delta_b^a$；$\bar R_{cd}^{ab}=M_{ce}R_{dh}^{ea}M^{hb}$ 与幺正性；包围 $n$-辫的圆柱 $x^2+y^2\le1$、$0\le z\le1$、$P_1,\dots,P_n$ 与 $Q_1,\dots,Q_n$；图 A.8（$R_{ab}^{ab}$、$\bar R_{ab}^{ab}$、$M^{ab}$、$M_{ab}$）；闭辫与 Markov 迹 $\tau(D)=\Tr[\eta\otimes\cdots\otimes\eta\,\rho_n(B)]$、$\eta_a^b=M_{ai}M^{bi}$；显式解 $R_{cd}^{ab}=AM^{ab}M_{cd}+A^{-1}\delta_c^a\delta_d^b$——一致。
- **p.285**（`p292.png`）：图 A.9（闭辫的平面图与圆柱内闭辫，原书圆柱上端标 $z=0$、下端标 $z=1$，Note 已说明）；$i^2=-1$、$M=\begin{pmatrix}0&iA\\-iA^{-1}&0\end{pmatrix}$；$J(A^4,A^{-4})=(-A)^{-3w(D)}\tau(D)$；定向图情形 $R_{cd}^{ab}=\bigl((q-q^{-1})[a<b]+q[a=b]\bigr)\delta_c^a\delta_d^b+[a\ne b]\delta_d^a\delta_c^b$、$I=I_n=(-n,-n+2,\dots,n)$；$\bar R$ 的代换 $q\mapsto q^{-1}$、$a,b\mapsto -a,-b$；$P_D^{(n)}=(q^{(n+1)})^{-w(D)}\langle D\parallel R,\bar R\rangle$；HOMFLY 取 $y=q^{n+1}$、$q=t^{1/2}$ 得 Jones；tangle 定义（$I=(-,+)$、割开外部边）——一致。
- **p.286**（`p293.png`）：Jaeger–Kauffman 的 $R=(q-q^{-1})X_{+-}+qX_{++}-q^{-1}X_{--}+Y$、$(X_{sp})_{cd}^{ab}$、$Y_{cd}^{ab}=[a\ne b]\delta_d^a\delta_c^b$（$a,b,c,d=\pm1$）；Burau 表示 $\rho(\sigma_i)=\operatorname{diag}(1,T,1)$、$T=\begin{pmatrix}0&t\\1&(1-t)\end{pmatrix}$、$A_{D_a}=(\det)^*(\rho(a)-1_n)$ 与「差 $\pm t^m$」；外幂恒等式 $\det(M-\lambda 1_n)=\sum_{j=0}^{j=n}\Tr((-\lambda)^k\Lambda^kM)$（原书 $j/k$ 混用，Note 正确）；Hecke/Temperley–Lieb(Jones)/Birman–Wenzl 三代数引入——一致。
- **p.287**（`p294.png`）：Hecke 关系 $\sigma_i-\sigma_{i-1}=z$（原书下标笔误，Note 正确）；TL 的 $v_iv_j=v_jv_i$、$v_iv_{i\pm1}v_i=v_i$、抽象迹 $f:TL\to\Z[A,A^{-1}]$、$f(uv)=f(vu)$、$\rho(\sigma_i)=av_i+b$；Jones 代数 $e_i=\delta^{-1}v_i$、$-\delta=A^2+A^{-2}$、$e_i^2=e_i$；Birman–Wenzl $\sigma_i-\sigma_i^{-1}=z(v_i-1)$；量子群段（Drinfeld、Jimbo、Sklyanin、Kulish、Faddeev、Takhtadjan、Reshetikhin、Voronovich；Hopf 代数、量子双、包络代数的量子形变）；Poisson 括号与「量子化」辨析——一致。
- **p.288**（`p295.png`）：量子群术语评论与 Landau 研究所轶事；项圈段（19 世纪末 Tait、Maxwell/Thompson）；交错纽结与不可约图（图 A.10，$K_1\#K_2=K$）；Kauffman–Murasugi 定理：不可约交错图的交叉数是拓扑不变量，且交叉数 $=$ Jones 多项式中 $t$ 的最高次幂与最低次幂之差；「经典拓扑方法显得不足」的评论——一致（建议改 1）。
- **p.289**（`p296.png`）：带状纽结（ribbon knot）$A(t,t^{-1})=f(t)f(t^{-1})$ 与 $f(t)$ 的存在性；§3 标题 "Vassiliev Invariants" 位置正确；$F_k$（恰有 $k$ 个二重点的浸入 $G_k:S^1\to\R^3$，$P_i,\bar P_i$）、扰动得 $G_{k-1}^{\pm}$（图 A.11）；$f_k:\pi_0(F_k)\to A$；Vassiliev 导数定义 $f_{k-1}(G_{k-1}^+)-f_{k-1}(G_{k-1}^-)=f_k(G_k)$；$k$-不变量（第 $(k+1)$ 阶导数为零）；Bar–Natan（Alexander 系数皆为 Vassiliev 不变量）、Bar–Natan–Lin–Birman 的 HOMFLY 代换 $y=\exp(Nx)$、$x=\exp(z/2)-\exp(-z/2)$——一致。
- **p.290**（`p297.png`）：HOMFLY 作为 $z$ 的幂级数的系数是 Vassiliev 不变量；Kontzevich 多重积分公式的背景与「通有 Morse 函数」；组合刻画：弦图（$2k$ 个点 $P_j,Q_j$，只看圆周上的循环次序）、关系 1（含与任一对都不「相链」的点对者为 0）、关系 2（$C_+$：$A_2=Q_{k-1}$、$A_3=Q_k$；$C_-$：$A_2=Q_k$、$A_3=Q_{k-1}$）、$C_+-C_-$ 与三点选取无关；图 A.12（图 $U$）与商群 $B_k$——一致。
- **p.291**（`p298.png`）：$B=\sum_{k\ge0}B_k$ 按弦图连通和构成分次 Hopf 环；Kontzevich 公式 $Z(K)=\sum_m\frac1{(2\pi i)^m}\int\cdots\int_{t_{\min}<t_1<\cdots<t_n<t_{\max}\parallel AS}(-1)^{N\downarrow}\prod_j d\log(z_j-z_j^1)D_N$（$N\downarrow$ 为关于 $t$ 的降弦数；$\sum_s m_s=m$；$s=s_K$ 为极小点数；$\gamma=Z(U)$）；$\gamma^{-s}Z(K)$ 是拓扑（Vassiliev）不变量；§4 标题与 Witten 泛函积分的引入（$Z(M^3)=\int DA\exp\{ikS(A)\}$ 在下一页）——一致（建议改 2）。

## 体例抽查
- 页标记：`% [原文 p.283]`…`% [原文 p.291]` 共 9 个，递增、无重复 ✓；经 tr-ding 判据扫描后，p.284、p.288、p.290 三处跨页句中标记已由作者/核验人合并句段并移到句末（现均合规）。
- 公式：本块原书无可编号公式，全部用无编号 `\[ \]` ✓；无自造编号，`tag 0` ✓。
- 图：A.8–A.12 五张裁图齐全（`src\figures\figA8.png`–`figA12.png`），裁图不含原书图题，`\figtitle` 中文另写 ✓。
- 陈述：Vassiliev 不变量定义段、TQFT 引入段等无编号内容处理为普通段落，未滥造环境 ✓。
- Tutor Note：9 条（要求 ≥ 3）✓，单行、无 `%` 字符 ✓。
- `% CHUNK appb DONE` 在末行 ✓。
- check_chunk 复跑：页 283..291、tag 0、陈述 0、Note 9、本节重点 2、OK（0 error）。

## 修正记录
- 2026-11-10：核验人按 lead 授权，仅动页标记行；本块 3 处跨页标记（p.284、p.288、p.290）由作者 tr-xin 与 tr-ding 先后合并句段、移到句末，复查合规；核验人未改动正文。
- 2026-11-10：Dijgraaf 拼写（appc，不属本块）另见 review/appc.md。
