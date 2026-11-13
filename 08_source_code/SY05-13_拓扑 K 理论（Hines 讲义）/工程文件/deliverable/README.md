# 《拓扑 K 理论》中文译注本 —— 交付说明

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；本项目语料默认不用于训练，要用须先整库审计并经 Lead 书面批准。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 底本：Robert Hines, *Topological K-theory*, 2016-12-15（公开讲义，10 页）。
> 本译注本由 DeepSeek Harness 多智能体流程完成：1 名 Lead + 3 名译者分块翻译（Lead 兼译 pp.1–2 与参考文献），
> 随后 3 名校对者交叉互检；全部改单由 Lead 以 exact-match patch 脚本落改（命中数校验），
> 最后真编译 3 遍并回读成品 PDF 逐项验收。

## 1. 底本信息与页码映射

| 项目 | 实测值 |
|---|---|
| 标题 | Topological K-theory |
| 作者 | Robert Hines |
| 日期 | 2016 年 12 月 15 日 |
| 来源 | 作者公开讲义（expository notes），未标注 arXiv 编号 |
| 原 PDF | `拓扑K理论讲义\pdfs\01_Hines_Topological_K-Theory_2016.pdf`，270,835 bytes |
| 原 PDF 页数 | **10 页**（Letter，612×792 pt；pdfTeX-1.40.16） |
| **页码对应** | **PDF 页号 = 原文印刷页码（偏移 0）** |
| 编号定理类 | 定义 1–8；命题 1–3；引理 1；**定理 1–9**（共 21 条） |
| 编号公式 | **0 条**（实测：右栏 `(x.y)` 形态的 tag 扫描为空） |
| 图 / 表 | **0 图 / 0 表**（p2、p3、p5、p6、p7 出现的矢量元素全是分段函数花括号、矩阵与交换图，均用 LaTeX 重排） |
| 脚注 / 习题 | 0 条 / 0 道 |
| 参考文献 | p.10，共 **5 条**（[Bott] [VBKT] [AGP] [K] [May]），保留英文原貌 |

译文在每一起始原文页处有注释 `% [原文 p.N]`（N = PDF 页号 = 印刷页号），便于对照。
成品为 A4 纸（原文 Letter），故成品页数（12 页）与原文页数（10 页）不同；成品 PDF 中 **第 4–12 页** 为正文，
第 1–3 页依次是封面、译者说明、目录（罗马数字页码区）。

## 2. 结构清单

```
封面
译者说明
目录
1  向量丛与 K(X)                    （原文 pp.1–4 上）
2  向量丛的分类                      （原文 pp.4 下–7）
3  Bott 周期性与作为广义上同调理论的 K 理论   （原文 pp.7–8）
   3.1 另一版本的 Bott 周期性        （原文 p.8）
4  K 理论的一个应用                  （原文 p.8）
5  K 理论的其他版本                  （原文 p.9）
   5.1 实 K 理论                     （原文 p.9）
   5.2 代数 K 理论                   （原文 p.9）
参考文献                            （原文 p.10，英文原貌，5 条）
```

成品 12 页中的章节起始页（PDF 页码）：§1 → p4；§2 → p7；§3 → p9；§3.1 → p11；§4 → p11；
§5 / §5.1 / §5.2 / 参考文献 → p12。

## 3. 编译方法

```powershell
powershell -ExecutionPolicy Bypass -File build.ps1
```

- 引擎：**LuaLaTeX ×3**（`ctex` 自动取系统中文字体，无需 fontconfig / `\setCJKmainfont`）。
- 本机实测两条硬约束（同《学术PDF翻译_标准作业手册 v2》M2）：**LuaTeX 不能写非 ASCII 路径与 Desktop**，
  故 `build.ps1` 先把 `src/*.tex`、`src/chunks/` 镜像到 ASCII 可写目录
  （默认 `<本地路径>`），把 `TMP`/`TEMP` 指向可写目录，
  编译成功后把 `main.pdf` 拷回 `src\main.pdf`，并打印 log 统计。
- 依赖宏包：`ctex`、`amsmath/amssymb/amsthm/mathtools`、`bm`、`graphicx`、`geometry`、`xcolor`、
  `enumitem`、`booktabs`、`array`、`multicol`、`fancyhdr`、`caption`、`tikz`（含 `cd` 库）、`hyperref`。
- 本次真编译结果（见 `compile.log`）：**LuaLaTeX ×3，0 error / 0 undefined / 0 missing character / 0 overfull**。

## 4. 译校体例

- **正文**：忠实逐段翻译，不增不减；原文笔误照译，仅在 `% [Tutor Note: …]` 批注中指出并给出正确形式。
- **定理类**：原文的编号定义/命题/引理/定理一律**手工给号**（`\begin{defn}{3}` 等），号数与原文逐条对应，
  不缺、不重、不跳、不重排。中文版正文用**直立体**（原文斜体是西文排版习惯，中文不用斜体）。
