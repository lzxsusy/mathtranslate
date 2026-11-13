# ch04b 译校报告（译者：tr06）

## 1. 覆盖范围
- chunk：`ch04b` = PDF p.223–241 = **原书 p.222–240**
- 内容：§4.3 斯通定理（4.3.1 单参数酉群、4.3.2 斯通定理）+ §4.4 斯通–冯·诺依曼定理（4.4.1 外尔关系、4.4.2 斯通–冯·诺依曼定理）+ §4.5 薛定谔算子（自由粒子、谐振子、半有界势、加藤–雷利希定理、特罗特乘积公式与费曼积分）+ §4.6 弗雷德霍姆算子与指标（4.6.1 弗雷德霍姆算子、4.6.2 指标的同伦不变性、4.6.3 托普利茨指标定理起头）
- 文件：`src/chunks/ch04b.tex`（约 47 KB，1180 行；汉字 31567）
- 块界：块首正好是原书 p.222 的 `\section{斯通定理}`，整句起头，**无补句**；块尾止于原书 p.240 的「推论 4.6.10」陈述完（该推论的证明从原书 p.241 起，在 `ch04c` 开头，**无重复、无缺失**）。

## 2. 节清单
| 节 | 小节 | 原书页 |
|---|---|---|
| §4.3 斯通定理 | 4.3.1 单参数酉群；4.3.2 斯通定理 | p.222–225 |
| §4.4 斯通–冯·诺依曼定理 | 4.4.1 外尔关系；4.4.2 斯通–冯·诺依曼定理 | p.225–228 |
| §4.5 薛定谔算子 | 4.5.1 自由粒子；4.5.2 谐振子；4.5.3 半有界势；4.5.4 加藤–雷利希定理；4.5.5 特罗特乘积公式与费曼积分 | p.228–237 |
| §4.6 弗雷德霍姆算子与指标 | 4.6.1 弗雷德霍姆算子；4.6.2 指标的同伦不变性；4.6.3 托普利茨指标定理（起头） | p.237–240 |

## 3. 陈述环境编号（全部手工照抄原文，共 28 条）
| 编号 | 名称 | 原书位置 |
|---|---|---|
| Definition 4.3.1 | 单参数酉群与强连续 | p.222 |
| Definition 4.3.2 | 无穷小生成元 | p.222 |
| Definition 4.3.3 | 用博雷尔函数演算定义 $e^{itA}$ | p.222 |
| Theorem 4.3.4 | 斯通定理 | p.223 |
| Theorem 4.4.1 | 斯通–冯·诺依曼定理 | p.225 |
| Example 4.4.2 | $P_\Phi$ 是谐振子基态投影 | p.228 |
| Definition 4.5.1 | 正分布 | p.230 |
| Example 4.5.2 | 连续函数给出的正分布 | p.230 |
| Lemma 4.5.3 | $L^1$ 收敛的子列几乎处处收敛 | p.230 |
| Definition 4.5.4 | 局部 $L^p$ 空间 | p.231 |
| Theorem 4.5.5 | 加藤不等式 | p.231 |
| Theorem 4.5.6 | $V\in L^2_{\mathrm{loc}}$、$V\ge0$ 时本质自伴 | p.232 |
| Example 4.5.7 | $-\Delta+\|\mathbf{x}\|^2$ 等本质自伴 | p.233 |
| Definition 4.5.8 | 相对有界与 $A$-界 | p.233 |
| Theorem 4.5.9 | 加藤–雷利希定理 | p.233 |
| Proposition 4.5.10 | $V_1\in L^2$、$V_2\in L^\infty$ 时自伴 | p.234 |
| Example 4.5.11 | 库仑势 | p.235 |
| Proposition 4.5.12 | 特罗特乘积公式 | p.235 |
| Definition 4.6.1 | 弗雷德霍姆算子与指标 | p.237 |
| Example 4.6.2 | 移位算子 | p.237 |
| Proposition 4.6.3 | $\operatorname{ind}(AB)=\operatorname{ind}A+\operatorname{ind}B$ | p.237 |
| Proposition 4.6.4 | $\operatorname{ind}(A^*)=-\operatorname{ind}A$ | p.237 |
| Theorem 4.6.5 | 阿特金森定理 | p.238 |
| Proposition 4.6.6 | $A+K$ 弗雷德霍姆 | p.238 |
| Proposition 4.6.7 | 指标局部常值 | p.239 |
| Corollary 4.6.8 | $\operatorname{ind}(A+K)=\operatorname{ind}A$ | p.239 |
| Lemma 4.6.9 | 托普利茨算子的紧交换子 | p.240 |
| Corollary 4.6.10 | $f$ 处处非零时 $T_f$ 弗雷德霍姆 | p.240 |

共 4 定义、4 定理、6 命题、2 推论、2 引理、4 例。

