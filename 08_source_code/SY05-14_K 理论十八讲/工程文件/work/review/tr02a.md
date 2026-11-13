# tr02a.tex 交叉校对报告

- 校对者：tr-08
- 被校文件：`work/src/chunks/tr02a.tex`（tr-02，原文 pp.28–39，§3 第二讲、§4 第三讲）
- **校对快照**：`SHA256 = 6A1EBD1E…C6EF54A5`、mtime `2026-11-06 22:40:59`、15899 字节、359 行（LF=359）、UTF-8 无 BOM。**校对期间该文件被并发编辑多次**：22:25 破折号规范化、22:36 `\ker→\Ker`（preamble 新增宏）、22:39 给两处 `tikzcd` 加 `\[…\]` 时**一度多出两个 `\end{tikzcd}`**、22:40:59 已修好（现 `\begin{tikzcd}`:`\end{tikzcd}` = 2:2）。若 Lead 之后又改动，请按本报告引文定位；需要的话我再按最终快照复核一遍。
- 校对依据：`work/pages/p028.png–p039.png`（200 dpi 页图，公式唯一真值）+ `work/split/p028–p039.txt`（仅定位）+ STYLE_GUIDE/BRIEF/glossary.tsv/TIMELINE
- 放大核对图（`work/tmp/`）：`rev08_a/l3/l4.png`、`rev08_b2/c/c2.png`、`rev08_d/e/f/g/m3/h/i/j/k.png`
- 大算符对照实验：`work/tmp/symtest/`（极小 LaTeX 测试 `t.tex`/`t2.tex`、`t.pdf`、`display.png`）
- **本报告只新建此文件；未改动 tr02a.tex / preamble.tex / 任何他人文件；未编译本书。**

---

## 0. 结论摘要

总体质量高：结构、编号、漏译、术语、边界全部合格；**剩下 1 处公式符号误用（必须改）**。

- **必须改 1 项**：p.28 的 `X = ? X_a` 原文是 **`\coprod`（∐）**，不是 `\bigsqcup`（⊔）。已用 PDF 字符层 + 对照编译实验双重确证（见 2.2）。现文件第 8 行仍为 `\bigsqcup`。
- 编号定理类：8 个编号环境（定义 1–4、定理 1–3、引理 1）顺序、号数与页图**完全一致**；§4 确实**无**编号定理类。
- 公式：抽查 14 组（超过要求的 8 组），除上述 1 处外**未发现错抄**。
- 漏译：逐页整段对照，**未发现整句/整段/脚注缺失**（本页段无脚注）。
- 边界：p.28 起、p.39 止与相邻块**无重复、无缺口**。
- 结构：两节标题与 BRIEF 逐字一致；`\tag` 0 处；`\resizebox` 1 处、实测可读；环境嵌套 22:40:59 快照已恢复正常（见上文「并发编辑」提示）。
- `\ker → \Ker` 的大小写问题已被 Lead 于 22:36 全局解决（preamble 新增 `\Ker`，tr02a 5 处均为 `\Ker`），本报告确认无误。
- 可选改 6 项（措辞/批注事实订正/全书记号统一），均给可直接替换文本。

---

## 1. 编号定理类完整性

### 1.1 §3（原文 pp.28–33）对照表

