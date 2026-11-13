# 交叉校对报告：Lead 块 c00 / c01a–c01d（tr-06 校对，只读，未改动任何 .tex）

校对者：**tr-06**　｜　被校对象：`c00.tex`、`c01a.tex`、`c01b.tex`、`c01c.tex`、`c01d.tex`
（原文印刷 pp.1–9 / PDF pp.2–10 上半；tag 区间 2.1–2.19）
方法：逐页对 `work/pages/pNNN.png` 目视，关键符号用 `crop.py` 以 470–1600 dpi 裁图复核；
并用脚本核对 tag、页标记、脚注、结构、禁用命令。

---

## 一、结论摘要

| 项目 | 结论 |
|---|---|
| 编号公式完整性 | **通过**。2.1–2.19 共 19 条，与 `tags_final.txt` 逐条对齐；无缺、无重、无自造、无跳号；(2.13) 正确置于脚注内 |
| 公式逐符号（19 条全部核对） | **18 / 19 通过**；**1 条符号错误**：(2.9) 末尾 $K$ 应为花体 $\cK$ |
| 其它符号错误 | **2 处**：§2.5 A-扭转守恒超荷漏 $\overline{\ }$ ；§2.6 Riemann 曲率定义中横杠位置整体错位 |
| 页码标记 | **4 处问题**（1 处重复、2 处错位、1 处偏晚）；详见末节 |
| 脚注 | **6 条原文脚注全部齐全**，但**多出 1 条**：c01d 把译者批注写成了 `\footnote`（原文印刷 p.7 无脚注），总数 7 条 ≠ 6 条 |
| 漏译 | **未发现**漏译（逐句比对 p002–p010 文字层；p.10 只取到 §2.7 末句，未侵入 tr-01 的 §3） |
| 结构 | **通过**：§1、§2、2.1–2.7 七个 `\subsection` 齐全；`\subsection{$A$ 与 $B}$` 的 A/B 为斜体 ✓；两个 `\para` 到位；**无图**；c01d 结尾正好止于 §2.7 末句，**无** `\section{T-对偶}` |
| 术语 | 与 `glossary.tsv` 一致（逐项见表六）；仅 3 个未入表的新词需 Lead 回写 |

**总计：必须改 8 项，可选改 8 项。**

---

## 二、编号公式完整性表（对 `tags_final.txt`）

| tag | 印刷页（PDF 页） | 文件:行 | 图像核对 | 状态 |
|---|---|---|---|---|
| 2.1 | p.1（2） | c01a:26 | ✓ | OK |
| 2.2 | p.1（2） | c01a:29 | ✓ | OK |
| 2.3 | p.1（2） | c01a:34 | ✓ | OK |
| 2.4 | p.1（2） | c01a:35 | ✓ | OK |
| 2.5 | p.1（2） | c01a:43 | ✓ | OK |
| 2.6 | p.2（3） | c01a:54 | ✓ | OK |
| 2.7 | p.3（4） | c01b:5 | ✓ | OK |
| 2.8 | p.3（4） | c01b:29 | ✓ | OK |
| 2.9 | p.4（5） | c01b:35 | ✗ $K\to\cK$ | **须改 M4** |
| 2.10 | p.4（5） | c01b:38 | ✓ | OK |
| 2.11 | p.4（5） | c01b:41 | ✓ | OK |
| 2.12 | p.5（6） | c01c:11 | ✓ | OK |
| 2.13 | p.6（7）脚注内 | c01c:51 | ✓ | OK（在 `\footnote` 内的 `equation` 里） |
| 2.14 | p.6（7） | c01c:58 | ✓ | OK |
| 2.15 | p.6（7） | c01c:67 | ✓ | OK |
| 2.16 | p.6（7） | c01c:68 | ✓ | OK |
| 2.17 | p.7（8） | c01d:31 | ✓ | OK |
| 2.18 | p.7（8） | c01d:35 | ✓ | OK |
| 2.19 | p.7（8） | c01d:39 | ✓ | OK |

