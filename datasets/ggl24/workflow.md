# workflow（第 24 篇）

## 1. 实际流程

1. **读规范**：`TASK.md`、`XREF.md`、`BRIEF.md §9/§10`、`cards/SCHEMA.md`，并把
   `tools/lint_cards.py`、`tools/verify_pages.py`、`tools/term_index.py`、
   `audit_locators.py` 的判定逻辑读了一遍（不是猜规则，而是照着源码写字段）。
2. **通读原文**：`txt/24/p001.txt`–`p083.txt` 全部读完，边读边把「页—式号—一句话」记成
   流水笔记：§1 两张图、§2 自对偶/谱曲线/SOV、§3 opers/Schlesinger/实切片、§4 量子化三方案
   与 Baxter、§5 共形块/退化场/半经典极限/Yang 势、§6 Fock–Goncharov/长度算子/Kähler 量子化、
   §7 临界层与 Hecke、§8 KZ/Θ 扭转/modular duality/量子局部系统/高秩。
3. **定卡**：先按「承重概念 + 不撞名」挑 10 个概念、3 条推导链；每条推导链要求能在原文里
   找到 5 个连续编号的式子，这样 `steps` 的 `locator` 才落得实。
4. **备料外校**：把 arXiv v1（`external/v1.txt`）、Nekrasov–Shatashvili 0908.4052、
   Kapustin 0811.3264、Teschner hep-th/0104158 下到 `external/`；对照 v1 §4.6 与 v5 §5.5
   的编号位移，确认 (5.38)/(5.41) 的 $\pi$ vs $2\pi$、以及 (5.47) 笔误跨版本存在。
5. **写卡**：每张卡先定 `sources` 的逐字 quote，用本地脚本 `_ggl24_qcheck.py`（归一化小写、
   只留字母数字、展开连字）回查该句真正落在哪一页，再决定 `pages` 区间；公式一律写原文编号。
6. **写 errata**：E1 (5.47)、E2 (3.41)、E3 (8.58) 判 medium 并订正；E4（p.8 的
   「$\theta=0$ 切片」表述）只有本篇一处内部矛盾、无第二独立出处，按 BRIEF §9.2 判 low、
   保留原文、在卡里标存疑。
7. **写 notes**：照库内 25 号包的节序（页码约定 / 一句话 / 骨架 / 主命题 / 接口 / 记号核对 /
   外部校正五项 / 不懂 / 核对与勘误）。
8. **自检**：`lint_cards.py --strict` → `verify_pages.py --strict` → `term_index.py check`
   → `audit_locators.py`；全绿后把 13 张卡的 `status` 从 `draft` 改 `dev`，再跑一次 lint。
9. **补件**：`terms.tsv`（22 行）、`excerpts.md`（4 段，每段 150–400 汉字）、`trace.md`
   （14 条、4 条弯路）、本文件。

## 2. 最耗时 / 最易错

- **最耗时**：给每条 `sources.quote` 找它究竟在哪一页。正文的句子常跨页断开（比如
  「The conformal blocks (5.28) form a complete set of solutions」在 p.37 顶部，而 (5.28) 在
  p.36），`verify_pages.py` 只认归一化后的连续子串，跨页就搜不到，所以每条 quote 都回查、
  必要时换成同页的另一句。
- **最易错**：
  1. `pages` 写成单页而 quote 实际邻页 → 统一写跨节区间；
  2. 撞名（`term_index.py` 索引含 ggl25/ggl17/kw06/bdh/glc 等）→ 标题避开已译包的定名；
  3. errata 的「影响卡片」写成「—」或写不存在的 id → lint 直接报错；
  4. `notes.md` 的「外部来源」表必须三列且 `|` 行 ≥4，两列会被判「核对节不全」；
  5. 推导卡 `locator` 必须也是 anchor 格式（`A p.38 eq (5.34)`），写「见上式」会被拒；
  6. 概念卡 `summary` 去 `$…$` 后数非空白字符 ≤120，含公式的 summary 很容易超。
- **两处真实的判断失误**（详见 `trace.md` 弯路 1、2）：实切片的锥奇点先写在 $\vartheta$
  零点（应为 $\gamma$ 零点）；E4 先想判 high（后按纪律降 low）。

## 3. 重做怎么改

按下面的顺序重跑，能把返工压到最少：

1. 先读 `tools/` 的四个校验脚本，把「字段—正则—退出码」抄成一张表，再动笔。
2. 先把 83 页读成「页—式号—一句话」三列表（约 80 行），再从这个表里挑卡；不要边读边写卡，
   否则同一段会被两张卡重复引用。
3. 每条 quote 先用回查脚本确认页码，再写 `pages`；**先定 quote 后定卡**，而不是先写卡再找引文。
4. 每写完 3–4 张卡就跑一次 `lint_cards.py`（不必等全部写完），错误定位快。
5. `notes.md` 最后写，但「外部来源」表先按三列模板起好，逐条填；errata 先写，卡里的
   `corrections` 才有 id 可引。
6. 全部 `draft` 通过后一次性改 `dev`，避免两次改状态。

## 4. 产出清单

| 文件 | 内容 |
|---|---|
| `notes.md` | 骨架、S1–S14 主命题、8 篇接口、记号核对、五项外校、7 条不懂、外部来源 6 行、勘误 E1–E4 |
| `cards/concepts/*.json` | 10 张 |
| `cards/derivations/*.json` | 3 张 |
| `terms.tsv` | 22 行术语（英文 / 中文 / 首见页 / 备注） |
| `excerpts.md` | 4 段精译（p.1、p.5、p.37、p.71） |
| `errata.tsv` | 4 条（E1–E3 fixed，E4 open/low） |
| `trace.md` | 14 条四栏判断记录，4 条弯路 |
| `external/` | v1 全文与 abs 页、NS 0908.4052、Kapustin 0811.3264、Teschner hep-th/0104158 |
