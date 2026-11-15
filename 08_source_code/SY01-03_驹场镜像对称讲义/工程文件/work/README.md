# 《驹场镜像对称讲义》中文译注本 —— 交付说明

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，保留权利，仅限非商业学术研读，权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

## 1. 底本信息与页码映射

| 项 | 内容 |
|---|---|
| 原文标题 | *Komaba Lectures on Mirror Symmetry* |
| 作者 | Kentaro Hori（堀健太郎），Kavli IPMU, University of Tokyo |
| 来源 | 2016 年 8 月 26--28 日东京大学驹场校区（Komaba）讲座讲义 |
| 文件 | `2016Lec(1).pdf`（49 页；元数据 `2016Lec.dvi`，dvips + Ghostscript 生成） |
| 性质 | 作者自述为**不完整版**（"A part of the notes ... A full version will be available soon"） |
| 页数 | PDF 49 页：p.1 标题页、pp.2--48 正文、p.49 参考文献 |

**页码映射：PDF 页号 = 原文印刷页脚页码 + 1。**
译文用注释行 `% [原文 p.N]` 标注每个原文**印刷页**的起始位置，便于与底本逐页对照。

| 内容 | 原文印刷页 | PDF 页 |
|---|---|---|
| 标题页 / 摘要 | —（p.0） | 1 |
| §1 引言、§2 二维 (2,2) 超对称量子场论 | 1--9 | 2--10 |
| §3 T-对偶 | 9--16 | 10--17 |
| §4 规范线性 sigma 模型 | 17--36 | 18--37 |
| §5 镜像对称 | 37--47 | 38--48 |
| 参考文献 | 48 | 49 |

> 注：原文没有 `\part` 划分，全文为连续的 5 个 `\section`；本译本同样不使用 `\part`。

## 2. 结构清单

- **5 个 `\section`**：1 引言 / 2 二维 (2,2) 超对称量子场论 / 3 T-对偶 / 4 规范线性 sigma 模型 / 5 镜像对称
- **20 个 `\subsection`**：2.1--2.7、3.1--3.3、4.1--4.5、5.1--5.5（与原文逐条对应）
- **139 条编号公式**：2.1--2.19、3.1--3.23、4.1--4.56、5.1--5.41（与原文一一对应，无增删、无重排）
- **8 张图**：Figure 1--8（原文矢量图按 500 dpi 裁取，图注为译文；图内英文标签保留原样）
- **10 条脚注**：原文每页脚注编号重新起算（每页 1、2…），译本改为全文连续编号（内容与位置逐条对应，见 §7 已知限制）
- **无表格、无 keybox、无习题、无附录、无致谢**（原文即如此）
- **参考文献 12 条**：按学术惯例不译，照原文转录

## 3. 编译方法（含本机字体与路径注意事项）

### 3.1 一键编译（本机）

在本交付包根目录下执行：

```powershell
powershell -ExecutionPolicy Bypass -File src\build.ps1
```

（工作区版本为 `work\src\build.ps1`，两者相同；脚本会自动识别 `main.tex` 在 `src\` 还是当前目录。）

`build.ps1` 做的事：找到 TeX bin → 把 `src/`、`chunks/`、`figures/` 镜像到
`<本地路径>`（ASCII、可写）→
设 `TMP`/`TEMP` → `lualatex -interaction=nonstopmode -file-line-error main.tex` **跑 3 遍** →
解析 `main.log` 的错误计数 → 把 `main.pdf` 拷回 `src\` 与 `deliverable\`。

### 3.2 手工编译（其他机器）

```powershell
cd src
lualatex -interaction=nonstopmode main.tex
lualatex -interaction=nonstopmode main.tex
lualatex -interaction=nonstopmode main.tex
```

需要 **LuaLaTeX + ctex + TeX Live 2025/2026**（含 tcolorbox、tikz、booktabs；本译本实际用到
amsmath、amssymb、mathtools、bm、graphicx、geometry、xcolor、enumitem、booktabs、array、
multicol、fancyhdr、caption、tcolorbox、tikz、hyperref）。

### 3.3 本机两条硬约束（换机器可忽略）

1. **LuaLaTeX 在非 ASCII 路径（如中文目录）下无法写 `.log`**，报 `I can't write on file main.log`；
2. **子进程不能写 Desktop**（同样报 `I can't write on file`），但可写 `default-workspace`。