脚本核验：tags 总数 19，`missing=[]`、`extra=[]`、`dups=[]`；正文引用一律纯文本（无 `\ref`/`\eqref`）✓。

---

## 三、逐符号核对表（全部 19 条 + 关键行内式，均对原图核对）

| 式号 | 原文（据 470–1600 dpi 图像） | 现状 | 判定 |
|---|---|---|---|
| (2.1) | $\{Q_\pm,\overline Q_\pm\}=H\pm P,$ | 同 | ✓ |
| (2.2) | all other anticommutators $=0.$ | `\text{其余所有反对易子}=0.` | ✓（译法，见 O6） |
| (2.3) | $[F_V,Q_\pm]=-Q_\pm,\ [F_V,\overline Q_\pm]=\overline Q_\pm,$ | 同 | ✓ |
| (2.4) | $[F_A,Q_\pm]=\mp Q_\pm,\ [F_A,\overline Q_\pm]=\pm\overline Q_\pm.$ | 同 | ✓ |
| (2.5) | $Q_A:=\overline Q_++Q_-,\quad Q_B:=\overline Q_++\overline Q_-.$ | 同 | ✓（横杠位置完全正确） |
| (2.6) | $Q^2=0,\quad [F,Q]=Q.$ | 同 | ✓ |
| 行内 | $i[M,H\pm P]=\mp2(H\pm P)$ | `\mp 2(H\pm P)` | ✓（1400 dpi 确认左为 ∓、括号内为 ±） |
| 行内 | $i[M,Q_\pm]=\mp Q_\pm$、$i[M,\overline Q_\pm]=\mp\overline Q_\pm$ | 同 | ✓ |
| 行内 | A-type: $Q_A$ and $Q_A^\dagger$ conserved | `$Q_A^\dagger$` | ✓ |
| (2.7) | $\langle\cO(x)\cO(y)\rangle=\dfrac{1}{\mathrm{dist}(x,y)^{2\Delta_{\cO}}}$ | 同 | ✓ |
| (2.8) | $\langle\cO_1(x)\cO_2(y)\rangle=\dfrac{G(v_1,v_2)}{\mathrm{dist}(x,y)^4}$ | 同 | ✓ |
| (2.9) | $\Delta_D\cL=Q_+Q_-\overline Q_-\overline Q_+\mathcal K,$ | `...+\overline Q_+K,`（正体 K） | **✗ M4** |
| (2.10) | $\Delta_A\cL=Q_+\overline Q_-\cO_A$ and its adjoint, | `\text{及其伴随},` | ✓ |
| (2.11) | $\Delta_B\cL=Q_+Q_-\cO_B$ and its adjoint, | `\text{及其伴随},` | ✓ |
| 行内 | $\hat c=c/3$；$c_{\rm UV}\ge c_{\rm IR}$ | 同 | ✓ |
| (2.12) | $\delta\cO=i\epsilon_+Q_-\cO-i\epsilon_-Q_+\cO-i\bar\epsilon_+\overline Q_-\cO+i\bar\epsilon_-\overline Q_+\cO.$ | 同 | ✓（正负号、横杠全部一致） |
| (2.13) | $S=\dfrac{1}{2\pi}\int_\Sigma \dd^2x\,\cL$（脚注内） | 同 | ✓ |
| (2.14) | 第 1 行 $g_{i\bar j}(\partial_0\phi^i\partial_0\bar\phi^{\bar j}-\partial_1\phi^i\partial_1\bar\phi^{\bar j}+i\bar\psi^{\bar j}_-(D_0+D_1)\psi^i_-+i\bar\psi^{\bar j}_+(D_0-D_1)\psi^i_+)$ | 同 | ✓ |
| (2.14) | 第 2 行 $+R_{i\bar jk\bar l}\psi^i_+\psi^k_-\bar\psi^{\bar j}_-\bar\psi^{\bar l}_++2\pi(\phi^*B)_{10}$ | 同 | ✓（指标次序、横杠全对） |
| 行内 | $D_\mu\psi^i_\pm=\partial_\mu\psi^i_\pm+\partial_\mu\phi^j\Gamma^i_{jk}\psi^k_\pm$ | 同 | ✓ |
| 行内 | $R_{i\bar jk\bar l}=-g_{\bar lm}(R_{i\bar j})^m{}_k$ | `-g_{l\bar m}(R_{i\bar j})^{\bar m}{}_k` | **✗ M6** |
| (2.15) | $\delta\phi^i=\epsilon_+\psi^i_--\epsilon_-\psi^i_+$ | 同 | ✓ |
| (2.16) | $\delta\psi^i_\pm=\pm i\bar\epsilon_\mp(\partial_0\pm\partial_1)\phi^i+\epsilon_\pm\Gamma^i_{jk}\psi^j_+\psi^k_-$ | 同 | ✓ |
| 行内 | $\delta\bar\phi^{\bar\imath}=\bar\psi^{\bar\imath}_-\bar\epsilon_+-\bar\psi^{\bar\imath}_+\bar\epsilon_-=-\bar\epsilon_+\bar\psi^{\bar\imath}_-+\bar\epsilon_-\bar\psi^{\bar\imath}_+$ | 同 | ✓ |
| 行内 | $[\omega]\to[\omega']=[\omega]+c_1(X)\log(\mu'/\mu)$；$\hat c=\dim_\C X$ | 同 | ✓ |
| 行内 | $\omega=\frac{i}{2\pi}g_{i\bar j}\dd z^i\wedge\dd\bar z^{\bar j}$；$\exp(-i\int_\Sigma\phi^*B)$；$\exp(-\int_\Sigma\phi^*(\omega-iB))$ | 同 | ✓ |
| (2.17) | 第 1 行 $\sum_{i=1}^N(|\partial_0x^i|^2-|\partial_1x^i|^2+i\bar\psi^i_-(\partial_0+\partial_1)\psi^i_-+i\bar\psi^i_+(\partial_0-\partial_1)\psi^i_+)$ | 同 | ✓ |
| (2.17) | 第 2 行 $-\frac14\sum|\partial_iW(x)|^2-\frac12\sum(\psi^i_+\psi^j_-\partial_i\partial_jW(x)+{\rm c.c.})$ | 同 | ✓（系数 1/4、1/2 与 c.c. 均正确） |
| (2.18) | $\delta x^i=\epsilon_+\psi^i_--\epsilon_-\psi^i_+$ | 同 | ✓ |
| (2.19) | $\delta\psi^i_\pm=\pm i\bar\epsilon_\mp(\partial_0\pm\partial_1)x^i-\frac12\epsilon_\pm\overline{\partial_iW(x)}$ | 同 | ✓（$\overline{\partial_iW(x)}$ 上划线位置正确） |
| 行内 | $W(\lambda^Rx)=\lambda^2W(x)$；$\lambda^Rx=(\lambda^{R_1}x_1,\dots,\lambda^{R_N}x_N)$；$\hat c=\tr(1-R)$ | 同 | ✓ |
| 行内 | $\fM^{0,c}_A$、$\fM^{0,c}_B$（哥特体 𝔐，上标 $0,c$） | `\fM^{0,c}_A` | ✓（`\fM` 已在 preamble 定义） |
| 行内 | $\R/2\pi\Z$、$\R/2\pi i\Z$、$\mathbb{F}$ 等 | 同 | ✓ |

