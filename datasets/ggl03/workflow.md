# 工作流（workflow）

## 实际顺序与产出

1. **读规范与任务书**（out/03_ggl03/TASK.md、XREF.md、BRIEF.md §2/§3/§9/§10、cards/SCHEMA.md、tools 三个脚本源码）。
   产出：一份内部规则清单（字段、正则、页数上限、严格模式的包级检查点），后续所有写作按它对齐。
2. **通读原文 90 页**（txt/03/p001–p090，PyMuPDF 渲染辅助）。先读摘要、目录、引言、§2.2 与 §4–§7 的主线，再补附录 A/B 与 §8 的弦论构造。
   产出：notes.md 的骨架（§1–§8 + 附录逐节一句话）与主定理清单 17 条（编号 + PDF 页 + 一句话）。
3. **外部校正**：web_fetch arXiv abs/0804.1561 与 INSPIRE recid 783139；核 KW06 原文 PDF p.6、p.30、p.75–76 的对应公式；nLab 两个页面与 Witten 0710.0631 作语境旁证；对 (3.16) 用 PyMuPDF 300 dpi 渲染 p039 存 external/p039_render.png 肉眼核对矩阵。
   产出：notes.md「## 核对与勘误」下 7 行外部来源表 + 五项清单逐条结论；errata 2 条（E1 medium、E2 low/open）。
4. **库内接口**：读 datasets/kw06 的卡目录与 ggl12 的 canonical-parameter 卡作格式样板；用 kw06 的 (2.1)/(2.2) 与 §2.6 的参数映射给 B 源锚点。
   产出：概念卡 half-bps-surface-operator-parameters 的 B 源两行、notes 的接口一节。
5. **建卡**：先写 10 张概念卡（刚性定义、半 BPS 参数、单幂零算子、强刚性幂零、强刚性半单、sigma model 实现、对偶群刚性算子、指纹、极多项式、中心/拓扑），再写 4 张推导卡（刚性极限、指纹、形变判据、量子化中心特征）。
   产出：cards/concepts 10 个 JSON、cards/derivations 4 个 JSON；每张卡写完后单独跑一次 JSON 解析。
6. **术语与精译**：terms.tsv 29 行（英文、中文定名、首见 PDF 页、备注）；excerpts.md 4 段，段前 [p.N]，每段 150–400 汉字。
   产出：terms.tsv、excerpts.md。
7. **勘误与决策记录**：errata.tsv 两行（9 列）；trace.md 12 条四栏决策，其中弯路两条（式号正则扫描失败、E2 先判单处笔误后改判约定差异）；双源核对后把 (3.16) 定为 medium、(7.7) 组定为 low。
   产出：errata.tsv、trace.md、本文件。
8. **四道检查与修复**：
   - `tools/lint_cards.py out/03_ggl03 --max-pages 90 --strict` → 14 张卡（概念 10 / 推导 4），0 错误。
   - `tools/verify_pages.py out/03_ggl03 --strict` → 首轮 7 条问题（2 条页码不符、5 条 quote 搜不到），逐条换成本页逐字句后 0 问题（48 条）。
   - `tools/term_index.py check out/03_ggl03/cards` → 0 处撞名。
   - `audit_locators.py out/03_ggl03 3 90` → 因脚本内部拼 `txt/3`（实际目录 `txt/03`）而 54 条全 mismatch；改用 `03` 实跑，得 3 条真错（(4.14) 标 p.46 实为 p.48；(2.29)、(2.30) 标 p.20 实为 p.21），改正后 OK。

## 最耗时 / 最易错

- **最耗时**：通读 90 页并逐条把定理与公式落到页码（约一半工作量）；其次是每张卡的 quote 逐字核对——OCR 有连字与控制字符，肉眼看似相同的句子在 txt 里常差一个连字符。
- **最易错**：
  1. 页码：PDF 页 = 印刷页 + 1（p003 页脚 2、p045 页脚 44、p071 页脚 70 均验证）。sources.pages 与 anchor 的 p.N 必须同为 PDF 页，否则 verify 报「页码不符」、audit 报 eq 不在页内。
  2. locator 的式号必须真在所标页：式号常印在页首或页尾，跨页时容易标错（(2.29)/(2.30) 实际在 p021，(4.14)/(4.15) 在 p048）。
  3. quote 必须能在该页 txt 中逐字搜到：希腊字母、上下标、连字（ﬁ/ﬂ）都会被归一化，稳妥做法是选纯 ASCII 的短句。
  4. errata.tsv 必须 9 个 tab 字段；high 必须填依据2；影响卡片列出的 id 必须真实存在。
  5. 卡片 corrections[].id 必须出现在 errata.tsv，否则 lint 直接报错（dual-group 卡最初漏了该字段，补 E1 后通过）。

## 如果要重做

1. **先定页码与 quote 池**：通读时同步记录每页 2–3 条纯 ASCII 候选句，写卡时直接从池里取，可省掉 verify 的首轮返工。
2. **先跑 lint 骨架再填内容**：每类卡先写最小可过 lint 的 JSON，再补 key_points/formulas/theorems，能避免字段遗漏（尤其 corrections、gaps、theorem proof）。
3. **locator 用「页内式号」而不是「节内式号」**：写完立即用 audit_locators（参数传目录名 03）跑一遍，把式号与页绑定后再写下一张。
4. **E2 这类符号问题先复算再定级**：按 (2.8) 把对偶单值性算出来，再决定是笔误还是约定差异；只有一处冲突就记 low，不为了「看起来干净」升 high。
5. **检查顺序**：lint → verify → term_index → audit；lint 管结构、verify 管页码与 quote、audit 管 locator，三者失败信息互不重叠，按此顺序返工最少。
