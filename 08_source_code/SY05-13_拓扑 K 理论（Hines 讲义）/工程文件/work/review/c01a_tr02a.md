# 交叉校对报告 rv-3 —— c01a（原文 pp.1–2，Lead）与 tr02a（原文 pp.6–7，tr-02）＋全书一致性

- 校对者：rv-3（交叉校对）
- 校对对象：`work/src/chunks/c01a.tex`（6357 B）、`work/src/chunks/tr02a.tex`（11161 B）；全书一致性涉及 `c00 / tr01a / tr03a / tr03b / c-refs`
- 底本：`<本地路径>`（10 页，PDF 页号 = 印刷页码）
- 依据：200 dpi 页图 `work/pages/p001|p002|p006|p007.png`；文字层 `work/split/p00{1,2,6,7}.txt`；公式全部另用 `work/tools/crop.py` 裁 800–2000 dpi 原图逐符号复核，裁图留在 `work/tmp/rv3/`（见文末证据清单）
- 本报告只读校对，**未修改任何人的文件、未编译**
- 文件快照：c01a / tr02a 分别在 23:04:17 / 23:12:26 写入；**tr01a 在校对期间 23:18:11 仍有改动**，本报告对 tr01a 的结论以该时刻内容为准

---

## 0. 结论摘要

| 维度 | 结论 |
|---|---|
| 覆盖/漏译 | **两块覆盖率 100%**。pp.1–2、pp.6–7 逐段（含全部 bullet）对上，无漏段；三处方括号说明（`[The abelian group $G(A)$…]`、`[There is also the real K-theory…]`、以及 p.4 的 `[For a discussion…]`）均在；itemize（定义 1 两条；例子 p1 三条 + p2 一条合并；命题 3 证明两半跨块；定义 5 四条）结构完整，无漏 bullet、无整句未译 |
| 编号完整性 | **通过**。c01a = 定义 1、命题 1、定义 2；tr02a = 引理 1、定理 1、定义 5、定义 6、定理 2；全书 定义 1–8 / 命题 1–3 / 引理 1 / 定理 1–9 无跳号、无重号；交界 定义 2→定义 3、命题 3→引理 1、定义 4→定义 5、定理 2→定理 3 全部接上 |
| 公式 | c01a 核 17 条、tr02a 核 21 条。**发现 1 条实错**：c01a 定义 1 的 `(p∘φ^{-1})(u,v)=u` 漏下标 `i`（原文印作 `φ_i^{-1}`，1100 dpi 复核）。其余符号（上下标、`\cong`/`\xrightarrow`、`\widehat`/`\bar`、`\bigoplus`、`\bigvee`、`\prod`、`\C`/`\N`/`\Z` 黑板体等）逐条对上 |
| 批注 | 数量达标（c01a 4 条：p.1×3、p.2×1；tr02a 9 条：p.6×3、p.7×6）。**质量复核**：c01a 关于「加法公式应为 $(a+c,b+d)$」的批注**完全正确**（另有独立验证，见 §5.2）；tr02a 关于 `d` vs `\bar d`、`cohmology`、`additve` 的批注均**正确**，仅 `presepectrum` 一处的措辞「多一个 e、一个 s」**不成立**（实际只在 `pres` 后多插了一个 `e`） |
| 源码卫生 | **通过**。7 个 chunk 全部 UTF-8 无 BOM、纯 LF、无 U+FFFD；无 `\tag` / `\newcommand` / `\documentclass` / `\usepackage` / `$$`；除已知唯一跨块项外 `\begin/\end` 全配对、`$` 全成对（逐行校验，0 条奇数行） |
| 页码标记 | **6 处全部正确**：c01a p.1(L6)/p.2(L49)、tr01a p.3(L3)/p.4(L54)/p.5(L92)、tr02a p.6(L2)/p.7(L49)，与内容页逐段对应（p.2 标在 H 展示式之后 / p.5 标在跨页句中间 / p.7 标在 p.6 末尾展示式之后，均与 TIMELINE 裁决一致） |
| **必须改** | **4 条**（c01a×2、tr02a×2；其中 1 条为全书记号统一，牵动 tr01a/tr03a/tr03b） |
| 可选改 | 8 条（纯体例/字形级，零数学风险） |

一句话：**两块译文可以定稿**；须先清掉 4 条必须改（1 条公式下标 + 2 条批注事实错误 + 1 条 `\tilde/\widetilde` 全书不统一），可选改留待最后一轮统一处理。

---

## 1. 编号完整性表

### 1.1 本块

| 块 | 契约（BRIEF §1 / TIMELINE） | 实际出现（顺序） | 是否齐全 |
|---|---|---|---|
| c01a（pp.1–2） | 定义 1、命题 1、定义 2 | `defn{1}` L18 → `prop{1}` L82 → `defn{2}` L110 | ✅ 恰 3 个，无多无缺 |
| tr02a（pp.6–7） | 引理 1、定理 1、定义 5、定义 6、定理 2 | `lem{1}` L28 → `thm{1}` L38 → `defn{5}` L69 → `defn{6}` L84 → `thm{2}` L90 | ✅ 恰 5 个，无多无缺 |

### 1.2 跨块连续性

| 交界 | 契约 | 实际 | 结论 |
|---|---|---|---|
| 定义 2（c01a 末）→ 定义 3（tr01a） | 定义独立计数连续 | tr01a L82 `\begin{defn}{3}` | ✅ 接上 |
| 命题 3（tr01a L120）→ 引理 1（tr02a L28） | 引理单独起 1 | 全书仅 1 个 `lem`，号 = 1 | ✅ 接上 |
| 定义 4（tr01a L111）→ 定义 5（tr02a L69） | 连续 | 4 → 5 | ✅ 接上 |
| 定理 1（tr02a L38）→ 定理 2（L90）→ 定理 3（tr03a L9） | 连续 | 1 → 2 → 3 | ✅ 接上 |
| 命题 3 证明环境 | 唯一跨文件环境（TIMELINE 2026-11-04 裁决） | tr01a L137 开 `itemize`、L127 开 `proof` 且不闭合；tr02a L9 `\item {[单射性.]}`、L17 `\end{itemize}`、L18 `\end{proof}` | ✅ **按裁决实现，不报错**；且 □ 位置正确（原图 p.6 第一段末右缘方框） |

