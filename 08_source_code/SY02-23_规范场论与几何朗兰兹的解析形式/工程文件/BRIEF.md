# BRIEF — SY02-23《规范场论与几何朗兰兹的解析形式》

## 0. 项目信息

- 仓库编号：SY02-23
- 中文题名：规范场论与几何朗兰兹的解析形式
- 英文原题：*Gauge Theory and the Analytic Form of the Geometric Langlands Program*
- 作者：Davide Gaiotto（Perimeter Institute）、Edward Witten（IAS）
- 底本：arXiv:2107.01732v4 [hep-th]，2022-08-22，112 页；期刊版：Annales Henri Poincaré 25 (2024) 557。
- 底本形态：arXiv LaTeX 源码（`GLDraft_D.tex`，4,493 行）＋ 11 个图 PDF；以源码为工作底本，保留全部编号与公式。
- 工作目录：`08_source_code/SY02-23_规范场论与几何朗兰兹的解析形式/`
- 目标：完成全文中文翻译、可核查译注、交叉审校、可编译源码与成品 PDF，并按仓库规范登记、推送。

## 1. 交付物清单

| 类别 | 路径 | 状态 |
|---|---|---|
| 翻译源码 | `源码/main.tex` + `源码/chunks/ch01–ch17.tex` + `preamble.tex` + `macros.tex` | 骨架完成；ch01 已译，ch02–ch17 待译 |
| 图 | `源码/figures/*.pdf`（11 个） | 已就位 |
| 风格指南 | `工程文件/STYLE_GUIDE.md` | 完成 |
| 术语表 | `工程文件/work/glossary.tsv` | 完成 |
| 通读笔记 | `工程文件/work/通读笔记.md` | 待写（本 BRIEF 附摘要） |
| 疑点清单 | `工程文件/work/疑点清单.tsv` | 待写 |
| 成品 PDF | `成品/SY02-23_…_arXiv-2107.01732_v1.0.pdf` | 待生成 |
| 资料卡五件套 | `资料卡/00-速览.md` … `04-术语文献勘误.md` | 待写 |
| 投稿信息 | `投稿信息.md` | 待写 |
| 精选片段 | `精选片段.md` | 待写 |
| 登记 | `RELEASE_REGISTER.csv` 一行 + `03_translations_meta/SY02-23/` | 待办 |

## 2. 分块表

块首注释给出了每块对应的原文行号；只译散文，公式/编号/引用/图锁定。

| 块 | 原文行 | 内容 | 目标文件 | 状态 |
|---|---|---|---|---|
| ch01 | 212–290 | §1 引言 | `chunks/ch01.tex` | 已译，样板 |
| ch02 | 291–559 | §2.1–2.2 基本设置、复流形量子化 | `chunks/ch02.tex` | 待译 |
| ch03 | 560–732 | §2.3–2.4 希格斯丛模空间、Hitchin 哈密顿量 | `chunks/ch03.tex` | 待译 |
| ch04 | 733–1033 | §2.5–2.8 对偶膜、局部约束、拓扑细节、oper 边界 | `chunks/ch04.tex` | 待译 |
| ch05 | 1034–1151 | §3 Hitchin 哈密顿量的本征值 | `chunks/ch05.tex` | 待译 |
| ch06 | 1152–1382 | §4.1–4.2 线算符、Wilson 算符 | `chunks/ch06.tex` | 待译 |
| ch07 | 1383–1765 | §4.3 对偶 't Hooft 算符、Hecke 对应、仿射 Grassmann 流形 | `chunks/ch07.tex` | 待译 |
| ch08 | 1766–1973 | §5 量子形变 WKB 条件 | `chunks/ch08.tex` | 待译 |
| ch09 | 1974–2284 | §6 实丛 | `chunks/ch09.tex` | 待译 |
| ch10 | 2285–2440 | §7.1–7.2 BAA 边界条件的四维化身、手征代数 | `chunks/ch10.tex` | 待译 |
| ch11 | 2441–2842 | §7.3–7.7 从角到态、Dirichlet、Nahm 极点、增广 Neumann | `chunks/ch11.tex` | 待译 |
| ch12 | 2843–3169 | §8 Hecke 算符与谱流模 | `chunks/ch12.tex` | 待译 |
| ch13 | 3170–3425 | §9 辛玻色子给出的波函数＋致谢 | `chunks/ch13.tex` | 待译 |
| ch14 | 3426–3539 | 附录 A 局部算子与 φF 量子修正 | `chunks/ch14.tex` | 待译 |
| ch15 | 3540–3802 | 附录 B B-模型希尔伯特空间 | `chunks/ch15.tex` | 待译 |
| ch16 | 3803–4099 | 附录 C 典范 oper 截面关系＋附录 D 本征函数奇异性局部模型 | `chunks/ch16.tex` | 待译 |
| ch17 | 4100–4488 | 参考文献（英文原样） | `chunks/ch17.tex` | 保持英文，仅校对 |

