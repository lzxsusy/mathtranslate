# 寺杣友秀《コンツェビッチによるウィッテン予想の解決》中文译注本

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：全库统一 CC BY 4.0，明确欢迎用于训练、蒸馏与商用（署名即可）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

上智大学数学講究録 No.40（Sophia Kokyuroku in Mathematics 40，1997 年 4 月）
—— *Witten's Intersection Theory of Moduli Spaces of Curves (After Kontsevich)*

## 产物

| 文件 | 说明 |
| --- | --- |
| `deliverable/寺杣友秀_KontsevichによるWitten予想の解決_中文译注本.pdf` | 成品（A4，正文 66 页） |
| `deliverable/交付说明.md` | 交付说明：底本、体例、译注统计、质量核对 |
| `deliverable/审校批注汇总.md` | 全部【译者注】按块汇总，附页范围 |
| `deliverable/README.md` | 本文件 |
| `deliverable/compile.log`、`deliverable/build_summary.txt` | 编译日志与四诊断计数 |
| `deliverable/src/` | LaTeX 源（`main.tex`、`preamble.tex`、`chunks/c00–c12.tex`、`figures/`） |
| `deliverable/build.ps1` | 一键构建（纯 ASCII 脚本） |
| `deliverable/check.py`、`deliverable/verify_pdf.py` | 源检查与 PDF 回读检查 |

## 编译

```
xelatex main.tex   # 两遍
```

引擎为 XeLaTeX + ctex（TeX Live 2026 / MiKTeX 均可）。整书构建请用 `build.ps1`
（内部连跑两遍并把成品改名、统计四诊断），或手工在 `src/` 下执行两遍 xelatex。

## 目录结构（工作区）

```
WP_工作区/
├── BRIEF.md                 译者手册（块边界、硬规矩、报告模板）
├── STYLE_GUIDE.md           中文文风细则
├── build.ps1  check.py  verify_pdf.py  collect_notes.py
├── src/
│   ├── main.tex             汇总（Lead 独占）
│   ├── preamble.tex         导言区（环境、宏、页眉）
│   ├── chunks/c00–c12.tex   13 个译块
│   ├── figures/             39 张图（原书 600 dpi 重裁，全部落版）
│   └── tools/compile_chunk.py  单块编译与编号自检
├── reports/                 每块完成报告 + 交叉校对报告
├── work/pages/pNNN.png      原书 95 页 150 dpi 页图（真值）
├── work/probe/text/         OCR 文字层（仅作检索提示）
├── work/zoom/               局部放大裁片
└── deliverable/             交付件
```

## 体例速查

- 页映射：**原书页码 = 底本 PDF 页码 − 6**（原书 89 页，扫描 PDF 95 页）。
- 页注 `% ===== 原书 p.N =====` 标出原书页界；节号、小节号、定理类环境编号一律照原书。
- 原书 §1 有 **Theorem 1.8 / Proposition 1.8 重号**，译本照排并加译注。
- 原书**没有编号公式**，译本也不给公式编号；少数式子保留原书 `(*)、(S_d)、(S)` 标记并排在式子左端。
- 译注写作 `\transnote{...}`（命令，非环境），排版为褐色独立段。
- 文献引用沿用原书方括号缩写（`[DM]`、`[K]` 等），参考文献表照原文抄录不翻译。

## 质量核对

`build.ps1` → `check.py` → `verify_pdf.py` 三道闸门：编译四诊断（errors / overfull /
undefined / missing char）全 0；47 个编号环境序列与原书逐一对应；22 个小节齐全；
39 张图全部落版；66 条译注；译注外无残留假名；参考文献 6 条。