### 1.3 全书记号盘点（脚本枚举，非人工目测）

```
c01a : defn1 prop1 defn2
tr01a: prop2 defn3 defn4 prop3
tr02a: lem1 thm1 defn5 defn6 thm2
tr03a: thm3 thm4 thm5 thm6
tr03b: defn7 thm7 thm8 thm9 defn8
```
定义 1–8、命题 1–3、引理 1、定理 1–9 全部在位，**无跳号、无重号、无 `\tag`、无 `equation` 编号**，与 STYLE_GUIDE §0 的契约一致。

---

## 2. 逐符号核对表

> 判定记号：✅ 与 200–2000 dpi 原图逐符号一致；△ 一致但字形/标点有细微差别（不误导数学）；✗ 与原文不符。

### 2.1 A 块：c01a（原文 pp.1–2）

| # | 原文页 / 位置 | 原图（裁图复核） | c01a 现状 | 判定 |
|---|---|---|---|---|
| A1 | p.1 定义 1 首句 | $E\xrightarrow{p}B$ | L20 `$E\xrightarrow{p}B$` | ✅ |
| A2 | p.1 定义 1 bullet1 展示式 | $\phi:p^{-1}(U_i)\xrightarrow{\cong}U_i\times k^n$ | L23 同 | ✅（末尾多一个 `,`，无害） |
| A3 | p.1 定义 1 bullet1 第 2 行（**必看**） | $(p\circ\phi_i^{-1})(u,v)=u$ —— φ **带下标 i**（`rv3/p1_phi.png` 1100 dpi） | L24 `$(p\circ\phi^{-1})(u,v)=u$` | **✗ 缺下标 `i`**（见 M1） |
| A4 | p.1 定义 1 bullet2 | $\phi_j\circ\phi_i^{-1}\big\|_{(U_i\cap U_j)\times k^n}:(U_i\cap U_j)\times k^n\to(U_i\cap U_j)\times k^n$ | L26–27 同（用 `\big\|`） | ✅（原式末尾 `.` 未保留，△极微） |
| A5 | p.1 粘合段 | $g_{ij}:U_i\cap U_j\to\GL_n(\C)$；`cocycle condition` $g_{jk}\circ g_{ij}=g_{ik}$ on $U_i\cap U_j\cap U_k$ | L36–37 同 | ✅ |
| A6 | p.1 粘合段 | $\coprod_i E_i/\sim$（原图为 CM 的 `∐`：倒置 ∏ 形、顶端带衬线；PDF 该字符取自 CMEX10） | L38 `\bigsqcup_i E_i/\sim` | △ 字形不同（见 O1） |
| A7 | p.1 粘合段 | $(x,v)\sim(x,g_{ij}v),\quad x\in U_i\cap U_j$ | L39 同 | ✅ |
| A8 | p.1 例子 | $H=\{(L,v):L\in P^1(\C),\ v\in L\}$ | L48 同 | ✅ |
| A9 | p.1 例子 | $E=B\times k^n$ | L45 同 | ✅ |
| A10 | p.2 双分段式（左） | $\{E\oplus E'\xrightarrow{p\oplus p'}B$ / $(p\oplus p')^{-1}(b)=p^{-1}(b)\oplus p'^{-1}(b)$（左花括号，**组后带逗号**） | L58–64 结构、符号全同；`\right.` 后**无逗号** | ✅ 符号（△ 缺尾逗号，见 O2） |
| A11 | p.2 双分段式（右） | $\{E\otimes E'\xrightarrow{p\otimes p'}B$ / $(p\otimes p')^{-1}(b)=p^{-1}(b)\otimes p'^{-1}(b)$ | L66–72 同；`\right.` 后无逗号 | ✅（△ 同上） |
| A12 | p.2 粘合函数 | $\{g_{ij}\oplus g'_{ij}\in\GL_{n+m}(k)\},\ \{g_{ij}\otimes g'_{ij}\in\GL_{nm}(k)\}$ | L77 同（`n+m` / `nm` 均对） | ✅ |
| A13 | p.2 命题 1 交换三角形 | A（左上）→R′（右，水平）；A→R（右下斜）；R→R′（竖直向上）；无箭头标号 | L86–89 `A \arrow[r] \arrow[dr] & R' \\ & R \arrow[u]` | ✅ 三箭头方向/方位全对 |
| A14 | p.2 命题 1 证明 | $(a,b)\sim(a',b')$ 当且仅当 $\exists c\in A$：$a+b'+c=a'+b+c$ | L96–97 同 | ✅ |
| A15 | p.2 命题 1 证明 | **原文印作** $(a,b)+(c,d)=(a+b,c+d)$；$(a,b)\cdot(c,d)=(ac+bd,ad+bc)$ | L99 照原文排 + 批注指出应为 $(a+c,b+d)$ | ✅ 照排正确、批注正确（见 §5.2） |
| A16 | p.2 命题 1 证明 | $\{(a\oplus a')-(a+a'):a,a'\in A\}$ | L101 同 | ✅ |
| A17 | p.2 定义 2 | $X\mapsto K(X)$ 反变函子（原文 `**K-theory**` 加粗） | L111–113 文字全同；**未加粗** | △ 字体（见 O3） |

### 2.2 B 块：tr02a（原文 pp.6–7）

| # | 原文页 / 位置 | 原图（裁图复核） | tr02a 现状 | 判定 |
|---|---|---|---|---|
| B1 | p.6 [Injectivity] | $A_t(z_i)=(1-t)(z_1,z_2,z_3,\dots)+t(z_1,0,z_2,0,z_3,0,\dots),$ | L12 同（`gathered` 两行，行末 `,` / `.` 与原图一致） | ✅ |
| B2 | p.6 [Injectivity] | $B_t(z_i)=(1-t)(z_1,z_2,z_3,\dots)+t(0,z_1,0,z_2,0,z_3,0,\dots).$ | L13 同 | ✅ |
| B3 | p.6 [Injectivity] | $g_0\simeq A_1\circ g_0=:G_0$；$g_1\simeq B_1\circ g_1=:G_1$；$G_0\simeq G_1$ via $(1-t)G_0+tG_1$ | L16 同（`A_1\circ g_0` 复合顺序对） | ✅ |
| B4 | p.6 [Injectivity] | $f_t(x)=g_t(p^{-1}(x))$ | L9 同 | ✅ |
| B5 | p.6 分裂段 | $d:\Vect_\C(X)\to[X,\N]$，$d_E(x)=\dim p^{-1}(x)$，$\bar d:K(X)\to[X,\Z]$ | L22 同；`[X,\N]` 的 N 在 PDF 中取自 **MSBM10**（黑板体），用 `\N` 正确 | ✅ |
| B6 | p.6 分裂段 | $\widehat K(X)=\ker\bar d$；$K(X)=\widehat K(X)\oplus[X,\Z]$；$X=\bigcup_n f^{-1}(n)$ | L22 同（`\widehat` 宽帽，与原图 CMEX 宽帽一致） | ✅ |
| B7 | p.6 | $\Vect^s_\C(X)$ = colimit of $\Vect^k_\C(X)$ under $[E]\mapsto[E\oplus\epsilon]$ | L24 同（散文译「有向极限」，公式内保留 `colim`） | ✅ |
| B8 | p.6 引理 1 | $E\xrightarrow{p}X$、$E'\xrightarrow{p'}X$、$E\oplus E'$ trivial | L28 同 | ✅ |
| B9 | p.6 引理 1 证明 | $g_i:E\to\C^{n_i}$，$g(x,v)=\phi_i(x)v$，$g:E\to\bigoplus_i\C^{n_i}$，$G(e)=(p(e),g(e))$ | L31 同（`\bigoplus` 对照原图大 ⊕ 正确） | ✅ |
| B10 | p.6 定理 1 | $\widehat K(X)\cong\Vect^s_\C(X)\cong[X,BU]$；$K(X)\cong[X,BU\times\Z]$ | L39/L41 同 | ✅ |
| B11 | p.6 定理 1 证明 | $\phi_k:\Vect^k_\C(X)\to\widehat K(X)$，$\phi_k([E])=[E]-[\epsilon^k]$ | L46 同 | ✅ |
| B12 | p.6 定理 1 证明 | $[E_1\oplus E'_2]-[\epsilon^n]=[E_1]-[E_2]\in\widehat K(X)$ | L48 同 | ✅ |
| B13 | p.7 满射性 | 原文 $d([E_1\oplus E'_2])=d([\epsilon^n])=n$（此 `d` 应为 `\bar d`） | L50 照排 + 批注 L59 指出 | ✅ 照排正确、批注正确 |
| B14 | p.7 单射性 | $E\oplus\epsilon^{l+n}\cong E'\oplus\epsilon^{k+n}$ | L52 同 | ✅ |
| B15 | p.7 colim 链 | $\widehat K(X)\cong\Vect^s_\C(X)=\operatorname{colim}_k\Vect^k_\C(X)\cong\operatorname{colim}_k[X,BU_k]\cong[X,BU]$ | L55 全同（含末尾 `,`） | ✅ |
| B16 | p.7 | $i_k^*(E_k(\C^\infty))=E_k(\C^\infty)\oplus\epsilon$ | L56 同 | ✅ |
| B17 | p.7 定义 5 bullet1 | $\widetilde E^n(\Sigma X)\cong\widetilde E^{n-1}(X)$，natural in X | L71 同 | ✅（数值全对；`\tilde` vs `\widetilde` 见 M4） |
| B18 | p.7 定义 5 bullet3 | $\widetilde E^n(X\cup CA)\to\widetilde E^n(X)\to\widetilde E^n(A)$，（maps induced by inclusions, $CA$ the reduced cone on $A$） | L74–75 同 | ✅ |
| B19 | p.7 定义 5 bullet4 | $\widetilde E^n(\bigvee_\alpha X_\alpha)\cong\prod_\alpha\widetilde E^n(X_\alpha)$，induced by the inclusions | L76 同（`\bigvee` / `\prod` 与原图 ∨ / ∏ 一致） | ✅ |
| B20 | p.7 定义 6 | $\epsilon_n:E_n\to\Omega E_{n+1}$ | L84 同 | ✅ |
| B21 | p.7 定理 2 | 两处 $\widetilde E^n=[X,E_n]_*$（**原图两处展示式行末都有句点** `.`） | L91 无句点；L93 有句点 | △ 体例不一（见 O4） |

---

## 3. 结构 / 漏译

### 3.1 逐段对照（原文章节 → 译本对应）

**p.1（6 段）**：摘要段→L11–14 ✅；`1 Vector Bundles and K(X)`→L16 ✅；定义 1（含两 bullet）→L18–30 ✅；clutching functions 段→L35–41 ✅；`Some examples:` + 3 bullet + $H$ 展示式→L43–48 ✅；（标题/作者/日期由 c00 titlepage 承担，分工正确）

**p.2（9 段）**：Möbius bullet→L50–51 ✅；`The canonical bundle…will be important later.`→L54 ✅；additive/multiplicative 段 → L56–57 ✅；两组花括号展示式→L58–72 ✅；`the fibrewise sum and product…`→L73 ✅；clutching functions of $\oplus,\otimes$ 段 + 展示式→L75–77 ✅；`These operation give … semi-ring` + virtual bundles 段→L79–80 ✅；命题 1（含说明句 + 方括号 + 三角形）→L82–93 ✅；证明（等价关系 + 加乘定义 + 自由阿贝尔群 + □）→L95–102 ✅；`This ring of virtual bundles is our object of study.`→L108 ✅；定义 2（含 `[There is also the real K-theory…]`）→L110–114 ✅

**p.6（7 段）**：[Injectivity] bullet + $A_t/B_t$ 展示式 + $G_0/G_1$ 段 + □ → L9–18 ✅；`Here is another splitting…`→L22 ✅；`Denote by $\Vect^s_\C$…`→L24 ✅；引理 1→L28 + 证明→L31–32 ✅；`Finally, we have…`+定理 1→L36–42 + 证明→L44–57（续 p.7）✅

**p.7（6 段）**：满射性收尾→L50 ✅；单射性段（含方括号 $[F,F'$ 说明$]$）→L52 ✅；`Finally, we have` + colim 链 + 拉回兼容说明→L54–56 ✅；`\section{Bott 周期性与作为广义上同调理论的 $K$ 理论}` + `References for the following section…`→L65–67 ✅；定义 5（四条 bullet）→L69–78 ✅；`Representability…(proofs definitely omitted)`→L82 ✅；定义 6→L84 ✅；`The hard direction…`→L88 ✅；定理 2（两段 + 两展示式）→L90–94 ✅

### 3.2 方括号说明（任务点 3 指定）

| 原文 | 位置 | 现译 | 判定 |
|---|---|---|---|
| `[The abelian group $G(A)$ obtained from an abelian semi-group $A$ in the constuction below is called the **Grothendieck group** of $A$.]` | p.2 命题 1 后 | c01a L91–92（含 `\textbf{Grothendieck 群}`，还原原文粗体） | ✅ |
| `[There is also the real K-theory of $X$, denoted by $KO(X)$.]` | p.2 定义 2 末 | c01a L112–113 | ✅ |
| `[For a discussion of the characteristic maps, see [VBKT] proposition 1.17.]` | p.4 | tr01a L91（不属我块，抽查一致） | ✅ |
| `[We know that there is some bundle $F$ …]` | p.7 单射性 | tr02a L52 方括号原样保留 | ✅ |

### 3.3 itemize 完整性

| 列表 | 原文条目 | 译本条目 | 结论 |
|---|---|---|---|
| 定义 1 两 bullet | 2（局部乘积／转移线性） | c01a L22、L25 | ✅ |
| `Some examples:` | p.1 三条 + p.2 一条 = 4（跨页同一列表） | c01a L45–51 共 4 条 | ✅ 合并合理 |
| 命题 3 证明两半 | `[Surjectivity.]` + `[Injectivity.]`（跨文件） | tr01a L139 + tr02a L9 | ✅ 正好两条 |
| 定义 5 四性质 | 4（悬挂／同伦不变／正合／可加） | tr02a L71–76 共 4 条 | ✅ |

### 3.4 `% [原文 p.N]` 标记位置核对（任务点 4③）

| 标记 | 文件:行 | 内容页判定 | 结论 |
|---|---|---|---|
| p.1 | c01a:6 | 摘要之前，p.1 起始 | ✅ |
| p.2 | c01a:49 | 紧接 p.1 末尾展示式 $H=\{\dots\}$ 之后、Möbius bullet（p.2 首行）之前 | ✅ 精确 |
| p.3 | tr01a:3 | 块首 | ✅ |
| p.4 | tr01a:54 | p.3 末 bullet `K(pt.)=Z` 之后、$K(S^2)$ bullet（p.4 首行）之前 | ✅ 精确 |
| p.5 | tr01a:92 | 插在跨页句 `通过添加一列` ／ `零，…` 之间（p.4 末 → p.5 首） | ✅ 精确，且与 TIMELINE 一致 |
| p.6 | tr02a:2 | 块首 | ✅ |
| p.7 | tr02a:49 | p.6 末展示式 $[E_1\oplus E'_2]-[\epsilon^n]=\dots$ 之后、p.7 首句 `so that $d(\dots)$` 对应句之前 | ✅ 精确 |

---

## 4. 术语 / 记号一致性（全书 7 个 chunk 通读）

### 4.1 术语表（英文 → 出现的中译 → 建议）

| 英文 | 出现的中译（首现处） | 全书用法 | 建议 |
|---|---|---|---|
| vector bundle | 向量丛（c01a L19，glossary） | 一致（c01a/tr01a/tr02a/tr03b） | 保持 |
| base space / total space | 底空间／全空间（c01a L19） | 仅 c01a 出现一次，glossary 收录 | 保持 |
| local trivialization / trivialization | 局部平凡化／平凡化（tr01a L8/L35） | 一致 | 保持 |
| transition function | 转移映射（c01a L25；原文此句用 `Transitions`） | 仅此 1 处；glossary 条目为「转移函数」 | **建议**：正文「转移映射是线性的」可保留（原文偏口语），但若严格按 glossary 宜作「转移（映射）是线性的」并首现括注 `transition functions` |
| clutching function | 粘合函数（c01a L35，glossary） | 一致（c01a、tr01a） | 保持；见 O3（原文加粗） |
| cocycle condition | 上链条件（c01a L37） | 仅 c01a | 保持 |
| canonical bundle | 典范丛（c01a L47，tr01a L55/L82，tr03a L50） | 一致 | 保持；建议 p.1 首现补英文（见 O7） |
| Möbius bundle | Möbius 丛（c01a L50） | 仅此 | 保持 |
| tangent / normal bundle | 切丛／法丛（c01a L46） | 仅此 | 保持 |
| direct sum / tensor product | 直和／张量积（c01a L60/L68） | 一致 | 保持 |
| semi-ring | 半环（c01a L79；原文拼 `semi-ring`） | 一致 | 保持 |
| virtual bundle | 虚拟丛（c01a L80，首现括注英文） | 一致 | 保持 |
| Grothendieck group | Grothendieck 群（c01a L92，tr03b L55） | 一致 | 保持 |
| contravariant functor | 反变函子（c01a L113） | 一致 | 保持 |
| Grassmann manifold | Grassmann 流形（tr01a L82） | 一致 | 保持 |
| classifying space | 分类空间（c01a L12 摘要、tr01a L111、tr03a L12） | 一致 | 保持 |
| cell structure | 胞腔结构（tr01a L91） | 一致 | 保持 |
| partition of unity | 单位分解（tr01a L41、tr02a L31） | 一致 | 保持 |
| colimit / direct limit | 有向极限（散文；tr02a L24/L47…），公式保留 `\operatorname{colim}` | 一致（tr02a 内部两种英文同一译法，正确） | 保持 |
| reduced K-theory | 约化 $K$ 理论（tr01a L78） | 一致（tr02a「约化上同调理论」、tr03b「约化群」） | 保持 |
| suspension | 悬挂（tr02a L71/L80、tr03a L58） | 一致 | 保持 |
| generalized cohomology theory | 广义上同调（理论）（c01a L12、tr02a §3 标题、tr03a L24） | 一致 | 保持 |
| prespectrum / Ω-prespectrum | 预谱／$\Omega$-预谱（c01a L12 首现括注英文，tr02a L80/L84，tr03a L26） | 一致 | 保持 |
| spectrum | 谱（仅作「预谱」构词） | 一致 | 保持 |
| weak homotopy equivalence | 弱同伦等价（tr02a L84） | 仅此 | 保持 |
| exactness / additivity / homotopy invariance | 正合性／可加性／同伦不变性（tr02a L72–76） | 一致 | 保持 |
| reduced cone | 约化锥（tr02a L75） | 仅此 | 保持 |
| representability | 可表示性（tr02a L82、tr03a L29） | 一致 | 保持 |
| H-space | $H$-空间（c01a L13、tr03a L66） | 一致 | 保持 |
| splitting principle | 分裂原理（tr03b L9） | 一致 | 保持 |
| Adams operations | Adams 运算（tr03b L9） | 仅此 | 保持 |
| projective bundle / line bundle | 射影丛／线丛（tr03b L23/L15） | 一致 | 保持 |
| Gauss map | Gauss 映射（tr01a L127） | 仅此 | 保持 |
| kernel / cokernel | 核／余核（tr02a L22，tr03b L55） | 一致 | 保持 |
| class group / number ring | 类群／数环（tr03b L59） | 一致 | 保持 |
| compact Hausdorff | 紧 Hausdorff（tr01a L14/L120、tr02a L28、tr03a L28、tr03b L48） | 5 处全一致；无「紧致」变体 | 保持 |
| dimension | 维数（c01a L73、tr01a L91） | 一致 | 保持 |
| rank | 秩（tr01a L120） | 仅此 | 保持 |

**结论**：无「同一英文多译」的实质冲突（clutching、suspension、canonical bundle、reduced、vector bundle、Grassmann、Bott、Grothendieck、$H$-空间 九项全部单一译法）；章节标题 8 条与 BRIEF §3 **逐字一致**（已 grep 核对）；`K` 理论写法全用 `$K$ 理论`，无 `K理论` / `K-理论` 变体。

### 4.2 记号一致性（发现 1 处全书级不一致）

| 记号 | 原文字形 | 全书用法 | 建议 |
|---|---|---|---|
| 约化 $K$ / $\widetilde E$ 的波浪号 | **宽波浪号**（PDF 中取 CMEX10 accent；p.4 K̃、p.7 Ẽ 均已用字体比对确认为 `\widetilde`，不是 `\tilde`） | **混用**：`\tilde` 正文 33 处（tr01a L78×2、**tr02a 16 处**：L22/69×2/71×2/72×2/74×3/76×2/91/92×2/93、tr03a L38×3/45×4/49/55×3/56×2、tr03b L55/L59）；`\widetilde` 仅 2 处（都在 tr03a:27） | **统一为 `\widetilde`**（M4）。注意 `\tilde\mu`（tr03a L38/L42/L56）是 μ 上的窄波浪号，**不随** K/E 一起替换 |
| $\widehat K$ | 宽帽（CMEX10） | 全文 `\widehat`（tr02a L22/39/46/47/48/52/55 等） | ✅ 已一致 |
| $\bar d$ | `\bar`（CMR macron） | 全文 `\bar`（tr02a L22/L59 等），无 `\overline` | ✅ 已一致 |

---

## 5. 必须改（4 条）

> 每条给：文件 + 原文页 + 位置 + 原文/原图描述 + 现状 + **可直接替换的文本**。

### M1　c01a：定义 1 的 $(p\circ\phi^{-1})$ 漏下标 $i$

- **文件**：`work/src/chunks/c01a.tex`
- **原文页 / 位置**：p.1，定义 1 第一条 bullet 第 2 行（文件第 **24** 行）
- **原图描述**：1100 dpi 裁图 `work/tmp/rv3/p1_phi.png` 明确印作 $(p\circ\phi_i^{-1})(u,v)=u$ —— **φ 带下标 i**（文字层 `work/split/p001.txt` 同一处抽作 `(p ◦φ−1` + 次行 `i )(u, v) = u.`，两源互证）。同一 bullet 上方的展示式则是**不带下标**的 $\phi$，原文自身只有这一处不统一。
- **现状**：`      使得 $(p\circ\phi^{-1})(u,v)=u$。`
- **替换为**：
  ```latex
        使得 $(p\circ\phi_i^{-1})(u,v)=u$。
  ```

### M2　c01a：定义 1 的批注把原文读错（与 M1 联动）

- **文件**：`work/src/chunks/c01a.tex`
- **原文页 / 位置**：p.1，文件第 **31–33** 行（`% [Tutor Note: …]` 三行）
- **原图描述**：原文三处写法为：①展示式 $\phi$（无下标）；②同 bullet 的 $(p\circ\phi_i^{-1})$（**有**下标）；③bullet2 的 $\phi_j\circ\phi_i^{-1}$（有下标）。现批注说「紧随其后的公式写 $(p\circ\phi^{-1})(u,v)=u$」——与原文不符（原文有下标），且「三处下标不一致」应改为「仅第一处展示式不带下标」。
- **现状**：
  ```latex
  % [Tutor Note: 定义 1 第一条里原文写作 “there is a an open cover”，冠词重复（原文笔误，照译未改）。
  % 另：第一条的展示式用 $\phi$（无下标），而紧随其后的公式写 $(p\circ\phi^{-1})(u,v)=u$、
  % 第二条用 $\phi_j\circ\phi_i^{-1}$，三处下标不一致；按上下文应统一为 $\phi_i$。正文照原文排，此处注明。]
  ```
- **替换为**：
  ```latex
  % [Tutor Note: 定义 1 第一条里原文写作 “there is a an open cover”，冠词重复（原文笔误，照译未改）。
  % 另：第一条的展示式写作不带下标的 $\phi$，但同一 bullet 紧接着的 $(p\circ\phi_i^{-1})(u,v)=u$ 与
  % 第二条的 $\phi_j\circ\phi_i^{-1}$ 都带下标（1100 dpi 裁图逐字复核：原文确有下标 $i$）；按上下文
  % 第一处展示式应读作 $\phi_i$，正文照原文保留无下标的 $\phi$，此处注明。]
  ```

### M3　tr02a：`presepectrum` 批注描述有误（「多一个 e、一个 s」不成立）

- **文件**：`work/src/chunks/tr02a.tex`
- **原文页 / 位置**：p.7，定义 6 后的批注（文件第 **86** 行）
- **原图描述**：1000 dpi 裁图 `work/tmp/rv3/p7_def6.png` 清楚印作 `An Ω-presepectrum`；与正确拼写 `prespectrum` 逐字比对为 **`pres` + `e` + `pectrum`**，即只在 `pres` 之后多插了 **一个 `e`**，没有多余的 `s`。
- **现状**：`把 prespectrum 拼成 "presepectrum"（多一个 e、一个 s）`
- **替换为**（把该括号内容整段替换）：
  ```latex
  （在 `pres` 之后多插了一个 `e`，正确拼写为 prespectrum）
  ```
  即该句读作：
  ```latex
  % [Tutor Note: p.7 原文定义 6 把 prespectrum 拼成 "presepectrum"（在 pres 之后多插了一个 e，正确拼写为 prespectrum），经 1400 dpi 裁图逐字复核确认（非连字误读），正文按其数学含义译作「$\Omega$-预谱」，拼写可疑处记入译注汇总。…
  ```

### M4　全书：$\widetilde K$ / $\widetilde E$ 的宽波浪号不统一（tr02a 16 处，牵动 3 个文件）

- **文件 / 位置**：`tr02a.tex` 正文 **16 处**（L22×1、L69×2、L71×2、L72×2、L74×3、L76×2、L91×1、L92×2、L93×1）；同一问题另见 `tr01a.tex` L78×2、`tr03a.tex` L38×3/45×4/49×1/55×3/56×2、`tr03b.tex` L55/L59 各 1
- **原文页 / 依据**：p.4 K̃、p.7 Ẽ 的波浪号在 PDF 中取自 **CMEX10**（宽波浪号，即 `\widetilde`），已用 `chars.py` 读字符字体确认（p.4 该 accent 宽 6.1 pt、居中覆盖 K；p.7 同）；tr03a:27 已写成 `\widetilde E^n / \widetilde K^n`，可作**基准**。全书现状：`\tilde` 正文 33 处 vs `\widetilde` 仅 2 处。
- **现状**：同一记号在 book 内两种字形（`\tilde K` 与 `\widetilde K` 并存；`\tilde E` 与 `\widetilde E` 并存）
- **可直接替换**（机械替换，数学零风险；`\tilde\mu` 不动）：
  ```text
  tr02a.tex : \tilde K → \widetilde{K} ；\tilde E → \widetilde{E}   （正文 16 处）
  tr01a.tex : 同（L78 两处）
  tr03a.tex : 同（L38/45/49/55/56 共 13 处）；\tilde\mu 保持
  tr03b.tex : 同（L55/L59 各 1 处）
  tr03a.tex : L27 已是 \widetilde，不动
  ```
  PowerShell 参考（逐文件执行，`-NoNewline` 保 LF）：
  ```powershell
  $p='...\tr02a.tex'; $s=Get-Content -Raw $p
  $s=$s -replace '\\tilde K','\widetilde{K}' -replace '\\tilde E','\widetilde{E}'
  Set-Content -Path $p -Value $s -NoNewline -Encoding utf8NoBOM
  ```
  > 若 Lead 决定反过来统一成 `\tilde`（更省事但与原文字形不符），则只需改 tr03a:27 一处即可；**建议按原文取 `\widetilde`**。

---

## 6. 可选改（8 条，体例/字形级）

### O1　c01a：$\coprod$ 被写成 $\bigsqcup$

- 文件/位置：`c01a.tex` L38（p.1 粘合段）
- 原图：原字符为 **CM 的 ∐**（倒置 ∏ 形、两竖顶端带横向衬线；PDF 中取自 CMEX10），裁图 `work/tmp/rv3/g_coprod.png`（1800 dpi）。
- 现状：`$\bigsqcup_i E_i/\sim$ 是 $X$ 上的向量丛`
- 替换为：`$\coprod_i E_i/\sim$ 是 $X$ 上的向量丛`
- 影响：数学等价（都表示无交并），仅字形差异；若严格执行 STYLE_GUIDE §3「逐符号」，建议改。

### O2　c01a：两组分段式后缺原文的尾随逗号

- 文件/位置：`c01a.tex` L58–72（p.2）
- 原图：两个左花括号组各自的第 2 行末尾**都有逗号**（`rv3/p2_cases.png`）。
- 现状：两处 `\right.` 后直接换行，无 `,`
- 替换为：把第 64 行与第 71 行的 `\right.` 改为 `\right.,`

### O3　c01a：原文两处加粗未还原

- 文件/位置：`c01a.tex` L35（p.1 `via **clutching functions**`）、L111（p.2 `is the **K-theory** of $X$`）
- 依据：`rv3/p1_cluthbold.png`（1400 dpi）、`rv3/p2_def2.png`（900 dpi）确认原文加粗；全书先例：tr01a L78 `\textbf{约化 $K$ 理论}`、tr03b L9 `\textbf{Adams 运算}（Adams operations）`、L23 `\textbf{分裂原理}` 均还原了原文粗体。
- 现状 / 替换：
  - L35 `人们也可以用粘合函数（clutching functions）如下地定义` → `人们也可以用\textbf{粘合函数}（clutching functions）如下地定义`
  - L111 `称为 $X$ 的 $K$ 理论（$K$-theory）` → `称为 $X$ 的 \textbf{$K$ 理论}（$K$-theory）`
- 注：原文 `virtual bundles`（p.2）是斜体，按 preamble「中文不用斜体」不强求；英文括注可考虑 `\emph`。

### O4　tr02a：定理 2 两处展示式句末标点不一致

- 文件/位置：`tr02a.tex` L91（p.7 第一式）
- 原图：`rv3/p7_thm2a.png` / `p7_thm2b.png` 显示两处展示式行末**都**有 `.`
- 现状：L91 `\[ \tilde E^n = [X, E_n]_* \]`（无句点）；L93 有句点
- 替换为：`\[ \widetilde{E}^n = [X, E_n]_*. \]`（与 M4 一并做）

### O5　tr02a：建议补批注——定义 5「同伦不变性」的箭头方向是原文笔误

- 文件/位置：`tr02a.tex` L72（p.7 定义 5 bullet2）
- 原图：`rv3/p7_def5a.png` 印作 `if $f\simeq g:(X,x_0)\to(Y,y_0)$ then $f^*=g^*:\widetilde E^*(X)\to\widetilde E^*(Y)$`
- 问题：$\widetilde E^*$ 是**反变**函子，$f,g:X\to Y$ 应诱导 $\widetilde E^*(Y)\to\widetilde E^*(X)$；原文方向写反。现译文照排（正确），但**未出批注**（STYLE_GUIDE §5 要求原文笔误须给正确形式 + 判断依据）。
- 建议在该 bullet 后加（可直接粘贴）：
  ```latex
  % [Tutor Note: p.7 定义 5 第二条的箭头方向是原文笔误：$f\simeq g:(X,x_0)\to(Y,y_0)$ 诱导的应是 $\widetilde E^*(Y)\to\widetilde E^*(X)$（$\widetilde E^*$ 为反变函子，见定义 5 首句 "contravariant functors"），原文印作 $\widetilde E^*(X)\to\widetilde E^*(Y)$。判断依据：同一条 bullet 里 $f^*=g^*$ 的右侧必须与 $f$ 的靶空间一致；正合性一条的箭头 $X\cup CA\to X\to A$ 也按反变方向排列。正文照原文排。]
  ```

### O6　c01a：批注漏记第 5 处原文拼写笔误 `These operation`

- 文件/位置：`c01a.tex` L106（p.2 证明末批注末句）
- 原图：`rv3/p2_semiring.png`（900 dpi）印作 `These operation give the isomorphism classes…`（主语复数，应为 `These operations`）
- 现状：批注只列了 homorphism / constructin / constuction / isomophism 四处
- 替换为（在该批注末句补一句）：
  ```latex
  % …另 p.2 正文 "These operation give …" 的 "operation" 应为 "operations"（主谓一致，900 dpi 复核）。]
  ```

### O7　c01a：术语首现缺英文括注（经典术语）

- 文件/位置：`c01a.tex` L46–47（p.1 例 2、例 3）
- 现状：`光滑流形的切丛与浸入流形的法丛；` / `$P^1(\C)$ 上的典范丛（过 $\C^2$ 原点的直线），`
- 建议：至少给全书重点术语 `canonical bundle` 补括注（与 glossary 对齐；tr01a/tr03a 后续都在用「典范丛」）：
  - `$P^1(\C)$ 上的典范丛（canonical bundle，过 $\C^2$ 原点的直线），`
  - 可选：`光滑流形的切丛（tangent bundle）与浸入流形的法丛（normal bundle）；`
- 注：属全书体例问题（tr01a 亦无括注），若 Lead 决定「只在术语表统一」则可不动。

### O8　c00 / STYLE_GUIDE：前附件与 §2 禁止清单的字面冲突

- 文件/位置：`work/src/chunks/c00.tex` L4 `\begin{titlepage}`、L55 `\tableofcontents`
- 现状：STYLE_GUIDE §2 的字面禁止清单含 `\title`/`\tableofcontents`；c00 是 Lead 独占的前附件，用 `titlepage`+`\tableofcontents` 属**有意设计**（编译验证由 Lead 负责）。
- 建议：不改代码，只在 STYLE_GUIDE §2 加一句豁免：「c00（前附件）例外，可用 `titlepage`/`\tableofcontents`/`\pagenumbering`」。避免后续校对再报同一「违规」。

---

## 7. 复核结论（任务点 5 专项）

### 7.1 c01a「加法公式」批注 —— **正确**

批注（L103–106）称：原文印作 $(a,b)+(c,d)=(a+b,c+d)$，应为 $(a+c,b+d)$。复核：

1. **原文确实是 $(a+b,c+d)$**：1400 dpi 裁图 `rv3/p2_addmul2.png` 逐字确认（非文字层误读）。
2. **独立验证（比批注更强的证据）**：按原文那个式子，运算在等价类上**不良定义**。取 $A=\N$：$(1,3)\sim(2,4)$（因 $1+4+c=2+3+c$ 对任意 $c$ 成立），但用原式
   $(1,3)+(5,0)=(1+3,\,5+0)=(4,5)$，$(2,4)+(5,0)=(2+4,\,5+0)=(6,5)$，
   而 $(4,5)\sim(6,5)$ 当且仅当 $\exists e:4+5+e=6+5+e$，即 $9=11$，不成立。故原式与 $\sim$ 不相容。
   按正确式 $(a+c,b+d)$：$(1,3)+(5,0)=(6,3)$、$(2,4)+(5,0)=(7,4)$，且 $6+4+e=7+3+e$ ⟺ $10=10$ ✅ 相容。
3. **与乘法式的相容性**：$(a,b)\cdot(c,d)=(ac+bd,ad+bc)$ 恰是 $(a-b)(c-d)$ 的「正部／负部」，批注这条判据也成立。
4. 结论：**批注无需修改**；正文照原文排 + 批注指出，符合 STYLE_GUIDE §8.1。

### 7.2 tr02a 三处笔误批注 —— **正确（仅 presepectrum 措辞需修，见 M3）**

| 批注对象 | 批注说法 | 复核 |
|---|---|---|
| `d` vs `\bar d`（L59） | p.7 写 $d([E_1\oplus E'_2])$，但 $d$ 只定义在 $\Vect_\C(X)$ 上，应为 $\bar d$ | ✅ 正确。且批注的「自洽核对」也成立：$[E_1\oplus E'_2]$ 秩为 $n$（由 $[E_1]-[E_2]\in\ker\bar d$ 得两秩相等），故属 $\Vect^n_\C(X)$，与 $\phi_n$ 定义域相符 |
| `cohmology`（L96） | 首句行末断作 `cohmol-` + `ogy`，应为 cohomology；同页另有写对的 `cohomology` 互证 | ✅ 正确（裁图 `p7_thm2a.png` 确认，且"Representability of cohomology theories…"一处拼写正确） |
| `additve`（L96） | 后半应为 additive | ✅ 正确（`p7_thm2b.png` 确认） |
| `we definitely omitted`（L96） | 不是笔误，是 `fi` 连字 | ✅ 正确（文字层 `deﬁnitely` 只是连字；印刷确为 definitely） |
| `presepectrum`（L86） | 「多一个 e、一个 s」 | ✗ **措辞错**：只多一个 `e`（见 M3）；拼写可疑这一**判断本身正确** |

---

## 8. 源码卫生（逐项 pass，证据为脚本扫描）

| 检查项 | c01a | tr02a | 说明 |
|---|---|---|---|
| UTF-8 解码 / 无 U+FFFD | pass | pass | 7 个 chunk 全部通过 |
| 无 BOM | pass | pass | 首字节非 `EF BB BF` |
| 纯 LF（无 CRLF / 孤立 CR） | pass（0 / 0） | pass（0 / 0） | |
| 无 `\tag` / `\newcommand` / `\documentclass` / `\usepackage` / `\begin{document}` / `$$` | pass | pass | |
| `$` 成对（逐行） | pass | pass | 每行 `$` 计数均为偶数，0 条异常 |
| `\begin/\end` 配对 | pass | pass（例外：`\end{itemize}` L17、`\end{proof}` L18 为 TIMELINE 裁定的跨文件环境，**不计错**） | tr01a 侧对应未闭合的 `proof`(L127)/`itemize`(L138) 亦属同一裁定 |
| `\left/\right` 配对 | pass | pass | c01a 两处 `\left\{…\right.` 均成对 |
| `\begin{tikzcd}/\end{tikzcd}` | pass（L86/L89） | —（本块无图） | |
| markdown 语法（`**`、`##`） | pass | pass | |

> 编译不在本报告范围；`main.tex` 的 include 顺序为 c00→c01a→tr01a→tr02a→tr03a→tr03b→c-refs，**正好满足跨文件环境的先后**，无需调整。

---

## 9. 证据清单（本轮新增裁图，均在 `work/tmp/rv3/`）

| 文件 | 用途 |
|---|---|
| `p1_phi.png`（1100 dpi） | 定义 1 的 $\phi$ 展示式与 $(p\circ\phi_i^{-1})$ 下标（M1、M2 依据） |
| `p1_bullet2.png`（1000 dpi） | bullet2 的 $\phi_j\circ\phi_i^{-1}\big|_{\dots}$ |
| `p1_coprod.png` / `g_coprod.png`（1000/1800 dpi） | `∐` 字形（O1 依据）+ `g_{jk}\circ g_{ij}=g_{ik}` |
| `p1_cluthbold.png`（1400 dpi） | `clutching functions` 原文加粗（O3） |
| `p1_ex.png`（900 dpi） | p.1 例子 + $H$ 展示式 |
| `p2_cases.png`（900 dpi） | 两组分段式与尾随逗号（O2） |
| `p2_addmul2.png`（1400 dpi） | $(a,b)+(c,d)=(a+b,c+d)$ 原文（§7.1） |
| `p2_clutchgl.png`（1200 dpi） | $\{g_{ij}\oplus g'_{ij}\in\GL_{n+m}(k)\}$ 等 |
| `p2_freerel.png`（1300 dpi） | $\{(a\oplus a')-(a+a'):a,a'\in A\}$ |
| `p2_semiring.png` / `p2_def2.png`（900 dpi） | `These operation` 笔误（O6）、`**K-theory**` 加粗（O3） |
| `p6_AB.png`（1000 dpi） | $A_t,B_t$ 两式 |
| `p6_G.png`（900 dpi） | $g_0\simeq A_1\circ g_0=:G_0$ 等 |
| `p6_split.png`（800 dpi） | $d/\bar d/\widehat K$、$[X,\N]$、$\bigcup_n f^{-1}(n)$ |
| `p6_lemproof.png`（800 dpi） | 引理 1 证明、$\bigoplus_i\C^{n_i}$ |
| `p6_phi.png` / `p6_thm1.png`（900/1100 dpi） | $\phi_k([E])=[E]-[\epsilon^k]$、定理 1 两式 |
| `p7_def5a/b.png`（900 dpi） | 定义 5 四性质 |
| `p7_def6.png`（1000 dpi） | `presepectrum`（M3 依据） |
| `p7_thm2a/b.png`（900 dpi） | 定理 2 两式与两处笔误（§7.2、O4） |
| `p7_colim.png`（900 dpi） | colim 链 |

**工具脚本**（本报告自用，未改动项目脚本）：`work/tmp/rv3/dump.py`（页内行 bbox）、`chars.py`（字符字体/坐标）、`lint.py`（卫生检查）、`tilde.py`、`cnt.py`。

---

## 10. 回执摘要（给 Lead）

1. 我块（c01a、tr02a）**可以定稿**：覆盖 100%、编号完整、跨块接续正确、源码卫生全 pass。
2. **必须改 4 条**：M1（c01a 定义 1 漏下标 $i$）、M2（c01a 该批注把原文读错）、M3（tr02a `presepectrum` 批注「多一个 e、一个 s」→ 只有一个 e）、M4（全书 `\tilde`→`\widetilde`，tr02a 16 处 + tr01a 2 + tr03a 13 + tr03b 2）。
3. **可选改 8 条**：`\coprod` 字形、分段式尾逗号、原文两处加粗、定理 2 展示式句点、定义 5 箭头方向笔误补批注、`These operation` 补记、术语英文括注、c00 与 STYLE_GUIDE §2 的豁免说明。
4. 专项复核：c01a 加法公式批注**完全正确**（附了不良定义的反例）；tr02a 的 $d$ vs $\bar d$ / `cohmology` / `additve` 三条批注**正确**，仅 `presepectrum` 措辞需修。
5. 全书一致性问题只有 1 处（M4 记号），术语层面无「同一英文多译」；章节标题与 BRIEF §3 逐字一致；7 处 `% [原文 p.N]` 位置全部正确。
