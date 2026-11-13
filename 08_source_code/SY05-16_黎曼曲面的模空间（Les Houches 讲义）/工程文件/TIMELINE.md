# TIMELINE.md — 分块表与接续锚点（Lead 独占）

> PDF 页号 = 印刷页码（偏移 0）。
> **公式区间两端都是"包含"**。开始块以本区间**第一条** `\tag` 为准；结束块以**最后一条**为准。
> 实际边界与表不符 → 不要自己改，回报 `BOUNDARY:`，Lead 裁决后更新本文件并通知上下游。

## 分块总表（9 块 = Lead + 8 队友）

| 块 | 负责人 | 文件 | PDF 页 | 原文 | 公式（含两端） | 条数 | 编号环境 | 图/表 |
|---|---|---|---|---|---|---|---|---|
| A | **Lead** | `sec1.tex` | 2–3 | §1 Introduction + 致谢/资助 | 1.1–1.2 | 2 | 无 | Fig 1(p2) 略；致谢、资助整段译 |
| B | tr-s21 | `sec21.tex` | 4–9 | §2.1 Definition of the moduli spaces | 2.1–2.16 | 16 | Def 2.1, Ex 2.1, Thm 2.2, Ex 2.2, Ex 2.3, Def 2.3 | Fig 2(p4), Fig 3(p6), Fig 4(p7), Fig 5(p9), Fig 6(p9) 均略 |
| C | tr-s22 | `sec22.tex` | 10–15 | §2.2 Stratification and tautological maps | 2.17–2.35 | 19 | Thm 2.4, Def 2.5, Ex 2.4 | Fig 7(p11), Fig 8(p11), Fig 9(p12), Fig 10(p13), Fig 11(p13) 均略 |
| D | tr-s23a | `sec23a.tex` | 16–20 | §2.3 前半（Intro + ψ 类之前） | 2.36–2.61 | 26 | Ex 2.5, Ex 2.6, Ex 2.7, Ex 2.8 | Fig 12(p18) 略 |
| E | tr-s23b | `sec23b.tex` | 21–26 | §2.3 后半（ψ/κ 类 → 2.79） | 2.62–2.79 | 18 | Ex 2.9, Ex 2.10, Thm 2.6, Ex 2.11 | **Table 1(p23) 抄**；Fig 13(p24), Fig 14(p25) 略 |
| F | tr-s31 | `sec31.tex` | 27–30 | §3.1 Axioms | 3.1–3.24 | 24 | Def 3.1, Ex 3.1, Example 3.2 | 无 |
| G | tr-s32 | `sec32.tex` | 31–34 | §3.2 Givental's action | 3.25–3.48 | 24 | Def 3.3, Prop 3.4, Def 3.5, Prop 3.6, Ex 3.2, Thm 3.7 | 无 |
| H | tr-s33 | `sec33.tex` | 35–37 | §3.3 Connection to topological recursion | 3.49–3.60 | 12 | Ex 3.3, Thm 3.8, Thm 3.9, Ex 3.4, Ex 3.5 | **Table 2(p37) 抄** |
| I | tr-s4 | `sec4.tex` + `refs.tex` | 38–42（§4）+ 43–46（文献） | §4 Further directions（4.1, 4.2）+ References | 4.1–4.14 | 14 | Thm 4.1, Thm 4.2, Ex 4.1, Thm 4.3 | Fig 15(p39) 略；**Table 3(p41) 抄**；文献 43–46 逐条抄 |

合计：155 条编号公式、35 处编号环境、15 图（略，仅译注）、3 表（抄）。

## 精确接续锚点（防重防漏）

> ⚠️ **2026-11-03 裁决**：实测发现 §2.2、§2.3、§3.1、§3.2、§3.3 五个小节标题都落在**页面中部**，其前面的公式属于该块的编号区间。因此这五个小节标题**由对应块在正文流里就地写出**，main.tex 不写。各块负责人以收到的修正消息 + 下表为准。
> §2、§2.1、§3、§4、§4.1 五个标题仍由 main.tex 写。

