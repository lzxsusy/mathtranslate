# 工作流说明 · SY01-26《镜像对称与代数几何》校订工程

本目录是可复现的完整工作流：从扫描 PDF 到《校订记录》《译注》《原文笔误表》与 24 张概念资料卡。所有脚本在 Windows 11 + Python 3（venv）+ MiKTeX 下实测跑通。

## 0. 环境

```
python  = .venv/Scripts/python.exe        # 需 rapidocr_onnxruntime, pymupdf
latex   = latexmk -xelatex（MiKTeX）      # 成品构建
OCR     = RapidOCR（onnxruntime，中英混排模型）
```

`python -m venv .venv && .venv/Scripts/pip install rapidocr_onnxruntime pymupdf`

## 1. 底本与页码换算

| 项 | 值 |
|---|---|
| 原书 | Cox & Katz, *Mirror Symmetry and Algebraic Geometry*, AMS MSM 66, 1999 |
| 主扫描 | 495 页，504×720 pt，纯图像无文本层 |
| 锐利扫描 | 251 页 A4 横版，每页并排两页印刷页，公式清晰，用于公式级核对 |
| 页码 | **PDF 物理页 = 印刷页 + 23**；译本 `\SourcePage{N}` 的 N 即 PDF 物理页 |

## 2. 流水线

| 步 | 脚本 | 作用 | 产出 |
|---|---|---|---|
| 1 | `ocr_book2.py` | RapidOCR 逐页 OCR（300 dpi，`det_limit_side_len=1600`，8 进程） | `ocr2/pNNN.txt`（483 页） |
| 2 | `build_altmap.py` | OCR 锐利扫描的页眉页码，建立印刷页→(PDF 页, 左/右半) 映射 | `altmap.json`（431 页） |
| 3 | `showpage.py` | 按**印刷页**渲染单页 PNG（公式核对用），自动回退主扫描 | `pvNNN.png` |
| 4 | `make_units.py` | 按 `\SourcePage` 切段，每 3 页合并为一个校对单元 | `units/u01..u153.tex` + `.en.txt` + `manifest.json` |
| 5 | `check_pages.py` | 校验 `\SourcePage` 覆盖、唯一性、单调性 | 控制台报告 |
| 6 | `02_校对workflow.js`（DSH workflow） | 153 单元分 8 批，每单元一个子智能体逐句对照，产出疑点 JSON | `review/uXX.json` |
| 7 | `apply_review.py` | 把疑点按 (file, quote→new) 机械套用到 `chapters/*.tex` | `review_applied.json`、`review_unmatched.json` |
| 8 | `global_fix.py` | 全局术语替换（单值化→单值性、虚基本类→虚拟基本类、通用族→万有族、线性束→线性系）；**必须在第 7 步之后** | 直接改 `chapters/*.tex` |
| 9 | `make_report.py` | 汇总为三份交付文档 | `校订记录.md`、`译注.md`、`统计.json` |
| 10 | `rank_pages.py` | 按「数学标记密度」排可疑页，供人工公式核对 | 排序表 |
| 11 | `audit_terms.py` / `audit2.py` / `cmp_glossary.py` | 术语审计、库内跨项目对照 | 术语对照与冲突表 |
| 12 | `03_资料卡workflow.js` | 24 张概念资料卡（每卡一个子智能体，按 playbook 13 号十一节模板） | `资料卡/MS-XX-*.md` |
| 13 | `04_核验workflow.js` | 逐卡核验卡片断言（外部文献 + 自算），24 张分 3 批 | `资料卡/_核验/MS-XX.json` |
| 14 | `make_verify_report.py` | 汇总核验 JSON 为核验记录（✓/✗/△ 三判 + 本机复算表） | `资料卡/_核验记录.md` |
| 15 | `verify_arith.py` / `verify_quintic.py` / `verify_instanton.py` | 本机复算：Betti/Euler 数、基础周期 ω₀、镜像映射 770、K(q) 前四项 | 控制台输出（已录入核验记录第三节） |

## 3. 校对单元协议

每个单元 `units/uXX.tex` 首行是 `% UNIT uXX ...` 注释，正文第 2 行起对应 `chapters/某章.tex` 的连续行；`uXX.en.txt` 是同页英文 OCR（`[p.123]` 标页）。子智能体只读这两个文件，输出：

```json
{"unit":"u30","issues":[{"line":46,"page":99,"type":"术语","quote":"单值化权滤过","new":"单值性权滤过","problem":"monodromy→单值化，应为单值性","confidence":"high"}],"skipped":[{"line":35,"reason":"该行公式 OCR 糊，无法逐字核对"}],"notes":[{"page":99,"text":"译注……"}]}
```

- `type ∈ {错译, 漏译, 增译, 术语, 记号, 数学, 病句, 指代}`
- `quote` 必须逐字、不跨行，供机械替换；`new` 为替换文本
- OCR 无法辨认的公式一律进 `skipped`，不许臆断
- 每单元最多 2 条译注

## 4. 并发约束（重要）

DSH 的 workflow 同时活跃子智能体上限为 **8**。全并行 `pipeline(153 项)` 会直接报
`subagent limit reached (active child limit: 8)`。必须用 `for` 批次 + `parallel`，每批 8 个；
实测每批 8 单元约 15–27 分钟，全书 153 单元约 4–6 小时。

## 5. 已知坑

| 坑 | 表现 | 解法 |
|---|---|---|
| 低分辨率 OCR 丢行 | 200 dpi、默认 det 尺寸时整行缺失（p14 少「for aspects of mirror symmetry…」）| 提到 300 dpi + `det_limit_side_len=1600` |
| 子智能体长时间无输出 | 单步卡住数小时（provider 侧）| 不是死锁，重发该单元即可 |
| `apply_review` 行号窗口 | 若先手工改 `chapters`，manifest 行号窗口失配 | 先 apply 再手改；或改后重跑 `make_units.py` |
| 术语替换与 quote 冲突 | 先替换术语会导致 quote 失配 | 顺序固定：apply → global_fix |
| 控制台 GBK | `UnicodeEncodeError` | `PYTHONIOENCODING=utf-8` 或写文件 |
| AMS 勘误表 | Cloudflare 拦截 curl/curl_cffi；`r.jina.ai`、Wayback 均失败 | 用搜索结果摘要中的条目，并在译注中注明「据 AMS 勘误表」 |
| 成品公开 | 在版图书译本受 COMPLIANCE L3 限制 | 成品 PDF 只留本地 `成品/`，仓库台账记「成品不公开」|

## 6. 交付物

| 文件 | 位置 | 说明 |
|---|---|---|
| 校订版 PDF | `成品/SY01-26_镜像对称与代数几何_校订版.pdf` | 403 页 → 校订后页数 |
| 校订记录.md | `工程文件/校对/` | 逐条：章、PDF 页、书页、类型、置信、原文、订正、依据 |
| 译注.md | `工程文件/校对/` | 作者未讲清处、原文笔误、术语说明 |
| 原文笔误表.md | `工程文件/校对/` | 勘误 + 存疑双表（仿 SY01-25 结构）|
| 术语对照与冲突.md | `工程文件/校对/` | 与 SY01-24/SY01-25 的对照与裁定 |
| 资料卡 MS-01…MS-24 | `资料卡/` | playbook 13 号十一节模板 |
