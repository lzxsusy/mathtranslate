# BRIEF —— 分工、边界与文件清单（Lead 独占维护；队友只读）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 为准：语料 / 轨迹 / 会话 CC BY 4.0，明确欢迎用于训练与蒸馏（译文与工程文档 CC BY-NC-SA 4.0）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

## 0. 一句话

底本是一份 SYZ 镜像对称学习讨论班的英文讲义网页（6 章 + 参考文献）。本工程已用脚本把网页
解析成 246 个**源块**（每块一个 `Bnnn` 编号），并按块边界切成 11 个翻译片段。
你要做的：把分配的片段逐块译成中文 LaTeX，写到 `work/src/chunks/<片段名>.tex`。

## 1. 工程根与关键路径

```
<本地路径>
├── raw\SYZ.html                          底本原始 HTML（只读）
├── work\
│   ├── STYLE_GUIDE.md                    硬规范（先读）
│   ├── BRIEF.md                          本文件
│   ├── TIMELINE.md                       边界裁决记录
│   ├── glossary.tsv                      术语冻结表
│   ├── source\
│   │   ├── chunks_src\<片段名>.md        ★ 你的源文（逐块，带 <<Bnnn kind>>）
│   │   ├── sections\NN_*.md              整章源文（查上下文）
│   │   ├── blockmap.tsv                  全部 246 块总表
│   │   └── manifest.json                 片段 → 源块号清单
│   ├── src\
│   │   ├── preamble.tex                  导言区（Lead 独占）
│   │   ├── main.tex                      汇总（Lead 独占）
│   │   ├── build.ps1                     一键编译（Lead 用）
│   │   └── chunks\                       ★ 你的输出目录
│   └── review\                           交叉校对报告
└── deliverable\                          最终交付（Lead 打包）
```

## 2. 施工顺序（每位译者相同）

