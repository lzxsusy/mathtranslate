# 第 08 篇 · 决策记录（trace）

只记录本轮真实做过的判断；「事后确认」写的是后来实际发生的事，不是预想。

| # | 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- | --- |
| 1 | 先读哪几节来定主线 | TASK 的读法建议（摘要→引言→结论），加上 XREF 显示本篇只有 v1、无后续修订 | 先读摘要、§1、§4.2、§5.5 末，确定主线是「六维 $(0,2)$ → 四维电磁对偶 → 曲面几何 Langlands」三层；§3 的 $U(1)$ 计算放到第二遍再逐式核 | 主线在写 notes 骨架时直接可用，没有返工 |
| 2 | §2（各种维数的算子）要不要建卡 | §2 只有 2 页，但 §1.2 与 §5 反复用到 't Hooft 算子与 Hecke 算子 | 建两张：`defects-of-various-dimension`（公理与 $p$-流形算子）与 `thooft-operator-to-hecke-operator`（算子词典）；理由是 't Hooft 算子是几何 Langlands 词典的核心，不可迁移性最低 | 两张卡在 lint 里 related 都被别的卡引用，没有孤立卡 |
| 3 | 概念卡取几张 | TASK 写 8±2；BRIEF 的公式 pages/12 给出 2.5、钳到下限 8 | 取 10 张（上限 8+2）：除主线五张外，加 Taub-NUT、$\Gamma_k$、BPS 两种描述、电/磁分级；理由是本篇一半篇幅在 §5.4–§5.5，砍掉就只剩引言 | lint 报「卡 14 张（概念 10 / 推导 4）」 |
| 4 | 推导卡取几张 | TASK 写 3±1 | 取 4 张：$U(1)$ 对偶、$\tau\to-1/\tau$、反常流入、$\Gamma_k$ 分解；理由后两条是 §5 的独立论证链，且都能迁移到别篇 | 4 张都通过 lint 的 steps/provenance 检查 |
| 5 | **弯路**：(3.4) 的 $\theta$ 项到底有没有 $i$ | 第一遍按 p.8 打印原样抄成无 $i$；读 KW06 时在其 p.48 看到 "in Euclidean signature ... $i\theta/8\pi^2$" | 先以为只是号差约定、不该记勘误；回头核 Gukov–Witten (2.26)(2.38) 也带 $i$，再看本篇 p.4「$\tau\to\tau+1$ 因为瞬子数取整」——无 $i$ 时 $e^{-I}$ 不变性不成立，属内部不自洽 ⇒ 判 high、记 E1、卡片按订正写 | errata.tsv 第 1 行；两张卡加 `corrections`；lint 校验 corrections.id 在 errata 中存在，通过 |
| 6 | **弯路**：(3.2) 的 ansatz 是否自动自对偶 | 一开始在推导卡第 1 步写「$H=\star H$ 自动成立」 | 实算：按 $dx\wedge dy$ 定向，$\star(F\wedge dx)=\star F\wedge dy$ 但 $\star(\star F\wedge dy)=-F\wedge dx$，故 $\star H=\star F\wedge dy-F\wedge dx$，不是 $H$；改成「需取 $T^2$ 的相反定向」并把这点写进 gaps 与 pitfalls | 重算两遍确认符号；steps 第 1 步与 gaps 已按实算写 |
| 7 | **弯路**：KW06 式 (4.16) 能否直接当卡片来源 | 它是 E1 最有力的外部依据 | 先写 `pages: [48,48]`，被 lint 的 `--max-pages 30` 拒绝（pages 必须 $\le 30$；该规则对所有 text 生效，不只 A）；改为引 Gukov–Witten p.13/p.17，KW06 (4.16) 只写进 errata 依据与 notes | lint 从 4 个 error 降到 0；推导卡 D1 的 C 源改为 Gukov–Witten p.13 |
| 8 | **弯路**：三条 quote 凭压缩摘要转述 | 写 `electric-magnetic-grading` 时手头只有摘要里的「important bigrading of H」等 | `verify_pages.py` 报三条「原文里搜不到」；回读 p.23/p.24，改成逐字句 "an important bigrading of the"、"We call this the electric grading"、"grading arises for topological reasons"，并把两条页码由 24 改为 23 | 再跑 verify：57 条、0 问题 |
| 9 | 推导卡的 `type` 写什么 | 目录叫 `derivations`、id 段叫 `deriv` | 先写 `"type": "deriv"`，lint 报「type 与目录不符」；读源码 `tools/lint_cards.py:43` 才知道 id 段用 `deriv`、`type` 必须写 `derivation` | 四张卡改字段后 lint 通过 |
| 10 | Taub-NUT 度量的 $1/2$ 是不是笔误 | 0902.0948 式 (2.2) 写 $U=\frac{1}{|\vec X-\vec x|}+\frac{1}{\lambda^2}$，本篇 (5.9) 写 $\frac{1}{R^2}+\frac{1}{2|\vec x|}$ | 一度怀疑本篇漏/多 $1/2$；查该文的 $\theta$ 周期与荷归一后判定为约定差异，不是笔误 ⇒ 不记 errata，只写进 notes「不计入勘误的约定差异」 | errata.tsv 只有 E1 一行；notes 有该条 |
| 11 | 术语译名以谁为准 | SCHEMA 的术语表 + 库内 kw06/ggl12 的既有卡 | 采 twist=扭化、eigenbrane=特征膜、Hecke eigensheaf=Hecke 特征层、't Hooft 算子不译、BPS 不译、ramification=分歧；Taub-NUT、Kac–Moody、Heisenberg 均不硬译 | terms.tsv 31 行；term_index 连报四轮撞名（surface operator / codimension-two defect / disorder operator / Hecke 算子 / Hecke 对应），逐条改我这边的别名后 0 处 |
| 12 | XREF 的「结论」列要不要回填 | XREF.md 自称「本栏必须逐条回填」，且它在 `out/08_ggl08/` 内（允许写） | 回填 5 行结论，同时在 notes 的「XREF 五项动作清单」里保留逐条细节；理由是两处互补：XREF 给结论，notes 给证据 | XREF.md 已改；notes 的表格 5 行 |
| 13 | 0711.2083 要不要作卡片来源 | 其 abs 页支持 §5.5.4 的对应 | 该文页码无法压到 $\le 30$，且引用它需要 arXiv abs 页页码，不是本篇页序；决定只进 notes 的外部来源表 | 卡片里没有 0711.2083 的 source；notes 外部来源表第 5 行 |
| 14 | §5.2.2 的弦论构造、§1.1 的 Chern–Simons 范畴要不要建卡 | 前者依赖 M-理论/D6 的具体对偶，后者两页带过 | 都不建卡，写进 notes 骨架与「不懂」；理由是它们不可迁移到别的篇目，且我无法独立核其系数 | notes 骨架与「不懂」各有一条；概念卡 10 张里没有它们 |
