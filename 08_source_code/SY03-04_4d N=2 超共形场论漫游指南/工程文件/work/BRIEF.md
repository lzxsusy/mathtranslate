# BRIEF —— 分工、边界与接续点

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 为准：语料 / 轨迹 / 会话 CC BY 4.0，明确欢迎用于训练与蒸馏（译文与工程文档 CC BY-NC-SA 4.0）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 项目根：`<本地路径>`
> 底本：M. Akhond, G. Arias-Tamargo, A. Mininno, H.-Y. Sun, Z. Sun, Y. Wang, F. Xu,
> *The Hitchhiker's Guide to 4d N=2 Superconformal Field Theories*, arXiv:2112.14764v3,
> 2022-08-21，**122 页**（Letter 612×792 pt）。
> **PDF 页号 = 印刷页码 + 1**（PDF p.3 = 印刷 p.2，正文从 §1 开始）。

## 0. 底本尽调实测（禁止臆测，均已实测）

| 检查项 | 实测值 |
|---|---|
| 总页数 | 122（PDF）；印刷页码 1–121 |
| 标题 / 作者 | 见上；PDF metadata 作者含 © 符号，以首页作者行为准 |
| 编号公式 | **164 条**：§2: 2.1–2.53（53）｜§3: 3.1–3.42（42）｜§4: 4.1–4.33（33）｜§5: 5.1–5.36（36）；**§1、§6 无编号公式** |
| 公式提取核对 | 164/164，重复 0，缺号 0（`work\tags.txt`、`work\tags_bypage.txt`） |
| 图 | **15 幅**（全为矢量图，0 位图）：F1 p8｜F2 p19｜F3 p27｜F4 p29｜F5 p38｜F6 p42｜F7 p54｜F8 p58｜F9 p62｜F10 p63｜F11 p64｜F12 p65｜F13 p66｜F14 p72｜F15 p74 |
| 表 | **8 张**：T1 p14｜T2 p30｜T3 p47｜T4 p70｜T5 p75｜T6 p89｜T7 p92｜T8 p94 |
| 定义 / 例 / 习题 | 定义 2.1–2.5（酒红左边框）；例 3.1、4.1–4.9、5.1–5.3（蓝左边框）；习题 2.1–2.4、3.1–3.2、4.1–4.3、5.1（细黑全框） |
| 附录 | **无附录**。§6 结论与开放问题（印刷 p.92 起，PDF p.94 中段）→ 致谢（PDF p.97 上部）→ 参考文献（PDF p.97 起至 p.122） |
| 目录 | PDF p.2–3，与正文起始页一致（已核对） |

## 1. 版式与素材

- 页图（公式唯一真值）：`work\pages\pNNN.png`（200 dpi，`p001`–`p122`）
- 逐页文字层：`work\split\pNNN.txt`（首行 `% PDF p.N (printed p.M)`）；整本：`work\full.txt`
- 编号公式清单：`work\tags.txt`（tag⇥页）、`work\tags_bypage.txt`（页: tags）
- 图：`work\figures\fig1.png … fig15.png`（450 dpi，已裁好、已目视复核；**不要重新裁**）
- 裁图工具：`& $py "$ROOT\work\tools\crop.py" <PDF页号> <x0> <y0> <x1> <y1> <out.png> [dpi]`
  （页面 612×792 pt；`$py = <本地路径>`）
- 术语表：`work\glossary.tsv`

## 2. 分工表（严格按此写，不越界）

| 块 | 文件 | PDF 页 | 印刷页 | **tag 区间** | 内容 |
|---|---|---|---|---|---|
| Lead | `c00`,`c01` | 1–8 | 0–7 | — | 标题页/译者说明/目录/§1 引言/图 1 |
| tr-01 | `tr01a,b,c` | **9–19** | 8–18 | **2.1–2.27** | §2 起、2.1、2.2；表 1、图 2 |
| tr-02 | `tr02a,b,c` | **20–31** | 19–30 | **2.28–2.53** | 2.3、2.4、2.5、2.6、§3 标题与引子；图 3、图 4、表 2 |
| tr-03 | `tr03a,b,c` | **32–40** | 31–39 | **3.1–3.27** | §3 续、3.1、3.2 起；图 5 |
| tr-04 | `tr04a,b,c` | **41–50** | 40–49 | **3.28–3.42、4.1** | §3 续（3.3–3.5）、§4 标题与 4.1、4.2 起；图 6、表 3 |
| tr-05 | `tr05a,b,c` | **51–63** | 50–62 | **4.2–4.22** | 4.2 续、4.3、4.4、4.5；图 7、图 8、图 9、图 10 |
| tr-06 | `tr06a,b,c` | **64–75** | 63–74 | **4.23–4.33** | 4.6、4.7、4.8、4.8.1、4.8.2、4.8.3；图 11–15、表 4、表 5 |
| tr-07 | `tr07a,b,c` | **76–85** | 75–84 | **5.1–5.27** | §5 标题与 5.1、5.2、5.3 |
| tr-08 | `tr08a,b,c` | **86–97** | 85–96 | **5.28–5.36** | 5.4、5.4.1、5.4.2、§6 结论（PDF p.94 中段起）、致谢（p.97）；表 6、表 7、表 8 |

