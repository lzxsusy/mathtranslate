# 规范场论中的进阶专题：Higgs 丛的数学与物理 —— 中文译注本

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> Laura P. Schaposnik, *Advanced topics in gauge theory: mathematics and physics of Higgs bundles*,
> arXiv:1907.09800v1 [math-ph]（PCMI 2019 研究生暑期学校短课程讲义）的中文译注本。
> 版本：v1.0（2026-11-04）；底本 53 页；成品 45 个印刷页（前置 i–ii + 正文 1–40 + 参考文献 41–45）。

## 一、底本信息与页码映射

| 项 | 值 |
|---|---|
| 作者 | Laura P. Schaposnik（University of Illinois at Chicago） |
| 标题 | Advanced topics in gauge theory: mathematics and physics of Higgs bundles |
| 来源 | arXiv:1907.09800v1 [math-ph]，2019-07-23；PCMI 2019 Graduate Summer School 讲义 |
| 底本 PDF | 53 页，单栏，letter（612×792 pt），PDF 页号 = 印刷页码（偏移 0） |
| 译本 | 45 个印刷页；LuaLaTeX 编译 3 遍，0 error / 0 undefined / 0 missing character |

**页码映射（章节级）**。原文正文 pp.1–48 按页序翻译；译文因中文更紧凑，页数少于原文（48 → 40 页），
逐页精确定位请看源码：**每一个原文页的起始处都有 `% [原文 p.N]` 注释**（源码与 `src/chunks/` 中可直接检索）。

| 原文 | 译本 | 原文 | 译本 | 原文 | 译本 |
|---|---|---|---|---|---|
| §1 引言 p.1–2 | p.1 | §3.3 奇异轨迹 p.22 | p.18 | §5 对应关系 p.39 | p.32 |
| §2 模空间的几何 p.3 | p.1 | §3.4 问题集 II p.24 | p.19 | §5.1 群同胚 p.39 | p.32 |
| §2.1 复群 p.3 | p.2 | §4 膜 p.26 | p.21 | §5.2 多边形/超多边形 p.42 | p.34 |
| §2.2 实 Higgs 丛 p.6 | p.4 | §4.1 有限群作用 p.26 | p.22 | §5.3 Langlands 对偶 p.45 | p.37 |
| §2.3 抛物 Higgs 丛 p.7 | p.5 | §4.2 反全纯对合 p.29 | p.24 | §5.4 问题集 IV p.47 | p.38 |
| §2.4 野 Higgs 丛 p.8 | p.6 | §4.3 问题集 III p.37 | p.30 | 致谢 p.49 | p.39–40 |
| §2.5 问题集 I p.13 | p.10 | §3 纤维化的几何 p.15 | p.12 | 参考文献 p.49–53 | p.41–45 |
| §3.1 Teichmüller 分支 p.15 | p.12 | §3.2 正则纤维 p.16 | p.14 | — | — |

## 二、结构清单（已逐项实测）

- **5 章 16 小节**：§1；§2（2.1–2.5）；§3（3.1–3.4）；§4（4.1–4.3）；§5（5.1–5.4）。
- **编号条目 46 条**：定理/命题/引理/定义/例/注/猜想/图/表（原文在每节内使用**统一递增计数器**，
  如 §2 中「例 2.10」之后紧接「式 (2.12)」；本译本严格照抄原文编号，未重排）。
- **编号公式 20 条**：(2.7)(2.8)(2.12)(2.17)(2.18)(2.21)(2.23)；(3.2)(3.3)(3.5)(3.8)(3.9)；
  (4.5)(4.6)(4.10)(4.11)(4.13)；(5.1)(5.2)(5.4)。编号印在左侧（与原文版式一致，文档类用 `leqno`）。
- **习题 20 道**（Problem 1–20，分布在四个问题集 2.5 / 3.4 / 4.3 / 5.4，编号独立递增）。
- **图 2 张**：图 2.24（两个 2 阶极点的触手，`fig1.png`）、图 5.10（星形箭图与加倍箭图，`fig2.png`）。
- **表 2 张**：表 4.7（经典李代数的紧形式 𝒖）、表 4.8（经典李代数 Gℂ 的非紧形式 G）。
- **参考文献 105 条**（[1]–[105]，英文原貌，编号与原文一致）。
- **译者批注 132 条**（`% [Tutor Note: ...]`，不进入排版；汇总见 `译注汇总.md`）。

