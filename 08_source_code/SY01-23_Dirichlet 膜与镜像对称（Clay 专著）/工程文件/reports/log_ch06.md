# ch06 校订日志（rv-ch06）

负责文件：`C:\Users\admin\Downloads\DBMS_work\Dirichlet-Mirror-Symmetry-zh\chapters\ch06.tex`
负责页码：PDF 431–518（第6章），对照块 `review\chunks\ch06\` 共 9 块。

## 已核对范围
- p431-440 ✅（段落 id：ch06-intro-001 … ch06-6.2.1-004，ch06.tex L3–L480）
- p441-450 ✅（段落 id：ch06-6.2.1-005 … ch06-6.2.3-023，ch06.tex L481–L1045）
- p451-460 ✅（段落 id：ch06-6.2.3-024 … ch06-6.2.5-021，ch06.tex L1046–L1538）
- p461-470 ✅（段落 id：ch06-6.2.5-022 … ch06-6.3.1-018，ch06.tex L1539–L2144）
- p471-480 ✅（段落 id：ch06-6.3.1-019 … ch06-6.3.2-027，ch06.tex L2145–L2611）
- p481-490 ✅（段落 id：ch06-6.3.2-028 … ch06-6.4.1-029，ch06.tex L2612–L3065）
- p491-500 ✅（段落 id：ch06-6.4.1-030 … ch06-6.4.2-028，ch06.tex L3066–L3390）
- p501-510 ✅（段落 id：ch06-6.4.2-029 … ch06-6.4.4-006，ch06.tex L3391–L3700）
- p511-518 ✅（段落 id：ch06-6.4.4-007 … ch06-6.4.4-032，ch06.tex L3701–L3975）

## 改动记录（p431-440）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 1 | ch06-6.1.2-015 / L320 | "the only other affine structure on the two-torus obtained from $M_R$ by dividing out by a properly discontinuous group action" | 对于从 $M_{\mathbb R}$ 除去正常不连续的群作用得到的二维环面 | 对于由 $M_{\mathbb R}$ 对正常不连续的群作用取商得到的二维环面 | 误译 | "dividing out by" 是"作商"，原译"除去（去掉）"把商作用误成删除，数学含义相反/不通 |

## 改动记录（p441-450）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 2 | ch06-6.2.3-019 / L995 | "For a B-field B not in the image of $H^1(B,\Lambda_R)$, $X(B,B)$ does not even coincide topologically with $X(B)$, and the construction which follows does not apply." | 对于不在这一像中的 B 场 $\mathbf B$，$X(B,\mathbf B)$ 作为 $X(B)$ 的环面丛，甚至可能在拓扑上也不同 | 对于不在这一像中的 B 场 $\mathbf B$，$X(B,\mathbf B)$ 甚至在拓扑上也不与 $X(B)$ 相同 | 病句/误译 | 原译插入"作为 X(B) 的环面丛"并加"可能"，句子不通且弱化了"拓扑上不相同"的断言 |

## 待确认 / 未改（p431-440，供 Lead 判断）

- **ch06-6.1-intro-001（p431）**：英文段落到 "$\operatorname{Im}\Omega|_M=0$." 结束，中文末尾多出一句"采用 $\Omega$ 与 $\omega$ 相容的通常归一化，并以 $\operatorname{Re}\Omega|_M$ 为 $M$ 的体积形式来选取定向。"原文无对应句。内容本身正确（标准归一化约定），疑为译者补注，故未删。
- **ch06-6.1.2-013（p437）**：英文 "Note that the linear part of $\rho$ is precisely the monodromy of $\Lambda$." 中文多出"在坐标变换的线性部分为整矩阵时"与"这一局部系统将在6.2.1中明确构造"两句；$\Lambda\subseteq TB$ 确在 §6.2.1 定义，内容不误，未改。
- **ch06-6.1.1-007（p433，定理6.2）**：英文 "a compact special Lagrangian submanifold"，中文多"无边界"。数学上冗余但正确，未改。
- **ch06-6.1.2-010/011（p434）**：英文 "submanifolds $\gamma_1,\ldots,\gamma_s\subseteq U$"（U 为 B 的小开集），中文作 $\gamma_i\subseteq\mathcal U$（$\mathcal U\subseteq B\times X$ 的总空间）。原书本身记号冲突，未改。
- **ch06-6.1.2-007（p436）**：英文 "A simple calculation then confirms that $\partial\check K/\partial\check y_i=y_i$"，中文同，属原文即如此，不动。

## 待确认 / 未改（p441-450，供 Lead 判断）

- **ch06-6.2.2-005（p444-445，L691-L706）：$\mu$ 的符号指数多一个 $p$**。原书："$\mu(\sum a_{IJ}\mathrm dy_I\wedge\mathrm dx_J)=(-1)^{q(q-1)/2+n(n-1)/2}\sum a_{IJ}\mathrm dy_I\wedge\iota(\partial/\partial\check x_J)(\mathrm d\check x_1\wedge\cdots\wedge\mathrm d\check x_n)$"；中译指数为 $(-1)^{p+q(q-1)/2+n(n-1)/2}$。**疑似数学错**，但译文另外把 B 场的基写成 $\mathrm d\check x_j\wedge\mathrm dy_i$（原书该处为 $\mathrm dy_i\wedge\mathrm d\check x_j$，且原书 p450 又把 $\omega$ 写成 $\sum\mathrm dy_i\wedge\mathrm d\check x_i$，与原书 p442 的 $\sum\mathrm d\check x_i\wedge\mathrm dy_i$ 自相矛盾）。经验算：中译"$\mu$ 含 $p$ + $B$ 用 $\mathrm d\check x_j\wedge\mathrm dy_i$ + $\omega=\sum\mathrm d\check x_i\wedge\mathrm dy_i$"是**自洽**的，能复现命题 6.26 的 $\bigwedge_i(\mathrm dx_i+\sum_j(b_{ji}+\mathrm i\delta_{ji})\mathrm dy_j)$；若去掉 $p$ 则命题 6.26 的公式会差一个负号。故**未改**，请 Lead 决定是否统一到原书约定（需同时改 4 处符号）。
- **ch06-6.2.1-010（p441，命题6.14）**：英文只说 "Ricci-flat iff K satisfies the real Monge-Ampère equation det = const"；中译增出"$\log\det(g_{ij})$ 在局部仿射坐标中为仿射线性函数"与"若要求自然全纯体积形式 $\Omega$ 平行……"两层中间论断。数学上更准确（原书此处略粗），属译者补正，未改。
- **ch06-6.2.1-014/015（p442，命题6.15）**：同样增出 $\check y_i=\partial K/\partial y_i$、$g_{ij}$ 定义与"$-\log\det(g^{ij})$ 表示为 $\check y$ 的函数后为仿射线性函数"一句；另将原书重复印刷的 "det(g_ij) = constant, iff det(g_ij) = constant" 处理为 "$\det(g^{ij})$ 为常数等价于 $\det(g_{ij})$ 为常数"，合理。
- **ch06-6.2.2-010（p446，命题6.20）**：中译多出"对偶映射采用整体符号 $(-1)^p$：将 $\mathrm dy_I\wedge\mathrm d\check x_J$ 对应于 $(-1)^p\mathrm dy_I\otimes\partial/\partial y_J$……"一段，原文无；该段是为上面命题 6.26 的符号约定作铺垫（与上一条自洽），未改。
- **ch06-6.2.2-011（p446）**：中译多出"对 $H^p(B,\bigwedge^q\Lambda_{\mathbb R})$ 的对偶构造完全相同"与"这里先取 $p>0$""对于 $p=0$，原来的闭半平坦形式本身就是这样的平坦截面"三处补语；均正确，未改。
- **ch06-6.2.2-005（p444）**：中译"将它乘以固定的归一化常数后，局部地有 $\Omega=\bigwedge(\mathrm dx_i+\mathrm i\mathrm dy_i)$"，"乘以固定归一化常数"原文无，未改。
- **ch06-6.2.1-021（p443，定义6.17）**：中译多"其 Hessian 矩阵正定并定义 $B$ 上的度量"；正确但原文无，未改。
- **ch06-6.2.3-010（p448，例6.22）**：原书 $\omega=2\sqrt{-1}(\check\tau_2/\tau_2)\mathrm dz\wedge\mathrm d\bar z$（pdftotext 版面），中译作 $\frac{\mathrm i}{2}\frac{\check\tau_2}{\tau_2}\mathrm dz\wedge\mathrm d\bar z$。按体积 $\check\tau_2$ 反算，中译的 $\mathrm i/2$ 系数才自洽（$2\mathrm i\partial\bar\partial$ 配 $K=\frac{\check\tau_2}{\tau_2}\frac{y^2}{2}$ 给出 $\mathrm i/2$），原书此式疑为排版/笔误，未改。
- **ch06-6.2.3-015（p449，命题6.24证明）**：中译把原书 "$d(\Omega\wedge\theta_i)=d\Omega\wedge\theta_i\pm\Omega\wedge d\theta_i$" 的 $\pm$ 写成 $+(-1)^n$，并据此得 $(-1)^n\Omega\wedge d\theta_i$，正确。

## 改动记录（p451-460）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 3 | ch06-6.2.4-018 / L1309 | "The family $f:X(B')\to X(V)$ is not topologically trivial." | 族 $f\colon X(B')\to X(\mathcal V)$，在拓扑上并不必然平凡 | 族 $f\colon X(B')\to X(\mathcal V)$，在拓扑上并不平凡 | 误译 | 原文是断言"不平凡"（下文随即证明单值变换非平凡），原译加"必然"把它弱化成"未必平凡" |
| 4 | ch06-6.2.4-019 / L1330 | "we have seen locally in the proof of Proposition 6.31 that after dividing out by $\Lambda'$, $p_*^{-1}(0)$ and $p_*^{-1}(\delta_1)$ are identified" | 除去 $\Lambda'$ 后 | 模去 $\Lambda'$ 后 | 误译 | "dividing out by"＝"对……取商/模去"，"除去"易读成"删掉"（同 p437 处错误） |

## 待确认 / 未改（p451-460，供 Lead 判断）

- **ch06-6.2.4-002（p452）**：英文 "the holonomy representation for $\delta'$ is given by $\rho':\pi_1(B)\to\operatorname{GL}(M\oplus\mathbb Z)$"，中译照录 $\operatorname{GL}(M\oplus\mathbb Z)$。按 $\rho'(\gamma)(m,r)=(Am+rb,r)$（$r\in\mathbb R$），此处应为 $\operatorname{GL}(M\oplus\mathbb R)$。原书疑为笔误，译文忠实照录，未改。
- **ch06-6.2.3-025（p451，例6.27）**：原书 $\mathbf B+\sqrt{-1}\omega=(\sqrt{-1}+\tau_1/\tau_2)\mathrm dy\wedge\mathrm d\check x$，中译作 $(\mathrm i+\tau_1/\tau_2)\mathrm d\check x\wedge\mathrm dy$（差一负号）；属前述"$\omega$ 统一用 $\mathrm d\check x\wedge\mathrm dy$"的自洽约定（见 p444-445 那条），未改。
- **ch06-6.2.4-019（L1326-L1329）**：原书 $\widetilde\varphi_r:p_*^{-1}(0)\to p_*^{-1}(\delta_1)$ 由"adding $(0,\delta_1)$"给出；中译改为"加上 $(0,r\delta_1)$"、靶为 $p_*^{-1}(r\delta_1)$。中译与 $\varphi_r:f^{-1}(\mathrm i\delta_2)\to f^{-1}(r\delta_1+\mathrm i\delta_2)$ 一致，数学上更对，原书疑笔误，未改。
- **ch06-6.2.4-013（p454，注6.30）**：原文仅 "This coincides with $[\delta]$."，中译多"在前述对偶符号约定下"；属承接 p445 对偶符号说明的补语，未改。
- **ch06-6.2.5-018（p460，例6.37(2)）**：原书 "$\varphi=\exp(\sqrt{-1}\omega)$ …… $(X+\xi)\cdot\varphi=0$ if and only if $\sqrt{-1}\iota(X)\omega=\xi$"，中译作 "$\xi=-\mathrm i\iota(X)\omega$"，并补一句"$E_\varphi$ 是例6.34(2)的广义复结构的共轭；该例中的 $+\mathrm i$ 特征丛本身，由 $\exp(-\mathrm i\omega)$ 给出"。手算 $\varphi=e^{\mathrm i\omega}$ 的一次项得 $\xi+\mathrm i\iota(X)\omega=0$，即 $\xi=-\mathrm i\iota(X)\omega$，**中译符号正确、原书此式疑笔误**；补句为译者所加但成立，未改。
- **ch06-6.2.5-019（p460，例6.37(3)）**：中译多"且 B 场为闭实2形式"；为使 $\exp(B)\wedge\varphi$ 保持闭形式所必需，原书默认，未改。
- **ch06-6.2.5-011（p459）**：中译多"交换奇偶分量"（Clifford 乘法的次数行为），正确，未改。
- 其余：Courant 括号公式、$\sigma(\varphi)=(-1)^{p(p-1)/2}\varphi$、旋量丛 $S^\pm$、B 场链式恒等式、命题 6.31/6.32 的论证与公式均逐条核对无误。

## 改动记录（p461-470）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 5 | ch06-6.2.5-025 / L1597 | "Let $S_{1,0}$ and $S_{0,1}$ denote the sheaves of semi-flat vector fields…" | 令 $S_{1,0}$ 与 $S_{0,1}$，分别表示…… | 令 $S_{1,0}$ 与 $S_{0,1}$ 分别表示…… | 标点 | 逗号插在"令……分别表示"之间，割断主谓 |
| 6 | ch06-6.2.5-027 / L1715 | "This demonstrates that $\widetilde\mu$ and $\mu$ respect Clifford multiplication." | 尊重 Clifford 乘法 | 保持 Clifford 乘法 | 术语 | "respect" 的标准译法是"保持/相容"；紧接下句 "$\widetilde\mu$ respects the indefinite inner product" 已译作"保持"，前后应统一 |

## 待确认 / 未改（p461-470，供 Lead 判断）

- **ch06-6.2.5-025（p462）**：原书 $\widetilde\mu(\mathrm dy_i)=\mathrm dy_i$、$\widetilde\mu(\partial/\partial y_i)=\partial/\partial y_i$（无负号）；中译加"采用与 $\mu$ 相容的符号约定"，写成 $-\mathrm dy_i$、$-\partial/\partial y_i$。此与 §6.2.2 起"$\mu$ 含 $(-1)^p$ 因子"的统一约定配套：中译在 $\widetilde\mu$ 与 $\mu$ 中同时多取 $(-1)^p$（$p$ 为 $\mathrm d y$ 部分次数），使 (6.1) $\widetilde\mu(X+\xi)\cdot\mu(\varphi)=\mu((X+\xi)\cdot\varphi)$ 仍成立；本块 p462-463 两组长算与 p463 的配对比较都按此约定重排指数，逐行自洽。未改。
- **ch06-6.2.5-029（p463，式(6.2)）**：原书 $\langle\varphi,\psi\rangle=(-1)^n\langle\mu(\varphi),\mu(\psi)\rangle$，并称"两个表达式的符号相差 $(-1)^n$"；中译按上述约定改成 $\langle\varphi,\psi\rangle=\langle\mu(\varphi),\mu(\psi)\rangle$，把"相差 $(-1)^n$"改成"符号相同"，同时给第二组计算的指数整体补 $(-1)^n$。该因子在定理6.39 的证明中两边同乘、不影响结论，未改。
- **ch06-6.2.5-036（p464，例6.44）/ ch06-6.2.5-042（p465，练习6.47）**：原书例6.44 只说到"$\omega^n$ 与 $\Omega\wedge\bar\Omega$ 成比例即定义6.43 的条件"；中译补"体积归一化""取相对于 Ricci 平坦度量平行的全纯体积形式""两个纯旋量可取为 $\Omega$ 与 $\exp(-\mathrm i\omega)$"，并把练习6.47 的 $\exp(B+\sqrt{-1}\omega)$ 写作 $\exp(B-\mathrm i\omega)$、补"两旋量配对之比为非零常数"。这是与例6.37(2) 处"中译把 $+\mathrm i$ 特征丛定为 $\exp(-\mathrm i\omega)$"配套的全局符号翻转，内部自洽（$\mathrm e^{-\mathrm i\omega}\leftrightarrow\mathcal J_\omega$，使 $G=-\mathcal J_1\mathcal J_2$ 正定）。未改，供 Lead 判断是否统一。
- **ch06-6.2.5-022（p461，定理6.38 证明末行）**：原书排版疑作 $\frac12[\mathcal L_Y\xi-\mathcal L_X\eta-\frac12\mathrm d(\iota(Y)\xi-\iota(X)\eta)]$（½ 外提）；中译作 $[\mathcal L_Y\xi-\mathcal L_X\eta-\frac12\mathrm d(\dots)]$。按 Cartan 公式手算，中译正确、外提 ½ 会使等式不成立，未改。
- **ch06-6.2.5-046（p466）/ ch06-6.3.1-013（p469，例6.57）**：中译分别补"由非零配对可知 $\beta\ne0$"、把"不含紧有理仿射子空间"补成"不含正维的**真**紧有理仿射子空间"（否则整个 $B$ 本身即反例）。均为正确补语，未改。
- **ch06-6.3.1-002（p468）**：原书 $X=f^{-1}(U)=U\times\sqrt{-1}(M_{\mathbb R}/M)$，中译写作 $U\times(M_{\mathbb R}/M)$ 并补"复结构仍由纤维坐标与底坐标组成的 $x+\mathrm i y$ 给出"；因子 $\mathrm i$ 移入说明句，等价，未改。
- **ch06-6.3.1-008（p468，命题6.54）/ ch06-6.3.1-011（练习6.55）**：中译分别补"$g_i$ 只在模去 $\Lambda_{\mathbb R}'+\Lambda|_{B'}$ 的意义下指定同一子流形"、"主齐性空间"译名，均为说明性补语，未改。
- **ch06-6.2.5-043（p465，例6.48）**：原书 "a three-dimensional space"，中译"一个三维复空间"；$n=4$ 时 $\ker\beta\subset T_bM\otimes\mathbb C$ 确为复三维，成立，未改。

## 改动记录（p471-480）

本块无改动。逐段核对命题6.59/6.60、例6.61、定理6.63 的证明与陈述、§6.3.2 A 膜、定义6.64/6.66、引理6.67（含 $(\mathbf B+\mathrm i\omega)|_{L(B',g)}$ 的拉回计算：$i\le p<j$ 时 $\delta_{ij}=0$，故首项只余 $b_{ij}$）、命题6.69、推论6.70、定理6.71 及证明，公式与中文表述均成立（详见下列各条，均为"未改"的记录）。

## 待确认 / 未改（p471-480，供 Lead 判断）

- **ch06-6.3.1-020（p472，命题6.59 证明）**：原书"$\operatorname{Trans}\colon\operatorname{Aff}(M_{\mathbb R})\to M_{\mathbb R}$ is the projection onto the **linear** part"——按上下文（$\operatorname{Trans}$ 之名、原文紧接着的"Note: Trans is not a homomorphism"、以及 $\phi_{ij}(m)=\operatorname{Lin}(\cdots)(m)\exp(2\pi\mathrm i[b_{ij}+\mathrm i\operatorname{Trans}(\cdots)])$ 的因子分解）应为**平移**部分；中译直接作"取平移部分的映射"，属正确修正，未改。
- **ch06-6.3.1-024 / ch06-6.3.1-025（p472-473，例6.61 及其后）**：原书无附加条件，中译两处补"当 $n\ge2$ 时"。$n=1$ 时 $\bigwedge^2\check\Gamma=0$，原文断言的"一般选择下 $H^1(B,\mathcal P_{B,\mathbf B})\to H^1(B,\check\Lambda)$ 为零 / 首映射为同构"是否成立需另算；补语使中译断言变弱而非变假，且不补则可能变成错的。未改，供 Lead 判断是否保留该限定。
- **ch06-6.3.1-028（p473-474，定理6.63 尾句）**：原书把"$\mathcal L$ 在相差张量积一个线丛的意义下唯一确定，该线丛属于 $H^1(B',\mathbb C^\times)/H^0(B',\check\Lambda_{B'})\subseteq H^1(B',\mathcal P_{B',\mathbf B'})$"中的商简写成混用 $H^0$/$H^1$ 的记号；中译改为 $\dfrac{H^1(B',\mathbb C^\times)}{\operatorname{im}(H^0(B',\check\Lambda')\to H^1(B',\mathbb C^\times))}$ 并补"分母中的映射，是相应长正合列的连接同态"。属正确澄清，未改。
- **ch06-6.3.1-030（p474）**：原书 "Let $B'\to B$ be a covering map"，中译作"有限覆盖映射"。原文随即称秩等于 $\pi$ 的次数、即 $\pi^{-1}(x)$ 的点数，隐含有限；补"有限"使陈述严密，未改。
- **ch06-6.3.2-001 / 6.3.2-009 / 6.3.2-022 / 6.3.2-024（p474-480）**：A 膜曲率条件中译统一作 $F=-2\pi\mathrm i\,\mathbf B|_L$（原书为 $F=2\pi\sqrt{-1}\mathbf B|_L$），并显式给出 $c_1(\mathcal L)=[\mathrm iF/(2\pi)]$、$\nabla=\mathrm d-2\pi\mathrm iA$、$F_{\mathrm{real}}$ 的归一化方式。自洽链为 $c_1=[\mathrm iF/2\pi]=[\mathbf B|_L]$，故"$\mathbf B|_L$ 为整类 ⇔ 存在该联络"成立，与例6.37(2) 起的全局 $\mathrm i\to-\mathrm i$ 翻转同源（见 p451-460 待确认第 5 条）。未改，供 Lead 判断全章是否统一。
- **ch06-6.3.2-021（p479）**：原书只说这些丛"模去规范等价后由 $H^1(L,\mathbb R/\mathbb Z)$ 参数化"；中译补"固定底层丛的拓扑类型时，应取其中相应的分量"。属说明性补语（措辞略绕），未改。
- **ch06-6.3.2-024（p479-480，定理6.71 数据(2)）**：原书仅"取 $[g]\in H^1(B',\check\Lambda')$ 到 $H^1(B',\mathcal P^{\mathbb R}_{B',B'})$ 的提升"；中译补"连同它与固定的 $g$ 所给出的第二分量代表的识别。在这一相对提升中，只模去第一分量的恰当1形式"。属解释性补语，未改。
- **ch06-6.3.2-025（p480）**：原书 "the $(0,1)$ part determines an $\alpha$"；中译补"按照所采用的楔积次序，$(0,1)$ 部分的**负**系数确定 $\alpha$"。与本章 $\mathrm dg^j\wedge\mathrm dy_i$ 的楔积次序（相对原书 $\mathrm dy_i\wedge\mathrm d\check x_j$）配套的符号说明，未改。
- **ch06-6.3.2-027（p480）**：原书 "changes the class of $\mathbf B'$ by the image of $\alpha'\in H^0(B',\Lambda_{\mathbb R}|_{B'}/\Lambda_{\mathbb R}')$ in $H^1(B',\Lambda_{\mathbb R}')$"；中译作"改变一个等于……的像的**负值**的元素"。由同段 $\mathbf B'=\mathbf B|_{B'}-\nabla\widetilde\alpha$ 可知中译符号正确（原文欠一个负号）。未改。
- **ch06-6.3.2-014（p477，笔记6.68）**：原书 "forms constant on fibers"，中译"在 $L(B',g)$ 的纤维上具有常系数"。严格说应作"沿纤维为常值"，现译可通（指系数沿纤维不变），未改。
- **ch06-6.3.2-004（p475，定义6.64 末）**：原书段末的 □（证明结束符）在中译里以 `\BookQED` 放在 `definition` 环境内部，会印在定义末尾；照原书版面如此，未改（如需处理属排版事项）。

## 改动记录（p481-490）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 7 | ch06-6.4.1-025 / L2995 | "but one can find a maximal partial crepant projective resolution, which resolves singularities in codimension less than 4" | 可以找到极大部分保典射影消解 | 可以找到极大的部分保典射影消解 | 病句 | "极大部分"会被读成"绝大部分（the vast majority of）"，原意是"极大的 部分（maximal partial）crepant 射影消解"；加一个"的"即消除歧义，术语"保典消解"与 glossary.csv 一致 |

## 待确认 / 未改（p481-490，供 Lead 判断）

- **ch06-6.3.2-028（p481，式(6.4)）**：原书 "if $\widetilde\alpha=\sum_j\widetilde\alpha_j\,\mathrm d\check x_j$"，并紧接着说"$\widetilde\alpha$ 可以看作 $f̌^{-1}(B')$ 上的半平坦 $(0,1)$ 形式"。中译改写为"若 $\widetilde\alpha=\sum_j\widetilde\alpha_j\,\partial/\partial y_j$，则相应的半平坦 $(0,1)$ 形式为 $a=-\sum_j\widetilde\alpha_j\,\mathrm d\check x_j$"，并把 (6.4) 按本章相反的楔积次序写成 $\sum(b_{ij}-\partial\widetilde\alpha_j/\partial y_i)\mathrm d\check x_j\wedge\mathrm dy_i$。经验算：$\mathrm da|_{L}=\sum(\partial\widetilde\alpha_j/\partial y_i)\mathrm dg^j\wedge\mathrm dy_i$，$\mathbf B|_{L}=\sum b\,\mathrm dg^j\wedge\mathrm dy_i$，故 $\mathbf B|_{L}-\mathrm da|_{L}=\sum(b-\partial)\mathrm dg^j\wedge\mathrm dy_i$ 与杯积表达式一致，**中译自洽**（$\widetilde\alpha\in\Gamma(C^\infty\otimes\Lambda_{\mathbb R}|_{B'})$、$\Lambda_{\mathbb R}\subset TB$，写成 $\partial/\partial y_j$ 更合字面；补出的 $a$ 只是把同一对象写成形式）。未改。
- **ch06-6.3.2-029（p481-482）**：原书 "precisely the form $-\mathbf B|_{L(U,g)}+\mathrm d\alpha|_{L(U,g)}$"，中译作"正是形式 $\mathbf B|_{L(U,g)}-\mathrm da|_{L(U,g)}$"。与其 $a=-\sum\widetilde\alpha_j\mathrm d\check x_j$ 的负号、以及 $\mathbf B|_{L}=\sum b\,\mathrm dg^j\wedge\mathrm dy_i$ 的次序配套，数值上仍等于杯积；属同一套约定的联合改写，未改。
- **ch06-6.3.2-033（p482）**：原书提升为配对 $(\widetilde\alpha',\widetilde g)$，满足 $\nabla_{\mathcal P}(\widetilde\alpha',\widetilde g)=(\mathrm d\widetilde\alpha'-\mathbf B'(\widetilde g),0)=0$；中译作 $(-\widetilde\alpha',\widetilde g)$，条件为 $(-\mathrm d\widetilde\alpha'-\mathbf B'(\widetilde g),0)=0$，即 $\mathrm d\widetilde\alpha'=-\mathbf B'(\widetilde g)$。这与中译 (6.5) $\mathrm d\widetilde\alpha'=\mathbf B|_{L}-\mathrm da|_{L}$（$=-\mathbf B'(\widetilde g)$）正好相符，自洽；未改。
- **ch06-6.3.2-035（p482-483，定理6.72 数据(1)）**：原书 Čech 0-链记作 $(g_i)$，与同一数据中的 $[g]\in H^1(B',\check\Lambda')$ 撞名；中译改用 $(h_i)$，并补"对于给定的 $\mathbf B'$，$(h_i)$ 的选择集合是……的主齐性空间"。属正确消歧与补语，未改。
- **ch06-6.3.2-036（p483，定理6.72 数据(2)）**：原书写 "$[g]\in H^1(B,\check\Lambda')$"（应为 $H^1(B',\check\Lambda')$），中译已改为 $B'$；另补"等价通过 $\mathbb R/\mathbb Z$ 值的 0 上链给出的规范改变取商"（原文 "modulo gauge transformations given by R/Z-valued 0-cochains" 已含此意）。未改。
- **ch06-6.3.2-037（p483）**：原书 "Comparing this with Theorem 6.63, we see that we have moduli spaces of semi-flat A- and B-branes which correspond."；中译开头增"使几何提升与联络提升的投影识别彼此相容，并同时取商"。属解释该比较何以成立的补语，未改。
- **ch06-6.3.2-038（p484）**：原书只说 "$H^1(X,\mathbb R/\mathbb Z)$ 作用于给定线丛上的 U(1) 联络模规范等价的空间，且该空间是主齐性空间"；中译补"若固定线丛 $\mathcal L$ 的拓扑类型，应限制到相应分量，此时平移群为 $H^1(X,\mathbb R)/\operatorname{im}H^1(X,\mathbb Z)$"。内容正确（固定丛的拓扑后平移群即 $H^1(X,\mathbb R)/H^1(X,\mathbb Z)$），属说明性补语，未改。
- **ch06-6.3.2-039 / 6.3.2-040（p484，例6.73）**：中译补"采用与例题6.27相同的归一化"；又把 "Note that from the exact sequence of Proposition 6.69, $H^1(B,\operatorname{Aff}_{\mathbb Z}(B,\mathbb R))$ fits into an exact sequence…" 增出"按周期 $\tau_2$ 将常数部分归一化后"。均为定位/说明性补语，与例题6.27 的 $\mathbf B$ 归一化一致，未改。
- **ch06-6.4.1-008 / 6.4.1-009（p486）**：中译补"其中，$\operatorname{Int}$ 表示相对内部"、"$v$ 为上述 $\mathcal P$ 的顶点"，均为澄清，未改。
- **ch06-6.4.1-015（p487）**：原书 "using the flat connection on $TB$"，中译作"利用 $TB_0$ 上的平坦联络"；因平坦结构只在 $B_0$ 上有定义，"$TB_0$"更准确，未改。
- **ch06-6.4.1-023（p489，命题6.81 证明）**：原书只说转移映射就是投影 $w^\perp\to M_{\mathbb R}/v\mathbb R$，并"显然限制为整同构 $w^\perp\cap M\to M/v\mathbb Z$"；中译补"的线性部分"以及"在 $A_\sigma$ 中选一个整顶点为仿射原点后，平移部分也在相应的整格中。因此，转移映射为整仿射映射"。补语数学上正确（整性是仿射性质，须同时管线性与平移部分），未改。

## 改动记录（p491-500）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 8 | ch06-6.4.2-013 / L3184 | "We can recover the $S^1$-bundle $Z\to C\times S^1$ by dividing $C\times\mathbb R\times S^1$ by the $\mathbb Z$-action" | 对 $C\times\mathbb R\times S^1$ 除去 $\mathbb Z$ 作用 | 对 $C\times\mathbb R\times S^1$ 按 $\mathbb Z$ 作用取商 | 误译 | "divide by the $\mathbb Z$-action" 是"按群作用取商"，"除去（去掉）"把取商误成删除；与 #1、#4 同类错误，统一改法 |

## 待确认 / 未改（p491-500，供 Lead 判断）

- **ch06-6.4.2-005（p492，nut 的 $c_1$）**：原书 $\theta=\sqrt{-1}\operatorname{Im}(\bar z_1\mathrm dz_1-\bar z_2\mathrm dz_2)/(|z_1|^2+|z_2|^2)$，曲率写作 $\frac{\mathrm d\theta}{2\pi\sqrt{-1}}=-\frac{u_1\mathrm du_2\wedge\mathrm du_3+\cdots}{4\pi(u^2)^{3/2}}$，随后又称 $\int_{S^2}\frac{\mathrm d\theta}{2\pi\sqrt{-1}}=1$——按所示表达式该积分应为 $-1$（原书此处欠一个负号）。中译按 $c_1=[\mathrm iF/(2\pi)]$ 改写成 $\frac{\mathrm i\,\mathrm d\theta}{2\pi}=\frac{u_1\mathrm du_2\wedge\mathrm du_3+u_2\mathrm du_3\wedge\mathrm du_1+u_3\mathrm du_1\wedge\mathrm du_2}{4\pi(u_1^2+u_2^2+u_3^2)^{3/2}}$，并显式给出 $\int_{S^2}\frac{\mathrm i\,\mathrm d\theta}{2\pi}=1$、$c_1=1$。经验算：由原书所示曲率式反解 $\mathrm d\theta=-\frac{\mathrm i}{2}\cdot\frac{u_1\mathrm du_2\wedge\mathrm du_3+\cdots}{(u^2)^{3/2}}$，故 $\frac{\mathrm i\,\mathrm d\theta}{2\pi}=+\frac{\Sigma u\,\mathrm du\wedge\mathrm du}{4\pi(u^2)^{3/2}}$，在单位球面上积分为 $1$，**中译自洽且修正了原书的符号矛盾**。属 $c_1=[\mathrm iF/2\pi]$ 全局约定的又一实例，未改。
- **ch06-6.4.2-010（p493，构造6.86 末）**：原书只说"取 $c_1=1$ 的 $S^1$ 丛，于是可以添加一个 nut，得到 $\overline q\colon\overline X\to\overline Y$"；中译补"这里的生成元与下面的粘合约定相容"。属提示性补语，未改。
- **ch06-6.4.2-013（p495）**：原书在 "(Exercise!)" 前无任何说明；中译补"在本段中，选取底环面的定向为 $\mathrm d\rho\wedge\mathrm d\theta$"。该定向约定正是 $c_1=1$ 成立所必需的，属正确补语，未改。
- **ch06-6.4.2-019（p497，构造6.89 证明）**：原书 "the restriction of $q$ to $\{y'\}\times(\mathbb R^3-\{0\})$ for any point $q\in U\cap S$"——此处 "$q$" 与丛映射 $q$ 撞名、且"$q\in U\cap S$"于上下文不通（应为 $B^{n-3}$ 中的点）；中译作"对于 $B^{n-3}$ 中的任意点 $y'$"，属正确修正，未改。
- **ch06-6.4.2-027（p500，构造6.92）**：原书 $S=\{(z_1,z_2,z_3,w)\in\overline X\mid\text{two of }z_1,z_2,z_3\text{ are zero},\ w=1\}$；中译作"$z_1,z_2,z_3$ 中至少两个为零"。因下文需把 $(0,0,0,1)$ 也含在 $S$ 内，"至少两个"是必要的澄清，未改。
- **ch06-6.4.2-025（p499，构造6.92 陈述）**：原书写作 $f(z_1,z_2,z_3)=(|z_1|^2-|z_2|^2,|z_1|^2-|z_3|^2,\log|w|)$（漏写自变量 $w$）；中译补成 $f(z_1,z_2,z_3,w)$，正确，未改。
- **ch06-6.4.2-026（p500）**：原书 "$\overline q\colon\overline X\to\overline Y$、$g\colon\overline Y\to\mathbb R^3$" 的分解与 $g(x_1,x_2,w)=(x_1,x_2,\log|w|)$ 中译均照录；原书对 $g$ 的定义域 $(\overline Y=\mathbb R^2\times\mathbb C^*)$ 与值域 $\mathbb R^3$ 的对应无误，未改。

## 改动记录（p501-510）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 9 | ch06-6.4.2-029 / L3392 | "we first divide $f^{-1}(U_1)$ out by the $S^1$-action $(z_1,z_2,z_3)\mapsto(e^{\mathrm i\theta}z_1,e^{-\mathrm i\theta}z_2,z_3)$" | 先对 $f^{-1}(U_1)$ 除去 $S^1$ 作用 $(z_1,z_2,z_3)\mapsto(\ldots)$，得到 | 先对 $f^{-1}(U_1)$ 按 $S^1$ 作用 $(z_1,z_2,z_3)\mapsto(\ldots)$ 取商，得到 | 误译 | "divide ... out by the $S^1$-action" 是取商；"除去"读作删掉该作用，与 #1、#4、#8 同类，统一为"按…取商" |
| 10 | ch06-6.4.3-010 / L3479 | "Let $B'$ be a tubular neighbourhood of $C$ in $B$, so that $B'\cap\Delta=C$, and $\partial B'$ is a two-torus as depicted in Figure 11." | 令 $B'$ 为 $C$ 在 $B$ 中的一个管状邻域，满足 $B'\cap\Delta=C$，并取这里所讨论的、边界 $\partial B'$ 为二维环面的情形，如\BookRef{fig:6.11}{图11}所示。 | 满足 $B'\cap\Delta=C$，其边界 $\partial B'$ 为二维环面，如\BookRef{fig:6.11}{图11}所示。 | 误译 / 病句 | 原文是陈述所选管状邻域的性质（"so that … and ∂B′ is a two-torus"），中译"并取…为…的情形"把它降格为一个额外假定，且句子结构破碎；改为陈述句 |

## 待确认 / 未改（p501-510，供 Lead 判断）

- **记号 $\overline B'$ vs $B'$（p504 起）**：原书在本节一律写 $B'$（管状邻域），只有纤维化底空间 $S^1\times\overline D$ 写 $\overline B$；中译 6.4.3-010 用 $B'$，而 6.4.3-023/024/025/026/030 改用 $\overline B'$。两者指同一对象，属记号不统一，不影响理解，未改（改动面较大，且 $\overline B'$ 不会与 $\overline B$ 冲突）。
- **ch06-6.4.3-012（p505）**：原书无此句；中译在"$b\in\{0\}\times(\overline D\setminus\{0\})\subseteq S^1\times(\overline D\setminus\{0\})$"后补"这里以 $\mathbb R/\mathbb Z$ 表示圆周"，属记号说明性补语，未改。
- **ch06-6.4.3-016（p506）**：原书只说"把 $X\to D$ 的纤维看作 Abel 群，通过取负作用"，未提奇异纤维；中译补"并将这一作用延伸到夹缩纤维"。要得到 $X\times S^1$ 的微分同胚必须作用于奇异纤维，属必要澄清，未改。
- **ch06-6.4.3-018（练习6.96，p506）**：原书无此句；中译补"单值变换保持定向时，这里可取 $\mathcal E$ 为平凡丛"。该论断正确（$\Gamma$ 的 holonomy 落在 $SL_3(\mathbb Z)$ 时 $\mathcal E$ 平凡），属补语，未改。
- **ch06-6.4.4-003（p510）**：原书 "However, it is always true that the stalks of $R^pf_*\mathbb Q$ are given by $(R^pf_*\mathbb Q)_b\cong H^p(f^{-1}(b),\mathbb Q)$"；中译作"在这里的固有纤维化中，$R^pf_*\mathbb Q$ 的茎由下式给出"。补"固有（proper）"提示了茎公式的成立条件，正确，未改。
- **定义6.101（p510）**：原书以等式 $i_*R^pf_{0*}\mathbb Q=R^pf_*\mathbb Q$（对所有 $p$）定义 $\mathbb Q$-简单；中译改述为"自然限制比较映射给出同构 $R^pf_*\mathbb Q\cong i_*R^pf_{0*}\mathbb Q$"，并把 $G$-简单 的条件同步改写。等价且更明确，未改。
- **ch06-6.4.3-030 性质(3)（p508）**：原书 "there is a fiberwise torus action on $f^{-1}(U)\to U$ of the torus $\Gamma(U\setminus\Delta,\Lambda_{\mathbb R}/\Lambda)$"；中译"$f^{-1}(U)\to U$ 上存在沿纤维的环面平移作用，由群 $\Gamma(U\setminus\Delta,\Lambda_{\mathbb R}/\Lambda)$ 给出"。补"平移"二字准确（该作用即 $\Gamma$ 的平移），未改。

## 改动记录（p511-518）

本块无改动。逐段对照 $R^pf_{0*}\mathbb Q=\bigwedge^p\check\Lambda_{\mathbb Q}$、$\bigwedge^p\Lambda\times\bigwedge^{n-p}\Lambda\to\bigwedge^n\Lambda\cong\mathbb Z$ 给出的 $\bigwedge^p\check\Lambda\cong\bigwedge^{n-p}\Lambda$、(6.7) $R^pf_*\mathbb Q\cong R^{n-p}\check f_*\mathbb Q$、命题6.102 的证明（$\Gamma(U,i_*R^pf_{0*}\mathbb Q)$ = 单值不变子空间、负型纤维的 $H_1=\mathbb Q^2$、三个单值矩阵 $\begin{pmatrix}1&0&1\\0&1&0\\0&0&1\end{pmatrix}$、$\begin{pmatrix}1&1&0\\0&1&0\\0&0&1\end{pmatrix}$、$\begin{pmatrix}1&-1&-1\\0&1&0\\0&0&1\end{pmatrix}$、$W^\perp=\langle e_1\rangle$）、Leray 谱序列的 $E_2^{p,q}=H^p(B,R^qf_*\mathbb Q)\Rightarrow H^{p+q}(X,\mathbb Q)$、$d_r\colon E_r^{p,q}\to E_r^{p+r,q-r+1}$、$E_{r+1}^{p,q}$ 的分式公式、$H^n(X,\mathbb Q)=F^0\supseteq\cdots\supseteq F^n$ 与 $F^p/F^{p+1}\cong E_\infty^{p,n-p}$、$E_2^{0,1}=E_\infty^{0,1}$、$d_2$ 与 $d_2'$ 皆为零的两次论证（$f^*$ 单射；$\sigma(B)$ 的 Poincaré 对偶类非零）、$E_2$ 页退化、四个同构 $H^0(B)\cong H^0(X(B))$、$H^1(B,R^1f_*)\cong H^2$、$H^2(B,R^2f_*)\cong H^4$、$H^3(B,R^3f_*)\cong H^6$、$H^3(X(B),\mathbb Q)$ 的四步滤过、$\dim F^1/F^2=\dim F^2/F^3$、定理6.103/6.104 的陈述与 $D_\sigma\in H^1(B,R^2f_*\mathbb Q)\cong H^1(B,R^1\check f_*\mathbb Q)\cong H^2(\check X(B),\mathbb Q)$——全部与原文逐行相符。

## 待确认 / 未改（p511-518，供 Lead 判断）

- **定理6.103 陈述（p507）**：原书 "Let $B$ be a three-dimensional simple affine manifold with singularities with holonomy in $\mathbb R^3\rtimes SL_3(\mathbb Z)$"；中译补"**紧、连通**"（"令 $B$ 为紧、连通、带奇点的三维简单仿射流形…"）。这是 §6.4.3 的全局假设（$B$ 紧、简单）且证明中用 $H^0(B,\mathbb Q)=\mathbb Q$（连通）与 $X(B)$ 紧致下的 Poincaré 对偶，属必要的假设补全，未改。
- **ch06-6.4.4-032 末句（p518）**：原书 "the topological (1,1)-coupling on $\check X(B)$ agrees with that predicted by the (1,2)-couplings on the complex moduli space of $\check X(B)$"；中译把第二个 $\check X(B)$ 改为 $X(B)$（"与镜像 $X(B)$ 的复模空间上的 $(1,2)$ 型耦合所预测的结果一致"），另补"在所讨论的大复结构极限退化情形中"。按 SYZ 镜像对偶（$\check X(B)$ 的辛侧 ↔ $X(B)$ 的复侧），中译是正确的、修正了原书疑似笔误，未改。
- **ch06-6.4.4-019（p515）**：原书 "This includes all hypersurfaces in toric varieties"；中译作"本书所考虑的环面簇中的 Calabi--Yau 三维超曲面也包括在内"，把"环面簇中所有超曲面"收窄为"CY 三维超曲面"（结论"基本群有限"不受影响），未改。
- **ch06-6.4.4-023（p516）**：原书 "…$\to E_2^{0,3}=H^0(X,R^3f_*\mathbb Q)$" 中 $H^0(X,\cdot)$ 应为 $H^0(B,\cdot)$；中译已写作 $H^0(B,R^3f_*\mathbb Q)$，属正确修正，未改。
- **ch06-6.4.4-014（p513）**：原书滤过写作 $H^n(X,\mathbb Q)=F^0\supseteq\cdots\supseteq F^n\supseteq 0$；中译写作 $\cdots\supseteq F^n\supseteq F^{n+1}=0$（并把"for each $n$"译为"对于每个总次数 $n$"），等价，未改。
- **ch06-6.4.4-016（p514）**：原书 "if we further assume that $B$ is simply connected ($B=S^3$)"；中译"进一步假定 $B$ 单连通，在这里的紧三维情形中为 $S^3$"，补"紧三维情形"交代了 $B=S^3$ 的前提，正确，未改。
