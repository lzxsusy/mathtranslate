# 《广义对称性讲义》中文译注本 —— 交付说明

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；本项目语料默认不用于训练，要用须先整库审计并经 Lead 书面批准。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 底本：L. Bhardwaj, L. E. Bottini, L. Fraser-Taliente, L. Gladden, D. S. W. Gould, A. Platschorre,
> H. Tillim, *Lectures on Generalized Symmetries*, arXiv:2307.07547v2 [hep-th], 8 Sep 2023。
> 本译注本由 DeepSeek Harness 多智能体流程完成：1 名 Lead + 8 名译者分块翻译，随后 8 轮交叉校对，
> 全部批注与校改均由 Lead 以 exact-match patch 脚本落改（命中数校验），最后真编译 3 遍并回读成品 PDF。

## 1. 底本信息与页码映射

| 项目 | 实测值 |
|---|---|
| 标题 | Lectures on Generalized Symmetries |
| 作者 | Lakshya Bhardwaj, Lea E. Bottini, Ludovic Fraser-Taliente, Liam Gladden, Dewi S. W. Gould, Arthur Platschorre, Hannah Tillim（据 L. Bhardwaj 所授课程整理） |
| arXiv | 2307.07547v2，2023-09-08 |
| 原 PDF 页数 | **150 页**（Letter，612×792 pt） |
| 正文范围 | pp.1–138 |
| 致谢 / 参考文献 | p.139 / pp.139–150（221 条） |
| **页码对应** | **PDF 页号 = 原文印刷页码（偏移 0）** |
| 图 / 表 | 位图 0 张；矢量图 28 张（Figure 1–28）；表 1 个（Table 1，p.47） |
| 编号公式 | **745 条**：§2: 2.1–2.109；§3: 3.1–3.221；§4: 4.1–4.267；§5: 5.1–5.94；§6: 6.1–6.54 |
| 彩色方框 | 蓝色 Statement ×14；绿色 Definition ×14；橙色 Example ×43；粉色带标题注释框约 10 处；无标题框若干 |
| 章节结构 | 6 节（见 §2） |

译文在每一原文页起始处有注释 `% [原文 p.N]`（N = PDF 页号 = 印刷页号），便于对照原文。
成品 PDF 采用 A4 纸（原文为 Letter），故成品页数与原文页数不同；页码映射以 `% [原文 p.N]` 注释为准。

## 2. 结构清单

```
摘要
目录
1  引言
2  高阶形式对称性导论
   2.1 0-形式对称性
   2.2 高阶形式对称性
       2.2.1 一般性质
       2.2.2 p-形式对称性的作用
   2.3 离散（高阶形式）规范理论
3  规范理论的高阶形式对称性
   3.1 延展算符的屏蔽
   3.2 阿贝尔规范理论
       3.2.1 含单个物质场的 Maxwell 理论
       3.2.2 含多个物质场的 Maxwell 理论
       3.2.3 多个阿贝尔规范场
       3.2.4 纳入磁物质
       3.2.5 纳入双荷物质
   3.3 非阿贝尔规范理论
       3.3.1 纯 SU(2) Yang–Mills 理论
       3.3.2 纯 SO(3) Yang–Mills 理论
       3.3.3 一般规范群的纯 Yang–Mills 理论
       3.3.4 包含物质场
       3.3.5 多个规范群因子
   3.4 四维规范理论中的离散 theta 角
       3.4.1 纯 SO(3)₋ Yang–Mills 理论
       3.4.2 一般的非阿贝尔四维规范理论
4  高阶形式对称性的性质
   4.1 背景场
   4.2 't Hooft 反常与 SPT 相
       4.2.1 't Hooft 反常基础
       4.2.2 SPT 相
       4.2.3 反常理论与反常多项式
       4.2.4 非阿贝尔规范理论的混合 't Hooft 反常
   4.3 规范化（gauging）
       4.3.1 定义
       4.3.2 离散挠率
       4.3.3 规范化后得到的对偶对称性
       4.3.4 规范化交换扭曲扇区与带电扇区
       4.3.5 规范化交换混合 't Hooft 反常与群扩张
   4.4 自发对称性破缺与禁闭
       4.4.1 一般概念
       4.4.2 例：具有 su(2) 规范代数的 4d N=1 SYM 理论
   4.5 对称性拓扑场论（Symmetry TFTs）
5  高阶群对称性
   5.1 连续高阶群对称性
   5.2 离散高阶群对称性
       5.2.1 动机：群扩张
       5.2.2 一般结构
       5.2.3 与混合 't Hooft 反常的关系
   5.3 混合连续-离散 2-群对称性
       5.3.1 0-形式对称性的全局形式
       5.3.2 Bockstein 2-群对称性
6  高阶形式对称性与弦论
   6.1 来自几何工程的高阶形式对称性
   6.2 全息中的广义对称性
致谢
参考文献（英文原貌，221 条）
```

