# 校对报告：tr-05 块（原文 pp.64–76；`tr05a.tex` / `tr05b.tex` / `tr05c.tex`）

校对人：tr-01　｜　日期：2026-11-03　｜　底本：arXiv:2006.14025v3
核对依据：`work/pages/p064–p076.png`（200 dpi 整页）+ 关键公式 700–2400 dpi 局部放大（`work/tmp/crop_tr01.py`）、`work/split/p064–p076.txt`、`work/tags_bypage.txt`、`work/glossary.tsv`、原 PDF 矢量层（`pymupdf get_drawings` 用于核对箭图几何）。
**未改动 `tr05a/b/c.tex` 任何字节**；报告中的行号以 2026-11-03 10:41 的文件状态为准。

## 0. 结论速览

| 项 | 结果 |
|---|---|
| tag 完整性 | **33/33 全对**：6.6–6.23（18 条）+ 7.1–7.15（15 条）；页归属与 `tags_bypage.txt` p064–p076 完全一致，无重、无漏、无自造、无错页 |
| 公式逐符号 | 33 条**全部**与图像核对（其中 15 条为重点高倍放大：6.6–6.12、6.16、6.19–6.23、7.1–7.5、7.8、7.15）。**未发现抄写错误**；唯一「记号与原文不同」是 3 处 $\overline{\mathcal F(\cdot)}$ 的上划线为译者所加（见 O1），另有 (7.1) 原文自身 ϕ/φ 混用（见 O2） |
| 结构 | `\part{第三篇…}`、§7 标题、6.2/6.3/7.1/7.2 小节、p.70 无标题要点框（`keyboxplain`）、脚注 50–58（9 条）、习题 6.3 **全部在位且顺序正确** |
| 漏译 | **未发现**漏句/漏段/漏脚注；9 处跨页句子（p.67→68、68→69、70→71、71→72、72→73、73→74、74→75、75→76、76→77）均由本块正确续完 |
| 术语 | 与 `glossary.tsv` 冲突 **1 处**（M1，simple puncture 三种译法并存）；另有 1 条批注推导有误（M2） |
| 体例 | 与全书一致；仅 2 处小差异（O3、O4） |

必须改 **2** 条（M1、M2）｜可选改 **7** 条（O1–O7）。

---

## 1. tag 完整性（p.64–76）

| 页 | `tags_bypage.txt` | `tr05*.tex` 中 `\tag` 行号 | 结果 |
|---|---|---|---|
| p.64 | 6.6, 6.7, 6.8, 6.9 | tr05a:15 / 26 / 49 / 65 | ✓ 4/4 |
| p.65 | 6.10, 6.11, 6.12, 6.13 | tr05a:73 / 85 / 93 / 122 | ✓ 4/4 |
| p.66 | 6.14, 6.15, 6.16, 6.17, 6.18 | tr05a:146 / 154 / 162 / 173 / 186 | ✓ 5/5 |
| p.67 | （无） | — | ✓ 无编号公式 |
| p.68 | 6.19 | tr05b:50 | ✓ 1/1 |
| p.69 | 6.20, 6.21, 6.22, 6.23 | tr05b:64 / 93 / 105 / 124 | ✓ 4/4 |
| p.70 | （无） | — | ✓ |
| p.71 | 7.1, 7.2, 7.3 | tr05b:192 / 203 / 228 | ✓ 3/3 |
| p.72 | 7.4, 7.5, 7.6 | tr05c:22 / 48 / 64 | ✓ 3/3 |
| p.73 | 7.7 | tr05c:83 | ✓ 1/1 |
| p.74 | 7.8, 7.9 | tr05c:172 / 182 | ✓ 2/2（p.74 另一条 "4.26" 是行文引用，非新式，处理正确） |
| p.75 | 7.10, 7.11, 7.12 | tr05c:222 / 242 / 250 | ✓ 3/3（p.75 的 "7.8" 是行文引用，处理正确） |
| p.76 | 7.13, 7.14, 7.15 | tr05c:285 / 293 / 320 | ✓ 3/3 |

