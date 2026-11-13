# ch04c 译校报告（译者：tr04）

## 1. 覆盖范围
- chunk：`ch04c` = PDF p.242–249 = **原书 p.241–248**
- 内容：§4.6 末（推论 4.6.10 的证明续段、定理 4.6.11 托普利茨指标定理）+ §4.7 别列津–托普利茨量子化（§4.7.1 相干态、§4.7.2 托普利茨算子）+ 第 4 章章末回顾
- 文件：`src/chunks/ch04c.tex`（约 27 KB）
- 块界：块首为推论 4.6.10 的证明（原书 p.241 起），该证明在 `ch04b` 末尾未出现，**无重复**；块尾止于原书 p.248 的完整句「……见 §6.1.3。」，`\chapterreview` 收束第 4 章，**第 4 章在本块结束**。

## 2. 陈述环境编号（全部手工照抄原文）
| 编号 | 名称 | 原书位置 |
|---|---|---|
| Theorem 4.6.11 | 托普利茨指标定理（Toeplitz Index Theorem） | p.241 |
| Proposition 4.7.1 | 相干态的超完备族与恒等分解 | p.242 |
| Proposition 4.7.2 | 相干态之间的内积 | p.242 |
| Definition 4.7.3 | 别列津量子化（Berezin quantization） | p.243 |
| Proposition 4.7.4 | $\langle\psi_{\mathbf q,\mathbf p}|a^B|\psi_{\mathbf q,\mathbf p}\rangle=(e^{\frac{\hbar}{2}\Delta}a)(\mathbf q,\mathbf p)$ | p.243 |
| Proposition 4.7.5 | 别列津量子化与外尔量子化的关系 | p.243 |
| Proposition 4.7.6 | Bergman 核 $K(\mathbf z,\mathbf w)=e^{\mathbf z\overline{\mathbf w}/\hbar}$ | p.245 |
| Proposition 4.7.7 | $\{K_{\mathbf w}\}$ 给出恒等分解 | p.245 |
| Proposition 4.7.8 | $\mathcal B(\psi_{\mathbf q,\mathbf p})=e^{-\frac{|w|^2}{2\hbar}}K_{\mathbf w}$ | p.245 |
| Remark 4.7.9 | 两个恒等分解的等同 | p.246 |
| Definition 4.7.10 | 托普利茨算子 $T_f=\Pi\circ M_f\circ\Pi$ | p.246 |
| Theorem 4.7.11 | 别列津量子化 = 托普利茨算子 | p.246 |
| Proposition 4.7.12 | $\hbar\to0$ 时 $\|a^B\|\to\|a\|_\infty$ | p.247 |
| Proposition 4.7.13 | $\hbar\to0$ 时 $\|a^W\|\to\|a\|_\infty$ | p.247 |

共 1 定理（4.6.11）、1 定义（4.7.3、4.7.10 共 2 个）、9 命题、1 注。另有无编号的证明续段（推论 4.6.10 的证明）。

## 3. 公式核对
逐页回页面图像核对（p242–p249 全页 150 dpi；关键式另做 300 dpi 裁图 `work/review/chk_p243_a.png`、`chk_p246_a.png`、`chk_p246_b.png`、`chk_p248_a.png`）：
- 高斯波包与相干态：$\psi_{\mathbf q,\mathbf p}=(T_{\hbar}(\mathbf p,-\mathbf q)\psi_0)$、$\mathbf a\psi_{\mathbf q,\mathbf p}=\frac{\mathbf q+i\mathbf p}{\sqrt{2\hbar}}\psi_{\mathbf q,\mathbf p}$（p.242）
- 恒等分解中的测度 $d\mathbf q\,d\mathbf p/(2\pi\hbar)^n$ 与四步积分链（p.242）
- 内积式指数 $-\frac{1}{4\hbar}[(\mathbf q_1-\mathbf q_2)^2+(\mathbf p_1-\mathbf p_2)^2]$、群律相位 $e^{\frac{i}{2\hbar}(\mathbf q_1\cdot\mathbf p_2-\mathbf p_1\cdot\mathbf q_2)}$（p.242–243）
- 拉普拉斯算子 $\Delta=\sum_i(\frac{\partial}{\partial q^i}\frac{\partial}{\partial q^i}+\frac{\partial}{\partial p^i}\frac{\partial}{\partial p^i})$（原文即重复指标写法，照抄）（p.243）
- 维格纳变换五步推导与 $2^n e^{-\frac{(\mathbf x-\mathbf q)^2}{\hbar}-\frac{(\mathbf p-\boldsymbol\xi)^2}{\hbar}}$（p.244）
- Segal–Bargmann 变换 $(\mathcal B\psi)(\mathbf z)=\frac{1}{(\pi\hbar)^{n/4}}\int d^n\mathbf x\,e^{-\frac{1}{2\hbar}(\mathbf z^2-2\sqrt2\mathbf z\cdot\mathbf x+\mathbf x^2)}\psi(\mathbf x)$ 与两条缠结关系（p.244–245）
- $\mathcal B(\psi_{\mathbf q,\mathbf p})$ 的六步推导（p.246）
- 范数连续性的 $\limsup/\liminf$ 论证与 $O(\hbar)$（p.247）

