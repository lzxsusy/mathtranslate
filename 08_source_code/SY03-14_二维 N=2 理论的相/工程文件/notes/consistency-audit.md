# 全稿一致性审计（只报不改）

- 审计对象：`sections/` 下全部 16 个 `.tex`（14 个正文分片 + `s05a2-comment.tex` + `appendix-pagemap.tex`），并与 `main.tex` 的装配顺序核对。
- 审计方式：Python 静态扫描（tag／公式引用／页码标签／脚注／标题／术语／英文残留）+ 原文 PDF 文本层与页面图像（`pages/page-02..92.png`）抽检定位。
- **快照说明**：本次审计以 2026-10-24 11:25 前后的文件状态为准（此前 11:22:43 Lead 对全部分片批量插入了 `\label{op:N}`，并调整了 `main.tex` 的同行 `\frag` 拼接与 `s05a2` 标题层级）。若之后文件再有改动，下文行号可能平移。
- **本次审计不修改任何分片文件**，仅产出本报告。

## 结论摘要

| 检查项 | 结果 |
|---|---|
| ① 公式 tag 完整性 | **188/188**（1.1–1.3、2.1–2.35、3.1–3.52、4.1–4.3、5.1–5.48、6.1–6.47），无缺号、无重号、无越界 |
| ① 公式交叉引用 | **376 处**引用（正文 131 + 批注 245），**0 处悬空**；正文无前向引用；无 `\ref/\eqref/\cite` |
| ① 页码标签 | 91 个 `\label{op:2..92}` 唯一无缺，附录 91 个 `\pageref` 全部可解析 |
| ② 术语 | GLOSSARY 强制项**全部合规**；发现 **6 类需统一**的变体（异常/反常、目标空间/靶空间、扭曲手征/扭手征、拉氏量/拉格朗日量、局域/局部、`\mathbf{C}`/`\mathbb{C}`） |
| ③ 代码区英文 | 14 个正文分片 **0 处**英文正文；`s07-references` 英文书目为设计保留（非缺陷） |
| ④ 脚注 | 原文正文 **11 条** + 标题页 1 条；译文 `\footnote` **11 条** + `main.tex` 的 `\thanks` 1 条，逐页对应，**无缺漏、无多余** |
| ⑤ 标题层级 | 编号小节 **11/11** 与原文一致；无编号小标题 **27/27** 对应；仅 `s05a2` 一处层级选择与全稿政策不一致（建议项） |

---

## ① 公式交叉引用

### 1.1 tag 清单与完整性

| 分片 | tag 数 | tag 区间 |
|---|---|---|
| `s01-intro` | 3 | 1.1–1.3 |
| `s02a-fieldtheory` | 16 | 2.1–2.16 |
| `s02b-fieldtheory` | 19 | 2.17–2.35 |
| `s03a-model` | 7 | 3.1–3.7 |
| `s03b-singularity` | 16 | 3.8–3.23 |
| `s03c-applications` | 9 | 3.24–3.32 |
| `s03d-twisted` | 20 | 3.33–3.52 |
| `s04-geometry` | 3 | 4.1–4.3 |
| `s05a-wps-toric` | 19 | 5.1–5.19 |
| `s05b-grassmann-intersect` | 17 | 5.20–5.36 |
| `s05c-topology` | 12 | 5.37–5.48 |
| `s06a-superfields` | 34 | 6.1–6.34 |
| `s06b-models` | 13 | 6.35–6.47 |
| `s05a2-comment`、`s07-references`、`appendix-pagemap` | 0 | —（原文该段无带号公式） |

- 合计 **188**，与期望集合（3+35+52+3+48+47=188）**完全相等**；缺号 0、越界 0、重复 0。
- `s05a2-comment` 为 p58 顶部纯文字段（原文无带号公式），`s07-references` 为书目，均无需 tag。

### 1.2 引用扫描

扫描规则：全文（正文与 `%` 批注都算）匹配 `(x.y)` 与全角 `（x.y）`，剔除 `\tag{...}` 自身。

