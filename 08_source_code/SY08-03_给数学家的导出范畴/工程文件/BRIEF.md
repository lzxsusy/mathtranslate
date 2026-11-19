# SY08-03 工程简报（BRIEF）

## 一、目标

把 R. P. Thomas 的 *Derived categories for the working mathematician*（arXiv:math/0001045，
2000-01-07；v2 2001-10-17，13 页）完整译成中文译注本，并交付三样东西：

1. **可编译的 LaTeX 源码**：`源码/` 下 `xelatex main.tex` 两遍即得 28 页中文 PDF；
2. **校订**：正文就地保留原文数学，凡判定的疑误用红色「校勘」框标出，另在附录 B 逐条
   给出位置、原文、判定、依据、建议；
3. **精读**：附录 D 提供论证地图、逐节导读、五个关键论证的拆解、后续发展（dg 范畴 /
   稳定 ∞-范畴 / 导出代数几何）与五道带提示的习题。

## 二、底本

- 原文：R. P. Thomas, *Derived categories for the working mathematician*,
  arXiv:math/0001045（v1 2000-01-07；v2 2001-10-17）。13 页，amsproc 类，
  两张图以 fig2dev 生成的 EPS 内嵌于源码。
- 会议版：*Winter School on Mirror Symmetry, Vector Bundles and Lagrangian
  Submanifolds*（Harvard, 1999），AMS/IP Stud. Adv. Math. **23** (2001), 349–361；
  Zbl 1008.18011。

## 三、范围

- 正文章节：§1 引言、§2 链复形、§3 拟同构、§4 范畴论、§5 锥与三角、§6 导出函子；
- 参考文献四条（GM、HRD、K、Ma）照录，不增补；
- 原文两张 EPS 图用 TikZ 重绘（不携带原始 EPS，见 `源码/sections/05_cones.tex`）。

## 四、交付物

| 交付物 | 位置 | 说明 |
| --- | --- | --- |
| 中文译注本 PDF | 不入仓（L3 外链） | 由源码构建，`main.pdf` 28 页 |
| LaTeX 源码 | `源码/` | `main.tex`、`preamble.tex`、`sections/*.tex` |
| 术语表 | 源码附录 A / `工程文件/work/glossary.tsv` | 76 条，中英对照 + 首次出现 |
| 校勘记 | 源码附录 B / `工程文件/work/疑点清单.tsv` | 确认 8 条 + 存疑 2 条 |
| 译注汇总 | 源码正文 / `工程文件/deliverable/译注汇总.md` | 20 条，均带来源或译者按 |
| 精读指南 | 源码附录 D / `工程文件/deliverable/阅读参考指南.md` | 地图 + 导读 + 论证 + 习题 |
| 工程总结 | `工程文件/deliverable/工程总结.md` | 方法、统计、遗留问题 |

## 五、约束（硬性）

1. 只改分配文件；不动 `\label`/`\ref` 语义与编号（本书节号已按实际顺序改正，见校勘 1）。
2. 不改原文数学内容；判定的疑误加框说明，不悄悄改。
3. 每条解释性译注末句必须带 `[来源：…]` 或 `[译者按（无外部依据）…]`。
4. 来源只用 A 级原始文献（Gelfand–Manin、Hartshorne、MacLane、Weibel、Kashiwara–
   Schapira 等）与 B 级白名单（nLab / Stacks Project / ProofWiki），黑名单站点一律不引。
5. 译文一句 ≤ 60–70 汉字，全角标点，英文术语两侧半角空格。
6. 交付前 `xelatex` 两遍零错误、零未定义引用、零 Overfull。

## 六、里程碑

1. 通读笔记 + 疑点清单（未解 = 0）——2026-11-19
2. 六节正文译完 + 两张 TikZ 图——2026-11-20
3. 附录 A–D——2026-11-20
4. 编译、目检（书名页 / 译序 / §4 / §5 图 / 附录 A、B、D）——2026-11-20
5. 工程文件、入仓、推送——2026-11-20

## 七、验收标准

- `cd 源码 && xelatex main.tex` 两遍，退出码 0，`grep -c '^!' main.log` 为 0；
- PDF 页数 28，图 1、图 2 与原文 EPS 的拓扑结构一致（锥的顶点与悬挂形）；
- 译注 20 条全部带来源标记；校勘 7 框与附录 B 的 K1–K7 一一对应（K8 为拼写，仅在附录记）；
- 术语表 76 条，正文术语与表一致（`工程文件/work/check.py` 抽查）。
