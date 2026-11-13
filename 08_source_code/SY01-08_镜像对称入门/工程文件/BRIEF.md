# JPB07『ミラー対称性入門』中文译注本 · 作战计划（BRIEF）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；本项目语料默认不用于训练，要用须先整库审计并经 Lead 书面批准。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

体例看 `STYLE_GUIDE.md`（必读，先读完再动手）。本文件只讲分工、进度与协作。

## 目标

把『ミラー対称性入門』（日本評論社，PDF 176 页、正文 162 页、12 章、九位作者）完整译成中文译注本，
交付：PDF + LaTeX 源码 + 译注汇总 + README + 阅读参考指南 + 工程总结 + 术语表。

## 工程根目录

```
<本地路径>
  src\chunks\      ← 译者写 chNN.tex
  src\figures\     ← 译者裁图 chNN-figM.png
  src\frontmatter\ ← Lead
  work\pages\      ← 页图 p001.png…p176.png
  work\split\      ← 逐页 OCR 文本 p001.txt…
  work\            ← glossary.tsv、full.txt、tools\
  reports\         ← 译者写 chNN.md
  deliverable\     ← 最终成品
```

## 成员与专属编译镜像（**必须用自己的，混用会互相覆盖**）

| 成员 | 负责 | 专属 -Root |
|---|---|---|
| Lead | ch01 + 前言/目次/书末/索引/汇编 | `…\default-workspace\mirror_JPB07_lead` |
| tr1 | ch02 → ch08 | `…\default-workspace\mirror_JPB07_tr1` |
| tr2 | ch03 → ch09 | `…\default-workspace\mirror_JPB07_tr2` |
| tr3 | ch04 → ch10 | `…\default-workspace\mirror_JPB07_tr3` |
| tr4 | ch05 → ch11 | `…\default-workspace\mirror_JPB07_tr4` |
| tr5 | ch06 → ch12 | `…\default-workspace\mirror_JPB07_tr5` |
| tr6 | ch07 →（补位/校对支援） | `…\default-workspace\mirror_JPB07_tr6` |
| qc | 术语 + 全书校对 + 术语表 | `…\default-workspace\mirror_JPB07_qc` |

（`…\default-workspace` = `<本地路径>`）

## 第一波（现在开工）

| 成员 | 任务 | PDF 页 | 原书页 | 页数 |
|---|---|---|---|---|
| Lead | ch01 江口徹《什么是镜像对称》+ 前置页 | 10–25 | 2–17 | 16 |
| tr1 | ch02 深谷賢治《Gromov–Witten 不变量入门》 | 26–40 | 18–32 | 15 |
| tr2 | ch03 高橋篤史《正多面体与镜像对称》 | 41–53 | 33–45 | 13 |
| tr3 | ch04 並河良典《Calabi–Yau 流形与代数几何》 | 54–67 | 46–59 | 14 |
| tr4 | ch05 高橋篤史《奇点与拓扑场论》 | 68–78 | 60–70 | 11 |
| tr5 | ch06 細野忍《镜像对称与共形场论》 | 79–91 | 71–83 | 13 |
| tr6 | ch07 今野宏《环簇几何与 Calabi–Yau 流形》 | 92–102 | 84–94 | 11 |
| qc | 术语表校对 + 全书术语扫描 + 术语附录草稿 | — | — | — |

## 第二波（做完第一波立刻接，Lead 用 send_message 正式派单）

| 成员 | 任务 | PDF 页 | 页数 |
|---|---|---|---|
| tr1 | ch08 深谷賢治《Floer 同调与镜像对称》 | 103–116 | 14 |
| tr2 | ch09 Guest・乙藤《镜像对称与 D-模》 | 117–128 | 12 |
| tr3 | ch10 深谷賢治《镜像对称与同调代数》 | 129–144 | 16 |
| tr4 | ch11 高橋篤史《奇点与镜像对称》 | 145–156 | 12 |
| tr5 | ch12 中島啓《超越镜像对称》 | 157–171 | 15 |
| tr6 | 支援：ch10 后半 / 图版测绘 / 校对 | — | — |
| qc | 第一波稿件校对（逐章出 `reports/qc_chNN.md`） | — | — |

## 章题（中文，Lead 已定，`\chapter{}` 照抄，不要改）

1. 什么是镜像对称（副题：Calabi–Yau 流形与超弦理论）
2. Gromov–Witten 不变量入门
3. 正多面体与镜像对称
4. Calabi–Yau 流形与代数几何
5. 奇点与拓扑场论
6. 镜像对称与共形场论
7. 环簇几何与 Calabi–Yau 流形
8. Floer 同调与镜像对称
9. 镜像对称与 D-模
10. 镜像对称与同调代数
11. 奇点与镜像对称
12. 超越镜像对称

## 质量标准（交付闸门，逐条可查）

1. **G1 覆盖**：本章 PDF 页段逐页翻完，页标记连续无缺（`% ===== PDF p.NNN (原书 p.N) =====`）。
2. **G2 术语**：`work\glossary.tsv` 全部照用；新术语进 `reports/chNN.md`「术语提议」。
3. **G3 公式**：每个公式回页图逐符号核对；编号照抄；正文引用（n）对得上。
4. **G4 语言**：无「被…所…」「进行…的」「对于…而言」；句长 ≤70 字；全角标点；中英间半角空格。
5. **G5 编译**：`build.ps1 -Chunk chNN -Root <你的镜像>` 输出 `BUILD OK`（六项全 0）。
6. **G6 批注**：Tutor Note 3–8 条/章，格式 `% [Tutor Note: …]`。
7. **G7 图**：本章所有图/表都已裁出、复核、插入，题注带原书页码。

## 工作节奏（重要）

- **小步落盘**：一次 turn 推进 4–6 页就写入文件，不要一口气憋 13 页再写（上下文/超时会丢稿）。
- 到 turn 末尾必须停在**页边界**，文件末尾留 `% CONTINUE: 下一页 PDF p.NNN，从「…」继续。`
- 一章全部完成（G1–G7 自查过、编译 BUILD OK）才发回执。
- 回执发 Lead，模板见 STYLE_GUIDE.md §8。**没收到回执等于没完成。**
- 遇到以下情况立刻停下问 Lead（不要自己拍板）：原书整段印刷不清 / 公式无法辨认 / 疑似严重笔误且影响结论 /
  术语表与实际用语冲突 / 需要改别人的文件。

## 协作禁区

- 不改 `preamble.tex`、`main.tex`、`glossary.tsv`、`build.ps1`、`check.py`、别人的 chunk。
- 不新建 `\usepackage`、不写 `\label`/`\ref`/`\cite`。
- 不把 OCR 文本当原文；不音译术语；不擅自"修正"原书。
- 一个章只有一个 `chNN.tex`；不要把一章拆成多个文件（main.tex 只认 chNN）。

## 参考：素材与工具速查

```powershell
# 看页图
read_image  work\pages\p041.png
# 叠网格（估裁图坐标）
python work\tools\grid.py 45            # → work\grid\p045_grid.png
# 裁图（x0 y0 x1 y1 为 0–1 比例）
python work\tools\crop.py 45 0.10 0.05 0.90 0.55 ch03-fig1 400
# 局部放大核对公式
python work\tools\crop.py 45 0.12 0.60 0.88 0.75 tmp_zoom 500
# 编译本章
powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch03 -Root <本地路径>
```
