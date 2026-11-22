# 10 · Edward Witten《Analytic Continuation Of Chern-Simons Theory》通读笔记

| 项 | 值 |
|---|---|
| 英文题名 | Analytic Continuation Of Chern-Simons Theory |
| 作者 | Edward Witten（单人，IAS） |
| arXiv | 1001.2933 [hep-th]，v1 2010-01-18 / v2 01-21 / v3 02-23 / v4 2010-08-28；本地 PDF 是 v4（p001 页眉 `arXiv:1001.2933v4`） |
| 篇幅 | 127 个 PDF 页（正文 p005–p123 + 参考文献 p123–p127；p001–p004 为标题与目录） |
| 期刊 | AMS/IP Stud. Adv. Math. 50 (2011) 347–446（INSPIRE recid 843014；会议 «Chern-Simons Gauge Theory: 20 Years After», Bonn 2009） |
| 体裁 | 长篇研究论文；**全文没有编号定理**，只有公式号 (n.m)；论证大量用「we expect / should be / it seems」 |

## 0 页码约定

- 本笔记与全部卡片一律用 **PDF 页序**，即 `txt/10/pNNN.txt` 的 NNN；`verify_pages.py` 按此回查。
- 页脚的印刷页号 = **PDF 页序 − 1**（p002 页脚 1、p008 页脚 7、p067 页脚 66、p127 无页脚）。目录印的「1 Introduction 4」对应 PDF p005。
- 公式号按原文 (n.m)；卡片 `anchor` 写成 `A p.NN eq (n.m)`，其中 NN 是**公式所在**的 PDF 页。
- 外部文献的页码一律注明 arXiv 号与节号，不与本篇页序混用。

## 1 一句话

Witten 把三维 Chern–Simons 理论从整数 level k **解析延拓**到非整数：把复化联络 (A,Ã) 的路径积分看成 Picard–Lefschetz 意义下的振荡积分，用 **Lefschetz thimble** 的整系数和描述积分 cycle，用 **Stokes 现象**跟踪 cycle 随参数（γ=n/k 或复 k）的跳变；这套机器给出 CS 流方程出人意料的**四维对称性**（流方程是四维一阶椭圆系统，平方和等于四维 Yang–Mills 作用量加 F∧F），并在三叶结与八字结上具体算出彩色 Jones 多项式的半经典极限；八字结的解析延拓把双曲体积 V 通过 Im W=∓V/2π 带进指数，复现体积猜想的 exp(nV/2π) 增长；最后指出 CS 的可能积分 cycle 构成一个向量空间，可解释为四维扭曲 N=4 超对称 Yang–Mills 的「物理 Hilbert 空间」，从而给 Khovanov 同调一个四维规范论解释的入口。

## 2 文章骨架（节 → PDF 页 → 一句话 → 关键公式）