版式说明：原文向量用粗正体 $\mathbf q,\mathbf p,\mathbf x,\boldsymbol\xi,\mathbf z,\mathbf w$，已用 `\mathbf` 照排；带指标的坐标 $z^i,x^i$ 原文为斜体，照排斜体。原文引用编号（4.6.7、3.2.8、5.3.5、3.2.15 等）照抄，未改。

## 4. 图
`python tools\figtool.py auto 242 249` 返回 0 张候选：本块**没有图**。

## 5. 术语增补（已记 `work/term_requests_ch04c.md`）
| 英文 | 译法 | 页 |
|---|---|---|
| Bergman kernel | 伯格曼核 | 245 |
| heat operator | 热算子 | 243 |
| shift operator | 移位算子 | 241 |
| overcomplete family | 超完备族 | 242 |
| multi-index | 多重指标 | 244 |
| reproducing property | 再生性质 | 245 |
| strict deformation quantization | 严格形变量化 | 248 |

沿用术语表：相干态、湮灭算子、阶梯算子、基态、福克空间、维格纳变换、外尔量子化、别列津、托普利茨、巴格曼、施瓦茨、恒等分解（resolution of the identity）、紧算子、拉普拉斯算子。
`\operatorname{ind}`、`\operatorname{Wig}` 为 preamble 未定义的算子名，按标准 LaTeX 写法使用；`\overset{\mathcal B}{\longleftrightarrow}` 替代 mathtools 的 `\xleftrightarrow`（preamble 未加载 mathtools）。

## 6. Tutor Note
1. 原书 p.246（命题 4.7.8 证明末行）写 $\mathbf w=\frac{\mathbf q-i\mathbf p}{2}$，与命题 4.7.8 中的 $\mathbf w=\frac{\mathbf q-i\mathbf p}{\sqrt2}$ 不一致，疑为笔误；正文照抄原文，已在该行后加 `% [Tutor Note: ...]`。
2. 原书节题作 "Berezin-Toepitz Quantization"（Toeplitz 拼写有误），中文按术语表译为「别列津–托普利茨量子化」，未加批注。

## 7. 存疑
- 原书 p.244 写「$I=\{i_1,\dots,i_n\}$ 是多重指标」，用集合括号表示多重指标，疑为 $(i_1,\dots,i_n)$ 的笔误；因不影响 $|I|,I!,\mathbf z^I$ 的读法，正文照抄，未加批注（若 Lead 认为需要可补一条 Tutor Note）。
- 原书 p.242 "eigenvectors of the annihilation operators $\mathbf a$"（复数 operators 配单个算子），中文按单数「湮灭算子」处理。
- 本块草稿 standalone 编译时 §4.7 显示为 0.1（无 `\chapter`），合书后应为 4.7，属预期。

## 8. 编译自检
```
powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch04c
LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0
DRAFT PDF -> work\tmp_ch04c.pdf   (9 页)
```
首轮出现 `\xleftrightarrow` 未定义（file:line=1），改用 `\overset` 后清零；另修正一处 14.2 pt overfull（定理 4.7.11 证明中的长行拆为两行 `align*`）。已渲染 `work/preview/ch04c_1..9.png` 逐页目检：公式与原书一致、无溢出页边、全角标点正常、`\takeaway` 与 `\chapterreview` 版式正常。

## 9. 状态
**完成并通过自检**（2026-11-07）。下一块：`ch06b`（PDF 314–334，原书 p.313–333）。
