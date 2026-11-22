# 本篇工作流（第 10 篇 · Witten 1001.2933）

## 顺序与产出

| 步 | 做了什么 | 产出 |
|---|---|---|
| 1 | 读 TASK.md、XREF.md、BRIEF §9–§10、cards/SCHEMA.md，对照 out/17_ggl17 的 notes/trace/workflow/卡/terms/errata | 明确 11±2 卡、4±1 推导、quote 12–120、包级核对节等硬约束 |
| 2 | 先读摘要 + 目录 + §1 + §6，定「文章解决什么、结论是什么」 | notes §1 一句话、§2 骨架的粗表 |
| 3 | 通读 p008–p127（§2–§6）；只对主线公式停下來推导，枝节（Bessel 原型、指标细节）只记骨架 | 全文结构、公式页表、S1–S17 的素材 |
| 4 | 用脚本把每个 (n.m) 在 txt/10 里检索，建立「公式 → PDF 页」表 | 卡片 pages/anchor 的唯一依据（见 trace 第 2 条弯路） |
| 5 | 外部校正：arXiv abs、INSPIRE API、arXiv v1 PDF；下载 Murakami 0802.0039、Hikami–Murakami 0711.2836；抓 nLab 两页 | notes「核对与勘误」的外部来源表 8 行；errata E1/E2 |
| 6 | 选卡：11 概念 + 4 推导；为每张卡选 2–4 条 A 类 quote 与 1 条 C 类外部对照 | cards/concepts/*.json、cards/derivations/*.json |
| 7 | 写 notes（骨架表、主命题、接口、核对与勘误、不懂） | notes.md |
| 8 | 写 terms.tsv（30 条）、excerpts.md（4 段精译，181–303 汉字） | terms.tsv、excerpts.md |
| 9 | 跑 lint/verify/term_index；按报错改 pages/anchor/别名 | 三项 0 问题 |
| 10 | 写 trace.md（14 条，4 条弯路）、workflow.md | 本文件与 trace.md |

## 最耗时的一步

通读 127 页 + 建立「公式 → 页」表。Witten 的论证大量依赖前文公式（(2.1)(2.4)(2.28)(2.34)(2.35)(4.8)(4.11)(4.42)(5.7)(5.8)(5.25)–(5.30)(5.42)(5.50)–(5.68)），每张卡都要回查 3–5 处；真正写字的时间反而少。第二耗时的是外部校正：Murakami 与 Hikami–Murakami 的公式要换算 m 的平方约定（本文 m = [17] 的 m^{1/2}）才能逐项对上。

## 最易错的地方

1. **公式页 ≠ 提到该式的页**。`verify_pages` 只查 quote 是否落在 `pages` 区间，不查 `anchor` 的 (n.m) 是否真在该页；我第一版有 5 条 quote 页错、3 条 anchor 与页不一致，都是靠脚本回查才发现的。
2. **γ 的方向**。p118 的「γ = k/n」与全篇的 γ=n/k 相反；如果照字面建卡，整条体积猜想的指数会写成 kV/2π 而不是 nV/2π。E1 是这篇最值得记的坑。
3. **meridian/longitude 的中译**。两者都容易写成「经线」；一旦混用，A 多项式卡的 l、m 就对不上。最后固定为子午线（meridian）/经线（longitude）。
4. **quote 的逐字性**。PDF 抽取有连字（ﬂ、ﬁ）与断词，`verify_pages` 会做 ligature 映射与去标点；但多一个字母、少一个字母都会搜不到。最好直接从 txt 里截连续片段，不要凭记忆写。
5. **C 类来源的 `quote`**。lint 只查 A 类，但任务要求每条 sources 都带 quote；给 C 类写外部英文原句时，必须确认是从该外部源逐字抄的，不能拿本篇的句子冒充。

## 如果重做，会怎么改

- 先写一个「公式 → 页」的 JSON 表，再写卡；不要边读边记页。这样能省掉第一轮 verify 的 5 处返工。
- 读 §5 之前先把 §2–§4 的公式表建好；§5 的每一步都在回引 (4.42)(3.57)(3.58)，没有表就只能反复翻页。
- 外部源先下载、先 grep 关键式，再决定哪些公式进卡；本篇是先写卡后补外部源，导致 C 类来源的 quote 返工一次。
- 术语表在写第一张卡之前定稿（尤其是 meridian/longitude、thimble、Stokes），不要写完再全局替换。

## 与其他篇的差异

- 本篇是 127 页的单篇长文，没有编号定理、没有合著者，公式密度高、修版多（v1→v4，comment 明说 many minor corrections）；out/17_ggl17 是 164 页但有编号引理与已译姊妹篇可对照，本篇只能靠外部文献与自算。
- 本篇的主线是「解析延拓 + 两个纽结例子」，所以推导卡集中在三叶结与八字结；§3 的 Bessel 原型虽长（p056–p062），但只是技术预演，没有单独建卡。
- 外部校正的难度高于库内互引：库内能直接对上本篇公式的只有 csw 的 CS 作用量卡与 ggl13 的复 CS 流方程卡；三叶结/八字结的公式必须去 Murakami 与 Hikami–Murakami 的原文换算约定。