| 节 | PDF 页 | 一句话 | 关键公式 |
|---|---|---|---|
| 1 Introduction | 005–007 | 动机：3 维量子引力 ≈ SL(2,C) CS；Jones 只在整数 k 定义，希望有解析延拓的规范论解释 | — |
| 2 Overview | 008–023 | 复化作用量、thimble 分解、Stokes、紧群/复群/实形式的 cycle | (2.1)–(2.36) |
| 2.1 有限维类比 | 009–010 | Airy 与 Z_g=∫\|d²z\|exp(g−ḡ)：把 z 与 z̄ 当独立变量 | (2.6)–(2.13) |
| 2.2 Morse 理论的作用 | 011–012 | 临界点=平坦联络对；C=ΣnσJσ，nσ=⟨C,Kσ⟩ | (2.14)–(2.16) |
| 2.3 Stokes 现象 | 012–013 | Jσ 与 nσ 跨 Stokes 曲线跳变，ΣnσJσ 不变；Im I 沿流守恒 | — |
| 2.4 奇点 | 013 | s=∞ 本质奇点、s=±iℓ 奇点；高斯积分类比 | (2.17) |
| 2.5 紧群的解析延拓 | 013–017 | 在覆盖 Û 上取 cycle C，Z_{H,C}(k) 对 k 全纯 | (2.18)–(2.23) |
| 2.5.1 向下流 | 015–017 | 用 h=Re(ikW) 从 C₀ 的边界向下流补 C₁；k∈Z 时回到原积分 | — |
| 2.5.2 C 的不确定性 | 017 | 每个临界点可乘 exp(2πimk)；一般给有限和 Σa_m exp(2πimk) | (2.25) |
| 2.5.3 纽结 | 017–018 | 纽结不变量可延拓为 q 的 Laurent 多项式、无本质奇点 ⇒ C 唯一 | — |
| 2.6 紧群与复群比较 | 018–021 | G=H_C 的 cycle 是 H 的两个 cycle 之积；k₁=t/2−h | (2.26)–(2.28) |
| 2.6.1 纽结（复群） | 019–021 | 全纯表示使 Ã 侧唯一，Z_G(K)=e^{B(t̃)}B(K;t) | (2.29)–(2.31) |
| 2.7 其他实形式 | 021–022 | U 与 U′ 都是 U_C 的实 cycle；k′+h′=k+h | (2.32)–(2.34) |
| 2.7.1 全纯体积形式 | 022–023 | DA=DA′exp(i(h−h′)W)、DÃ=DA exp(ihW) | (2.35)–(2.36) |
| 3 有限维振荡积分 | 024–062 | Airy、Morse 理论、最速下降、Bessel 原型；为 §4–§5 提供全部技术 | (3.1)–(3.75) |
| 3.1 Airy | 024–034 | 三好区域、Stokes 射线、thimble 渐近、单值性 M³=1/−1 | (3.1)–(3.18) |
| 3.2 推广到 n 维 | 035–041 | 复 n 维全纯函数实部的临界点指标恒 n；Morse 引理 | — |
| 3.3 对称性 | 042–049 | 群作用、临界点流形、Im I 守恒；可交换临界点的系数不跳 | — |
| 3.4 奇点 | 049–055 | Airy 型、SO(2) 型、$(uv)^3$ 型三种局部模型 | (3.44)–(3.65) |
| 3.5 对 k 的解析延拓：原型 | 056–062 | Bessel 函数：复 κ 的 contour、ρ=±1 的 Airy 奇点 | (3.66)–(3.75) |
| 4 应用到 CS 理论 | 063–085 | 流方程的四维形式、指标、纽结、临界点分类、W 的变分 | (4.1)–(4.45) |
| 4.1 CS 的流方程 | 064–068 | A=A+iφ 的梯度流 ⇒ (4.8)+(4.10)；平方和 (4.11) | (4.1)–(4.13) |
| 4.1.1 指标 | 067–069 | 四维算子 L 的指标为 0；行列式线丛平凡 | — |
| 4.1.2 流方程的应用 | 069–071 | nσ 的带符号计数；mστ 与 wall-crossing | (4.14) |
| 4.2 纽结与 Morse 理论 | 072–085 | Wilson 圈写成 ρ 场路径积分；有纽结的经典方程 | (4.15)–(4.45) |
| 4.2.1 有纽结的经典方程 | 074 | kF/2π=δ_Kμ_R；U=exp(2πμ_R/k) | (4.20)–(4.23) |
| 4.2.2 再论经典方程 | 075–077 | Nahm 型奇点；U→1 时单值趋于幂幺元 V | (4.24)–(4.31) |
| 4.2.3 非紧群的类比 | 078 | 全纯表示下 Ã 独立；实 cycle 不收敛 | (4.32) |
| 4.2.4 临界点分类 | 079–080 | 临界点=平坦联络+CS 不变量的提升；复群只能对角平移 | (4.33) |
| 4.2.5 作用量的变分 | 081–083 | δW=(1/π)δln l·ln m；A 多项式 | (4.34)–(4.43) |
| 4.2.6 对数的分支 | 084 | ln l 的分支何时是临界点数据 | — |
| 4.2.7 与平坦线丛张量 | 085 | E→E⊗L 结合 n→n+k+2；只对纽结成立 | (4.44)–(4.45) |
| 5 彩色 Jones 的解析延拓 | 086–121 | 三叶结与八字结的详细计算；体积猜想 | (5.1)–(5.68) |
| 5.1 预备 | 087–089 | 实 cycle、canonical lifting、γ=n/k | (5.1)–(5.3) |
| 5.1.1 局部模型 | 090–091 | V=H¹(M,ad E)、Massey 积、三种 Φ | — |
| 5.1.2 路径积分的归一 | 092–093 | (5.4)–(5.6)：η-不变量与解析挠率 | (5.4)–(5.6) |
| 5.1.3 积分 cycle 的定向 | 094 | 平方根奇点 = 绕 k=∞ 的定向反转 | — |
| 5.2 三叶结 | 095–108 | A_nab、l=−m⁻⁶、W、I、Stokes 曲线 | (5.7)–(5.39) |
| 5.2.1 模空间的奇点 | 096–100 | (uv)²/2−ǫuv；n^{1/2} 标度 | (5.7)–(5.24) |
| 5.2.2 CS 函数 | 100 | W=−(3/π)ln²m−π/12−2πs；I=−3πinγ⁻¹(γ−y)² | (5.25)–(5.30) |
| 5.2.3 cycle 与渐近 | 101–103 | J_ab+J_{1/6}−J_{5/6}±…；Z_y 的指数 | (5.31)–(5.33) |
| 5.2.4 Stokes 曲线 | 104–108 | b²=−a(a−y)²/(a−2y)；正虚轴的本质奇点 | (5.34)–(5.39) |
| 5.3 八字结 | 109–121 | A_±、A 多项式、W 的实部/虚部、体积猜想 | (5.40)–(5.68) |
| 5.3.1 m 实 | 110–111 | (uv)³/3−ǫuv；n^{2/3} 标度 | (5.44)–(5.51) |
| 5.3.2 \|m\|=1 | 112–113 | Airy x³/3−ǫx；n^{1/6} 与 n^{2/3} | (5.52)–(5.56) |
| 5.3.3 W 的实部 | 114–116 | Re W≡0 或 π（按 m 的分支） | (5.57)–(5.59) |
| 5.3.4 W 的虚部 | 117 | Im W=∓V/2π；l=−1 | (5.60)–(5.61) |
| 5.3.5 八字结的体积猜想 | 118–121 | J_n∼exp(nV/2π)(e^{−iπk}−e^{iπk}) | (5.62)–(5.68) |
| 6 四维或五维解释 | 122–123 | V 作为 4d 扭曲 N=4 的 Hilbert 空间；Khovanov 的入口 | — |
| References | 123–127 | [1]–[63] | — |

