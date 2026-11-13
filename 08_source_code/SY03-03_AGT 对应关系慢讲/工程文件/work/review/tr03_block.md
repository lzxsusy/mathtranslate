# 校对报告：tr-03 块（原文 pp.38–50；`tr03a.tex` / `tr03b.tex` / `tr03c.tex`）

校对人：tr-08　｜　日期：2026-11-03　｜　底本：arXiv:2006.14025v3（`work/pages/p038–p050.png` 200 dpi + 关键公式 700–900 dpi 局部放大）
核对依据：`work/tags_bypage.txt`、`work/split/p038–p050.txt`、原 PDF 图像、`work/glossary.tsv`。
**未改动 tr03a/b/c 任何字节。**

## 0. 结论速览

| 项 | 结果 |
|---|---|
| tag 完整性 | **33/33 全对**：4.19–4.28（10 条）+ 5.1–5.23（23 条），顺序、页归属与 `tags_bypage.txt` p038–p050 完全一致，无重、无漏、无自造 |
| 公式逐符号 | 33 条全部与图像核对；**1 处符号缺失**（M1：(5.1) 的 $\overline{C}$） |
| 结构 | Part II 标题、§5 标题、4.3/4.4/5.1/5.2 小节、2 个要点框、脚注 35–41、习题 4.8–4.14 与 5.1–5.3 **全部在位** |
| 漏译 | **未发现**漏译的整句/整段/脚注 |
| 术语 | 与 `glossary.tsv` 一致；未发现误译 |

必须改 **1** 条（M1，一个字符级修正，但属符号错误）；可选改 **5** 条（O1–O5）。

---

## 1. 必须改

### M1 —— p.43 式 (5.1)：关联函数的下标是 $\overline{C}$（带横线），译文漏了横线

- 位置：`tr03b.tex:47–48`
- **原文**（p.43，900 dpi 放大确认；同时见 p.9 的 (1.8)，两处都是带横线的 $\overline{C}$）：
  $$Z_{S^4_b}\big(\mathrm{T}(\mathfrak{su}(2),C,m)\big)=\Big\langle\widehat V_{\alpha_1}(z_1)\cdots\widehat V_{\alpha_n}(z_n)\Big\rangle^{\mathrm{Liouville}}_{\overline C}.$$
  这里下标是**紧致化曲线 $\overline C$**（穿刺曲线 $C=\overline C\setminus\{z_i\}$ 的紧致化），与 $C$ 不是同一个对象；p.44 正文「a 2d Liouville CFT correlator on the Riemann surface $C$」用的是 $C$，而 (5.1) 的下标刻意写成 $\overline C$。
- **现状**：`…\Big\rangle^{\mathrm{Liouville}}_{C}.` —— 下标写成了 $C$。
- **建议改法**（整式替换，`tr03b.tex:46–50`）：

```latex
\begin{equation}
  Z_{S^4_b}\big(\mathrm{T}(\fsu(2),C,m)\big)
  =\Big\langle\widehat{V}_{\alpha_1}(z_1)\dots\widehat{V}_{\alpha_n}(z_n)\Big\rangle^{\mathrm{Liouville}}_{\overline{C}}.
  \tag{5.1}
\end{equation}
```

> **顺带（跨块）**：Lead 块 `c01.tex:262–264` 的式 (1.8) 同样漏了这个横线（原文 p.9 的 (1.8) 是 $\overline C$，已 900 dpi 复核）。两处是同一记号，建议一并把 `_{C}` 改成 `_{\overline{C}}`，否则译本内部不一致。

---

## 2. 可选改

### O1 —— p.42 式 (4.26) 的箭图比原图少一个 $\mathrm{U}(1)$ 味节点
- 位置：`tr03a.tex:224–245`（TikZ）
- **原文**（p.42，800 dpi 放大）：上排共 **5 个 U(1) 方框**——左端叉口 1 个、两节点之间 1 个、"···" 左右各 1 个、右端叉口 1 个；即 `U(1) — N — U(1) — N — U(1) — ··· — U(1) — N — U(1)`（3 个圆角 SU(N) 节点 + 省略号）。
- **现状**：TikZ 只有 4 个 U(1)（`UL`、`U12`、`U23`、`UR`），其中 `U23` 在 G2 与省略号之间，**省略号与 G3 之间没有 U(1)**。
- **建议**：在 `tr03a.tex:234` 之后插入一行、并在 `tr03a.tex:241` 之后补一条竖线：

