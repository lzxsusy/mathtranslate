# SY02-46 中译本独立审校 r1

**审校范围**：`源码/sections/s00-intro.tex`（引言，p1）、`s01-prelim.tex`（§0，p2–4）、`s02-classfield.tex`（§1，p4–6）、`s03-main.tex`（§2，p6–8），合计 18 + 65 + 88 + 75 = **246 行**；逐句对读法文权威源 `texsrc/Bourbaki2002.tex` L846–1404，并以 `工程文件/work/src/p01.txt`–`p08.txt` 对页复核。
**版本快照**：以 2026-11-27 14:05 的源码为准，sha1 前 8 位——s00 `33a1a9fb`、s01 `6bbc647a`、s02 `44e30c2f`、s03 `a43085d7`。s00-intro.tex 在我首读之后（mtime 14:00:18）有过改动：现版 L8 作「阿贝尔类域论的一个宏大扩展」，与法文 `une vaste extension de la théorie du corps de classes abélien`、与 `glossary.tsv` L4（théorie du corps de classes→类域论）均相符；我首读所见旧文曾作「阿贝尔类域对应……宏大推广」，如交付版仍是旧文，请按此条回改。
**结论**：**通过（0 critical、0 major、2 minor）**。四节与法文逐句对应，公式、上下标、量词、正合列方向、函子方向、编号与术语均一致；两处 minor 同在 s01:37，属术语表未落实与正文增补括号，不影响数学判断。

## 已逐句核验（备查，不计为问题）

- §0 三个三元组（Betti / De Rham / ℓ-进）、`D^b_c(S)` 定义、六种运算、中间反常 t-结构、`V̄=[V/G_m]`、`P(V)=[V°/G_m]=V̄°↪V̄`、齐次 Fourier 变换与逆、`Ψ=β_*C`、`H^0=C`、`H^1=α_*C`、式 (0.1)、定义 (0.2)、引理 (0.3)(0.4)、Radon 变换：与 L899–1120 一一相符。
- s01:21「关于对偶 $D$ 自对偶」对应法文 L980 `auto-duale pour la dualité D`（非 `stable par dualité`），译法正确。
- s01:52、s01:64 两处 `proper` 均按体例保留不译；`\newtheorem*{definitionZ}/{lemmaZ}` 手动编号 (0.2)(0.3)(0.4) 与原文 (0.1)…(0.4) 共用序号的安排自洽（preamble L32–35）。
- §1 全部条目（周期、`J(X)`、`Pic` 正合列、定理 1.1、`Aut_χ`、定理 1.2、代数证明与式 (1.3)）：与 L1127–1271 相符；`d≥2g−1` 两处（s02:74、s02:85）与 L1238、L1261 同为非严格不等式。
- §2 全部条目（`Fib_n(X)`、初等下修改、`deg L′=deg L−1`、Hecke 叠与对应图、`H(K)=(q,p′)_*p^*K[n−1]`、`H∘H` 的 S₂-等变、定义 2.1、定理 2.2、两步证明）：与 L1277–1404 相符；对应图中 `(q,p′)` 取相对维数 n−1、`p` 取 n，顺序与 L1328–1329 一致。
- 编号：§1 两个 theorem → 1.1、1.2；§2 首个 theorem 类环境为 definition → 2.1，其后 theorem → 2.2；「定理 1.2 的代数证明」引用正确。
- 引文键 `[B-B-D] [B-D] [B-L] [Br] [B-G] [Dr 1] [Dr 2] [Dr 3] [F-G-V 2] [Ga] [La] [L-M] [Lau 3] [Ly 1] [Ly 2] [Se]` 在 `s09-refs.tex` 均有对应 `\refitem`。
- 三处译注（s01:10、s01:19、s01:48）内容与原文/事实相符（系数域 C 与 ℂ 之别；原文同一字母 S 兼指代数叠与呈现它的概形；proper 为 (0.2) 术语、与态射的「紧合」无关，BBD = Astérisque 100）。

---

### [minor] s01-prelim.tex:L37

- 原文：`faisceau pervers ponctuel α∗ C[−1] par le faisceau pervers constant C`（`work/src/p03.txt` L43；TeX 原文件此行跨 L1041–1042：`extension du faisceau pervers` / `ponctuel $\alpha_{\ast}C[-1]$ par le faisceau pervers constant $C$.`）
- 译文：`实际上 $\Psi$ 不是不可约反常层，它是 $\alpha_*C[-1]$ 通过常数反常层 $C$ 的扩张（$C$ 为子层，商为 $\alpha_*C[-1]$）。`
- 问题：类别 3（术语）——`faisceau pervers ponctuel` 在 `glossary.tsv` L51 定为「点状反常层」，且其首现页正标为 3（即本句），译文丢了「点状」这一限定语；对象本身已由公式 $\alpha_*C[-1]$ 指明，故不影响数学。
- 建议：`实际上 $\Psi$ 不是不可约反常层，它是点状反常层 $\alpha_*C[-1]$ 通过常数反常层 $C$ 的扩张（$C$ 为子层，商为 $\alpha_*C[-1]$）。`

### [minor] s01-prelim.tex:L37

- 原文：`… extension du faisceau pervers ponctuel α∗ C[−1] par le faisceau pervers constant C.`（`work/src/p03.txt` L43）——原句无括号说明。
- 译文：`（$C$ 为子层，商为 $\alpha_*C[-1]$）`
- 问题：类别 1（增译括号说明）——正文夹注为原文所无。内容经核对无误：法语「extension de A par B」= $0\to B\to E\to A\to 0$，与 `extension du … α_*C[−1] par … C` 相符，故子层为 $C$、商为 $\alpha_*C[-1]$；但它属译者解释，正文宜与原文一一对应。
- 建议：删去该括号，或改用 `\yizhu{...}{术语背景，A（原文 p3）}` 收入译注；若主控认可正文夹注体例，可保留（内容不必改）。

---

## 无法判定

1. 译注标注体例（s01:10、s01:19、s01:48）：`\yizhu` 第二参数现写作「术语背景，A（原文 (0.2)；参 BBD，Astérisque 100）」「术语背景，I（原文 p2；上下文推断）」，而 preamble L41 的注释约定为「出处只许 A·B·I 或「上下文推断」」；现式在 A/I 之外又并列「原文 pN」「上下文推断」，是否统一（例如只留等级，或只留「上下文推断」）属体例问题，不影响内容，未计为错误，请主控裁决。
2. s01:37 那条夹注的去留（见上条 minor）：若项目体例允许正文夹注解释，则无须改动，仅需主控确认；若要求正文严格对应原文，则按建议改为译注。