注意：
- 原文 §2.3、§3 等标题前有前导空格，`grep '^\\section'` 会漏；以文件内容为准。
- ch16 同时含附录 C 与 D，块首注释已更正。
- ch13 末尾含致谢（3420–3424），一并译出。
- ch17 只保留 `thebibliography` 环境内容，`\end{thebibliography}` 与 `\end{document}` 已由 `main.tex` 处理；不要重复。

## 3. 翻译与译注要求（摘要）

完整规范见 `STYLE_GUIDE.md`。要点：

1. 准确优先；术语以 `work/glossary.tsv` 为准；首现关键术语给英文。
2. 公式、`\label`、`\ref`、`\eqref`、`\cite` 键、图文件名、文献表不动。
3. 作者脚注用 `\footnote`；译者注用 `\zy{}`（短）或 `yizhu` 环境（长，每块至多一个）。
4. 译注必须有来源或明确写“译者按（无外部依据）”；禁止编造文献、禁止黑名单网站、禁止把推测写成事实。
5. 原文笔误照译，另加译注并在 `work/疑点清单.tsv` 记录。
6. 只改自己负责的 chunk 文件；不改 `main.tex`、`preamble.tex`、其他 chunk。

## 4. 已知原文笔误（翻译时照译＋译注＋勘误）

| 位置 | 原文 | 应为 |
|---|---|---|
| §2.3（约 567 行） | `$G$-bundle $E\to G$` | `$E\to C$` |
| §4.2（约 1290 行） | `the fiber of this bundle at $b\times b$` | `$b\times p$` |
| §2.7 等 | `Stieffel-Whitney` | `Stiefel–Whitney` |
| §5.1 | `characteristic poiynomial` | `characteristic polynomial` |
| 图 Timing 标题 | `Diffemorphism inariance` | `Diffeomorphism invariance` |
| §6.2 | `antihomomorphic involution` | `antiholomorphic involution` |
| §6.2 | `assume thast` | `assume that` |
| §7.1 | `deformed Neuman boundary` | `deformed Neumann boundary` |
| 全文 | `Kahler` 未加变音 | 译文统一“凯勒” |

## 5. 工作流程

1. **翻译**：每块一个智能体，按本 BRIEF 与 STYLE_GUIDE 施工，完成后报告译注条数与存疑点。
2. **合并编译**：lead 跑三遍 `xelatex`，修未定义引用、缺图、溢出；抽查页面。
3. **交叉审校**：另派审校智能体逐块核对译注来源与措辞，重点清除无依据的“事实性”译注；审校者可直接修订。
4. **元数据**：写资料卡五件套、投稿信息、精选片段、疑点清单定稿、通读笔记。
5. **登记与闸门**：`RELEASE_REGISTER.csv`、`03_translations_meta/SY02-23/`、`make_stats.py --write`；跑 `make_stats.py --check`、`tools/check_numbers.py`、`tools/build_norm.py --check`、按需 `check_compliance.py`。
6. **提交**：git add/commit/push 三远端（至少 origin）。

## 6. 验收标准

- `源码/` 可在干净目录用 `xelatex main.tex` 连编三遍通过，无 `!` 错误，无未定义引用/文献。
- 成品 PDF 页数与原文相当（预计 120–140 页），图完整，公式编号与原文一致（按节编号）。
- 译注全部可追溯或明确标注无依据；交叉审校记录留存。
- 仓库规范要求的文件齐全，闸门脚本通过。
- 推送成功，远端可见。
