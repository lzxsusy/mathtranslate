# 04 术语 · 文献 · 勘误

本卡服务于三类读者：查术语的译者、核引用的审稿人、追踪原文缺陷的读者。每一条都给出可回查的位置（`pNN` 为印刷页，等于 `工程文件/work/pages/pNNN.png` 的编号）。

核验口径分三档：

- **OK**：外部标识（DOI / arXiv 号 / 刊名卷期页）已在 Crossref 或 arXiv API 命中，且题名、作者、年份与原文一致；或该事实已在本篇一手 PDF 上逐页核对。
- **DIFF**：外部记录与原文有出入（年份、出处、卷期），差异写在备注里，正文按原文照录。
- **无法核验**：外部数据库无对应记录，或记录无法唯一对应；不作任何推测性补全。

## 一、勘误与待裁定

| # | 位置 | 类型 | 现状 | 处理 | 依据 |
|---|---|---|---|---|---|
| 1 | p37（§7） | 原文笔误 | 原文写 "the kernels … applied to $\Delta_{!}\overline{\mathbb Q}_{\ell}$ on $\mathrm{Bun}_{G\times G}$"，按上下文应为 $\mathrm{Bun}_{G}\times\mathrm{Bun}_{G}$ | 译文照录并加【译注·原文笔误】，未改数学内容 | 同一页自对偶数据写作 $D(\mathrm{Bun}_G)\otimes_{K_D}D(\mathrm{Bun}_G)=D(\mathrm{Bun}_G\times\mathrm{Bun}_G)$；图 p037 复核 |
| 2 | p38（§8） | 原文笔误 | 循环 Bar 复形末项重复 $ma\otimes b$，按复形结构应为 $mb\otimes a$ | 译文照录并加【译注·原文笔误】 | 复形各项为 $A^{\otimes n}$ 的循环置换，相邻项相差一次转置；图 p038 复核 |
| 3 | p28（§5 推论 5.3） | 体例 | 原文定理名中含 "Main Theorem 14.3.2" 的定位，译文把定位移入正文括注 | 保留，标**待裁定**：若要求定理名严格逐字，可改回 | 原文标题行 "Corollary 5.3 (…) Main Theorem 14.3.2" 与译文 `s05-spectral.tex` 对应行 |
| 4 | p53（文献表） | DIFF | 原文标 Beraldo–Kazhdan–Schlank (2022)，arXiv:1801.00655 初版为 2018 | 按原文年份 2022 照录，备注标 DIFF | arXiv API 记录：1801.00655v2，2018 初版 |
| 5 | p53（文献表） | DIFF / 无法核验 | 原文标 Fargues (2025) *J. Math. Sci. Univ. Tokyo* 32(2) 157–240；Crossref 只命中同题异文 "…, motivically"（Crelle 2026） | 出处按原文照录，标 DIFF；外部定位写「无法核验」 | Crossref 检索结果与原文出处不一致 |
| 6 | p53（文献表） | 无法核验 | Lafforgue–Zhu, arXiv:1811.07976 | 题名实存，仅 arXiv API 返回 UTF-8 乱码导致自动比对失败 | arXiv API 原始返回 `D��composition…`；人工判为编码问题，非文献不存在 |

除上述六条外，13 个 tex 与 56 条文献在本次校对中未发现数学错误或引用错误；逐节结论见 `工程文件/reports/校对-v2.md`。

## 二、术语表

下表 24 条为全文反复出现、且中文译法容易分叉的术语。译文实际统一用法以 `工程文件/work/glossary.tsv`（123 条）为准，本表只列高风险项。

