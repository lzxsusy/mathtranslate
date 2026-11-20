# 交付说明（README）—— Wolpert《Mirzakhani 体积递推与 Witten–Kontsevich 定理》中文译注本

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

## 1. 底本信息与页码映射

| 项 | 值 |
|---|---|
| 作者 | Scott A. Wolpert（加州大学戴维斯分校数学系） |
| 标题 | *Lectures and notes: Mirzakhani's volume recursion and approach for the Witten-Kontsevich theorem on moduli tautological intersection numbers* |
| 出处 | arXiv:1108.0174v1 [math.DG]，2011 年 7 月 31 日 |
| 场合 | 2011 年 Park City 数学研究所（PCMI）研究生暑期学校 "Riemann 曲面模空间" 短课程讲稿 |
| 页数 | 38 页（US Letter，612×792 pt） |
| 图 | 11 幅（全部为矢量图，0 张位图） |
| 表 | 0 张 |
| 编号公式 | **4 条**（(1)(2)(3) 在 p.18，(4) 在 p.21；其余公式底本不编号） |
| 编号陈述 | **15 条**（Theorem 1–15，其中编号 12 为 Definition） |
| 参考文献 | 33 条（作者-年份标签，英文原貌转录，未翻译；实测清点，非初估的 35） |
| 页码偏移 | **0**：PDF 页号 = 印刷页码 |

**页码映射**：正文 pp.1–35（其中 pp.1 为标题页，pp.2–3 §1 引言，pp.4–7 §2 组织纲要，pp.8–35 §3 讲义）；
参考文献 pp.35–38（"References" 标题在 p.35 页中）。译本的每个原文页起始处都有 `% [原文 p.N]` 标记
（源码中可见，编译后不显示）。

## 2. 结构清单

- 标题页 / 短课程说明 / 译者说明 / 目录 — 原文 p.1
- §1 引言（含"第一篇论文简述""第二篇论文简述"与两条不编号定理）— 原文 pp.2–3
- §2 组织纲要与阅读指南 — 原文 pp.4–7
- §3 讲义 — 原文 pp.8–35
  - 一般背景（Teichmüller 空间、映射类群、Fenchel–Nielsen 坐标、WP 辛几何）
  - 体积结果概述（定理 1–5，图 2–5）
  - Zograf 猜想、长度恒等式（定理 6–8，图 6–7）
  - 余体积公式与辛约化（定理 9–10）
  - S¹ 主丛、特征类、辛约化（命题 11、定义 12、定理 13，图 8–11）
  - ψ 类、Witten 配分函数、Virasoro 约束（定理 14–15）
- 参考文献 — 原文 pp.35–38

**编号陈述对照表**（本译本的验收锚点）：

| 编号 | 类型 | 原文页 | 内容 |
|---|---|---|---|
| 1 | 定理 | p.9 | Fenchel–Nielsen 坐标 |
| 2 | 定理 | p.10 | dℓ∧dτ 公式 |
| 3 | 定理 | p.12 | 2π²κ₁ = ω |
| 4 | 定理 | p.13 | WP 体积多项式 |
| 5 | 定理 | p.13 | 体积多项式首项系数的递推（dilaton/string 方程） |
| 6 | 定理 | p.18 | 长度恒等式（β-袖口裤子求和） |
| 7 | 定理 | p.18 | 简单测地线测度为零（Birman–Series） |
| 8 | 定理 | p.18 | Mirzakhani–Tan–Wong–Zhang 长度恒等式 |
| 9 | 定理 | p.21 | 余体积公式 |
| 10 | 定理 | p.25 | 带尖点边界体积与紧致体积的关系 |
| 11 | 命题 | p.28 | 辛约化 |
| 12 | 定义 | p.28 | S¹ 主丛与联络 |
| 13 | 定理 | p.29 | 模空间上唯一闭 2-形式 Ω |
| 14 | 定理 | p.33 | Witten–Kontsevich 猜想（Virasoro 约束） |
| 15 | 定理 | p.34 | Virasoro 约束的具体形式 |

**图对照表**：图 1 p.1、图 2 p.8、图 3 p.9、图 4 p.11、图 5 p.12、图 6 p.17、图 7 p.17、
图 8 p.26、图 9 p.26、图 10 p.28、图 11 p.29。全部由原文矢量图以 500 dpi 裁取，裁后逐幅目视复核
（完整、无相邻正文/图注残影、不含原编号残迹）。

## 3. 编译方法（含本机字体与路径注意事项）

```powershell
# 在 src/ 目录（含 main.tex / preamble.tex / chunks/）下：
powershell -ExecutionPolicy Bypass -File build.ps1
# 脚本会：找 TeX bin → 把 src 与 figures 镜像到 ASCII 可写目录 → lualatex ×3 → 解析 main.log → 拷回 main.pdf
```

本机（Windows + TeX Live 2026）三条硬约束与对策：

