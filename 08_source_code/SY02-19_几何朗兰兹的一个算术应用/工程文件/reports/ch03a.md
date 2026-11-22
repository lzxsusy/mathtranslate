# ch03a 施工报告（pp.16–19，§3 引言 + §3.1 + §3.2）

- **范围**：原文 p016 的「3. Spectral Eisenstein series」标题起，至 p019 末（Remark 3.2.6.1 结束）。含 §3 导言（$k=\Fb$ 的约定、$\Eisspec$ 的目标）、3.1.1–3.1.3（$\Eis_!$、ps-Eis、(3.1)(3.2) 与 Prop 3.1.1.1）、3.2.1–3.2.6（QCA/ind-QCA 术语、(3.3) proper 推前、(3.4) 最终余连通拉回、(3.5)(3.6) 显式构造、3.2.5 范畴迹框架、3.2.6 复原）、Remark 3.2.3.1 / 3.2.4.1 / 3.2.6.1、脚注 22–29。p016 上半（(2.7) 与 §2.5 末段）属 ch02d，未重译。
- **内容摘要**：先定义 $\Eis_!:\Shv(\Bun_T)\to\Shv(\Bun_G)$（$*$-拉回 + $!$-推前），并援引 [6] 的 Hecke 性质与 [2] 定理 14.4.3 得 Prop 3.1.1.1：$\qLisse(\Bun_T)\to\Shv_{\Nilp}(\Bun_G)$；再定义 ps-Eis 为「限制 + 沿纤维求和」，用 [4] 主定理得 (3.1)，并说明 (3.2) 交换（几何 Eisenstein 级数的迹 = 伪 Eisenstein 级数）。§3.2 在一般叠论框架下构造 $\phi$-不动点叠之间的映射：$f$ 可表紧合时用 $f^{\phi,\IndCoh}_*\dashv f^{\phi,!}$ 得 (3.3)，$f$ 最终余连通时经 (3.5)(3.6) 与基变换得 (3.4)，再用 3.2.5 的范畴迹函子性统一解释（3.2.6）。
- **编译**：`test_ch03a.tex`（由 `test_ch00.tex` 复制、`chunks/ch00`→`chunks/ch03a`），xelatex exit 0，5 页，0 Overfull，0 Underfull。
- **技术处理**：
  - (3.2) 交换方块、(3.5)(3.6) 前的 Cartesian 方块（$\mathcal{Y}\to\mathcal{Y}\times\mathcal{Z}$ 等）与 p019 两个基变换方块一律用 tikz-cd 重画，不截图。
  - (3.1)(3.3)(3.4)(3.5)(3.6) 逐符号对页面图核；$f^{!,\IndCoh}$、$\mathrm{Graph}^{\IndCoh}_{\phi_{\mathcal{Z}}\circ f,*}$、$\Delta^!_{\mathcal{Y}}$、$\varpi^{\IndCoh}_{\mathcal{Z},*}$ 等上下标照原文排。
  - 编号段用 `\pnum`/`\pnumt`；Prop 3.1.1.1 与三条 Remark 用环境，不手写编号；脚注 22–26 原样保留（中文）。
  - 单块编译时公式标签为 (1.1)–(1.6)，全书中为 (3.1)–(3.6)；正文对 (3.x) 的引用按原文硬编码，合成后一致（与 ch02a 报告同一处理）。
- **译注（1 条）**：QCA = quasi-compact with affine diagonal 的缩写，`\zy{...}`，[来源：A/原文 §3.2.1 及所引 [8]]。
- **原文缺陷（已保留 + `% [Tutor Note]` + 登记）**：p018「Let $\varpi_{\mathcal{Y}}$ denote the canonical map $\mathcal{Y}^\phi\to\mathcal{Y}$ sending a pair $(y\in\mathcal{Y},\,y\simeq\phi_{\mathcal{Z}}(y))$ to $y$」——$\mathcal{Y}^\phi$ 由 $\phi_{\mathcal{Y}}$ 定义，且同段其余公式均作 $\phi_{\mathcal{Y}}$，故 $\phi_{\mathcal{Z}}$ 应为 $\phi_{\mathcal{Y}}$ 之笔误；译文照原文保留并在行末加注释。
- **疑难/取舍**：「ind-QCA assumption is overkill」译「过强」（非「过分」）；「loc. cit.」统一译「前引文献」；「(even in its formulation)」译「（甚至其表述本身）」；「good theory of pushforwards」译「良好的推前理论」；「appear more concrete」译「看到构造的具体样子」。
