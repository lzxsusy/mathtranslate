# BRST 约化

- **id**：`bdh/concept/brst-reduction`
- **类型**：concept
- **位置**：§7.13
- **问题**：为什么解方程 $\{Q^{c},i^{c}_n\}=\mathcal{L}ie_n$ 得到的 $Q^{c}$ 自动满足 $\{Q^{c},Q^{c}\}=0$，而 $H^{0}$ 又恰好给出哈密顿约化？

> 在 $\mathcal{C}l^{\cdot}\otimes\mathcal{R}$ 上解出唯一的 $Q^{c}$（$\{Q^{c},i^{c}_n\}=\mathcal{L}ie_n$），或在 $\mathrm{Cl}^{\cdot}\otimes R$ 上取其量子类比，以 $d=\operatorname{Ad}_Q$ 为微分；正则时 $H^{0}$ 正是哈密顿约化。

## 定义

设 $\mathfrak{n}$ 是有限维李代数。取 $F=\mathfrak{n}$ 的 Clifford 代数 $\mathrm{Cl}^{\cdot}=\mathrm{Cl}^{\cdot}_{\mathfrak{n}}$，其分次使 $F$ 的度为 $-1$、$F^{*}$ 的度为 $1$；置 $\mathrm{Cl}^{\cdot}_i:=\Lambda^{\le i}F\cdot\Lambda F^{*}$，并令经典 Clifford 代数 $\mathcal{C}l^{\cdot}:=\operatorname{gr}\mathrm{Cl}^{\cdot}$，它是交换分次泊松代数，由 $F=\mathcal{C}l^{-1}_1$ 与 $F^{*}=\mathcal{C}l^{0}_1$ 自由生成，$\{f,f^{*}\}=f^{*}(f)$（7.13.1）。经典设定是：$\mathcal{R}$ 为泊松代数，$l^{c}:\mathfrak{n}\to\mathcal{R}$ 为李代数态射，$\mathcal{A}^{\cdot}:=\mathcal{C}l^{\cdot}\otimes\mathcal{R}$ 带附加分次 $\mathcal{A}^{\cdot}_{(i)}:=\mathcal{C}l^{\cdot}_i\otimes\mathcal{R}$，并有李代数态射 $\mathcal{L}ie:\mathfrak{n}\to\mathcal{A}^{0}$，$\mathcal{L}ie_n:=a^{c}(n)\otimes1+1\otimes l^{c}(n)$（7.13.2）。引理 7.13.3（本质上属于 Akman）断言：存在唯一 $Q^{c}=Q^{c}_{\mathcal{A}}\in\mathcal{A}^{1}$，使对一切 $n$ 有 $\{Q^{c},i^{c}_n\}=\mathcal{L}ie_n$；事实上 $Q^{c}\in\mathcal{A}^{1}_{(\le1)}$，且 $\{Q^{c},Q^{c}\}=0$。于是 $d:=\operatorname{Ad}_{Q^{c}}=\{Q^{c},\cdot\}$ 是 $\mathcal{A}$ 的度 $1$ 平方零导子，$\mathcal{A}$ 成为泊松 DG 代数，称为 $\mathcal{R}$ 的 BRST 约化；若 $H^{i}\mathcal{A}=0\ (i\ne0)$ 则称约化是正则的（7.13.4）。量子设定是：$R$ 为结合代数，$\mathfrak{n}^{\flat}$ 为 $\mathfrak{n}$ 被 $\mathbb{C}$ 的中心扩张，$l:\mathfrak{n}^{\flat}\to R$ 为李代数态射且 $l(1_{\mathfrak{n}^{\flat}})=-1$，$A^{\cdot}:=\mathrm{Cl}^{\cdot}\otimes R$；引理 7.13.7 给出唯一 $Q=Q_A\in A^{1}$ 使 $[Q,i_n]=\operatorname{Lie}_n$，且 $Q\in\mathrm{Cl}^{1}_1\otimes R$、$Q^{2}=0$，取超意义下的 $\operatorname{Ad}_Q$ 得结合 DG 代数，同样称为 BRST 约化（正则性定义相同）。经典正则时 $H^{i}\mathcal{A}=0\ (i<0)$ 且 $H^{0}\mathcal{A}\cong[\mathcal{R}/\mathcal{R}l^{c}(\mathfrak{n})]^{\mathfrak{n}}$（7.13.5），这正是 $\mathcal{R}$ 关于哈密顿作用 $l^{c}$ 的通常哈密顿约化。