## 3. 编译方法

本机（Windows + TeX Live 2026）实测两条硬约束：

1. **LuaLaTeX 不能在非 ASCII 路径（中文目录）下写 `.log`**，报 `I can't write on file main.log`（报错极具误导性）；
2. **子进程（lualatex.exe）不能写 Desktop**，同样报 `I can't write on file`。

因此 `build.ps1` 把 `src/*.tex`、`src/chunks/`、`figures/` **镜像**到 ASCII 可写目录
（默认 `<本地路径>`），把 `TMP`/`TEMP` 指向可写目录，
再用 `lualatex` 编译三遍，成功后把 `main.pdf` 拷回 `src/main.pdf`，并打印 log 统计
（file:line 错误 / `!` 错误 / Undefined / Missing character / Overfull）。

一键编译（在 `src/` 或任意目录都可，脚本按自身位置定位工作区）：

```powershell
powershell -ExecutionPolicy Bypass -File build.ps1
```

关键环境：LuaLaTeX + `ctex`（自动取系统字体，不需要 fontconfig，不需要手写 `\setCJKmainfont`）；
`tcolorbox`（breakable 方框）、`amsmath/mathtools`、`graphicx`、`booktabs`、`multicol`、`fancyhdr`、`hyperref`。

本次真编译结果（见 `compile.log`）：**3 遍 × LuaLaTeX，0 error / 0 undefined / 0 missing character / 0 overfull**。

## 4. 译校体例

- **正文**：忠实逐段翻译，不增不减；原文笔误照译，仅在 `% [Tutor Note: ...]` 批注中指出并给出正确形式。
- **公式**：全部 745 条编号公式用 `\tag{X.Y}` 复刻原文编号（不缺、不重、不跳、不重排、不自造）；
  原文无编号公式一律 `\[...\]`/`equation*`，不加编号；正文引用公式写纯文本「式 (3.13)」，不用 `\ref`/`\eqref`。
- **章节**：`\section`/`\subsection`/`\subsubsection` 自动编号，与原文 1–6 及各小节一致。
- **方框**：蓝色 Statement → `statementbox`；绿色 Definition → `definitionbox`；橙色 Example → `examplebox`；
  粉色带标题注释框 → `notebox`；无标题细边框 → `noteboxplain`。框内编号照抄原文，跨页断框合并为一个。
- **图注/表题**：`\figtitle{N}{…}` / `\tabtitle{N}{…}` 手工编号；图 1–28 为原图 400 dpi 截取（图内文字保留英文原样），图注照译。
- **参考文献**：保留英文原貌（学术惯例），由脚本从原 PDF 文字层自动转录（见 §7）。
- **批注**：`% [Tutor Note: ...]` 为译者批注，**不进入排版**，全部汇总于《译注汇总.md》；
  内容包括可验证的易错点、补出的省略论证、原文笔误与判断依据、术语首现英文原词。
- **术语**：`work/glossary.tsv` 冻结（约 120 条），全库统一（如：gauging → 规范化、twisted sector → 扭曲扇区、
  cocycle → 上闭链、obstruction → 障碍、bifundamental → 双基础、Abel/abelian → 阿贝尔/非阿贝尔，
  $D_p$ 等价类群用无衬线 `\mathsf{D}`，群名 SU/SO/U/Spin 一律正体宏）。

