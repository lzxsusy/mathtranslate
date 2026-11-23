# 批注来源抽查（01 v2.1 §9）

抽查日期：2025-11-23。对象：`源码/sections/*.tex` 中已补 `[来源：…]` 的 182 条批注。方法：按批注前最近的 `% ==== 原文 PDF 第 N 页` 取页，在 `work/audit/review/pNNN.txt` 的英文列中核对批注所述原文事实。

| # | 批注位置 | 标注页 | 核对原文事实 | 结论 |
|---|---|---|---|---|
| 1 | `s02-duality.tex:42` | p.14 | p14 英文为 “Hitchin’s equations … $F-\phi\wedge\phi=0$, $d_A\phi=d_A\star\phi=0$”，与批注的直算说明一致 | 通过 |
| 2 | `s03b-genus1.tex:109` | p.30 | p30 英文 “$U\oplus S$, where $W$ is a rank two local system” 确将 $U$ 误印作 $W$，批注定位正确 | 通过 |
| 3 | `s05a-spectral.tex:84` | p.58 | p58 英文 “Stieffel-Whitney” 确为原文拼写，批注所述两处一致 | 通过 |
| 4 | `s05a-spectral.tex:166` | p.61 | p61 英文 “Let $E'=D-(g)$” 确与应得的 $E-(g)$ 不符，批注定位正确 | 通过 |
| 5 | `s11-appendix.tex:38` | p.124 | p124 条件 (2′) 英文/译文均作 “$f(xu)=f(x)$”，而该空间函数为 $\phi$，批注定位正确 | 通过 |

结论：5/5 条批注的页码定位与其所述原文事实相符。自动补标采用的是“批注前最近页锚点”，对页边界处的批注仍可能有半页偏移；本次抽查未发现错页。
