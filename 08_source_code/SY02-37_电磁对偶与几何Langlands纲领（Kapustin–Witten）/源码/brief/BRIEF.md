# BRIEF：KW06 中译注本工程

## 0. 一句话

把 **A. Kapustin & E. Witten, "Electric-Magnetic Duality And The Geometric Langlands Program"**
（arXiv:hep-th/0604151v3，231 页，2006 年 4 月；v3 2007 年 1 月）译成简体中文学术版
LaTeX 源码 + 成品 PDF，并附：思路导读、注疏（译注）、译对报告（对照校订）、插件评估报告。

## 1. 底本与工作目录

| 项 | 值 |
|---|---|
| 底本 | `src_orig/glshort.tex`（arXiv e-print 解包的 harvmac 源码，11886 行，12 节 71 小节 348 编号公式 146 文献） |
| 编号映射 | `src_orig/glshortspare.defs`（公式号/节号/文献号） |
| 已出版 PDF 文本 | `C:\Users\admin\Downloads\kw06_text.txt`（pdftotext 全文）、`kw06_pages\p001–p118.txt`（逐页） |
| 原 PDF | `C:\Users\admin\Desktop\威腾讨论班_第二期\work\source\pages\KW06.pdf`（PDF 页 = 印刷页 + 1） |
| 翻译脚手架 | `skel/NN-sXX.tex`（36 片，英文 LaTeX，公式/编号/`\label`/`\cite` 已锁定） |
| 译稿输出 | `zh/NN-sXX.tex`（同名同序） |
| 分片校对日志 | `logs/NN-sXX.md` |
| 成品 | `out/KW06_中译注本_v1.0.pdf` |

## 2. 必读材料（每个译者强制）

1. `brief/SPEC.md` —— 翻译与排版规范（硬约束，先读）。
2. `brief/GLOSSARY.tsv` —— 111 条术语定译（含「首现」「易混淆点」两列，务必按表）。
3. `brief/reading/witten2008.txt` —— Witten, *Mirror Symmetry, Hitchin's Equations, And Langlands Duality*（arXiv:0802.0999）全文：**同一作者对同一套想法的短综述**，用来校准术语与物理图像。
4. `brief/reading/frenkel2009.txt` —— E. Frenkel, *Gauge Theory And Langlands Duality*（arXiv:0906.2747，Séminaire Bourbaki）全文：**数学家的反向综述**，用来校准几何侧术语（Hecke 特征层、D-模、oper）。
5. `brief/SECTION-MAP.md` —— 12 节 ↔ 本工程分片 ↔ 概念地图（来自既有解经本）。
6. 需要时：`brief/一页纸.md`（全局速览）。

## 3. 参考而不许抄袭

本机已有既有成果，可用作**理解与术语核对**，但**禁止照抄其译文/表述**：

- 解经本（219 页）：`C:\Users\admin\Desktop\数译发布\gitee_shuyi\05_seminar_witten\seminars\SEM-0604151\`
  - `deliverables/WIT-0604151-EMDGL_exegesis.pdf`、`deliverables/章节地图.md`、`一页纸.md`
  - `manuscript/sections/30_flesh_twist.tex`、`31_flesh_hitchin.tex`、`32_flesh_hecke.tex`、`33_flesh_dmod.tex`（四张深读卡）
  - `plan/02_符号与风格卡.md`（符号与易错译法表，**必读一遍**）
- 讨论班导读：`C:\Users\admin\Desktop\威腾讨论班_第二期\work\rounds\U06\report_v2.md`
- 姊妹篇 GW06 中译本（体例范本）：`C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-06_规范理论、分歧与几何朗兰兹纲领\`

抄袭判定：连续 15 字以上与既有中文成果相同且无引号标注 = 抄袭。译文必须是**从英文原文重新生成的**。

## 4. 交付物清单（工程内）

```
KW06_work/
├─ brief/          BRIEF.md SPEC.md GLOSSARY.tsv SECTION-MAP.md 一页纸.md reading/
├─ src_orig/       arXiv 源码 + defs
├─ skel/           36 片英文脚手架（只读，不改）
├─ zh/             36 片中译（译者写这里）
├─ logs/           36 份分片校对日志（译者写这里）
├─ figures/        20 张图（EPS→PNG）
├─ tools/          harvmac2tex.py postfix_tables.py build.py …
├─ reports/        译对报告、插件评估、注疏汇编、思路导读
├─ main.tex refs.tex macros.tex
└─ out/            成品 PDF
```

仓库落点（全部完成后由 lead 上传）：
`数译发布/gitee_shuyi/08_source_code/SY02-XX_Kapustin-Witten_电磁对偶与几何朗兰兹纲领/`

## 5. 流程

1. **脚手架**（lead，已完成）：arXiv 源码 → harvmac→LaTeX → 36 片 + `refs.tex` + `macros.tex` + 3 张表重排 + 20 图。
2. **分片翻译 + 逐片校对**（译者，每人领 1–3 片）：读 SPEC/GLOSSARY/两份综述 → 逐段译为中文 → 写 `logs/NN-sXX.md`（P1/P2 问题、检索记录、术语新增）。
3. **「译对」**（对照校订，第二轮）：抽 12 个关键片段，与已出版 PDF 原文逐式对照 + 与 Witten 08 / Frenkel 09 说法互校，出 `reports/译对报告.md`。
4. **注疏汇编**：`yizhu` 汇成 `reports/注疏汇编.md`（分类：易错点 / 含糊点拨 / 物理图像 / 原文疑误）。
5. **思路导读**：`reports/思路导读.md`（12 节，每节：任务—输入—构造—产物—出口，附原文页锚）。
6. **插件评估**：`reports/插件评估.md`（本机知识库 `kb.mjs`、nLab 本地索引、外部 nLab/web 的实际使用与命中率，含失败案例）。
7. **编 PDF** → `out/`，验收：公式编号与原文一一对应、无 `@@` 残留、无编译错误、目录完整。
8. **上传** AtomGit（`git push atomgit master:main`）。

## 6. 验收标准

- [ ] 36 片全部有 `zh/` 译文，中文占比 > 95%（数学/文献除外）。
- [ ] 公式编号与原文逐式对齐（`grep -c "式 ("` 与 348 对应量级）。
- [ ] 每片 3–8 条 `yizhu`，每节 `keytakeaways`。
- [ ] 术语首现「中文（English）」，全书一致（对照 `GLOSSARY.tsv`）。
- [ ] `xelatex` 三遍零错误，PDF ≥ 200 页，目录/交叉引用正常。
- [ ] 五个报告齐备。