## 4. 公式核对
逐页看全页 150 dpi 图（`work/pages/p223.png`–`p241.png`），关键式另做 300 dpi 裁图（`work/review/`）：`chk_p227_thm.png`（定理 4.4.1 中心作用 $e^K=e^{i/\hbar}$）、`chk_p228_dag.png`（$(\dagger)$ 式系数 $+\frac{i\hbar}{2}ab$）、`chk_p229_ex.png`（例 4.4.2 四行）、`chk_p229_spec.png`（谱测度首行 $\overline{\widehat{\varphi}(\boldsymbol{\xi})}$ 的上划线）、`chk_p230_dphi.png`（$d\varphi_{-\Delta,\varphi}$ 系数）、`chk_p226_q.png`（$\delta^k_j$ 上下标）、`chk_p232_x.png`（$(\sgn u)(\mathbf{x})$ 分段）、`chk_p235_line.png`（加藤–雷利希 ① 末项）、`chk_p236_ineq.png`（命题 4.5.10 证明首式）。
排版照原文：位置变量粗正体 $\mathbf{x},\mathbf{y}$，频率粗体 $\boldsymbol{\xi}$；一维谐振子用斜体 $x$；Hilbert 空间 $\mathcal{H}$；$\mathbf{F}(\mathcal{H}),\mathbf{B}(\mathcal{H}),\mathbf{K}(\mathcal{H})$ 用粗体；谱测度算子原文为黑板体 $\mathbb{P}_A$，用 `\mathbb{P}` 照排。

## 5. 图
- 唯一一张：原书 p.237 命题 4.6.3 证明中的**行正合交换图**（$0\to\mathcal{H}\to\mathcal{H}\oplus\mathcal{H}\to\mathcal{H}\to0$ 两行、三条竖直箭头，标注 $I\oplus B$、$(B,-I)$、$A\oplus I$、$(I,-A)$、$B$、$AB\oplus I$、$A$）。
- 处理方式：**TikZ 按原图重绘**（图内只有数学符号，无英文词标签）。图后注释：`% [图：原书 p.237 的交换图，本图按原文重绘；图内只有数学符号，原图无题注]`。
- `python tools\figtool.py auto 223 241` 只识别出 p.228 的框式公式（数学装饰，未嵌）与交换图（数学图，用 TikZ 重绘）。本块**无裁切 PNG 图**。

## 6. 术语与宏
- 术语增补已记 `work/term_requests_ch04b.md`（17 条）。
- `\ind`、`\Coker` 在 preamble 中未定义：按标准 LaTeX 用 `\operatorname{ind}`、`\operatorname{Coker}`，未改 preamble。
- 原文的圈号 ①②（Enclosed Alphanumerics U+2460/2461）在当前 CJK 字体配置下会落到拉丁字体、报 missing character；改用标准 LaTeX 的 `\textcircled{1}`、`\textcircled{2}` 排版。

## 7. Tutor Note（3 条）
- 定理 4.4.1 后：说明 $e^K$ 中 $K$ 是海森堡群中心元（易错点，非笔误）。
- 定理 4.5.5 证明末：原文写 $\Delta\varphi$，由 $\varphi_\epsilon\to|u|$ 推疑应为 $\Delta|u|$，正文保留原文。
- 定理 4.5.9 证明 ①：不等式右端为 $(a+\frac b\lambda)\|\varphi\|$ 而左端是 $\psi$，疑为 $\|\psi\|$ 之笔误，正文保留原文。

## 8. 存疑（请 Lead 裁夺）
1. **§4.6 缺 `\takeaway`**：§4.6 跨块（托普利茨指标定理的证明与 §4.6 结尾在原书 p.241，属 `ch04c`），本块不能把 takeaway 放在节中间；`ch04c.tex` 现有 `\takeaway` 只对应 §4.7，也没有补 §4.6 的。建议由 ch04c 所有者（tr04）在 `\section{别列津–托普利茨量子化}` 之前补一句 `\takeaway{...}`，或由 Lead 合书时统一补。lint 对本块的提示项正是「4 个 `\section` 对 3 个 `\takeaway`」。
2. 本块草稿 standalone 编译时 §4.3 显示为 0.1（无 `\chapter` 前缀），合书后应为 4.3，属预期。
3. 例 4.5.7 与定理 4.5.9 证明内的 ①② 用 `\textcircled` 近似，观感与原书圈号略有差异（详见 §6）。

## 9. 编译自检
```
powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch04b
LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0
DRAFT PDF -> work\tmp_ch04b.pdf   (22 页)
```
`python tools\lint.py ch04b` → `合计：问题 0 条`（1 条提示，见 §8.1）。
首轮曾出现 missingchar=12（①②）、overfull=4（$\Phi\#(\delta\#\Phi)$ 长式 50.3 pt、两处内积式、TikZ 图 20 pt），已分别用 `\textcircled`、把长式拆行、`aligned` 拆行、图整体 `scale=0.86` 修正，复检归零。已渲染 `work/preview/ch04b_1,4,7,8,18,19,20,22.png` 目检：公式与原书一致、无溢出页边、交换图版式正确、全角标点正常、`\takeaway` 版式正常。

## 10. 状态
**完成并通过自检**（2026-11-07）。下一块：`ch05a`（PDF 251–272 = 原书 p.250–271，第 5 章章首 + §5.1 相空间的辛几何 + §5.2 几何半经典量子化）。
