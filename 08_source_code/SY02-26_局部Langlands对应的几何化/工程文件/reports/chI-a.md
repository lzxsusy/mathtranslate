# Chapter I · 块 A（p.7–p.22）

## 1. 完成范围

| 原文节 | 原文标题 | 原文页 | 译文小节 | 段落/环境 |
| --- | --- | --- | --- | --- |
| §I.1 | The local Langlands correspondence | p.7 | `\section{局部 Langlands 对应}` | 4 个散文段 + (1)(2) 两个独立行 + 2 处行间式 |
| §I.2 | The big picture | p.8–17 | `\section{总体图景}` | 15 个编号对象 + 若干注记段 + (i)–(ix) 齐头条目（(viii)(ix) 在 p.18） |
| §I.3 | The Fargues–Fontaine curve | p.18–20 | `\section{Fargues–Fontaine 曲线}` | 5 个编号对象 + 4 个正文段 |
| §I.4 | The geometry of Bun_G | p.20–22 | `\section{$\Bun_G$ 的几何}` | 1 个编号对象（七条 (i)–(vii)）+ 8 个正文段 |

- 页锚点共 16 个：`\srcpage`（页边注）7 个 = p.8, 11, 13, 15, 19, 21, 22；`\srcpageinl`（上标〔p.N〕）9 个 = p.7, 9, 10, 12, 14, 16, 17, 18, 20（其中 p.7/10/16/18 原为段首边注但排不出版，见 §7）。
- 编译：`build.bat check sections/s01-chI-1.tex a` → `Output written on _check_a.pdf (16 pages).` + `[OK] _check_a.pdf`；0 error、0 missing character、0 overfull/underfull、0 undefined。
- 页锚点检查：`check_pagemarks.py _check_a --start 7 --end 22 --pdf` → `[ok] 16 个锚点全部在 PDF 中可见`、`[ok] p.7–p.22 锚点齐全`。

## 2. 编号对象对齐

| 原文 | 译文 label | 一致 | 备注 |
| --- | --- | --- | --- |
| Theorem I.2.1 | `thm:I.2.1` | 是 | 自动编号 1.2.1 |
| Definition I.2.2 | `def:I.2.2` | 是 | 定义体跨 p.12–13，`\end{definition}` 置于 p.13 首行斜体句之后 |
| Proposition I.2.3 | `prop:I.2.3` | 是 | |
| Definition I.2.4 | `def:I.2.4` | 是 | |
| Remark I.2.5 | `rem:I.2.5` | 是 | |
| Theorem I.2.6 | `thm:I.2.6` | 是 | 两段（第二段以 Under this bijection 起） |
| Theorem I.2.7 | `thm:I.2.7` | 是 | 两段 |
| Remark I.2.8 | `rem:I.2.8` | 是 | |
| Remark I.2.9 | `rem:I.2.9` | 是 | |
| Remark I.2.10 | `rem:I.2.10` | 是 | |
| Theorem I.2.11 | `thm:I.2.11` | 是 | 单段 + 行间式 |
| Theorem I.2.12 | `thm:I.2.12` | 是 | |
| Remark I.2.13 | `rem:I.2.13` | 是 | 段落跨 p.16–17 |
| Remark I.2.14 | `rem:I.2.14` | 是 | |
| Remark I.2.15 | `rem:I.2.15` | 是 | |
| Theorem I.3.1 | `thm:I.3.1` | 是 | |
| Theorem I.3.2 | `thm:I.3.2` | 是 | |
| Theorem I.3.3 | `thm:I.3.3` | 是 | 两段（第二段 If S=Spa C …） |
| Theorem I.3.4 | `thm:I.3.4` | 是 | 两段 |
| Definition I.3.5 | `def:I.3.5` | 是 | 定义体内含两处行间式 |
| Theorem I.4.1 | `thm:I.4.1` | 是 | 引句 + (i)–(vii)，跨 p.20–21 |

共 21 个编号对象，20 个为「章.节.序」自动编号且与原号逐个吻合；本节所在的 4 个 `\section` 恰好对应原文 I.1–I.4，故自动编号与原文编号一致（唯一需要人工保证的是对象在同一节内的出现次序，已逐页核对）。