注：`z^i` 处原文为 $z^i$；c01c 写作 `z^i` ✓；`\bar\imath` 与原文 `\bar\imath` 一致 ✓。

---

## 四、结构核对

| 检查项 | 结果 |
|---|---|
| `\section{引言}`（§1） | ✓ c01a:3 |
| `\section{二维 $(2,2)$ 超对称量子场论}`（§2） | ✓ c01a:9 |
| 2.1 二维 $(2,2)$ 超对称 | ✓ c01a:14 |
| 2.2 `$A$ 与 $B$`（A、B 斜体） | ✓ c01a:38，斜体符合原图 |
| 2.3 重整化群流 | ✓ c01a:77 |
| 2.4 形变 | ✓ c01b:18 |
| 2.5 拓扑扭转 | ✓ c01c:2 |
| 2.6 例子 | ✓ c01c:31 |
| 2.7 镜像对称 | ✓ c01d:69 |
| `\para{非线性 sigma 模型}` | ✓ c01c:40 |
| `\para{Landau--Ginzburg 模型}` | ✓ c01d:18 |
| 本块不应有图 | ✓ 全文无 `\includegraphics`（fig1/2 在 tr-01，正确未侵入） |
| 块尾接缝 | ✓ c01d 正文止于"这些例子中的一些推论已在数学上得到证明。"（§2.7 末句）；**无** `\section{T-对偶}`，未重复 tr-01 |
| 禁用命令 | ✓ 无 `\documentclass/usepackage/begin{document}/newcommand/**` |
| 编码 | ✓ 五个文件均为 UTF-8 无 BOM、LF，无 U+FFFD |
| 括号/环境平衡 | ✓ 脚本逐行核过（花括号、`$`、`\left/\right`、`begin/end`） |

