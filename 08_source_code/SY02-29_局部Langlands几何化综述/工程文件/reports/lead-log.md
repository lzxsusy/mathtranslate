# lead-log —— SY02-29 决策流水

记录 Lead 在统稿期做的每一次**会影响多文件**的裁定。逐文件的小修在各 `trace-*.md` 里。

## 1. 编号与命名

- 发布编号 **SY02-29**。核查 `RELEASE_REGISTER.csv`：现有至 SY02-28；`08_source_code/` 无同名目录。
- 章节文件按语义命名（`s02-curve-a`、`s04-bung`、`s10-kottwitz`…），不按原文节号命名，
  以便页界与原文目录不完全对齐时仍能自由切分。
- 单篇结构：`\section` 直接对应原文 1–9 节，`\renewcommand{\thesection}{\arabic{section}}`；
  定理/定义/命题/注/例/猜想/期望**共用一个** `[theorem]` 计数器，故自动得到原文的 3.1、4.3 这类编号。

## 2. 术语裁定（即冻结，改名须三同步：正文 + glossary + 卡片）

| 英文 | 中译 | 依据 |
|---|---|---|
| diamond | 菱形 | SY02-26 已冻结 |
| untilt | 保留英文 | 无稳定中译，SY02-26 同 |
| perfectoid | 完满（空间） | SY02-26 已冻结 |
| `Bun_G`、`B_dR`、`B^+_cris` | 保留 | 记号，不译 |
| shtuka | shtuka（斜体） | 学界通用，不译 |
| perverse sheaf | 反常层 | 与 SY02-26 一致 |
| Hecke eigensheaf | Hecke 特征层 | 术语表 1.7 行 |
| extended pure inner form | 扩充纯内形式 | 与 Kottwitz 原文对应 |
| basic | 基本 | `B(G)_basic` 基本轨迹 |
| admissible locus | 容许轨迹 | 学界常用 |
| Hodge–Tate period morphism | Hodge–Tate 周期态射 | 与 §7 行文统一 |
| Newton / Harder–Narasimhan 分层 | 牛顿分层 / HN 分层 | 不缩写为「HN 层」以外的形式 |

## 3. errata 政策（本册统一）

1. **拼写、衍字、明显笔误**：正文照译原样，紧跟一条 `\yizhuw` 或 `\yizhu` 说明原文写法；
   同时登记 `疑点清单.tsv`（状态「已解」）。不静默改。
2. **小节标题讹误**（§1.5.3「equal characteristic」、§3.3.2 同）：**按内容改题**，并在该节
   首段挂译注说明原文标题，登记疑点清单。理由：标题进目录，照排会让读者系统性误读。
3. **数学错误或未定论**（p.32 的 $\mathbb D_S\subset\mathbb D_S^*$、p.37 Tate 扭转符号、
   p.42 命题 9.1(2) 的指标）：保留原样，登记「待核」，不擅自订正。
4. **已撤的 errata**：曾把 p.28「via the conjecture 3.21」判为讹误，后核出 §3.5 确有
   Conjecture 3.21（`conj:3.21`），遂撤销该条并删去相应译注。

## 4. 页锚与页码

- `\srcpage{N}` 排页边（`marginnote`），`\srcpageinl{N}` 排行内（页界落在句中时用）。
- 每页起点标一次；文件边界处允许重复（两个文件各自可单章编译所必需），故 `main.pagemarks`
  形如 `1 2 3 3 4 …`，最终覆盖 p.1–p.46 无缺页。
- 页脚注编号连续，不做「每页重置」。

## 5. 事故与修复（影响全书，勿重犯）

| 症状 | 根因 | 修复 |
|---|---|---|
| 首轮 `xelatex` 报 `Undefined control sequence \cE` | preamble 只逐字定义了部分 `\cX` | `\@tfor` 一次定义 `\cA`–`\cZ` |
| 正文页眉一直显示「目录」 | book 类 `\sectionmark` 为空、本文无 `\chapter` | `\renewcommand{\sectionmark}` + `\section*` 后手加 `\markright` |
| 页边「p.N」跑到纸外 | `book` 默认 `\marginparwidth=116pt` > 2.6cm 页边距 | `\setlength{\marginparwidth}{1.9cm}`、`\marginparsep=2pt` |
| 单章各自 `\providecommand{\llbracket}` 等 | 各译手并行、互不知情 | 宏集中到 preamble（`stmaryrd` + `\Perf` + `\Ql`），删各文件局部定义 |
| 子代理派工被拒 `active child limit: 8` | 同时活跃 8 个（7 译手 + 1 卡片组） | 按空槽数逐个补派，完成通知到即补位 |
| 同一术语三写（`torsor`／挠子／扭子） | 7 名译手各自体例、glossary 未先收该条 | 统一保留英文 `torsor`（首现括注「主齐性空间」），glossary 补条，台账 `CF-2026-11-23-06` 关单 |

## 6. 工具

- `工程文件/tools/render_pages.py`：pymupdf 渲染页面图（核对公式用），
  `PYTHONIOENCODING=utf-8 python 工程文件/tools/render_pages.py 3-10 --dpi 150`。
- 资料卡质检：`python 资料卡/tools/lint_cards.py 资料卡/cards --prefix sy29 --max-pages 46`、
  `python 资料卡/tools/verify_quotes.py 资料卡/cards --root . --strict`。
  注意 `verify_quotes.py` 原先硬性要求工程根存在 `01_pages/`（真正读的是
  `工程文件/work/src/`）。后改为 `_has_pages(root)`：`01_pages/` 或 `工程文件/work/src/`
  任一存在即可，故空的 `01_pages/` 标记目录已删；两套目录都按 COMPLIANCE L4 不入仓。
