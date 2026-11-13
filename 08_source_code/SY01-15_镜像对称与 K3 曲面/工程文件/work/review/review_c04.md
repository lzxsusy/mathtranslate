# 交叉校对报告：c04（reviewer = jp11-c03）

- 被校文件：`src/chunks/c04.tex`（jp11-c04 译，155 行）
- 范围：PDF p008–p010（原书 p.134–136），§5 二次栈 + §6 开头；编号公式 14 条 (5.1)–(5.13)、(6.1)
- 方法：通读 c04.tex；逐段对照 `work/split/p008.txt`–`p010.txt` 查漏译/增译；14 条公式逐条对照 `work/pages/p008.png`–`p010.png`（150 dpi 通读 + 300/400/500 dpi 裁图核对箭头、标签、上下标、括号、下划线、连等、上下限）；术语对照 `work/glossary.tsv`；哥特体强调逐处对照原图。
- 只读复核：`python check.py c04` → **ALL CHECKS PASSED**（tags=14，5.1..6.1；section 5: 1–13，section 6: 1）。本报告未改动 c04.tex 及任何工程文件。

## 逐条公式核对表

| 公式 | 原书页/行号 (c04.tex) | 核对要点 | 结果 |
|---|---|---|---|
| (5.1) | p.134 / 15 | 箭头标签 $\beta$（正文却称 $P$）、$\check N$、$\mathbb{L}$ | ✓（$\beta$ 在箭头上；P/β 不一致已加 Tutor Note，见下） |
| (5.2) | p.134 / 23 | $\tilde\beta$ 在箭头上、$\check N\oplus\mathbb{Z}$ | ✓ |
| (5.3) | p.134 / 27 | 首坐标 $-c_1^{(p)}-\cdots-c_{n+r}^{(p)}$ 的负号与省略号 | ✓（逐符号一致） |
| (5.4) | p.134 / 31 | $\check M$、$\beta^{\vee}$ 紧跟在 $M\to\mathbb{Z}^{n+r}$ 的箭头上 | ✓ |
| (5.5) | p.134 / 37 | $C(\underline{\Delta})$ 下划线只在下 $\Delta$；式末逗号 | ✓ |
| (5.6) | p.135 / 76 | $\sum_{i=0}^{n+r}$、$a_i x_1^{v_{i1}}\cdots x_n^{v_{in}}$ | ✓ |
| (5.7)(5.8) | p.135 / 81–82 | $x_i\mapsto\alpha_i x_i$、$a_k\mapsto\alpha_1^{-v_{k1}}\cdots\alpha_n^{-v_{kn}}a_k$ 及 $i,k$ 范围 | ✓ |
| (5.9)(5.10) | p.135 / 86–87 | $x_i\mapsto x_i$、$a_k\mapsto\alpha a_k$ | ✓ |
| (5.11) | p.135 / 101 | 连等 $W=\partial W/\partial x_1=\cdots=\partial W/\partial x_n=0$ | ✓ |
| (5.12) | p.136 / 118 | $\prod_{j=1}^{n}\bigl(\sum_{p=1}^{r}c_j^{(p)}\lambda_p\bigr)^{c_j^{(q)}}$ 的上下限与指数 | ✓（指数确为 $c_j^{(q)}$） |
| (5.13) | p.136 / 129 | $\varphi_Y^{reg}\colon\mathfrak Y_A^{reg}\to X_{\mathcal F(A)}^{reg}$ | ✓ |
| (6.1) | p.136 / 142 | 左端 $H^{\bullet}_{amb}$、$\Imm(\iota^*\colon H^{\bullet}(\check X)\to H^{\bullet}(\check Y))$ | **✗ 左端漏 $\bullet$**（见 M1）；箭头、$\iota^*$、$\check X/\check Y$ 均 ✓ |