---

## 五、漏译检查（逐页 §2.x 对照 p002–p010 文字层）

| 印刷页（PDF） | 原文内容要点 | 结果 |
|---|---|---|
| p.1（2） | §1 引言全段；§2 导语；2.1 首段；Lorentz/R-荷 对易关系；(2.1)–(2.5)；脚注 1（central terms） | 全部译出，脚注 ✓ |
| p.2（3） | (2.6)；chiral ring 段；半 Minkowski 边界条件 A/B-type；A-膜/B-膜段；范畴段；脚注 1（Z₂ 分次）、脚注 2（anomaly [1]）；2.3 开头 | 全部译出，两脚注 ✓ |
| p.3（4） | RG 流续；标度不变；(2.7)；维数；共形不变；中心荷 $c$；ĉ=c/3；2.4 Deformations 整节至 (2.8) | 全部译出 |
| p.4（5） | (2.9)–(2.11) 及解说；脚注 1（twisted F-term/F-term 术语）；D/A/B-项 对应关系；exactness 段；SCFT 中 D-项无关；$\fM_A,\fM_B$ 段；$\fM^0_A,\fM^0_B$；2.5 标题 + 首段 | 全部译出，脚注 ✓ |
| p.5（6） | 超对称延续段；(2.12)；协变化讨论；拓扑扭转整段；$\Sigma$ 上拓扑场论；拓扑弦论/拓扑引力；2.6 标题；Non-linear sigma model 标题 + 首段 | 全部译出 |
| p.6（7） | 场变量；拉氏量 (2.14)；脚注 1 含 (2.13)；脚注 2（Kähler 类归一化）；坐标/协变导数/曲率；(2.15)(2.16)；复共轭例；R-对称异常与 Ricci 流；ĉ=dim_ℂX；手征环表（R_A, R_B, C_A, C_B） | 全部译出，两脚注 ✓ |
| p.7（8） | $\fM^{0,c}_A,\fM^{0,c}_B$ 表；子流形段；RG low 段；Gromov–Witten/Calabi–Yau；Landau–Ginzburg 模型标题 + 设定；(2.17)–(2.19)；拟齐次/矢量 R-对称；ĉ=tr(1−R)；R_A = ? | 全部译出；**但原文此页无脚注**（见 M7） |
| p.8（9） | R_B/C_A/C_B/M_A/M_B 表；The lecturer does not know…；B-扭转段；拟齐次+FJRW 段；2.7 标题 + 两段（至 "a non-Calabi-"） | 全部译出 |
| p.9（10 上半） | "Yau target and the Landau-Ginzburg model, and the one between Landau-Ginzburg orbifolds. Some of the consequences in these examples are mathematically proven."（其后 §3 属 tr-01） | ✓ 恰好收在此句，未越界 |

