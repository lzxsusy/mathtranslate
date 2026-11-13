# 核验报告 · ch04d（原书 p.176–186）

核验人：译者己　　作者：译者戊　　日期：2026-11-09

## 结论
需修改（2 条必须改：一条是 Example 4 的边界与 □ 位置，一条是两处原书笔误被悄悄改正；另有 3 条建议改）

## 必须改（影响正确性）

1. **Example 4 的范围与 □ 位置错**（→ ch04d.tex 第 44 行）。
   原书 p.177 开头是 Example 4（全纯函数 $g$、$\mathrm{Re}\,g$ 是临界点指标都为 $n$ 的 Morse 函数、超平面截面 $W^{n-1}$、包含同态 $H_j(W^{n-1})\to H_j(M^n)$ 在 $j<n-1$ 同构、$j=n-1$ 满射），但**例 4 并未在 p.177 结束**：p.178 整页仍在例 4 之内，依次讲 Lefschetz 的射影簇同调论（「将在综览复代数几何的相应卷册中详细考察」）、亚纯映射 $f:M^n\to\CP^1\cong S^2$ 的消失闭链与单值性、Leray 层 $\mathcal F_U=H_*(g^{-1}(U))$、Picard–Lefschetz 理论，最后以「……只是严格的证明稍后才给出。$\square$」收尾。
   现状：第 44 行 `\end{example}` 把例 4 在第 42 行的「当 $j=n-1$ 时为满射。」处关闭，于是
   - 自动印出的 $\square$ 落在 p.177 的「满射。」之后，**而原书 p.177 此处没有 $\square$**；
   - 原书 p.178 末真正有 $\square$ 的位置反而没有 $\square$；
   - p.178 的三段散文被排成例外的正文，读者无法判断它们属于例 4（原书的缩进与 □ 表明它们是例 4 的内容）。
   改法：把 `\end{example}` 从第 44 行移到第 65 行（p.178 末段「……只是严格的证明稍后才给出。」之后），第 43 行的 Tutor Note 留在环境内；`% [原文 p.178]`（第 46 行）保持在环境内、紧接在例 4 的第二段之前（段落边界，符合页标记规则）。改完 `check_chunk.py` 的陈述数不变（仍 4 个 example），只是 □ 落位正确。

2. **两处原书笔误被悄悄改正，未按「照排 + 批注」处理**（→ ch04d.tex 第 65 行、第 135 行）。
   - 第 65 行「区域 $g^{-1}(U)$ 可缩到单一纤维上」：原书 p.178 印作 `region $p^{-1}(U)$`（该段中的映射是 $g$，$p$ 是下一段才出现的纤维丛投影，故原书显系笔误）。
   - 第 135 行「利用 $\Lambda^k$（$k\ge0$）的截面只要求为 $C^\infty$ 类」：原书 p.180 印作 `sections of $\Lambda^k$ ($h\ge0$)`（$h$ 与本段无关，按上下文应为 $k$）。
   项目规则是**照原书排印 + Tutor Note 说明疑为笔误及正确形式**（我在 ch04g 也是这么处理的），不能悄悄改成正确形式——否则核验与读者都无从知道底本此处印错。建议改回原书形式并各加一条批注：「原书 p.178 作 $p^{-1}(U)$…疑为笔误，正确应为 $g^{-1}(U)$」「原书 p.180 作 $h\ge0$…疑为笔误，正确应为 $k\ge0$」。

## 建议改（可读性/版式/体例）

1. **「Hermite 度量」与「Hermitian 度量」混用**（→ ch04d.tex 第 252 行）。同一位译者（或同一章）在 ch04c 里用的是「Hermitian 度量」，本块第 252 行作「Hermite 度量」，建议全书统一为「Hermitian 度量」（或按 glossary 若已有条目则从 glossary）。
2. **(2.34)、(2.35) 缺原书的列举标号「1)」「2)」**（→ ch04d.tex 第 330–338 行）。原书 p.186 把两个变分问题排成 `1) S{γ}=…`、`2) S(γ)=…`，正文先说「边界条件分下列两种类型之一」，译文中标号消失，靠「；」和「即」承接，读者要自己数。建议在两条公式前补 `1)`、`2)`（可写成 `\text{1)}\quad` 置于公式内，或行首加标号）。
3. **`% [原文 p.179]` 标记位置过早**（→ ch04d.tex 第 67 行）。核对页图：Cartan 那一段其实**起于 p.178 页末**（原书 p.178 最后五行是 `A completely different approach, via tensors … Particular important types of 1-forms and 2-forms, together`），p.179 是从这个词组的后半句 `with some of their deeper topological …` 接续的（页图 p186 顶端可证）。现在第 67 行把整段算在 p.179 名下。因原书断页落在句中，按项目规则页标记应落到最近的句界——即该段第一句（「……然而完整的系统理论归功于 Cartan。」）之后。建议把第 67 行移到那一句之后；`audit_pagemarks.py` 不会报这类错，但它影响「每页起始」的页码归属。

## 抽查记录（逐页）

