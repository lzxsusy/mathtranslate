# 第 8 章审校记录（review_ch08.md）

范围：原书 Chapter 8 *Quantum Cohomology*。
本文件的条目 3–9 由 **第 8 章后半译者（ch08 后半：§8.5–§8.7，PDF p.225–p.238）** 记录；
条目 1–2 属 §8.4 末尾（同一 PDF 页 p.225），供前半译者核对。若前半译者另建了同文件，
请把本文件的条目合并（勿覆盖）。
「页」为印刷页码；PDF 页码 = 印刷页码 + 8。

| # | 页 / 位置 | 原文（照录/描述） | 疑点 | 建议改法 |
|---|---|---|---|---|
| 1 | p.217（PDF 225），§8.4 末尾 | `then ℓ(x)+ℓ(−x) = (−a)+a = 0` | 定理 8.4.1 的结论是 $\ell(x)+\ell(x^{-1})\ge-c$，而 $\ell(-x)$ 对 Novikov 环元素无定义，应为 $\ell(x^{-1})$ | 改为 `ℓ(x)+ℓ(x⁻¹)` |
| 2 | p.217（PDF 225），§8.4 末尾 | `x* y = (−1)^{deg x deg y} y*x` 等超对称性 | 无错误；仅提示与 §8.7 量子乘积的符号约定须一致 | — |
| 3 | p.223（PDF 231），$\Phi$ 的改写 | 第一行内层求和写作 `Σ_{i=1}^{n} t_i e_i` | 基为 $\{e_0,\cdots,e_n\}$（$n+1$ 个元素），定义 (8.47) 亦作 $\sum_{i=0}^{n}$；此处应为 $i=0$ | 改为 `Σ_{i=0}^{n}` |
| 4 | p.225（PDF 233），定理 8.6.1 末句 | `for any 0 ≤ i, j ≤ n`（在 (8.49) 之后） | $i,j$ 已被求和为哑指标，此句重复且错误；应约束 $a,b,c,d$ | 改为 `for any 0 ≤ a,b,c,d ≤ n` |
| 5 | p.225（PDF 233），例 8.6.3 | `Φ₂₁₂ = Σ_{d≥2} N_d t₂^{3d−4}/(3d−4)! q^d e^{dt₁}` | 该式实为 $\Phi_{222}=\partial^3/\partial t_2^3\Phi$；真正的 $\Phi_{212}=\partial_{t_1}\partial_{t_2}^2\Phi=\sum_{d\ge1}N_d\,t_2^{3d-3}/(3d-3)!\,q^d\,d\,\ee^{dt_1}$（与 $\Phi_{122}$ 相同）。而 (8.50) 恰需 $\Phi_{222}$ | 下标改为 `Φ₂₂₂` |
| 6 | p.225（PDF 233），例 8.6.3 | `This holds trivially since Φ₀₀₀ = Φ₁₁₀ = 0 and Φ₁₀₁ = Φ₁₁₀ = 0.` | 与所给 $\Phi=\frac12t_0^2t_1+\ee^{t_1}q$ 不符：按此 $\Phi$ 有 $\Phi_{100}=\Phi_{010}=\Phi_{110}=1\ne0$，而 $\Phi_{000}=\Phi_{101}=0$。此时 (8.49) 的两端分别等于 $\Phi_{100}\Phi_{110}=1$ 与 $\Phi_{010}\Phi_{101}+\Phi_{110}\Phi_{100}=1$，等式仍成立，但并非「trivially」由所列零点得到 | 改为说明 $\Phi_{000}=\Phi_{101}=0$ 且 $\Phi_{100}=\Phi_{110}=1$，两端同为 1 |
| 7 | p.224（PDF 232），例 8.6.2(i) | 系数写作 `1/(2!1!)`、`1/(1!2!)` | 按 (8.47) 的重数因子应为 $1/(\alpha_0!\alpha_1!\alpha_2!)$，即 $1/(2!\,0!\,1!)$；原文省略了 $0!$，数值上无碍 | 补全为 `1/(2!0!1!)`、`1/(1!2!0!)` |
| 8 | p.228（PDF 236），例 8.7.1 | `c ∗ c ∗ ··· ∗ c = c ∗ cⁿ = T^L = T^L·1` | 记号不严谨（「$(n+1)$ 个 $c$ 相乘」写作 $c*c^n$），且未说明 $T^L$ 与 $T^{\omega(L)}$ 的约定 | 建议写为 $\underbrace{c*\cdots*c}_{n+1}=T^L\cdot1$ 并注明 Novikov 约定 |
| 9 | p.226（PDF 234），例 8.6.4 | `N₄ = 620, N₅ = 87304, N₆ = 26312976, N₇ = 14616808192` | 已用 (8.51) 复核：$N_4,N_5,N_6,N_7$ 与所列数值一致，无误（记录于此作为核对凭据） | — |

