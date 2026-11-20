# 拓扑量子场论与几何朗兰兹对应（中文译注本）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

Kevin Setter, *Topological Quantum Field Theory and the Geometric Langlands Correspondence*
（California Institute of Technology 博士学位论文，2013；2012 年 8 月 24 日答辩）的中文 LaTeX 译注本。

---

## 1. 底本信息与页码映射

| 项 | 内容 |
|---|---|
| 作者 | Kevin Setter |
| 标题 | Topological Quantum Field Theory and the Geometric Langlands Correspondence |
| 学位/机构 | Ph.D. Thesis, California Institute of Technology, Pasadena, California, 2013 |
| 导师 | Anton Kapustin（致谢中提及；论文核心思想来自其工作 [1]） |
| 原 PDF | `Setter_thesis.pdf`，**169 页**，pdfTeX 生成（2012-09-19） |
| 正文范围 | 印刷 **pp.1–154**（9 章 + 附录 A–D）；印刷 **pp.155–159** 为参考文献（64 条，本译本保留英文原貌） |
| **页码映射** | **PDF 页号 = 印刷页码 + 10**（PDF p.11 页脚为 “1”，PDF p.169 页脚为 “159”） |

本译本正文每页内容前用注释标注原文页码：`% [原文 p.N]`，可与原 PDF 逐页对照。

## 2. 结构清单

| 原文 | 中文 | 印刷页 |
|---|---|---|
| Chapter 1 Introduction and overview | 第 1 章 引言与概述 | 1–8 |
| Chapter 2 Duality of four-dimensional gauge theories | 第 2 章 四维规范理论的对偶 | 9–19 |
| Chapter 3 Vafa-Witten theory as a gauged 4d A-model | 第 3 章 Vafa–Witten 理论作为带规范场的 4d A-模型 | 20–32 |
| Chapter 4 Topological field theory, categories, and 2-categories | 第 4 章 拓扑场论、范畴与 2-范畴 | 33–41 |
| Chapter 5 Compactifications of Vafa-Witten and GL-twisted theories on a circle | 第 5 章 Vafa–Witten 与 GL-扭转理论在圆上的紧化 | 42–58 |
| Chapter 6 Surface operators of 4d TFTs | 第 6 章 4d TFT 的面算子 | 59–83 |
| Chapter 7 Modified A-model | 第 7 章 修正 A-模型 | 84–99 |
| Chapter 8 Vafa-Witten theory compactified on a genus g ≥ 2 Riemann surface | 第 8 章 Vafa–Witten 理论在亏格 $g\ge2$ 黎曼面上的紧化 | 100–106 |
| Chapter 9 Defects of two-dimensional sigma models | 第 9 章 二维 σ-模型的缺陷 | 107–121 |
| Appendix A 2d TFTs | 附录 A 2d TFT | 122–131 |
| Appendix B 3d TFTs | 附录 B 3d TFT | 132–141 |
| Appendix C Associated fiber bundles and equivariant cohomology | 附录 C 相伴纤维丛与等变上同调 | 142–149 |
| Appendix D Proofs of propositions in Chapter 9 | 附录 D 第 9 章命题的证明 | 150–154 |
| Bibliography | 参考文献（英文原貌） | 155–159 |

## 3. 编译方法

环境：**XeLaTeX**（MiKTeX 或 TeX Live 均可，需 `ctex` 宏包），编译 **3 遍**。

```bat
:: 在交付目录双击运行
build_xelatex.bat
```

或手动：

```bash
cd src
xelatex -interaction=nonstopmode -file-line-error main.tex   # ×3
```

**字体注意事项**：`src/preamble.tex` 用绝对路径调用 Windows 自带字体
（`C:/Windows/Fonts/simsun.ttc`、`simhei.ttf`、`simkai.ttf`、`simfang.ttf`），不依赖 fontconfig。
在 Linux/macOS 上编译时，请把 `\setCJKmainfont` 等四行改为本机的宋/黑/楷字体
（例如 `Noto Serif CJK SC` / `Noto Sans CJK SC`），或删去 `fontset=none` 改用 ctex 自带的 `fontset=ubuntu`。

**若 PDF 为 0 字节或出现 `xdvipdfmx` 崩溃**：把 `TMP`/`TEMP` 指向可写目录再编译
（本机实测 `xdvipdfmx` 拿不到临时目录时会直接崩溃，与 TeX 本身无关）。

**编译实测结果（交付时）**：见 `compile.log`；判据：`file:line` 错误 0、`!` 错误 0、
`Undefined control sequence` 0、`Missing character` 0、`main.pdf` 页数合理。

