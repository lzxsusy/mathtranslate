# ch06 章读者报告 · Lieblich《曲线上层模空间的算术方面》

**status = partial**（六个交付文件均已按质量门写完；未完全还原的是 §5.2 局部模型的两处细节与 A.2.3(2) 的计数，详见「存疑」第 3–5 条）

## 一、做了什么（分节）

1. **材料摄取**。读 `tmp/task-ch06.md` 全文、`BRIEF.md`（§1 页表、§7 质量门、§8 文件格式）、`STATUS.md`、`source/TERMINOLOGY.md`；用 `tools/pdf_pages.py text en 104-129` 导出英文对照 `tmp/en_ch06.txt`（1435 行，含全部 26 个英文页页标），逐段读完；用 `ops_inspect_local_file` 分 6 段读完 `source/chapters/ch06.tex`（777 行）；对 13 条已有译注逐条回查英文原文与页码，未发现需要另立 `existing-note-wrong` 的条目。
2. **页码校准**。由 13 条译注的「原书页 / 中译页 + tex 行号」反解出本章恒定换算：**中译页 = 英文 PDF 页 − 10；原书页 = 英文 PDF 页 − 9**（ch06：中译 p.94–115 = 英文 PDF p.104–129 = 原书 p.95–120）。errata 三条页码均再用英文页标反查确认（p.105 / p.110 / p.118 / p.123×2 / p.121 / p.126）。
3. **对读定 errata**。自定 8 条，全部有英文原句或同句 tex 内部不一致作证据；13 条已有译注不重复登记（其中 note 8 的“建议未落到正文”改列为译注-核对批注）。
4. **写批注 18 条**，五种必需类型齐全（数学-难点 8 / 数学-补证 5 / 译注-核对 1 / 译文-问题 1 / 联系-他章 1，另加 背景-补充 1，编号 1–18 连续）。
5. **写导读**（五节齐全）、**笔记**（五节齐全，含真实的六条疑问）、**卡片候选 10 张**（8 概念 + 2 例子，anchor 逐条回查指向 tex 实际内容行）。
6. **回查**：批注编号连续、两 tsv 每行列数一致、anchor 行号逐条用 `ops_inspect_local_file` 或 `ops_grep` 验证过（见下「统计」）。

## 二、统计

| 项目 | 数量 / 数值 |
| --- | --- |
| 导读字数（不含空白与 markdown 记号） | 约 2 300 字（质量门 ≥1200） |
| 笔记字数 | 约 2 700 字（质量门 ≥1500） |
| 批注条数 | 18（质量门 ≥12），编号 1–18 连续 |
| 批注类型分布 | 数学-难点 8、数学-补证 6、译注-核对 1、译文-问题 1、联系-他章 1、背景-补充 1（共 18，必需五类各至少 1） |
| errata 条数 | 8（translation-error 2、original-error 1、typo 3、term 2；severity：medium 1、low 7） |
| errata 列数 | 10（表头与 BRIEF §8.3 一致，每行 10 个字段） |
| 卡片候选数 | 10（概念 8 + 例子 2，质量门 ≥7 且 ≥6 概念 + ≥1 例子） |
| cards 列数 | 7（每行 7 字段） |
| 回查过的 anchor | 10 条全部回查：521、527、70、648、330、426、678、673、191、463 均指向对应定义/定理/例子的正文行 |

## 三、存疑处