## 5. 原文笔误登记表

以下疑点均由译者/校对者**先裁 500–1200 dpi 原图复核**，确认后登记；正文一律照原文翻译，批注中给出正确形式。

| 序号 | 页 | 原文（疑） | 说明 / 正确形式 |
|---|---|---|---|
| 1 | p.31 | "as they they have" | 重复 `they` |
| 2 | p.32 (3.30) | $\delta b_{d-2}$ | 按余微分理解次数不匹配；应读作余边界算子 |
| 3 | p.34 (3.43) | 平凡群写作 $=0$ | (3.27) 用 $=1$，$\gcd(2,1)=1$，两处均指平凡群，记号不一致 |
| 4 | p.40 | "the two non-trivial equivalence classes" | non-trivial 疑为笔误（指两个类中的平凡类） |
| 5 | p.43 图 11 图注 | "the the identity" | 重复 `the` |
| 6 | p.43 图 10 图注 vs 正文 | $D_2$（图注）vs $D^2$（散文句） | 同一圆盘混用上/下标；译文各处照原文保留 |
| 7 | p.52 (3.167)–(3.169) | "a $2p\times(m+p)$ matrix $Y=(Z\|Q)$" | $Z$ 为 $p\times p$、$Q$ 为 $p\times m$，故 $Y$ 应为 $p\times(m+p)$；min 上限亦应为 $p$ |
| 8 | p.53 (3.175) | $\mathrm{SNF}(Y)=\begin{pmatrix}0&4&0\\0&0&1\end{pmatrix}$ | 对角元错位排版（按 SNF 应为 diag(1,4)）；原文如此 |
| 9 | p.54 | "arises inside $W_jH_\phi$ the OPE of $W_j$ and $H_\phi$" | 语序错乱，应读作 "arises in the OPE of $W_j$ and $H_\phi$" |
| 10 | p.59 | "similar to the theory considered in (3.11)" | 应为「例 3.11」而非公式 (3.11) |
| 11 | p.66 | "The boundary of $s_i$" | 应为 $\widehat{s}_i$（对偶三角剖分的 $i$-单形） |
| 12 | p.67 | "a counter-term, which is a function of $B_p$" | 应为 $B_{p+1}$（与 (4.34) 的同变性一致） |
| 13 | p.70 (4.47) 后 | "in the presence of $B^e_p$" | 应为 $B^e_{p+1}$（与 (4.44)(4.48) 一致） |
| 14 | p.72 (4.56) | $g_1,\cdots,g_{i+2},g_{i+3}\cdots,g_{p+1}$ | 原文写法正确（是 $g_{i+2},\dots,g_{p+1}$ 的展开），**非笔误**（已裁图复核，批注说明） |
| 15 | p.95 | "as explained right before example (4.8)"；"statement (4.6)" | 括号为误加，分别指例 4.8、陈述 4.6 |
| 16 | p.96 | "then the operator $\mathcal{O}_p$ does not exist in the IR" | 应为 $\mathcal{O}'_p$（(4.203) 的主语） |
| 17 | p.100 小节标题 | "Gauge Algbebra" | 应为 "Gauge Algebra"（笔误） |
| 18 | p.117 | "is described a cohomology class" | 缺 `by` |
| 19 | p.121 | "The argument is the same the one taking (4.194) to (4.197)" | 缺 `as`（the same as the one） |
| 20 | p.123 | "irreducible representations of $R_i^f$ of $F$" | 词序错乱（应读作 $R_i^f$ of $F$） |
| 21 | p.138 (6.46) | 第二、三行的 $\omega_2$ 印成 $w_2$ | 字形与 (6.45) 的 $\omega$ 不同，判为笔误；译文照印并注明 |
| 22 | p.137 (6.43) | 两处 $\mathbb{CP}^3$ 的 P 字形不一致（一处黑板体） | 照原文保留并注明 |

