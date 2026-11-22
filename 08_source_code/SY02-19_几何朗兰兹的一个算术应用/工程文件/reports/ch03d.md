# ch03d 施工报告（pp.22–25，§3.6 + §3.7）

- **范围**：p022 下半页「3.6. Proof of Theorem A」起，至 p025 上部 Corollary 3.7.2.1 末句「is a surjection.」止（其后 §4「Grothendieck–Springer theory for $\LS^{\arthm}$」属 ch04a）。含 §3.6 全部（3.6.1–3.6.3、Warning 3.6.1.1、(3.13)、脚注 32–35）与 §3.7 全部（3.7.1「Analogies」、(3.14)、(3.15)、Lemma 3.7.1.1 及证明（(3.16)）、Remark 3.7.1.2、3.7.2、Corollary 3.7.2.1、脚注 36）。p022 上半页的定理 3.5.2.1 归 ch03c。
- **内容摘要**：§3.6 由定理 3.5.2.1 推定理 A。3.6.1 给出 Langlands 参数的显式含义：$\sigma$ 为 $\LS^{\arthm}_{\bG}$ 的 $\e$-点，$\mathrm{ev}_\sigma:\Exc_{\bG}\to\e$、极大理想 $\mathfrak m_\sigma\subseteq H^0(\Exc)$，据此定义 $\mathfrak m_\sigma$-挠部分 $\Aut^{\unr}_{G,c,[\sigma]}$ 及其尖部分。Warning 3.6.1.1：$\Aut^{\unr}_{G,\cusp}$ 有限维，故按 $\sigma/\!\sim$ 分解为直和 (3.13)；但紧支撑自守函数没有这样的分解。3.6.2 由 $\mathrm{ps}\text{-}\Eis(\Aut^{\unr}_{T,c})\cap\Aut^{\unr}_{G,\cusp}=0$ 把目标归约为：证明 $\Aut^{\unr}_{G,c,[\triv]}$ 含于 $\mathrm{ps}\text{-}\Eis$ 的像。3.6.3 反转 $\delta_{\bG}$ 的作用，得满射 $\mathrm{ps}\text{-}\Eis:\Aut^{\unr}_{T,c}[\delta_{\bT}^{-1}]\to\Aut^{\unr}_{G,c}[\delta_{\bG}^{-1}]$，故 $\delta_{\bG}^n\cdot\psi=\mathrm{ps}\text{-}\Eis(\psi_0)$；再由 $\lambda=\delta_{\bG}(\triv)\ne 0$、$(\delta_{\bG}-\lambda)^m\cdot\psi=0$ 与 Bezout 多项式 $q(t)t^n\equiv 1 \bmod (t-\lambda)^m$ 得 $\mathrm{ps}\text{-}\Eis(q(\delta_{\bT})\cdot\psi_0)=\psi$。§3.7 给出定理 3.5.2.1 的玩具模型：把 $\LS^{\restr}$ 图换成 (3.14) 的 $B\check B/B\check T/B\check G$，取恒等自同态的不动点得 $\check H^{\mathrm{ad}}/\check H$ 的图（$\check H^{\mathrm{ad}}/\check H\simeq(\mathbf B\check H)^{S^1}$，$\OO\to\omega$ 同构），于是 (3.15) 给出 $\Eissoyt$；Lemma 3.7.1.1 断言两端集中在上同调次数 0 且 $\Eissoyt$ 满，证明用 $\Rep(\check T)=\bigoplus_{\lambda\in\bar\Lambda}\Vect$、$\Rep(\check G)=\bigoplus_{\lambda\in\bar\Lambda^+}\Vect$ 与 Borel–Weil–Bott（(3.16)）；3.7.2 用 $\check T/\!/W=\Spec(\e[\bar\Lambda]^W)$ 说明这是 $\mathrm{Fun}(\check T/\!/W)$-模的满态射，得 Corollary 3.7.2.1：局部化后仍满射。
- **编译**：`test_ch03d.tex`（`test_ch00.tex` 复制后 `chunks/ch00`→`chunks/ch03d`），xelatex exit 0，**4 页**，0 Overfull，0 Underfull，0 Missing character。
- **技术处理**：
  - 编号段用 `\pnum`/`\pnumt`（3.6.1、3.6.2、3.6.3、3.7.1「类比。」、3.7.2）；`lem`/`remark`/`cor`/`warning` 用环境，不手写编号；脚注 32–36 全部保留（32 在「半单的」后，33 在「有限维的」后，34 在「回忆」后，35 在「给定」后，36 在「我们提醒」后）。
  - 图表用 tikz-cd 重画并逐符号核：3.7.1 的 $\LS^{\restr}$ 菱形（$q$ 在左腿、$p$ 在右腿，均标在箭头上方）、(3.14) 的 $\mathbf B\check B$/$\mathbf B\check T$/$\mathbf B\check G$、不动点图 $\check B^{\mathrm{ad}}/\check B$ 等三点菱形、3.7.2 的四点大方图（下排两箭头汇到 $\check T/\!/W$）。
  - (3.16) 用 `aligned` 排两行、$\simeq$ 对齐，共享一个编号；$\tr_{\Rep(\check T)}(\id)$、$\ell^{w_0(\bar\lambda)}$、$\Rep(\check T)^{\vee}$ 等逐符号对页面图核。$\check T/\!/W$ 统一用 `\check T/\!/W`。
  - 单块文件以 `\subsection` 开头，故单块编译显示「0.1/0.2」节号与 (0.1)–(0.4) 公式号；合成到 main 后为 3.6/3.7 与 (3.13)–(3.16)。
