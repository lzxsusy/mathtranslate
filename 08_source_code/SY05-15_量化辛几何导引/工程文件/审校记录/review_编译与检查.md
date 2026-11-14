# 编译与检查报告

**工程**：《量化辛几何导引》中文译注版（张俊、祝安铜 原著，英文版，中国科学技术大学出版社 2025）
**日期**：2026-10-24
**结论**：源码在本地 TeX Live 2026 下**实际编译通过**：**317 页，0 error，0 Missing character，0 未定义引用**；全书 334/334 页正文逐页覆盖；13 个分部静态检查全部通过。

---

## 一、编译环境与方法

| 项目 | 说明 |
|---|---|
| 编译器 | XeLaTeX（TeX Live 2026，`xelatex`） |
| 文档类 | `ctexbook`（UTF8，fontset=Fandol，11pt，A4，oneside，openany） |
| 宏包 | amsmath, amssymb, amsthm, mathtools, bm, graphicx, xcolor, tcolorbox, caption, enumitem, booktabs, array, multirow, fancyhdr, hyperref, bookmark |
| 命令 | `python tools/build.py`（内部：`tools/make_main.py` 生成 main.tex → xelatex 两遍） |
| 输出 | `main.pdf`，317 页，约 28.8 MiB |
| 编译日志 | 0 个 `!` 错误；`Missing character` 0；未定义引用 0；Overfull hbox 4 处、Underfull hbox 36 处（长 URL 与中英混排所致，视觉上不可见/不影响阅读） |

> 注：编译过程中曾两次因**并发 xelatex 占用 `main.aux`** 导致 `main.aux` 出现 NUL 字节而报 `Missing \begin{document}` / `invalid character`；该问题与正文源码无关。最终编译前已清空 `main.aux/main.toc/main.out` 并串行执行，`tools/build.py` 现在会在编译前自动清理这些中间文件。

## 二、覆盖与结构核查（`tools/check.py all`）

- **正文覆盖**：13 个分部（ch01–ch10b）合计 **334/334 页**全部有 `% >>> pNNN` 覆盖标记，无缺页；仅 ch05a 与 ch05b 在接缝页 p128 按体例各标一次。
- **章节**：10 章、59 节；每章恰有一个 `\chapter`（第 5、8、9、10 章由两位译者分段续写，续写文件均无 `\chapter`）。
- **本节重点**：59 个 `\section` 每个都有且仅有一个 `keytakeaways` 框。
- **定理类环境**：652 个（定义/定理/命题/引理/推论/猜想/例/练习/注/记号/断言/问题/疑问/事实，编号逐条照原文手工传入；原书为「同类环境在节内独立计数」）。
- **编号公式**：351 条 `\tag`，按章连续，无重号/跳号。第 9 章原书两次印出 (9.16)，译文以 `\tag{9.16}` 与 `\tag*{(9.16)}` 忠实保留。
- **插图**：131 处 `\includegraphics`，对应 `figures/` 中 131 个 300 dpi 裁剪文件，**文件全部存在**；124 幅为原书编号图（图号逐章连续），其余为无编号示意图；图注均含中文说明与原书图号/印刷页码/PDF 页码。
- **Tutor Note**：426 条 `% [Tutor Note: …]`（LaTeX 注释，不进入排版）。
- **参考文献**：248 条（原书 [1]–[248]，保留英文原文；长 URL 已用 `\url` 与 `\sloppy` 处理）。
- **索引**：418 条（中文术语 + English + 原书页码；页码为原书印刷页码，已在索引开篇注明）。

## 三、交付文件

```
量化辛几何导引_中文译注版/
├── main.tex                     # 主文件（自动生成，63 个 \input）
├── preamble.tex                 # 导言区
├── tex/                         # 64 个片段：00-front、ch01–ch10（含分段）、90-bib、91-index
├── figures/                     # 131 张 300 dpi 插图
├── tools/                       # build.py / make_main.py / check.py / pageimg.py / stats.py / collect_reviews.py
├── 审校记录/                    # 原文疑误汇总、各章审校记录、QA 报告、本报告
├── 量化辛几何导引_中文译注版.pdf
└── README.md
```

## 四、已知限制（须提请教授注意）

1. **底本缺失附录 Exams**：扫描件中无原书印刷页 335–344（四次考试），经目录页码与文献页起始页核对确认系扫描遗漏。本译注版不含该附录；如需完整，请提供该 10 页的高清扫描。
2. **底本 PDF p353（印刷页 355）为损坏扫描页**：整页二次曝光/重影，页眉与条目编号不可辨。该页 18 条文献（原书 [179]–[196]）按字母序与前后编号 [178]/[197] 夹逼恢复，人名按学界通行拼写排印，**建议对照原书复核**。
3. **索引页码**：照原书 Index 转录，页码为原书印刷页码（不是本译注版页码）；已在索引开篇说明。
4. **公式与符号**：全部公式均由译者逐符号从扫描图像手工录入并加批注核对；个别扫描模糊处已在正文以 `% [Tutor Note]` 或 `% [系统提示]` 标注。原书疑误一律保留原文写法并加注（约 150 条，见 `review_原文疑误_汇总.md`）。
5. **版式**：文档类采用 `ctexbook`（专著体例）而非 article；若教授希望改为 article/revtex4-2，只需替换 main.tex 首行并调整 `\chapter` 为 `\section`，其余环境定义保持不变（preamble 已刻意兼容）。

## 五、复现命令

```bash
# 编译（XeLaTeX 两遍）
python tools/build.py

# 逐章覆盖与静态检查
python tools/check.py all

# 统计
python tools/stats.py
```