（另有若干处**记号不统一**而非笔误，已在批注说明：$\phi_g$ vs $\phi(g)$（p.19 vs p.17）、
杯积 $\cup_\eta$ 与普通 $\cup$ 混用、式 (5.19)/(5.34) 参数列表末项逗号不一致等。）

## 6. 统计

| 项目 | 数值 |
|---|---|
| 原 PDF 页数 | 150（正文 138 + 文献 12） |
| 成品 PDF 页数 | **117**（A4；含标题、摘要、目录、6 节正文、28 图、表 1、致谢、参考文献） |
| 编号公式 | **745**（`check.py`：MISSING/EXTRA/DUPLICATE 全空；`verify_pdf.py`：成品文本中 745/745 全部出现） |
| 图 / 表 | 28 / 1 |
| 参考文献 | 221 条（自动转录，0 缺号 0 重号） |
| Tutor Note 批注 | **162 条**（见《译注汇总.md》） |
| 原文笔误登记 | 22 项（见 §5）+ 记号不一致若干 |
| 分工 | Lead pp.1–12；tr-01 13–28；tr-02 29–44；tr-03 45–60；tr-04 61–76；tr-05 77–92；tr-06 93–108；tr-07 109–124；tr-08 125–138；致谢/参考文献由 Lead 处理 |
| 交叉校对 | 8 轮互检（A 校 B 环形），报告见 `work/review/*.md`；共 26 条「必须改」，25 条已 exact-match 落改，1 条（p.92→93 跨页句归属）经 Lead 裁决按现状接受（无重复、无缺口） |
| 编译 | LuaLaTeX ×3：0 error / 0 undefined / 0 missing character / 0 overfull |

## 7. 已知偏差与限制

1. **参考文献自动转录**：221 条由脚本从 PDF 文字层自动转录，未逐条人工校对；原文标题中的数学符号在文字层中被拍平
   （如 $C^2/\mathbb{Z}_p$ 记作 C2/Zp），行尾连字符偶有丢失（如 `non-Abelian` → `nonAbelian`），仅作检索用。
2. **脚注编号**：LaTeX 自动编号；原文约 11 个脚注，跨块处译文脚注号与原文不保证逐号一致（内容均已翻译）。
3. **图**：图 1–28 为原件 400 dpi 截取的位图（原图为矢量），图内标签保留英文原样；图幅按各图原始长宽比设置。
4. **排版页面**：成品用 A4，原文为 Letter，故成品页数与原文不同；原文页码通过 `% [原文 p.N]` 注释与页边界对齐。
5. **方框排版**：原文彩色方框（tcolorbox 风格）按 5 类环境近似复刻，标题条颜色与原文略有差异；跨页断开的方框合并为一个。
6. **原文无习题、无附录**（已实测），译本亦无。
7. **行内粗体小标题**：原文的 "**Screening.**" 等译为 `\para{…}`（独立成段粗体小标题），与原文的行内粗体在断行上略有不同。
8. **跨文件环境**：原文 p.124→125 的「例 5.3」方框跨块，源码中 `\begin{examplebox}` 在 `tr07c.tex` 末尾、`\end{examplebox}` 在
   `tr08a.tex` 开头；这是全工程唯一的跨文件环境（编译顺序固定为 tr07→tr08，`main.tex` 中按序注入，已实测可编译）。
   单独编译某一分片时需注意这一点。
9. **术语**：个别译名可能有更常见的替代（如 coupling→耦合、normalization→归一化等按常规处理）；
   全书统一以 `work/glossary.tsv` 为准。

## 8. 版权声明

原文 © Lakshya Bhardwaj, Lea E. Bottini, Ludovic Fraser-Taliente, Liam Gladden, Dewi S. W. Gould,
Arthur Platschorre, Hannah Tillim，以 arXiv 非排他性分发许可发布于 arXiv:2307.07547v2。
本译注本为个人学习研究之用，**不用于商业用途**；原文版权归原作者所有，
如需引用或再分发请以 arXiv:2307.07547v2 原文为准。