| 分片 | 正文引用 | 批注引用 |
|---|---|---|
| s01-intro | 0 | 8 |
| s02a-fieldtheory | 8 | 18 |
| s02b-fieldtheory | 10 | 32 |
| s03a-model | 8 | 17 |
| s03b-singularity | 11 | 34 |
| s03c-applications | 3 | 12 |
| s03d-twisted | 29 | 12 |
| s04-geometry | 3 | 5 |
| s05a-wps-toric | 6 | 9 |
| s05b-grassmann-intersect | 10 | 15 |
| s05c-topology | 16 | 10 |
| s06a-superfields | 14 | 55 |
| s06b-models | 13 | 15 |
| s07-references | 0 | 3 |
| **合计** | **131** | **245** |

- **在 188 个 tag 中找不到对应式的引用：0 处**；引用越界／编号错误：0 处。
- 正文无「引用后文公式」的情形（前向引用 0 处），与原文叙述顺序一致。
- 无 `\ref{}`／`\eqref{}`／`\cite{}`（符合 SPEC §4.8「一律写字面编号」）。
- 疑似项 1 例，**非错误**：`s05b-grassmann-intersect.tex:12` 批注中的「GLOSSARY/§4.5」指本项目 SPEC 的 §4.5，不是原文 §4.5。

### 1.3 页码标签与附录（新增交叉引用）

- 各分片在页锚点注释后统一带 `\label{op:N}`：共 **91 个**（N=2…92），唯一、无缺号、无重名。
- `appendix-pagemap.tex` 中 91 个 `\pageref{op:N}` **全部可解析**（缺 target 0）。
- 页锚点注释共 97 条、覆盖 91 个不同页；页 4、16、44、58、75、87 在相邻两分片各出现一次页锚（分片边界共享页，属正常），`\label` 只在其中一处，故不产生重名标签、pagemap 结果唯一。

---

## ② 术语一致性

### 2.1 GLOSSARY 强制项（全部合规）

| 术语组 | 统计 | 判定 |
|---|---|---|
| 手征 / 手佂 | 手征 **144**，手佂 **0** | ✅ 统一 |
| 凯勒 / 卡勒 | 凯勒 **54**，卡勒 **0** | ✅ 统一 |
| 轨形 / 轨道 | 轨形 **31**（orbifold）；轨道 **32** | ✅ 全部为 orbit／「轨道空间」，非 orbifold 误用 |
| 胀开 / 爆破 | 胀开 **10**，爆破 **0** | ✅ 统一 |
| 辛商 / 辛约化 | 辛商 **42**，辛约化 **0** | ✅ 统一 |
| 横截 / 横断 | 横截 **26**，横断 **0** | ✅ 统一 |
| 反常 / 异常 | 反常 **34**，异常 **1** | ⚠ 见 2.2-① |
| 靶空间 / 目标空间 | 靶空间 **39**，目标空间 **3** | ⚠ 见 2.2-② |
| 扭手征 / 扭曲手征 | 扭手征 **29**，扭曲手征 **1** | ⚠ 见 2.2-③ |

### 2.2 需统一的变体（建议）