| # | 页 | 原文 | tr02a 行号 | tr02a 写法 | 判定 |
|---|---|---|---|---|---|
| 1 | p.28 | **Definition 1.** Two vector bundles … stably isomorphic | 23–26 | `\begin{defn}{1}` | ✅ 号数 1 |
| 2 | p.28 | **Definition 2.** The reduced K-group … | 28–30 | `\begin{defn}{2}` | ✅ 号数 2 |
| 3 | p.29 | **Theorem 1.** ẼKX = [X, G∞] | 51–53 | `\begin{thm}{1}` | ✅ 号数 1 |
| 4 | p.30 | **Lemma 1.** V(f₀) ≃ V(f₁) | 67–70 | `\begin{lem}{1}` | ✅ 号数 1 |
| 5 | p.30 | **Theorem 2.** Vect_k(SX) = [X, GL_k(ℂ)] | 73–75 | `\begin{thm}{2}` | ✅ 号数 2 |
| 6 | p.30 | **Theorem 3.** ẼK(SX) = [X, GLℂ] | 84–86 | `\begin{thm}{3}` | ✅ 号数 3 |
| 7 | p.32 | **Definition 3.** The negative powers … | 135–138 | `\begin{defn}{3}` | ✅ 号数 3 |
| 8 | p.32 | **Definition 4.** The relative K-groups … | 142–145 | `\begin{defn}{4}` | ✅ 号数 4 |
| — | p.30 | **Remark:**（原文**无**编号） | 92 | `\para{注：}` | ✅ 按 STYLE §4 作未编号小标题 |

**顺序判定**：定义 1 → 定义 2 → 定理 1 → 引理 1 → 定理 2 → 定理 3 → 定义 3 → 定义 4，与页图逐页一致；**无跳号、无重号、无自造编号**。原文 §3 没有 Proposition / Corollary / 编号 Remark，tr02a 也没有。与 Lead 预期顺序完全吻合。

### 1.2 §4（原文 pp.34–39，tr02a 第 182 行起）

逐页核对 p34–p39：**§4 确实没有任何编号定理类**（页图只有正文、展示式与三组手写编号列表）。tr02a 在 §4 内只有 `enumerate`（`label=\arabic*.`，均从 1 起）：p32 的列表 1–2（属 §3 末尾）、p34–p35 的性质列表 1–6（跨页正确）、p37 的列表 1–2。编号与原文逐项一致。✅

---

## 2. 公式逐符号核对（14 组，≥8）

核对方式：500–1600 dpi 裁图 + PDF 字符层（`get_text("rawdict")`）+ 大算符对照编译实验（2.2）。

### 2.1 核对表