因此必须**镜像到 ASCII 可写目录再编译**，编译完把 PDF 拷回。另：日志**绝不能**重定向到
`<jobname>.out`（TeX 会把它当输入文件读，满屏 `Text line contains an invalid character`）。

## 4. 译校体例

1. **正文**：忠实直译，术语按 `glossary.tsv` 冻结；模型名、缩写（GLSM、CFT、SCFT、T-duality、
   Calabi--Yau、Landau--Ginzburg、Fano、Bott--Morse、FJRW 等）保留原文形式；术语首现括注英文。
2. **公式**：139 条编号公式逐条用 `\tag{}` 复刻原文编号；无编号公式用 `\[...\]`/`equation*`，
   **绝不自造编号**；正文引用公式写纯文本"式 (3.13)"，不用 `\ref`/`\eqref`。
3. **文字层不可信**：底本 PDF 的数学符号抽提严重失真（`\widetilde{X}`→`eX`、`\tilde\phi`→`eφ`、
   `\widetilde W`→`fW`、`\bar\psi`→空白、上下标错位），所有公式均按 200 dpi 页图逐符号重抄，
   关键式另用 500--1000 dpi 裁图复核。
4. **批注**：译者的补充一律写成 `% [Tutor Note: ...]`（不进入排版），汇总见《译注汇总.md》。
   批注只做四类事：指出原文笔误、补出作者跳过的推导、标注易错点与判别判据、术语首现说明。
   **不在批注里编造物理内容**。
5. **图**：原图按 500 dpi 裁取（不含图注），图注翻译；图内英文标签（Phase I/II/III、ζ、φ 等）保留。
6. **页码**：每个原文印刷页起始处插 `% [原文 p.N]`。
7. **不补写**：原文为不完整讲义，5.5 中 "The CP^{N−1} Model" 小标题下无正文；照排并批注说明。

## 5. 原文笔误登记表

> 原则：**正文照原样排（或按原意直译），只在批注中指出并给出正确形式**；数学式笔误先用 300+ dpi
> 裁图复核后才登记。

| 序号 | 原文页 | 原文 | 说明 / 正确形式 |
|---|---|---|---|
| 1 | p.4 | "exacly marginal" | 应为 "exactly" |
| 2 | p.5 | "Forthermore" | 应为 "Furthermore" |
| 3 | p.6 | "supersymetry transformation" | 应为 "supersymmetry" |
| 4 | p.6, p.15 | "Lagragian" | 应为 "Lagrangian" |
| 5 | p.7 | "there is an RG low on $\mathfrak{M}^{0,c}_A$" | "low" 应为 "flow"（RG 流） |
| 6 | p.8 | "Fukaya category controled by $W$" | 应为 "controlled" |
| 7 | p.8 | "Jac(W) Jocobi ring" | "Jocobi" 应为 "Jacobi"（雅可比环） |
| 8 | p.10 | "obatin" / "peridicity" | 应为 "obtain" / "periodicity" |
| 9 | p.11 | "equaivalence" | 应为 "equivalence" |
| 10 | p.12 | "tranformation" | 应为 "transformation" |
| 11 | p.13 | "at the same positon" | 应为 "position" |
| 12 | p.15 | "empolyed" | 应为 "employed" |
| 13 | p.22 | "hyeprsurfaces" | 应为 "hypersurfaces" |
| 14 | p.27 | "corrsponding" | 应为 "corresponding" |
| 15 | p.28 | "choise" / "topologival A-models" | 应为 "choice" / "topological" |
| 16 | p.29 | "negtative" | 应为 "negative" |
| 17 | p.30 | "one pont blow up" | 应为 "one-point blow-up" |
| 18 | p.33, p.38 | "rˆole" | 应为 "rôle"（原文排版把 ô 拆成了 ˆ+o） |
| 19 | p.34 | "isomorophism" | 应为 "isomorphism" |
| 20 | p.36 | "intry" | 应为 "entry" |
| 21 | p.41 | "diemsional" / "repect" | 应为 "dimensional" / "respect" |
| 22 | p.42 | "defomation" / "must be ture" | 应为 "deformation" / "true" |
| 23 | p.43 | "Furtheremore" / "genertated" | 应为 "Furthermore" / "generated"（本译本按正确词义直译为"此外""产生"） |
| 24 | p.45 | "constanits" / "surprize" | 应为 "constraints" / "surprise" |
| 25 | p.47 | "This make it certain" / "Berglund-Hubsch" | 应为 "This makes it certain" / "Berglund--Hübsch" |
| 26 | p.16, p.40 | "na¨ıve" | 原文把 ï 排成 ¨+i；本译本统一译作"朴素" |
| 27 | p.40 | (5.18) 规范动能项印作 $\frac{1}{e_a^2}\lvert\sigma_a\rvert^2$ | 与 (5.8) 的 $\frac{1}{2e^2}\lvert\sigma\rvert^2$、(5.23) 的 $\frac{1}{2e_a^2}\lvert\sigma_a\rvert^2$ 及同页行内的 $K=\lvert\sigma\rvert^2/(2e^2)+\cdots$ 不一致，疑漏印因子 $1/2$；**正文照原样排印**，批注说明 |