## 3 主命题清单（原文无编号，S1–S17 为笔记所加）

| 编号 | 页 | 命题 | 关键式 |
|---|---|---|---|
| S1 | 008 | 复群 CS 的 W 规范不变模 2π；I=tW/2+t̃W̃/2，t=ℓ+is | (2.1)–(2.4) |
| S2 | 011 | 临界点=一对平坦联络；C=ΣnσJσ，nσ=⟨C,Kσ⟩ | (2.14)–(2.16) |
| S3 | 014–015 | 在覆盖 Û_C 上取 cycle，Z_{H,C}(k) 对 k 全纯；k∈Z 时还原原积分 | (2.18)–(2.23) |
| S4 | 019 | 复群的有效耦合是 k₁=t/2−h、k₂=t̃/2−h | (2.28) |
| S5 | 022–023 | 实形式之间 k′+h′=k+h；测度比 DA=DA′exp(i(h−h′)W) | (2.34)–(2.36) |
| S6 | 065 | 半稳定 ⇔ 单值不严格上三角；矩映射 μ=d_A⋆φ | (4.3)–(4.4) |
| S7 | 066–067 | 流方程 (4.8)+(4.10) 有四维形式；平方和 (4.11) 给出四维 YM 型作用量 | (4.8)–(4.13) |
| S8 | 074–082 | 有纽结时 kF/2π=δ_Kμ_R；U=exp(2πμ_R/k)；m=exp(iπ(n−1)/k) | (4.20)–(4.35) |
| S9 | 084 | δW=(1/π)δln l·ln m；A 多项式 A(l,m)=0 | (4.38)–(4.43) |
| S10 | 085 | E→E⊗L 结合 n→n+k+2；只对纽结成立 | (4.44)–(4.45) |
| S11 | 089 | unknot：J_n(q;K₀)=√(2/(k+2))sin(πn/(k+2)) | (5.3) |
| S12 | 100 | 三叶结：W(Anab)=−(3/π)ln²m−π/12−2πs；I=−3πinγ⁻¹(γ−y)² | (5.25)–(5.30) |
| S13 | 103 | 三叶结的 cycle 是 J_ab+J_{1/6}−J_{5/6}±⋯±J_x | (5.31) |
| S14 | 106 | 三叶结的 Stokes 曲线 b²=−a(a−y)²/(a−2y)，y=±(1/6+p) | (5.39) |
| S15 | 111–113 | 八字结的局部模型 (uv)³/3−ǫuv、Airy；n^{2/3}、n^{1/6} | (5.50)–(5.56) |
| S16 | 118–121 | Im W=∓V/2π；J_n∼exp(nV/2π)(e^{−iπk}−e^{iπk}) | (5.61)–(5.68) |
| S17 | 122–123 | CS 的积分 cycle 空间 V ≅ 4d 扭曲 N=4 SYM 的物理 Hilbert 空间 | §6 |