| # | 页 | 公式（原文页图） | tr02a 现状 | 判定与证据 |
|---|---|---|---|---|
| **1** | **p.28** | `X = ∐ X_a`（原文为 **`\coprod`**，display 变体） | 第 8 行：`X = \bigsqcup X_a` | ❌ **必须改**。字符层：p28 该符号 = CMEX10 **U+0061（槽 0x61）**；对照实验：display `\coprod`=0x61、`\bigsqcup`=0x47 → 原文是 `\coprod`。视觉上页图符号是「两竖 + 顶部宽衬线 + 底横」的 ∐，与 `display.png` 左字一致 |
| 2 | p.28 | `K(X) = ∏ K(X_a)` | `\prod K(X_a)` | ✅ 字符层 U+0059（0x59）；对照实验：display `\prod`=0x59 ✓ |
| 3 | p.28 | `G_k = ∪_n G_k(ℂ^n)`（行内） | `\bigcup_n G_k(\C^n)` | ✅ 字符层 U+0053（0x53）；text `\bigcup`=0x53 ✓ |
| 4 | p.29 | `SX = C_+X ∪_X C_-X` | `C_+X\cup_X C_-X` | ✅ 下标确为 X（`rev08_b2.png`，800 dpi） |
| 5 | p.29 | `V(f) = (C_+X×ℂ^k ∪ C_-X×ℂ^k)/((x,v)≡(x,f(x)v))` | 同左 | ✅ 分式/∪/≡/参数顺序一致（`rev08_c.png`、`rev08_c2.png`） |
| 6 | p.30 | `A ↦ ( A 0 ; 0 1 )`（pmatrix） | `pmatrix` | ✅（`rev08_d.png`，800 dpi） |
| 7 | p.32 | `ẼK^{-n}X = ẼK(S^nX)`；`ẼK^{-n}(X,A) = ẼK^{-n}(X/A) = ẼK(S^n(X/A))` | 同左 | ✅ 上标/括号与页图一致 |
| 8 | p.33 | 六项正合列（上行 →、下行 ←、左端 ↑、右端 δ↓） | `tikzcd`（第 172–177 行） | ✅ 箭头方向、δ 位置正确（`rev08_e.png`，600 dpi） |
| 9 | p.35 | 同上图**重复一次**，图末有一个句点「.」 | `tikzcd`（第 222–227 行）；**图后无句点** | ✅ 图正确；句点缺失仅属标点，见「可选改 E」 |
| 10 | p.36 | `(X×ℂ^k ∐ CA×ℂ^k)/(glue via f)` | `\frac{X\times\C^k\ \coprod\ CA\times\C^k}{\textit{glue via } f}` | ✅ 字符层 U+0060（0x60）；text `\coprod`=0x60 ✓；分母斜体（`rev08_g.png`、`rev08_m3.png`） |
| 11 | p.37 | `([ξ₁]−[η₁])⊗([ξ₂]−[η₂]) := [ξ₁⊗ξ₂]+[η₁⊗η₂]−[η₁⊗ξ₂]−[ξ₁⊗η₂]` | 同左 | ✅ 四项顺序、正负号、⊗ 位置逐符号一致（`rev08_h.png`） |
| 12 | p.38 | `ẼK⁰(S^n(X/A))⊗ẼK⁰(S^m(Y/B))→ẼK⁰(S^n(X/A)∧S^m(Y/B)) = ẼK⁰(S^{n+m}∧(X/A)∧(Y/B))` | 同左（`\resizebox`） | ✅ 逐符号一致（`rev08_i.png`）。**可读性实测**：原文该行 451.9 pt/12 pt；按 11 pt 折算 ≈414 pt，`0.98\textwidth`≈439 pt，缩放比 ≈1.06（≈11.7 pt），不缩小、清晰 |
| 13 | p.38 | `(X×Y)/(A×Y ∪ X×B) = X/A ∧ Y/B` | 同左 | ✅ |
| 14 | p.39 | SO_N 同伦群表 7+1 行 | 8 行逐条照录（第 347–355 行） | ✅ 逐行核对；**末行原文确作 `i≡1(8)`**（700 dpi 复核），应为 `i≡0(8)`；tr02a 照录并在批注指出（第 357 行）✅ |
| 15（附） | p.39 | `π_{2n+1}(GL_N(ℂ)), N > 2n+2)`、`GL_N(ℂ))` 多余右括号 | 原样保留 | ✅ 照录，批注第 359 行已说明 |

**其他抽查**：p.28 `ξ⊕ℂ^M_X = η⊕ℂ^N_X`；p.29 `G_k = lim G_k(ℂ^n) = ∪_n G_k(ℂ^n)`（display `\bigcup`=0x5B ✓）；p.30 `GLℂ = lim GL_k(ℂ) = ∪_k GL_k(ℂ)`；p.31 `S^{2n}(S^1)=S^{2n+1}`、`S^{2n-2}(S^2)=S^{2n}`；p.32 `(X,∅)=X^+`、`K^n(X,A)=K^{n-2}(X,A)`；p.37 smash 积 `(X×Y)/(x₀×Y∪X×y₀)`；p.38 `K^nX⊗K^mX→K^{n+m}(X×X)\xrightarrow{\Delta^*}K^{n+m}X`。全部与页图一致。✅

### 2.2 大算符鉴定（附：对照编译实验）

**为什么要做**：Lead 的清单按「p.28 的 ⨆」预期；但页图放大后该符号与 `\bigsqcup`（⊔）不像，而与 `\coprod`（∐）一致。两步鉴定：

**(a) 原书 PDF 字符层（`rawdict`）的 CMEX10 槽位：**