**脚注清点**：p.1×1、p.2×2、p.5×1、p.6×2 = **6 条**，全部存在且内容准确；
另 c01d:10 多出 1 条 `\footnote`（译者批注，原文无），须改为注释（M7）。

---

## 六、术语核对（对 glossary.tsv）

| 英文 | 译文（c01 实际） | glossary | 判定 |
|---|---|---|---|
| chiral ring | 手征环 | 手征环 | ✓ |
| A-brane / B-brane | A-膜 / B-膜 | A-膜 / B-膜 | ✓ |
| topological twist / A-twist / B-twist | 拓扑扭转 / A-扭转 / B-扭转 | 同 | ✓ |
| Zamolodchikov metric | Zamolodchikov 度规 | 同 | ✓ |
| D-term / A-term / B-term | D-项 / A-项 / B-项 | 同 | ✓ |
| Kähler (potential/class/manifold) | Kähler 势 / Kähler 类 / Kähler 流形 | 同 | ✓ |
| Fukaya category | Fukaya 范畴 | 同 | ✓ |
| matrix factorization | 矩阵分解 | 同 | ✓ |
| supercharge / R-charge / R-symmetry | 超荷 / R-荷 / R-对称性 | 同 | ✓ |
| vector / axial R-symmetry | 矢量 / 轴 R-对称性 | 同 | ✓ |
| charge integrality | 荷整性 | 同 | ✓ |
| marginal / irrelevant / relevant | 边缘的 / 无关的 / 相关的 | 同 | ✓ |
| exactly marginal / marginally irrelevant | 精确边缘的 / 边缘无关的 | 同 | ✓ |
| scale invariant / conformal invariance | 标度不变 / 共形不变 | 同 | ✓ |
| central charge | 中心荷 | 同 | ✓ |
| moduli space | 模空间 | 同 | ✓ |
| orbifold | 轨形 | 同 | ✓ |
| primitive form / versal deformation | 原始形式 / 泛形变 | 同 | ✓ |
| canonical bundle / holomorphic line bundle | 典范丛 / 全纯线丛 | 同 | ✓ |
| quasi-homogeneous / Morse function | 拟齐次 / Morse 函数 | 同 | ✓ |
| B-field | B-场 | 同 | ✓ |
| topological gravity / topological string theory | 拓扑引力 / 拓扑弦论 | 同 | ✓ |
| derived category | 导出范畴 | 同 | ✓ |
| quantum cohomology | 量子上同调 | 同 | ✓ |
| Wick rotation / covariant derivative / Levi-Civita | Wick 转动 / 协变导数 / Levi-Civita | 同 | ✓ |
| Dirac fermion | Dirac 费米子 | 同 | ✓ |
| non-linear sigma model / Landau-Ginzburg model | 非线性 sigma 模型 / Landau–Ginzburg 模型 | 同 | ✓ |

**未入 glossary 的新译法（建议 Lead 回写）**：
1. twisted $F$-term → 扭 F-项（原文脚注 p.5 术语说明）
2. polyvector fields → 多向量场（p.6 表："cohomology ring of polyvector fields"）
3. A-model / B-model（拓扑）→ A-模型 / B-模型（p.6、p.8）

---

## 七、必须改（8 项，均给出可直接替换文本）