## 4 与已译文献接口

| 已译篇 | 主题 | 与本篇的接口 |
|---|---|---|
| 01 kw06（67 卡） | 电磁对偶与几何朗兰兹 | 本篇 §4.1 的流方程首见 [53]；**本文的 u 就是 KW 的 t**（脚注 16），且 k=t/2−h 的移位可与 KW 的规范化对照。库内 `datasets/kw06` 有 t-族与 Bogomolny 方程的卡，可逐式对照 |
| 02 SY02-06 | 规范理论、分歧与 GLC | 本篇 §4.2.2 的 Nahm 型奇点、曲面算子来自 [55]（Gukov–Witten），与分歧算子同源；本机无该篇交付目录，只能按主题标注 |
| 06 SY05-25 | 镜像对称、Hitchin 方程与朗兰兹对偶 | 本篇 §4.1 的四维方程是 Hitchin 方程族的近亲（[53]）；本机无该篇交付目录 |
| 11 SY03-01 | 量子力学路径积分的新视角 | Picard–Lefschetz/振荡积分的语言；本机无该篇交付目录 |
| 16 SY01-07 | 几何内窥与镜像对称 | 本机 `datasets/sy0117` 是 Bocklandt《同调镜像对称性浅入门》，与第 16 篇不是同一文献；第 16 篇无本机交付目录，只能按主题标注 |
| 23 SY05-01 | 四维规范场论中的纽结不变量 | 本篇 §5 的 CS 纽结不变量与 4d 边界条件/曲面算子相关；本机无该篇交付目录 |
| 28 datasets/bdh | Hitchin 可积系统量子化与 Hecke 特征层 | oper/特征层与几何 Langlands；本篇 §6 的 V 与 bdh 的 oper 卡可对照，但本文没有直接使用 oper |
| 36 SY03-21 | 朗兰兹纲领与共形场论讲义 | 整体图景与术语定名；本机无该篇交付目录 |
| 12_ggl12（已译） | Fivebranes and Knots | CS/Khovanov 的五维实现；与本篇 §5–§6 的纽结不变量、Khovanov 入口直接相接 |
| 13_ggl13（已译） | Khovanov Homology and Gauge Theory | 复 CS 的 Morse 函数与四维流方程；其 t=tan(α/2) 与本篇 u 完全一致，是最强的库内互证 |
| 19_ggl19 / 22_ggl22（已译） | 量子 GLC / S-对偶边界条件 | 与 §6 的扭曲 N=4 Hilbert 空间、brane 图景相关 |

说明：任务书列的 01/02/06/11/16/23/28/36 八篇里，本机能实际打开交付物的只有 01（`datasets/kw06`）与 28（`datasets/bdh`）；02/06/11/16/23/36 没有本机交付目录，只按 XREF 的主题列接口，待 lead 合并时按实际篇目补行。