**记号**：$\mathrm{Cl}^{\cdot}$：$F\oplus F^{*}$ 的 Clifford 代数，$F$ 度 $-1$、$F^{*}$ 度 $1$；$\mathcal{C}l^{\cdot}=\operatorname{gr}\mathrm{Cl}^{\cdot}$ 为经典（泊松）Clifford 代数、$i^{c}_n$、$i_n$：$\mathcal{C}l^{-1}_1\subset\mathcal{A}^{-1}_{(1)}$ 与 $\mathrm{Cl}^{-1}_1\subset A^{-1}$ 中对应 $n$ 的元素，起「内乘」作用、$\mathcal{L}ie_n$、$\operatorname{Lie}_n$：$a(n)\otimes1+1\otimes l(n)$ 型元素，是李代数态射 $\mathfrak{n}\to\mathcal{A}^{0}$（或 $A^{0}$）的取值、$\mathcal{A}^{\cdot}_{(i)}$、$A_{(i)}$：由 Clifford 滤链诱导的附加分次，$Q^{c}=Q_1+Q_0$ 就按此分解、$Q^{c}_{\mathcal{A}}$、$Q_A$：由 $\{Q^{c},i^{c}_n\}=\mathcal{L}ie_n$（经典）或 $[Q,i_n]=\operatorname{Lie}_n$（量子）唯一确定的 BRST 荷

## 关键点