| # | 问题 | 位置（行号为当前快照） | 建议 |
|---|---|---|---|
| ① | **异常**（anomaly） | `s01-intro.tex:50`「更温和的异常抵消条件」；全书其余 34 处均作「反常」 | 改为「反常抵消条件」（GLOSSARY：anomaly=反常） |
| ② | **目标空间**（target space） | `s03b-singularity.tex:178`、`s05b-grassmann-intersect.tex:42`、`:59` 共 3 处；其余 39 处作「靶空间」 | 统一为「靶空间」（GLOSSARY 强制项） |
| ③ | **扭曲手征**（twisted chiral） | `s03b-singularity.tex:142`（批注内）1 处；其余 29 处作「扭手征」 | 改为「扭手征超势」 |
| ④ | **拉氏量 / 拉格朗日量**（Lagrangian） | 拉氏量 13 处：s02a 3、s03c 5、s03d 1、s05b 1、s05c 1、s06a 2；拉格朗日量 15 处：s02b 7、s03a 1、s03b 5、s05a 1、s06b 1 | **按分片分裂**，择一统一：推荐「拉格朗日量」（正式；首次出现给英文 Lagrangian），或全书简作「拉氏量』。两式不可并存 |
| ⑤ | **局域 / 局部**（local / localization） | 「局域化」3 处（`s03d-twisted.tex:23–24` 及正文）vs 全书「局部」13 处 | 若保留「局域化」（localization 常用译名），建议在 s03d 首次出现处加括注并全书统一；否则改「局部化」 |
| ⑥ | **`\mathbf{C}` / `\mathbb{C}`** | 正文 3 处 `\mathbf{C}`：`s03d-twisted.tex:215`（`\mathbf{C}^*`）、`:240`、`:241`（`SL(2,\mathbf{C})`）；全书 `\mathbb{C}` 144 处 | 统一为 `\mathbb{C}`（`s04:7–8`、`s05a2:13`、`s06a:11` 仅是说明性批注） |

### 2.3 可接受／无需处理

- **相消 9 / 抵消 8**：表示「成对抵消」的「相消」可保留；但固定搭配「规范反常抵消」宜用「抵消」——`s02b-fieldtheory.tex:183`「规范反常在左右手之间相消」可改「抵消」，其余（s01:58、s03b、s03c、s03d、s06a、s06b）为一般「cancellation」，不改亦可。
- **翻转 3 / flop 10**：均出现在 `s05c-topology`，每处都带中文对译（「flop（翻转）」或「翻转（flop，…）」），符合 GLOSSARY「翻转（flop）」体例，不必强改。
- **破折号**：正文模型名统一 `--`（Calabi--Yau 100、Landau--Ginzburg 102、Fayet--Iliopoulos 16、Wess--Zumino 13）；`s07-references` 书目中 `Calabi-Yau`（10）、`Landau-Ginzburg`（8）、`Wess-Zumino`（1）为英文原题，按「书目逐字保留」体例保留，**非缺陷**。
- **批注内小项**（P3）：`s07-references.tex:23` 批注用 Unicode 破折号「Calabi–Yau」、`:18`「Landau–Ginzburg」，建议与正文统一为 `--`；`s07-references.tex:16` 批注「N=2 共形场论」2 处建议写 `$N=2$`。
- **`\mathbf{CP}`**：全书 147 处一致（原文字形即粗体 CP），无需改动。

### 2.4 误报排除（勿据此修改）

- 「零点模」（`s05b:46` 附近）：实为「矩映射零点模去 $U(k)$」的断词，不是 zero mode 的译名变体。
- 「束」（17 处）：均为「约束」等，不是 bundle 的另一种译法；bundle 一律作「丛」（38 处）。
- 「轨道」（32 处）：均为 orbit／「轨道空间」，与「轨形」（orbifold）不冲突。
- 「投影」（s04 一处）：为 projection map，不是 projective space。
- 「分解」（s06a/s06b 两处）：为 decompose，不是 resolution（resolution 统一作「消解」）。
- 「左右手」（2 处，s01/s02b）与「左行/右行」（各 23 处）分别对应 handedness 与 moving，用法正确。

---

## ③ 代码区残留英文正文

| 文件 | 判定 |
|---|---|
| 14 个正文分片（s01–s06b） | **0 处**英文正文句（已剔除注释、`\text{}`/`\mbox{}`/`\texttt{}` 内容与数学） |
| `s07-references.tex` | 53 条 `\bibitem` 全英文——按体例保留书目原貌（`main.tex` 译者说明已声明），**非缺陷** |
| `appendix-pagemap.tex` | 全中文，无英文残留 |

- 抽检两处「疑似」均为误报：`s01-intro.tex:68` 的 "change of topology"、"birational equivalence class" 是首次出现术语的英文括注；`s06a-superfields.tex:157` 是数学行（`\mathrm{h.c.}`、`\mathrm{d}`）。
- 建议：无需处理。

