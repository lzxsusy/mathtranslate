# 核验报告 · ch04b（原书 p.153–164）

核验人：译者丙　　作者：译者丁　　日期：2026-11-09

## 结论
小改（正文与公式全部正确：逐页核对 12 页，编号 (1.18)–(1.36) 连续、与原书逐式对应；规范变换、平行移动、协变微分、示性类定义、$BG$ 与上同调环、Chern/Pontryagin/Stiefel–Whitney 类、加法与乘法特征标、Euler 类、六个例子均无实质错误。必须改 2 条：图 4.3 裁图不完整、1 处页标记仍在句中。建议改 2 条。）

## 必须改（影响正确性）
1. **图 4.3 裁图不完整**（`src/figures/fig4_3.png`，第 59–62 行引用）：下缘被裁掉，原书 p.154 图中下方那条道路曲线只露出上半截，右下角的 $\gamma(t)$ 标注被切掉一半。按补充规则⑦「裁完 read_image 自检」，须重裁：下边界要包含完整的下方曲线与 $\gamma(t)$ 标注，上边界含 6 条竖线状纤维与 $\tilde\gamma(t)$，但**不得含** `Fig. 4.3` 题注行。
2. **第 385 行页标记仍在句中**：第 384 行以「（其中 $i^*$ 由包含 $i:M^n\to N^k$ 诱导），于是」结尾，`% [原文 p.164]` 紧接其后、再接公式块，把一个句子劈开。按 lead 新规须移到句子结束之后再放；本句（含后续三行公式与「最后一式对复 $U_n$-流形 $M^n\subset N^k$ 成立。」）是跨页句，建议把标记移到「……成立。」之后，并在回执注明页界归属。

## 建议改（可读性/文风/排版）
1. **第 169 行**：「自然同态 $H^*(BO_n;\Z/2)\to H^*(BSO_n;\Z/2)$ 是满的（即满同态）」——「满的」与「满同态」重复，建议改为「是满同态（$epimorphism$）」。
2. **图 4.5 的图题**（第 362 行）：原书 `Fig. 4.5` 只有图形、无题注文字，译文自拟「射影平面 $\RP^2$ 中的射影直线 $\RP^1$」可以保留，但图中实际画的是一条阴影带（$\RP^1\subset\RP^2$ 即 Möbius 带），建议补「（图中阴影带）」或「即 $\RP^2$ 中的 Möbius 带」，便于读者与图对照。