- 引理 7.13.3 的存在性证明把 $\mathcal{A}$ 看成 $\Lambda\mathfrak{n}$-模（$n$ 作用为 $\operatorname{Ad}_{i^{c}_n}=\{i^{c}_n,\cdot\}$）：被所有 $\operatorname{Ad}_{i^{c}_n}$ 零化的子空间等于 $\Lambda\mathfrak{n}\otimes\mathcal{R}\subset\mathcal{A}^{\le0}$，这给唯一性；自由性加 $n_1,n_2\mapsto\{\mathcal{L}ie_{n_1},i^{c}_{n_2}\}$ 的斜对称性给存在性。
- $\{Q^{c},Q^{c}\}=0$ 的验证只用 Jacobi：$\operatorname{Ad}_{i^{c}_n}\operatorname{Ad}_{i^{c}_{n'}}(\{Q^{c},Q^{c}\})=2\{i^{c}_{[n,n']},Q^{c}\}+2\{\mathcal{L}ie_{n'},\mathcal{L}ie_n\}=0$，而被 $\Lambda\mathfrak{n}$ 零化又落在 $\mathcal{A}^{\le0}$ 的元素必为零。
- 7.13.4：$Q^{c}=Q_1+Q_0$，$Q_1\in\mathcal{A}^{1}_{(1)}=\mathfrak{n}\otimes\Lambda^{2}\mathfrak{n}^{*}\otimes\mathcal{R}$、$Q_0\in\mathcal{A}^{1}_{(0)}=\mathfrak{n}^{*}\otimes\mathcal{R}$；微分按附加分次分解为双微分 $d'$、$d''$，$\mathcal{A}$ 是相应双复形的全复形，$\mathcal{A}_{(0)}=C(\mathfrak{n},\mathcal{R})$ 是 DG 子代数并给出 (365)。
- $(\mathcal{A}^{\cdot}_{(-)},d'')$ 是 Koszul 复形 $P=\Lambda^{-\cdot}\mathfrak{n}\otimes\mathcal{R}$，$\mathcal{A}$ 是 $C^{\cdot}(\mathfrak{n},P)$；$\mathcal{A}/\mathcal{I}\cong C(\mathfrak{n},\mathcal{R}/\mathcal{R}l^{c}(\mathfrak{n}))$ 给出 (366)。$l^{c}$ 正则（即 $H_i(P)=0,\ i\ne0$）时 (366) 是同构，故 $H^{0}\mathcal{A}\cong[\mathcal{R}/\mathcal{R}l^{c}(\mathfrak{n})]^{\mathfrak{n}}$，即哈密顿约化（7.13.5）。
- 量子版：$a:\mathfrak{n}^{\flat}\to\mathrm{Cl}^{0}$ 满足 $a(1_{\mathfrak{n}^{\flat}})=1$，而 $l(1_{\mathfrak{n}^{\flat}})=-1$，两者抵消使 $\operatorname{Lie}:=a+l$ 下降为 $\mathfrak{n}\to A^{0}$ 的李代数态射；$Q\in\mathrm{Cl}^{1}_1\otimes R$，$d=\operatorname{Ad}_Q$（对奇 $v$ 有 $dv=Qv+vQ$）；7.13.8 还给出与微分相容的嵌入 $C(\mathfrak{n},R)\subset A$，即 (367)。

## 公式

```latex
\{Q^{c},i^{c}_n\}=\mathcal{L}ie_n,\qquad \mathcal{L}ie_n:=a^{c}(n)\otimes1+1\otimes l^{c}(n)
```
```latex
d:=\operatorname{Ad}_{Q^{c}}=\{Q^{c},\cdot\},\qquad d^{2}=0
```
```latex
[Q,i_n]=\operatorname{Lie}_n,\qquad Q^{2}=0
```
```latex
H^{0}\mathcal{A}\xrightarrow{\ \sim\ }[\mathcal{R}/\mathcal{R}l^{c}(\mathfrak{n})]^{\mathfrak{n}}
```

## 定理

**引理 7.13.3（经典 BRST 荷的存在唯一性）**：存在唯一元素 $Q^{c}=Q^{c}_{\mathcal{A}}\in\mathcal{A}^{1}$，使得对任意 $n\in\mathfrak{n}$ 有 $\{Q^{c},i^{c}_n\}=\mathcal{L}ie_n$；此时 $Q^{c}\in\mathcal{A}^{1}_{(\le1)}$ 且 $\{Q^{c},Q^{c}\}=0$。

证明：略证（§7.13.3，原书 p.338）

- 把 $\mathcal{A}$ 视为 $\Lambda\mathfrak{n}$-模，$n$ 的作用为 $\operatorname{Ad}_{i^{c}_n}=\{i^{c}_n,\cdot\}$；其零化子（即 $\mathfrak{n}\subset\mathcal{A}^{-1}_{(1)}$ 的中心化子）等于 $\Lambda\mathfrak{n}\otimes\mathcal{R}\subset\mathcal{A}^{\le0}$，这给出 $Q^{c}$ 的唯一性
- 该 $\Lambda\mathfrak{n}$-模自由，故存在性等价于 $n_1,n_2\mapsto\{\mathcal{L}ie_{n_1},i^{c}_{n_2}\}$ 的斜对称性，而这是李括号的斜对称性
- 由 $\mathcal{L}ie_n\in\mathcal{A}^{0}_{(\le1)}$ 得 $Q^{c}\in\mathcal{A}^{1}_{(\le1)}$；最后用 Jacobi 计算 $\operatorname{Ad}_{i^{c}_n}\operatorname{Ad}_{i^{c}_{n'}}(\{Q^{c},Q^{c}\})=2\{i^{c}_{[n,n']},Q^{c}\}+2\{\mathcal{L}ie_{n'},\mathcal{L}ie_n\}=0$，故 $\{Q^{c},Q^{c}\}=0$

**引理 7.13.5（正则性给出哈密顿约化）**：若 $l^{c}$ 正则（$H_i(P)=0,\ i\ne0$，$P=\Lambda^{-\cdot}\mathfrak{n}\otimes\mathcal{R}$），则 (366) 是同构；于是 $H^{i}\mathcal{A}=0\ (i<0)$ 且 $H^{0}\mathcal{A}\cong[\mathcal{R}/\mathcal{R}l^{c}(\mathfrak{n})]^{\mathfrak{n}}$。

证明：略证（§7.13.4–7.13.5，原书 p.338–339）

- 正则性即投影 $P\to\mathcal{R}/\mathcal{R}l^{c}(\mathfrak{n})$ 是拟同构
- 故 $\mathcal{A}\to C^{\cdot}(\mathfrak{n},\mathcal{R}/\mathcal{R}l^{c}(\mathfrak{n}))$ 是拟同构，过渡到上同调得 (366) 是同构
- 取 $i=0$ 并注意 $C^{\cdot}(\mathfrak{n},-)$ 的 $H^{0}$ 是 $\mathfrak{n}$-不变量，得 $H^{0}\mathcal{A}\cong[\mathcal{R}/\mathcal{R}l^{c}(\mathfrak{n})]^{\mathfrak{n}}$

## 常见错误

- 把经典与量子的归一化混用：经典 $l^{c}:\mathfrak{n}\to\mathcal{R}$ 不带任何单位元条件，量子 $l:\mathfrak{n}^{\flat}\to R$ 则要求 $l(1_{\mathfrak{n}^{\flat}})=-1$。这个 $-1$ 与 $a(1_{\mathfrak{n}^{\flat}})=1$ 相消，才使 $\operatorname{Lie}=a+l$ 在中心元上取零、从而下降为 $\mathfrak{n}$ 的态射；漏掉符号就得不到 $\operatorname{Lie}_{[n_1,n_2]}=[\operatorname{Lie}_{n_1},\operatorname{Lie}_{n_2}]$，引理 7.13.7 的证明前提不成立。
- 把 $Q^{c}$ 当成附加分次的齐次元：$Q^{c}=Q_1+Q_0$，$Q_1\in\mathcal{A}^{1}_{(1)}=\mathfrak{n}\otimes\Lambda^{2}\mathfrak{n}^{*}\otimes\mathcal{R}$ 与 $Q_0\in\mathcal{A}^{1}_{(0)}=\mathfrak{n}^{*}\otimes\mathcal{R}$ 缺一不可；只保留 $Q_1$ 会丢掉 $d''$ 部分，Koszul 复形 $P$ 随之算错，正则性判据与 $H^{0}$ 的计算全部失效。
- 把「正则」的两个层次混为一谈：7.13.4 的正则性指 $H^{i}\mathcal{A}=0\ (i\ne0)$（BRST 约化本身），7.13.5 的正则性指 Koszul 复形 $P$ 正合（$l^{c}$ 正则）；后者强得多且是可检验的线性条件。不验证 $H_i(P)=0$ 就断言 (366) 是同构，等于把 7.13.5 的假设悄悄用掉，得到的 $H^{0}\mathcal{A}\cong[\mathcal{R}/\mathcal{R}l^{c}(\mathfrak{n})]^{\mathfrak{n}}$ 可能是错的。

## 批注

### 易错预警：原书 p.338 的 $\mathcal{A}^{1}_{(1)}$ 疑为 $\mathcal{A}^{1}_{(0)}$

7.13.4 在分解 $Q^{c}=Q_1+Q_0$ 时，把 $l^{c}$ 所在的齐次项印成 $l\in\operatorname{Hom}(\mathfrak{n},\mathcal{R})=\mathcal{A}^{1}_{(1)}$；但 $\operatorname{Hom}(\mathfrak{n},\mathcal{R})=\mathfrak{n}^{*}\otimes\mathcal{R}=\mathcal{A}^{1}_{(0)}$，与前一句 $Q_0\in\mathcal{A}^{1}_{(0)}$ 一致，故末项应为 $(0)$。中译校订本以译注保留原文并说明理由。若照 $(1)$ 读，就会把 $Q_0$ 与 $Q_1$ 放在同一个附加分次里，双复形分解与 (366) 的 Koszul 复形都无法对齐。

### 背景直觉：BRST 是哈密顿约化的精致版本

7.13 开头说明：BRST 是哈密顿约化的 refined 版本，在无穷维情形尤其重要；正文两次真正调用它——定义 Feigin–Frenkel 同构，以及构造 Hecke 证明中的局部化函子 $L\Delta$（7.14）。有限维的模型就是这里：$\mathcal{A}_{(0)}=C(\mathfrak{n},\mathcal{R})$ 已经是 Chevalley 复形，正则性把它的上同调与 $\mathcal{A}$ 的上同调对齐，于是 $H^{0}$ 精确复现 $[\mathcal{R}/\mathcal{R}l^{c}(\mathfrak{n})]^{\mathfrak{n}}$。理解这个有限维模型后，7.13.16 起用 Tate 中心扩张做的半无限版本才有对照物。

### 含糊点拨：为什么 $Q$ 的存在性是「自由性 + 斜对称」

解 $\{Q,i^{c}_n\}=\mathcal{L}ie_n$ 看似是无穷多个方程，但把 $\mathcal{A}$ 看成 $\Lambda\mathfrak{n}$-模后，$i^{c}_n$ 就是乘 $n$ 再取括号（即 $\operatorname{Ad}_{i^{c}_n}$）。$\Lambda\mathfrak{n}$ 在 $\mathcal{A}$ 上的作用是自由的，故只需在生成元（一次项）上解，斜对称性 $\{\mathcal{L}ie_{n_1},i^{c}_{n_2}\}=-\{\mathcal{L}ie_{n_2},i^{c}_{n_1}\}$ 正好是唯一障碍；而所有 $\operatorname{Ad}_{i^{c}_n}$ 的零化子只含 $\mathcal{A}^{\le0}$，这既保证唯一性，也解释了为何 $Q^{c}\in\mathcal{A}^{1}_{(\le1)}$ 而不是更高阶。量子版 7.13.7 的证明「与经典版本相同」，正是同一论证的逐字搬运。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §7.13.2–7.13.3；印刷页 [337, 338] / PDF 页 [337, 338]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch07.tex:2938-2955`
- 原书 p.337–338：\SourcePage{338} 在第 2940 行，2938–2939 属 p.337，2940–2955 属 p.338。本书 PDF 页 = 印刷页。
- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §7.13.4；印刷页 [338, 339] / PDF 页 [338, 339]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch07.tex:2956-2976`
- 原书 p.338–339：\SourcePage{339} 在第 2962 行，2956–2961 属 p.338，2962–2976 属 p.339。
- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §7.13.6–7.13.7；印刷页 [340] / PDF 页 [340]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch07.tex:2983-2997`
- 原书 p.340：\SourcePage{340} 在第 2983 行、\SourcePage{341} 在第 3005 行，锚点整段落在两者之间。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