1. **任务书与 BRIEF 的列数冲突**。任务书写「errata 表头固定 11 列」，但随后只列出 10 个字段名；BRIEF §8.3 明确为 10 列。按“冲突以 BRIEF 为准”，本文件按 **10 列** 写。若 Lead 的汇总脚本期待 11 列（多一列 `n` 或 `page_en`），需要整表重排，请统一后再合并。
2. **§5.2 句子的原书残缺**。英文 PDF p.118「…one can ensure that C such that [C ⊗Q] ∈H2(P ⊗Q, μ2) has the form [Λ]^{1/2}…」语法不完整；中译 L423 照译，因此中文也不成句。我把它记为 `original-error / medium` 并给出建议改法；若 Lead 认为“中译忠实照译即不算错”，可降为 low 或只留在批注里。
3. **Prop 5.2.2 局部模型（L444–448）**：$\chi^0\oplus\chi^1\oplus\chi^\varepsilon\oplus\chi^{1+\varepsilon}\cong\rho^{\oplus2}$ 我算通了两项（$\varepsilon=0$ 与 $\varepsilon=1$ 的特征标集都等于 $\{0,1\}$ 二重），但“粘合局部模型”（L448 引 A.2.3(1)）的具体下降数据没有还原——批注 9 只写到“粘合是技术活”。这是本章 §5.2 我**卡住**的地方。
4. **A.2.3(2) 的 Lang–Weil 计数（L600）**：从“存在 $M$ 的截面过 $R$ 中的点 $q$”到“$q$ 的像是 $|M|$ 的元素”的不等式没有还原；批注 12 只解释了“负次幂让 $M$ 变大”这一层。
5. **Claim 1.4 的“伴随性”与 Thm 1.9 的 Giraud 引用**：两处都依赖 $\Theta$ 作为扭子的 $T$-值点翻译，我按“直觉上对”处理，未逐项验证（见笔记「疑问」1–2）。
6. **Claim 1.4 中 $\epsilon$ 的核**：Lemma 1.7 只说 $\mathrm{H}^2(S,\mu_r)\to\mathrm{H}^2(X,\mu_r)$ 单射，因而“粗空间不刻画 $\mathscr{C}$”；但 L170 说“$\epsilon$ 有非平凡核”，严格说核应是 $\mathrm{H}^0(S,\mathbf{R}^1f_*\mu_r)$ 的像与 $E_2^{1,1}$ 的交互，我在批注 3 里写得含糊（“严格说核来自 $E_2^{1,1}$ 与 $E_2^{0,2}$ 的交互”），待 Lead 复核。
7. **原书排印问题（非中译错，未入 errata）**：英文 p.114 少右括号、p.115「There result two」、p.116 多右括号，中译均已静默修好；p.113「[C⊗k̄(t)]」PDF 文字层丢横线，中译正确。这些可作为“中译优于原书”的例证，但按质量门不属于中译 errata。

## 四、给 Lead 的 TODO

1. **统一 errata 列数**（10 列 vs 11 列）后合并；并确认 `loc_tex` 的写法（我用 `chapters/ch06.tex:29` 全路径前缀，若汇总要求 `ch06.tex:29` 需批量替换）。
2. **fallback 处理 original-error 一条**：若汇总只收 translation-error/term/typo/formula/numbering，把 L423 那条降级或挪进批注 17（那里已解释同一句）。
3. **译注 8 的正文修补**：建议在 `00-修订补丁.md` 里加一条“ch06.tex:405 右端补 $\otimes\overline{k}$”，与本报告批注 16 对应。
4. **卡片 id 归并**：本章 10 个 `local_id` 均以 `ch06-` 打头；其中 `ch06-period-index`、`ch06-parabolic`、`ch06-faddeev` 可能与第 7、9 篇的概念卡重复，合并时请保留本章的 anchor 并在他章卡里交叉引用。
5. **术语**：本章出现而 `TERMINOLOGY.md` 未收的词有「剩余 gerbe（residual gerbe）」「驯顺（tame）」「热点（hot point）」「通有形变空间（versal deformation space）」「根叠（root stack）」。术语表已收 residual gerbe、tame Artin stack、hot point 三条；**root stack / 根叠** 与 **versal deformation space / 通有形变空间** 建议补入 `术语增补.tsv`。
6. **若需抬到 complete**：需要补 §5.2 粘合的一页推导（A.2.3(1) 的下降数据）与 A.2.3(2) 的计数；我判断这需要读 [19]（Lieblich, *Period and index in the Brauer group of an arithmetic surface*）而不是本章，故本轮标 partial 而不硬写。