## 三、编译方法

环境：**TeX Live 2026 + LuaLaTeX**（ctex 自动调用系统字体；本机已验证）。
在交付包根目录执行（两条命令等价，根目录的 `build.ps1` 只是转调 `src/build.ps1`）：

```powershell
powershell -ExecutionPolicy Bypass -File .\build.ps1
# 或： powershell -ExecutionPolicy Bypass -File .\src\build.ps1
```

已实测：直接对交付包 `src/` 独立重编译通过（0 file:line 错误 / 0 `!` / 0 Undefined /
0 Missing character / 0 Overfull），成品 PDF 与随包 PDF 同为 48 页。

`build.ps1` 会把 `src/` 与 `src/figures/` 镜像到一个 **ASCII、可写**的目录再编译 3 遍，
成功后把 `main.pdf` 拷回 `src/`，并解析 `main.log` 打印 file:line 错误数 / `!` 错误数 /
Undefined / Missing character / Overfull。

> 本机实测的两条硬约束（换机器时按需调整 `build.ps1` 顶部常量）：
> ① LuaLaTeX 在**非 ASCII 路径**（中文目录）下无法写 `.log`（报 `I can't write on file main.log`）；
> ② 子进程（lualatex.exe）**不能写 Desktop**；因此 `build.ps1` 固定镜像到
> `…\default-workspace\` 下的 ASCII 目录，并显式设置 `TMP`/`TEMP`。
> 这两条都已写进脚本，读者换用别的机器时只需改 `$bin` / `$root` 两处。

源码结构（`src/` 可独立重编译，不依赖 200dpi 页图等中间素材）：

```
src/
  main.tex          总装（\InputIfFileExists 逐块注入，缺片也能编译）
  preamble.tex      导言区：ctex、amsmath、leqno、编号环境、图/表标题宏、参考文献宏
  chunks/c00.tex    标题页 / 摘要 / 译者说明 / 目录
  chunks/c01.tex    原文 pp.1–5（§1 + §2.1）
  chunks/tr01a–c.tex … tr07a–c.tex   7 位译文块（原文 pp.6–49，按 a→b→c 拼装）
  chunks/c-refs.tex 参考文献（脚本自动转录）
  figures/fig1.png, fig2.png
  build.ps1