## 5 term_index 撞名检查

- 命令：`PY tools/term_index.py check out/10_ggl10/cards` → **检查 15 张卡，与既有语料撞名 0 处**。
- 过程中撞过一次：`ggl10/concept/stokes-jumping` 的别名 `Stokes phenomenon` 与 `pathintegral:pi/concept/stokes-phenomenon` 同名。按「新卡写专、不改旧卡」的原则，把别名改成 `Stokes jumping of Lefschetz thimbles` / `wall-crossing of thimble coefficients`，标题保留「Stokes 曲线与 thimble 系数的跳跃」。
- 术语定名沿用旧库：twist=扭化、eigenbrane=特征膜、Hecke eigensheaf=Hecke 特征层、canonical coisotropic brane=典范余各向同性膜、't Hooft 与 BPS 不译；本篇新增的 Lefschetz thimble 沿用 `seidel` 包的「Lefschetz 顶针」。

## 核对与勘误

### 外部校正动作清单（XREF §4 五项）逐条结论

| 项 | 核了什么 | 结论 |
|---|---|---|
| ① 主定理陈述与符号 | 摘要 + 正文 §1/§2 + arXiv abs 页 + nLab 「analytically continued Chern-Simons theory」 | 一致：解析延拓、Morse/Picard–Lefschetz、四维流方程、三叶结/八字结、4d 扭曲 N=4 的 Hilbert 空间均在摘要与正文中对应。唯一差异：本地 v4 PDF 摘要写 “by generalizing the usual integration cycle”，arXiv 元数据写 “by rotating the integration cycle”——属于摘要措辞/元数据差异，不影响数学内容，不记 errata |
| ② 关键公式系数/符号/指数 | (2.1) 与 `datasets/csw/concept/cs-action`；(4.9) 与 `datasets/ggl13/deriv/complex-cs-gradient-flow`；(5.42)–(5.43) 与 arXiv:0802.0039；(5.24)(5.51) 与 arXiv:0711.2836；(5.61)–(5.62) 与 nLab volume conjecture | (2.1) 的 1/4π、2/3 与 csw 卡一致；(4.9) 的 u 与 ggl13 的 t=tan(α/2) 一致；(5.42) 与 Murakami 综述逐项对上（其 ℓ=l、m=m_W²，与脚注「我们的 m 是 [17] 的 m^{1/2}」一致）；(5.24) n^{1/2}、(5.51) n^{2/3} 分别对上 Hikami–Murakami 的 Theorem 1.2/1.1；(5.62) 的 2π 因子与 nLab 的 (2π/N)log\|V_N\|→vol 一致 |
| ③ 命题编号与交叉引用 | 全文无编号定理；抽查 (5.24)→[16] Thm 1.2、(5.51)→[16] Thm 1.1、(5.34)–(5.39) 的推导链、§5.3.5 的 (5.63)–(5.68) | 链条一致；但发现两处正文笔误 E1（p118 的 γ=k/n）与 E2（p119 的 just greater than 1/3），均已在 errata.tsv 登记 |
| ④ 数值/维数一致性 | γ=n/k 与 p118 的 k/n；γ=±(1/6+p) 与 \|m\|=1 时 m²+m⁻²=2cos2θ∈[−2,2]；k′+h′=k+h；n^{1/6} 与 n^{2/3} 的归一化换算 | 除 E1/E2 外自洽：m²+m⁻²∈[−2,2] 使 (5.28) 与 (5.52) 的区间 [1/3,2/3] 互洽；n^{1/6} 除以 unknot 的 n^{−1/2} 得 n^{2/3}，与 (5.56) 的说明一致；k′+h′=k+h 与 (2.28) 的 t/2−h 在 G=H×H 情形一致 |
| ⑤ 记号前后定义 | m、l、γ、w、u、t、φ_t、W、Ã 的定义与复用 | 基本一致：m、l 在 §4.2.5 与 §5 同义；u 与 [53] 的 t 有脚注 16；w 在 §5.3.5 使用前已由「CS 不变量 2πw」定义。例外是 E1 的 γ=k/n，按 n/k 读 |

