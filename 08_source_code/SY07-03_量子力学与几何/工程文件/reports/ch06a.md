# ch06a 译校报告（译者：tr07）

## 1. 覆盖范围

- chunk：`ch06a` = PDF p.298–313 = **原书 p.297–312**
- 内容：**第 6 章章首** `\chapter{形变量子化}`＋章引言；§6.1 形变量子化（6.1.1 形式形变、6.1.2 泊松代数作为经典极限、6.1.3 严格形变量子化）；§6.2 辛流形上的几何进路（6.2.1 外尔丛、6.2.2 辛联络、6.2.3 费多谢夫的阿贝尔联络、6.2.4 象征映射、6.2.5 整体化）
- 文件：`src/chunks/ch06a.tex`（927 行、130 个行间公式；lint 统计汉字 22961）
- 块界：本块是章首块，起于原书 p.297 的章标题；止于原书 p.312 页末「象征映射把两个结合代数等同起来」的式 (Γ_D^flat,∗) ≅ (C^∞(M)[[λ]],∗_D)。文件末注释已写明 **ch06b 从原书 p.313 起**，与 ch06b 无重复、无缺页。

## 2. 陈述环境编号（全部手工照抄原文）

| 编号 | 名称 | 原书页 |
|---|---|---|
| Definition 6.1.1 | 形式幂级数环 𝕍[[λ]] 与形式洛朗级数 𝕍((λ)) | p.297 |
| Definition 6.1.2 | 形式形变（λ 双线性＋展开式） | p.297–298 |
| Example 6.1.3 | Moyal 乘积（λ=iℏ） | p.298 |
| Example 6.1.4 | ℝ[[xⁱ,pᵢ]] 上的 Moyal 乘积 | p.298 |
| Definition 6.1.5 | 泊松代数 | p.299 |
| Example 6.1.6 | (C^∞(M),{−,−}) | p.299 |
| Proposition 6.1.7 | (A,·,{−,−}) 是泊松代数 | p.299 |
| Definition 6.1.8 | （形式）形变量子化 | p.300 |
| Example 6.1.9 | 一族星积 ∗_α | p.300–301 |
| Definition 6.1.10 | 严格形变量子化（四条） | p.301 |
| Example 6.1.11 | ℝ²ⁿ 的外尔量子化给出严格形变量子化 | p.301 |
| Example 6.1.12 | 非交换环面／量子环面 | p.301 |
| Definition 6.2.1 | 形式外尔代数 𝒲(V) | p.302 |
| Definition 6.2.2 | 外尔丛 𝒲(M) | p.303 |
| Definition 6.2.3 | 辛联络 | p.304 |
| Theorem 6.2.4 | 辛联络存在且构成仿射空间 | p.305 |
| Definition 6.2.5 | 辛曲率 R^∇_ω | p.306 |
| Lemma 6.2.6 | (Ω^•(M,𝒲),δ) 的上同调 | p.309 |
| Theorem 6.2.7 | 费多谢夫的阿贝尔联络存在性（Fedosov） | p.309 |
| Proposition 6.2.8 | H_D^•(M,𝒲) 的计算 | p.311 |
| Definition 6.2.9 | 象征映射 | p.312 |

共 21 个带编号陈述（3 定义前段＋…；计：定义 9、例 4、命题 2、定理 3、引理 1＝21）。编号全部照抄原文，同节共用一个计数器，未用自动编号。

## 3. 公式核对

逐页读 `work\pages\p298.png`–`p313.png`（150 dpi）核对；关键式另做 300 dpi 裁图（如 p.309 的 γ₀ 曲率式、p.301 的双向箭头图）。核对要点：

- p.297–298：𝕍[[λ]]／𝕍((λ)) 的集合式与指标范围；R[[λ]] 的乘法公式 (Σaᵢλⁱ)(Σbⱼλʲ)=Σ_k(Σ_{i+j=k}aᵢbⱼ)λᵏ；Moyal 乘积左右导数箭头与 μ_k=1/k!(1/2)ᵏ f[Σ…]ᵏg。
- p.298：结合性一阶展开四行（在两处断行避免 overfull，数学内容未变）、μ₁ 的上闭链方程。
- p.299–301：{−,−}=lim_{λ→0}(1/λ)(a∗b−b∗a)；Def 6.1.8；∗_α 的显式式与 α=0,1 的特例（x∗₁p=xp、p∗₁x=xp−λ）。
- p.301：严格形变量子化四条，第 3 条狄拉克条件 ‖(i/ℏ)[Q_ℏ(f),Q_ℏ(g)]−Q_ℏ({f,g})‖→0。
- p.302：ω_{ij}、{f,g}=Σω^{ij}∂_{yⁱ}f∂_{yʲ}g、𝒲(V)=(Ô(V)[[λ]],∗) 与 ∗ 的指数式。
- p.303：𝒲(M)=∏Sym^k(T*M)[[λ]]、纤维 𝒲(M)|_p=𝒲(T_pM)、截面的多重指标展开、逐纤维 Moyal 乘积。
- p.304–305：辛联络两条；∇=∇^g+α 的构造、ξ 的定义、α 的解 ω(α(X,Y),Z)=⅓ξ(X,Y,Z)+⅓ξ(Y,X,Z)、四行验算；定理 6.2.4 的仿射空间结论 β∈Γ(M,Sym³(T*M))。
- p.306–307：R^∇ 与 R^∇_ω 的五步反对称链；第一比安基恒等式；ω_{ij}、R^∇_ω=¼ΣR_{ijkl}dxⁱ∧dxʲ⊗yᵏyˡ；∇²y^m 的推导与 ∇²s=[−λ⁻¹R^∇_ω,s]_∗。
- p.308：D 的相容性三行、D² 的三行（含 ½[γ,γ]_∗=γ∗γ）、阿贝尔联络条件、δ、γ₀、∇γ₀+½λ⁻¹[γ₀,γ₀]_∗=−ω。
- p.309–310：霍奇型关系 δδ*+δ*δ=p+q；权的赋值 wt(yⁱ)=1、wt(λ)=2；定理 6.2.7 的方程与逐权求解（δγ₃⁺−R^∇_ω−λω₁=0 起，O_{m−1} 的归纳）。
- p.311–312：滤链 F_mΩ^p、Gr^F_m、谱序列退化；象征映射 σ:s(x,y,λ)↦s(x,0,λ)；f∗_Dg:=σ(σ⁻¹f∗σ⁻¹g)。