- **p.176**（`pages\p183.png`）：开头承接 ch04c 末段，(2.13) Morse 不等式的一般形式 $\sum_\alpha b_{i-\lambda_\alpha}(W^k_\alpha)\ge b_i(M^n)$（含临界子流形 $W^k_\alpha$、法丛 $\nu^{\lambda_\alpha}$ 可定向性、相对闭链的最速下降解释）与页图一致；Example 1（2 个临界点的 Morse 函数刻画球面、Reeb 的球面刻画、Smale–Wallace 与 Milnor 的 $S^7$ 例）、Example 2（$h$-配边与 Smale 的 $h$-配边定理）、Example 3 前半（闭曲面分类、Novikov 的任意单连通流形分类路线）——逐句与页图一致；Example 3 续到 p.177（3 维流形的 Heegaard 分解），`% [原文 p.177]` 落在例 3 内部的段落边界，符合页标记规则。
- **p.177**（`p184.png`）：Example 4 开头（一般位置全纯函数、$\mathrm{Re}\,g$ 的临界点指标全为 $n$、仿射部分上的 Morse 函数、$K\to M^n$ 可同伦到超平面截面、包含同态 $H_j(W^{n-1})\to H_j(M^n)$ 在 $j<n-1$ 同构 / $j=n-1$ 满射）逐句一致；□ 位置问题见必须改 1。
- **p.178**（`p185.png`）：Lefschetz 同调论综述、亚纯映射 $f:M^n\to\CP^1\cong S^2$、消失闭链 $z_0\in H_{n-1}(F_\eps)$、单值性 $A_j=1\ (j\ne n-1)$ 与 $A_{n-1}(z)=z\pm(z_0\cdot z)z_0$、Leray 层 $\mathcal F_U=H_*(g^{-1}(U))$、Picard–Lefschetz——内容与页图一致；原书 $p^{-1}(U)$ 的笔误及其处理见必须改 2。
- **p.179**（`p186.png`）：页首是 p.178 未竟之句的后半（`with some of their deeper topological and algebraic-topological properties …`），其后为微分形式复形 $\Lambda^*(M^n)$ 与 $\Omega_k=\sum_{j_1<\cdots<j_k}T_{j_1\cdots j_k}dx^{j_1}_\alpha\wedge\cdots\wedge dx^{j_k}_\alpha$、外微分反对称性 (2.14)、de Rham 复形 (2.15)；Poincaré 与自守形式、Cartan 系统理论的历史评述——内容与页图一致，页标记归属问题见建议改 3。
- **p.180**（`p187.png`）：左不变形式与李群李代数（(2.16)(2.17) 的 $\mathfrak g'_0,\mathfrak g'_1$）、正合列 (2.18)、谱序列与超渡 (2.19)、$H^j(\Lambda^k)=0\ (j>0)$ (2.20)——5 个 tag 与页图逐符号一致；$\Lambda^k$（$h\ge0$）笔误见必须改 2。
- **p.181**（`p188.png`）：(2.21)(2.22) 的谱序列收敛与 $H^{k+1}(Z^0)\cong H^{k+1}(M^n;\R)$（de Rham 定理的这条证明链完整，$(2.18)\to(2.19)\to(2.20)\to(2.21)(2.22)$ 无断环）——一致。
- **p.182**（`p189.png`）：Hodge 内积 $\langle\omega,\omega'\rangle=\int_{M^n}\omega\wedge*\omega'$ (2.23)、$*$ 与 $d,\delta$ 的关系——一致。
- **p.183**（`p190.png`）：Hodge 分解 (2.24) 与调和形式 (2.25)、Singer 的解析挠率公式 (2.26) $2\log|R(K,\rho)|=\sum_q q(-1)^q\log\det\Delta|_{C_q(K;\rho)}$——三处逐符号一致；注 p.183 脚注 1（Schwarz 1980、Witten、拓扑量子场论）与页图一致。
- **p.184**（`p191.png`）：$(p,q)$ 型分解 (2.27)、$\Lambda^{p,q}$ 的局部表达式 (2.28)、$\bar d_c,\bar\delta_c$ 与 Kähler 恒等式 (2.29)–(2.31)——一致。原书 (2.27) 右端求和指标印作 $p+q=n$（按左侧 $\Lambda^k$ 应为 $p+q=k$）、(2.31) 印作 $\Delta_c=\Delta_c$（按上文应为 $\bar\Delta_c=\Delta_c$），译者均照原书排印并在 Tutor Note 指出正确形式，**处理正确**，不必改。
- **p.185**（`p192.png`）：Hodge 分解 (2.32)、(2.33) 代数闭链的基本类 $D[N^{n-k}]\in H^{k,k}(M^n;\C)\cap H^{2k}(M^n;\Z)$、Lefschetz 的 $k=1$ 情形与 Thom 的 $k>1$ 障碍、Hironaka、Grothendieck 的 étale 同调与 mod $p$ 类比——一致；跨页句「用代数闭链的有理线性组合实现」在本块内收束，未见断句。
- **p.186**（`p193.png`）：$k=1$ 的 Lefschetz 强形式、Thom 的障碍、Hironaka、Grothendieck 同调论与 Weil–Tate 纲领的评述、变分问题 (2.34)(2.35)——公式与页图一致，标号缺失见建议改 2。

## 体例抽查
- 页标记：`% [原文 p.176]`…`p.186]` 共 11 条，递增无重复；`python work\tools\audit_pagemarks.py` 通过（无句中插标）。
- 编号公式：(2.13)–(2.35) 共 23 个，连续、无自造、无重号；正文引用（式 (2.13)、式 (2.27) 等）为纯文本，未用 `\ref`。
- 陈述环境：`example{1}`–`example{4}` 共 4 个（原书均有 □，用无星版正确）；check_chunk 提示「编号为空」不适用（本块编号齐全）；例 4 的边界见必须改 1。
- Tutor Note：6 条（11 页，要求 ≥3）；内容均属易错预警或省略论证点拨，无空话。
- 末行 `% CHUNK ch04d DONE` ✓；`python work\check_chunk.py src\chunks\ch04d.tex` → OK，0 error。
