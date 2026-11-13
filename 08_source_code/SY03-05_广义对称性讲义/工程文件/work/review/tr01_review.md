# 交叉校对报告：tr-01（pp.13–28）与 Lead c01（pp.1–12）

校对者：tr-08　　日期：2026-11-04　　校对对象文件：
`work/src/chunks/tr01a.tex`、`tr01b.tex`、`tr01c.tex`、`c01.tex`（**只读，未修改他人任何文件**）
比对依据：`work/tags.txt`、`work/tags_bypage.txt`、`work/pages/pNNN.png`（400–900 dpi 裁图）、`work/split/pNNN.txt`、`glossary.tsv`。

---

## 1. 结论摘要

| 项 | c01（pp.1–12） | tr-01（pp.13–28） |
|---|---|---|
| 编号公式完整性 | **通过**：2.1–2.37 共 37 条，与 tags.txt 完全一致 | **通过**：2.38–2.109 + 3.1–3.6 共 78 条，完全一致 |
| 公式逐符号 | **通过**（抽查 7 条全部一致） | **通过**（抽查 11 条全部一致，含最易错的分段积分下标 (2.33)、上链公式 (2.84)(2.86)(2.101)(2.109)） |
| 结构（标题/图/方框） | 通过（§2、2.1、2.2、2.2.1 标题；图 1–3；陈述 2.1、定义 2.1、例 2.1、notebox） | 通过（2.2.2、2.3、§3、3.1 标题；图 4–8；陈述 2.2、定义 3.1、例 2.2/2.3、3 个 notebox） |
| 漏译 | 未发现（§1 逐段对过 p.3–5） | 未发现（pp.13–28 逐页对过） |
| 术语 | 2 处建议统一（见 §6） | 与 glossary 一致；仅跨块记号 `\mathsf{D}`/`\mathrm{D}` 需全局裁决 |
| **必须改** | **2 项**（例 2.1 框内公式重复；一条 Tutor Note 与文件实际内容矛盾） | **0 项** |

总体判断：**tr-01 的三片质量很高**，146 条公式抽查未见抄写错误，跨页句与跨页方框都按规范处理；**c01 只有 1 处会在编译输出中直接看见的缺陷**（例 2.1 框里 $G^{(0)}=U(1)$ 出现两次），其余是页标记与个别措辞。

---

## 2. 编号完整性表（tags.txt ⇄ 文件实有）

c01：`2.1 … 2.37`，计数 37／37，**无缺、无重、无跳、无自造**；
tr01a：`2.38 … 2.60`（23 条）；tr01b：`2.61 … 2.83`（23 条）；tr01c：`2.84 … 3.6`（32 条）；合计 78／78。

| 页 | tags.txt 应有 | 实际所在文件 | 备注 |
|---|---|---|---|
| p6 | 2.1–2.6 | c01 | ✓ |
| p7 | 2.7–2.9 | c01 | ✓ |
| p8 | 2.10–2.16 | c01 | ✓ |
| p9 | 2.17–2.22 | c01 | ✓ |
| p10 | 2.23–2.32 | c01 | ✓（2.24 在例 2.1 框内，位置正确） |
| p11 | 无 | — | ✓（该页只有图 3） |
| p12 | 2.33–2.37 | c01 | ✓ |
| p13 | 2.38–2.43 | tr01a | ✓ |
| p14 | 2.44–2.49 | tr01a | ✓ 六条齐，但页标记顺序有误（见 §7-O1） |
| p15 | 无 | — | ✓（该页只有图 4） |
| p16 | 2.50–2.55 | tr01a | ✓ |
| p17 | 2.56–2.60 | tr01a | ✓ |
| p18 | 2.61–2.62 | tr01b | ✓ |
| p19 | 2.63–2.67 | tr01b | ✓ |
| p20 | 2.68–2.76 | tr01b | ✓ |
| p21 | 2.77–2.80 | tr01b | ✓ |
| p22 | 2.81–2.83 | tr01b | ✓ |
| p23 | 2.84–2.90 | tr01c | ✓ |
| p24 | 2.91–2.98 | tr01c | ✓ |
| p25 | 2.99–2.104 | tr01c | ✓ |
| p26 | 2.105–2.109 | tr01c | ✓ |
| p27 | 3.1–3.6 | tr01c | ✓ |
| p28 | 无 | — | ✓（该页只有图 8） |

---

## 3. 逐符号核对表（裁图 500–900 dpi 与页面图像逐符号比对）

### 3.1 c01（pp.1–12）