| 边界 | 前块最后一条 | 后块第一条 | 说明 |
|---|---|---|---|
| A→B | (1.2)，p3 末"Funding information"结束 | (2.1) | B 从 p4 "Terminology." 开始；§2 标题 + §2 引言段 + §2.1 标题由 main.tex 写 |
| B→C | (2.16) + p9→p10 的稳定条件段（"…$2g(v)-2+n(v)>0$ for all $v$."） | p10 "The main result about the Deligne–Mumford moduli space is that…" 段（含 **Thm 2.4**、$\partial\Mc$、**(2.17)(2.18)(2.19)**） | **§2.2 标题在 p10 中部，C 就地写出**：插在 "…often called intersection theory." 之后、"Before discussing the cohomology…" 之前 |
| C→D | (2.35)，p15 末 | p16 顶部 "In terms of differential forms…" 段（含 **(2.36)(2.37)(2.38)** + 投影公式） | **§2.3 标题在 p16 中部，D 就地写出**：插在投影公式段之后、"Recall our main goal…" 之前 |
| D→E | (2.61) | (2.62) | 都在 §2.3 内部，无标题 |
| E→F | (2.79) | p27 §3 标题后第一段（Virasoro 约束段，含 **(3.1)(3.2)(3.3)**、TQFT 类比段、Kontsevich–Manin 段） | **§3.1 标题在 p27 中部，F 就地写出**：插在 "…2D TQFTs [Dub96]." 之后、"Fix once and for all…" 之前 |
| F→G | (3.24) | p31 顶部（Example 3.2 余下 bullet，含 **(3.25)**、Novikov 变量段） | **§3.2 标题在 p31 中部，G 就地写出**：插在 "…see [KM94]." 之后、"We have already seen how…" 之前；§3.2 内的 3.2.1/3.2.2/3.2.3 用 `\subsubsection`（自动编号与原文一致） |
| G→H | (3.48) | p35 顶部（"where $\delta_m=\dots$" + **(3.49)**、Exercise 3.3、Teleman 段） | **§3.3 标题在 p35 中部，H 就地写出**：插在 "…Pretty neat!" 之后、"Givental's action provides a recursive construction…" 之前 |
| H→I | (3.60) | (4.1) | §4 与 §4.1 标题由 main.tex 写；**§4.2 标题在 p41 中部，由 I 在 sec4.tex 里就地写出** |

## 已知细节（防止踩坑）

1. **p13 没有编号公式**（全页是 Fig 10/11 与文字）。p12, p14 有。
2. **p23 的 Table 1** 与公式 2.70–2.71 混排；表在正文之间，不要漏表前后的句子。
3. **p37 的 Table 2** 在 §3.3 末尾，Table 2 后还有 Exercise 3.5（p37）。
4. **p41 的 Table 3**（Weil–Petersson 多项式 $V^{\mathrm{WP}}_{g,n}(L)$）是多行数据表，抄的时候逐格对图；表后还有 §4.2 的收尾段落。
5. **p43–46 参考文献**：条目不翻译（作者/标题/期刊保持原文），只重排；`[键]` 用 `\bibitem[键]{...}`。正文里的 `[DM69]` 类引用格式保持。
6. **p3 的 "Funding information"** 是原文正文段落（不是脚注），整段译。
7. **p2 的 Figure 1 图注**很长（"A string travelling through spacetime…"），照译，放在图从略标记后。
8. 原文 `2.1. Definition of the moduli spaces.` 标题末尾带句点，中文标题不带句点。
9. 原文 p16 的 §2.3 开头提到 "brackets $[\cdot]$"，注意与公式编号方括号区分。
10. 原文 §2.2 讲 stable graph 与对偶图，术语按 glossary（重言类/重言环）。