---

## ④ 脚注

### 4.1 原文脚注清单（PDF 自动检测，小字号 ⋆/† 标记）

| 原文页 | 标记 | 内容起头 | 译文承接分片 |
|---|---|---|---|
| p1 | ⋆ | Research supported in part by NSF Grant PHY92-45317 | `main.tex` 的 `\thanks` ✅ |
| p7 | ⋆ | All conventions will be those that follow by dimensional reduction… | s02a |
| p27 | ⋆ | This is in accord with the fact that for the A model… | s03b |
| p28 | † | Its definition is well-known and is given below. | s03b |
| p36 | ⋆ | Recall the Wick rotation… | s03d |
| p56 | ⋆ | The FC action on Z = V//H… | s05a |
| p59 | ⋆ | For r > 0. For r < 0… | s05b |
| p60 | † | Alternatively, the Grassmannian can be realized… | s05b |
| p65 | ⋆ | Apparently the relevant cases are precisely… | s05b |
| p75 | ⋆ | There have been previous discussions… | s06a |
| p80 | ⋆ | To put the θ expansion of Σ′… | s06a |
| p82 | ⋆ | All supermultiplets here will be (0,2)… | s06b |

正文脚注共 **11 条**（p7–p82），标题页另有 1 条。

### 4.2 译文脚注统计与对应

| 分片 | `\footnote` 数（行号） | 对应原文页 |
|---|---|---|
| `s02a-fieldtheory` | 1（146） | p7 |
| `s03b-singularity` | 2（170、184） | p27、p28 |
| `s03d-twisted` | 1（30） | p36 |
| `s05a-wps-toric` | 1（320） | p56 |
| `s05b-grassmann-intersect` | 3（38、42、158） | p59、p60、p65 |
| `s06a-superfields` | 2（33、203） | p75、p80 |
| `s06b-models` | 1（22） | p82 |
| 其余分片 | 0 | — |
| **合计** | **11** | = 原文正文 11 ✅ |

- **无缺失页、无多余、无错页**；p1 致谢脚注由 `main.tex:96` 的 `\thanks` 承担 ✅。
- 编号说明：译文脚注由 LaTeX 自动编号（1,2,…），原文用 ⋆/†，属预期差异（`main.tex` 译者说明已交代）。

### 4.3 易误判提示

5 个分片的头部/说明批注里出现 `\footnote` 字样（`s03b:9`、`s05a:15`、`s05b:14`、`s06a:13`、`s06b:11`），是说明文字，不是实际脚注；若用粗字符串计数会多算 5 条。以正文实际 `\footnote{...}` 为准。

---

## ⑤ 标题层级

### 5.1 分片标题清单（当前快照）