## 4. 译校体例

1. **正文忠实翻译**：不删、不增、不“顺手修正”。原文笔误照原文排印，只在批注中指出并给正确形式。
2. **公式编号与原文一一对应**：全部用 `\tag{原文编号}`（共 57 条：1.1–1.3, 2.1–2.4, 3.1–3.11,
   5.1–5.8, 7.1–7.9, 8.1–8.3, 9.1–9.3, B.1–B.14, D.1–D.2）。原文中没有编号的公式一律不编号。
3. **术语**：以 `glossary.tsv` 为准；人名、机构名、模型名（Kapustin、Witten、Gukov、Hitchin、Vafa–Witten、
   Rozansky–Witten、Nahm 等）保留原文；术语首现处批注给英文原词。
4. **图**：原文 10 张图（图 1.1、2.1、4.1–4.7、6.1）按原文页面图像 **400 dpi** 截取，图注由译者译出；
   没有图的地方绝不造图（原文无表格，本译本也不造表）。
5. **定理类环境**：编号一律手工照抄原文——第 9 章的定义 1–7、命题 1–10；附录 D 证的是命题 1、3、6、7、8；
   附录 C 有 4 处不编号的「定理」块。原文**没有**编号定理（“Theorem 3.3.8” 是引用文献 [21] 的编号）。
6. **批注（Tutor Note）**：所有译者补充的解释以 `% [Tutor Note: ...]` 形式写在源码里，**不进入排版**；
   全量索引见 `译注汇总.md`。批注内容限定为：可验证的易错点 / 补出的省略论证 / 原文笔误（附判断依据）/ 术语首现。
7. **参考文献**：保留英文原貌，仅做编码层面整理（把 PDF 文字层的连字符断行、连字 ﬁ、变音符号还原），不改条目内容。
8. **公式引用**一律写纯文本“式 (2.3)”（手工 `\tag` 无法自动交叉引用）。

## 5. 原文笔误登记表

（均为原文如此；本译本正文照原文排印，只在批注中给出判断依据与正确形式。页码为印刷页码。）