版式说明：环面统一 `\mathbb{T}^n`（preamble 无 \T）；形式幂级数环用 `\widehat{\mathcal{O}}(V)`；权用 `\mathrm{wt}`；分次片 `\mathrm{Gr}^F_m`；`\bigwedge^2` 画外积幂；`\xrightarrow{\ \simeq\ }` 画同构；圈号 ①②③ 用段落式，Definition 6.1.10 的 1.–4. 用 `enumerate[label=\arabic*.]`。

## 4. 图（2 处）

| 文件／形式 | 来源页 | 处理方式 |
|---|---|---|
| TikZ 重绘（无独立文件） | 原书 p.299 | 「泊松代数 ⇄ 结合代数」双向平行箭头图（上标 quantization／量子化，下标 classical limit／经典极限）。纯线条＋英文词标签，按规则 TikZ 重绘、图内标注译中文；图后注释 `% [图：原书 p.299，本图按原文重绘，图内标注已译为中文；原图无题注]` |
| `figures/fig_p304_a.png` | 原书 p.303 | 切空间示意图：球面 M、斜放的切平面 T_pM、点 p，只有数学符号标签 → 裁切 PNG（`figtool auto 298 313` 产出），`\includegraphics[width=0.65\textwidth]` 居中，无题注；注释 `% [图：原书 p.303，图内文字照原样保留；原图无题注]` |

`python tools\figtool.py auto 298 313` 只给出 1 个位图候选（p304），与人工核对一致：本块另有 1 个纯线条箭头图（p.299），已重绘。

## 5. 术语增补（见 `work/term_requests_ch06a.md`）

| 英文 | 译法 | 页 |
|---|---|---|
| formal Weyl algebra | 形式外尔代数 | 302 |
| Weyl bundle | 外尔丛 | 303 |
| symplectic connection | 辛联络 | 304 |
| torsion free | 无挠的 | 304 |
| Levi-Civita connection | 列维-奇维塔联络 | 304 |
| symplectic curvature | 辛曲率 | 306 |
| First Bianchi identity | 第一比安基恒等式 | 306 |
| abelian connection | 阿贝尔联络 | 308 |
| weight（ℤ 分次） | 权 | 309 |
| filtration | 滤链 | 309 |
| graded piece | 分次片 | 311 |
| spectral sequence | 谱序列 | 311 |
| symbol map | 象征映射 | 311 |
| flat section | 平坦截面 | 311 |
| de Rham complex | 德拉姆复形 | 311 |
| globalization | 整体化 | 312 |
| null-homotopic | 零伦的 | 309 |
| fiberwise | 逐纤维 | 303 |
| noncommutative torus / quantum torus | 非交换环面／量子环面 | 301 |
| continuous field of C*-algebras | 连续 C* 代数场 | 301 |
| Rieffel | 里费尔 | 301 |
| Hodge | 霍奇 | 309 |

## 6. 自检

- 编译：`powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch06a`
  `LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0` / `DRAFT PDF -> work\tmp_ch06a.pdf`（18 页）
- lint：`python tools\lint.py ch06a`
  `OK   ch06a       汉字 22961  节 2  小节 8  陈述 21  公式 130  图 1(TikZ 1)  批注 1` / `合计：问题 0 条，提示 0 条`
- 页标：297–312 共 16 个，连续无缺口、无越界
- 预览抽查（`work\preview\ch06a_{1,5,7,8,14,18}.png`）：首页章标题与定义 6.1.1、严格形变量子化四条、外尔丛页的裁切图、定义 6.2.2、定理 6.2.7、末页 takeaway —— 公式与原书一致、无溢出页边、图清晰、中文标点全角
- 每节 1 个 `\takeaway`（§6.1 末、§6.2 末），均 40–90 汉字，只概述本节内容

## 7. 存疑与批注

- **Tutor Note（1 条）**：定理 6.2.4 证明中原文作 "which is equivalent to the total symmetry of ξ"，但该句讨论的是 β(X,Y,Z):=ω(α(X,Y),Z) 的全对称性；已照原文录入并在其后加 `% [Tutor Note: …]`，正文不改。
- 原书 p.303 末「{Γ(U,𝒲} | U ⊂ M open subset}」花括号不配对，译文按数学含义写作 {Γ(U,𝒲) | U ⊂ M 为开子集}，不加批注。
- 定义 6.1.10 中 $Q_0$ 是 $C_c^\infty(M)$ 到 $C_0(M)$ 的「典范包含」（canonical inclusion），照原文译。
- p.309 的霍奇型关系 δδ*+δ*δ=p+q：p 是微分形式次数、q 是 Sym^q 的次数，按原书排版把右侧写成 $p+q$ 并注明所在空间。
- 定义 6.1.10 里 "Planck's constant h" 在原文排版为 ℏ，译文照原文用 $\hbar$。