### 外部来源

| # | 来源 | 定位 | 核了什么 |
|---|---|---|---|
| 1 | arXiv abs 页 1001.2933（https://arxiv.org/abs/1001.2933，2026-11-23 抓取，HTTP 200） | abs 页 | 四版日期、comment「125 pp, many minor corrections in v. 4」、摘要全文；确认本地 PDF 的 v4 身份与 125 页声明 |
| 2 | INSPIRE-HEP API，recid 843014（https://inspirehep.net/api/literature?q=arxiv%3A1001.2933，2026-11-23 抓取） | JSON `publication_info` | 期刊 AMS/IP Stud. Adv. Math. 50 (2011) 347–446；会议 C09-08-03.10；被引 656 |
| 3 | arXiv:1001.2933v1 PDF（`external/arxiv-1001.2933v1.pdf`，121 页，1,115,963 字节） | v1 全文（grep） | E1「γ = k/n」与 E2「just greater than 1/3」在 v1 已逐字存在 ⇒ 不是 v4 修版引入，而是作者笔误；v1 只有 121 页，故页码不与 v4 逐页对应，只用于文字比对 |
| 4 | arXiv:0802.0039（https://arxiv.org/abs/0802.0039；H. Murakami《An Introduction to the Volume Conjecture…》） | §3.1 p.11–12；§4.1 p.19–20 | 八字结 A 多项式（其 ℓ=l、m=m_W²）；三叶结单值 x=[[m^{1/2},1],[0,m^{−1/2}]]、y=[[m^{1/2},0],[−d,m^{−1/2}]]，λ 的本征值 −m^{−3}（与本文 l=−m_W^{−6} 在 m=m_W² 下一致） |
| 5 | arXiv:0711.2836（https://arxiv.org/abs/0711.2836；Hikami–Murakami《Colored Jones Polynomials With Polynomial Growth》） | Theorem 1.1、Theorem 1.2 | 八字结 J_N(E;e^{ξ/N})∼Γ(1/3)(3ξ)^{2/3}N^{2/3}；环面纽结 T(a,b) 在 q=e^{2πi/(abN)} 时 ∼const·N^{1/2}；对应本文 (5.51) 与 (5.24) 的标度 |
| 6 | nLab「analytically continued Chern-Simons theory」（https://ncatlab.org/nlab/show/analytically+continued+Chern-Simons+theory，2026-11-23 抓取，HTTP 200） | Idea 节 | 复群联络、取值 ℂ/ℤ；Wilson 线是纽结不变量的解析延拓；与本文的复化 W 定位一致（归一差 2π） |
| 7 | nLab「volume conjecture」（https://ncatlab.org/nlab/show/volume+conjecture，2026-11-23 抓取，HTTP 200） | Idea 节 (1) | lim (2π/N)log\|V_N(K;e^{2πi/N})\|=vol(K)；与本文 (5.62) 的 exp(nV/2π) 只差把 N 与 n 对齐，2π 因子一致 |
| 8 | 库内旧卡 `datasets/csw/concept/cs-action`、`datasets/ggl13/deriv/complex-cs-gradient-flow`、`datasets/ggl13/concept/complex-cs-morse-function` | 各卡 formulas/key_points | CS 作用量 1/4π 与 2/3；复 CS 的 Morse 函数与 t=tan(α/2) 的四维方程；与本文 (2.1)、(4.8)–(4.9) 对齐 |

### 勘误

本稿发现 **2 条 high**、0 条 low（另有 1 条只影响记法的说明，未入 errata）：

