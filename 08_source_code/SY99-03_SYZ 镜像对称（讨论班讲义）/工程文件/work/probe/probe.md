# probe.md —— 环境探测与底本尽调（实测，2026-11-04）

> 原则：R2 不臆测底本、R6 先探测后断言。本文件所有数字均来自脚本实测，脚本在 `work/tools/`。

## 1. TeX 工具链（不要只看 PATH）

| 项 | 实测值 |
|---|---|
| TeX 安装 | `<本地路径>` |
| 引擎 | `lualatex` = LuaHBTeX 1.24.0（TeX Live 2026），冒烟编译 3 行文档 → PDF 成功 |
| 关键宏包（`kpsewhich` 逐个实测） | ctex OK；tikz-cd OK；tcolorbox OK；booktabs OK；longtable OK；multicol OK；fancyhdr OK；amsthm OK；mathtools OK；enumitem OK；multirow OK；hyperref OK；caption OK |
| XeLaTeX | 存在，但 xdvipdfmx 在本机不稳定 → **统一用 lualatex** |
| 编译冒烟 | `work/src/build.ps1` 三遍：pass1/2/3 exit=0；file:line=0，`!`=0，Undefined=0，Missing char=0，Overfull=0，PDF 155 KB（含定理/tikz-cd/表格/中文的测试块） |

## 2. 本机三个硬约束（沿用 AGT 项目实测，本工程再次遵守）

- `lualatex` 在**非 ASCII 路径**（中文目录）下无法写 `.log`；子进程**不能写 Desktop**；
- `TMP`/`TEMP` 必须显式指向可写目录；
- → 编译策略：把 `work/src/` 镜像到 `<本地路径>`（ASCII、可写）编译，再把 PDF 拷回 `work/src/main.pdf`。见 `work/src/build.ps1`。

## 3. Python / PDF 库

| 项 | 实测值 |
|---|---|
| Python | `<本地路径>`（3.12.14） |
| pymupdf | 2.0（MuPDF 1.28.5）——用于成品回读、渲染抽页 |
| 写盘测试 | `default-workspace\syzbuild\tmp` 可写（已实测）；`syz_work` 目录可写 |

## 4. 底本尽调（Deck Check）

| 检查项 | 方法 | 实测值 |
|---|---|---|
| 底本形态 | `Invoke-WebRequest` | **网页** `https://diewildkatze.com/SYZ.html`，HTTP 200，106,386 字节（HTML+MathJax） |
| 作者/标题 | `<h1>` + 正文 | `Learning Seminar: SYZ Mirror Symmetry`；**底本无正式作者署名**（只在日程表列报告人：Si-Yang Liu、Yunpeng Niu、Kyoungmo Kim、Maximilien Schimpf 拼作 Maximilian Schimpf） |
| 页数 | — | **无页码（非 PDF）** → 改用「源块编号」定位与验收（246 块，见 `source/blockmap.tsv`） |
| 章节 | `<h2>`/`<h3>` 解析 | 6 章：Overview（无章号）+ Introduction、Lagrangian Torus Fibrations、SYZ Mirror Symmetry for Toric Fano Varieties、Focus-focus Singularities and Almost Toric Fibrations、SYZ Mirror Symmetry for Toric Varieties (Continued) + References |
| 小节 | `<h3>` | 14 个（LTF 4 个、Fano 3 个、Focus-focus 3 个、Toric2 3 个、Overview 1 个） |
| 有没有图 | `<img>` / `<svg>` / `<canvas>` / tikz 扫描 | **位图 0 张、SVG 0 张、`<canvas>` 2 张**（图 1「Moment polytope for $\mathbb{P}^2$」在 B112，图 2「Orbits of $H_1$」在 B167 附近；均为页面内联 JS 绘制，**无位图/ SVG 可提取**）。正文另有 1 处 "the following picture" 引用，即上述 canvas 图，不是缺图。本译本据 canvas 绘制指令用 tikz 忠实重画为图 1、图 2（见 README「已知偏差与限制」） |
| 有没有表 | 解析 `<table>` | **3 张**：表 1 讨论班日程（Overview）、表 2 Williamson 型（第 4 章）、表 3 底流形与节点数（第 4 章） |
| 交换图 | `iframe.quiver-embed` | **3 个**（全在第 2 章，q.uiver.app 嵌入；URL 里的 base64 JSON 已解码，见 BRIEF §5） |
| 编号公式 | 扫描 `\tag`/`\begin{equation}`/`(n.m)` | **0 条**（源文 38 处独立公式全部无编号） |
| 独立公式总数 | `$$…$$` 配对 | **38 处**（分布：概论 3、第1章 6、第2章 7、第3章 11、第4章 5、第5章 6 —— 以 `stats.txt` 为准） |
| 定理类环境 | `<div class="env">` | **62 个**（Definition/Theorem/Lemma/Proposition/Corollary/Remark/Example/Exercise/Statement，含若干粗体小标题句） |
| 证明 | `<div class="prf">` | **12 个** |
| 参考文献 | 第 7 章逐条解析 | **32 条**，key 无重复（`gen_refs.py` 实测）；正文引用 key 26 个，其中未被引用的 6 条保留 |
| 文字量 | 正则词数 | 约 9,500 英文词；源块字符 74,874 |
| 目录可信性 | — | 底本无目录；译本用 `\tableofcontents` 自动生成（章/节标题由各译者按 BRIEF 定稿名写） |

## 5. 素材制备产物

| 产物 | 路径 | 数量/说明 |
|---|---|---|
| 逐块源文 | `work/source/chunks_src/*.md` | 11 个片段，246 块，每块 `<<Bnnn kind>>` |
| 整章源文 | `work/source/sections/*.md` | 7 个文件（6 章 + 参考文献） |
| 块总表 | `work/source/blockmap.tsv` | 246 行（id/章/类型/摘要） |
| 片段清单 | `work/source/manifest.json` | 片段 → 源块号 |
| 统计 | `work/source/stats.txt` | chapters/h3/env/prf/table/quiver/display_math 等 |

## 6. 已知风险（开始前登记）

1. **公式是网页源码而非扫描图**：优点是无需 OCR，缺点是底本自身的 LaTeX 笔误会原样带入 → 已知 `\espan`（= span）与英文拼写错误（Sympletic/recollment/thta/paris 等），一律照译 + 批注 + 登记 README。
2. 源文有 `[ENV]` 块实为粗体小标题句 → 已在 STYLE_GUIDE 规定用 `\para`。
3. 底本无图 → 交付物**不插图**；正文提到 "picture" 处保留文字并加批注说明底本缺图。
4. 网页可能随作者更新 → 本译本锁定 2026-11-04 抓取的 HTML 快照（`raw/SYZ.html`），README 声明。