1. **LuaLaTeX 在非 ASCII 路径下无法写 `.log`**（报 `I can't write on file main.log`，极具误导性）：
   `build.ps1` 因此把源码镜像到 `<本地路径>`
   这类纯 ASCII 目录再编译，最后把 `main.pdf` 拷回 `src/`。
2. **`TMP`/`TEMP` 必须显式指向可写目录**，否则 xdvipdfmx/字体缓存可能崩；`build.ps1` 已设。
3. **中文由 ctex 自动取系统字体**（不需要 fontconfig、不需要手写 `\setCJKmainfont`）。
   换到无中文系统字体的机器时，可用 `\usepackage[UTF8,fontset=fandol]{ctex}` 走 Fandol 字体。

引擎：**LuaLaTeX**（TeX Live 2026）；三遍编译（目录/交叉引用）。
`figures/` 需与 `main.tex` 同级（`\graphicspath` 已同时指向 `figures/` 与 `../figures/`）。

## 4. 译校体例

- **正文照原文翻译**，不放宽、不删节、不合并段落；原文的列表、缩进层级、粗体行内小标题（译作 `\para{…}`）逐项保留。
- **公式**：底本只有 4 条编号公式（(1)(2)(3) 在 p.18，(4) 在 p.21），译本用 plain TeX 的 `\eqno{(N)}`
  手工复刻编号（不用 LaTeX 自动编号，以保证与原文一致）；其余公式底本不编号，译本同样不编号
  （`\[ … \]`、`equation*`、`align*`）。正文对公式的引用一律用原文的纯文本形式
  （如"formula (1)"、"[Mir07a, 公式 (5.1)]"）。
- **编号陈述**：手工复刻原文编号 1–15（环境 `thm`/`prop`/`defn`）。原文 p.3 上两条不带编号的
  "Theorem." 段用 `thmplain` 排版，**不给编号**（原文亦无编号）。
- **文献引用**：纯文本 `[Mir07a]`、`[Mir07a, 定理 6.3 与 6.4]`，不用 `\cite`。
- **批注**：全部写在 LaTeX 注释 `% [Tutor Note: …]` 中，**不进入排版**；全文汇总见《译注汇总》。
  批注只写三类内容：可验证的易错点、作者省略的论证、原文笔误（附正确形式与判断依据）。
- **术语**：以 `work/glossary.tsv` 冻结；人名与标准缩写（Teichmüller、Weil–Petersson、tautological、
  Fenchel–Nielsen、Dehn、Witten–Kontsevich、Mirzakhani、MCG、WP）保留英文原貌。tautological 一词
  学术上尚无统一中译，译本保留英文并首次出现时括注。
- **参考文献**：英文原貌逐条转录，不翻译（学术惯例），由脚本/人工核对缺号重号。

## 5. 原文笔误登记表

> 原则：正文照原样翻译；笔误只在批注中指出并给出正确形式。凡登记项均已用 500+ dpi 裁图复核。