| # | 位置 | 原文 | 应为 / 说明 | 判断依据 |
|---|---|---|---|---|
| 1 | p.9 起通篇 | `t’Hooft` | 通行写法 `'t Hooft` | 作者习惯性误排；译文照排 + 首现批注 |
| 2 | p.12 | “with respect to which **which**…”／“at the **the** quantum level” | 重复 which / the | 冗余词 |
| 3 | p.15 | DW 扭转 `4 → (2,1)⊗(1,1)⊗(1,1)` | 应为直和 `(2,1)⊕(1,1)⊕(1,1)` | 量纲 2·1·1=2≠4；相邻 VW/GL 行均为 4 维 |
| 4 | p.19 | “which fact will **allows** one to write down” | allow | 情态动词后用原形 |
| 5 | p.26 | “…a field Φ: M→E, which is no longer merely a map into **M**” | into **X** | E 是以 X 为纤维的相伴丛 $P\times_GX$ 的全空间，Φ 是其截面 |
| 6 | p.27 | $d_A\Phi\in\Omega^1(\Sigma,\Phi^*VE)$ | 底流形应记 **M** | 同段下文写在 $U^{(\alpha)}\subset M$ 上 |
| 7 | p.36 | “还能融合壁上插入了局部算子的壁（图 4.4）” | 图 **4.5** | 该句讲 2-态射融合，图 4.4 画的是 1-态射；下句即引图 4.5 |
| 8 | p.38 | “an object **on** $\mathbb{W}$ by an object of $\mathbb{V}$” | an object **of** $\mathbb{W}$ | 同段后文一律作 “an object of $\mathbb{W}$” |
| 9 | p.42 / p.49 / p.50 | “will be turn out to be”／“After the integrating out”／“under the the 3d rotation subgroup” | 多 be / the / the | 语法冗余 |
| 10 | p.46 式 (5.1) | 第三行 $\delta\varsigma=\rho$ | 应为 $\delta_Q\varsigma=\rho$ | 同组其余各行均带 $\delta_Q$ |
| 11 | p.50 式 (5.6) 与 p.31 式 (3.9) | $-\bar\tau/(4\pi\ii)=+\ii\bar\tau/4\pi$ 与 $-\ii\tau/4\pi$ | 二者在 $\theta=0$ 时一致、$\theta$ 项反号 | 属约定差异，非笔误；批注说明 |
| 12 | p.61 | “must vanish, **The** Neumann…” | 应为 “must vanish. The Neumann…” | 逗号后接大写，应断句 |
| 13 | p.62 | “but it easy to see” | “it **is** easy to see” | 漏 is |
| 14 | p.64 | “turns out to endowed with” | “turns out to **be** endowed” | 漏 be |
| 15 | p.68 | “consider a complex **manifolds** $X$” | manifold | 单复数 |
| 16 | p.70 | “allows us to **identity** $S^1$…” | identify | 拼写 |
| 17 | p.81 | “**it** category of branes” | its | 拼写 |
| 18 | p.88 式 (7.5) | $\dd H=-\iota_V\Omega$ | 应为 $+\iota_V\Omega$ | 同页分量式 $\partial_JH=\Omega_{IJ}V^I$ 与 p.90 的 BRST 抵消均要求正号 |
| 19 | p.94 | “with respect to **the the** symplectic form” | 重复冠词 | 语法 |
| 20 | p.97 | “closed Riemann surface $F_{\mathbb C}$” | $\Sigma_{\mathbb C}$ | 全纯图册长在底曲面上；后句说复共轭作用在纤维 $\mathbb C^n$ |
| 21 | p.102 式 (8.2) | 第二式 $D_3\varphi^3+D_4\varphi^4=0$ | 应为下标 $\varphi_3,\varphi_4$ | (8.1) 中 $B_{13},B_{14}$ 均为下标，且第二式与第三式同属 $D_C^*\varphi=0$ |
| 22 | p.112 式 (9.1) | Neumann 条件 $G(u,w)=F(v,w)$ | 应为 $G(v,w)=F(u,w)$ | 同页推导取 $w=u$ 得 $G(u,v)=G(v,u)=F(u,u)$；p.117 完整清单与 (9.1) 变分 $\delta S_D=\int[-G(v,w)+F(u,w)]$ |
| 23 | p.113 | “the preceding theorem” / “A pair … **are** said” | 实指命题 2；应为 “is said” | 上文只有定义与命题 1、2；主谓一致 |
| 24 | p.117 | “setting half … to zero **［缺 on］** the defect line D” | to zero **on** the defect line | 缺介词 |
| 25 | p.122 | $\chi=\Omega^2(\Sigma,\mathrm{ad}P)$ | 应为 $\chi\in\Omega^2$ | 前两行均用 $\in$ |
| 26 | p.122 | $\delta_Q\bar\sigma=\eta$ | 应为 $\beta$ | 本页费米子清单只有 $\beta,\lambda,\chi$；由 $\delta_Q^2=2\ii\delta_\sigma$ 对 β 反推 |
| 27 | p.124 | “The field **σ** has ghost number 2” | 应为 **φ** | 本段讲 B-模型，σ 属 A-型一侧；下句自注 “σ 与 φ 等同” |
| 28 | p.127 | “the 2d gauge **theory theory** on a circle” | 重复 theory | 排印 |
| 29 | p.135 | “replacing … by **a a** Lie group-valued scalar” | 重复 a | 排印 |
| 30 | p.136 / p.141 | RW 曲率项 $\Omega_{ij}R^{j}{}_{kl\bar m}\chi^i\wedge\chi^j\wedge\chi^k\wedge\chi^i\wedge\eta^{\bar m}$ | 应为 $\chi^i\wedge\chi^k\wedge\chi^l\wedge\eta^{\bar m}$ | 3-流形上 4 个 1-形式外积恒为零；$\Omega_{ij}$ 反对称使 $\Omega_{ij}\chi^i\wedge\chi^j=0$；两处互证 |
| 31 | p.146 / p.147 | “**principle** bundle” | principal bundle | 拼写 |
| 32 | p.148 | 定理块陈述 “Proposition 2.2 of [18]” | 原文如此（引用 [18] 的命题 2.2） | 该块为不编号定理 + 三条性质 |
| 33 | p.149 | “In case $k=m$ and $S=M$” | 应为 $k=2m$ | p.142 已声明 $M$ 是 $2m$ 维；$S=M$ 时须 $k=\dim M=2m$ |
| 34 | p.151 | “Theorem 1 tells us…” | 原文**悬空引用**（全文无 Theorem 1） | 第 9 章只有定义 1–7 与命题 1–10；作者或指第 9 章命题 1 或附录 D 命题 (1)，未改 |
| 35 | p.151 | 命题 (3) 证明 “$(u,(\widetilde G^{-1}\widetilde F)\tilde u)$ is an allowed pair” | 第一分量应为 $\tilde u$ | 上一句刚给出 $(\tilde u,\tilde v)$ 的判据 |
| 36 | p.151 | $G(v,v_0)=F(v,v_0)=0$ | 第二项应为 $F(u,v_0)$ | 本证明 p.152 用 $F(u,w)=G(v,w)$；结论 $v\in TY$ 需 $G(v,v_0)=0$ |
| 37 | p.153 | “**Kosczul** formula”／“Since $s,t\in\Gamma(\mathcal{R}_+)$. we can…” | Koszul；句号应为逗号 | 拼写/标点 |
| 38 | p.97 | “(see Theorem 3.3.8 of [21])” | 文献 [21] 的定理编号（非本文定理） | 全文无本论文编号定理；[21] = Katz–Liu |
| 39 | p.143 起（附录 C） | 4 处不编号 `Theorem.` 块 | 原文如此（非编号定理） | 排版为 “Theorem.” + 陈述；p.148 一条陈述即 “[18] 的命题 2.2” |