```latex
  \node[fl] (U34) at (4.65,0.95) {$\mathrm{U}(1)$};
…
  \draw (U34.south) -- (4.65,0);
```

（这样省略号两侧各有一个 U(1)，与原图一致；纯示意图，不影响任何公式含义。）

### O2 —— 两处页标注位置偏晚（STYLE_GUIDE §8：每页有标注即合规，故非必须）
- `tr03a.tex:83` 的 `% [原文 p.39]` 在其后、(4.21) 之后；但 (4.21) 本身就印在 p.39 上（`tags_bypage` p039: 4.21, 4.22），所以 p.39 的标注应移到 (4.21) 之前。
- `tr03c.tex:41` 的 `% [原文 p.48]` 在 (5.11) 之后；但 (5.11) 印在 p.48 上（`tags_bypage` p048: 5.11, 5.12, 5.13），标注应移到 (5.11) 的 `\begin{equation}` 之前（p.47 恰好在其前一句中间换页：「…Q-closed (namely V is invariant under the bosonic」）。

### O3 —— 三个公式末尾标点与原文不符（统一体例时一并处理即可）
| 式 | 页 | 原文 | 现状 |
|---|---|---|---|
| (4.21) | p.39 | 图后有一个句点「$\cdot$」再是 (4.21) | `tr03a.tex:75` `\end{tikzpicture}` 后缺 `.` |
| (4.27) | p.42 | 无标点 | `tr03a.tex:254` 末尾多了 `,` |
| (5.4) | p.45 | 无标点 | `tr03b.tex:107` 末尾多了 `,` |
| (5.9) | p.46 | 无标点 | `tr03b.tex:149` 末尾多了 `,` |
建议：删掉 (4.27)/(5.4)/(5.9) 末尾的逗号、给 (4.21) 补句点（`…\end{tikzpicture}.` 或 `\end{tikzpicture}\,.`）。

### O4 —— p.40 习题 4.11 的小问编号：原文印作 1., 2., 2., 3.（第三问重复 "2."）
- `tr03a.tex:132–139` 用 `enumerate[label=\arabic*.]` 自动编号为 1.–4.，并在 `tr03a.tex:141` 加了批注说明原文面貌。
- 现状**可接受**（批注已尽到说明义务）；若严格执行「原文笔误照译」体例，可改成 `\item[1.]`、`\item[2.]`、`\item[2.]`、`\item[3.]` 的手工标号。二选一，不必两者都做。

### O5 —— 建议补一条批注：p.47 "on-shell" 疑为原文笔误
- 原文（p.47，200 dpi 复核）：`For highly supersymmetric theories (such as 4d N = 2), realizing all supersymmetries **on-shell** requires infinitely many auxiliary fields, but only a finite number are typically needed to realize a single supercharge off-shell.`
- 逻辑上前半句应为 **off-shell**（4d $\cN=2$ 要在**壳外**实现全部超对称需无穷多辅助场；而实现单个超荷只需有限多个）。译文 `tr03c.tex:26` 忠实照译为「要在壳上实现全部超对称需要无穷多个辅助场」，但没有指出这处疑误。
- 建议在 `tr03c.tex:26` 后加：

```latex
% [Tutor Note: p.47 原文 “realizing all supersymmetries on-shell requires infinitely many auxiliary fields” 中
% 的 “on-shell” 疑为笔误，应为 “off-shell”：4d N=2 的全部超对称要在壳外实现需无穷多辅助场，
% 而单个超荷只需有限多个辅助场即可在壳外实现，后半句的对比也指向 off-shell。译文照原文处理。]
```

---

## 3. 已逐条核对通过（供复检时省事）

### 3.1 tag 完整性（33/33，脚本比对）
- `tr03a`：4.19, 4.20, 4.21, 4.22, 4.23, 4.24, 4.25, 4.26, 4.27
- `tr03b`：4.28, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9
- `tr03c`：5.10–5.23
- 与 `tags_bypage.txt` p038–p050 的期望序列**逐项相等**（脚本输出 MATCH，missing=[]，extra=[]）；页归属也对：p38(4.19,4.20)、p39(4.21,4.22)、p40(无)、p41(4.23,4.24)、p42(4.25,4.26,4.27)、p43(4.28,5.1)、p44(5.2)、p45(5.3–5.5)、p46(5.6–5.9)、p47(5.10)、p48(5.11–5.13)、p49(5.14–5.18)、p50(5.19–5.23)。

### 3.2 公式逐符号核对（33/33，重点项加粗）
| 式 | 页 | 核对结果 |
|---|---|---|
| (4.19) | 38 | $z=O(m_1^2/u),\ z=q+O(m_2^2/u),\ z=1+O(m_3^2/u),\ z=O(u/m_4^2)$ ✔ 四式的分子分母方向都对（第四式是 $u/m_4^2$，不是 $m_4^2/u$） |
| (4.20) | 38 | $q=\lambda(\tau_{\rm IR})=16e^{\pi i\tau_{\rm IR}}-128e^{2\pi i\tau_{\rm IR}}+\dots$；$\tau=\frac12\tau_{\rm IR}+\frac{\log16}{2\pi i}-\frac{8}{2\pi i}e^{\pi i\tau_{\rm IR}}+\dots$ ✔ 系数 16/−128/−8、指数 $\pi i\tau_{\rm IR}$ vs $2\pi i\tau_{\rm IR}$ 均对 |
| **(4.21)** | 39 | TikZ 三图 ✔：①`q`：四味框直连中央 SU(2)；②`1/q`：上排两条连**交叉**（左上→节点右侧、右上→节点左侧），下排直连；③`1−q`：上二连 `north`、下二连 `south`；味标号 2/1/3/4 位置与原文三图**逐一相同**；标签 `q` 在下、`1/q` 在下、`1−q` 在节点右侧 ✔ |
| **(4.22)** | 39 | TikZ ✔：`T(su(2),CP¹\{0,z₁,z₂,1,∞})=`＋两个圆角 SU(2) 节点＋**5 个** SU(2) 味框（左上、左下、上中、右上、右下各一）；上中味框自 `M.south` 竖线落到两节点连线上 ✔ |
| **(4.23)** | 41 | TikZ ✔：中央 `SU(N)`，左 U(1)/SU(N)、右 U(1)/SU(N) 四味框；LHS `T(su(N),CP¹\4pt,合适的数据)` ✔ |
| (4.24) | 41 | $\varphi(z)\sim(\frac{m_i}{z-z_i}+O(1))dz\Longrightarrow\phi_k(z)=(\frac{(-1)^{k+1}\sigma_k(m_i)}{(z-z_i)^k}+O(\frac{1}{(z-z_i)^{k-1}}))dz^k$ ✔ $(-1)^{k+1}$、极点阶 $k$ 与 $k-1$ 全对 |
| (4.25) | 42 | 两行 $O(\frac{1}{(z-z_i)^{k-1}})dz^k$（满）/ $O(\frac{1}{z-z_i})dz^k$（单），右侧中文标签 ✔ |
| **(4.26)** | 42 | TikZ ✔：LHS 带 `\underline{z_1}`、`\underline{z_{n-2}}`（单穿刺点加下划线）；`gathered` 排版；箭头/连线与 `(4.26)` 编号位置 ✔（只差 O1 的一个 U(1)） |
| (4.27) | 42 | $x^N=\sum_{k=2}^N\frac{P^{(k)}_{n-4}(z)}{(z-z_1)\cdots(z-z_{n-2})z^{k-1}}x^{N-k}$ ✔ 分子 $n-4$ 次、分母 $z^{k-1}$ 与 $n-2$ 个因子均对 |
| **(4.28)** | 43 | TikZ 膜图 ✔：3 条 NS5 竖线、每段 $N$（=3）条粗 D4、两端半无限 D4；四组 D4 的相对高度分布与原文**一致**（左端：一高一低双线；第一段：高/中/低；第二段：最高/中/最低；右端：上/中/下）；`NS5`/`D4` 标签位置 ✔ |
| **(5.1)** | 43 | 除 M1 的 $\overline C$ 外全部正确：$Z_{S^4_b}(\mathrm{T}(\mathfrak{su}(2),C,m))=\langle\hat V_{\alpha_1}(z_1)\cdots\hat V_{\alpha_n}(z_n)\rangle^{\rm Liouville}_{\overline C}$ |
| (5.2) | 44 | $\mathfrak{osp}^*(2|4)\subset\mathfrak{su}^*(2|4)$ ✔（与上一段 $\mathfrak{su}^*(4|2)$ 的指标顺序差异是**原文如此**，tr03b 的批注已正确指出） |
| (5.3) | 45 | $\nabla_\mu Y_\nu+\nabla_\nu Y_\mu=\frac2d g_{\mu\nu}\nabla_\rho Y^\rho$ ✔ |
| (5.4) | 45 | $D_\mu G^\mu:=\nabla_\mu G^\mu+\frac14\omega_\mu{}^{ab}\gamma_a\gamma_b G^\mu=0$ ✔ |
| (5.5) | 45 | $D_\mu\xi:=(\partial_\mu+\frac14\omega^{ab}{}_{\mu}\gamma_a\gamma_b)\xi=0$ ✔ |
| (5.6) | 46 | $D_\mu\xi=\frac1d\gamma_\mu\gamma^\nu D_\nu\xi$ ✔ |
| (5.7) | 46 | $D_\mu\xi:=(\partial_\mu+\frac14\omega^{ab}{}_{\mu}\gamma_a\gamma_b+V_\mu)\xi=0$ ✔ |
| (5.8) | 46 | $S^4_b:=\{y_5^2+b^2(y_1^2+y_2^2)+b^{-2}(y_3^2+y_4^2)=r^2\}\subset\R^5$ ✔ |
| (5.9) | 46 | $Q^2=\frac br(M_{12}-\frac12J_3^{\rm R})+\frac1{br}(M_{34}-\frac12J_3^{\rm R})$ ✔ 两项都带 $-\frac12J_3^{\rm R}$（原文如此，批注已说明） |
| (5.10) | 47 | $\langle\mathcal{O}\rangle=\int[\mathrm{D}\phi]e^{-S}\mathcal{O}$ ✔ |
| (5.11) | 48 | $V=\sum_{\text{all spinors }\psi}\psi\overline{Q\psi}\Longrightarrow(QV)_{\rm bosonic}=\sum_\psi|Q\psi|^2$ ✔ |
| (5.12) | 48 | $\langle\mathcal{O}\rangle_t$、$\partial_t\langle\mathcal{O}\rangle_t=-\int e^{-S-tQV}\mathcal{O}QV=-\int Q(e^{-S-tQV}\mathcal{O}V)=0$ ✔（两行 `aligned` 对齐正确） |
| (5.13) | 48 | $\langle\mathcal{O}\rangle=\langle\mathcal{O}\rangle_{t=0}=\lim_{t\to\infty}\langle\mathcal{O}\rangle_t=\int_{QV=0}[\mathrm{D}\phi]e^{-S[\phi]}Z_{\rm one-loop}[\phi]\mathcal{O}[\phi]$ ✔ |
| (5.14) | 49 | $(QV_{\rm hyper})_{\rm bosonic}=|Dq|^2+\|D\tilde q\|^2+\dots+\frac R6|q|^2+\frac R6|\tilde q|^2+|K_q|^2$ ✔ |
| (5.15) | 49 | $q=\tilde q=K_q=0$ ✔ |
| (5.16) | 49 | $\frac{r-x^0}{2r}(F^-_{\mu\nu}+w^-_{\mu\nu}\Re\phi)^2+\frac{r+x^0}{2r}(F^+_{\mu\nu}+w^+_{\mu\nu}\Re\phi)^2+\|D\phi\|^2+[\phi,\phi^\dagger]^2+\|K_{\phi,i}+w_i\Im\phi\|^2$ ✔ 系数 $(r\mp x^0)/2r$、上下标、$\Re/\Im$ 全对 |
| (5.17) | 49 | $0=D^\mu F_{\mu\nu}=D^\mu(-w_{\mu\nu}\Re\phi)=-(\partial^\mu w_{\mu\nu})\Re\phi-w_{\mu\nu}\Re(D^\mu\phi)$ ✔ |
| (5.18) | 49 | $A_\mu=0,\ \phi=a,\ K_{\phi,i}=-w_i a$（极点之外）✔ |
| (5.19) | 50 | 瞬子 ($F^+=0$) 在 $x^0=r$；反瞬子 ($F^-=0$) 在 $x^0=-r$ ✔ |
| (5.20) | 50 | $\mathcal{M}_{\rm inst}=\prod_I(\bigsqcup_{k_I\ge0}\mathcal{M}_{G_I,k_I})$ ✔ `\bigsqcup` |
| (5.21) | 50 | $\langle w,a\rangle\in i\R$，对每个权 $w$ ✔ |
| (5.22) | 50 | $S_{\rm cl}=-\Re(2\pi i\tau)\Tr(ra)^2+2\pi i\tau n-2\pi i\bar\tau\bar n$；$\tau=\frac\theta{2\pi}+\frac{4\pi i}{g^2}$ ✔（批注里关于 $\Tr(ra)^2$ 应读作 $\Tr((ra)^2)$ 的解释**是对的**：$|q|^{r^2|a|^2}=e^{-\Re(2\pi i\tau)r^2|a|^2}$ 自洽） |
| (5.23) | 50 | $Z_{\rm one-loop}=Z^{\rm vector}_{\rm one-loop}Z^{\rm hyper}_{\rm one-loop}$，当 $k=\bar k=0$ ✔ |

> 结论：(1.2)(1.6)/(4.21)(4.22)(4.23)(4.26)(4.28) 这类 **TikZ/图形公式**的编号、节点标签、连线拓扑都与原图一致（只差 O1 的一个 U(1) 方框，属示意细节）。

### 3.3 结构与物件（逐项在位）
- **Part II**：`tr03b.tex:41` `\part{第二篇\quad AGT 对应}`，位置正确（p.43，膜构造两段之后），与 tr-01/tr-05 的 `\part` 写法一致；preamble 已把 `\partname/\thepart` 置空，不会重复出现“第二部分”。
- **§5 标题**：`tr03b.tex:43` `\section{4d 箭图的局域化}`（原文 p.43 "5 Localization for 4d quivers"）✔
- **小节**：4.3 `tr03a.tex:85`、4.4 `tr03a.tex:153`、5.1 `tr03b.tex:72`、5.2 `tr03c.tex:4` ✔（标题译名与原文章节名逐一对应）
- **2 个要点框**：`tr03b.tex:56–66`「局域化与因子化」（原文 p.44 侧栏 "Localization and factorization"，5 个 bullet 全对）；`tr03c.tex:15–22`「超对称局域化的配方」（原文 p.47 "Recipe for supersymmetric localization"，4 个 bullet 全对）✔
- **脚注 35–41（7 条）**：35（p.39 排除病态曲面）、36（p.40 规范单态的困惑）、37（p.41 群整体结构不准确）、38（p.43 忽略 Wick 转动困难）、39（p.44 平直/球面算子对应）、40（p.45 自旋结构）、41（p.45 常旋量的措辞滥用）——逐句与原文一致，挂靠位置也对（`tr03a:87/147/159`、`tr03b:45/74/90/112`）✔
- **习题**：4.8、4.9、4.10（2 小问）、4.11（4 小问）、4.12（3 小问）、4.13（3 小问）、4.14、5.1（2 小问）、5.2、5.3（2 小问）——共 10 个习题环境，内容逐句核对一致 ✔
- **`\para{}` 行内小标题**：tr03a 9 个（耦合常数/S 对偶/五穿刺球面/穿刺球面/穿刺环面/共形 SQCD/自由超多重态/穿刺点/线性箭图规范理论）、tr03b 6 个（膜构造/简单情形：圆球面/共形 Killing 矢量/共形 Killing 旋量/广义 Killing 旋量/压扁球面）、tr03c 5 个（超对称局域化的设置/鞍点计算/椭球上的鞍点/Coulomb 分支参数与质量的实性/圆球面与压扁球面上的结果）——与原文 20 处粗体行内标题**一一对应** ✔
- **每页标注**：p.38–p.50 共 13 个 `% [原文 p.N]` 都在（p.39、p.48 两处偏晚，见 O2）✔

### 3.4 漏译检查
按 `split/p038–p050.txt` 逐段比对：p.38 起（"By tuning more than just u…"）、13 页共约 70 段文字 + 10 个习题 + 7 条脚注，**未发现漏译的整句或整段**；p.43 的 Part II/§5 之间也没有跳段。

### 3.5 术语一致性（抽查，均合 `glossary.tsv`）
压扁球面（squashed sphere）、瞬子/反瞬子、模空间、规范单态、味对称性、双基本表示、双重态超多重态、裤子分解、Killing 矢量/旋量、标架场、自旋联络、Levi–Civita 联络、高斯积分、单圈行列式、鞍点、Berezin 积分、Ricci 标量、辅助场、规范微子、Cartan 子代数、权、Weyl 群、指标定理、zeta 函数正则化、超对称流、能动张量、拓扑扭曲、R 对称性、椭圆函数、Liouville 定理、分支点、覆盖、Bianchi 恒等式、矩阵模型。

### 3.6 LaTeX 机械检查（脚本，只读）
- 花括号平衡、`\begin/\end` 配对、`\left/\right` 配对、`$` 成对：**全部 OK**（三文件均通过）
- 无 BOM、无 CR、无 U+FFFD；无 `\documentclass/\usepackage/\newcommand/\begin{document}`
- TikZ 宽度估算：(4.21) ≈14.4 cm、(4.26) ≈7.4 cm、(4.22)(4.23) 更窄，均在 16 cm 版心内，不会 Overfull

---

## 4. 备注 / 风险提示

1. **边界**：`tr03a.tex` 从 p.38 "只要不只调节 $u$…"（原文 "By tuning more than just u…"）起，符合 Lead 裁决；p.38 顶部那段（"so when the VEV of the vector multiplet φ matches…"）属 tr-02。**但 `tr02c.tex` 目前是 0 字节**（tr-02 尚未交稿），跨块首尾（tr-02 的 (4.18) → tr-03 的 (4.19)）暂时无法从 tr-02 一侧核对；建议合成时再确认一次，尤其是 p.38 那句话不要让两边都写。
2. **块尾**：`tr03c.tex` 止于 (5.23)，未越界写入 p.51 的 (5.24)（归 tr-04）✔。
3. **与 Lead 块的交叉项**：`c01.tex` 的 (1.8) 与本块 (5.1) 是同一记号（$\overline C$ 下标），两处都缺横线；本块改了以后 c01 也应同步（见 M1 的顺带说明）。
4. **(4.21) 的叉口写法**：原文每个味框先经短斜线汇到一点、再由一条水平线连到规范节点（叉形）；TikZ 用两条独立斜线直连节点的 `west/east`。拓扑相同、视觉略不同，属可接受的 TikZ 重画风格，未列为问题。
5. **p.44/p.47 的要点框在原书中是“文字绕排的侧栏”**，译本改为独立 `keybox` 环境（符合 STYLE_GUIDE §2 的做法），文字未增删。

*（本报告只做校对，未改动 tr03a/b/c 任何字节；建议改法均为可直接替换的 LaTeX 文本。）*