| # | 原文页 | 原文 | 说明 / 正确形式 |
|---|---|---|---|
| 1 | p.6 | "The elliptic stack 2." | 数字 `2` 存疑（1000 dpi 裁图确认字形确为 2，疑原稿丢失记号，如 $\overline{\mathcal M}_{1,1}$ 的写法）；照录。 |
| 2 | p.10 | $\omega=2\omega_{WP}$ **Kähler** | 公式后紧跟一个孤立斜体词 Kähler（疑为"即 Kähler 形式"的残留）；照录，批注说明应读作"$\omega=2\omega_{WP}$，即 Kähler 形式"。 |
| 3 | p.10--11 | "Each **strata** is symplectic." | strata 是复数，应为 "Each **stratum** is symplectic."；照录。 |
| 4 | p.12 | "-The pullback to $\overline{\mathcal M}$ by a puncture section $s$ … canonical psi class $\psi$.-" | 句首、句末各有一个孤立连字符（疑为待改写标记残留）；照录，批注给出句读。 |
| 5 | p.19 | "geodesic $\delta_\beta$ emanating at one end" | $\delta_\beta$ 全篇仅此一见；该裤子只有 $\beta,\alpha,\lambda$ 三条边界，同句四边形四边为 $\tilde\alpha,\tilde\delta_\alpha,\tilde\beta_\alpha,\tilde\sigma$，缺 $\delta_\alpha$ 无法闭合。应为 $\delta_\alpha$。 |
| 6 | p.24 | "while the second has degree $i+j+2$" | 该处指标只有 $j,k$（$i$ 全文未出现于此处）；按 $t\to\infty$ 的渐近行为（$\log$--$\log$ 斜率 $=2(j+k+2)$）应为 $j+k+2$。 |
| 7 | p.25 | "to define a symplectic **from** $\omega_{\mathcal T_g(L)}$" | from 应为 form（"辛形式"）。 |
| 8 | p.25 | "lengths $L_1,\ldots,,L_n$" | 多一个逗号；照录。 |
| 9 | p.26 | 短正合列第三项印作 $\mathrm{MCG}(R)$ | 与 p.21 定理 9 证明中的同型列（第三项为 $\prod_{R(\beta)\ \text{分支}}\mathrm{MCG}(R')$）对照，此处为简记；照录 + 批注说明精确含义。 |
| 10 | p.28 | "For $\widehat{\mathcal T}_{g,n}/(S^1)^n\approx \mathcal T_g(L)$, then …" | 条件句缺主句（原文如此）；译文按"若……，则……"处理。 |
| 11 | p.29 | "$\sinh w(\alpha)\sinh\ell_\alpha/2=1$" | 未加括号，标准写法 $\sinh w(\alpha)\cdot\sinh(\ell_\alpha/2)=1$；照录。 |
| 12 | p.35 | "$\widetilde\psi_k=\pi^*\psi_k,+D_k$" | $\psi_k$ 与 $+D_k$ 之间多一个逗号；照录 + 批注。 |

**两处"记号不统一"（非笔误，照原文保留，批注已说明）**：

| # | 位置 | 现象 |
|---|---|---|
| N1 | p.31 vs p.32 | 同一记号 $\mathcal M$ 的上划线不统一：p.31 定义式、p.34 两处积分、p.35 全段都写 $\overline{\mathcal M}$，而 p.31 正文 "moduli spaces $\mathcal M_{g,n}$" 与 p.32 的 $\int_{\mathcal M_{1,1}}$ 确实不带 overline。译本逐处按页图保留。 |
| N2 | p.20 vs p.32 / p.15 | 体积归一化两套约定：$V(L)=\pi^2/6+L^2/24$（不含椭圆对合 $1/2$ 因子）与 $V_{1,1}=\pi^2/12+L^2/48$（含）。原文两页各自明说，非笔误。 |

## 6. 统计

| 指标 | 数值 |
|---|---|
| 底本页数 | 38 |
| 译本 PDF 页数 | 32 |
| 编号陈述 | 15（定理 13 / 命题 1 / 定义 1） |
| 图 | 11（全部由原文矢量图 500 dpi 位图化） |
| 编号公式 | 4（(1)–(3) p.18，(4) p.21；其余公式不编号） |
| 参考文献 | 33 条 |
| 批注（Tutor Note） | 64 条 |
| 编译 | LuaLaTeX ×3：file:line 错误 0 / `!` 错误 0 / Undefined 0 / Missing character 0 / Overfull 0 |
| 分工 | Lead（pp.1–3）+ 6 位译者（tr-01 pp.8–13、tr-02 pp.14–19、tr-03 pp.20–25、tr-04 pp.26–30、tr-05 pp.31–35、tr-06 pp.4–7 与参考文献），共 7 人 |
| 交叉校对 | 6 轮互检（每人校一块别人的）+ Lead 校 tr-06，共 7 份报告，全部"必须改"已落改 |

## 7. 已知偏差与限制

1. **公式编号极稀疏**：底本只有 4 条编号公式，其余公式不编号；原文引用他人文献的公式编号
   （如 (5.1)、(6.2)）作为文本保留，无法在译本内交叉链接。
2. **参考文献为自动+人工混合转录**：保留英文原貌，未逐条与出版方数据库核对；变音符号与连字符
   （如 `Birkh\"auser`、`Ast\'erisque`）已按页图核对，但不排除个别排版细节差异。
3. **图为矢量图 500 dpi 位图化**：文本/标注可缩放但有分辨率上限；原文图内的英文标注未翻译（保持原貌）。
4. **批注是译者判断**：批注中的补充论证与"原文笔误"标注属译校者意见，正文仍照原样呈现，读者可自行裁断。
5. **术语**：tautological 等无统一中译的词保留英文；如需完全本土化，可据 `glossary.tsv` 全文替换。
6. **中文强调不可见**：原文的斜体强调（如 *The basic point:*、*main gaps*）在源码中以 `\emph{}` 忠实保留，
   英文斜体正常显示；但 ctex 对汉字没有斜体字形，故**中文强调在成品中看不出变化**。这是 ctex 的字体限制，
   不是漏译；若需中文强调，可改为楷体或着重号。
7. **图的浮动位置**：图为 `figure[htbp]` 浮动体，位置由 LaTeX 决定，与原文插图位置不完全一致
   （图注编号与内容完全对应）。
8. **未做**：原文图内文字的汉化、索引（底本无索引）、逐条参考文献与出版方数据库校勘。

## 8. 版权声明

底本为 arXiv 公开预印本（arXiv:1108.0174v1，math.DG），版权归作者 Scott A. Wolpert 所有。
本译本为学习/研究用中文译注，不含原文 PDF 的整页复制；图的位图化用于学术评论与说明。
若权利人认为不妥，请联系译者删除。译文与批注的著作权归译者，按本库 [`LICENSE`](../../../LICENSE) 的 CC BY 4.0 分享（署名即可）；底本权利不受影响。