作者原脚注 4 个，均以 `\footnote{}` 按原顺序保留：

| 原文脚注 | 位置 | 译文中序号 |
| --- | --- | --- |
| 1（叙述与思想史无关） | p.8 | 4 |
| 2（Bernstein 也强调换记号） | p.8 | 5 |
| 3（层/分层的出处） | p.11 | 10 |
| 4（BC(O(−1)[1]) 不可表示仅 p-进确知） | p.20 | 19 |

序号后移是因为译注同样排成脚注（见 §7）。

## 3. 公式核对

逐页把原 PDF 以 `dpi=150` 渲染为 PNG 后对照录入，个别记号再以 `dpi=400` 局部裁切放大确认；共核对 p.7–p.22 十六页。发现并修正 OCR/转录错误 6 处：

1. **p.9 友矩阵**：OCR 只剩一串 0/1，无法判断位置。放大后确认上对角线为 1、左下角为 π^s（即 `σ(e_i)=e_{i+1}`、`σ(e_r)=π^s e_1` 的友矩阵），据此录入 `pmatrix`。
2. **p.12 `Ė`**：OCR 作 `E`，实为 `\breve{E}`（短音符）；同页 `maps \ol{\FF}_q((t))=\breve E\to R` 的 `\ol{\FF}_q` 上划线 OCR 亦丢失，据图补回。
3. **p.8 `\breve E=\ol{\FF}_q((t))`**：同上，OCR 丢掉 `\FF_q` 上划线。
4. **p.20 `\pi_1(G_{\ol E})_\Gamma`**：低分辨率下上划线看似在 G 上；400dpi 放大确认在 E 上，故录 `G_{\ol E}`（不是 `\ol G_E`）。
5. **p.22 `\mathrm{Spd}\,\ol{\FF}_q[[t^{1/p^\infty}]]`**：OCR 作 `F_q`，图上为 `\ol{\FF}_q`。
6. **p.10 `\widetilde R`、p.19 `\mathbb A^1_{C^\sharp}`、p.21 `\ul E^\times`**：`R̃` 的波浪线、`A^1` 的上标 1、下划线 `E` 均据图确认（OCR 全丢）。

另核对过的排版细节：`\dot\times`（p.12/13/17）、`\mathbb{D}^*` 与 `\mathbb{D}`（p.12/13/20）、`\varprojlim_{x\mapsto x^p}`（p.13）、`\begin{pmatrix}` 上三角（p.21）、`[\ast/G]` 的 `\ast`（全篇）、花体 `G\text{-}\mathcal{I}\mathrm{soc}` 与正体 `G\text{-}\Isoc` 的分工（p.9 正体 groupoid；p.10–p.11 花体 prestack；p.15 正体；p.16 Rem I.2.10 又花体）。

## 4. 译注

共 15 条：术语首现 10、跳步/歧义 4、疑似笔误 1。

**术语（10）**
1. p.7 朗兰兹对偶群（Langlands dual group）：统一译名，别名「Langlands 对偶群」。
2. p.7 $L$-包（$L$-packet）：同一 $L$-参数之下的不可约表示纤维。
3. p.8 纯内形式（pure inner form）：由 $G$-主丛 $\mathcal{E}$ 给出的内形式。
4. p.9 等晶体（isocrystal）：$\breve E$ 上带 $\varphi$-线性自同构的空间。
5. p.11 Hecke 算子：由沿曲线作修正给出，使 $W_E$ 与 $\widehat G$ 同时出现。
6. p.12 完满空间（perfectoid space）：取「完满」而非「完美」，与 perfect 区分。
7. p.13 经典点（classical point）：局部对应环的极大理想的点，须逐点定义。
8. p.14 菱形（diamond）：完满空间按 pro-étale 等价关系取的商。
9. p.15 unipotent group diamond（幂幺群菱形）：Chapter I 只作描述性使用，定义见 §III.2。
10. p.16 几何 Satake 等价：把 $\Rep\widehat G$ 与 Hecke 叠上反常层的卷积幺半范畴等同。

**跳步/歧义（4）**