> 以上均为**拼写/排版笔误**，不影响数学内容；译文按其正确含义直译，表中登记备查。
> 数学式中若发现疑似笔误，须先用 300+ dpi 裁图复核原文后才登记（见 §4 第 3 条）。

## 6. 统计

| 指标 | 数值 |
|---|---|
| 底本 | 49 页（正文 48 页 + 参考文献 1 页） |
| 编号公式 | 139 条 |
| 图 | 8 张（矢量图 0 位图） |
| 脚注 | 10 条（原文每页重新编号，译本全文连续编号） |
| 译文篇幅 | 38 页 |
| 编译 | LuaLaTeX ×3：file:line 错误 0 / Undefined 0 / Missing character 0 / Overfull 0 |
| 批注 | 69 条 Tutor Note |
| 公式编号核对 | 139/139 全部出现在成品 PDF 文本中 |
| 交叉校对 | 7 份报告（6 位译者互校 + Lead 校 tr-01），必须改项全部落改 |
| 分工 | Lead（§1--2）+ 6 位译者（§3、§4.1--4.3、§4.4 前半、§4.4 后半+§4.5、§4 末+§5.1--5.3、§5.3--5.5） |

## 7. 已知偏差与限制

1. **原文为不完整讲义**：5.5 节 "The CP^{N−1} Model" 小标题下没有正文（原文如此），
   本译本照排小标题并加批注，**未补写任何内容**。
2. **脚注编号**：原文每页脚注从 1 重新编号；本译本采用 LaTeX 全文连续编号（共 10 条，内容与位置
   与原文一一对应）。这是排版层面的差异，不影响内容。
3. **图**：8 张图为位图裁取（500 dpi），放大后略见锯齿；图内英文标签未译。
4. **数学记号**：原文 `\mathfrak{M}`、`\mathcal{M}` 等花体/哥特体字形在文字层中会丢失，本译本已按
   图像逐处核对；若仍有个别字形差异（如 `\bar` 与 `\overline`），以图像为准。
5. **虚数单位**：原文用**斜体** $i$（Computer Modern 数学斜体）；本译本中宏 `\ii` 即定义为斜体 $i$，
   全书的 $i$ 与原文同形。恒等常数 $e$、微分 $d$ 用正体。
6. **强调格式**：原文用整句下划线强调若干 case 分句（"In Phase I/II/III"、"When ζ>0" 等）。本译本
   该强调**未复刻**（按普通正文排），以避免中文整句下划线的排版噪音；内容未减。
7. **参考文献**：照原文转录，未逐条校对出版信息（原文只有 12 条，其中 [7] 仅作 "Convexity..."，
   作者未写全，属原文如此）。
8. **术语**：个别术语存在多种通行译法（如 orbifold → 轨形 / 轨道流形），本译本统一采用
   `glossary.tsv` 中的译法。
9. **模型名"一点爆破"**：原文 p.30 的 "one pont blow up" 为 "one-point blow-up" 之笔误，译文统一作
   "一点爆破"。

## 8. 版权声明

本译本仅供学习与研究使用。原文 *Komaba Lectures on Mirror Symmetry* 的著作权归 Kentaro Hori 所有；
译文与批注的著作权归译者。未经原作者许可，不得将本译本用于商业用途。若原文后来正式发表，
请以正式发表版本为准。
