# trace-kottwitz — §8 逐段译法 / 公式清单 / 核对记录

译手：kottwitz　｜　目标文件：`源码/sections/s10-kottwitz.tex`　｜　底本 p.36–p.42

## 0. 核对方法

1. `PYTHONIOENCODING=utf-8 python 工程文件/tools/render_pages.py 36-42 --dpi 150` → `工程文件/work/pages/pNNN.png`（p036–p042 均在）。
2. 整页通读 150 dpi 图，确定段落、环境、图的**结构**与页界。
3. 公式逐条用 PyMuPDF `get_text("blocks")` 取块 bbox，再 `get_pixmap(dpi=400~900, clip=Rect)` 裁窄条到 `%TEMP%\kot\*.png` 后 `read_image`：裁图绕过 read_image 的 1400 px 降采样，等价 400–900 dpi，可逐符号核对上下标、帽子、箭头方向。
4. `work/src/pNNN.txt`（pdftotext）只用于定位段落，公式一律以图像为准（本节公式密，文本层完全不可用）。

## 1. 页锚（`_check_f.pagemarks` = 36 37 38 39 40 41 42）

| 锚 | 位置 | 依据 |
|---|---|---|
| 36 | `\section` 之后 | p.36 顶格即 §8 标题 |
| 37 | **句中** `\srcpageinl{37}`，插在"开层对应｜的是这样的轨迹"之间 | 原文 p.36 末行 "The open stratum correspond to" / p.37 首行 "the locus where…"，页界确实落在句中 |
| 38 | `\subsection{一般情形}` 之后、"8.2.1" 标题之前 | p.37 末行只有裸标题 "8.2. The general case."，p.38 从 "8.2.1" 起 |
| 39 | 段首 | p.38 末 "…checking compatibility with the preceding descent datum."；p.39 从 "Here is a two step construction…" 起 |
| 40 | 段首 | p.39 末 L-包句结束；p.40 从 "Suppose now moreover that φ is cuspidal…" 起 |
| 41 | 段首（8.2.2 标题前） | p.40 末 Remark 8.3 结束；p.41 从 "8.2.2" 起 |
| 42 | **文件末尾** | p.42 顶部即 "9. The abelian case"，§8 在 p.41 末已结束。任务书要求 7 锚，故保留此锚；已在报告疑点 19 提示 s11 勿重复 |

## 2. 公式清单（逐条已对图核对）

**p.36**
1. `b = ( 0⋯0 π; 1 …0; ⋱ ⋮; 1 0 )^{-1}` —— n×n 示意矩阵，`−1` 在右括号外（400 dpi 裁图确认）。
2. `ℰ_b = O(1/n)`、`J_b(E)=D^×`（同行正文，`\mathscr{E}_b`）。
3. 笛卡尔图（tikz-cd #1）：`[P^{n−1,◊}_E/GL_n(E)] → [Spa(E)/GL_n(E)]`，`i`、`(x_1,id)`，底行 `Hecke^μ --h→--> Bun_G × Spa(E)^◊`。
4. (9) `0 → O^n → ℰ → i_*𝔽 → 0`（`\tag{9}`）。
5. `f : [P^{n−1,◊}_E/GL_n(E)] → Hecke^μ \xrightarrow{h←} Bun_G`。
6. `ℰ ≅ O^i ⊕ O(1/(n−i))`，`i ∈ {0,…,n−1}`（裁图确认指数是 `i` 与分母 `n−i`）。

**p.37**
7. `[Ω^◊/GL_n(E)] ⊂ [P^{n−1,◊}_E/GL_n(E)]`。
8. `f|_{[Ω^◊/GL_n(E)]} : [Ω^◊_Ė/GL_n(E)] → Bun^{ss}_{G,F_q} \xleftarrow[x_b]{\sim} [Spa(\bar F_q)/D^×]` —— 左侧下标 **F_q**（无上划线）、右侧 **\bar F_q**，逐字照排。
9. `φ : W_E → GL_n(\bar Q_ℓ)`（`\overline{\mathbb{Q}}_\ell`，600 dpi 确认）。
10. `x_1^*𝓕_φ = π`、`x_b^*𝓕_φ = ρ`（两行 aligned）。
11. `RΓ_c(P^{n−1}_{C_p}/GL_n(E), i^*h←^*𝓕_φ)((n−1)/2)[n−1] = π⊗φ` —— 上标 `*` 长在箭头上（`\overleftarrow{h}^*`）。
12. `i^*h←^*𝓕_φ = j_! j^* i^* h←^*𝓕_φ`。
13. `j^* i^* h←^*𝓕_φ = M_∞ ×_{D^×} ρ`。
14. `RΓ_c(M_∞⊗C_p, \bar Q_ℓ) ⊗_{D^×} ρ = π⊗φ((1−n)/2)[1−n]`。

