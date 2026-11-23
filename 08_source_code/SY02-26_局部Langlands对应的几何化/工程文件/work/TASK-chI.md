# 任务书 · Chapter I（样板章）p.7–44

开工前必读（按顺序）：`工程文件/BRIEF.md` → `工程文件/SPEC.md` → `工程文件/work/通读笔记.md`
→ `工程文件/work/glossary.tsv` + `work/symbols.tsv` → 你这块的原页 `01_pages/pNNN.txt` + 渲染图像。

## 分块与产出文件

| 块 | 覆盖 | 页 | 产出 tex | 报告 | trace |
|---|---|---|---|---|---|
| A | I.1 局部 Langlands 对应；I.2 总体图景；I.3 FF 曲线；I.4 Bun_G 的几何 | 7–22 | `源码/sections/s01-chI-1.tex` | `reports/chI-a.md` | `work/trace-chI-a.md` |
| B | I.5 ℓ-进层；I.6 几何 Satake；I.7 shtuka 模空间上同调；I.8 L-参数叠；I.9 L-参数的构造 | 23–38 | `源码/sections/s02-chI-2.tex` | `reports/chI-b.md` | `work/trace-chI-b.md` |
| C | I.10 谱作用；I.11 思想来源；I.12 致谢；I.13 记号 | 39–44 | `源码/sections/s03-chI-3.tex` | `reports/chI-c.md` | `work/trace-chI-c.md` |

> main.tex 已 `\input{sections/s01-chI-1}` 等三处，你不用改 main.tex；如果一行都还没写，文件里只有一行注释，直接覆盖。

## 硬要求（违反即退回）

1. **逐段对照翻译**，段落数、环境类型（定理/定义/注/例/证明）与原文一致；不许合并、不许跳段。
   原文某段是目录/公式列表也照原样排。
2. **每页起点**放 `\srcpage{N}`（PDF 页号）。**必须放在段首**（`\par` 之后、该页第一段正文之前），
   不要夹在句子中间或行内公式后面——`marginnote` 在行中间会静默不印（已实测丢过 p.40）。
   编译后跑一遍：
   ```bat
   cd 源码 && build.bat check sections/sNN-*.tex <tag>
   python ..\工程文件\tools\check_pagemarks.py _check_<tag> --start <首> --end <末> --pdf
   ```
   必须 `[ok] … 锚点齐全` 且 `[ok] … 全部在 PDF 中可见`。丢了的，把锚点挪到段首再编；
   **页界本来就落在句子中间、挪不开**的，改用行内锚点 `\srcpageinl{N}`（排成小上标〔p.N〕，不会被吞）。
3. **公式回图核对**：含公式的段落，用 `pymupdf` 把该页渲染成 PNG（dpi 150）看一眼，再落笔。
   渲染代码：
   ```python
   import pymupdf
   d = pymupdf.open(r"00_原文\fargues-scholze-2102.13459v4.pdf")
   d[18].get_pixmap(dpi=150).save(r"_page19.png")   # d[18] = PDF p.19
   ```
   看完删图，别把 png 留在工程里。
4. **译注**：术语首次出现、跳步、疑似笔误各至少一条；格式 `\yizhu{注文}{A：原文 §I.3 p.20；nLab "…"}`，
   无依据用 `\yizhuw{…}`。**注文不许出现"我认为作者想说"式推测**。
5. **术语按 glossary.tsv**；缺的词不许自造，保留英文 + 在报告 §术语新增 里提，Lead 裁定后补表。
6. **编号对象对齐表**（报告里）：原文定理/命题/引理/定义/注/例/公式 编号 → 译文 label → 一致?
   数量必须等于原文（少一个 = 漏译）。
7. **编译**：`cd 源码 && build.bat check sections\sNN-*.tex` → `_check.pdf`，必须 0 error。
   注意 `build.bat check <file>` 用的是相对 `源码/` 的路径。
8. **只写自己的三个文件**（tex + report + trace）。不许动 main/preamble/别人的 sections/glossary/pages/PDF。
9. **trace 文件**：≥10 条决策，四栏（判断点 / 依据 / 结论与理由 / 事后确认），其中 ≥2 条是弯路
   （先写错→发现→改回来）。只写真实发生的，禁止编造。
10. 不 git push；不写本机绝对路径进 tex；控制台 GBK 不要 print 中文；文件 UTF-8 无 BOM。

## 报告模板（`reports/chI-x.md`）

```
# Chapter I · 块 X（p.a–b）
## 1. 完成范围
逐节列出（I.k 标题 / 原文页 / 译文小节数）
## 2. 编号对象对齐
| 原文 | 译文 label | 一致 | 备注 |
## 3. 公式核对
核对了 p.a–p.b 共 N 页；提取错误 M 处（列出）
## 4. 译注
共 N 条：术语 a / 跳步 b / 笔误 c / 其他 d；每条一句摘录
## 5. 术语新增（待 Lead 并入）
英文<TAB>建议中文<TAB>依据
## 6. 疑点（未解）
...
## 7. 遗留问题
```

## 回报（≤15 行）
块编号、页范围、编译结果（0 error?）、编号对象数、译注条数、新增术语数、疑点未解数、trace 条数与弯路数、遗留问题。
