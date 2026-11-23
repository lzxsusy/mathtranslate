# BRIEF —— SY02-27《无穷范畴讲义》中译注本

## 一、底本

| 项 | 内容 |
| --- | --- |
| 书名 | *Lectures on Infinity Categories*（课程讲义，未出版；原 PDF 无书名页，题名取课程名） |
| 作者 | 陈麟（Lin Chen），清华大学求真书院 |
| 版本 | 2024 年秋季课程讲义，2024-12-28 生成，共 27 讲 |
| 底本 | 本机 PDF，203 页，US Letter，文字层可抽（Adobe Acrobat Pro DC 22.1 导出） |
| 页码口径 | 底本每讲重新计页（每讲第 1 页印“1”）；**原书页 = PDF 页 − 该讲起始 PDF 页 + 1**，起始页见 `work/lecture_pages.tsv` |
| 底本身份核验 | SHA256 `d8812d052738c9b9d1f5b9c147a3277bea4a1408313362692bb9e824f6bfd267`；首页 "LECTURE 1"，日期 Sep. 10, 2024 |

底本 PDF 只存于仓外 `_底本/SY02-27/`，**不入仓**（04_playbook/17 §3.3）。

## 二、翻译范围

1. 全部 27 讲（PDF 第 1–203 页），每讲含正文、附录（部分讲有 "Appendix A"）与参考文献。
2. 术语与文献：参考文献条目保留原文，不译书名；正文引用标签（`[Lur09]` 等）原样保留。
3. 原书 5 幅编号图（Figure 1–5，均在第 3 讲，PDF 第 19–20 页）由译者用 TikZ 重绘；不改变图的数学内容。
4. 原书第 1 讲的一幅未编号 2-态射示意图（PDF 第 2 页）：以文字说明替代，不另出译注。
5. 封面、译本体例、记号表、讲题总表由 Lead 撰写，非原文内容。

## 三、交付物

| 路径 | 内容 |
| --- | --- |
| `源码/` | `main.tex` + `preamble.tex` + `front/` + `chunks/lec01.tex … lec27.tex` |
| `工程文件/BRIEF.md` | 本文件 |
| `工程文件/STYLE_GUIDE.md` | 译手作业合同（编号、环境、标签、术语、编译） |
| `工程文件/work/glossary.tsv` | 术语表（英—中—等级—依据—首现） |
| `工程文件/work/通读笔记.md`、`疑点清单.tsv` | 通读产物（疑点未解数须为 0） |
| `工程文件/work/lecture_pages.tsv`、`work/src/lecNN.txt` | 讲页表与抽取源文 |
| `工程文件/tools/extract_src.py`、`compile_chunk.py`、`build.sh` | 抽取、单讲编译、整书编译 |
| `工程文件/deliverable/*.pdf` | 成品 PDF |
| `资料卡/` | `00-速览.md`、`01-概念.tsv`、`02-命题.tsv`、`03-论证链.md`、`04-术语文献勘误.md`、`index.jsonl`、`cards/*.json` |

## 四、验收（G0–G7）

- G0 抽取完整：27 讲页码连续、无缺页；源文可读。
- G1 单讲：`compile_chunk.py NN` 零 error；编号对象数与源文一致；无手打编号。
- G2 整书：xelatex 三遍零 error、无 `??` 引用、无缺字（missing character）。
- G3 版式：正文 10pt、1in 边距、页眉左“无穷范畴讲义”右讲题；定理头加粗、正文直立；公式按节编号；附录 A/B 正常。
- G4 术语：glossary 全覆盖，正文术语与表一致；`build_norm.py --check` 通过。
- G5 资料卡：五件套齐全，01/03 每条带原书页；至少 1 条对齐卡进 `index.jsonl`。
- G6 登记：`RELEASE_REGISTER.csv` 一行 + `03_translations_meta/SY02-27/投稿信息.md`；`check_compliance.py` 无 error。
- G7 统计：`make_stats.py --write` 后与 `_meta/stats.json` 一致；CHANGELOG 一条。

## 五、合规红线

1. 底本 PDF、页图、扫描件不进仓库；正文不出现本机绝对路径。
2. 不提交 `*.aux`、`*.log`、`*.out`、`*.toc`、`*.synctex.gz`、`_test_*.tex`、`__pycache__`。
3. 英文短引 ≤120 字符，只引必要片段；译文为演绎作品，按仓库许可条款处理。
4. 来源黑名单（知乎、百度百科、CSDN、简书、公众号、B 站、个人博客、“XX 笔记”）命中数必须为 0。
5. 不 push 他人未完成的改动；提交只含本工程与登记文件。
