# 实际工作流（第 12 篇）

## 1. 顺序与每步产出

1. **读规矩**：读 TASK.md、XREF.md、BRIEF §9/§10、cards/SCHEMA.md，并核对交付目录已有文件（META.json、errata 表头、external/xref.json）。产出：一张必交清单 + lint/verify 的硬判定规则（记在 trace 第 1、6 条）。
2. **定主线**：先读 PDF 目录页（p2–p5）与 §1（p6–p17），再读摘要；随后按节标题扫 §2–§6。产出：notes 骨架表（28 行，节 → 一句话 → 页码）与主定理清单（10 条）。
3. **公式核对**：对准备进卡片的公式做三件事——(a) 回 PDF 看排版（用 PyMuPDF 裁 500–600dpi 图，存 external/）；(b) 找第二出处（KW06 文本、nLab、1108.3103）；(c) 内部自洽复算（(2.28)↔(2.49)↔(3.5)↔(2.41)；(2.14) 与 p20 脚注 4；G2 的 (3.45)；p1 归一与 (5.53)）。产出：notes §4 的五项动作清单表 + E1 一条 errata。
4. **抽引文**：用 norm 脚本（小写、只留 a–z0–9、ligature 展开）把候选英文句与 150 页逐一匹配，先验后写。产出：36 条可回查的 A 源 quote（每张卡 1–2 条）。
5. **写卡（分批）**：第一批 4 张概念卡（CS、Khovanov、D3-NS5、twisting），跑一次 lint；第二批 9 张概念卡（Ψ、Nahm、framing、't Hooft、5d 迹、q-分次、非单连通、6d、Morse）；第三批 5 张推导卡。每批写完立刻 lint + verify_pages。产出：concepts 13、derivations 5。
6. **术语查重**：`term_index.py check` 两轮（khovanov、nahm 各一处撞名），改 title/alias 后再查。产出：0 撞名；旧卡 id 记入 notes §3.1。
7. **精译**：从 p13、p14 选 4 段（研究目标、基本想法、T-对偶失败、S-对偶修复），逐段对照原文译，控制每段 150–400 字。产出：excerpts.md。
8. **收尾**：trace.md（12 条，含 4 条真实弯路）、workflow.md（本文），最后三检 + status draft→dev。

## 2. 最耗时的一步

**逐页扫读 + 抽引文**占了一半以上时间。150 页里真正进卡片的内容集中在 §1–§5，但可引的英文句必须与 txt 的抽取结果逐字对上（PDF 的 ﬁ/ﬂ 连字、U+2212 减号、上划线都会让"看起来一样"的句子匹配失败），所以每条 quote 都先跑 norm 脚本、命中后才写进 JSON。36 条引文里约有 6 条第一次不命中，靠改选相邻句子解决，而不是改 quote 去迁就抽取结果。

## 3. 最易错的地方

1. **txt 抽取丢符号**：(2.28) 的 τ 上横杠、p20 的 \overline{NS5} 上划线在 txt 里都没有。凡公式含分式/上划线，一律回 PDF 裁图确认，再决定是不是笔误（trace 第 2 条）。
2. **页码口径**：页脚印 N−1，若误用印刷页，verify_pages 会整体报错，且错得很隐蔽（差一位仍可能碰巧命中相邻页）。所以 cards 的 sources.pages 与 anchor 全部用 PDF 页序。
3. **term_index 查两处**：title 与 aliases 都查。第一轮只改中文题名，第二轮又被英文 alias 撞上（trace 第 8 条）。
4. **卡片的 related 只能指包内**：一开始想把旧卡 id 写进 related，lint 会判不存在；改为写进 notes §3.1。
5. **proof.status 别拔高**：作者的"conjecturally"、"not clear"、"straightforward exercise"必须如实落到 gap/sketch，否则卡片会替作者宣称未证之事。

## 4. 重做怎么改

- **单卡公式错**：先回 PDF 裁图确认原文 → 改 JSON 的 formula/step → 只对该卡跑 `lint_cards.py`（它会顺带 verify 吗？不会，需单跑 verify_pages 的机制是整包；故改完仍整包跑一次，代价可接受）→ 若原公式有误且构成笔误，补 errata 行并在卡片 corrections 里引用 E 号。
- **引文不命中**：不要改 quote 的字母去凑 norm，而是回 txt 找同页相邻的完整句；若整页无可引句，改用另一页的 A 源，或降为 C 源并在 section 写清出处。
- **撞名**：先判断是不是同一概念。同概念 → 不造新卡，related 指不过去就记 notes；不同概念 → 改 title 与 alias 两处，直到 check 为 0。
- **卡数超限**：优先合并"同一公式的不同侧面"（例如把 5d 迹与 Khovanov 定义合并），不要删掉唯一承载某主定理的卡。
- **最后一遍**：`lint_cards.py out/12_ggl12 --max-pages 150 --strict` → `verify_pages.py out/12_ggl12 --strict` → `term_index.py check out/12_ggl12/cards`，三者全 0 才把 status 从 draft 改 dev；改完 dev 再跑一次 lint 确认（lint 不因 dev 改变判定，但保持交付物与检查同步）。