| 页 | 位置 | 字符 | 槽位 |
|---|---|---|---|
| p.28 | `X = ? X_a`（display） | `a` | **0x61** |
| p.28 | `K(X) = ? K(X_a)`（display） | `Y` | 0x59 |
| p.28 | `G_k = ?_n G_k(ℂ^n)`（inline） | `S` | 0x53 |
| p.29 | `= ?_n G_k(ℂ^n)`（display） | `[` | 0x5B |
| p.36 | `X×ℂ^k ? CA×ℂ^k`（分数内 text） | `` ` `` | **0x60** |

**(b) 极小 LaTeX 文档编译出的「命令 → CMEX10 槽位」对照表**（`work/tmp/symtest/t2.tex`，MiKTeX pdfTeX + 标准 Computer Modern）：

| 命令 | text 样式 | display 样式 |
|---|---|---|
| `\coprod` | 0x60 | **0x61** |
| `\bigsqcup` | 0x46 | 0x47 |
| `\prod` | 0x51 | 0x59 |
| `\bigcup` | 0x53 | 0x5B |
| `\sum` | 0x50 | 0x58 |

**结论**：原书 p.28 与 p.36 用的**都是 `\coprod`**（p.28 为 display 变体 0x61，p.36 为 text 变体 0x60）。故：p.28 应写 `\coprod X_a`（tr02a 现作 `\bigsqcup`，错）；p.36 的 `\coprod` 正确；p.28 的 `∏`、p.28/p.29 的 `∪` 均正确。视觉对照：`work/tmp/symtest/display.png`（左 = `\coprod` display，右 = `\bigsqcup` display）；`work/tmp/rev08_l4.png`（原书 p.28 符号）与左字相同。

---

## 3. 漏译检查

逐页把 `split/p028–p039.txt` 的每一句与 tr02a 对应段落对读，**未发现整句、整段或脚注缺失**（本页段无脚注）。容易漏掉的短句均已存在：

- p.28：`(to be precise we mean equality of the cardinalities …)` ✓；`Yet K(∗)=ℤ whereas the dimension … X→ℤ …` ✓
- p.29：`Intuitively, G∞ is the double inductive limit …` ✓
- p.30：`For the proofs of Theorems 2 and 3 one can see Atiyah's notes.` ✓；`Remark: … where ΩG∞ the loop space …` ✓
- p.31：`because Grassmannians are contractible.` ✓（并批注指出原文有误）
- p.32：`To summarise:` 及两条 ✓
- p.33：`(this is the wrong way funcoriality in K-Theory) where at the same time given …` ✓
- p.34：`using Bott periodicity.` ✓；`(which follow from the Eilenberg-Steenroad axioms)` ✓
- p.35：`Thus we have a generalised (or exotic) cohomology theory.` ✓；`along with the maps …` ✓
- p.36：`The proof of exactness is tedious.` ✓；`Now let us study the products.` ✓
- p.37：`For example, the suspension of a space X is the smash product with the circle:` ✓
- p.38：`Hence we obtain:` ✓；`which is a graded commutative ring.` ✓；`We are now in a position to see …` ✓
- p.39：`is an isomorphism (recall that ẼK⁰S² = ℤ).` ✓；`Bott periodicity is perhaps the most useful tool …` ✓

原文笔误（Grassmann 可缩、funcoriality、conecting、esentially、onviously、orhtogonal、Steenroad、多余右括号、SO 表末行 i≡1(8)）均按 STYLE「照译+批注」处理，批注齐全（15 条），未发现漏注。✅

---

## 4. 边界接缝

| 交界 | 上一块结束 | 本块开始 | 判定 |
|---|---|---|---|
| tr01a → tr02a（p.27/p.28） | tr01a 末句 `…（详见 [9]）。`（= p.27 末 `we refer to [9] for more details`） | tr02a 第 4–7 行：p.28 标记 + `\section{第二讲…}` + 「我们假设底空间紧的复向量丛。」（= p.28 首句） | ✅ 无重复、无缺口；tr01a 未写 §3 标题 |
| tr02a → tr03a（p.39/p.40） | tr02a 末行（第 355 行）`π_i(SO_N) = ℤ/2, i≡1(8).`（= p.39 末行） | tr03a 首段：`\section{第四讲（Chern 特征与 Chern 类）}` + 「我们已经看到，$K^n(X,A)$ 是一个可乘的广义上同调理论。」（= p.40 首句） | ✅ 无重复、无缺口；tr02a 未写 §5 标题，未越界抄 p.40 |
| 块内页缝 | 逐页核对 p.28→p.39 的 11 处页界（如 p.28 末 `G_k(ℂ^n) ↪ G_k(ℂ^{n+1})` / p.29 首 `and taking the inductive limit we get`） | 均连续 | ✅ |

