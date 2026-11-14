# 第 9 章后半（9.4–9.7）原文疑误与待核清单

- 9.4–9.5（PDF p258–p273）：译者 ch01-symplectic，条目待其追加（见文末）。
- 9.6–9.7（PDF p274–p289）：译者 ch05a-floer，条目见下。
- 说明：下列疑误均在译文中保留原文写法，并加 `% [Tutor Note: ...]` 注释。

## 9.6–9.7（PDF p274–p289）

| # | 位置（印刷页/PDF 页） | 原文 | 疑点 | 建议 |
|---|---|---|---|---|
| 1 | p.269 / PDF 277 | 定理 9.6.1 证明中「where $d_C^{k+1}(c)\in C_{k+2}$ and $f^{k+1}(c)+d_D^k(d)\in D_{k+1}$」 | 本节通篇是\emph{上}链复形（$C^k$、$d^k$），此处却印成下指标 $C_{k+2}$、$D_{k+1}$ | 改为 $C^{k+2}$、$D^{k+1}$（译文照原文保留并加注） |
| 2 | p.271 / PDF 279 | (9.39) 后的「$C^\bullet(U_1+U_2)$」，同段又用 $U_1\cup U_2$ | 「$+$」在此意为并（链群相加），与 $\cup$ 记号混用，易误解为不交并 | 建议统一为 $C^\bullet(U_1\cup U_2)$，或在首次出现处说明 $U_1+U_2:=U_1\cup U_2$ |
| 3 | p.272 / PDF 280 | (9.40) 的三角链：首行 $Y\to0\to Z_1\to Y[1]$、次行 $E_2\to Z_1\to Z_2\to E_2[1]$、末行 $E_{k-1}\to Z_{k-1}\to X\to E_{k-1}[1]$ | 首行以 $Y$ 起、次行却以 $E_2$ 起（相当于把 $Y$ 记作 $E_1$），而「$E_i\in F$，$2\leqslant i\leqslant k-1$」又排除了 $E_1$；记号不闭合 | 待核：建议把 $Y$ 也记作 $E_1$（并写 $E_1=Y$），或统一说明 $E_1:=Y$、$E_k:=X$ |
| 4 | p.274 / PDF 282 | (9.42) 之前：「an embedding $\varphi:\T^n\hookrightarrow(\CP^n,\omega_{\mathrm{FS}})$ is called \emph{exact} if any embedded disk $(\mathbb D^2,\partial\mathbb D^2)\xrightarrow{f}(\CP^n,\varphi(\T^n))$ satisfies」 | 「嵌入圆盘」的边界应落在 $\varphi(\T^n)$ 上（原文由记号隐含），且应对\emph{所有}这样的圆盘成立；原文表述略松，但数学上可读 | 建议明确写「for every embedded disk with boundary in $\varphi(\T^n)$」；译文按原意译出 |
| 5 | p.278 / PDF 286 | 例 9.7.4 中 $X^+=\left((-\infty,0]\times\varphi(S^*_gL)\right)\cup_{\varphi(S^*_gL)}(X\setminus\varphi(D^*_gL))=X\setminus\varphi(0_L)$ | 第一个等号用到 $(-\infty,0]\times S^*_gL\cong D^*_gL\setminus0_L$ 的等同（沿 $\R$-方向伸缩），原文未说明 | 建议补一句「其中 $(-\infty,0]\times S^*_gL$ 经 $(r,\xi)\mapsto\ee^r\xi$ 等同于 $D^*_gL\setminus0_L$」 |
| 6 | p.280 / PDF 288 | 例 9.7.5：「$\mathrm{GW}^{\CP^n}_{L,3}(c^i,c^j,c^k)=1$ if $i+j+k=2n+1$（见事实 8.7.1）」 | 该分次条件依赖第 8 章（事实 8.7.1）的维数/分次约定；本译者无法在本章内独立验证 | 待核：请 ch08 译者核对事实 8.7.1 的编号与 $2n+1$ 条件是否一致 |
| 7 | p.279 / PDF 285 | (9.43)：$\omega_k$ 在 $\widetilde X^-$ 上取 $\ee^{-k}\omega$，在 $[-k,0]\times M$ 上取 $\dd(\ee^r\lambda)$ | 要在 $r=-k$ 处光滑衔接，需 $\omega=\dd\lambda$（或 $\omega=\dd(\ee^r\lambda)$）在 $M$ 的管状邻域内成立；原文默认这一标准设置 | 体例说明：非笔误，但建议在 (9.43) 前加一句「在 $M$ 的接触管状邻域内 $\omega=\dd(\ee^r\lambda)$」 |
| 8 | p.266 / PDF 274 | (9.36) 的嵌套写法「$\mathrm{Cone}(L_{k-1}\to\mathrm{Cone}(L_{k-2}\to\cdots)\cdots\to\mathrm{Cone}(L_2\to\mathrm{Cone}(L_1\to L'))\cdots)$」 | 省略号与括号的嵌套在原文中较含混（排版歧义），不易一眼读出迭代结构 | 建议改写为归纳式：$L^{(j)}=\mathrm{Cone}(L_j\to L^{(j-1)})$、$L^{(0)}=L'$，或加括号说明；译文照原文保留 |

## 体例与宏说明（9.6–9.7）

1. **交换图**：preamble 无 tikz/amscd 等绘图宏包（且禁改 preamble），故 9.6 节的 7 个交换图均用 `array` + `\xrightarrow`、`\big\downarrow`、`\swarrow` 手工排版，已逐页编译核对。
2. **插图**：9 幅（图 9.18–9.26）均从扫描页 300 dpi 裁剪为 `qsg/figures/fig_pNNN_k.png`，经 `read_image` 验证完整；图注为中文并标注原书图号、印刷页、PDF 页。
3. **`Fact` 环境**：本章未用到。
4. **原书 `//` 记号**：例 9.6.1–9.6.3、9.7.1–9.7.5 末尾沿用原书「//」结束记号（`\hfill$//$`）。

## 自检结果（本半 p274–p289）

- `python qsg/tools/check.py ch09b`：本半 **p274–p289 全部覆盖、无缺页、无结构错误、无重复 tag、无缺失图片、无禁用命令**；节 2、keytakeaways 2、Tutor Note 21、图 9、公式编号 11（(9.36)–(9.46)）。
- 试编译（`preamble` + ch09b-s03/s04）通过：14 页，零 Overfull/Underfull、零 undefined；测试文件已删除，未改 preamble/main/00-front 及他人文件。
- 注：整章 `check.py ch09b` 目前仍报缺 p258–p273，属 ch01-symplectic 的 ch09b-s01/s02 尚未完成（其 s01 已出现），非本半缺页。

## 9.4–9.5（译者 ch01-symplectic）

范围：印刷页 250–265，PDF p258–p273。文件 `qsg/tex/ch09b-s01.tex`（9.4，含 p258 顶部 §9.3 收尾）、
`qsg/tex/ch09b-s02.tex`（9.5）；插图 `qsg/figures/fig_p261_1.png` … `fig_p273_1.png` 共 10 幅
（图 9.8–9.17）。

### 跨节接缝说明

- PDF p258 顶部是 §9.3 的收尾（推论 9.3.1 及其证明、命题 9.3.1 证明的后 3/4 页），之后才出现
  「9.4 Distance Between Lagrangians (Large Scale)」。因 ch09a 只覆盖到 p257，该页由本译者承接，
  置于 `ch09b-s01.tex` 开头，并加 `% >>> p258` 标记。
- PDF p264 中部为 9.4 节末尾（`ch09b-s01.tex` 结束）与 9.5 节开头（`ch09b-s02.tex` 开始）的分界，
  两文件均带 `% >>> p264` 标记。
- PDF p274 顶部仍是 9.5 节内容（(9.36)、注 9.5.5），由 ch05a-floer 写入 `ch09b-s03.tex` 开头；
  本译者只写到 p273 页脚，无重复。

### 疑误清单

| # | 位置（印刷页/PDF 页） | 原文 | 疑点 | 建议 |
|---|---|---|---|---|
| 1 | p.251 / p.259、p.252 / p.260 | 练习 9.4.1 的 (ii)「for $L(\kappa)$ obtained from **(a)** above」；(iii)「Deduce from **(a)** above」 | 本题小问标号为 (i)–(iv)，并无 (a)；按上下文均应为 (i) | 改为 (i) |
| 2 | p.252 / p.260 | 「given $r\in\mathbb{R}$, first construct $f_r\in C_c([0,1];\mathbb{R})$」，而上文简化定理要求 $r,s\in[0,\infty)$ | 定义域前后不一致；$r<0$ 时 $f_r\le0$，几何解释需对称处理 | 统一为 $r\ge0$（或说明 $r$ 任意、结论对 $\|r-s\|$ 成立） |
| 3 | p.254 / p.262 | 事实 9.4.1 (ii)「a Hamiltonian function $F:[0,1]\times M\to\mathbb{R}$」 | 本事实的辛流形是 $(\CP^1,\omega_{\mathrm{FS}})$，此处 $M$ 应为 $\CP^1$（沿用了第 1 章的通用记号） | $F:[0,1]\times\CP^1\to\mathbb{R}$ |
| 4 | p.255 / p.263、p.256 / p.264 | Alexander 技巧中用参数 $s$（$\psi_s$、$s\in[\epsilon,1]$），而 (9.33) 直接写 $\psi_\epsilon$ | 相当于在 (9.33) 处取 $s=\epsilon$，原文未交代这一替换 | 在 (9.33) 前说明「取 $s=\epsilon$」 |
| 5 | p.256 / p.264 | 「Since $H_t$ needs to be compactly **support**」 | 语法：应为 compactly supported | 语义译为「需具有紧支撑」 |
| 6 | p.257 / p.264 等多处 | 「homogenous quasi-morphism」 | 拼写：应为 homogeneous（齐次） | 译文统一按「齐次」处理 |
| 7 | p.262 / p.270 | 定义 9.5.2：「the fiber of the projection $\pi:V\to\mathbb{R}^2$ is $\bigcup_{i}([R,+\infty)\times\{s=i\}\times L_i)$」 | 该式给出的是**原像** $\pi^{-1}(\{t\ge R\})$，而非单点上的纤维；单点纤维应为 $L_i$ 或空集 | 改为「$\pi(V)\cap\{t\ge R\}=\bigcup_i([R,+\infty)\times\{s=i\})$，且 $\pi^{-1}([R,+\infty)\times\{s=i\})=[R,+\infty)\times\{s=i\}\times L_i$」 |
| 8 | p.259 / p.267 | 「$a(t),b(t)$ 是 $\mathbb{R}$ 上固定的函数……且 $\gamma(t)$ is smooth for $t\in[0,1]$」 | 按前后文 $\gamma$ 定义在整个 $\mathbb{R}$ 上，限定 $t\in[0,1]$ 与「$\mathbb{R}$ 上的函数」矛盾 | 应为「$\gamma(t)$ 在 $t\in\mathbb{R}$ 上光滑」 |
| 9 | p.264 / p.272 | $\mathrm{Mor}(L,L')$ 定义中「$V$ is a Lagrangian cobordism; $L_1\cdots,L_{k-1}$ are Lagrangians」 | 逗号缺失；且未说明 $k$ 可等于 1（此时即平凡配边） | 补逗号，并说明 $k=1$ 时 $L_1=\cdots=L_{k-1}=\varnothing$ |
| 10 | p.257 / p.265 | 引理 9.5.1 出处写作「(Proposition in 3.1.E in [180])」 | 编号体例怪异，应为「[180] 第 3.1.E 节中的命题」 | 已按此意译为「[180] 中命题 3.1.E」 |
| 11 | p.252 / p.260 | 简化定理写「嵌入 $\Phi:([0,\infty),|\cdot|)\hookrightarrow(\mathcal{O}(L),\delta_{\mathrm{CH}})$」，而定理 9.4.1 用 $C_c^\infty([0,1];\mathbb{R})$、证明中用 $C_c([0,1];\mathbb{R})$ | 三处定义域口径不同（非笔误，仅记，便于对照） | 无需改动 |

### 体例与术语（9.4–9.5）

1. **图**：图 9.8–9.17 共 10 幅，均按 150 dpi 页面图像素坐标裁剪、300 dpi 输出，
   `read_image` 逐幅验证完整无截断；图注为中文并标注原书图号、印刷页、PDF 页。
2. **术语**：Lagrangian suspension 译「拉格朗日悬浮」；Lagrangian surgery 译「拉格朗日手术」；
   quasi-morphism 译「拟同态」（与第 1 章一致）；defect 译「缺陷」；shadow 译「影子」；
   displaceable 译「可位移的」；cobordism category 译「配边范畴」；hom-set 译「同态集」；
   unit 译「单位」；scl 保留记号并注「换位子长度的齐次化」。人名 Chekanov、Hofer、Bavard、
   Alexander、Biran、Cornea 一律保留拉丁字母。
3. **`//` 结束记号**：例 9.5.1 末尾沿用原书「//」。
4. **$L_1\#_xL_2$**：原书用 $\#$ 记手术，译文保留（`\#`），并注意与「连通和 $\#$」区分。

### 自检结果（本半 p258–p273）

- `python qsg/tools/check.py ch09b`：**p258–p273 全部覆盖、无缺页、无结构错误、无重复 tag、
  无缺失图片、无禁用命令**；本半节 2、keytakeaways 2、Tutor Note 14、图 10、
  公式编号 (9.26)–(9.35) 共 10 个。
- 试编译（`preamble` + ch09b-s01/s02）通过：14 页，0 error，无 Missing character；测试文件
  在 `work/tmp/`，未改 preamble/main/00-front 及他人文件。