> 说明：上表只收录**影响阅读或可能引起误解**的原文问题；纯排印（破折号、空格、标点种类）未逐一列入。
> 所有对应位置的 `% [Tutor Note: ...]` 批注可在 `译注汇总.md` 中检索。

## 6. 统计（实测）

- 原文 **169 页** / 正文 **154 页**（9 章 + 附录 A–D）/ 参考文献 **64** 条
- 编号公式 **57** 条（与原文一一对应，`tools/check.py` 校验：MISSING = EXTRA = DUPLICATE = 无）
- 图 **10** 张（400 dpi 原图截取）；表 **0** 张
- 中译本 PDF：**118 页**（A4，11pt）
- 源码：**41 个片段文件，4636 行** LaTeX
- **Tutor Note：281 条**（索引见 `译注汇总.md`）
- 覆盖检查：原文 pp.1–154 每页均有 `% [原文 p.N]` 标注（`tools/check_pages.py` 全部 OK）

## 7. 已知偏差与限制

1. 本译本按 A4 版式重新排版，**页码与原文不一一对应**（每页有 `% [原文 p.N]` 标注，可逐页对照）；
   行宽、断行、浮动体位置不可能逐一复刻。
2. 原文的方框公式（如 (1.1)–(1.3)）用带边框的 LaTeX 排版复现，框内断行位置与原图可能略有差异。
3. 原文 10 张图为 400 dpi 位图截取（原图为矢量），放大到很高倍率时会有轻微像素化。
4. 参考文献只做编码层面整理，未逐条与原刊核对。
5. 译文为学习与研究用途，**非官方译本**；原文版权归原作者所有。
6. 原文个别笔误/存疑处只在批注中指出，正文照排；批注内容由译者负责，读者应以原文为准。
7. 原文若干**不编号的粗体小标题**（如 p.20、§B.4、第 5 章 p.45/47/49 等处）在本译本中统一排为
   `\para`（行内粗体小标题）或 `\subsection*`（独立粗体行，不进目录），两种排法与原文 12pt 标题的字号
   不完全一致，但文字内容与位置忠实原文，且不影响编号体系。
8. 正文引用公式时，「式 (N.M)」与裸 `(N.M)` 两种写法并存（均为纯文本、无 `\ref`），不影响读者定位；
   其中 `(2.55)/(2.56)` 是引用文献 [3]（Vafa–Witten）的方程编号，非本论文编号。
9. 编译日志有 4 处 `Overfull \hbox`（最宽约 44.7pt，均出现在含长公式的行），为可接受的排版溢出；
   `Missing character` = 0、`Undefined control sequence` = 0。

## 8. 交付清单

```
deliverable/
├── Setter_thesis_中文译注本.pdf   成品（可编译交付）
├── src/                          全部 LaTeX 源码（main.tex / preamble.tex / chunks/ / figures/）
├── tools/                        素材制备、静态检查、编译、验证、打包脚本
├── build_xelatex.bat             一键编译
├── compile.log                   真实编译日志（0 error 凭证）
├── 译注汇总.md                    全部 Tutor Note 索引
├── probe.md                      环境探测 + 底本尽调实测记录
├── tags.txt                      57 条编号公式清单（唯一验收依据）
├── glossary.tsv                  术语冻结表
├── STYLE_GUIDE.md                工程规范（写作前必读）
└── README.md                     本文件
```

## 9. 版权声明

原文 © 2013 Kevin Setter，保留所有权利。本中文译注本为学习与研究用途译本，
不用于任何商业目的；译文、批注与排版由本译本译者完成，原文版权归原作者所有。
如权利人认为本译本不妥，请联系删除。
