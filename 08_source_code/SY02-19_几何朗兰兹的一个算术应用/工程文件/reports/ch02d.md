# ch02d 施工报告（pp.12–16，§2.4–§2.5）

- **范围**：2.4.1–2.4.5、例 2.4.1.1/2.4.5.1、2.5.1–2.5.6、(2.5)–(2.7)、脚注 17–22。
- **编译**：exit 0，5 页，0 Overfull。
- **技术处理**：
  - 2.4.2 的 Frobenius 不动点笛卡尔图用 tikz-cd 重画（`\LS^{\arthm}\to\LS^{\restr}`、`\LS^{\restr}\xrightarrow{\Delta}\LS^{\restr}\times\LS^{\restr}`）。
  - `\qLisse^\phi` 与 `\LS^{\arthm}` 的拟紧性（[2] Thm 16.1.4）照译，不弱化“非形式”这一限定。
  - 2.5.2 的 shtuka 构造：`\Sht_{I,V}` 由 `\Graph_{\Frob}\times\mathrm{id}_{X^I}` 拉回、沿 `\Bun_G` 紧支撑推前；`I=\varnothing` 时 `\mathcal K_V=\Delta_!(\e_{\Bun_G})`，得 `C_{\et,c}(\Bun_G(\F_q))=\Aut^{\unr}_G`。
  - (2.6)(2.7) 与五步证明（Xue、Beilinson 谱投影、`\Sht^!`）逐符号对 p.15–16 核。
- **勘误/译注**：脚注 22 说明本文 `\Sht^!_I` 与 [4] 的 `\Sht` 记号不一致，照译并加注。
- **教训**：长文件改动前先 `wc -l`；本次一次 python 定位失误导致文件被截断，已整篇重写。