**p.38**
15. 五节点图（#2）：Spa(\bar F_p) --x_b--> Bun；Hecke^{≤μ}⊗\bar F_p 出两箭头 `h←`（左下）、`h→`（右下）；Spa(Q̌_p)^◊ --(x_1,id)--> Bun×Spa。
16. Sht 纤维积定义（跨两行，`gather*`）：两个下标行 `x_b, Bun, h←` 与 `h→, Bun×Spa, (x_1,id)`。
17. `Q̌_p^◊ = Q_p^◊ ⊗_{F_p} \bar F_p`。
18. `x_b : Spa(\bar F_p) → [Spa(\bar F_p)/J_b(Q_p)] → Bun`；`x_1 : … /G(Q_p)] …`（此处**无**下划线）。
19. Frobenius 图（#3）：`x_{b^σ}`（上弯）/ `x_b`（下弯）+ `⇓`；正文 `Frob^*x_b = x_{b^σ}`、`b^σ = b^{-1}.b.b^σ`。
20. 两个周期态射（#4）：`Sht → Gr^{≤−μ}⊗_{Q_p^◊} Q̌_p^◊`（π_dR）与 `→ Gr^{≤μ}`（π_HT）。

**p.39**
21. 两步构造方（#5）。
22. `f : Gr^{≤−μ}⊗Q̌^◊ → Hecke^{≤μ}⊗\bar F_p \xrightarrow{h→} Bun×Spa \xrightarrow{\mathrm{proj}} Bun`（proj 正体）。
23. `(Gr^{≤−μ}_{Q̌_p^◊})^{ad} = f^{-1}(Bun^{1,ss}_{G,\bar F_p})`（上标 **1,ss**）。
24. `(Gr^{≤−μ})^{ad} → Bun^{1,ss} = [Spa(\bar F_p)/\ul{G(Q_p)}]`。
25. 两条性质：`π_{dR}` 是 `\ul{G(Q_p)}`-挠子；`π_{HT}` 是 `\widetilde{J}_b`-挠子，位于 `Gr^{≤μ,b} ⊂ Gr^{≤−μ}`（原文如此）。
26. `h→_!(h←^*𝓕_φ ⊗ IC_μ) = 𝓕_φ ⊠ r_μ∘φ`（`⊠` = `\boxtimes`）。
27. 真基变换方（#6）：`[Gr^{≤μ}⊗Q̌^◊/\ul{G(Q_p)}]`、`[Spa(Q̌)^◊/\ul{G(Q_p)}]`（注意左边是 **≤μ**）。
28. `RΓ_c(Gr^{≤−μ}_{C_p^♭}/G(Q_p), (i^*h←^*𝓕_φ)⊗IC_μ) = x_1^*𝓕_φ⊗r_μ∘φ`。
29. `x_1^*𝓕_φ = ⊕_{ρ∈π_0(S_φ)} ρ⊗π_ρ`。

**p.40**
30. 三行四列分解图（#7）。
31. `i^*h←^*𝓕_φ = j_!(Sht(G,b,μ) ×_{J_b(Q_p)} x_b^*𝓕_φ)`。
32. `x_b^*𝓕_φ = ⊕_{ρ∈Ŝ_φ, ρ|_{Z(Ĝ)^Γ}=κ(b)} ρ⊗π_ρ`（两行下标 substack）。
33. `ℋom(ρ, r_μ∘φ) = ⊕_{ρ′∈(S_φ/Z(Ĝ)^Γ)^∧} ρ′⊗σ_{ρ,ρ′,μ,φ}` —— 900 dpi 裁图确认是**上标 `\wedge`**（不是 `\widehat` 宽帽）。
34. `H^•_c(Sht(G,b,μ)_{C_p^♭},IC) ⊗_{J_b(Q_p)} π_ρ ≃ ⊕ … π_{ρ′}⊗σ_{ρ,ρ′,μ,φ}`（`\bullet` 作上标）。
35. `H^i_c(…,\bar Q_ℓ)⊗…π_ρ = {0 (i≠d); ⊕ π_{ρ′}⊗σ(−d/2) (i=d)}`，`d = dim Sht(G,b,μ)`（`\dim\,\Sht` 加细空格，否则印刷成 "dimSht"）。
36. Remark 8.3 的 `κ(b) = \widehat{μ}|_{Z(Ĝ)^Γ}`。