- **译注（0 条，`% [Tutor Note]` 2 条）**：
  1. p022 末「We remind that we have assumed $G$ is semi-simple.³² here.」——原文在脚注标记之后残留 `here.`，语序不通，疑为编辑残留；译文把 `here` 的含义并入「此处提醒」，并在行末注明。
  2. p024「sends $\ell^{w_0(\bar\lambda)}$ … to $V^{\lambda}$ …(the representation with highest weight $\lambda$)」——原文在此处 $V$ 的上标与「highest weight」均**不带**横线（$\lambda$），而本段其余处处为 $\bar\lambda\in\bar\Lambda$；译文照录原文（$V^{\lambda}$、最高权 $\lambda$），并在行末注明不一致。
- **原文缺陷/疑难**：
  1. 上述两条 `% [Tutor Note]`。
  2. (3.16) 右端的括号：(3.16) 第一行写作 $\bigoplus_{\lambda\in\bar\Lambda}k\simeq\tr_{\Rep(\check T)}(\id)\,(\simeq\Gamma(\cdots))$，第二个 $\simeq$ 在括号内，与 Lemma 3.7.1.1 的「两端集中于次数 0」相呼应；照原文排印，未把括号内的同构提升为主断言。
  3. Warning 3.6.1.1 后的括注（关于等价关系 $\sim$ 与 [22] Prop 0.38）在原排版中紧随 (3.13)，语义上仍属该 Warning 的说明；译文把括注放在 `warning` 环境内部、公式之后，以保持行文连贯（原文视线上的缩进亦如此）。
  4. 3.7.1 中「$\check B^{\mathrm{ad}}/\check B$」这类记号原文把 `ad` 排在斜线上方（$\check B^{\mathrm{ad}}\!/\check B$）；译文用上标 `^{\mathrm{ad}}` 表示，全块统一。
  5. 「Here for an algebraic group $H$, $H^{\mathrm{ad}}/H$ denotes the (stack) quotient of $H$ acting on itself by conjugation」中的 $H$ 是与 $\check B,\check T,\check G$ 无关的一般代数群，译文保留 $H$ 不换成 $\check H$。
- **遗留**：与 ch03c 的分界为 p022 的 §3.6 标题（ch03c 止于「该结果将在 §4 中证明。」），与 ch04a 的分界为 p025 的 §4 标题，均无重复、无缺漏。合成后请确认 (3.13)–(3.16) 与正文硬编码引用（3.13、3.14、3.15、3.16）一致；另需注意 `\check T/\!/W` 与 ch04 起 Borel 记号的衔接。