```

## 四、译校体例

1. **编号**：原文每节内定理/命题/定义/例/注/猜想/**公式**/图/表共用一个递增计数器；本译本所有编号
   **一律照抄原文**（`\tag{2.7}`、`\begin{thm}{4.2}`、`\figtitle{2.24}{…}`、`\tabtitle{4.7}{…}`），
   **不使用 LaTeX 自动编号**（避免任何漏项导致全书编号错位）。三级行内标题（`X.Y.Z.`）用
   `\para{4.2.2.\ 非阿贝尔化}` 手工写编号。
2. **公式**：编号公式 20 条全部与原文一一对应；无编号公式用 `\[ … \]`；正文引用写纯文本「式 (3.8)」。
   公式编号印在左侧（`leqno`），与原文版式一致。
3. **章节层级**：`\section` / `\subsection` 由 LaTeX 自动编号（已由 Gate 3 回读校验 5 个 section、
   16 个 subsection 的编号均正确）。原文的**行内粗体小节标题**（run-in）在本译本中改为独立标题行，
   便于阅读与目录导航——这是有意的版式调整，不改变内容。
4. **图/表**：图 2.24、图 5.10 为原图 400–500 dpi 裁切（不含原图注与正文）；表 4.7、表 4.8 用 booktabs
   逐格重建（表 4.7 第 2 列在原表中数据行为空，照原样保留空列）。图注/表题照原文翻译，编号手工给出。
5. **习题**：`\begin{prob}{1} … \end{prob}`（编号照抄），子项 `(i)(ii)…` 用 `enumerate[label=(\roman*)]`。
6. **参考文献**：按学术惯例**不译**，以英文原貌转录 [1]–[105]（自动转录、未逐条校对，见 §七）。
7. **批注**：`% [Tutor Note: …]`，编译后不显示；内容限于可验证的易错点、补出的省略论证、
   原文笔误（附正确形式与判断依据）、术语首现。共 132 条，汇总见 `译注汇总.md`。
8. **术语**：`glossary.tsv` 冻结；首次出现括注英文；人名、模型名、缩写（Higgs、Hitchin、Prym、
   Langlands、Stokes、F-theory、Calabi–Yau、SL(2,ℂ) 等）保留英文/原记号。
9. **页标注**：源码中每个原文页起始处有 `% [原文 p.N]`，可据此把译文与底本逐页对照。

## 五、原文笔误登记表（正文一律照原样排，仅在批注中指出）

> 本表只登记经页图（必要时 500–1000 dpi 裁图）复核确认者；"照排"= 译文正文按原文排，
> 正确形式写在 `% [Tutor Note]` 里。原文另有大量拼写/语法小疵，详见各块批注与 `译注汇总.md`。

| # | 页 | 原文 | 说明 / 正确形式 |
|---|---|---|---|
| 1 | p.2 | "Through these correspondances" | 拼写：correspondences |
| 2 | p.4 | "the induced quotient the quotient $(E/F,\Phi')$" | the quotient 重复 |
| 3 | p.6 | 含因子 $x$ 的 $\det(x-A)$ 形式 | 只对 $\mathfrak{so}(2n+1,\mathbb{C})$ 成立，偶数维 $\mathfrak{so}(2n,\mathbb{C})$ 不含 $x$ 因子 |
| 4 | p.8 | "This space hasdimension" | 缺空格 |
| 5 | p.8 | $m_{j,i}=\dim(E_{p_j,i}/E_{p_j,i+1})$ | 与 p.7 的**递增**旗不自洽，应为 $E_{p_j,i}/E_{p_j,i-1}$（存疑） |
| 6 | p.9 | "see Example 2.4.1" | 无对应编号（疑指小节 2.4.1） |
| 7 | p.9 | "see Section 2.3)." | 多一个右括号 |
| 8 | p.10 | "the number of anti-Stokes directions in any half-period is **1**" | 按上下文应为 $l$（页图与文字层均印作 1，照排） |
| 9 | p.11 | 注 2.22 中 $q_1-q_2$ 首项 $a/z^4$ | 与同注 $q_{12}=a/z^3$、6 条反 Stokes 方向不自洽（存疑） |
| 10 | p.12 | "a rank 2 Higgs bundles" | 单复数 |
| 11 | p.13 | "holomorphic Higgs filed" | field |
| 12 | p.13 | 问题 2(i)「$4\times4$ matrix expression…of $\mathfrak{sp}(2p,2q)$」 | 一般应为 $(2p+2q)\times(2p+2q)$，4×4 仅 $p=q=1$ |
| 13 | p.14 | "and and"、"Though those identifications" | 重复 and；Though→Through |
| 14 | p.15 | 题词只有结尾一个右引号 | 原文如此（照排） |
| 15 | p.15 | 式 (3.2) 首项 $\operatorname{tr}$ 与通项 $\operatorname{Tr}$ | 大小写不统一（照排） |
| 16 | p.17 | "so $K_S\otimes\pi^*K^{-m}$ is trivial and $K_S=\pi^*K^n$" | $m$ 应为 $n$（下一式要求） |
| 17 | p.18 | "dimension $g_S$ as in (3.2)" | $g_S$ 公式实为 p.17 的无编号式 |
| 18 | p.18 | "additional conditions on the Higgs field $\Sigma$" | $\Sigma$ 是底曲面，条件应加在 Higgs 丛上 |
| 19 | p.19 | "has been studied" 印作 "as been" | has |
| 20 | p.20 | "$\sigma(\eta)=-\sigma$" | 应为 $\sigma(\eta)=-\eta$ |
| 21 | p.20 | "Example newexample" | 原稿未解析的交叉引用（照排） |
| 22 | p.20 | "$\omega\in H^2(\Sigma,K^2)$" | 上标 2 应为 0 |
| 23 | p.21 | 晶格符号印作 $\wedge$ | 按语境应为 $\Lambda$（照排） |
| 24 | p.21 | $\Lambda^pW_1\cong\Lambda^qW_2^*$ | 右端指数 $q$ 应为 $p$（$q=0$ 情形） |
| 25 | p.21 | 覆盖映射 $\pi$ 与 $\rho$ 混用 | 照排，批注给出统一读法 |
| 26 | p.22 | "the spectra curve"、"fibration For" | spectral；脱句号 |
| 27 | p.24 | 问题 7.i 缺动词 | 应为 "Use GRR to show…" |
| 28 | p.25 | 问题 9.i「$\bar\pi_*U_1=V$ and $\bar\pi_*U_1=W$」 | 第二式应为 $U_2$ |
| 29 | p.25 | 问题 10"summery"、"in terms the" | summary；in terms of |
| 30 | p.26 | A-膜/B-膜的定义 | 首段与同页下文定义相反（存疑） |
| 31 | p.27 | "$G_\mathbb{C}(n,\mathbb{C})$-connection" | 应为 $G_\mathbb{C}$-connection |
| 32 | p.28 | "In the later case"、"surface surface" | latter；重复 |
| 33 | p.29 | "Lagrangians subspaces"、"this phenomena" | Lagrangian；phenomenon |
| 34 | p.30 | 式 (4.6) 首项 $f^*(\partial_A)$ | 应为 $f^*(\bar\partial_A)$（同式第二项可证） |
| 35 | p.31 | 表 4.7 $\mathfrak{a}_n$ 行 $\dim\mathfrak{u}=n(n+1)$ | 应为 $\dim\mathfrak{su}(n)=n^2-1$（其余三行正确） |
| 36 | p.32 | "the reminder of this section" | remainder |
| 37 | p.33 | (4.10)/(4.13) 中变量 $x$ | 应为 $\eta$（对照 p.21 式 (3.8)） |
| 38 | p.34 | "$\pi':\bar S:=S/\sigma\to S$" | 应为 $\to\Sigma$；"$\bar\pi(E^+)=W_2$" 第二个 $E^+$ 应为 $E^-$；"line line bundle" 重复 |
| 39 | p.35 | $i_2$ 式第二分量 $f^*(\partial_A)$ | 应为 $f^*(\bar\partial_A)$（对照 p.30 式 (4.6)） |
| 40 | p.35 | 猜想 4.14 作 $\mathrm{SO}(p+q,q)$ | 前文一律 $\mathrm{SO}(p+q,p)$（存疑，照排） |
| 41 | p.37 | 问题 11 标题印作 "textbfTopological invariants." | 源码漏 `\`，本译本按作者本意恢复为粗体标题（见 §七） |
| 42 | p.37 | "Toledo Toledo invariant"、"of flat space is" | 重复；衍文 |
| 43 | p.39 | "Group homeomorphisms" | homomorphisms（照原样译作「群同胚」+ 批注） |
| 44 | p.39 | "In what fallows"、"isogenies between complex are" | follows；缺 "Lie groups" |
| 45 | p.40 | (h) "$\mathfrak{su}(4)$" | $\mathfrak{su}^*(4)$（同表 (c) 带星号可证） |
| 46 | p.40 | "$Q(u,\Phi v)=-Q(\Phi u,w)$" | 右端 $w$ 应为 $v$ |
| 47 | p.41 | $p(x)$ 中 $+\operatorname{tr}(\Phi)x^{n-1}$ | 应为 $-\operatorname{tr}(\Phi)x^{n-1}$ |
| 48 | p.41 | $\operatorname{Prym}(\hat S,\hat S/\sigma)$ | 应为 $\hat S/\hat\sigma$ |
| 49 | p.42 | "as bellow"、"n outer vertices $v_0,\dots,v_n$" | below；第一个 $v_0$ 应为 $v_1$ |
| 50 | p.43 | "Section 2.9" | §2.9 不存在（全书 2.1–2.5），应为 §2.1 |
| 51 | p.44 | "can be defined be the" | by |
| 52 | p.45 | "the Hitchin basis"、"$G_\mathbb{C}$-Higgs bundle" | base；单数 |
| 53 | p.47 | "an $\mathrm{SL}(4,\mathbb{R})$-Higgs bundles"、"(E,\varphi)…and $\Phi$ is trace free" | 复数多余；$\Phi$ 应为 $\varphi$ |
| 54 | p.47 | "this over pairs"、"obtained thought the isogeny" | i.e.；through |
| 55 | p.48 | "so textrmAut$(Q_n)$" | 源码漏反斜杠，PDF 直接印出 "textrmAut"；本译本照印出字样排 + 批注给出 $\operatorname{Aut}(Q_n)$ |
| 56 | p.48 | "the covariant involution which sending" | which sends |
| 57 | p.49 | "the Institute of Advance Studies" | Advanced |

## 六、统计

| 指标 | 数值 |
|---|---|
| 底本 | arXiv:1907.09800v1，53 页（正文 48 + 参考文献 5） |
| 译文 | 45 个印刷页（前置 i–ii；正文 1–40；参考文献 41–45） |
| 编号公式 | 20 条（实测 tags.txt：0 缺、0 重、0 自造，Gate 1/3 双重校验） |
| 编号条目 | 46 条（定理/命题/定义/例/注/猜想/图/表，逐节连续） |
| 习题 | 20 道（分布 2.5/3.4/4.3/5.4 四个问题集） |
| 图 / 表 | 2 图（2.24、5.10）/ 2 表（4.7、4.8） |
| 参考文献 | 105 条（0 缺号、0 重号） |
| 译者批注 | 132 条（`译注汇总.md`） |
| 编译 | LuaLaTeX ×3：file:line 错误 0；`!` 错误 0；Undefined 0；Missing character 0；Overfull 0（1 处经修复后归零） |
| 交叉校对 | 7 轮互检（每位译者校一块别人的）+ Lead 复核；报告在 `work/review/`（交付包不含） |

## 七、已知偏差与限制

1. **参考文献为自动转录**：`c-refs.tex` 由脚本从 PDF 文字层转录（已剥离页眉/页码/hyperref 回链/断行连字符、
   恢复 ligature、转义特殊字符、把希腊字母与上下标映射为数学），**未逐条人工校对**；编号与原文一一对应
   （105 条、0 缺 0 重），但个别条目的数学排版可能与原文有细微差别。
2. **版式未逐像素复刻**：原文为 letter 单栏窄版心（正文宽约 360 pt）；译本改用 A4、2.6 cm 页边距，
   页数因此少于原文。原文的**行内粗体小节标题**改为独立标题行（有目录），内容不变。
3. **群名写法**：原文正文把 $G_\mathbb{C}$、$\mathrm{SL}(n,\mathbb{C})$ 等排为正体；本译本中经典群名一律用正体
   （`\Sl`、`\SO`、`\SU`、`\Sp`、`\Gl` 等，即 `\mathrm`），仅 $G_{\C}$ 按通行数学排版用斜体 `$G_{\C}$`，
   与原文的正体写法略有差异；全书已归一（交叉校对阶段把最后 47 处斜体群名统一为正体）。
   p.48 问题 20 箭图右顶点按原图写作 $\mathrm{l}(1)$。
4. **p.37 问题 11 标题**：原文源码漏写 `\textbf` 的斜杠，PDF 上印出字面 "textbfTopological invariants."；
   本译本**恢复为粗体标题**「拓扑不变量。」（属恢复作者本意，已在批注与 §五 登记）。
5. **p.48 "textrmAut"**：原文以同样方式漏写，PDF 印出 "textrmAut$(Q_n)$"；本译本**照印出字样**保留，
   正确形式 $\operatorname{Aut}(Q_n)$ 写在批注里。两者处理不同，原因是前者为标题（照印会破坏排版层级），
   后者为行内公式（照印仍可读且保持与原文一致）。
6. **例 5.8 的星形箭图**：原文该图为正文内的未编号行内图，本译本用 TikZ 重画（忠实照抄节点与箭头方向）。
   问题 19、20 的箭图（p.48）按「不重画、不裁剪正文图」的约定**以文字逐项描述**代替，读者请对照原文 p.48。
7. **图 2.24、5.10** 为原图 400–500 dpi 裁切（图内文字不再重排/翻译），图注为译者翻译。
8. **原文笔误**：正文一律照原样排，正确形式只写在批注里（§五 登记 57 项，另有若干拼写小疵见批注）。
9. **批注不进入排版**：132 条 Tutor Note 只在源码注释与 `译注汇总.md` 中；成品 PDF 中看不到批注。
10. **原文自身不一致处未代为统一**：如 p.15 的 tr/Tr、p.41 的 $\mathcal{L}$/$L$、p.20/p.38 的 $\pi/\bar\pi$ 等，
    译文按原文分别保留并在批注说明。

## 八、版权声明

原文 © Laura P. Schaposnik，依 arXiv:1907.09800v1 的 arXiv 许可发布。本译本为**学习与研究用途**的
中文译注本，原文版权归原作者所有；译注（Tutor Note）、体例与排版由本译本贡献，引用原文内容时
请以 arXiv 原版为准并注明出处：

> L. P. Schaposnik, *Advanced topics in gauge theory: mathematics and physics of Higgs bundles*,
> arXiv:1907.09800 [math-ph] (2019).

如原作者或版权方对译本有任何异议，请联系删除。