---

## 5. 术语与记号

### 5.1 对照 glossary（相关条目全部一致）

约化 K 理论 / 约化 K 群、悬挂、环路空间、分类空间、Bott 周期性、稳定同构、Grassmann 流形、正合列、切除、维数公理、广义（非寻常）上同调理论 —— 均与 `glossary.tsv` 一致。✅

### 5.2 同一英文多译 / 跨块一致

- `smash product` → 「smash 积」3 处一致，且与 tr10a 一致 ✅。
- `external tensor product` → 「外张量积」1 处；与 glossary「张量积」相容 ✅。
- `clutching` → 「粘合」（批注），与 tr01a「粘合函数（clutching functions）」一致 ✅。
- 无同词异译。

### 5.3 记号一致性

1. **Ker 大小写（已解决，无需改）**：原书一律大写 `Ker`；22:36 起 tr02a 的 5 处均为 `\Ker`（第 18、185、289 行 + 批注第 32、196 行），`preamble.tex` 已新增 `\newcommand{\Ker}{\operatorname{Ker}}`。✅
2. **负幂写法（待 Lead 决策）**：tr02a 保持原文紧凑式 `ẼK^{-n}X`、`K^{-n}X`（第 137、148、189、191 行；第 163 行批注亦同）；而 tr08a 把 p.104 的 `K^{-1}X` 写作 `K^{-1}(X)`。BRIEF §5 只规定 `KX → K(X)`，未规定负幂。建议二选一全书统一（见「可选改 F」）。

---

## 6. 修改建议

### 6.1 必须改（1 项）

**M1. p.28 大算符：`\bigsqcup` → `\coprod`（第 8 行）**

- 原文（页图 p.28；字符层 0x61 = display `\coprod`）：`X = ∐ X_a,`
- 现状（第 8 行）：`\[ X = \bigsqcup X_a, \]`
- 依据：PDF 字符层 + 对照编译实验（2.2）；`\bigsqcup` 渲染成 ⊔，与原文 ∐ 不符。
- **替换（第 8 行整行）**：
  ```latex
  \[ X = \coprod X_a, \]
  ```

### 6.2 可选改（6 项，均给可直接替换文本）

> 以下为更贴原文/更符合 STYLE/批注事实订正的建议，Lead 可择取；不改也不算错。

**A. p.28 首句语法（第 7 行）**

- 原文：`We assume complex vector bundles with compact base.`
- 现状：`我们假设底空间紧的复向量丛。`（「假设…复向量丛」缺谓语搭配）
- 替换（第 7 行整行）：
  `我们假定所讨论的复向量丛的底空间是紧的。若底空间是不交并`

**B. p.31 强调范围（第 105 行）**

- 原文：`which means that the infinite Grassmannian G∞ is a classifying space of the infinite group GLℂ:`
- 现状：`这意味着\emph{无穷 Grassmann 流形} $G_\infty$ \emph{是无穷群} $\GL\C$ \emph{的分类空间}：`（\emph 被公式切成三段）
- 替换（第 105 行整行）：
  ```latex
  这意味着\emph{无穷 Grassmann 流形 $G_\infty$ 是无穷群 $\GL\C$ 的分类空间}：
  ```

**C. p.33 「wrong way functoriality」（第 169 行）**