## 说明

- 第 3–6 项为实质性的公式/记号问题，译文中对应位置已加 `% [Tutor Note: ...]` 说明，
  并**保留原文写法**（第 5、6 项在批注中给出正确形式）。
- 第 7、8 项为记号不严谨，不影响结论；译文按语义通顺处理，未逐字照录分母。
- 第 9 项为正向核对记录，供审校者抽查递推公式 (8.51) 的实现是否正确。
- 其余细节：§8.7 中 PSS 映射 $\Phi_{\mathrm{PSS}}$ 的定义域写作
  $\mathrm{HF}_*(M,\omega,H,J)$，而定理 5.4.1 的原始记号可能带不同下标约定，
  译文按原书照录，读者可对照第 5 章核对。

---

# 附：第 8 章前半（§8.0–§8.4，PDF p.203–224）审校记录

由 **ch08b 前半译者（§8.0–§8.4，PDF p.203–p.224）** 追加；编号接上表（10 起）。
「页」为印刷页码；PDF 页码 = 印刷页码 + 8。对应源码：`ch08-s01.tex`（章首引言 + §8.1）、
`ch08-s02.tex`（§8.2）、`ch08-s03.tex`（§8.3）、`ch08-s04.tex`（§8.4）。

| # | 页 / 位置 | 原文（照录/描述） | 疑点 | 建议改法 |
|---|---|---|---|---|
| 10 | p.195（PDF 203），章首引言 | `this is the born of the quantum cohomology` | `born` 应为 `birth`（名词误用） | 改为 `birth` |
| 11 | p.195（PDF 203），同上 | `... from various symplectic machinery. therefore, only requiring ...` | 句号后 `therefore` 小写，前句句号应改为分号（或 `Therefore` 大写另起） | 标点/大小写修正 |
| 12 | p.195（PDF 203），同上 | `quantities rend off from various symplectic machinery` | `rend off` 疑为 `rendered off`（或 `descending from`）之误 | 改为 `rendered off` |
| 13 | p.196（PDF 204），例 8.0.1 末句 | `there is no uniform κ>0 satisfying the monotone condition (8.2)` | 单调条件应为 (8.1)；(8.2) 是 $\CP^n$ 上的具体计算 | 改为 `(8.1)` |
| 14 | p.198（PDF 206），§8.1(2) | `Λ^{k,R} ≅ k[T]. Here, k[T] either denotes the completion of the polynomial ring k[T] in the positive direction, or simply follows the standard name, the ring of Laurent series.` | 同一记号 $\mathbf{k}[T]$ 先后指形式幂级数环、多项式环与 Laurent 级数环，三者不同；正确的断言应为 $\Lambda^{\mathbf{k},\Z}\cong\mathbf{k}(\!(T)\!)$（形式 Laurent 级数域），其「正方向完备化」为 $\mathbf{k}[\![T]\!]$ | 分别记作 $\mathbf{k}[T]$、$\mathbf{k}[\![T]\!]$、$\mathbf{k}(\!(T)\!)$ |
| 15 | p.199（PDF 207），(8.6)–(8.7) | `x = Σ a_A T^A ... and t is a formal variable`；`x = Σ a_{(B,λ)} t^{(B,λ)} = Σ(Σ a_{(B,λ)} S^B) T^λ` | 形式变量同一式中先写 $T$、再写 $t$（正文亦作 `t`），前后不一致；按上下文应统一为 $T$ | (8.7) 左端 `t^{(B,λ)}` 改为 `T^{(B,λ)}`，正文 `t` 改为 `T` |
| 16 | p.199（PDF 207） | `Note that so far the sum Σ notations in (8.7) is just a formal sum` | 语法：`notations ... is` 应为 `are`；不影响数学内容 | 语法修正 |
| 17 | p.201（PDF 209），(8.10) | `x ⊥_{(R^n,|·|)} y if and only if |x+y| = |x| + |y|` | **实质错误**：Euclid 范数下正交应满足 $|x+y|^2=|x|^2+|y|^2$；线性关系 $|x+y|=|x|+|y|$ 刻画的是同向共线。作者似把非阿基米德判据 $\ell(x+y)=\max\{\ell(x),\ell(y)\}$（注 8.2.1）误「翻译」成了 Euclid 情形 | 改为 $|x+y|^2=|x|^2+|y|^2$（或 $|x-y|^2=|x|^2+|y|^2$），与注 8.2.1 的非阿基米德类比一致 |
| 18 | p.208（PDF 216），(8.21) 前 | `we will still have a diagram like (??)` | 原书交叉引用未解析，`(??)` 应为 (8.18)（定义 8.3.1 的交换图表） | 改为 `(8.18)` |
| 19 | p.206（PDF 214），定义 8.3.1 | `It is called multiply covered if there exists a J-holomorphic curve u' ... and a holomorphic map φ ...` | 未要求 $\deg(\varphi)\geqslant2$；若允许 $\varphi$ 为双全纯，则任何曲线都平凡地「多重覆盖」，概念失效 | 补上 $\deg(\varphi)\geqslant2$（或要求 $u$ 与 $u'$ 不等价） |
| 20 | p.212（PDF 220），例 8.3.3 | `... the class A = 2L can come from nodal curve ...` 及维数 $4+2\cdot(2\cdot(2+1))+2\cdot0-6-2=8$ | 数值核对无误（$4+12-6-2=8$）；记录作为 (8.28) 的正向核对凭据 | — |
| 21 | p.215（PDF 223），(8.32) | `deg(T) = 2n+2` | 与 $\deg(e_1^{n+1})=2n+2$、$c_1(T\CP^n)=n+1$ 一致，核对无误 | — |
| 22 | p.200（PDF 208） | `The extreme situations are either this subgroup is trivially 0 or is the entire 2Z` | 「this subgroup」指代不明（应为 $\deg$ 在 $H_2^S(M)$ 上取值所生成的子群）；语义可解，但表述含糊 | 建议改为「$\deg(T^A)$ 在 $H_2^S(M)$ 上取值所生成的子群要么平凡、要么为整个 $2\Z$」 |

## 前半部分说明

- 第 13、14、15、17、18、19 项为较实质的问题，译文中对应位置均已加
  `% [Tutor Note: ...]` 说明，并**保留原文写法**（第 17、19 项在批注中给出正确形式）。
- 第 10、11、12、16 项为文字/拼写小误，不影响数学内容，译文按语义通顺处理。
- 两半章的接缝已核对：§8.4 在 PDF p.224（印刷 p.216）并非结束，尚余 PDF p.225 的内容
  （定理 8.4.1 等）由后半译者续写；前半止于练习 8.4.1（p.224 末），无重复、无遗漏。
- 公式编号 $(\text{8.1})$–$(\text{8.35})$ 连续，与后半的 $(\text{8.36})$–$(\text{8.53})$
  无重复、无缺号（`check.py ch08` 全章 36/36 页、53 条编号、无重复）。