- **E1（high，p118 §5.3.5 第 1 段）** 原写「where as usual γ = k/n」，应为「γ = n/k」。依据1：本篇 p087 §5 开头明确定义「fixed ratio γ = n/k」，p102 也用「1/6 < n/k < 5/6」；依据2：p099 (5.27) 的 ln m=iπγ 与 p082 (4.35) 的 m=exp(iπ(n−1)/k) 只在 γ=n/k 下相容，p100 (5.28) 的 γ=±(1/6+p) 也是按 n/k 推出。v1 同误，排除版本差异。影响卡：`ggl10/concept/colored-jones-semiclassical`、`ggl10/deriv/figure-eight-volume-cycle`；状态 fixed（卡片按 n/k 写，并挂 corrections）。
- **E2（high，p119 §5.3.5 第 3 段）** 原写「The integration cycle for γ just greater than 1/3 is therefore」，应为「just greater than 2/3」。依据1：同段开头「To continue past γ = 2/3, we use eqn. (3.57)」，跳变点明确是 2/3；依据2：紧接下段「with Re γ > 2/3, exponential growth comes from the terms J″_{+,−1/2}−J″_{+,1/2}」，且 (5.66) 是在 γ→2/3 下方取的 cycle。影响卡：`ggl10/deriv/figure-eight-volume-cycle`；状态 fixed。

排除项（曾疑、后撤回）：

- **p116 的「m²+m⁻²+1 > 1」** 初看像应为「>0」（因为 §5.3.3 的 case (2) 用 >0）。但 p116 该段只讨论「一对 SL(2,C) 平坦联络被复共轭交换」的某个子区，>1 是更强的充分条件，不是与后文冲突的等式；按 §9.2「只有一处冲突」的标准不足以判笔误，撤回，不列 errata。
- **p094 的 (5.11)–(5.12)** 直接符号计算给出：印出的 C 满足 C⁻¹xC=diag(m,m⁻¹)、C⁻¹yC=(5.12)，而 CxC⁻¹=[[m,2],[0,m⁻¹]]≠diag。也就是说文中「C·C⁻¹」的写法与 C 的定义差一个逆。这只影响记法，bc<0 的判据与所有结论不变；没有任何卡片引用 (5.11)–(5.12)，故不列 errata，只在「不懂」第 1 条留记录。
- **(2.35)/(2.36) 的 η-不变量相位** 只找到本篇与 [48] 两处，且 [48] 未逐字核对；符号若反，k′+h′=k+h 仍成立（只改 h 的符号约定），不影响卡片，未列 errata。

## 不懂

1. **(5.11)–(5.12) 的共轭约定**：我算出 C⁻¹xC=diag(m,m⁻¹)、C⁻¹yC 恰好是 (5.12)，而文中写的是 C·C⁻¹；CxC⁻¹ 的对角元是 (m, 2; 0, m⁻¹)，不是 diag。因为只用 bc<0，结论不变；但我没有找到作者用 C⁻¹ 的第二种定义，故不敢判为笔误，只记在这里。
2. **(5.11)/(5.12) 的 bc<0 判据在复 m 时的含义**：b=(m−m⁻¹)⁻²、c=1−m²−m⁻²；|m|=1 时 b<0、c>0 给出 (5.14)。但 m²+m⁻² 为复数时「bc<0」不是全序判断，原文只写「can be conjugated iff bc<0」，我没有把它严格化成复数的条件。
3. **p116 的 w=1**：原文说「It can be shown by integrating (4.42) that w=1」。我只核了它使 W(A±)=±3π 与 (5.59) 的 π mod 2π 相容，没有独立做那个积分；若 w 取别的整数，(5.68) 的相位会变，但体积指数不变。
4. **(5.68) 的相位 e^{±iπk}**：我按 w=±1/2 与 CS 不变量的复提升理解，但没有从 (5.67) 的系数逐项复算相位；特别是 e^{−iπk} 与 e^{iπk} 哪个对应 J″_{+,−1/2} 没有独立验算。
5. **§4.1.1 的指标论证**：L₀=d_A+d_A* 的指标 −χ(X)dim H 与边界项相消，我只读了结论，没有逐项核 Dirac 指标的边界贡献（APS 条件那一段）。
6. **(2.35)/(2.36) 的测度比较**：本文只引 [48] 的 η-不变量计算，我没有独立验证相位 exp(i(h−h′)W) 的符号；这会影响 k′+h′=k+h 中 h 的符号约定。
7. **§5.2.4 的「每条 Stokes 曲线与实轴相交」**：我核对了 (5.37)/(5.38) 的代数化简，但没有证明每条分支都真的与实轴相交（原文给的是论证思路，不是逐分支证明）。