页码标注 `% [原文 p.N]`：64–76 共 13 个，连续无缺 ✓。

---

## 2. 公式逐符号核对（Lead 指定的重点式全部覆盖）

**方法**：每式先在 200 dpi 整页定位，再按 bbox 裁 700–2400 dpi 局部放大逐字符比对；箭图用 PDF 矢量层取 bbox 复核几何。

| 式 | 页 | 核对要点 | 结果 |
|---|---|---|---|
| (6.6) | 64 | 求和下标两行（`V,V'` primaries / `Y,Ȳ,Y',Ȳ'` Young diagrams）、$g^{-1}$ 的六个自变量、末尾 $\langle V'\vert\mathbb L_{Y'}\mathbb L_{\bar Y'}V_3V_4\rangle$（原文此处确实**没有**竖线分隔，译文照抄，正确） | ✓ |
| (6.7) | 64 | $C_{125}g^{-1}_{56}C_{634}$、$\mathcal F(h_1,\dots,h_5;z_1,\dots,z_4)$ | ✓（唯 $\overline{\mathcal F(\dots)}$ 见 O1） |
| (6.8)(6.9) | 64 | $S[\phi]$ 的 $\partial_\nu\phi\partial^\nu\phi+QR\phi+4\pi\mu e^{2b\phi}$；$R(\alpha)$ 两个 Γ 比与 $\lambda^{Q-2\alpha}$ 的符号 | ✓ |
| **(6.10)** | 65 | $\delta_{\alpha_1+\alpha_2=Q}+R(\alpha_1)\delta_{\alpha_1=\alpha_2}$（两个 δ 的下标条件，不是差式） | ✓ |
| **(6.11)** | 65 | 分子 $(b^{2/b-2b}\lambda)^{Q-\alpha_1-\alpha_2-\alpha_3}\Upsilon'_b(0)\Upsilon_b(2\alpha_1)\Upsilon_b(2\alpha_2)\Upsilon_b(2\alpha_3)$；分母**四个** $\Upsilon_b$ 的顺序 $\alpha_1{+}\alpha_2{+}\alpha_3{-}Q,\ \alpha_1{+}\alpha_2{-}\alpha_3,\ \alpha_2{+}\alpha_3{-}\alpha_1,\ \alpha_3{+}\alpha_1{-}\alpha_2$ | ✓ 完全一致 |
| **(6.12)** | 65 | $\frac12\int_{Q/2+i\mathbb R}\mathrm d\alpha_s$、$C_{\alpha_1\alpha_2\alpha_s}C_{(Q-\alpha_s)\alpha_3\alpha_4}$、$\lvert q^{h_s-h_1-h_2}(1+O(q))\rvert^2$ | ✓ |
| (6.14) | 66 | $\prod_{\pm\pm}$ 的四因子式、第二行四因子 | ✓ |
| (6.15) | 66 | $(b^{2/b-2b}\lambda)^{\alpha-Q/2}/\Upsilon_b(2\alpha)$ | ✓ |
| **(6.16)** | 66 | 分子 $\delta_{\alpha+\alpha'=Q}+\delta_{\alpha=\alpha'}$；分母**两个** $\Upsilon_b$ 且顺序为 $\Upsilon_b(Q-2\alpha)\Upsilon_b(2\alpha-Q)$（Lead 提示的「双 $\Upsilon_b$ 因子」） | ✓ 完全一致 |
| (6.17)(6.18) | 66 | $\int_{i\mathbb R/\mathbb Z_2}$ 与 $\int_{Q/2+i\mathbb R/\mathbb Z_2}$ 的**积分域不同**（前者无 $Q/2$ 平移）；$q^{h(\alpha)}\bar q^{\bar h(\alpha)}$ | ✓（$\overline{\mathcal F}$ 见 O1） |
| **(6.19)** | 68 | 两项系数 $q/8\pi,\ \tilde q/8\pi$；$\mathrm{Tr}(\mathcal A\wedge\mathrm d\mathcal A+\frac23\mathcal A\wedge\mathcal A\wedge\mathcal A)$；第二项 $\bar{\mathcal A}$ 全带杠；$\mathrm d$ 为**直立体**（原文如此，译文用 `\dd` ✓） | ✓ |
| **(6.20)** | 69 | $k=1$、$s=(1-b^2)/(1+b^2)$（分子 $1-b^2$ 不是 $b^2-1$） | ✓ |
| (6.21) | 69 | 两式 $g=\mathrm dy_5^2+(r^2-y_5^2)g_{S^3_b}+g_C$ 与 $\frac{1}{r^2-y_5^2}g=g_{S^3_b}+\frac{\mathrm dy_5^2+g_C}{r^2-y_5^2}$ | ✓ |
| **(6.22)** | 69 | 横杠位置：第一积分 $\langle\partial\Phi,\bar\partial\Phi\rangle$（**只有第二个 ∂ 带杠**，Φ 不带杠）；第二积分 $\langle\partial\bar\Phi,\bar\partial\bar\Phi\rangle$（两个 Φ 都带杠）与 $e^{\langle e_j,\bar\Phi\rangle}$；两个积分都带 $\dd^2z$、系数 $q/8\pi$ 与 $\tilde q/8\pi$ | ✓ **逐字符一致**（tr05b:96–105） |
| **(6.23)** | 69 | 陪集 $\widehat{\mathfrak{su}}(N)_k/\widehat{\mathfrak u}(1)^{N-1}$（$N$ 与 $k$ 的位置与正文「另一个陪集 $\widehat{\mathfrak{su}}(N)_k/\widehat{\mathfrak u}(1)^{N-1}$」「首个 $\widehat{\mathfrak{su}}(k)_N/\widehat{\mathfrak u}(1)^{k-1}$」的非对称性一致）、$\psi_j\bar\psi_j e^{(b/\sqrt k)\langle e_j,\phi\rangle}$、无 $1/8\pi$ 因子 | ✓ |
| **(7.1)** | 71 | $\frac{1}{8\pi}(\hat g^{ab}\langle\partial_a\phi,\partial_b\phi\rangle+2\langle Q,\varphi\rangle\hat R)+\mu\sum_{i=1}^{\mathrm{rank}\,\mathfrak g}e^{b\langle e_i,\varphi\rangle}$：**势项在 $1/8\pi$ 括号之外**，求和上限是 $\mathrm{rank}\,\mathfrak g$ | ✓（ϕ/φ 见 O2） |
| **(7.2)** | 71 | $h(\alpha)=\frac12\langle\alpha,2Q-\alpha\rangle$（$\frac12$ 因子与 $2Q$ 都正确，属最易抄错处） | ✓ |
| (7.3) | 71 | $W^{(k)}(z)V_\alpha(0)=\frac{w^{(k)}(\alpha)}{z^k}V_\alpha(0)+\cdots$（极点阶数 $z^k$ 与流自旋 $k$ 一致） | ✓ |
| **(7.4)** | 72 | 分子 $\lambda^{\langle\rho,\alpha-Q\rangle}$（**$\rho$ 在前、$\alpha-Q$ 在后**）；分母 $\prod_{e>0}$（**正根**）$\Upsilon_b(\langle Q-\alpha,e\rangle)$；末尾 $V_\alpha(z)$ | ✓ 完全一致 |
| **(7.5)** | 72 | 分母 $\prod_{\text{roots }e}$（**全部根**，不是正根——与 (7.4) 刻意不同）；$\lvert z\rvert^{-4h(\alpha)}$；分子 $\sum_{w\in\mathrm{Weyl}}\delta_{Q-\alpha'=w(\alpha-Q)}$ | ✓ 完全一致 |
| (7.6) | 72 | $\lvert z_1-z_2\rvert^{2h_{12}}\lvert z_1-z_3\rvert^{2h_{13}}\lvert z_2-z_3\rvert^{2h_{23}}$ | ✓ |
| (7.7) | 73 | $\int_{a\in\mathfrak h/\mathrm{Weyl}}$、$\sum_Y$、$\langle\hat V_{Q-a}\hat V_{Q+a}\rangle$ 归一因子、$\hat V^{[Y]}$ 的上标位置 | ✓ |
| **(7.8)** | 74 | TikZ 箭图：2 个圆角 $\mathrm{SU}(N)$ 主节点 + 2 个 $\mathrm{SU}(N)$ 方框（下方） + **4 个** $\mathrm{U}(1)$ 方框（左右叉口各 1、中间 2）+ 中间 $\cdots$；左右叉口的外侧分叉、中间两个 $\mathrm{U}(1)$ 的竖线落在主线上 | ✓ 与 p.74 原图逐一对应（原图 4 个 U(1) 的 x 坐标为 133.6/181.8/210.1/258.3） |
| (7.9) | 74 | $\alpha_j=Q+rm_j$；$\mu_j=\big(\frac N2(b+\frac1b)+rm_j\big)\varpi_1$；"$j=2,\cdots n-1$" 缺逗号处也照原文 ✓ | ✓ |
| (7.10) | 75 | $\int_{a_j\in\mathfrak h/\mathrm{Weyl},\,2\le j\le n-2}$、分子 $n-2$ 个三点函数、分母 $\langle\hat V_{Q+a_2}\hat V_{Q-a_2}\rangle\cdots$ | ✓（$\overline{\mathcal F}$ 见 O1） |
| (7.11)(7.12) | 75 | $(\Upsilon_b(b))^{N-1}\Upsilon_b(\kappa)$ 的**幂次 $N-1$**；$\kappa/N-\langle a_1,h_i\rangle-\langle a_2,h_j\rangle$；$\prod_{i,j=1}^N$ | ✓ |
| (7.13)(7.14) | 76 | $\mu_1=\tilde Q_2Q_2-\frac1N\mathrm{Tr}(\tilde Q_2Q_2)$；$J_1^{\oplus n_1}\oplus\dots\oplus J_\ell^{\oplus n_\ell}$ | ✓ |
| **(7.15)** | 76 | TikZ 箭图尾：链表 $\cdots-N_\ell-N_{\ell-1}-\cdots-N_1$，上方三个方框 $n_\ell,n_{\ell-1},n_1$ 分别接在 $N_\ell,N_{\ell-1},N_1$ 正上方 | ✓ 与 p.76 原图一致（唯一差别是节点形状，见 O6） |

> 补充核对：(6.22) 的横杠、(6.16) 的双 $\Upsilon_b$、(7.4)/(7.5) 的「正根 vs 全部根」这三处正是本块最容易抄错的地方，均为 **PASS**，可以放心并入。

---

## 3. 结构核对

| 检查项 | 期望 | 现状 | 结果 |
|---|---|---|---|
| `\part{第三篇\quad AGT 的推广}` | 原文 p.70 中部（在 para-Toda 讨论之后、§7 标题之前） | `tr05b.tex:140`，位于 p.70 段之后、`\section`（:142）之前 | ✓ |
| §7 标题 | "General class S theories" → 「一般 class S 理论」 | `tr05b.tex:142` | ✓ |
| 6.2 / 6.3 小节 | "Finding the AGT dictionary" / "Liouville from 6d" | `tr05a.tex:116` / `:224` | ✓ |
| 7.1 / 7.2 小节 | "Toda CFT" / "Higher rank AGT correspondence" | `tr05b.tex:174` / `tr05c.tex:108` | ✓ |
| p.70 要点框 | 原文**无深色标题条**的灰底框（5 条 bullet） | 用 `keyboxplain`（`tr05b.tex:154`），5 条 bullet 齐全，无标题条 | ✓（preamble 已定义该环境） |
| 脚注 50–58（9 条） | 位置依次：p.67 瞬子配分函数后、p.68「quotients thereof」、p.70 simply-laced、p.71 共形维数后、p.71 early review 后、p.72 (7.4) 前、p.72 precise condition、p.73 non-Lagrangian、p.75 differential equation | 依次在 tr05a:204、tr05b:6、tr05b:181、tr05b:199、tr05b:215、tr05c:16、tr05c:32、tr05c:112、tr05c:234，共 9 条 | ✓ |
| 习题 | 本块仅 Exercise 6.3（p.65） | `tr05a.tex:107` | ✓（编号体例见 O4） |
| 要点框数 | p.70 一个 | 1 个 `keyboxplain` | ✓ |

---

## 4. 漏译与跨页核对

对照 `split/p064–p076.txt` 逐段比对，**未发现整段/整句缺失**。逐页首尾衔接：

| 边界 | 原文上一句结尾 / 下一句开头 | 译文处理 | 结果 |
|---|---|---|---|
| p.67→p.68 | "…performed this reduction in three steps:" / "$\mathcal X(\mathfrak g)$ reduced on $S^1$ yields 5d…" | tr05a 末句写完，tr05b 从 p.68 正文起，无重复 | ✓ |
| p.68→p.69 | "…with action (6.19)" / "subject to $G_\mathbb C$ gauge invariance stemming from…" | (6.19) 后接 tr05b:59「它在来自通常规范不变性与虚规范不变性的 $G_\C$ 规范不变性下成立。」 | ✓ |
| p.70→p.71 | "…describes a real scalar field $\phi\in\mathfrak h$" / "subject to the Lagrangian density" | tr05b:184 末「…描述一个实标量场 $\phi\in\fh$，」+ tr05b:187「其拉氏量密度为」 | ✓ |
| p.71→p.72 | "…the quantum" / "numbers $w^{(k)}(\alpha)$ simplify to…" | tr05b 末「量子的」+ tr05c:8「数 $w^{(k)}(\alpha)$ 简化为…」 | ✓ |
| p.72→p.73 | "(7.6)" / "where $h_{ij}=h(\alpha_i)+h(\alpha_j)-h(\alpha_k)$" | tr05c:68 | ✓ |
| p.73→p.74 | "A large program to" / "classify tinkertoys has been carried out by…" | tr05c:118 一句写完「Chacaltana 与 Distler 及其合作者…开展了对 tinkertoy 分类的大型研究计划」 | ✓ |
| p.74→p.75 | "…the action" / "of arbitrary $W_N$ generators can be converted…" | tr05c:197「任意 $W_N$ 生成元的作用」+ tr05c:200「都可以转成 Virasoro 生成元的作用」 | ✓ |
| p.75→p.76 | "…the one-loop determinants of $N^2$ hypermultiplets" / "on $S^4_b$ with suitable masses." | tr05c:262「即 $S^4_b$ 上、带适当质量的 $N^2$ 个超多重态的单圈行列式」 | ✓ |
| p.76→p.77 | "(which is" / p.77 "the length of the j-th row)…" | tr05c:323–324 写完「（后者即第 $j$ 行的长度）。换言之，$N_j$ 计数第 $1,\cdots,j$ 行中的全部方块，特别地 $N_\ell=N$。」——按「开始者写完」正确；tr-06 应从 p.77 的 "The flavour symmetry is (7.16)" 起，**不要**重复写这句 | ✓ |
| 段内小句 | 全部核对 | 无漏 | ✓ |

---

## 5. 必须改

### M1 —— `simple (tame) puncture` 在同一块内有三种译法，且与 `glossary.tsv` 冲突

- **原文（p.74，两处长式）**：
  - "Besides full and simple tame punctures, there are other tame punctures…"
  - "The U(1) flavour symmetries correspond to **simple tame punctures** where each $\phi_k$ has a simple pole…"
- **glossary 冻结**：`full/simple tame puncture → 满驯服穿刺/单驯服穿刺`。
- **现状（`tr05c.tex`）**：
  - `tr05c:114`：「另一类驯服穿刺点（称为**简单穿刺点**）」← 原文 "simple punctures"（命名处）
  - `tr05c:116`：「除满与**单驯服穿刺点**之外」← 原文 "full and simple tame punctures"（长式）
  - `tr05c:138`：「…对应于**简单驯服穿刺点**」← 原文 "simple tame punctures"（长式）
  - `tr05c:206` / `tr05c:273`：「**简单穿刺点**」「**满穿刺点**」← 原文 "simple/full punctures"（短式）
  
  即同一术语出现「简单穿刺点 / 简单驯服穿刺点 / 单驯服穿刺点」三种形态，其中 116 与 138 都是长式却不同译。
- **建议改法**（最小改动、兼顾原文长短式）：
  1. `tr05c.tex:138`：`简单驯服穿刺点` → `单驯服穿刺点`（与 :116 一致、合 glossary）。
  2. `tr05c.tex:114`：`（称为简单穿刺点）` → `（称为单驯服穿刺点）`，使命名处即用全称。
  3. 若要更严格：把 :206、:273 的「简单穿刺点/满穿刺点」保留为短式（原文这里确实用短式 "simple/full puncture"），但建议在首次出现处加一句「（下文简称为单穿刺点、满穿刺点）」；或者全篇统一用全称，不再区分长短式。二者取其一即可。
- **影响**：仅术语一致性，不影响编译与数学内容。

### M2 —— `tr05a.tex:98–105` 的 Tutor Note 中，(6.11)↔(6.14) 的「反射配对」推导写错了

- **现状（`tr05a.tex:98–105`，编译不显示，但会进《译注汇总》）**：
  > 「…逐项展开 (6.14) 中 $\prod_{\pm\pm}$ 的四种符号：$\alpha_1+(\alpha_2-Q/2)+(\alpha_3-Q/2)$ **与** $\alpha_1-(\alpha_2-Q/2)-(\alpha_3-Q/2)$ **由该反射性互相等同**，余下两个为 $\alpha_1+(\alpha_2-Q/2)-(\alpha_3-Q/2)$、$\alpha_1-(\alpha_2-Q/2)+(\alpha_3-Q/2)$，**再用 $\Upsilon_b(Q-x)=\Upsilon_b(x)$ 把它们化成** $\Upsilon_b(\alpha_2+\alpha_3-\alpha_1)$ 与 $\Upsilon_b(\alpha_3+\alpha_1-\alpha_2)$…」
- **验算**（四个自变量）：
  $$\begin{aligned}
  \text{①}&=\alpha_1+\alpha_2+\alpha_3-Q &&(= \text{(6.11) 第 1 因子，直接对应})\\
  \text{②}&=\alpha_1+\alpha_2-\alpha_3 &&(= \text{第 2 因子，直接对应})\\
  \text{③}&=\alpha_1-\alpha_2+\alpha_3=\alpha_3+\alpha_1-\alpha_2 &&(= \text{第 4 因子，直接对应})\\
  \text{④}&=\alpha_1-\alpha_2-\alpha_3+Q &&(\text{需一次反射})
  \end{aligned}$$
  只有 ④ 需要反射：$\Upsilon_b(\alpha_1-\alpha_2-\alpha_3+Q)=\Upsilon_b\big(Q-(\alpha_1-\alpha_2-\alpha_3+Q)\big)=\Upsilon_b(-\alpha_1+\alpha_2+\alpha_3)=\Upsilon_b(\alpha_2+\alpha_3-\alpha_1)$，恰为 (6.11) 第 3 因子。
- **为什么现批注不对**：① 与 ④ 相差 $2(\alpha_1-Q/2)$，只有 $\alpha_1=Q/2$ 时才相等，一般情形下 $\Upsilon_b(①)\ne\Upsilon_b(④)$；而 ③ 本身已经是 $\alpha_3+\alpha_1-\alpha_2$，不需要反射。结论（(6.11) 与 (6.14) 的分母一致）本身是对的，但配对被张冠李戴。
- **建议改法**（把 `tr05a.tex:100–103` 那三行批注替换为）：
  ```
  %   逐项展开 (6.14) 中 $\prod_{\pm\pm}$ 的四种符号，四个自变量为
  %   $\alpha_1+\alpha_2+\alpha_3-Q$、$\alpha_1+\alpha_2-\alpha_3$、$\alpha_1-\alpha_2+\alpha_3$、$\alpha_1-\alpha_2-\alpha_3+Q$；
  %   前三个直接就是 (6.11) 分母的第 1、2、4 因子（注意 $\alpha_1-\alpha_2+\alpha_3=\alpha_3+\alpha_1-\alpha_2$），
  %   第四个用一次反射 $\Upsilon_b(Q-x)=\Upsilon_b(x)$：$\alpha_1-\alpha_2-\alpha_3+Q\mapsto-\alpha_1+\alpha_2+\alpha_3=\alpha_2+\alpha_3-\alpha_1$，
  %   恰是 (6.11) 分母的第 3 因子。故两者分母逐因子相等。
  ```

---

## 6. 可选改

### O1 —— (6.7)/(6.18)/(7.10) 的第二个共形块多加了外层 `\overline`
- **原文**（p.64 (6.7)、p.66 (6.18)、p.75 (7.10)，均以 1000–2000 dpi 放大确认）：作者写的是
  $$\mathcal F(h_1,\dots;z_1,\dots)\,\mathcal F(\bar h_1,\dots;\bar z_1,\dots),\qquad
  \mathcal F(\alpha_i,\alpha;q)\,\mathcal F(\alpha_i,\alpha;\bar q),\qquad
  \mathcal F(z)\,\mathcal F(\bar z)$$
  即**第二个 $\mathcal F$ 本身不带横线**，只有自变量带杠。
- **现状**：`tr05a.tex:25`、`tr05a.tex:184`、`tr05c.tex:220` 都写成 `\overline{\mathcal F(\bar\cdots)}`。
- **说明**：数学上完全等价（$\mathcal F$ 全纯），且 `\overline{\mathcal F(\bar z)}` 是更常见的记号；但严格按「逐符号照抄」体例应去掉外层上划线。
- **建议**：三处统一改为 `\mathcal{F}(\bar h_1,\dots,\bar h_5;\bar z_1,\dots,\bar z_4)`、`\mathcal{F}(\alpha_i,\alpha;\bar q)`、`\mathcal{F}(\bar z)`；若想保留上划线，则在同一处加一条批注说明「原文此处无上划线，仅自变量带杠，译文为记号清晰加」。二选一，**不要**两者都不做（这三处是本次唯一发现的「公式记号与原文不同」处，不处理会被下一位校对人反复提出）。

### O2 —— (7.1) 原文内部 ϕ/φ 不一致，译文统一成了 `\phi`
- **原文**（p.71，(7.1) 2400 dpi 放大）：第一项 $\langle\partial_a\phi,\partial_b\phi\rangle$ 用的是 **ϕ（phi，竖笔贯穿）**，而 $2\langle Q,\varphi\rangle\hat R$ 与 $e^{b\langle e_i,\varphi\rangle}$ 用的是 **φ（varphi，圈形）**——即**同一条公式内部两符号混用**（正文 "a real scalar field $\phi\in\mathfrak h$" 等处从 200 dpi 看是 φ，未逐处放大）。
- **现状**：`tr05b.tex:189–191` 全用 `\phi`，内部自洽。
- **建议**：保持现状（更自洽），可在 (7.1) 后加一句批注指出原文两符号混用、译文统一；若 Lead 要求逐符号照抄，则把 (7.1) 第二、三项改成 `\varphi`（但正文也要跟着改，工作量大于收益）。

### O3 —— p.70 要点框的位置把「First/Second」结构拆开了
- **原文版式**（p.70）：框是右缘浮动框，与「Second, in subsection 7.3…」这一段**并排**（框 y 733–965，该段 y 745–900）；「The 6d (2,0) theory…in subsection 7.2.」段在框上方。
- **现状**：`tr05b.tex:154–162` 的 `keyboxplain` 插在「…in subsection 7.2.」（:151 结束）之后、「其次，在 7.3 小节中…」（:164）之前。
- **建议**：把 `keyboxplain` 整块移到 :167 之后（即「Second」段之后）。这样「we now extend the story in two ways →（一）→（二）」连续不断，框作为本节总览落在 §7.1 之前。纯排版顺序，不影响内容。

### O4 —— 习题 6.3 的小问编号用手工 "1." "2."
- **原文**（p.65）：Exercise 6.3 是 1./2. 两项的编号列表。
- **现状**：`tr05a.tex:107–114` 在 `exercise` 环境内直接写「1. …」「2. …」（且 `exercise` 环境整体是 `\itshape`，编号也会被斜体化）。
- **建议**：与全书其它习题（如块 1 的习题 2.1、tr-03 的习题）统一，改成 `\begin{enumerate}[label=\arabic*.,leftmargin=1.6em]`；若希望忠实原文的斜体效果，可保留现状。属体例统一，非必须。

### O5 —— `tr05c.tex:332–334` 的批注已过时
- 现文：「p.70 的灰底要点框在原文中并无标题条…故 p.70 处 keybox 的标题参数留空；若编译后出现一条空白深色标题条，那是排版副作用，可在 preamble 的 keybox 定义中加 no-title 处理。」
- 实际：preamble 已有 `keyboxplain`（preamble:75），`tr05b.tex:154` 用的就是它，不会有空标题条。
- **建议**：删除该批注，或改成一句「p.70 框无标题条，用 `keyboxplain` 排版」。

### O6 —— (7.15) 的节点形状与原文略有差异
- 原文（p.76）：$N_j$ 节点是**圆形/椭圆**（矢量层 `get_drawings` 显示为闭合曲线），译文用圆角矩形（`tnd` 样式，`tr05c.tex:302–319`）。
- 建议（可做可不做）：把 `tnd` 改为 `circle,minimum size=6mm`（或 `ellipse`），使与 p.76 原图形似；不影响含义。

### O7 —— 习题 6.3 第 2 问的 "fixed generic $\alpha_1,\alpha_2$"
- **原文**："…show that at fixed **generic** $\alpha_1,\alpha_2$, the $\alpha_3\to0$ limit of $C_{\alpha_1\alpha_2\alpha_3}$ vanishes."
- **现状**（`tr05a.tex:111`）：「证明在固定的**普遍** $\alpha_1,\alpha_2$ 下…」——`generic` 译成「普遍的」不准确（此处是「一般位置/非特殊取值」之意，且与「固定」连用别扭）。
- **建议**：改为「在固定的、一般（generic）的 $\alpha_1,\alpha_2$ 下」。

---

## 7. 附：核对过程中确认无误的易错点（供 Lead 抽查时快速定位）

1. (6.22) 第一积分 $\langle\partial\Phi,\bar\partial\Phi\rangle$ 的 Φ **不带杠**、第二积分两个 Φ **都带杠**——已 2400 dpi 逐字确认，译文正确（这是本块最易抄错处）。
2. (7.4) 用正根 $\prod_{e>0}$、(7.5) 用全部根 $\prod_{\text{roots }e}$——两者刻意不同，译文未统一，**正确**。
3. (6.16) 分母是两个 $\Upsilon_b$（$Q-2\alpha$ 与 $2\alpha-Q$），不是单个。
4. (7.1) 势项 $\mu\sum e^{b\langle e_i,\varphi\rangle}$ 在 $\frac{1}{8\pi}$ 括号**外**。
5. (7.2) 的 $\frac12$ 与 $2Q$ 都在。
6. (6.19) 的 $\mathrm d$ 直立体、$\frac23$ 系数、$\bar{\mathcal A}$ 的横杠数。
7. (7.8)/(7.15) 的箭图节点/连线/标签与 PDF 矢量层几何逐一对应（U(1) 4 个、SU(N) 主节点 2 + 方框 2；尾图 3 个方框 3 个圆节点）。
