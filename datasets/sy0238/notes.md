# sy0238 资料卡包笔记

## 1. 选卡原则

- 一讲取 3–5 个「离开原文就说不清」的对象：定义、定理、构造、易混概念。
- 优先收**原文只给陈述不给证明**的结论（本书大量如此），卡片用 `proof.status = "gap"` 明示缺口。
- 概念卡讲「是什么、为什么重要、和谁易混」；推导卡讲「怎么从 A 到 B」，每步带 `locator`。

## 2. 页码与引用

- 页码 = PDF 页序（偏移 0），`anchor = "A p.NN"`。
- `quote` 一律取自 `08_source_code/SY02-38_朗兰兹纲领入门课程讲义/工程文件/work/pages/pNNN.txt`，逐字，12–120 字符，不含中文。

## 3. 核对与勘误

外部来源核对（按 TRANSLATION-STANDARD v2.1 「来源分级」：A 级原书/经典教材/原始论文优先）：

| 条目 | 本库/原文说法 | 外部来源 | 判定 |
| --- | --- | --- | --- |
| ordinary / supersingular 定义（p.68 定义 8.6） | 原文写 $E(\mathbb{F}_p)=\mathbb{Z}/p\mathbb{Z}$ | Brian Conrad 等标准教材；Goren, *Hilbert Modular Forms*, Ex 3.10（wstein.org，2026-11-26） | 原文应为 $E[p](\overline{\mathbb{F}}_p)\neq0$（ordinary） |
| Hasse 不变量与 $E_{p-1}$ 同余（p.80–81） | $Ha=V^*\in\Gamma(\omega^{\otimes(p-1)})$，$q$-展开恒 1 | MIT 讲义 Murilo（math.mit.edu/nt/Murilo2020-02-26.pdf，2026-11-26）；Deligne 1973 | 一致：$A(E,\omega)$ 由 $F^*\eta=A\eta$ 定义，零点为超奇异曲线 |
| Eichler–Shimura 同构维数（p.74 定理 9.1 证明） | $\tilde h^1=2h^0-\chi_{top}$，$\chi_{top}=2\chi_{hol}$ | Deligne 1971（Sém. Bourbaki 355）、Diamond–Shurman 2005 §5.4 | 一致；原文的 Riemann–Roch 中间步需补 Serre 对偶 |
| Satake 参数与 $L$-群（p.96–97） | $c_p(\pi)$ 的特征多项式含 $p^{i(i-n)/2}\tilde a_{p,i}$ | Getz–Hahn, *An Introduction to Automorphic Representations*（[GH19] §7.2）；Buzzard–Gee 2010 §2 | 一致（原文自引 [GH19]） |

### 勘误

正文发现的笔误逐条记在 `errata.tsv`（28 条，`状态=fixed`），卡片 `provenance_note` 与 `pitfalls` 里只提**影响理解**的几条（E06、E07、E10、E17、E21、E25）。核对详情另见工程内 `工程文件/work/疑点清单.tsv`（25 行）与 `工程文件/work/reports/kb_plugin_feedback.md`。

## 4. 已知缺口

- 本书「不给证明」的定理（如定理 2.5 谱分解、定理 9.1、定理 10.1/10.2）在卡里标 `gap`，并指向 [GH19]/[Del71]/[DS74] 的原始证明位置。
- 权 1 形式提升到复表示一节（p.84–87）原文步骤跳得快，卡 `deligne-serres-lifting` 用推导卡补出骨架，缺口标在 `gap_note`。
