# 第 3 章 译注工作笔记

E. Kowalski, *Classical Automorphic Forms*，《An Introduction to the Langlands Program》（Bernstein–Gelbart 编，Birkhäuser 2004）第 3 章。

## 一、范围与工作文件

- 原文：`work/en/ch03_raw.txt`，页标记 `===== PDF PAGE n (BOOK m) =====`，**book = PDF − 7**，范围 PDF 46–78 = 印刷页 39–71（与任务书一致；STYLE.md 里「原书页 = PDF 页 − 2」是别的卷的偏移，未采用）。
- 页图：`mutool draw -o work/pages/ch03/p%04d.png -r 150 <pdf> 46-78`，实得 p0046.png … p0078.png（按 PDF 页号命名，916×1388，共 33 张）。
- pdftotext 对本书公式完全乱码，故**每个公式都回页图逐符号核对**；小字号与上下标用 PIL 裁剪放大 6–12 倍复核（临时图 `work/tmp_ch03/crop_*.png`：crop_idx2–5 核 Γ₀ 指数公式、crop_union2 核并集下标、crop_lam3 核 λ/s、crop_eps3–4 核 (6.1) 末尾因子）。
- 译法：按书页切片段 `work/tmp_ch03/ch39.tex` … `ch71.tex`（33 个），最后按序 `cat` 成 `src/chapters/ch03.tex`，故行号与书页大致对应。

## 二、通读笔记（原书结构与本译本对应）

| 原书 | 内容 | 译本 |
|---|---|---|
| §1 | 引言：GL(2) 是 GL(1)（Dirichlet 特征）的类比 | `\section{引言}` |
| §2 | 三个动机 | `\section{自守形式的三个动机}` |
| 2.1 | Theta 函数：(2.1) θ(z)，函数方程 θ(−1/z)=(−iz)^{1/2}θ(z)（原书未编号），(2.2) 分式线性作用，(2.3) r₂,r₄,r₆ | `\subsection{Theta 函数}` |
| 2.2 | 行列式方程的解数：矩 I_k(T)、(2.4)、四阶矩、S=Σ(bc/ad)^{it}、按 h=ad−bc 拆分、Kloosterman 和（脚注 1） | `\subsection{行列式方程的解数}` |
| 2.3 | 椭圆曲线的不变量：格、τ′=γ·τ、g(z;γτ)=(cτ+d)^k g(z;τ)、例 2.1（℘ 函数、G_k） | `\subsection{椭圆曲线的不变量}` |
| §3 | 定义与例子：H、Δ、dμ、Γ₀(q)、(3.1)、(3.2)、注 3.1–3.3、例 3.4（Poincaré/Eisenstein 级数 (3.3)）、猜想 3.5、例 3.6（Θ(z;A)）、命题 3.7、例 3.8（Δ） | `\section{定义与例子}` |
| §4 | Fourier 展开与 L 级数：4.1 定义 (4.1)–(4.3)；4.2 例子 (4.4)–(4.8)（例 4.1 Kloosterman、例 4.2 Eisenstein、例 4.3 τ(n)）；4.3 L 级数 (4.11)–(4.14)、命题 4.4 | `\section{Fourier 展开与 L 级数}` |
| §5 | Hecke 算子：(5.1)–(5.4)，引理 5.1、5.2，推论 5.3，引理 5.4，推论 5.5，例 5.6，定理 5.7（Atkin–Lehner），推论 5.8，旧空间/新空间 | `\section{Hecke 算子及其应用}` |
| §6 | 其他「开场白」：6.1 逆定理（定理 6.1、Weil）；6.2 Rankin–Selberg（命题 6.2、推论 6.3、注 6.4、6.5）；6.3 theta 与二次域（命题 6.6） | `\section{其他的“开场白”}` |
| — | 参考文献 32 条 | `\section*{参考文献}` |

全章主线：自守形式既是 theta 型「可算」的对象，又是椭圆曲线模空间上的函数；全纯与 Maass 两类必须合看（谱论、Eisenstein 级数、Rankin–Selberg 积分表示）；Hecke 理论一路走到 Atkin–Lehner 的新形式，再由 Weil 逆定理把「L 函数的函数方程」反过来刻画模形式。

