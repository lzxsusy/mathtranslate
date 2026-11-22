# ch03b 施工报告（pp.19–21，§3.3 + §3.4）

- **范围**：p019 末至 p021 上半。起点为 p020 首「3.3. Spectral Eisenstein series」，终点为 Prop 3.4.3.1 之后一句「Indeed, this follows from the realizations of ps-Eis and $\Eisspec$ via traces, see (3.2) and §3.2.6.」，即 §3.5 之前。含 3.3.1、Def 3.3.1.1、3.4.1–3.4.3、(3.7)(3.8)、Prop 3.4.2.1、Prop 3.4.3.1、脚注 30。p021 的「3.5. Formulation of the main result」、3.5.1、(3.9)(3.10) 与 Lemma 3.5.1.1 属 ch03c，本块未译。
- **内容摘要**：§3.3：由对应 $\LS^{\restr}_{\bB}\xrightarrow{q}\LS^{\restr}_{\bT}$、$\LS^{\restr}_{\bB}\xrightarrow{p}\LS^{\restr}_{\bG}$（$p$ 可表紧合、$q$ 拟光滑 1-可表，二者缠绕 Frobenius）用 (3.3)(3.4) 得 $\Gamma(\LS^{\arthm}_{\bT})\to\Gamma(\LS^{\arthm}_{\bB})\to\Gamma(\LS^{\arthm}_{\bG})$，其复合定义为谱 Eisenstein 级数（Def 3.3.1.1）。§3.4.1：回忆受限几何朗兰兹（猜想 2.3.1）预测的等价 (3.7)，并列出 Hecke 相容性与 Eisenstein 相容性（$P=B$）两条，后者给出方块图表交换（左侧竖直箭头为 [2] 例 21.2.9 的无条件等价）。§3.4.2：Prop 3.4.2.1 给出缩并条件下 $\tr_{\IndCoh_{\mathcal{N}}}(\phi^!)\xrightarrow{\sim}\tr_{\IndCoh}(\phi^!)$ 的同构，由此得 (3.8) $\Aut^{\unr}_{G,c}\simeq\Gamma(\LS^{\arthm}_{\bG},\omega)$，并在 Hecke 相容下升级为 $\Exc_{\bG}$-模之间的等价。§3.4.3：Prop 3.4.3.1 断言 ps-Eis 与 $\Eisspec$ 在 (3.8) 下相容。
- **编译**：`test_ch03b.tex`（由 `test_ch00.tex` 复制、`chunks/ch00`→`chunks/ch03b`），xelatex exit 0，2 页，0 Overfull，0 Underfull。
- **技术处理**：
  - 三个图表（§3.3 的对应菱形、Eisenstein 相容性方块、Prop 3.4.3.1 方块）用 tikz-cd 重画；箭头方向、$q$/$p$ 的位置、方块的 $\cong$ 与「左侧竖直箭头」的指认均对页面图核。
  - (3.7)(3.8) 逐符号核：$\IndCoh_{\Nilp^{\mathrm{spec}}}$（Nilp 斜体、spec 正体）、$\Shv_{\Nilp}(\Bun_G)$、$\Exc_{\bG}$、$\Aut^{\unr}_{G,c}$ 与 $\Aut^{\unr}_{c}$ 的两种写法照原文。
  - 编号段用 `\pnum`/`\pnumt`（3.3.1、3.4.1、3.4.2、3.4.3）；Def 3.3.1.1、Prop 3.4.2.1、Prop 3.4.3.1 用环境，不手写编号；脚注 30 原样保留。
  - 单块文件以 `\subsection` 开头（沿用 ch02b 惯例，不重复 `\section`），故单块编译时出现「0.1/0.2」节号与 (0.1)(0.2) 公式号；合成到 main 后为 3.3/3.4 与 (3.7)(3.8)。
- **译注（1 条）**：$P=B$ 指抛物子群取为 Borel 子群，即极小抛物情形，`\zy{...}`，[来源：A/原文 §3.4.1 括注「$P = B$ case」]。
- **原文缺陷/疑难**：本块未发现需要 `% [Tutor Note]` 的原文错误。可疑但照译之处：p020「We highlight two of salient interest here」措辞略拗（按「其中两个特别值得注意的」译）；p020「contracting onto $0$」按「收缩到 $0$」译；(3.8) 后「this is an equivalence of $\Exc_{\bG}$-modules」中的 equivalence 按「等价」保留（源文本沿用范畴语言）；「restricted geometric Langlands」首次出现处括注英文，并与 glossary 的「受限变差」（restricted variation）保持「受限」一致。
- **遗留**：本块与 ch03a 在 p019/p020 交界处无重复；若合成后 (3.7)(3.8) 编号与硬编码引用不符，需在 main 中确认 §3 为第 3 节。