- **公式**：原文无编号公式，译本亦无（不使用 `\tag`）；全部展示式按 200 dpi 原页图逐符号重排，
  矩阵用 `pmatrix`、分段函数用 `cases`、交换图用 `tikzcd`，**无一处截图**。
- **文献引用**：`[VBKT] 1.6`、`[AGP] 8.4.4.` 等照抄英文方括号，不译键名。
- **参考文献**：保留英文原貌（学术惯例），按原文逐条转录。
- **批注**：`% [Tutor Note: …]` 为译者批注，**不进入排版**，全部汇总于随附《译注汇总.md》。
  内容为可验证的易错点、补出的省略论证、原文笔误与判断依据、术语首现英文原词。本次共 **37 条**。
- **术语**：`work/glossary.tsv` 冻结（73 条），全稿统一（如：vector bundle → 向量丛、clutching function → 粘合函数、
  Grothendieck group → Grothendieck 群、canonical bundle → 典范丛、splitting principle → 分裂原理、
  Adams operations → Adams 运算、suspension → 悬挂、external product → 外积）。
- **符号**：`GL` 统一用正体 `\GL`（原文混用斜体，属西文习惯）；约化 $K$ 与 $\widetilde E$ 统一用宽波浪号
  `\widetilde`（与原文 PDF 的 CMEX10 宽 accent 一致）。

## 5. 原文笔误登记表

以下疑点均由译者/校对者**先用 500–1500 dpi 裁图复核原文**（并借助 PDF 字形层判定斜体/上下标），确认后登记；
正文一律照原文翻译，批注中给出正确形式。