- 原文：`(this is the wrong way funcoriality in K-Theory)`
- 现状：`（这是 K 理论中方向相反的函子性。）`
- 替换（第 169 行）：
  ```latex
  （这是 K 理论中的反向函子性。）同时，给定
  ```

**D. p.30 批注（第 90 行）事实订正——建议改**

- 现状（批注末句）：`其逆由沿 $S^1$ 方向的转移函数给出。`
- 问题：$SX=C_+X\cup_X C_-X$ 是**沿赤道 $X$** 粘合两个锥，过渡信息（粘合函数）定义在 $X$ 上，不在 $S^1$ 上；且 glossary 中 clutching function 作「粘合函数」，不是「转移函数」。
- 替换（第 90 行批注末句）：
  `其逆由沿赤道 $X$ 的粘合函数（clutching function）给出。`

**E. p.35 六项正合列图后的句点（第 222–227 行）**

- 原文：p.35 页图上该图 δ↓ 右侧有一个句点「.」（整段以图为句末）。
- 现状：`\end{tikzcd}`（第 226 行）后无句点。
- 替换（把第 226 行改为）：
  ```latex
  \end{tikzcd}.
  ```

**F. 全书写法统一：负幂记号（Lead 决策项）**

- 现状：tr02a 保持原文紧凑式 `ẼK^{-n}X` / `K^{-n}X`（第 137、148、189、191 行）；tr08a 把 p.104 的 `K^{-1}X` 写作 `K^{-1}(X)`。
- 建议：二选一全书统一。若选「加括号」，本块约 6 行替换为 `\wt K^{-n}(X)`、`K^{-n}(X)`、`K^{-n}(X,\emptyset)`；若选「保持紧凑」，只需统一 tr08a 侧。**需 Lead 决策，故不列单行替换。**

---

## 7. 机械自检结果（22:40:59 快照）

| 检查项 | 结果 |
|---|---|
| UTF-8 无 BOM / LF | ✅ 15899 字节；LF=359；CRLF=0 |
| U+FFFD 乱码 | ✅ 0 |
| 页标记 `% [原文 p.N]` | ✅ 12 个，p.28–p.39 连续无漏 |
| `\section` | ✅ 2 个，与 BRIEF 逐字一致 |
| `\tag` | ✅ 0 |
| `\resizebox` | ✅ 1 处，实测可读（缩放比 ≈1.06） |
| 环境嵌套 | ✅ 通过（`\begin{tikzcd}`:`\end{tikzcd}` = 2:2，无失配、无残留） |
| 花括号 | ✅ 非注释行净差 0 |
| `$` 成对 | ✅ 逐行无奇数个 `$` |
| `\left/\right` | ✅ 0/0（3 处 `\left` 实为 `\leftarrow`） |
| `\ker` / `\Ker` | ✅ `\ker` 0 处；`\Ker` 5 处，preamble 已有宏 |
| Tutor Note | 15 条（§3 七条、§4 八条），达标 |
| 未编译 | ✅ 未编译本书；只做过 2 页极小对照实验（`work/tmp/symtest/`），未改任何 .tex |

> ⚠️ **并发编辑提醒**：22:39 的快照里，两处 `tikzcd` 被包进 `\[…\]` 时一度各多出一个 `\end{tikzcd}`（`begin` 2 个、`end` 4 个，会直接编译报错「Extra \end{tikzcd}」）；22:40:59 快照已恢复 2:2。若 Lead 的批量脚本再次跑过这些文件，建议编译前再 grep 一遍 `\begin{tikzcd}`/`\end{tikzcd}` 计数。

---

### 附：一句话给 Lead

tr02a.tex 只剩 1 处硬错误——**p.28 第 8 行的 `\bigsqcup` 应为 `\coprod`**（原文是 ∐，不是 ⨆；证据见 2.2）；改完即可定稿。`\ker→\Ker` 已由你在 22:36 解决；22:39 一度出现的两个多余 `\end{tikzcd}` 已在 22:40:59 修好。建议优先做可选改 D（p.30 批注事实订正）。
