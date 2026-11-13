# TIMELINE —— 边界裁决（Lead 维护；每条已同时通知上下游两人）

约定：`PDF 页号 = 印刷页码 + 1`。下表按「块」给出起止锚点句，**开始者写完**（跨页句由开始的一侧负责收尾，
除非下表另有裁决）。

| # | 边界 | 裁决 | 上游（写到哪） | 下游（从哪开始） | 已通知 |
|---|---|---|---|---|---|
| B1 | lead / tr-01（PDF p.10 内，印刷 p.9） | §2.7 结尾两句在 PDF p.10 顶部，归 **lead**；tr-01 从同页的 `\section{T-对偶}` 起 | lead 写到 "Some of the consequences in these examples are mathematically proven." | tr-01 第一行写 `% [原文 p.9]` + `\section{T-对偶}` | lead, tr-01 |
| B2 | tr-01 / tr-02（PDF p.17→p.18） | 干净接缝（段末 → 新 § 标题） | tr-01 写到 "...gauged linear sigma models to which we turn next." | tr-02 从 `\section{规范线性 sigma 模型}` 起 | tr-01, tr-02 |
| B3 | tr-02 / tr-03（PDF p.23→p.24） | 干净接缝（4.3 末尾 → 4.3 内小标题） | tr-02 写到 "...complex structures of the Higgs branch, respectively." + (4.20) | tr-03 从 `\para{非 Calabi–Yau 情形}` 起 | tr-02, tr-03 |
| B4 | tr-03 / tr-04（PDF p.30→p.31） | 干净接缝（(4.34) 之后 → 新段落） | tr-03 写到 (4.34) 公式环境结束 | tr-04 从 "The space of FI parameter $\R^2=\{(\zeta_1,\zeta_2)\}$ is separated into three phases..." 起 | tr-03, tr-04 |
| B5 | tr-04 / tr-05（PDF p.37→p.38） | 干净接缝（(4.54) 之后 → 新段落） | tr-04 写到 (4.54) 公式环境结束 | tr-05 从 "This means that $v_i$ is an inward normal to the polytope..." 起 | tr-04, tr-05 |
| B6 | tr-05 / tr-06（PDF p.44→p.45） | **(5.27) 后的续写分句**：tr-05 写到含 (5.27) 的公式环境结束即打住，**不写** "which defines..." 分句；tr-06 从该分句起续写 | tr-05 最后一行为 (5.27) 的 `\end{equation}` | tr-06 第一句："它定义一个代数环面 $T^{N-k}_{Q,t}\subset(\C^\times)^N$，与 $(\C^\times)^{N-k}$ 同构……" | tr-05, tr-06 |

## 其他已裁决事项
1. **标题归属**：见 BRIEF「标题归属表」。任何人不得写不属于自己的 `\section`/`\subsection`
   （否则自动编号会整体错位）；行内小标题用 `\para{…}`。
2. **图归属**：fig1/fig2 → tr-01；fig3 → tr-03；fig4–fig8 → tr-04。其他块不插图。
3. **公式编号**：139 条，各块区间见 BRIEF；块内**无编号公式**一律 `\[…\]`/`equation*`，绝不自造编号。
4. **原文页码标注**：每页起始 `% [原文 p.N]`，N = 印刷页码（= PDF 页号 − 1）。
5. **不完整版声明**：5.5 的 "The CP^{N−1} Model" 小标题下原文无内容（讲义为不完整版），
   照排并批注；不得编造内容。
6. **参考文献**：不译，Lead 用 `\refitem{…}{…}` 原貌转录。
