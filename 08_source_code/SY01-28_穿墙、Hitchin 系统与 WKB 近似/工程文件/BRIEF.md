# BRIEF —— GMN2《Wall-crossing, Hitchin Systems, and the WKB Approximation》中译

- 原文：arXiv:0907.3987v2，180 页（PDF 页 = 印刷页 + 1），LaTeX 源 `00_原文/GMN2_0907.3987/0907.3987v2_src/wkb-paper.tex`（9910 行）
- 作者：Davide Gaiotto, Gregory W. Moore, Andrew Neitzke（IAS / Rutgers NHETC / Harvard，2009）
- 译名：**《穿墙、Hitchin 系统与 WKB 近似》**
- 工程根：`C:\Users\admin\Desktop\GMN系列\01_翻译\GMN2_0907.3987\`
- 规模：14 节 + 附录 A–E；**编号公式约 544 条**（§1 9、§2 11、§3 136、§4 16、§5 41、§6 11、§7 70、§8 5、§9 42、§10 30、§11 57、§12 1、§13 48、§14 8、附录 A 14 / B 17 / C 11 / D 15 / E 2）；**插图约 80 幅**（`figures/*-crop.pdf`，94 个文件）

## 一、这篇文章在讲什么（给没读过原文的人）

**一句话**：给 GMN1 那座「达布坐标 + 黎曼–希尔伯特问题」的大厦换一个**纯几何的地基**——用黎曼面上 Higgs 丛谱曲线（Seiberg–Witten 曲线）的 **WKB 曲线**所定出的三角剖分，把 $d=4$、$\CN=2$ 理论的达布坐标 $X^\RH_\gamma$ 具体算成 **Fock–Goncharov 坐标**，从而在**任意半径 $R$**（不只是 GMN1 成立的大 $R$）下给出 $X^\RH_\gamma$，并顺带得到一个**计算 BPS 谱的算法**。

**逻辑链**（五步，任何一节译文都不能与它冲突）：

1. **理论从哪来**：本文处理 class $\CS$（"six"）——六维 $(2,0)$ 超共形理论在带 punctures（= 缺陷算符）的黎曼面 $C$ 上约化。再在 $S^1$ 上约化到三维，低能是靶空间为 $\CM$ 的 sigma 模型，而 $\CM$ 正是 $C$ 上 **Hitchin 系统**的解模空间（Hitchin 方程 (1.1)–(1.3)）。
2. **为什么能用 Fock–Goncharov**：Hitchin 模空间 $\CM$ 同时是**平坦联络**模空间：给定 Hitchin 解，$\CA=\frac{R}{\zeta}\varphi+A+R\zeta\bar\varphi$（(1.8)）对一切 $\zeta\in\IC^\times$ 平坦；反之亦然。于是 Fock–Goncharov 的三角剖分坐标（平坦联络模空间的坐标）可以直接用在 $\CM$ 上。
3. **选哪个三角剖分（全文的钥匙）**：取 **WKB 三角剖分** $T_\WKB(\vartheta,\lambda^2)$——由相位 $\vartheta$ 的 WKB 曲线 $\langle\lambda,\p_t\rangle=e^{i\vartheta}$ 生成的理想三角剖分，每个 puncture 处再加"小平坦截面"的 decoration。这样得到的 $X^\vartheta_\gamma$ **天生**满足 P1（泊松括号）与 P2（$\zeta\to0,\infty$、$R\to\infty$ 时趋于半平坦坐标 $X^{\sf}_\gamma$）——这正是这个定义被设计出来的理由。
4. **P3 从哪来**：$\vartheta$ 变化时三角剖分只经历三种初等变换 —— **flip**（翻转一条边）、**juggle**（不同 limit triangulation 之间）、**pop**（换掉某顶点的特征线）。它们恰好发生在 $\vartheta$ 等于某条 BPS 射线倾角时，而 $X^\vartheta_\gamma$ 的跳变恰好是 KS 变换 $\CK_\gamma^{\Omega(\gamma;u)}$（超多重态 ↔ flip，矢量多重态 ↔ juggle）。于是 P3 也自动满足。
5. **算谱**：把 $\vartheta$ 连续转 $\pi$，净变换 = 所有 pop 同时做（**omnipop**）的变换 $\mathbf{S}=\prod\CK_\gamma^{\Omega(\gamma;u)}$（按 $\arg Z_\gamma$ 排序）。$\mathbf{S}$ 可以**显式算出**，其乘积分解唯一，于是直接读出整个 BPS 谱 —— 这就是**谱生成元**算法，且**不需要**预先知道 BPS 中心荷的相位。

**技术内核**（第 5、6、7 节，全文最硬）：

- **WKB 曲线 / 谱网络**：$w=\int^z_{z_0}\lambda$ 中为直线、相位 $e^{i\vartheta}$；一般 WKB 曲线被奇点"俘获"，两端落在 puncture 上；**有限** WKB 曲线（闭合，或两端在分支点上）↔ BPS 态（Klemm–Lerche–Mayr–Vafa–Warner）。
- **Fock–Goncharov 交比坐标**：由四条平坦截面的交比定义 $X^T_E$（(5.2)、(7.3)、(7.4)），带 cluster 变换性质；decorated triangulation、limit triangulation 的群胚（flip/juggle/pop 生成全部态射）。
- **辛几何**：Hitchin 模空间的全纯辛形式 $\varpi_\zeta=\frac12\int_C\Tr\delta\CA\wedge\delta\CA$（(1.9)=(4.10)），Fock–Goncharov 坐标的泊松括号取简单形式 (5.9)，P1 由此自然得到（§5.4–5.5 + 附录 B）。
- **$R\to\infty$**：与 $C$ 上的 sinh-Gordon 方程（及其推广）的联系（§13），由此控制 $X^\vartheta_\gamma$ 的奇点结构。
- **二次加细**（quadratic refinement，§7.7）、**谱生成元的代数计算**（§11.1）。

**读者定位**：读过 GMN1（至少其 §2、§5）的数学物理读者；本文是 GMN1 的续篇，也是「谱网络 / 穿墙」这一整套机器（后来 GMN 第 3 篇、GMW 两篇）的起点。数学读者可从 §4、§5 切入，跳过 §3 的膜构造。

## 二、分块与页映射

页：**印刷页**（PDF 页 = 印刷页 + 1；PDF p1 是标题页，p2–5 是目录，§1 从 PDF p5 起）。
行号：`wkb-paper.tex`。式数为按 PDF「行末 (x.y)」统计的估计值，跨页边界有 ±1~3 误差，**译前须回原文复核**。

| 块 | 内容 | 印刷页 | PDF 页 | 原文行号 | 式数(估) | 目标文件 | 状态 |
|---|---|---|---|---|---|---|---|
| ch01 | §1 A narrative table of contents（全文导读） | 4–14 | 5–15 | 325–1031 | 9 | `chunks/ch01.tex` | ✅ 样板已译 |
| ch02 | §2 Review（2.1 Setup / 2.2 Darboux coordinates / 2.3 Wall-crossing / 2.4 RH problem） | 14–18 | 15–19 | 1032–1373 | 11 | `chunks/ch02.tex` | ⬜ |
| ch03 | §3.1 Compactifying the (2,0) theory（3.1.1–3.1.8：$\IR^{1,5}$ → $\IR^{1,3}\times C$ → BPS 弦 → 电荷格 → 动能项 → Hitchin 方程 → 缺陷与几何 Langlands → 五膜交叠的边界条件） | 19–31 | 20–32 | 1374–2190 | 38 | `chunks/ch03.tex` | ⬜ |
| ch04 | §3.2.1–3.2.3 Witten 构造：Type IIA / M 理论提升 / 共形箭图（含弱耦合、SW 曲线、例子） | 32–41 | 33–42 | 2191–2793 | 34 | `chunks/ch04.tex` | ⬜ |
| ch05 | §3.2.4–3.2.7 映射到 Hitchin 系统 / 带基本物质的线性共形箭图 / 弯膜与不规则奇点 / 渐近自由情形 | 42–54 | 43–55 | 2794–3263 | 58 | `chunks/ch05.tex` | ⬜ |
| ch06 | §3.2.8–3.2.9（意外的同构、非阿贝尔味对称）+ §3.3 Type IIB 构造 + §4 Hitchin systems（4.1 模空间 / 4.2 超凯勒结构 / 4.3 缺陷的另一种看法） | 55–62 | 56–63 | 3264–4061 | 19 | `chunks/ch06.tex` | ⬜ |
| ch07 | §5 Fock–Goncharov coordinates（5.1 定义 / 5.2 单值 / 5.3 计数 / 5.4 哈密顿流 / 5.5 泊松括号 / 5.6 群胚 / 5.7 flip / 5.8 pop / 5.9 juggle） | 63–75 | 64–76 | 4062–4707 | 41 | `chunks/ch07.tex` | ⬜ |
| ch08 | §6 The WKB triangulation（6.1 WKB 曲线 / 6.2 局部 / 6.3 整体 / 6.4 定义 / 6.5 decoration / 6.6 跳变） | 76–83 | 77–84 | 4708–5109 | 10 | `chunks/ch08.tex` | ⬜ |
| ch09 | §7.1–7.5 同调标记 / 典范坐标的定义 / 简单性质 / 渐近行为 / 到 KS 辛同胚 | 84–89 | 85–90 | 5110–5418 | 22 | `chunks/ch09.tex` | ⬜ |
| ch10 | §7.6–7.8 特殊 $\vartheta$ 处的跳变 / 二次加细 / 关于全谱的评论 | 90–99 | 91–100 | 5419–5954 | 46 | `chunks/ch10.tex` | ⬜ |
| ch11 | §8 Irregular singularities + §9.1–9.3（线性 $SU(2)$ 箭图与参数空间 / 标度极限 / Hitchin 系统） | 100–106 | 101–107 | 5955–6356 | 18 | `chunks/ch11.tex` | ⬜ |
| ch12 | §9.4.1–9.4.5 例子 $N=1,2,3$（含 Taub-NUT、辛同胚与单值两段 intermission） | 107–115 | 108–116 | 6357–6845 | 20 | `chunks/ch12.tex` | ⬜ |
| ch13 | §9.4.6 $N=4$ + §9.5 一般 $N$ 与 associahedron | 116–122 | 117–123 | 6846–7107 | 9 | `chunks/ch13.tex` | ⬜ |
| ch14 | §10.1–10.3 SU(2) 规范理论：$N_f=0$ / $N_f=1$ / $N_f=2$ 第一种实现 | 123–131 | 124–132 | 7108–7511 | 15 | `chunks/ch14.tex` | ⬜ |
| ch15 | §10.4–10.7 非阿贝尔味对称与 WKB 三角剖分（intermission）/ $N_f=2$ 第二种实现 / $N_f=3$ / $N_f=4$ 超共形 | 132–140 | 133–141 | 7512–7872 | 14 | `chunks/ch15.tex` | ⬜ |
| ch16 | §11 The spectrum generator（11.1 omnipop / 11.2 $N=3$ / 11.3 $N=4$ / 11.4–11.6 SU(2) 各例） | 141–151 | 142–152 | 7873–8420 | 54 | `chunks/ch16.tex` | ⬜ |
| ch17 | §12 Categorical matters + §13 $R\to\infty$ limit（13.1–13.7，sinh-Gordon）+ §14 Comparison with [1] | 152–163 | 153–164 | 8421–9207 | 57 | `chunks/ch17.tex` | ⬜ |
| ch18 | 附录 A Expressing monodromy matrices in terms of Fock–Goncharov coordinates | 164–168 | 165–169 | 9232–9524 | 14 | `chunks/appA.tex` | ⬜ |
| ch19 | 附录 B Computing the Hamiltonian flows + 附录 C WKB error analysis | 169–171 | 170–172 | 9525–9759 | 28 | `chunks/appB.tex` `chunks/appC.tex` | ⬜ |
| ch20 | 附录 D Holomorphic coordinates on multi-center Taub-NUT + 附录 E Configurations of integers with nonpositive second discrete derivative | 172–179 | 173–180 | 9760–9909 | 17 | `chunks/appD.tex` `chunks/appE.tex` | ⬜ |

合计 **20 块**（15–20 块目标达成），每块 3–17 页；最大块 ch05/ch17（17 / 12 页）。

## 三、施工流程（每一块都照此走）

1. **通读原文**：按上表行号读整块，先读懂再落笔；卡住处记 `work/02_疑点清单.md`。
2. **数式**：落笔前先数本块「行末 (x.y)」条数，与上表核对（差 > 2 说明行号切偏）。
3. **对术语**：查 `04_共享/术语/glossary_master.tsv`；缺的追加（含依据：原文式号或定义所在节）。
4. **落笔**：写 `源码/chunks/chNN.tex`；公式逐字符核对（$\pm$、上下标、$\zeta$ 与 $\bar\zeta$、$R$ 与 $R^{-1}$、$\vartheta$ 与 $\theta$）。
5. **编译**：`cd 源码 && xelatex -interaction=nonstopmode main.tex` ×3；0 error、overfull > 3pt 要修、无 `??`、无未定义引用。
6. **自检 + 记账**：段数对照、脚注对照、图号对照；更新本表状态、`进度.md`、`排期.md`。

## 四、质量标准（不可让步）

- **忠实**：不增删论点；「we expect / it would be interesting / we do not understand」这类语气原样保留，不许升格为断言。
- **公式**：编号与原文 $(x.y)$ 逐节对齐；带编号一律 `equation`/`align`，原文不编号才用 `\[...\]`；**不得增删公式**。
- **术语**：全库统一（见 STYLE_GUIDE 硬性表）；新术语入表后才用；`glossary_master.tsv` 旧行**一个都不许改**。
- **中文**：可读的数学中文——长句拆开、逻辑词显式、专名保留拉丁原文。
- **译注**：只在「按字面会误解」处加（术语首现 / 原文笔误 / 跨篇引用），≤120 字。

## 五、交付物

- `成品/GMN2_穿墙-Hitchin-WKB_全文中译_v1.0.pdf`（合稿后）
- `资料卡/` 五件套（00-速览 / 01-结果清单 / 02-论证地图 / 03-条款索引 / 04-术语文献勘误）
- `工程文件/work/`：通读笔记、疑点清单、本篇术语补充表
- `工程文件/reports/`：每块施工记录

## 六、已知坑

1. **原文宏有毒，不能抄**：`\def\a{\alpha} \def\b{\beta} \def\c{\check} \def\p{\partial} \def\la{\langle} \def\ra{\rangle} \def\re{...} \def\im{...}` 这些单字母宏会与 LaTeX 的 `\c`（重音）、`\b`（重音）冲突；`\def\be{\bar{e}}` **不是**公式环境（原文另有 `\be…\ee` 的用法只有 2 处）。译文一律写完整命令。
2. **`\sect` 宏会重置式号**：原文 `\newcommand{\sect}[1]{\setcounter{equation}{0}\section{#1}}`，即某些节用 `\sect` 手动把式号归零。译文用 `\numberwithin{equation}{section}` 复现，但若原文某节实际用了 `\section` 而非 `\sect`，式号会整体错位 —— 每块译完必须抽 5 条回 PDF 核对。
3. **图是全新工作量**：原文 80 处 `\insfig{宽}{名字}{图注}` → `figures/名字-crop.pdf`（94 个文件）。需在 preamble 定义 `\insfig`，并按块把用到的图复制进 `源码/figures/`。GMN1 无插图，无先例可抄。
4. **三种"墙"必须分开译**：① 模空间的**边缘稳定墙**（wall of marginal stability，穿墙的墙）；② §6.2 局部行为里 WKB 曲线与 anti-WKB 曲线夹出的**壁**；③ 三角剖分的**边**（edge）。三者混用会读不懂 §6–§7。
5. **`turning point` 冻结译名是「转向点」**（术语表第 72 行），不是交接说明里写的「转折点」；不改旧行，记入疑点清单。
6. **谱网络有三次记法**：§6 的 WKB 曲线族、§7 的有限 WKB 曲线、§8 对 irregular 奇点的改写（"故事类似，作如下修改"）。定义以 §6.4 为准。
7. **三个 $X$ 不可混用**：$\CX^\RH_\gamma$（GMN1 的达布坐标）、$\CX^\vartheta_\gamma$（本文构造的）、$\CX^T_E$（Fock–Goncharov 坐标）；本文的全部内容就是把后两者接到第一个上。上标一旦写错，整段论证失效。
8. **`\CP_i` 是 puncture 的记号**（$\mathcal P_i$），不是射影空间；`\nsing` 是 puncture 个数。
9. **`\N` 是 $\mathcal N$（超对称数）**，`\CN` 同；不要与规范群 $N$（如 $N_f$ 的 $N$）混。
10. **§3 可以快，但别跳**：它是全篇的物理来源（膜构造 → Hitchin），数学读者可跳读，译者不能（大量术语首现于此）。