## 三、编号处理（重要决策，需向下游说明）

- 原书条号是**「节 . 节内序号」**：例 2.1、注 3.1、例 3.4、命题 3.7、例 3.8、例 4.1、命题 4.4、引理 5.1 … 推论 5.8、定理 6.1、命题 6.2、注 6.5、命题 6.6。序号按节内递增，不跨节累计。
- `main.tex` 里的 `\ob{编号}{label}` 实现为 `\refstepcounter{oblk}\textbf{\arabic{oblk}.}`，第一个参数**未被使用**，只印全局递增的 1.、2.、3.，无法复现「3.7」「6.4」这类带节号的号码。若照用，会得到与原文不符的编号。
- 故本章**未使用 `\ob`**，改为粗体 run-in：`\par\medskip\noindent\textbf{命题 3.7}\quad …`，逐条照录原书编号（这也符合 STYLE“带编号的条不重编”）。节与小节仍用 `\section`/`\subsection`；`main.tex` 已设 `\thesection=\arabic{section}`，故排版为 1、2、…、6 与 2.1、4.3 等，与原书完全一致。
- 方程照原书编号 (2.1)–(6.1)，用 `\tag{}`，label 取 `c3:eq:n.m`；节 label 取 `c3:sec:N` / `c3:sec:N.M`。原书未编号的公式（θ 的函数方程、Fourier 展开、Bessel 方程等）一律不加号。

## 四、原书笔误清单

已回页图放大核实。「照录」者均在正文对应处加了 `annote`。

