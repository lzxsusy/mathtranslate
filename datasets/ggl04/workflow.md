# 04 工作流程

## 实际顺序

1. **读任务与规范**：TASK.md、XREF.md、BRIEF 的 §9（外部校正）与 §10（训练数据）、cards/SCHEMA.md，另读了 tools/lint_cards.py、tools/verify_pages.py、audit_locators.py、term_index.py 的源码，先把四条自检的判定规则抄成清单（id 正则、summary ≤120、quote 12–120 且逐字、anchor 正则、errata 九列、notes 表格行数）。
2. **摸清交付目录**：`out/04_ggl04/` 已有 META.json、TASK.md、XREF.md、errata.tsv（仅表头）、external/（v1 PDF 与 diff 脚本）。确认只需补 notes/cards/terms/excerpts/trace/workflow。
3. **通读正文**（PDF p1–p72）：先按节做骨架表，再把每节的式号、页、结论记进笔记；§1–§2 慢读，§3 的四个表示论例子（SU(2)、离散、主、互补）逐例核对，§4 只抓构造链。
4. **版本核对**：下载 arXiv v1，抽文后与本篇 v2 做逐词 difflib，得 5 处实质差异（新增 §1.5 一段、一句引文、脚注移位、参考文献插一条、页脚数字），确认式号未变；记录放 external/ 与 notes §4。
5. **外部校正**：从库内旧卡挑可对照的 5 张（kw06 c.c. 膜、ggl19 distinguished c.c. 膜、csw 半形式、mloc Harish-Chandra、sy38 sl2 Casimir），加 nLab 的几何量子化词条；逐条比对符号与系数，写进 notes 的外部来源表。nLab 的 coisotropic brane 页 404，弃用。
6. **定 errata**：三条。E1（p.65 isotropic→coisotropic，high，两条独立旧卡支撑）；E2（(3.44) 乘→除，medium，本篇内部两式联立 + $S^1$ 模型自算）；E3（p.51 引 (3.11)，low，保留原文）。另把 (3.28) 的括号问题排除在外（渲染核对）。
7. **写卡**：先用 Python 脚本批量落盘（概念 8 张、推导 3 张），再做逐项核验。卡 id 与文件名一致，related 只指向本包已存在 id。
8. **补交付件**：notes.md（骨架/主定理清单/接口/版本差异/核对与勘误/不懂）、terms.tsv（38 行）、excerpts.md（4 段，178–235 汉字）、trace.md（15 条）、workflow.md。
9. **四件自检**：lint_cards（0 error）→ verify_pages（0 问题）→ term_index check（撞名逐条处理）→ audit_locators（OK）。status 由 draft 改 dev 后再各跑一遍。

## 每步产出

| 步骤 | 产出 |
| --- | --- |
| 规范 | 自检规则清单（写在 trace 的判断依据里） |
| 通读 | 骨架表 + 式号/页索引（进 notes §1–§2） |
| 版本 | external/0809.0305v1.pdf、v1 抽文、v1v2_diff.txt、diff 脚本 |
| 外校 | notes §5 的 6 条外部来源表 |
| 勘误 | errata.tsv 3 行（E1/E2/E3） |
| 写卡 | cards/concepts/8 张、cards/derivations/3 张 |
| 交付 | notes.md、terms.tsv、excerpts.md、trace.md、workflow.md |

## 最耗时 / 最易错

- **最耗时**：§3 的四个表示论例子。每例都要把「曲线 $\ell$ 的端点 → $J_z$ 谱 → 是否酉 → 与旧卡的 Casimir 对上」串一遍，任一环松了就写不出可核对的 locator。其次是 v1/v2 的逐词 diff（先抽 v1 文本、按页对齐，再切词）。
- **最易错**：
  1. 公式抽取失真。(3.28) 的分数线、(3.42) 的除法、(3.44) 的乘除，光看 txt 会全判错；凡是要写进卡片的式子，最终都得回 PDF 渲染图确认。
  2. 页码基准。印刷页比 PDF 页小 1，混用会让 anchor 与 locator 全体错位；本包统一 PDF 页序，并在 journal 里记了换算。
  3. quote 必须逐字。少一个 $\psi_s$ 或把连字 `ﬁ` 写成 `fi` 之外的写法都会让 verify_pages 失败；我是先按抽文抄、失败后回原文 grep 上下文修的。
  4. 结构字段。推导卡的 `type` 是 `derivation` 而不是 id 里的 `deriv`；summary 限 120 且会剥掉 `$…$`；notes 的「核对与勘误」节必须在 `### 勘误` 之前有 ≥4 行表格（表头 + ≥3 条外部来源），否则包级 lint 直接拦。

## 重做会怎么改

1. 一开始就把「公式一律回 PDF 渲染核对」写成硬流程，而不是等抽文起疑再补；这能省掉两轮 errata 反复。
2. 先批量生成卡骨架（只含 id/type/title/related/status），跑一次 lint 把结构错误清空，再填内容；这次是内容写完才发现 `type` 字段错，改了三张卡。
3. quote 不要手打，直接从 txt 里用正则截取（带词边界、限 12–120 字符），可一次过 verify_pages。
4. 版本 diff 直接做逐词对齐，不要先看页数与字节数下判断。
5. 外部校正的候选旧卡应在通读前就列好（这次是读到 §4 才去找 csw 的半形式卡），提前列可以边读边核，减少回读。