> 参考文献（PDF p.97 起）由 Lead 脚本自动转录，**不由任何译者承担**。

## 3. 标题归属（谁写哪个标题，严格按表；编号手工给定 `\SEC`/`\SUB`/`\SUBSUB`）

| 标题 | 原文位置（印刷页 → PDF 页） | 归属 |
|---|---|---|
| §1 Introduction（`\SEC{1}{引言}`） | p.2 → p.3 | Lead |
| §2 Basics of 4d N=2 Supersymmetry | p.8 → p.9 | **tr-01** |
| 2.1 N=2 superconformal Symmetry and Representations | p.8 → p.9 | tr-01 |
| 2.2 4d N=2 Multiplets and General N=2 Lagrangians | p.14 → p.15 | tr-01 |
| 2.3 Supersymmetric Vacuum Moduli Space | p.18 → p.19 | **tr-01**（PDF p.19 是 tr-01 最后一页）|
| 2.4 Holomorphy and N=2 RG Flows | p.22 → p.23 | tr-02 |
| 2.5 Lagrangians for N=2 SCFTs | p.24 → p.25 | tr-02 |
| 2.6 Anomalies of N=2 SCFTs | p.26 → p.27 | tr-02 |
| §3 Coulomb Branch Effective Theory and Argyres-Douglas Points | p.30 → p.31 | **tr-02**（PDF p.31 是 tr-02 最后一页）|
| 3.1 Electric-Magnetic Duality | p.33 → p.34 | tr-03 |
| 3.2 Prepotential and Special Geometry on Coulomb Branch | p.38 → p.39 | tr-03 |
| 3.3 Seiberg-Witten Solution to Quantum Prepotential | p.41 → p.42 | tr-04 |
| 3.4 Scale-invariant Seiberg-Witten Solutions and Argyres-Douglas Theories | p.43 → p.44 | tr-04 |
| 3.5 SCFT data at the Argyres-Douglas point from a Coulomb Branch EFT | p.45 → p.46 | tr-04 |
| §4 Class S Constructions from Five-branes | p.47 → p.48 | **tr-04** |
| 4.1 A Lightning Review of N=(2,0) Theories | p.47 → p.48 | tr-04 |
| 4.2 Seiberg-Witten Solution from the Abelian N=(2,0) Theory | p.49 → p.50 | **tr-04**（PDF p.50 是 tr-04 最后一页）|
| 4.3 The UV Curve C and Class S Construction | p.50 → p.51 | tr-05 |
| 4.4 Quantum Geometry From Classical Hitchin System | p.52 → p.53 | tr-05 |
| 4.5 Codimension-2 Defects and Punctures on C | p.55 → p.56 | tr-05 |
| 4.6 Examples of N=2 SCFTs in Class S[A_n] | p.64 → p.65 | tr-06 |
| 4.7 A Glimpse of the AGT Correspondence | p.67 → p.68 | tr-06 |
| 4.8 Further Generalizations | p.68 → p.69 | tr-06 |
| 4.8.1 General N=(2,0) Theory | p.68 → p.69 | tr-06 |
| 4.8.2 Irregular (wild) Punctures | p.70 → p.71 | tr-06 |
| 4.8.3 Outer-Automorphism Twist | p.73 → p.74 | tr-06 |
| §5 Geometric Engineering in IIB String Theory | p.75 → p.76 | **tr-07** |
| 5.1 4d N=2 SCFTs From 3-fold Singularities | p.76 → p.77 | tr-07 |
| 5.2 Examples of N=2 SCFTs from (G,G') Singularities | p.82 → p.83 | tr-07 |
| 5.3 Relation with Class S Constructions | p.83 → p.84 | tr-07 |
| 5.4 Further Generalizations | p.85 → p.86 | tr-08 |
| 5.4.1 General Singularities | p.85 → p.86 | tr-08 |
| 5.4.2 F-theory Constructions and S-folds | p.87 → p.88 | tr-08 |
| §6 Conclusion and Open Questions | p.92 → **p.93 页末**（实测更正：标题在 p.93 底部；其后首段跨到 p.94，表 8 是 p.94 页首浮动体，按引用点排在其前）| tr-08 |
| Acknowledgements（`\SEC` 不用，用 `\section*{致谢}`）| p.96 → p.97 | tr-08 |

## 4. 图/表归属（谁写哪张图/表，不要重复、不要漏）

| 图 | PDF 页 | 归属 | 表 | PDF 页 | 归属 |
|---|---|---|---|---|---|
| 图 1 | 8 | Lead | 表 1 | 14 | tr-01 |
| 图 2 | 19 | tr-01 | 表 2 | 30 | tr-02 |
| 图 3 | 27 | tr-02 | 表 3 | 47 | tr-04 |
| 图 4 | 29 | tr-02 | 表 4 | 70 | tr-06 |
| 图 5 | 38 | tr-03 | 表 5 | 75 | tr-06 |
| 图 6 | 42 | tr-04 | 表 6 | 89 | tr-08 |
| 图 7 | 54 | tr-05 | 表 7 | 92 | tr-08 |
| 图 8 | 58 | tr-05 | 表 8 | 94 | tr-08 |
| 图 9 | 62 | tr-05 | | | |
| 图 10 | 63 | tr-05 | | | |
| 图 11 | 64 | tr-06 | | | |
| 图 12 | 65 | tr-06 | | | |
| 图 13 | 66 | tr-06 | | | |
| 图 14 | 72 | tr-06 | | | |
| 图 15 | 74 | tr-06 | | | |

## 5. 边界裁定（「开始者写完」；只列容易出错的接缝）

| 接缝 | 位置（PDF 页） | 裁定 |
|---|---|---|
| Lead → tr-01 | p.8/p.9 | §1 在 p.8 末结束（图 1 在图注后）。tr-01 从 p.9 第一行「§2 标题」开始。 |
| tr-01 → tr-02 | p.19/p.20 | p.19 含 §2.3 标题与正文开头；**tr-01 写完 p.19 上开始的句子**（含跨到 p.20 的半句时写完整）。tr-02 从 p.20 首行续写，**不重译上文**。 |
| tr-02 → tr-03 | p.31/p.32 | p.31 含 §2.6 结尾、**§3 标题与 §3 引子**（tr-02 写）。tr-03 从 p.32 首行续写；3.1 标题在 p.34。 |
| tr-03 → tr-04 | p.40/p.41 | tr-03 写完 p.40 上开始的句子。 |
| tr-04 → tr-05 | p.50/p.51 | §4.2 标题在 p.50（tr-04 写），**4.2 开始的两条公式 (4.2)(4.3) 在 p.51（tr-05）**；tr-05 从 p.51 首行续写 4.2 正文。 |
| tr-05 → tr-06 | p.63/p.64 | tr-05 写完 p.63（含图 10 与图注）。tr-06 从 p.64 首行（图 11 之后正文）开始；4.6 标题在 p.65。 |
| tr-06 → tr-07 | p.75/p.76 | p.75 有表 5（tr-06 写）。§5 标题在 p.76 → tr-07；tr-07 从 p.76 首行开始。 |
| tr-07 → tr-08 | p.85/p.86 | tr-07 写完 p.85（含 5.3 末与跨页半句）。tr-08 从 p.86 首行开始；5.4/5.4.1 标题在 p.86。 |
| tr-08 → 参考文献 | p.97 | tr-08 写到「致谢」结束（p.97 上部 `Acknowledgments` 全段）。参考文献由 Lead 接手。 |

**规则**：块末若是半句，写完整并标 `% [边界] 本句已写完`；块首若是半句，**直接续写**，不补上文。

## 6. 交付与回报

- 文件写到 `<本地路径>`，命名 `trNNa.tex`/`trNNb.tex`/`trNNc.tex`（小写，无空格）。
- **不编译**（Lead 统一编译）；**不改** `preamble.tex`/`main.tex`/`STYLE_GUIDE.md`/别人的 chunks。
- 写完按 STYLE_GUIDE §11 的 5 项回执格式 `send_message` 给 lead。
- 参考：`work\STYLE_GUIDE.md`（硬规范）、`work\glossary.tsv`（术语）、`work\TIMELINE.md`（边界补充裁决）。