### M1. 页标记 `% [原文 p.3]` 错位 16 行（印刷 p.3 / PDF p.4）
- **原文位置**：印刷 p.3 首行是 "the behaviour of the theory changes — it may be identified as the behaviour of a different theory before the change of the scale."（即 c01b 第 1 行）。
- **现状**：`c01b.tex:17` 才出现 `% [原文 p.3]`（紧接 `\subsection{形变}`），导致 c01b:1–16（含 (2.7)、(2.8)、ĉ=c/3 段）落在 c01a:51 的 `% [原文 p.2]` 之后，被误标为印刷 p.2。
- **替换**：删除 `c01b.tex` 第 17 行 `% [原文 p.3]`；在 `c01b.tex` 第 1 行 `理论的行为就会改变——…` 之前插入一行
  ```
  % [原文 p.3]
  ```

### M2. 页标记 `% [原文 p.5]` 过早约 7 行（印刷 p.5 / PDF p.6）
- **原文位置**：印刷 p.4 末尾是 "2.5 Topological Twists" 标题 + 首段（"The theory can be formulated not just on the (half of) Minkowski space. … Furthermore, we may formulate the"）；印刷 p.5 从跨页句的后半 "system on a two-dimensional manifold with an arbitrary metric and spin structure, via the standard covariantization." 起，其后的新句才是 "Does the supersymmetry survive?"。
- **现状**：`c01c.tex:1` 即 `% [原文 p.5]`，但其后 2.5 标题与首段（c01c:2–7）实为印刷 p.4 的内容。
- **替换**：删除 `c01c.tex` 第 1 行 `% [原文 p.5]`；在 `c01c.tex` 第 8 行 `超对称还能存活吗？…` 之前插入
  ```
  % [原文 p.5]
  ```
  （若想严格贴住换页处，可放在第 7 行 `进一步，我们可以通过标准的协变化…` 之前，因为该句跨 pp.4–5；二者择一即可，建议后者加批注说明跨页。）

### M3. 重复的页标记 `% [原文 p.8]`（c01d）
- **现状**：`c01d.tex:46` 与 `c01d.tex:68` 各有一个 `% [原文 p.8]`；`2.7 镜像对称` 标题位于印刷 p.8 之内（印刷 p.8 = PDF p.9，从数组第二行 `\cR_B` 起至 "…a non-Calabi-" 止），不是新页起点。
- **替换**：删除 `c01d.tex` 第 68 行的
  ```
  % [原文 p.8]
  ```

### M4. (2.9) 的 $K$ 应为花体 $\cK$（印刷 p.4 / PDF p.5）
- **原文**：$\Delta_D\cL=Q_+Q_-\overline Q_-\overline Q_+\mathcal K,$（末符号为花体 $\mathcal K$；600 dpi 与 1100 dpi 两次数图均确认带花笔，且 p.5 正文 "for scalar operators $\mathcal K,\cO_A$ and $\cO_B$, where $\mathcal K$ is arbitrary" 同为花体）。
- **现状**：`c01b.tex:35` `  \Delta_D\cL=Q_+Q_-\overline Q_-\overline Q_+K, \tag{2.9}`；`c01b.tex:43` `其中 $K$ 是标量算子且任意，…`
- **替换**：
  ```
    \Delta_D\cL=Q_+Q_-\overline Q_-\overline Q_+\cK, \tag{2.9}
  ```
  ```
  其中 $\cK$ 是标量算子且任意，$\cO_A$ 是 \emph{A-手征的}，$\overline Q_+ \cO_A=Q_-\cO_A=0$；
  ```

### M5. §2.5 A-扭转守恒超荷漏横杠（印刷 p.5 / PDF p.6）
- **原文**："In the A-twisted (resp. B-twisted) theory, the supercharges **$\overline Q_+$** and $Q_-$ and hence their sum $Q=Q_A$ (resp. $\overline Q_\pm$ and their sum $Q=Q_B$) are conserved."（700 dpi 裁图：第一个超荷的 $Q$ 上确有横杠；与 (2.5) $Q_A=\overline Q_++Q_-$ 自洽）。
- **现状**：`c01c.tex:23` `在 A-扭转（相应地 B-扭转）理论中，超荷 $Q_+$ 与 $Q_-$、从而它们的和 $Q=Q_A$`
- **替换**：
  ```
  在 A-扭转（相应地 B-扭转）理论中，超荷 $\overline Q_+$ 与 $Q_-$、从而它们的和 $Q=Q_A$
  ```

