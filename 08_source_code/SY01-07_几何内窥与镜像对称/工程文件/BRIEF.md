# BRIEF · SY01-07《几何内窥与镜像对称》中译注本

## 1. 书目信息

| 项 | 内容 |
|---|---|
| 原文标题 | Geometric Endoscopy and Mirror Symmetry |
| 作者 | Edward Frenkel（University of California, Berkeley）、Edward Witten（Institute for Advanced Study） |
| 出处 | arXiv:0710.5939v3 [math.AG]，2008-04-05；文末署 Date: October 2007 |
| 底本 | 原书 PDF，130 页；正文 p.3–127，参考文献 p.127–130；PDF 页 = 印刷页 |
| 语言 | 英 → 中（简体） |
| 体例 | 中文译注本：逐句对译 + 公式逐式核对 + 源码内四类批注（Tutor Note / 原文疑误 / 存疑 / 背景补充） |
| 编译 | `xelatex main.tex` 连续两遍（ctex + fandol） |
| 成品 | `工程文件/deliverable/Frenkel-Witten_几何内窥与镜像对称_中文译注本.pdf` |
| 工程编号 | SY01-07（镜像对称组） |

## 2. 结构与页码（PDF 页，据原书目录与页锚点实测）

| 节 | 原文标题（照录） | 页 |
|---|---|---|
| — | 标题、摘要、目录 | 1–2 |
| §1 | Introduction（1.1 T–duality Of Singular Fibers；1.2 A-branes And D-modules；1.3 From Curves Over C To Curves Over Fq；1.4 Classical Endoscopy；1.5 Geometric Endoscopy；1.6 Connection With The Work Of B.-C. Ngô；1.7 Quantum Field Theory；1.8 Plan Of The Paper；1.9 Acknowledgments） | 3–13 |
| §2 | Duality, Branes, and Endoscopy（2.1–2.3） | 13–21 |
| §3 | Explicit Example In Genus One（3.1–3.11） | 21–42 |
| §4 | A-Branes And D-Modules（4.1–4.9） | 42–56 |
| §5 | Spectral Covers, Hecke Operators, and Higher Genus（5.1–5.3） | 56–76 |
| §6 | Categories Of Eigensheaves（6.1–6.6） | 76–87 |
| §7 | The Classical Story（7.1–7.4） | 87–96 |
| §8 | From Hecke Eigensheaves To Hecke Eigenfunctions（8.1–8.10） | 96–111 |
| §9 | Other groups（9.1–9.4） | 111–119 |
| §10 | Gerbes（10.1–10.5） | 119–124 |
| §11 | Appendix. L-packets for SL2 | 124–127 |
| — | References | 127–130 |

> 原书无编号 Figure、无带框表格；唯一插图在 p.18（奇异 Hitchin 纤维，A-模型 $G=SL_2$ 与 B-模型 ${}^{L}G=SO_3$），译本已按 600 dpi 裁剪插入 §2，图注译中文并标原文页码。

## 3. 翻译决定（立项时定下）

1. **标题**：`Geometric Endoscopy and Mirror Symmetry` →「几何内窥与镜像对称」；`endoscopy` 一律「内窥」，`endoscopic`「内窥的」。
2. **术语**：以 `工程文件/GLOSSARY.md` 为唯一裁决书；核心如 geometric Langlands correspondence = 几何 Langlands 对应、Hitchin fibration = Hitchin 纤维化、Hecke eigensheaf = Hecke 本征层、perverse sheaf = 反常层、eigenbrane = 本征膜、fractional = 分数。
3. **保留英文**：gerbe、oper、improper Hecke functor、L-packet、Bun_G、人名与定理名（Langlands、Hitchin、Hecke、Ngô、Kottwitz、Labesse、Shelstad 等）。
4. **编号照抄**：公式 (1.1)–(11.6)、章节号、文献标签 `[KW]`、`[N1]` 等全部保留；不重新编号。
5. **页锚点**：每页正文前插 `% ==== 原文 PDF 第 N 页（印刷页 N）====`；全书 138 处，正文 3–127 无缺页。
6. **批注**：源码内 `% [Tutor Note: …]`（推导补足/易错预警/物理图像）、`% [原文疑误: …]`（判定为原书笔误，译文照录并说明）、`% [存疑: …]`、`% [背景补充: …]`；不改数学内容，不把译者修正伪装成原文。
7. **参考文献**：保留英文原貌（书目信息不可译），编号与原文一致。
8. **脚注**：原文脚注保留为脚注，编号由 LaTeX 重排，可能与原文编号整体偏移。

## 4. 与仓库其他部分的关系

- **资料卡**：`资料卡/` 五件套（00 速览、01 结果清单、02 论证地图、03 条款索引、04 术语文献勘误）；
  另建 YAML frontmatter 单卡（`资料卡/GE-*.md`）供 `kb/ingest.py frontmatter` 入库。
- **术语表**：`工程文件/work/glossary.tsv`，由 `GLOSSARY.md` 转出；完工后并入 `01_corpus_zh/termbase.jsonl`（`pkg=SY01-07`）。
- **数语规范**：服从 `01_corpus_zh/数语规范/`（README + STYLE_NL + STYLE_FORMAL）。
- **原文层**：原文抽文已由 `tools/build_src_corpus.py` 收进 `01_corpus_src/`；本工程不再另做全文扫描件入库。

## 5. 工程状态

- [x] 立项、取底本、确认 130 页与页锚点
- [x] 译本初稿与成品 PDF（97 页，225 个编号公式）
- [x] 四类批注 182 条（Tutor Note 135、原文疑误 29、存疑 12、背景补充 6）
- [x] 2026-11-23 建立页对齐审校底稿（`work/audit/`，13 块）
- [x] BRIEF / STYLE_GUIDE / glossary.tsv
- [x] 整书对照审校（13 块全覆盖）与修订落地（18 处：P1 9、P2 9）
- [x] 批注来源标记（v2.1 §2.5.6）
- [x] 重编译成品入 `deliverable/`
- [x] 资料卡五件套与 work 卡入库（`kb/cards/SY01-07.jsonl`）
- [x] 至少 1 条对齐卡（`leanstmt/fw08-g01`，gap，进 `datasets/leanstmt/index.jsonl`）
- [ ] `RELEASE_REGISTER.csv` 行、`03_translations_meta/SY01-07/`、`make_stats.py --write`

## 6. 许可与来源

原文版权归作者；arXiv 版按 arXiv 许可发布。本译本是研究用中文译注本，不代原作者授权、不另设限制；权利人通知即撤。自产的术语表、资料卡、审校文档按仓库 `COMPLIANCE.md` 与 `LICENSE` 处理。