## 抽查记录（逐页）
- **p.153**（`pages\p160.png`）：(1.18) $\phi_U\psi_U^{-1}:(x,g)\mapsto(x,\lambda(x)g)$、(1.19) 截面变换与「规范变换」；(1.20) (i) $\omega_\phi\mapsto\omega_\psi$，$A'_a=\lambda A_a\lambda^{-1}+(\partial_a\lambda)\lambda^{-1}$，(ii) $F_{ab}\mapsto\lambda F_{ab}\lambda^{-1}=F'_{ab}$；例 1（Abel 群，$p^*\Omega=d\omega$，$[\Omega]\in H^2(B;\R)$ 整值）；例 2（$G=U_n$，$[\Tr\Omega]=c_1$，$\Tr(\Omega^m)$ 与 $\tilde c_m$）——逐符号一致。
- **p.154**（`p161.png`）：$\tilde c_i=P_i(c_1,\ldots,c_i)$；Newton 多项式与 $c_j=\sum_{i_1<\cdots<i_j}u_{i_1}\cdots u_{i_j}$、$\tilde c_1=c_1$、$\tilde c_2=c_1^2-2c_2$（例 2 末 □，用无星 example ✓）；例 3（$G=SO_n$，$\tilde p_i=[\Tr\Omega^{2i}]$，末 □，无星 ✓）；水平子空间场诱导到相伴丛、道路的水平提升（图 4.3）、平行移动与「同伦联络」的光滑版——一致。
- **p.155**（`p162.png`）：协变微分、(1.21) $D_a=\partial_a+A_a$、$D_a\eta^i=\partial_a\eta^i+A_{aj}^i\eta^j$；(1.22) $[D_a,D_b]=F_{ab}$；Weyl/Cartan/Yang–Mills 史段与规范场、$U_1\cong SO_2\cong S^1$ 电磁场；定义 1.1 示性类（无 □，用 `definition*{1.1}` ✓）——一致。
- **p.156**（`p163.png`）：紧 Abel 群 $G$ 的 $BG$ 清单（$S^1,T^n,(\Z/2)^n,\Z/m$ 与无穷维透镜空间）；(1.23) 三条上同调环公式与 $\Lambda_p(v)\otimes\Z/p[u]$、$u=\beta v$；$U_n\supset T^n$ 极大环面、Weyl 群 $S_n$、$i^*$ 单射与 $c_i$ 的定义——一致。
- **p.157**（`p164.png`）：(1.24) $c_i\mapsto\sum_{j_1<\cdots<j_i}u_{j_1}\cdots u_{j_i}$、$\tilde c_i\mapsto\sum_j u_j^i$；$SO_{2n},SO_{2n+1}$ 的核只含 2-挠、(1.25) $\sigma_{ij}$、(1.26) $\sigma_i$；(1.27) $p_i$ 与 $\chi_{2n}$ 的像与次数；$\R/\Q$ 上的情形；模 2 的 $(\Z/2)^n$ 与 $B\Z/2=\RP^\infty$——逐符号一致。
- **p.158**（`p165.png`）：(1.28) $w_j$ 的定义；$H^*(BO_n;\Z/2)\to H^*(BSO_n;\Z/2)$ 满、核为 $(w_1)$；$w_{2i}=c_i$、$w_{2n}=\chi_{2n}$（模 2）；$p_i(\eta)\equiv w_{4i}(c\eta)=\sum_{2j+2k=2i}w_{2j}w_{2k}$、$\chi_{2n}=c_n$（$U_n$）；流形的示性类；$w_1=0$ 与可定向；Stiefel 纤维化的「第一障碍」与 $\pi_j(F)$ 的条件——一致。
- **p.159**（`p166.png`）：$\pi_1(B)$ 在 $\pi_{k-1}(F)\otimes\Z/2$（复情形 $\pi_{2k-1}$）上平凡作用；$Dw_i$、$D\chi_{2m}$ 的闭链构造与「一般位置的 $k$ 元向量组」；结构群归约与极大紧子群；$r$、$c$、$\rho\eta$ 三个运算；(1.29) $\Lambda^2\eta\oplus S^2\eta=\eta\otimes\eta$、(1.30) $rc(\eta)\cong\eta\oplus\eta^*$、$c\bar\eta\cong c\eta$、$cr(\eta)\cong\eta\oplus\bar\eta$，五项运算清单——一致。
- **p.160**（`p167.png`）：(1.31) $(-1)^ip_i(\eta)=c_{2i}(c\eta)$、$2c_{2i+1}(c\eta)=0$；(1.32) 四条直和公式（含 (iv) 的 $k+m=n$ 与 $\dim\eta_1=2k$ 约定）；稳定性 $w_i(\eta\oplus\varepsilon^N_\R)=w_i(\eta)$ 等；Chern 特征标 (1.33) $\ch(\eta)=\sum_j e^{u_j}=\sum_m\frac1{m!}\tilde c_m=\sum\ch_m$、$\ch_m=P_m(c_1,\ldots,c_m)$；$SO_n$ 情形 $\ch(\eta)=\ch(c\eta)$；(1.34) $\ch(\eta_1\otimes\eta_2)=\ch\eta_1\ch\eta_2$——逐符号一致。
- **p.161**（`p168.png`）：跨页句（p.160 末「为暂时回到」→ p.161「$B$ 上向量丛之和…」）处理正确；$\Lambda(\eta)$、$S(\eta)$ 与 (1.35)；形式幂级数 $w,c,p$ 与 (1.32) 的乘法形式；加性表达式 $f(u)=\sum a_mu^m$、$f(\eta)=\sum_{j=1}^nf(u_j)$（实情形 $u_j^2$ 与 $b_m$）；(1.36) $f(\eta)=\sum m!a_m\tilde c_m=\sum m!a_m\ch_m(\eta)$ 与实情形 $\tilde c_{2m}$、$\ch_{2m}$——一致。
- **p.162**（`p169.png`）：乘性特征标的乘积形式；$f(M_1^n\times M_2^m)=f(M_1^n)f(M_2^m)$ 与 $f(M^{2n})=\langle f(c_1,\ldots,c_n),[M^{2n}]\rangle$（复）、$f(M^{4n})=\langle f(p_1,\ldots,p_n),[M^{4n}]\rangle$（实可定向）；Euler 示性数的 $f(u)=1+u$；例 1（$\RP^n$，$\tau\oplus\varepsilon_\R\cong\eta^{\oplus(n+1)}$、$w_1(\eta)=v$、$w_i=0$、$Dv\leftrightarrow\RP^{n-1}$、$w(\tau)=(1+v)^{n+1}$）——一致。
- **p.163**（`p170.png`）：图 4.4（Möbius 带，图题译文完整）、图 4.5；(例 2) $\tau(\CP^n)\oplus\varepsilon_\C\cong\eta^{\oplus(n+1)}$、$c_1=u$、$c(\tau)=(1+u)^{n+1}$、$Du\leftrightarrow\CP^{n-1}$；(例 3) 法丛 $\nu$ 与 $i^*\tau(N^k)=\tau(M^n)\oplus\nu(M^n)$——一致。
- **p.164**（`p171.png`）：$i^*w(N^k)=w(\tau)w(\nu)$、$i^*p(N^k)=p(\tau)p(\nu)$（模 2-挠）、$i^*c(N^k)=c(\tau)c(\nu)$；$N^k=\R^k$ 时 $i^*w=i^*p=1$ 及由此互表切丛与法丛的示性类；例 4（$\langle\chi_{2n}(\tau),[M^{2n}]\rangle=\chi(M^{2n})$）；例 5（Lie 群切丛平凡、可平行化）；例 6（$f_i=0$ 定义子流形、法丛平凡、稳定示性类为零、$\chi(S^{2k})=2$、末 □ 故用无星 example ✓）；复流形定义与「实维数 $2n$」收尾（本块不越界 p.165）——一致。