11. p.7 「本质上是双射」：须与上句合看——$\mathrm{GL}_n$ 的 $L$-包单点，而参数侧只计半单 $L$-参数（原文 p.36）。
12. p.9 单射 $H^1_{\text{ét}}(\Spec E,G)\hookrightarrow B(E,G)$：单射性来自 $E$-向量空间范畴到 $\Isoc_E$ 的全忠实嵌入。
13. p.10 完满化不改变 étale 层：$X_{\mathrm{perf}}\to X$ 是万有同胚，故两者 étale 站点给相同层范畴。
14. p.20 $\kappa$ 经 z-扩张间接定义，与 $\pi_1$ 的完整对应（含基本集上为双射）正式见 §III.2。

**疑似笔误（1）**

15. p.22 「Part (iv) is a also consequence」：多出一个冠词 a，按「(iv) 也是定理 I.3.4 的推论」译。

## 5. 术语新增（待 Lead 并入）

英文<TAB>建议中文<TAB>依据

- prestack<TAB>保留英文<TAB>glossary 未收；与「叠」对举时译「预叠」易与 pro- 混淆，故保留。
- groupoid<TAB>保留英文<TAB>glossary 未收；`G-Isoc` 是 groupoid 而 `G-𝓘soc` 是 prestack，译文靠正体/花体区分，不译可保留这一区别。
- classifying space<TAB>分类空间<TAB>与「分类叠」（classifying stack）对举。
- semi-orthogonal decomposition<TAB>半正交分解<TAB>原文 p.11/p.15；范畴论语境。
- globally generated<TAB>由整体截面生成<TAB>原文 p.19 Thm I.3.3。
- locally ringed space<TAB>局部环化空间<TAB>原文 p.19。
- graded ring<TAB>分次环<TAB>原文 p.19。
- universal cover<TAB>万有覆盖<TAB>原文 p.19（Lubin–Tate 形式群律的万有覆盖）。
- numerator<TAB>分子<TAB>原文 p.19（维数由 λ 的分子给出）。
- exotic<TAB>保留英文<TAB>原文 p.10/p.15/p.19，作「更 exotic 的对象」，不译以免坐实技术含义。
- profinite<TAB>保留英文（profiniteness）<TAB>原文 p.10/p.11/p.15；glossary 只收 locally profinite 的用法。
- resp.<TAB>resp.<TAB>原文惯例，保留以免与「分别」混淆。
- Schur-irreducible<TAB>Schur 不可约<TAB>原文 p.17。

## 6. 疑点（未解）

1. p.7「essentially a bijection」的准确含义已在译注中按原文 p.36 处理，但「参数侧只取半单 $L$-参数」在 §I.1 未定义，若需严格应回引 §I.9。
2. p.15「unipotent group diamond」在 Chapter I 只有描述，完整定义在 §III.2；译文按描述性措辞处理，未加形式定义。
3. p.21 (iv)/(v) 与 p.87 Thm III.0.2 的 (iv)/(v) 编号互换（§III.2 把 (iv)/(v) 对调）。本块严格按 p.20–p.21 原文编号译，未加译注；若全书以 III.0.2 为准，需回改并加对照说明——留待 Lead 裁定。
4. p.22 末句「For …」在 p.23 继续；本块依页界止于「对于」，接续由后续块负责。

## 7. 遗留问题

1. **4 个段首锚点未印**：p.7、p.10、p.16、p.18 的 `\srcpage` 即使放在段首、并加 `\leavevmode\mbox{}` 前置，`\marginnote` 仍不落版（其余 9 个正常）。已改用 `\srcpageinl`，排成上标〔p.N〕，`check_pagemarks` 两项均 `[ok]`。版式上与页边注不完全统一，若 Lead 有统一方案可回改。
2. **脚注序号**：译注与作者脚注共用 `\footnote`，故原文脚注 1–4 现编号为 4/5/10/19；顺序未变。
3. **hyperref 书签警告**：`\section{$\Bun_G$ 的几何}` 的数学触发 `Token not allowed in a PDF string`（不影响编译，也不是 error）；如需消除可加 `\texorpdfstring`，但那要改 section 行，未擅动。
4. **p.23 接续**：本文件末段停在「对于」，与原文页界一致，不计为缺陷。