补充核对：$C(\underline{\Delta},\Delta')$（p.135 无编号式，下划线只在 $\Delta$）、$\mathcal O_{X_{\tilde{\mathcal F}(A)}}(1)$、$X^{reg}_{\mathcal F(A)}=\mathbb L_{\mathbb C^\times}\setminus\nabla_A$、$\mathscr F_A^p=H^{4-2p}_{amb}\otimes\mathcal O_U$ 均与原图一致。

## 必须改

**M1. (6.1) 与 $\mathscr H_A$ 定义中的 $H^{\bullet}_{amb}$ 漏了上标 $\bullet$（2 处）。**
- `c04.tex:142`：现为 `H_{amb}(\check{Y};\mathbb{Z})=...`；原书 p.136 的 (6.1) 印作 $H^{\bullet}_{amb}(\check Y;\mathbb{Z})=\Imm(\iota^*\colon H^{\bullet}(\check X;\mathbb Z)\to H^{\bullet}(\check Y;\mathbb Z))$（H 上有实心圆点，已用 400/500 dpi 裁图确认）。
- `c04.tex:149`：现为 `\mathscr{H}_{A}=H_{amb}(\check{Y};\mathbb{C})\otimes\mathcal{O}_{U}`；原书同段印作 $H^{\bullet}_{amb}(\check Y;\mathbb{C})\otimes\mathcal O_U$（同样带 $\bullet$）。
- 理由：原书在同一页区分三种记号——$H^{\bullet}_{amb}$（总上同调）、$H^{2}_{amb}$（2 次部分，c04 已正确作 $H_{amb}^{2}$）、$H^{amb}_{A,\mathbb Z}$（局部系统，c04 正确）；(6.1) 的 $\bullet$ 不是排版噪声。c04 在 (6.1) 右端与下一句都已写 $H^{\bullet}(\check Y;\mathbb Z)$，唯独左端和被定义量漏 $\bullet$，属漏抄而非体例。
- 改法：`H_{amb}` → `H^{\bullet}_{amb}`（仅这两处）。

## 建议改（不影响数学正确性，属中文表达）

- **S1**（`c04.tex:91–93`）「把族 … 用 $\mathbb{T}\times\mathbb{C}^{\times}$ 的作用取商」→「对 $\mathbb{T}\times\mathbb{C}^{\times}$ 的作用取商」（原文「による作用で割り」，「用…取商」偏生硬）。
- **S2**（`c04.tex:89`）「下被乘以 $\alpha$」→「下乘以 $\alpha$」或「下变为 $\alpha$ 倍」（消灭被动）。
- **S3**（`c04.tex:40`）「在 $M_{\mathbb{R}}$ 上仿射线性函数所成的加法群 $\Aff(M_{\mathbb{R}})$ 的作用下不变」→「在由 $M_{\mathbb{R}}$ 上的仿射线性函数所成的加法群 $\Aff(M_{\mathbb{R}})$ 的作用下不变」。
- **S4**（`c04.tex:47–48`）「把 $\mathbb{Z}^{A}$ 的基送到 $\mathcal{F}(A)$ 的一维锥的生成元」→ 原文是「基底の像たちは…生成元をなし」，宜作「使 $\mathbb{Z}^{A}$ 的基的像构成 $\mathcal{F}(A)$ 的一维锥的生成元」。
- **S5**（`c04.tex:63`）「诸锥 … 的集合」→「各个锥 … 的集合」（「诸」带日文语感）。
- **S6**（`c04.tex:106`）「它到 $\mathbb{C}^{A}$ 的投影的像的闭包」→「它到 $\mathbb{C}^{A}$ 的投影之像的闭包」（连用两个「的」）。
- **S7**（`c04.tex:120`）「则已知有理映射 $h\colon…$ 的像给出 …」→「则已知：有理映射 … 的像给出 …」（或「……，这一点是已知的」），现语序易把「已知」误读到「有理映射」上。
- **S8**（`c04.tex:128`）「把 … 上的限制表作 (5.13)」→「记作 / 表示为」（原文「で表す」，「表作」生硬）。
- **S9**（`c04.tex:99`）「Laurent 多项式 $W$ 的临界点集合，在 $(\mathbb{C}^{\times})^{n}\times\mathbb{C}^{A}$ 上由 (5.11) 定义。」→ 删去「集合」后的逗号（原文「は，」是日语主题标记，不必照搬）。
- **S10**（`c04.tex:145`）「取作由外围环面簇的上同调群作限制所得的 … 的子空间时」→「取作外围环面簇的上同调群经限制得到的 … 的子空间时」。

## 需裁定

- **R1. 「入れ物のトーリック多様体」的译名。** c04 作「外围环面簇」（`c04.tex:145`）；更通行的译法是「环境环面簇」。该词全篇只出现这一次（p.136），改与不改都不影响跨块一致，请 Lead 决定是否统一为「环境环面簇」。
- **R2. c04 已声明的三处「照原文」，逐一判定如下：均合格，无需改。**
  1. **(5.1) 的 $P$ 与 $\beta$ 不一致**（`c04.tex:19` 的 Tutor Note）：原书 p.134 的 (5.1) 箭头标 $\beta$、正文称该映射为 $P$、(5.4) 又用对偶 $\beta^{\vee}$；c04 分别保留 $P$ 与 $\beta$ 并说明，处理正确（我另核了 p.134 原图，Note 所述与原文一致）。
  2. **(5.12) 后的 $\Phi_1(\lambda_1)$**（`c04.tex:124` 的 Tutor Note）：原书 p.136 确印 $\Phi_1(\lambda_1)$（400 dpi 裁图复核，不是 $\lambda$），而同段下一分量作 $\Phi_r(\lambda)$；按 (5.12)，$\Phi_q(\lambda)$ 依赖整个 $\lambda$，所以 Note 判「$\lambda_1$ 疑为 $\lambda$ 之误」是合理的，c04 照原图录 $\lambda_1$ 也正确。
  3. **$\mathscr{F}^{\bullet}$ 上标**：原书 p.136 的变形五元组 $(H^{vc}_{B,\mathbb Z},\nabla^B,\mathscr F_B^{\bullet},Q_B)$、正文「$\mathscr F_B^{\bullet}$ は Hodge フィルトレーション」（r10j 裁图确认带 $\bullet$）以及末尾 $(H^{amb}_{A,\mathbb Z},\nabla^A,\mathscr F_A^{\bullet},Q_A)$ 都带 $\bullet$；c04 在 `c04.tex:135`、`139`、`153` 全部作 `\mathscr{F}_{B/A}^{\bullet}`，`150` 行作 $\mathscr F_A^p$，处理合格。
- **R3. 与 M1 相关**：$H^{\bullet}_{amb}$ 这一记号的体例应在 c05 起（p.011 的 $H^{amb}_{A,\mathbb Z}$、数值 Grothendieck 群一段）保持一致；c05 的作者若尚未处理，建议 Lead 一并提醒。

## 漏译 / 增译检查

- p.008–p.010 逐段比对，**无漏译、无增译**。跨页处处理正确：p.008 末「2 次スタッ」→ p.009 首「ク (secondary stack)」在 c04 中合并为一句；p.010 段首承上「で定義されるが」接在 (5.11) 之后译出；结尾止于「……[Iri11, Definition 6.2]。」，与 BRIEF §4 的 c04/c05 边界一致（下一句「局所系 $H^{amb}_{A,\mathbb Z}$ のファイバーは…数値」留给 c05）。
- 新增的只有 2 条 Tutor Note（P/β、$\Phi_1(\lambda_1)$）和段首必要的衔接词，未改原意。

## 术语与文风

- 术语全部符合 `glossary.tsv`：扇序列、除子序列、二次扇、正则三角剖分、回路、二次栈、Chow 商、Lafforgue 扇/栈、判别式簇、$A$ 判别式、二次多面体、既约 $A$ 判别式簇、Horn–Kapranov 单值化、纯极化整 Hodge 结构、消没闭链、局部系统、Gauss–Manin 联络、Hodge 滤过、Poincaré 配对、反典范丛、全局截面、粗模空间、稠密环面、栈式扇、环面 Deligne–Mumford 栈、仿射线性、分片线性凸函数、完备扇、商锥、正合列、核、基、格点、自反多面体等。
- 哥特体强调逐处对照原图，全部一致：扇序列（p.134）、除子序列、二次扇、正則三角分割（首见处，p.134）、回路、二次栈、Chow 商（p.135）、Lafforgue 扇/栈、判别式簇、$A$ 判别式、二次多面体、簡約 $A$ 判別式多様体、Horn–Kapranov 一意化（p.136）；未发现多余或遗漏的 `\textbf`。
- 翻译腔主要即 S1–S10 所列；无「被……所……」「进行……的讨论」类句式（全文仅 1 处「被乘以」，见 S2）。

## 结论

c04 内容完整、公式与原文逐符号一致，术语与哥特体强调均合规；唯一必须改的是 **(6.1) 与被定义量 $\mathscr H_A$ 中的 $H^{\bullet}_{amb}$ 漏上标 $\bullet$（M1，2 处）**，其余为文字润色（S1–S10）和一处译名选择（R1）。改掉 M1、酌情采纳 S1–S10 后即可通过。

（本报告未修改 c04.tex 或任何其他工程文件；核对用裁图已在报告完成后从 `work/` 清理。）