## 体例抽查
- 页标记：`% [原文 p.153]` … `% [原文 p.164]` 共 12 个，递增、无重复 ✓；但第 385 行仍在句中（见必须改 2）。
- 编号：`\tag` (1.18)–(1.36) 共 19 个，连续无缺、无自造 ✓；(1.20)(1.23)(1.27)(1.32)(1.33)(1.35)(1.36) 多行用 `aligned/gathered` 单 tag，与原书右侧单编号一致 ✓。
- 陈述：10 个（例 1–3 与例 1–6 两轮编号、定义 1.1），**原书在 p.162 重新从「例 1」编号**，译文照原样，符合补充规则⑤ ✓；带 □ 处用无星环境（例 2、例 3（p.154 的 Pontryagin 例）、例 6），无 □ 处用星号环境（例 1、例 2、例 3（p.163）、例 4、例 5、定义 1.1），已逐页对照页底 □ 位置核对 ✓。
- 图：图 4.3/4.4/4.5 均为原页裁图，未含 `Fig.` 题注行 ✓（但 4.3 裁图不完整，见必须改 1）；`\figtitle` 用中文另写 ✓。
- Tutor Note：5 条（要求 ≥ 12/3 = 4）✓；单行、无 `%` 字符。
- 本节起始于 p.153 中段，块首直接续写正文、未重复 `\section` ✓；`% CHUNK ch04b DONE` 在末行 ✓。
- check_chunk：`python work\check_chunk.py src\chunks\ch04b.tex` 复跑 **0 error**。

## 复审（2026-11-10，作者修后）

- **必须改 1 已解决**：`src/figures/fig4_3.png` 已重裁为 2250x699；read_image 自检确认下方道路曲线完整、箭头在右、$\gamma(t)$ 标注完整可读，且不含 `Fig. 4.3` 题注行 ✓。
- **必须改 2 已解决**：页标记已不再劈开句子；`% [原文 p.164]` 现位于句末之后 ✓。
- **新增必须改 1 条**：第 268–271 行页标记仍在句中。第 268 行以「……为暂时回到」结尾（句子未完），`% [原文 p.161]` 独占一行后第 271 行才接「$B$ 上向量丛之和 $\eta_1\oplus\eta_2$ 的示性类，我们考虑形式级数（对每个向量丛 $\eta$ 定义）：」。本句起于 p.160，跨页到 p.161；按补充规则①（跨页句整句归起始页所在块、页标记按起始页）与 lead 新规（标记只落在句末/段首/环境前后），须把该标记移到第 271 行末「……定义）：」之后、公式块 `\[` 之前。这是全块唯一残留的页标记违规（`work	mp_scan2.py` 复跑：ch04b 1 处，ch03j/ch03k/ch04a 均 0 处）。
- 建议改 2 条未采纳（「是满的（即满同态）」仍重复；图 4.5 图题未补「图中阴影带」），属可读性问题，不阻塞。
- 复跑 `work\check_chunk.py src\chunks\ch04b.tex`：0 error；页标记 12 个（p.153–164）递增无重复；`	ag` 19 个；陈述 10 个；Tutor Note 5 条。