### M6. Riemann 曲率定义的横杠位置错（印刷 p.6 / PDF p.7）
- **原文**：$R_{i\bar jk\bar l}=-g_{\bar l m}(R_{i\bar j})^{m}{}_{k}$（1400 dpi 裁图：$g$ 的下标为 $\bar l m$，横杠在 $l$ 上、$m$ 无杠；$(R_{i\bar j})$ 的上标为 $m$、无杠。指标自洽：$g_{\bar l m}$ 与 $(R)^{m}$ 收缩掉全纯指标 $m$，剩下 $\bar l$ 与 $k$，正好与左端的 $k\bar l$ 匹配）。
- **现状**：`c01c.tex:63` `$R_{i\bar jk\bar l}=-g_{l\bar m}(R_{i\bar j})^{\bar m}{}_k$ 是 $TX$ 的 Riemann 曲率。`
- **替换**：
  ```
  $R_{i\bar jk\bar l}=-g_{\bar l m}(R_{i\bar j})^{m}{}_{k}$ 是 $TX$ 的 Riemann 曲率。
  ```

### M7. 译者批注误写成 `\footnote`（印刷 p.7 / PDF p.8；原文该页无脚注）
- **原文**：印刷 p.7 通页无脚注；原句为 "When $c_1(X)\neq 0$, there is an RG low on $\fM^{0,c}_A$ in the direction of $c_1(X)$, and the shift in the direction of $ic_1(X)$ is absorbed by the axial rotaion."（"low"、"rotaion" 两处原文笔误）。
- **现状**：`c01d.tex:10–11`
  ```
  在 $\fM^{0,c}_A$ 上存在沿 $c_1(X)$ 方向的 RG 流\footnote{原文此处作 "there is an RG low"，
  其中 "low" 应为 "flow" 之笔误。}，
  ```
  这会**印出一条脚注**，使本块脚注数由原文的 6 条变成 7 条，且与本工程"批注一律为 `% [Tutor Note: …]` 注释"（STYLE_GUIDE §5、c00 译者说明第 5 条）自相矛盾。
- **替换**：正文改回
  ```
  在 $\fM^{0,c}_A$ 上存在沿 $c_1(X)$ 方向的 RG 流，
  ```
  并在该段之后另起一行加注释：
  ```
  % [Tutor Note: 印刷 p.7 原文此处作 "there is an RG low"，其中 "low" 应为 "flow"（同句 "rotaion" 应为 "rotation"）；译文按正确含义处理，未改动原文。]
  ```

### M8. c00 笔误举例的页码与拼写有误
- **原文实际**：PDF p.16（印刷 p.15）"empolyed" ✓；PDF p.30（印刷 **p.29**）"non-negtaive integer"（拼写为 **negtaive**）；PDF p.43（印刷 **p.42**）"it must be ture for the general model"。
- **现状**：`c00.tex:66` `  系原文如此；（二）原文若干明显笔误（如 p.15 "empolyed"、p.28 "negtative"、p.41 "ture" 等）`
- **替换**：
  ```
    系原文如此；（二）原文若干明显笔误（如 p.15 "empolyed"、p.29 "negtaive"、p.42 "ture" 等）
  ```

---

## 八、可选改（8 项，不改也成立）

**O1.** `c01a.tex:17` 的 `% [原文 p.1]` 偏晚 14 行：其前的 §1、§2 标题与 2.1 标题也属印刷 p.1。建议把标记移到 `c01a.tex:3` 的 `\section{引言}` 之前（属"首块首页"情形，影响很小）。

