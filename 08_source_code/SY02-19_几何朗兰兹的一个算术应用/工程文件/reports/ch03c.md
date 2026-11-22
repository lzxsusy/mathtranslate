# ch03c 施工报告（pp.21–22，§3.5）

- **范围**：p021 中部「3.5. Formulation of the main result」起，至 p022 中部「This result will be proved in §4.」止（§3.6 之前）。含 3.5.1、(3.9)(3.10)、Lemma 3.5.1.1（三项）、3.5.2、Theorem 3.5.2.1 与 (3.11)(3.12)、脚注 31。p021 顶部的 3.4.3 与 Prop 3.4.3.1 及「Indeed, this follows…§3.2.6」一句属 §3.4，已在 `ch03b.tex`，本块未重复译（与 `reports/ch03b.md` 的边界声明一致）。
- **内容摘要**：§3.5 处理 $\Eisspec$ 的局部化版本。3.5.1 设给定交换图 $\LS^{\arthm}_{\bB}\to\LS^{\arthm}_{\bG},\LS^{\arthm}_{\bT}\to\A^1$（$\bG$ 侧标 $f$、$\bT$ 侧标 $g$，二者在 $\LS^{\arthm}_{\bB}$ 上一致），令 $\mathring{\A}^1=\A^1\setminus 0$，把 $\Gamma(\LS^{\arthm}_{\bG},\omega)[f^{-1}]$ 写成 $\colim_{f\cdot-}$ 并识别为 $\Gamma(\LS^{\arthm}_{\bG}\times_{\A^1}\mathring{\A}^1,\omega)$。由底变换得到的对应 (3.9)（左腿紧合且可表、右腿最终余连通且 1-可表）给出典范映射 (3.10) $\Gamma(\LS^{\arthm}_{\bT},\omega)[g^{-1}]\to\Gamma(\LS^{\arthm}_{\bG},\omega)[f^{-1}]$；Lemma 3.5.1.1 记三条性质：与乘 $f$、$g$ 算子相容（即 $\e[t]$-模态射）、(3.10) 等于在 $\e[t]$ 上张量 $\e[t,t^{-1}]$、以及原映射与 (3.10) 构成交换方块。3.5.2 陈述主定理 3.5.2.1：存在 $\delta_{\bG}\in\Om^{\infty}\Gamma(\LS^{\arthm}_{\bG},\OO)$、$\delta_{\bT}\in\Om^{\infty}\Gamma(\LS^{\arthm}_{\bT},\OO)$ 填入 (3.11)，且 (1) $\delta_{\bG}$ 在平凡 Weil 局部系统处非零；(2) $\Gamma(\LS^{\arthm}_{\bG},\omega)[\delta_{\bG}^{-1}]$ 位于上同调次数 0（$\bT$ 同理）；(3) (3.12) 的 $\Eisspec$ 是 $\Vect^{\heartsuit}$ 中的满射。
- **编译**：`test_ch03c.tex`（`test_ch00.tex` 复制后 `chunks/ch00`→`chunks/ch03c`），xelatex exit 0，**2 页**，0 Overfull，0 Underfull，0 Missing character。
- **技术处理**：
  - 图表全部用 tikz-cd 重画，逐符号对页面图核：首图三点菱形（$f$、$g$ 标在箭头下方，用 `"f"{below}`/`"g"{below}`，不用 `'`，否则撇号会印进标签）；(3.9) 三个底变换对象写作 $\LS^{\arthm}_{\bX}\times_{\A^1}\mathring{\A}^1$；(3.11) 中 $\delta_{\bG}$、$\delta_{\bT}$ 分居左右两箭头的内下侧；Lemma 3.5.1.1 (3) 的方块图横箭头上标 $\Eisspec$ 与 (3.10)。
  - 「编号段落」用 `\pnum`（3.5.1、3.5.2）；Lemma 与 Theorem 用 `lem`/`thm` 环境，不手写编号；脚注 31 原样保留在 (2) 的「上同调次数 $0$」之后。
  - 单块文件以 `\subsection` 开头（沿用 ch03b 惯例，不重复 `\section`），故单块编译显示「0.1」节号与 (0.1)–(0.4) 公式号；合成到 main 后为 3.5 与 (3.9)–(3.12)。
  - 数学记号的定名与原文一致：$\Om^{\infty}\Gamma(\LS^{\arthm}_{\bG},\OO)$、$\Vect^{\heartsuit}$、$\colim_{f\cdot-}$、$\e[t,t^{-1}]$；原文「$\A^1\setminus 0$」中的 $0$ 未加粗，照录。
- **译注（0 条）**：本块未加 `\zy` 译注（原文无需要向读者交代的隐含约定；$\mathring{\A}^1$、$\e[t]$-模、$\Vect^{\heartsuit}$ 等均在正文中已由原文自身说明）。
- **原文缺陷/疑难**：
  1. `% [Tutor Note]` 1 条：p021「with left arrow proper and representable」——`proper` 按 `glossary.tsv` 的分配由 ch03a 首次括注「紧合的（proper）」，本块只写「紧合」，已在行末注明，避免两处重复括注。
  2. 原文 (3.9) 的对应图与 (3.10) 的方向易误读：左腿（指向 $\LS^{\arthm}_{\bG}$）才是紧合腿，右腿（指向 $\LS^{\arthm}_{\bT}$）是最终余连通腿；据此 (3.10) 只能由「沿右腿拉回、沿左腿推前」得到，方向才是 $\Gamma(\LS_{\bT})\to\Gamma(\LS_{\bG})$。已照此理解核对，图与公式均照原文排印，未改动。
  3. 原文 3.5.1 末句「and similarly for $(\check T,g)$ or $(\check B, f|_{\LS^{\arthm}_{\check B}} = g|_{\LS^{\arthm}_{\check B}})$ in place of $(\check G,f)$」中的 $\check B$ 上标为 $\arthm$（不是 $\restr$），与 (3.9) 用 $\arthm$ 一致，照录。
  4. 原文 (3.12) 把 $\Eisspec$ 直接写成 $\Vect^{\heartsuit}$ 中的对象（而非「映射的靶」），中文照录为「映射 … $\in\Vect^{\heartsuit}$ 是满射」，语义上以原文为准。
- **遗留**：本块与 ch03b 在 p021 交界处无重复、无缺漏；与 ch03d 的分界为 p022 的「3.6. Proof of Theorem A」标题。若合成后 (3.9)–(3.12) 编号与硬编码引用不符，需在 main 中确认 §3 为第 3 节、且 ch03a/ch03b 提供的 `\subsection` 数恰为 4（3.1–3.4）。