| # | 页 | 原书 | 应为 | 处理 |
|---|---|---|---|---|
| 1 | 44 | `[Γ₀(1):Γ₀(q)] = q∏_{p|q}(1+1/q)` | `1+1/p` | 照录 + 注（q=6 时印式给 49/6，非整数） |
| 2 | 45 | `F_Γ = ⋃_{g∈Γ\H} g·F₁` | `g ∈ Γ\SL(2,Z)` 的陪集代表 | 照录 + 注 |
| 3 | 50 | 「λ>0 转化为 λ∈]0,1[（若 λ≤1/4）或 λ=1/2+it」 | 两处 λ 均为 s | 照录 + 注 |
| 4 | 51 | 命题 3.7「Θ(z; a)」 | `Θ(z; A)` | 径改，记此 |
| 5 | 56 | (4.13) 左端 `L(f,s)` | `Λ(f,s)` | 径改 + 注 |
| 6 | 64 | (6.1) 末尾 `τ(ψ)² r^{−1}`，`r` 未定义 | 按 \|τ(ψ)\|²=m 应为 `m^{−1}` | 照录 + 注（存疑） |
| 7 | 66 | 「在 s ↦ (k+ℓ)/2 − s 下不变」 | `s ↦ k+ℓ−s` | 照录 + 注 |
| 8 | 68 | 注 6.5「s = 1 处极点的阶数」 | `s = k` | 照录 + 注 |
| 9 | 46/63 | 「on gets」「transgmogrified」 | one gets / transmogrified | 径改，不影响数学 |
| 10 | 51 | 「推广了公式 (2.5)」 | 本章无 (2.5) | 照录，计入疑点 |
| 11 | 50 | 注 3.3 括号不配对（原文即如此） | — | 照译，未改标点层级 |

另：例 3.6 中 `A[x] = {}^t xAx` 与「`NA^{-1}` 整」的条件，是为保证 Θ(z;A)∈M_{r/2}(2N)（命题 3.7），译文按原文照录，未加解释性脚注（避免注多于原文）。

## 五、未解疑点（2 条）

1. **(2.5) 指什么**（书页 51）：本章带号公式止于 (2.4)，(2.5) 不存在。最可能是 2.1 节中未编号的 theta 变换公式 θ(−1/z)=(−iz)^{1/2}θ(z)，高秩 Θ(z;A) 正是它的推广；也不能排除指第 2 章的某个公式。已在正文出注存疑。
2. **(6.1) 的 `r^{−1}`**（书页 64）：`r` 全章未定义。由函数方程中的 `(qm²)^{k/2−s}` 知 ε 必为模 1 复数，而 |τ(ψ)|²=m，故 `m^{−1}` 才自洽；但原文确印 `r`，无法排除是另一定义被删。照录并出注。
3. （次要，未计）书页 69 及正文的 `[I2, 8]`、`[I1, 5.3]` 等文献页码/节号记法照录，未逐条核对原书页码。

## 六、术语（本章新增/统一）

| 英文 | 中文 | 备注 |
|---|---|---|
| nebentypus | 旁特征（保留原文 nebentypus） | 德文旧称；注 3.1 处出注 |
| moderate growth | 适度增长 | |
| cuspidal / cusp form | 尖点的 / 尖点形式 | |
| cusp | 尖点 | 记 $\mathfrak{a}$ |
| horocycle | 极限圆 | |
| scaling matrix | 伸缩矩阵 | σ_a |
| parabolic | 抛物元 | |
| stabilizer | 稳定化子 | |
| commensurator | 可通约化子 | 附英文，避免与「换位子」混淆 |
| newform / primitive form | 新形式 / 本原形式 | |
| old space / new space | 旧空间 / 新空间 | 记号 S_k(q,χ)^b、S_k(q,χ)^* |
| Hecke form | Hecke 形式 | |
| Petersson inner product | Petersson 内积 | |
| Fricke involution | Fricke 对合 | W |
| converse theorem | 逆定理 | |
| exceptional eigenvalue | 异常特征值 | |
| residual eigenvalue | 剩余特征值 | |
| Weyl law | Weyl 律 | |
| scattering matrix | 散射矩阵 | φ(s) |
| conductor | 导子 | |
| quadratic character | 二次特征 | |
| class group | 类群 | |
| twist（⊗ψ） | 扭 | |
| Rankin–Selberg L-function | Rankin–Selberg L 函数 | |

## 七、译注（12 条，序号按正文出现顺序）

1. p.39 后（§2.3 末）℘ 的 Laurent 展开为何写作 Σ(m+1)z^m G_{m+2}——奇数 m 项因 G_k=0 消失。
2. p.44 后 Γ₀(q) 指数公式分母印作 q。
3. p.46 后 nebentypus 与 χ(−1)=(−1)^k 的来源。
4. p.45 后 F_Γ 并集下标应为陪集代表。
5. p.47 后两种 q（级 vs 局部坐标 e(z)）。
6. p.49 后 Weyl 律中 Vol(X₀(q)) 与 Vol(Γ₀(q)\H) 相等（尖点零测）。
7. p.50 后 λ 与 s 的混淆。
8. p.51 后 (2.5) 悬空引用。
9. p.56 后 (4.13) 的 L 应为 Λ，并说明两种伽马因子。
10. p.64 后 (6.1) 的 r^{−1}。
11. p.66 后 s↦(k+ℓ)/2−s 应为 s↦k+ℓ−s。
12. p.68 后注 6.5 的 s=1 应为 s=k。

来源分级均为 A（原书、Iwaniec、Serre、Lang 等经典教材），「两种 q」一条兼用 I（本库术语）。

## 八、自测记录

- 临时目录 `work/build_ch03/`：由 `src/main.tex` 生成 `main_ch03.tex`（只保留 `\setcounter{chapter}{2}` 与 `\InputIfFileExists{chapters/ch03}`），xelatex 三遍。
- 结果：**0 error、0 undefined、0 overfull、0 missing character**，本章单独成册 27 页（原书 33 页，中文行文较紧）。
- 全量 `main.tex` 目前无法编译，原因是第 8 章 `chapters/ch08.tex` 有未闭合的 `\emph{`（`File ended while scanning use of \emph`），与本章无关；本章内容在单章构建中已全部通过。
- 页眉、节号（1–6、2.1–6.3）、公式号（2.1–6.1）、脚注 1–8（原书编号）均在 PDF 上复核过。