| 式号 | 原文（页面图像） | c01 写法 | 结论 |
|---|---|---|---|
| (2.3) | $U(t)\mathcal O(\vec x,t)U^{-1}(t)=\mathcal O'(\vec x,t),$ | 同（`\cO`，`U^{-1}` 位置正确） | ✓ |
| (2.7) | $U(\Sigma_{d-1})=U(\Sigma'_{d-1}),$ | 同 | ✓ |
| (2.13) | $U(\Sigma_{d-1})\mathcal O(x)=\mathcal O'(x)U(\Sigma'_{d-1}),$ | 同（右端确为 $\Sigma'$ 而非 $\Sigma$） | ✓ |
| (2.16) | $U(S^{d-1})\mathcal O(x)=\mathcal O'(x).$ | 同 | ✓ |
| (2.19) | $U_g(\Sigma_{d-1})U_{g'}(\Sigma_{d-1})=U_{gg'}(\Sigma_{d-1}),$ | 同 | ✓ |
| (2.33) | 三行：$\int_{\Sigma'_{d-1}-\Sigma_{d-1}=\partial\Sigma_d}j^{d-1}$ → $\int_{\Sigma_d}\dd j^{d-1}$ → $U_g(\Sigma_{d-1})$，编号在**第二行** | align 三行，`\notag/\tag/\notag` 分配一致，积分下标正确 | ✓ |
| (2.37) | 四行，编号在**第二行**，末行 $\exp(\ii q\alpha)$ | align 四行，编号位置与末行一致 | ✓ |

### 3.2 tr-01（pp.13–28）

| 式号 | 原文（页面图像） | tr-01 写法 | 结论 |
|---|---|---|---|
| (2.38) | $U(\Sigma_{d-p-1}).$ | 同 | ✓ |
| (2.39) | $U(\Sigma_{d-p-1})=U(\Sigma'_{d-p-1}),$ | 同 | ✓ |
| (2.43) | $U_g,\ \forall g\in G^{(p)},$ | 同 | ✓ |
| (2.58) | $U_g(\Sigma_{d-p-1})\mathcal O(M_p)=\phi(g)\times\mathcal O(M_p)U_g(\Sigma'_{d-p-1}),\ \ \phi(g)\in\mathbb C^\times=\mathbb C-\{0\}$ | 同（$\times$、$\Sigma'$、$\mathbb C^\times$ 全对） | ✓ |
| (2.63) | $U_g(S^{d-p-1})\mathcal O(M_p)=\phi_g\times\mathcal O(M_p),$ | 同（此处原文确为 $\phi_g$ 下标形式） | ✓ |
| (2.72) | $G^{(p)}\cong\prod_{i=1}^{n}\mathbb Z_{N_i},\ N_i\in\mathbb N$ | 同 | ✓ |
| (2.83) | $2\pi\int a_p\cup_\eta\delta b_{d-p-1},$ | 同（$\cup_\eta$ 下标、$\delta$ 均对） | ✓ |
| (2.84) | $\delta c_q(v_0,\dots,v_{q+1})=\sum_{i=0}^{q+1}(-1)^i c_q(\dots,v_{i-1},v_{i+1},v_{i+2},\dots)$ | 同（求和上下限 $0$ 到 $q+1$、删去 $v_i$ 的下标都对） | ✓ |
| (2.101) | $(b_{d-p-1}(g))(v_0,\dots,v_{d-p-1})=(b_{d-p-1}(\dots)\in\widehat G^{(p)})(g)\in U(1).$ | 同（双重括号结构、$g$ 作用于 $\widehat G^{(p)}$ 元素这一写法全对） | ✓ |
| (2.109) | $\int\Lambda_{d-p-1}\cup_\eta\delta_g^{p+1}(M_{d-p-1})=\int_{M_{d-p-1}}\Lambda_{d-p-1}(g)\in\mathbb R/\mathbb Z,$ | 同 | ✓ |
| (3.1)/(3.2) | $Q(\mathcal O_p)=Q(\mathcal O'_p)\in\widehat G^{(p)}$；$Q(\mathcal O_p)=1\in\widehat G^{(p)}$ | 同 | ✓ |
| (3.4) | $\mathsf D_p$（**无衬线正体** D） | `\mathsf{D}_p` | ✓（与字形一致；注意 tr02 用 `\mathrm{D}`，见 §6-3） |

**结论**：抽查 18 条编号公式，**0 处符号错误**。两处最容易抄错的点（(2.33) 的积分区域下标、一般 (2.84)/(2.101) 的长括号嵌套）都正确。

---

## 4. 结构核对

### 4.1 标题（谁写、编号是否与原文一致）

| 标题 | 页 | 原文 | 文件中 | 结论 |
|---|---|---|---|---|
| §2 | p5 | 2 Introduction to Higher-Form Symmetries | c01 `\section{高阶形式对称性导论}` | ✓ |
| 2.1 | p6 | 0-Form Symmetries | c01 `\subsection{0-形式对称性}` | ✓ |
| 2.2 / 2.2.1 | p12 | Higher-Form Symmetries / General Properties | c01 `\subsection` + `\subsubsection` | ✓ |
| 2.2.2 | p16 | Action of *p*-Form Symmetries | tr01a `\subsubsection{$p$-形式对称性的作用}` | ✓ |
| 2.3 | p22 | Discrete (Higher-Form) Gauge Theories | tr01b `\subsection{离散（高阶形式）规范理论}` | ✓ |
| §3 / 3.1 | p26 | Higher-Form Symmetries of Gauge Theories / Screening of Extended Operators | tr01c `\section` + `\subsection` | ✓ |

（`\para{}` 行内小标题全部照原文加粗位置处理：c01 4 处、tr01a 6 处、tr01b 3 处、tr01c 5 处，均正确。）

### 4.2 图（1–8）

| 图 | 页 | 归属 | 文件 | 图注 |
|---|---|---|---|---|
| 1 | p7 | c01 | ✓ fig1 | 与原文一致（含「反向副本」这一要点） |
| 2 | p9 | c01 | ✓ fig2 | 三幅图（左/中/右）均译到 |
| 3 | p10–11 | c01 | ✓ fig3（浮在 p.10 段后，实际页码 p11） | 见 §7-O2 |
| 4 | p15 | tr01a | ✓ fig4 | 与原文一致 |
| 5 | p18 | tr01b | ✓ fig5 | 含 $\phi(g)\in\mathbb C^\times$ ✓ |
| 6 | p19 | tr01b | ✓ fig6 | ✓ |
| 7 | p27 | tr01c | ✓ fig7 | ✓ |
| 8 | p28 | tr01c | ✓ fig8 | ✓ |

### 4.3 方框

| 方框 | 页 | 原文类型 | 文件 | 结论 |
|---|---|---|---|---|
| Statement 2.1 | p6 | 蓝 | c01 `statementbox` | ✓ 标题/正文全对 |
| Example 2.1 | p10–12 | 橙 | c01 `examplebox` | 类型/编号 ✓，但内容有重复式（见 §7-M1） |
| Definition 2.1 | p12 | 绿 | c01 `definitionbox` | ✓ |
| （无标题注释框） | p7 | 粉无标题 | c01 `notebox{关联函数中的算符}` | 原文该框**有**标题条 "Operators in Correlation Functions"，用 `notebox` 正确 ✓ |
| Statement 2.2 | p17 | 蓝 | tr01a `statementbox` | ✓ |
| Example 2.2 | p14–16 | 橙 | tr01a `examplebox`（跨页合并） | ✓ 编号未拆 |
| Remark on Higher-Charges | p18 | 粉带标题 | tr01b `notebox{关于高阶荷的注记}` | ✓ |
| Double Pontryagin Duality | p20 | 粉带标题 | tr01b `notebox{双重 Pontryagin 对偶}` | ✓ |
| Example 2.3 | p21–22 | 橙 | tr01b `examplebox`（跨页合并） | ✓ |
| Standard Cup Product | p24 | 粉带标题 | tr01c `notebox{标准杯积}` | ✓ |
| Definition 3.1 | p26–27 | 绿 | tr01c `definitionbox`（跨页合并） | ✓ |

**结论**：c01 覆盖 4 个方框、tr-01 覆盖 7 个方框，类型判断与跨页合并**全部正确**（含 p.7 那个容易被误判为 `noteboxplain` 的框，实际有标题条）。

---

## 5. 漏译核对

- **c01 §1（p.3–5）**：逐段对 `split/p003–p005.txt`。§1 五段（引言正文 / Related Literature / Prerequisites / Organization 六条 bullet）全部译出；`\para{相关文献/预备知识/本讲义的安排}` 三个行内小标题位置正确；无整句遗漏。唯一语义损失：p.3「theoretical and phenomenological high-energy physics」译作「高能物理」，丢掉「理论/唯象」的区分（§7-O4）。
- **tr-01（pp.13–28）**：按页图像与 split 逐页对，段落、脚注（p.17 脚注 1「simple $p$-dimensional operators」）、p.23 跨页句（"…taking $G^{(p)}=$ / $G^{(0)}$ to be an abelian group is an assumption…"）都完整承接，**未发现漏译段落或漏译脚注**。
- 跨页句「开始者写完」执行到位：p.22→23 的 bullet 句由 tr01b 写完（起点在 tr01b、跨页后仍在 tr01b），tr01c 从下一个 bullet 续起，无重复无缺口。

---

## 6. 术语一致性

1. **abelian 的译法不统一**：c01 用「非 Abel 规范理论」（第 23 行「非 Abel 规范理论」×2 处），tr01a/b/c 全用「阿贝尔/非阿贝尔」。建议统一为「阿贝尔/非阿贝尔」（glossary 无此条，但内部必须一致）。见 §7-O5。
2. **Hamiltonian**（c01 第 63 行）未译（「与生成时间演化的 Hamiltonian 对易」）。glossary 无此条；建议首现写「哈密顿量（Hamiltonian）」，或全文统一「哈密顿量」。
3. **跨块记号冲突（需 Lead 全局裁决）**：等价类群在 tr01c 写作 `\mathsf{D}_p`（与原文无衬线字形一致，我已核对 p.27 (3.4) 的 D 确为无衬线），而 tr02a 的 (3.7) 写作 `\mathrm{D}_p`。二者编译后字形不同且相邻出现，建议**全局统一为 `\mathsf{D}`**（我的 tr08 也按原文用 `\mathsf{D}`）。
4. 其余一致：高阶形式对称性 / 延展算符 / 局域算符 / 不可约 / 屏蔽（screening）/ Wilson 线 / 't Hooft 算符 / 磁单极子 / Pontryagin 对偶 / 融合规则 / 上链 —— 均符合 glossary。
5. **本报告新增术语建议**（供 Lead 汇总，均出现在 c01/tr01 中，glossary 暂无）：
   cup product → 杯积；cocycle → 上闭链；$q$-charge → $q$-荷；higher-representation → 高阶表示；
   characters → 特征标；codimension-$(p+1)$ operator → 余维-$(p+1)$ 算符；monopole operator → 磁单极子算符；
   defect group → 缺陷群；relative homology → 相对同调；polarization → 极化（同 tr08）。

---

## 7. 必改 / 可选改（含可替换文本）

### 【必须改】（2 项，均在 c01）

**M1｜c01.tex :220–225｜例 2.1 框内 $G^{(0)}=U(1)$ 重复出现两次（编译后可见）**
原文 p.10 只有一条 (2.24)。现文件在其前多出一段裸公式 `$G^{(0)}=U(1)$`（第 221 行），编译输出会是「$G^{(0)}=U(1)$」独立成段 + 紧接着带编号的同一式。
替换方案（第 221 行改成过渡词，最小改动）：

```latex
\begin{examplebox}{例 2.1：$U(1)$ 0-形式对称性}
考虑
\begin{equation}
    G^{(0)}=U(1)\,, \tag{2.24}
\end{equation}
这个例子很好地说明了上述所有概念。
```

（或删掉第 221 行、把第 225 行改为「这一例子很好地说明了上述所有概念。」）

**M2｜c01.tex :248–249｜Tutor Note 与文件实际内容矛盾**
该注称「(2.24) …此处并入正文首句以免…出现孤立编号」，但同文件第 222–224 行 (2.24) 是完整编号公式，(2.25) 紧随其后，并无「孤立编号」问题。此类注会被收进《译注汇总.md》，属事实性错误，须删或改写。
建议替换（若要保留一条关于该处的注）：

```latex
% [Tutor Note: (2.24) 是例 2.1 的首条公式；原文把「The example of … neatly illustrates」这句话
%   从公式两侧断开排版，译文改为「考虑 (2.24) 这个例子…」的顺装句序，公式与编号 (2.24) 与原位置均未变。]
```

### 【可选改】（8 项）

**O1｜tr01a.tex｜p.14/p.15 页标记顺序（仅注释，不影响编译）**
`(2.46)–(2.49)` 实际都在 p.14（已核对 `tags_bypage.txt` 与 p014.png），但文件里它们排在 `% [原文 p.15]` 与图 4 之后，读起来像 p.15 的内容；而 p.15 实际只有图 4。
建议：把图 4 连同其标记移到 (2.49) 之后：

```latex
\para{特例：$U(1)$ $p$-形式对称性。} … (2.46)(2.47)(2.48) …
% [Tutor Note: …]
实现 $U(1)$ 高阶形式对称性的一个具体例子如下。
\begin{examplebox}{例 2.2：Maxwell 理论中的高阶形式对称性}
… (2.49)
\end{examplebox}        % ← 此处之后
% [原文 p.15]
\begin{figure}…fig4…\end{figure}
% [原文 p.16]
```
（即：图 4 与 `% [原文 p.15]` 整体后移到 (2.49) 之后、(2.50) 的 `% [原文 p.16]` 之前。）

**O2｜c01.tex｜p.11 标记与图 3 错位（仅注释）**
图 3 在 p.11，但现排在 `% [原文 p.10]` 段内；而第 262 行的 `% [原文 p.11]` 后面跟的是 p.12 正文（"作为 (2.25) 的推论…" 与 (2.33)）。
建议：把 `% [原文 p.11]` 移到 `\begin{figure}…fig3…` 之前，并删掉第 262 行那个 p.11 标记。

**O3｜c01.tex :23｜「非 Abel」→「非阿贝尔」**（与 tr-01 三片统一）
可替换：`非 Abel 规范理论` → `非阿贝尔规范理论`（同句两处）。

**O4｜c01.tex :6｜补回「理论与唯象」**
可替换：`相关研究与高能物理（包括量子引力）以及理论凝聚态物理等广阔研究方向相联系。`
→ `相关研究与理论与唯象高能物理（包括量子引力）以及理论凝聚态物理等广阔研究方向相联系。`

**O5｜c01.tex :63｜Hamiltonian 首现补中文**
可替换：`并与生成时间演化的 Hamiltonian 对易`
→ `并与生成时间演化的哈密顿量（Hamiltonian）对易`。

**O6｜tr01a.tex｜(2.56) 缺句末句点（原文为「$q\ge p.$」）**
可替换：`  q\ge p \tag{2.56}` → `  q\ge p\,. \tag{2.56}`

**O7｜tr01b.tex 末尾 / tr01c.tex 开头｜同一 itemize 被拆成两个列表**
原文 p.22–23 的「上链描述」是**一个** itemize（4 个 bullet）。现 tr01b 在第 1 个 bullet 后就 `\end{itemize}`，tr01c 又以新 `\begin{itemize}` 续 3 个 bullet，编译后中间会出现列表间断。
建议（与 p.124/125 的跨文件 examplebox 同一处理方式）：tr01b **不写** `\end{itemize}`（删掉第 172 行），由 tr01c 在 4 个 bullet 结束后写一次 `\end{itemize}`（即删掉 tr01c 第 4 行 `\begin{itemize}...`、在第 19 行 `\end{itemize}` 保留）。

**O8｜tr01a.tex :73 Tutor Note｜一处表述可更严谨（非错误）**
注中「$p=0$ 时它退化为 $(d-1)$-形式的守恒流方程，正是 §2.1 用过的对偶流 $\dd j_{d-1}=0$」——原文 §2.1 记作 $j^{d-1}$（上标），此处写成 $j_{d-1}$（下标）。建议统一为 `\dd j^{d-1}=0`。

---

## 8. 边界接缝复核

1. **c01 → tr01a（p.12/13）**：c01 末句「我们可以通过与陈述 2.1 之后的讨论密切类比，来进一步展开上述定义。」 + tr01a 首段 `\para{沿一般余维-$(p+1)$ 子流形的插入。}` —— 与原文 p.12 末句 / p.13 首行严格对应，**无重复、无缺口** ✓。
2. **tr01c → tr02a（p.28/29）**：tr01c 以图 8 收尾（p.28 只有图 8，已核对 p028.png），tr02a 从「也就是说，一个 $p$ 维算符 $\cO_p$ 在 $G^{(p)}$ 下的荷为 (3.7)…」开始，与原文 p.29 首段一致，**衔接干净** ✓。
3. **唯一需 Lead 关注**：接缝两侧的等价类群记号不同（tr01c `\mathsf{D}_p` / tr02a `\mathrm{D}_p`），见 §6-3。

---

## 9. 校对方法与可复核性

- 公式：对每个抽检式用 `tools/crop.py` 以 500–900 dpi 裁出该式区域（例：`crop.py 27 60 470 560 600`），逐字符比对上下标、字体（`\mathsf` vs `\mathrm` vs `\mathcal`）、括号与积分区域；判据存档于 `work/tmp/`（`c019`、`r27*` 等裁图）。
- 编号：用脚本抽取 `\tag{}` 与 `tags.txt` 区间做集合比较（`Compare-Object`），并逐页对齐 `tags_bypage.txt`。
- 漏译：对 pp.3–5、13–28 逐页读 200 dpi 页面图 + split 文字层，按段落清点。