| 序号 | 页 | 原文（疑） | 说明 / 正确形式 |
|---|---|---|---|
| 1 | p.1 定义 1 | "there is a an open cover" | 冠词重复，应为 "an open cover" |
| 2 | p.1 定义 1 | 第一条展示式作 $\phi$（无下标） | 后文用 $\phi_i^{-1}$、$\phi_j\circ\phi_i^{-1}$，此处应作 $\phi_i$（漏下标） |
| 3 | p.2 命题 1 证明 | $(a,b)+(c,d)=(a+b,c+d)$ | 应为 $(a+c,b+d)$；按原式运算在等价类上不良定义（反例见批注） |
| 4 | p.2 命题 1 | "homorphism"（两处） | → homomorphism |
| 5 | p.2 命题 1 | "constructin" | → construction |
| 6 | p.2 命题 1 | "constuction" | → construction |
| 7 | p.2 | "These operation give" | → These operations give |
| 8 | p.2 定义 2 | "isomophism" | → isomorphism |
| 9 | p.3 命题 2 证明 | 分段式落点 $X\times I\times\C^n\to B$ | 该映射是 $E$ 的平凡化，落点应为 $E$ |
| 10 | p.3 命题 2 证明 | $h_0(x,t,v)$ | 局部平凡化作用在平凡化坐标上，应读作 $h_0^{-1}(x,t,v)$ |
| 11 | p.4 | "mulitiplication" | → multiplication |
| 12 | p.4 | "the cluthing for" | → clutching |
| 13 | p.4 定义 3 | "orthogoal complement" | → orthogonal complement |
| 14 | p.4 定义 3 | 两个展示式作 $v\in p$（小写） | 应为 $v\in P$（$P$ 为 $n$-平面） |
| 15 | p.4 末式 | 端点给出 $-\mathrm{diag}(z^2,1)=-f(z)$ | 与 $f(z)$ 差左乘 $-I$；$-I$ 在 $\GL_2(\C)$ 中与 $I$ 同伦，结论 $f\simeq g$ 仍成立（批注补算） |
| 16 | p.5 命题 3 | "ismophism" | → isomorphism |
| 17 | p.5 命题 3 证明 | $g=\tilde f\circ\pi$ | 与图示复合顺序相反，应为 $\pi\circ\tilde f$（再与左端同构复合） |
| 18 | p.5 | 4-胞腔例子给的是 $3\times5$／$3\times6$ 矩阵 | 正文说「$n\times(N-n)$ 矩阵」；例子实为含主元列的 $n\times N$ 阶梯形，应理解为「删去主元列后剩 $n\times(N-n)$ 个自由元」 |
| 19 | p.7 定义 6 | "presepectrum" | → prespectrum（pres 后多插一个 e） |
| 20 | p.7 定理 2 | "cohmology"（原文跨行断作 cohmol-/ogy） | → cohomology（同段下一句即写作 cohomology，可互证） |
| 21 | p.7 定理 2 | "additve" | → additive |
| 22 | p.7 定理 2 | "Representability of cohomology theories are mediated" | 主谓不一致，应为 "is mediated" |
| 23 | p.7 定理 1 证明 | $d([E_1\oplus E'_2])$ | $d$ 只定义在 $\Vect_\C(X)$ 上，此处的延拓应记作 $\bar d$ |
| 24 | p.7 定义 5 | 同伦不变性写作 $f^*=g^*:\widetilde E^*(X)\to\widetilde E^*(Y)$ | 上同调反变，方向应为 $\widetilde E^*(Y)\to\widetilde E^*(X)$ |
| 25 | p.8 定理 3 | cases 第二行 $\pi_i(BU)=0$（$i\ge1$） | 应为 $\pi_i(BU)$；否则与同页 $\tilde K(S^2)\cong\Z$ 矛盾 |
| 26 | p.9 定理 7 | $f^*P(E)$ 分裂为线丛之和 | 应为 $f^*E$（$P(E)$ 是射影丛空间，只有 $E$ 能分裂） |
| 27 | p.9 定理 7 | $K(F(E))$ | 应为 $K(P(E))$；$F(E)$ 全文仅此一处 |
| 28 | p.10 参考文献 | "Raol Bott" | 通行拼写 Raoul Bott |
| 29 | p.10 参考文献 | "Homotpical" | → Homotopical（Aguilar–Gitler–Prieto 原书名） |

**非笔误（已澄清，避免误登记）**：p.7 "proofs definitely omitted" 是作者口语（文字层的 `defi-/nitely` 只是 fi 连字丢失）；
p.9 "briefly" 亦为文字层连字丢失，印刷无误。文字层还会把 `fi` 连字抽成乱码、希腊字母与花体丢失，
因此**所有公式均以 200 dpi 页图为唯一真值**逐符号重排。

## 6. 统计

| 项目 | 数值 |
|---|---|
| 原 PDF 页数 | 10（Letter） |
| 成品 PDF 页数 | **12**（A4；封面 + 译者说明 + 目录 + 正文 9 页） |
| 编号定理类 | **21**：定义 8 + 命题 3 + 引理 1 + 定理 9 |
| 编号公式 | **0**（原文亦 0；`check.py`：TAG 禁用扫描 0） |
| 图 / 表 / 脚注 / 习题 | 0 / 0 / 0 / 0 |
| 参考文献 | 5 条（英文原貌） |
| 展示式 | 46 条（全部 LaTeX 重排，含 10 个 `pmatrix`、2 组 `cases`、2 个 `tikzcd` 交换图，**无一处截图**） |
| Tutor Note 批注 | **37 条**（见《译注汇总.md》；按文件：c01a 4、tr01a 13、tr02a 10、tr03a 4、tr03b 5、c-refs 1） |
| 原文笔误登记 | **29 项**（见 §5）+ 记号不统一若干 |
| 分工 | Lead pp.1–2 + p.10；tr-01 pp.3–5；tr-02 pp.6–7；tr-03 pp.8–9 |
| 交叉校对 | **3 轮**（rv-1 校 pp.8–9、rv-2 校 pp.3–5、rv-3 校 pp.1–2 与 pp.6–7 并做全书一致性检查），报告见 `work/review/*.md`；共 **7 条「必须改」全部落改**，另有 9 条「可选改」按取舍落改 |
| 编译 | LuaLaTeX ×3：**0 error / 0 undefined / 0 missing character / 0 overfull** |
| 成品回读 | 21/21 条编号定理类、9 个章节标题、全部字体子集嵌入 —— 均通过（`verify_pdf.py`） |

## 7. 已知偏差与限制

1. **中文定理正文为直立体**：原文用斜体（西文排版惯例），中文无对等的斜体语义，故按中文习惯排直立体；
   定理编号、标题层级与原文一一对应。
2. **页码体系**：成品 A4、原文 Letter，页数不同（12 vs 10）。原文位置一律以源码 `% [原文 p.N]` 注释标记，
   成品页码与原文页码**不逐页对应**。
3. **参考文献**：5 条按原文逐条**手工转录**，保留英文原貌，未逐条校对（条目本身简短，风险低）；
   其中两处原文拼写已登记在 §5。
4. **图示**：原文 0 图 0 表；p2/p5 的交换图用 Ti*k*Z 重画，箭头样式、标签位置与原图**略有差异**（不改变内容）。
5. **原文笔误照译**：29 项笔误一律按原样排，仅在批注中给出正确形式；不做"顺手修正"。
6. **符号规范化**：`GL` 统一正体（原文混用斜体）；约化 $K$ 与 $\widetilde E$ 统一宽波浪号（与原文 accent 一致）。
7. **术语**：个别译名可能有更常见的替代（如 clutching function → 粘合函数，也有「过渡函数」的译法），
   全稿以 `work/glossary.tsv` 为准。
8. **未做**：原文无目录、无习题、无附录，译本亦无；未增补任何原文没有的内容。

## 8. 版权声明

原文 © Robert Hines, 2016，为作者公开提供的讲义（expository notes）。
本译注本为个人学习研究之用，**不用于商业用途**；原文版权归原作者所有，如需引用或再分发请以原文为准。