| 分片 | `\section` | `\subsection`（编号） | 无编号标题（层级：行号） |
|---|---|---|---|
| s01-intro | 引言 | — | — |
| s02a-fieldtheory | 场论背景 | — | `\subsection*`：扭手征超场；规范场强（203） |
| s02b-fieldtheory | — | — | `\subsection*`：拉格朗日量（19）、扭手征超势（118）、对称性（161） |
| s03a-model | Calabi--Yau 与 Landau--Ginzburg 的对应 | 模型（55） | — |
| s03b-singularity | — | “奇点”（20） | `\subsection*`：故事的寓意（16）；`\subsubsection*`：$\sum_iQ_i=0$ 的情形（88）、若 $\sum_iQ_i\neq0$（128）、寓意再探（188） |
| s03c-applications | — | 应用（25） | `\subsubsection*`：指标（68）、延拓到欧氏世界面；扭转（115） |
| s03d-twisted | — | 扭模型详述（18） | `\subsubsection*`：$B$ 模型（28）、$A$ 模型（37）、$r\ll0$（132）、$r\gg0$（174） |
| s04-geometry | 几何背景 | — | — |
| s05a-wps-toric | 推广 | 加权射影空间中的超曲面（66）、环面簇中的超曲面（145） | `\subsubsection*`：更一般的环面簇（287） |
| s05a2-comment | — | — | `\subsection*`：一点一般性评论（24）⚠ 见 5.4 |
| s05b-grassmann-intersect | — | 格拉斯曼流形中的超曲面（18）、超曲面的交（86） | `\subsubsection*`：一个例子（64）、超曲面交的 Landau--Ginzburg 模型（123） |
| s05c-topology | — | 拓扑的改变（26） | `\subsubsection*`：瞬子求和（130） |
| s06a-superfields | 向 $(0,2)$ 模型的推广 | $(0,2)$ 超场（31） | `\subsubsection*`：规范多重态（52）、手征多重态（94）、Fermi 多重态（115）、作用量中的其他项（147）、$(2,2)$ 多重态的约化（199） |
| s06b-models | — | 一些模型（16） | `\subsubsection*`：Landau--Ginzburg 相（69）、Calabi--Yau 相（84）、共形不变性？（133） |
| s07-references | —（`thebibliography` 自动生成「参考文献」标题） | — | — |
| appendix-pagemap | `\section*`：附录：原文页码—译文页码对照（6） | — | — |

### 5.2 与原文编号小节对照（11/11 一致）

| 原文页 | 原文标题 | 译文（分片） | 层级 |
|---|---|---|---|
| p17 | 3.1 The Model | 模型（s03a） | `\subsection` ✅ |
| p20 | 3.2 The “Singularity” | “奇点”（s03b） | `\subsection` ✅ |
| p29 | 3.3 Applications | 应用（s03c） | `\subsection` ✅ |
| p35 | 3.4 The Twisted Models In Detail | 扭模型详述（s03d） | `\subsection` ✅ |
| p50 | 5.1 Hypersurfaces In Weighted Projective Space | 加权射影空间中的超曲面（s05a） | `\subsection` ✅ |
| p52 | 5.2 Hypersurfaces In Toric Varieties | 环面簇中的超曲面（s05a） | `\subsection` ✅ |
| p58 | 5.3 Hypersurfaces in Grassmannians | 格拉斯曼流形中的超曲面（s05b） | `\subsection` ✅ |
| p62 | 5.4 Intersections Of Hypersurfaces | 超曲面的交（s05b） | `\subsection` ✅ |
| p66 | 5.5 Change Of Topology | 拓扑的改变（s05c） | `\subsection` ✅ |
| p75 | 6.1 (0,2) Superfields | $(0,2)$ 超场（s06a） | `\subsection` ✅ |
| p82 | 6.2 Some Models | 一些模型（s06b） | `\subsection` ✅ |

- §1、§4 原文无编号小节，译文亦无 ✅；§7 用 `thebibliography` 自动生成「参考文献」标题（`main.tex` 已设 `\refname`），未另加 `\section*`，合理 ✅。
- `\section` 共 6 个（§1–§6），各出现一次，LaTeX 自动编号 1–6，无重复/缺章。

### 5.3 原文无编号小标题对照（27/27）

