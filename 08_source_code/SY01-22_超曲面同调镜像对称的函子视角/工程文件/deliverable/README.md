# EN49 —— Jeffs《超曲面的同调镜像对称：函子视角》中文译注

> 文献号 **EN49**｜主题域 01_镜像对称与同调镜像对称｜类型 学位论文｜语种 英语
> 状态：**已交付**（2026-11-12 立项，2026-11-12 交付）｜施工总纲见 [`BRIEF.md`](BRIEF.md)

## 一、底本信息

| 项 | 内容 |
|---|---|
| 作者 | Maxim Jeffs（Harvard University, Department of Mathematics） |
| 导师 | Denis Auroux；第二部分为与 Benjamin Gammage 的合作工作 |
| 原题 | *A Functorial Perspective on Homological Mirror Symmetry for Hypersurfaces* |
| 类型 | PhD dissertation, Harvard University, 2023 |
| 原书页数 | 145 页（PDF 156 页，含前置页与空白页） |
| 来源 | Harvard DASH，`URN-3:HUL.INSTREPOS:37375753` |
| 直链 | https://dash.harvard.edu/bitstreams/ccffba57-5d2a-4f53-be55-252303b424e4/download |
| 本地底本 | `work\source\EN49_原文_Jeffs2023_156p.pdf`（794,892 B） |
| 中译名 | 《超曲面的同调镜像对称：函子视角》 |

**页映射：原书页 = PDF 页 − 11**（PDF 第 12 页 = 原书第 1 页）。
前置页：PDF 1 引用页 / 2 空白 / 3 标题页 / 4 版权 / 5–6 摘要 iii–iv /
7–9 目录 v–vii / 10–11 致谢 viii–ix。

源码中每页起首用注释 `% ===== 原书 p.N =====` 标记（前置页为 `% ===== FRONT MATTER =====`）。
页图 `work\pages\pNNN.png` 的编号是 **PDF 页号**（PDF 页 = 原书页 + 11）。

## 二、章节结构与块划分

| 块 | 原书页 | PDF 页 | 内容 | 状态 |
|---|---|---|---|---|
| c00 | i–ix | 1–11 | 摘要、致谢 | 已完成（2026-11-12） |
| c01 | 1–11 | 12–22 | 第 1 章 §1.1–1.3（含 1.3.1） | 已完成（2026-11-12） |
| c02 | 12–21 | 23–32 | 第 1 章 §1.4–1.5（含 1.5.1） | 已完成（2026-11-12） |
| c03 | 22–28 | 33–39 | 第 1 章 §1.6–1.7（含 1.6.1） | 已完成（2026-11-12） |
| c04 | 29–47 | 40–58 | 第 2 章 §2.1–2.3 | 已完成（2026-11-12） |
| c05 | 48–57 | 59–68 | 第 3 章 | 已完成（2026-11-12） |
| c06 | 58–64 | 69–75 | 第 4 章 §4.1 | 已完成（2026-11-12） |
| c07 | 65–75 | 76–86 | 第 4 章 §4.2 | 已完成（2026-11-12） |
| c08 | 76–86 | 87–97 | 第 5 章 §5.1–5.3 | 已完成（2026-11-12） |
| c09 | 87–97 | 98–108 | 第 6 章 §6.1–6.2 | 已完成（2026-11-12） |
| c10 | 98–111 | 109–122 | 第 7 章 §7.1–7.2 | 已完成（2026-11-12） |
| c11 | 112–127 | 123–138 | 第 8 章 §8.1–8.3 | 已完成（2026-11-12） |
| c12 | 128–134 | 139–145 | 第 9 章 §9.1 | 已完成（2026-11-12） |
| c13 | 135–145 | 146–156 | 附录 A 记号 + 参考文献 | 已完成（2026-11-12） |

全书 9 章 + 附录 A + 参考文献。原书 23 个图表（图 1.1–9.3），译文全部按原编号复现。

## 三、目录结构

```
EN49_Jeffs_超曲面HMS函子视角_中文译注\
├─ BRIEF.md                   施工总纲（Lead 独占）
├─ README.md                  本文件
├─ build.ps1                  整书编译（3 遍 xelatex → deliverable）
├─ check.py                   交付前审计（病灶句式 / 禁用写法 / 编译指标）
├─ src\
│  ├─ main.tex                汇总文件（扉页、译本说明、目录、\input 14 块）
│  ├─ preamble.tex            导言区：定理环境、共享编号、记号宏、\transnote
│  ├─ chunks\c00–c13.tex      14 个块（骨架已给标题层级）
│  ├─ figures\                从页图裁下的图
│  └─ tools\
│     ├─ compile_chunk.py     单块编译自检
│     └─ zoom.py              页图局部放大（核对公式）
├─ work\
│  ├─ source\                 底本 PDF
│  ├─ en\                     文字层全量 + 分块（BOOK PAGE 标记）
│  ├─ pages\p001–p156.png     130dpi 页图
│  ├─ zoom\                   放大截图
│  ├─ glossary.tsv            术语表草案（256 行）
│  └─ page_map.csv            页映射表
├─ reports\                   每块报告 cNN.md
├─ review\                    分章校对报告
└─ deliverable\               七件套（最终交付）
```

## 四、术语冻结状态

`work\glossary.tsv` 终版（2026-11-12 冻结）：**437 条**，全部标注「冻结」；
导出成品 `deliverable\术语表.md`（按英文排序，分 A–E / F–J / K–O / P–T / U–Z 五节）。
状态：**已冻结**。并行译期只增不改（新术语由各块记入 `work\glossary_new_cNN.tsv`，
Phase 6 由 Lead 用 `work\tools\merge_glossary.py` 合并）。
全书统一改名的术语：`gluing` 粘接 → **粘合**；`pair of pants` → **裤子（pair of pants）**；
`coherent sheaf` 凝聚层 → **相干层**；`graded` 分级 → **分次**；`counit` 馀单位 → **余单位**。

## 五、编译方式

```powershell
# 整书（三遍，结果在 work\main_build\，成品复制到 deliverable\）
powershell.exe -NoProfile -File build.ps1

# 单块自检（必须 errors=0 overfull=0 undefined=0 missing_char=0）
python src\tools\compile_chunk.py c01

# 公式放大（PDF 页号 + 300dpi + 可选 PDF 点坐标）
python src\tools\zoom.py 12 300 100 200 500 320

# 交付前审计
python check.py
```

环境：MiKTeX（xelatex），本机无 LibreOffice / Word。`build.ps1` 必须以
UTF-8 BOM 保存，否则 PowerShell 5.1 按 GBK 读会把中文路径读坏。

## 六、变更日志

| 日期 | 变更 |
|---|---|
| 2026-11-12 | **交付**：14 块译完（181 条译注）、整书 83 页、三遍编译 errors=0 overfull=0 underfull=0 undefined=0 missing_char=0、check.py VERDICT: PASS、结果编号与图表编号逐类与原书比对一致、七件套齐 |
| 2026-11-12 | 立项：建目录、复制底本、抽文字层、渲染 156 张页图、切 14 块、写 preamble/main、骨架编译通过（14 页，errors/overfull/undefined/missing_char 全 0） |
