# 实际工作流（workflow）

本篇（arXiv:1401.6996，26 页）首轮卡片化的实际执行顺序，按时间排列；括号内是每步的产出。

## 0. 读任务与规范

1. 读 `out/14_ggl14/TASK.md`、`XREF.md`、`META.json`；读 `BRIEF.md` 的 §2/§3/§9/§10（交付物定义、纪律、勘误置信度规则）。
2. 读 `cards/SCHEMA.md` 全文，确认概念卡/推导卡的必填字段、`proof.status` 与 `provenance` 的取值、`sources.quote` 的长度约束。
3. 读 `tools/lint_cards.py`、`tools/verify_pages.py`、`tools/term_index.py` 的源码与 `audit_locators.py`，把它们实际检查的东西抄成清单（比读文档可靠）。

## 1. 读原文

4. 按 `txt/14/p001–p026.txt` 顺序通读，边读边记：节标题与起止页、每个编号公式的页位、每处「作者自称的缺口」。产出是 notes §1 的骨架表与 §2 的主定理清单草稿。
5. 同时读同作者的 `datasets/ggl12`（Fivebranes and Knots，13 概念 + 5 推导）作为体例样板：notes 的分节、卡片的字段顺序、errata 的写法。

## 2. 渲染 PDF 核对（本篇的关键步骤）

6. 用 PyMuPDF（fitz）把 p002/p003/p004/p013/p014/p016/p019/p020 的目标区域渲染成 300 dpi PNG，逐张读图判读：
   - p2 脚注 1 的 `q^{3/4}`；
   - p3 fig.2 的十二格权重与 (1.1) 的系数 2/3；
   - p4 的 (1.4)(1.5) 与脚注 4 的分母写法；
   - p13 的对偶句 `τ∨ replaced by τ = −1/(n_g τ∨)`；
   - p14 的 `G = Sp(2n+1)` 与 `Stieffel-Whitney`；
   - p19 的 π₄(G) 表（确认**无编号**）；
   - p16 的 (2.4)(2.5) 与 Q 的三条性质；
   - p20 的 (2.12)(2.13)。
   理由：txt 抽取会压平公式（`2^7`→`27`、(1.5) 的分式丢失、τ 句乱序），而 `sources.quote` 要逐字回查，必须以 PDF 排版为准。

## 3. 外部校正

7. `web_fetch` arXiv abs 页与 INSPIRE API（recid 1278911）：核标题、页数、版本、摘要、参考文献条数与图注。
8. `web_fetch` nLab 的 "Khovanov homology" 与 "Chern-Simons theory"：核 5d 指标解释与 CS 作用量的独立表述。
9. 查库内 `datasets/ggl12`、`ggl13`、`ggl10`、`gtgl15`、`kw06`、`ggl22` 的 `index.jsonl`，抄下真实卡 id 备用（不凭印象编 id）。
10. 五项动作清单（主定理、公式系数、编号、数值一致性、记号一致性）逐项过一遍，结果写进 notes §4.1；外部来源写成 §4 的第二张表。

## 4. 定 errata

11. 先列出所有「可疑点」，再用两条腿判定：本篇内部是否自洽、是否有独立出处。结论：
    - E1（p14 `Sp(2n+1)`）high：本篇 p19 与 ggl12 对偶表两处独立出处，且 p14 自身与 p19 冲突 → 改卡 + 记账；
    - E2（p4 脚注 4 缺括号）medium：同页 (1.5) 特例可判读，ggl12 (3.13) 同读法；
    - E3（`Stieffel`）low：纯拼写，wontfix；
    - p13 的 τ 句**不是**笔误（等价改写），只记入 notes 的记号陷阱。

## 5. 建卡

12. 先建 10 张概念卡（顶点模型、framing 因子、CS 与 Wilson 圈、Lefschetz 顶针、KW 方程、q 作瞬子数、H=H(V,Q)、五维提升、Nahm 极点、even/odd Khovanov），再建 4 张推导卡（CS→KW、q 作瞬子数、5d→Khovanov、Nahm 极点由 KW 约化）。
13. 每张卡先写 definition/goal 与 key_points/steps，再回填 sources：每条 source 选一句 12–120 字符的英文原句，先在 txt 里检索确认落在所标页，再写进 JSON。
14. 写完后跑一次非 strict 的 lint，按报错修：id 段必须小写（`khovanov-homology-H` → `-h`）、related 只能指向本包已有 id（推导卡尚未建时会报错，故先建概念后补 related 的顺序要留意）。

## 6. 收尾文档

15. `terms.tsv`：27 条，英文用原文首现写法，首见页用脚本在全篇检索确认（不是凭记忆）。
16. `excerpts.md`：4 段精译（p2 顶点模型、p11 CS 梯度流、p16 V/Q/H、p20 Nahm 极点），每段 150–400 字，段前 `[p.N]`。
17. `notes.md`：§1 骨架、§2 主定理、§3 接口（11 条，附撞名处理）、§4 核对与勘误（五项表 + 外部来源 6 行 + 勘误 3 条）、§5 不懂/遗留。
18. `trace.md`（15 条，含 2 条真实弯路）与本文。

## 7. 收尾检查

19. 依次执行：

```
PY tools/lint_cards.py out/14_ggl14 --max-pages 26 --strict
PY tools/verify_pages.py out/14_ggl14 --strict
PY tools/term_index.py check out/14_ggl14/cards
PY <外部审计脚本> out/14_ggl14 14 26
```

20. 全部通过后，把 14 张卡的 `status` 由 `draft` 改为 `dev`，再跑一次 lint 确认没有回退。

## 踩过的坑（简记）

- txt 里的公式不可直接引用：(1.5)、τ 对偶句、`2^7` 都被压平，必须回 PDF 渲染核对。
- 早期笔记把 p19 的 π₄ 表记成 (2.16)，全篇其实没有这个编号；`audit_locators.py` 会按 locator 里的式号回查页面，编造编号必失败。
- `verify_pages.py` 只做「去标点后逐字包含」匹配：多写一个 `it is` 就会判失败，quote 必须与原文逐字连续。
- `related` 不能跨包引用；跨篇接口只能写进 notes。
