# SY07-08 扶磊《代数几何》（第二版）中文译注本

把扶磊（Lei Fu）*Algebraic Geometry (Second Edition)*（现代数学基础 81，高等教育出版社）整本译为中文，并附带来源的译注、索引与术语对照表。

**成品**：`成品/SY07-08_代数几何_中文译注本.pdf`（209 页）
**术语表**：`成品/SY07-08_术语对照表.md`（220 条）
**交付报告**：`成品/SY07-08_交付报告.md`

## 底本

- 原书 265 个 PDF 页，纯图像扫描，无文本层（98.7 MB）。
- 页映射：**原书页 = PDF 页 − 7**（罗马页 iii = PDF 4，v = PDF 5，vii = PDF 7）。
- 正文 246 页（第 1 章 1–116，第 2 章 117–246）；Bibliography 原书 247；Index 原书 249–251。
- 译文正文与公式全部对照 200 dpi 页面图像逐句、逐符号核对；OCR 文本仅用于定位与措辞参照，**公式一律不取自 OCR**。

## 结构

```
源码/
  main.tex          # 装配：标题页 → 目录 → 译者说明 → 序言 → 第 1、2 章 → 参考文献 → 索引
  preamble.tex      # 版式、字体、数学宏、条目计数器、tnote / exercises 环境、索引
  translator_note.tex
  refs.tex
  chunks/
    c00_preface.tex c01a…c19.tex   # 21 个块，按原书页切分
  _check_cNN.tex    # 各块自检驱动（只影响自检 PDF，不影响成书编号）
工程文件/
  BRIEF.md STYLE_GUIDE.md glossary.tsv
  build.ps1         # xelatex → makeindex → xelatex ×2，产出 成品/*.pdf
  check.py          # 全文审计
  audit_numbering.py stats.py export_glossary.py normalize.py
  pages/pNNN.png    # 200 dpi 页面图像（265 页）
  work/en/pNNN.txt  # OCR 文本（仅参考）
  work/通读笔记.md  work/疑点清单.tsv  work/chunks.tsv  work/index-map.tsv
  reports/          # 逐块报告、译注核查、术语抽查、接缝审计、校勘报告
成品/
```

## 编译

```powershell
cd 工程文件
powershell -NoProfile -File .\build.ps1
```

依赖 MiKTeX（xelatex + makeindex）与 Windows 系统字体（simsun/simhei/simkai/simfang）。`build.ps1` 必须以 **UTF-8 with BOM** 保存，否则 PowerShell 5.1 会按 ANSI 读中文路径。

## 审计

```powershell
python 工程文件\check.py        # 术语残留 / 译注来源 / 黑名单 / label / 索引键 / 标点 / 引号
python 工程文件\audit_numbering.py   # 从 PDF 抽条目编号，逐节检查连续性（两处「异常」是正文交叉引用造成的误报）
```

当前状态：**0 未定义引用、0 重复 label、0 Overfull、0 缺字、审计 0 问题**；编号 210 条逐节连续（每节均从 1 起）。

## 翻译约定（摘要）

- 有通行中译则用通行中译；无通行译法或译法并存者保留英文；禁音译（Koszul、Morita 等除外）；人名一律拉丁写法。
- 条目（命题、定理、引理、推论）沿用原书**单一计数器**，编号 `章.节.序号` 自动生成，与原书一致；习题按节单独编号。
- 译注只三类：易错预警、含糊点拨、背景直觉；每条以 `[来源：…]`／`[依据：原书 p.N …]`／`[译者按…]` 收尾。
- 原书笔误：照录原书印法 + 译注说明；若照录会明显致误，正文按正确含义译出并加译注（见 `STYLE_GUIDE.md` §5.1）。
- 中文文风：短句、主谓前置、全角标点、英文与数字两侧半角空格、引号统一 `「」`。

## 版权

中文译注本仅供学习与研究，不作商业发行；原文著作权归作者与出版者所有。