**O2.** `c01d.tex:46` 的 `% [原文 p.8]` 提前 1 行：原文印刷 p.8（PDF p.9）从数组第二行 `\cR_B = \mathrm{Jac}(W) …` 起，第一行 `\cR_A = ?,` 是印刷 p.7 的末行。若不影响可读性可保留；严格起见可把标记下移到 `\cR_B` 行之前。

**O3.** `c01d.tex:81–83` 的 p.9 标记把 `Calabi--` 与 `Yau` 拆在两行之间：
```
$h^{p,q}(X)=h^{n-p,q}(Y)$，其中 $n=\dim X=\dim Y$。其他众所周知的例子包括：以非 Calabi--
% [原文 p.9]
Yau 靶为靶的 sigma 模型与 …
```
原稿换行会在 "Calabi–" 后产生一个空格（排版成 "Calabi– Yau"）。建议第 81 行行尾加注释符，即改为 `…以非 Calabi--%`（紧跟 `%` 吃掉换行），或把标记移到整句之后。

**O4.** 批注里的数学未加 `$…$`（`c01a.tex:45–49`、`c01c.tex:34–38`，如 `Q_A²={Q_-,Q_-}+…`、`e^{πiF}`、`E⊗T_Σ^{⊗q/2}`）。注释不参与编译，但《译注汇总.md》抽取后会显示裸 LaTeX；建议统一加 `$…$`（与 c01b:45 等批注风格一致）。

**O5.** `c01d.tex:91–93` 第三条 Tutor Note 结尾 `R_i+R_j=2−2+... 可交叉检验` 语义不完整（推导写到一半），建议补完或删去该半句，以免《译注汇总》出现残缺论证。

**O6.** (2.2) 正文式用中文 `\text{其余所有反对易子}=0.`（原文为英文 "all other anticommutators = 0."）。这符合"不留英文整句"的规则，可保留；若希望公式栏与原文形式完全一致，可作双语 `\text{其余所有反对易子（all other anticommutators）}=0`。非错误。

**O7.** 虚数单位：c01b/c01c 多处用裸 `i`（如 `$i\epsilon_+$`、`$\frac{i}{2\pi}$`、`$-i\int_\Sigma$`）而未用宏 `\ii`。当前 preamble 已把 `\ii` 定义为斜体 `i`，两者输出完全相同，故仅为源码风格不统一；若要统一，请注意勿把指标 $i,j,k$ 一并替换。

**O8.** `c00.tex:16` 单位行漏了原文的 ", Japan"（原文 "Kavli IPMU, University of Tokyo, Japan"）。属标题页装饰性信息，可补可省。

---

## 九、备注（供 Lead 参考，不属本块）

- 本次校对**未修改任何 `.tex`**；所有引用的行号基于校对时刻（2026-11-05 10:20 前后）的文件内容。
- 建议在统一编译前先修 M4/M5/M6（三处数学符号），因为它们会影响审读者对公式的判断；M1–M3、M7 是机械问题但会造成页码/脚注口径不一致；M8 是元信息错误。
- 本块原文脚注 6 条的页码分布为：p.1、p.2（×2）、p.5、p.6（×2）——修 M7 后即与之一致，可作为验收判据。
- 关键裁图证据（供复核，非排版素材）：
  - `work/review/evidence/ev_2.9_scriptK_600dpi.png` —— (2.9) 末尾花体 $\mathcal K$（M4）
  - `work/review/evidence/ev_2.5_atwist_Qbar_700dpi.png` —— A-扭转守恒超荷 $\overline Q_+$（M5）
  - `work/review/evidence/ev_curvature_bars_1400dpi.png` —— $g_{\bar l m}(R_{i\bar j})^{m}{}_k$ 横杠位置（M6）
  - `work/review/evidence/ev_2.12_700dpi.png` —— (2.12) 全式（与正文逐符号一致，无问题）