1. 读完 `STYLE_GUIDE.md` 全文 → 读 `glossary.tsv` → 读 `TIMELINE.md`；
2. 打开 `work\source\chunks_src\<你的片段>.md`，逐块翻译；需要上下文时看 `work\source\sections\`；
3. 每块译文前写 `% [源 Bnnn]`；环境/公式严格按 STYLE_GUIDE 转写；
4. 写完用 STYLE_GUIDE §10 自检，然后 `send_message` 给 lead 交回执（5 项）。

## 3. 章标题与小节标题（**全工程统一，直接照抄，不要自创译名**）

| 底本 | 定稿译名 | 写作者 |
|---|---|---|
| Overview | 概论（`\section*`，进目录） | Lead（c01） |
| 第 1 章 Introduction | 引言 | tr-01（tr01a 写 `\section`） |
| 第 2 章 Lagrangian Torus Fibrations | 拉格朗日环面纤维化 | tr-02（tr02a 写 `\section`） |
| 　└ Regular Lagrangian fibrations. | 正则拉格朗日纤维化 | tr-02 |
| 　└ Integrable hamiltonian systems. | 可积哈密顿系统 | tr-02 |
| 　└ Equivalences. | 等价 | tr-02 |
| 　└ Flux. | 通量 | tr-02 |
| 第 3 章 SYZ Mirror Symmetry for Toric Fano Varieties | 环簇 Fano 集的 SYZ 镜像对称 | tr-03（tr03a 写 `\section`） |
| 　└ Symplectic toric varieties. | 辛环簇 | tr-03 |
| 　└ Homological Mirror Symmetry. | 同调镜像对称 | tr-03 |
| 　└ SYZ mirror construction for toric Fano varieties. | 环簇 Fano 集的 SYZ 镜像构造 | tr-04 |
| 第 4 章 Focus-focus Singularities and Almost Toric Fibrations | 焦点-焦点奇点与近环面纤维化 | tr-05（tr05a 写 `\section`） |
| 　└ Standard focus-focus singularity. | 标准焦点-焦点奇点 | tr-05 |
| 　└ Monodromy. | 单值化 | tr-05 |
| 　└ Almost toric manifolds. | 近环面流形 | tr-05 |
| 第 5 章 SYZ Mirror Symmetry for Toric Varieties, Continued | 环簇的 SYZ 镜像对称（续） | tr-06（tr06a 写 `\section`） |
| 　└ Toric manifolds: complex & symplectic. | 环簇流形：复结构与辛结构 | tr-06 |
| 　└ Sympletic aspects. | 辛几何方面（底本拼作 Sympletic，按 Symplectic 理解） | tr-06 |
| 　└ Morse-Bott Floer cohomology. | Morse–Bott Floer 上同调 | tr-06 |
| References | 参考文献（英文原貌，脚本生成） | Lead |

> 章号由 LaTeX 自动编号（`\section`），**不要**在标题里手写「第 1 章」；行文里引用章节时写「第 3 章」纯文本。

## 4. 分工表（源块号以 `work\source\blockmap.tsv` 为准）

| 片段 | 译者 | 源块区间 | 输出文件 | 章节归属 | 内容提要 |
|---|---|---|---|---|---|
| c01 | Lead | B001–B011 | `chunks/c01.tex` | 概论 | Kontsevich HMS 提议、SYZ 提议、墙穿越、Maurer–Cartan 空间、讨论班日程（表 1，B010） |
| tr01a | tr-01 | B012–B023 | `chunks/tr01a.tex` | 第 1 章开头（写 `\section{引言}`） | HMS 陈述、Bondal–Orlov 重构定理、点对象与可逆层、Floer 定理 |
| tr01b | tr-01 | B024–B037 | `chunks/tr01b.tex` | 第 1 章 | 引理与证明、Koszul 复形、Novikov 环、$A_\infty$ 形变、超势 $W$ |
| tr02a | tr-02 | B038–B085 | `chunks/tr02a.tex` | 第 2 章开头（写 `\section{拉格朗日环面纤维化}`） | 分层/纤维化定义、可积哈密顿系统、作用-角坐标、Little/Big Arnold–Liouville、整仿射结构、**交换图 B082** |
| tr02b | tr-02 | B086–B104 | `chunks/tr02b.tex` | 第 2 章 | 等价、**交换图 B089**、重构定理与**交换图 B093**、Lagrange 子流形、通量 |
| tr03a | tr-03 | B105–B115 | `chunks/tr03a.tex` | 第 3 章开头（写 `\section{环簇 Fano 集的 SYZ 镜像对称}`） | 环簇、扇/锥、多面体、Atiyah–Guillemin–Sternberg、矩映射、Batyrev 判据 |
| tr03b | tr-03 | B116–B131 | `chunks/tr03b.tex` | 第 3 章（同调镜像对称） | 同调镜像对称的环面侧陈述、Fang–Liu–Treumann–Zaslow/Kuwagaki 定理 |
| tr04a | tr-04 | B132–B139 | `chunks/tr04a.tex` | 第 3 章（SYZ 镜像构造） | Cho–Oh 的 Maslov 指标与全纯圆盘分类 |
| tr04b | tr-04 | B140–B154 | `chunks/tr04b.tex` | 第 3 章（同上） | 曲率项 $\mathfrak{m}^0$、Hori–Vafa 超势、$HF^\ast$ 良定义 |
| tr05a | tr-05 | B155–B174 | `chunks/tr05a.tex` | 第 4 章开头（写 `\section{焦点-焦点奇点与近环面纤维化}`） | 非退化奇点、Williamson 型（**表 2，B164**）、标准焦点-焦点模型、单收缩环面 |
| tr05b | tr-05 | B175–B188 | `chunks/tr05b.tex` | 第 4 章 | 单值化、仿射单值化、节点整仿射结构、近环面流形（**表 3，B188**） |
| tr06a | tr-06 | B189–B214 | `chunks/tr06a.tex` | 第 5 章开头（写 `\section{环簇的 SYZ 镜像对称（续）}`） | 环簇的复/辛构造、原语集、Morse–Bott Floer 上同调 |
| c-refs | Lead | —（第 7 章参考文献） | `chunks/c-refs.tex` | 参考文献 | 32 条英文原貌转录（脚本生成） |

**表格归属**：表 1（讨论班日程，B010）= Lead；表 2（Williamson 型，B164）= tr-05 写在 `tr05a`；
表 3（底流形与节点数，B188）= tr-05 写在 `tr05b`。编号顺序即 表 1 → 表 2 → 表 3。

## 5. 交换图数据（q.uiver.app 解码，tr-02 用 tikz-cd 重画）

B082（在 tr02a，位于 B081 引理「$G,H\colon M\to\R^n$ 与 diffeo $\psi\colon\R^n\to\R^n$」的陈述之后；
原文句子为 "…$\psi\colon\mathbb{R}^n$ a diffeomorphism fitting into the commutative diagram [图] then $\psi$ is integral affine."）
- 节点：`M`（上中），`\R^n`（左下），`\R^n`（右下）
- 边：`M → \R^n` 标 `G`；`M → \R^n` 标 `H`；`\R^n → \R^n` 标 `\psi`
- 建议：
  ```latex
  \begin{tikzcd}
    & M \arrow[dl, "G"'] \arrow[dr, "H"] & \\
    \R^n \arrow[rr, "\psi"'] & & \R^n
  \end{tikzcd}
  ```

B089（在 tr02b，B088 定义「两个正则拉格朗日纤维化同构」里的交换图）
- 节点：`M`(左上)、`M'`(右上)、`B`(左下)、`B'`(右下)
- 边：`M → M'` 标 `\Phi`；`M → B` 标 `\pi`；`B → B'` 标 `\phi`；`M' → B'` 标 `\pi'`
- 建议：
  ```latex
  \begin{tikzcd}
    M \arrow[r, "\Phi"] \arrow[d, "\pi"'] & M' \arrow[d, "\pi'"] \\
    B \arrow[r, "\phi"'] & B'
  \end{tikzcd}
  ```

B093（在 tr02b，B092 重构定理「$\pi\colon M\to B$、$\pi'\colon M'\to B$ 带整体拉格朗日截面 $\sigma,\sigma'$」里的交换图，
原文随后一句是 B094 "commutes."）
- 节点：`M`(左上)、`B`(中下)、`M'`(右上)
- 边：`M → M'` 标 `\Phi`，**点线**；`M → B` 标 `\pi`，向左弯；`M' → B` 标 `\pi'`，向右弯；
  `B → M` 标 `\sigma`，向左弯；`B → M'` 标 `\sigma'`，向右弯
- 建议：
  ```latex
  \begin{tikzcd}
    M \arrow[rr, "\Phi", dotted] \arrow[dr, "\pi", bend left=18] & & M' \arrow[dl, "\pi'", bend right=18] \\
    & B \arrow[ul, "\sigma", bend left=18] \arrow[ur, "\sigma'", bend right=18] &
  \end{tikzcd}
  ```
- 若某条边在你读上下文后确认方向/样式不同，**以原图语义为准**并在回执里说明（这三张图是纯排版重画，不允许改变数学含义）。

## 6. 边界锚点（首尾句，逐字对齐；`work\source\blockmap.tsv` 可查）

| 片段 | 首块 / 首句（截断） | 末块 / 末句（截断） | 下一位从哪开始 |
|---|---|---|---|
| tr01a | B012 `In this talk I aim to provide a brief overview…` | B023 `Let $p\in\check X$ be a smooth closed point…`（段末） | tr01b 从 B024 的引理开始 |
| tr01b | B024 `**Lemma.** $\Hom^{\ast}(\cO_p,\cO_p)\cong…` | B037 `…concerning SYZ and Homological Mirror Symmetry.`（章末） | tr02a 从 B038 开始 |
| tr02a | B038 `In this talk we will review some basic geometric facts…` | B085 `**Corollary.** If $\pi\colon M\to B$ is a regular Lagrangian fibration…`（完整推论） | tr02b 从 B086 小节标题 `Equivalences.` 开始 |
| tr02b | B086 `Equivalences.` | B104（本章末段） | tr03a 从 B105 开始 |
| tr03a | B105 `In this talk we will give a review on toric varieties…` | B115 `**Definition/Proposition(Batyrev).** …`（完整环境） | tr03b 从 B116 小节 `Homological Mirror Symmetry.` 开始 |
| tr03b | B116 `Homological Mirror Symmetry.` | B131（小节末段） | tr04a 从 B132 小节 `SYZ mirror construction…` 开始 |
| tr04a | B132 `SYZ mirror construction for toric Fano varieties.` | B139 `In particular, the numbers $\mu_i$ are intersection multiplicities…`（段末） | tr04b 从 B140 引理开始 |
| tr04b | B140 `**Lemma.** The summation …` | B154（本章末段） | tr05a 从 B155 开始 |
| tr05a | B155（第 4 章开篇段） | B174 `**Theorem[[Sym03]].** …`（完整定理） | tr05b 从 B175 小节 `Monodromy.` 开始 |
| tr05b | B175 `Monodromy.` | B188（表 3，章末） | tr06a 从 B189 开始 |
| tr06a | B189 `In this talk we provide more details of [[CO06]]…` | B214（本章末段） | 之后是参考文献（Lead） |

- **不许跨文件拆环境**：若你的末尾块是一个 `env`，把它写完整；下一片段的第一块由下一片段独立开始。
  若某环境的内容横跨两个片段（实际切分已避免），以开始者为准，由 Lead 在 TIMELINE 记录。

## 7. 质量要求摘要（详见 STYLE_GUIDE）

- 每块前面写 `% [源 Bnnn]`，**246 块全覆盖、每块恰好一次**；
- 独立公式 38 处全部转写（`\[…\]`/`align*`），**严禁 `\tag`/`\label`/`\ref`**；
- 定理类环境 62 个、证明 12 个、表 3 张、交换图 3 个，一个不许漏、一个不许造；
- 术语一律以 `glossary.tsv` 为准，首次出现给英文原词；
- 批注 `% [Tutor Note: …]`：每文件 ≥3 条，全工程 ≥30 条，必须具体可验证；
- 中文标点、UTF-8 无 BOM、LF；不写 `\newcommand`、不编译（Lead 统一编译）。

## 8. 交稿后的流程（预告）

1. Lead 合成 + 跑 `check.py`（Gate 0/1）+ 真编译（Gate 2）+ 成品 PDF 回读（Gate 3）；
2. **交叉校对**：每人校另一位的一块（只写 `work\review\<块名>.md` 报告，**绝不改别人的 tex**）；
3. Lead 用 patch 脚本落改 → 重编译 → 重跑 Gate；
4. 打包 `deliverable\`（PDF + src/ + build.ps1 + compile.log + 译注汇总.md + README.md）。