**p.41**
37. `\widehat{\mathcal{M}}`、`(\mathcal{M}_K)_{K⊂\ul{G}(Z_p)}`、`\mathcal{M}_{\ul{G}(Z_p)}=\widehat{\mathcal{M}}_η` —— 原文把前两个各自单独排成一行展示，译文照办。
38. `ρ : \mathbb{H}⊗_{\bar F_q} R^+/ϖ_R → H⊗_{R^+} R^+/ϖ_R` —— 左侧 **黑体 ℍ**（被形变的固定 p-可除群），右侧斜体 `H`（形变对象），600 dpi 确认。
39. `g : M_∞ → 𝓑𝓣 \xrightarrow{u} Hecke^μ`。
40. 两条 bullet 的 `h←∘g`、`h→∘g` 分解（`\mathscr{E}_b` 显式出现）。

## 3. 版式决定

- **Hecke 的正斜体**：原文图内用正体 `\mathrm{Hecke}`，行内/展示式用斜体（PDF 里 `H` 的斜体悬挑造成 "H ecke" 视觉空隙）。译文照此区分：`tikzcd` 内 `\mathrm{Hecke}`，正文展示式 `\mathit{Hecke}`。
- **下划线**：原文在 p.39–p.40 若干处给 `G(Q_p)`、`J_b(Q_p)` 整串加下划线（规则落在括号内、基线之下，非箭头杆）。用 preamble 的 `\ul{}` 照排：`\ul{G(\QQ_p)}` 6 处、`\ul{J_b(\QQ_p)}` 2 处，并在首次出现处加 `\yizhuw` 说明。（另有 10 处 `\ul{G}` 是原文的**整模型**记号，与这一排版现象无关。）
- **Sht 定义**：先试 `multline*`（第二行 flush right，难看），改 `gather*` 两行居中。
- **`\tag{9}`**：原文公式号必须硬保，避免与其他块公式号冲突。
- **`\mathcal{BT}`**：原文花体，与 preamble 的 `\BT`（正体）不同，按原文取 `\mathcal{BT}`（报告疑点 17 请 Lead 裁决）。
- **Frobenius 2-胞腔**：tikz-cd 无原生 2-胞腔，用中间格 `{\Downarrow}` + 两条 `bend left/right` 箭头近似，视觉与原图一致。
- **p.40 分解图**：原图 3 行 4 列，含 4 个 hook 箭头（`\arrow[hook]`）与 2 条长对角线；用空单元 `{}` 占位以满足 tikz-cd 的节点要求（否则报 "No shape named tikz@f@…"）。

## 4. 逐段译法要点

- 8.1 首段把 "Consider G=GL_n over the p-adic field E. And set μ(z)=…" 合译为一句"设 G=GL_n 定义在 p-进域 E 上。并令 μ(z)=…"，保留原文的 And 起句口吻。
- p.36→p.37 是**同一段**被页界切断（"…correspond to ｜ the locus where…"），译文不作分段，页锚用 `\srcpageinl`。
- p.37 "This is the pullback via f of the semi-stable locus and coincides with Drinfeld's space Ω" —— "This" 指上一句的 locus，中文用"它"承接，不加"这个开层"以免过度解释。
- p.38 "We note Q̌_p for L when this is the base field" —— note 是 denote 的动词用法，译"记 L=Q̌_p"。
- p.39 "the so called admissible locus" 原文即带 so called，译"所谓的"。
- p.40 "this is left to the courageous reader…" 保留作者口吻："这留给勇敢的读者……"。
- p.41 "as in the preceding section we take its Galois orbit" —— 译"与上一小节一样"，与 SPEC 的 subsection 层级一致。
- p.41 "because of the 'sheaf associated to the presheaf'" 引号照排为中文引号。
- 术语一律按 glossary：基本 Rapoport–Zink 空间、局部 shtuka、Kottwitz 集、σ-中心化子、L-包、紧支上同调、修正、菱形、完满、p-可除群、F-等晶体、pro-étale（不译）、shtuka（不译）。

## 5. 编译与自检记录

```
cd 源码 && build.bat check sections/s10-kottwitz.tex f
第 1 次：Undefined control sequence \Id      → 改用 preamble 的 \id
第 2 次：pgf Error: No shape named `tikz@f@7-2-2'（tikzcd 空单元被当箭头目标）→ 补 {} 占位
第 3 次：[OK] _check_f.pdf（6 页）
补译注后：      [OK] _check_f.pdf（7 页，0 error，0 overfull）
```
- `grep Overfull _check_f.log` → 0。
- `cat _check_f.pagemarks` → 36 37 38 39 40 41 42。
- 7 页逐页 `read_image` 目检：矩阵、7 张 tikz-cd、10 条脚注、cases 分段函数、`\ul{}` 下划线均正常；`dim Sht` 已加 `\,` 避免连排。

## 6. 留给 Lead 的三件事

1. `\srcpage{42}` 在文件末尾 —— s11 不要再写 42。
2. 导引自述句（"study of this key case is the main ingredient…"，p.3）属于 s01，本块无法承载。
3. `[22]/[23]/[30]` 以方括号数字排版；若全书统一 `\cite`，需同步替换这 3 处。