| 原文页 | 原文标题 | 译文（层级） |
|---|---|---|
| p9 | Twisted Chiral Superfields; Gauge Field Strength | 扭手征超场；规范场强（`\subsection*`） |
| p10 | Lagrangians | 拉格朗日量（`\subsection*`） |
| p13 | Twisted Chiral Superpotential | 扭手征超势（`\subsection*`） |
| p14 | Symmetries | 对称性（`\subsection*`） |
| p20 | The Moral Of The Story | 故事的寓意（`\subsection*`） |
| p23 | The Case $\sum_iQ_i=0$ | $\sum_iQ_i=0$ 的情形（`\subsubsection*`） |
| p25 | What Happens If $\sum_iQ_i\neq0$ | 若 $\sum_iQ_i\neq0$（`\subsubsection*`） |
| p28 | The Moral, Revisited | 寓意再探（`\subsubsection*`） |
| p31 | Indices | 指标（`\subsubsection*`） |
| p33 | Continuation To Euclidean World-Sheet; Twisting | 延拓到欧氏世界面；扭转（`\subsubsection*`） |
| p36 | The B Model | $B$ 模型（`\subsubsection*`） |
| p36 | The A Model | $A$ 模型（`\subsubsection*`） |
| p38 | r << 0 | $r\ll0$（`\subsubsection*`） |
| p40 | r >> 0 | $r\gg0$（`\subsubsection*`） |
| p55 | More General Toric Varieties | 更一般的环面簇（`\subsubsection*`） |
| p58 | A General Comment | 一点一般性评论（`\subsection*`）⚠ |
| p61 | An Example | 一个例子（`\subsubsection*`） |
| p63 | Landau-Ginzburg Models For Intersections Of Hypersurfaces | 超曲面交的 Landau--Ginzburg 模型（`\subsubsection*`） |
| p71 | The Instanton Sum | 瞬子求和（`\subsubsection*`） |
| p76 | The Gauge Multiplet | 规范多重态（`\subsubsection*`） |
| p77 | The Chiral Multiplet | 手征多重态（`\subsubsection*`） |
| p78 | The Fermi Multiplet | Fermi 多重态（`\subsubsection*`） |
| p79 | Other Terms In The Action | 作用量中的其他项（`\subsubsection*`） |
| p80 | Reduction Of (2,2) Multiplets | $(2,2)$ 多重态的约化（`\subsubsection*`） |
| p84 | The Landau-Ginzburg Phase | Landau--Ginzburg 相（`\subsubsection*`） |
| p84 | The Calabi-Yau Phase | Calabi--Yau 相（`\subsubsection*`） |
| p86 | Conformal Invariance? | 共形不变性？（`\subsubsection*`） |

**无漏译、无多余小标题**（27 = 27）。

### 5.4 层级政策一致性

- 全稿实际执行的层级政策是：**直接隶属于 `\section` 的无编号标题 → `\subsection*`；隶属于编号 `\subsection` 的无编号标题 → `\subsubsection*`**（因为原文所有无编号标题视觉层级相同，译文按逻辑嵌套分层）。
- **26/27 符合该政策**；唯一偏差：`s05a2-comment.tex:24` 的「一点一般性评论」（原文 p58 "A General Comment"，位于 §5.2 内容之后）当前写作 `\subsection*`，而同类位置的 `s05a.tex:287`「更一般的环面簇」（p55，同属 §5.2 内）与 `s05b.tex:64`「一个例子」（p61，属 §5.3）均为 `\subsubsection*`。
  - 建议：改回 `\subsubsection*` 以与同类标题一致；若 Lead 有意把 "A General Comment" 提升为与 5.1/5.2 同级的小节标题，则需在 §5 全章统一该政策（当前状态属「局部不一致」，非内容错误）。
- 其余：`s05a2-comment` 与相邻分片（s05a 末句 → s05a2 首句、s05a2 末 → s05b 的 5.3）句中断句已由 `main.tex` 同行 `\frag` 拼接处理 ✅；`s03a` 末句与 `s03b` 首句同理 ✅。

---

## 附：未修改声明与建议优先级

- 本次审计**未修改任何分片**；以上全部为报告项。
- 建议修复优先级：
  - **P1（术语硬伤，改动极小）**：① `s01-intro.tex:50` 异常→反常；② `s03b:178`、`s05b:42`、`s05b:59` 目标空间→靶空间；③ `s03b:142` 扭曲手征→扭手征。
  - **P2（跨分片一致性）**：④ 拉氏量/拉格朗日量择一；⑤ 局域/局部统一；⑥ `s03d:215/240/241` 的 `\mathbf{C}`→`\mathbb{C}`。
  - **P3（批注与层级的小项）**：`s07:16/18/23` 批注内破折号与 `$N=2$`；`s05a2:24` 层级；`s02b:183` 相消→抵消（可选）。
