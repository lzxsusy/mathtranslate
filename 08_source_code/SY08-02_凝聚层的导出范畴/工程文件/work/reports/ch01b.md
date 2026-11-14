# ch01b 交稿报告

块名：ch01b　｜　底本：D. O. Orlov, *Derived categories of coherent sheaves and equivalences between them*, Russian Math. Surveys 58:3 (2003) 511–591　｜　书页 = PDF 页 + 510
产出：`src/chunks/ch01b.tex`（341 行）、`work/proposals/ch01b.tsv`（19 条术语提案）、本报告

## 1 内容与结构

范围：原书 p.523 的 `1.2. Derived categories and derived functors` 标题起，到 p.530 上 `CHAPTER 2` 标题之前（即 Proposition 1.3.8 与其后的式 (5) 为止）。共 8 页，两个小节，13 条陈述，1 个章末回顾。

| 位置 | 书页 | 小节 | 内容 |
| --- | --- | --- | --- |
| ch01b.tex:6–42 | 523 | 1.2 | 复形范畴 $\mathbf{C}(\cA)$、$\mathbf{C}^{\pm,b}$、零伦、同伦范畴 $\mathbf{H}(\cA)$、平移函子、标准三角与映射锥 |
| :43–68 | 524 上 | 1.2 | 引理 1.2.1、$\mathbf{H}^{\pm,b}$ 的像、零调复形的定义、引理 1.2.2、拟同构与 Quis、定义 1.2.3 |
| :69–90 | 524 下 | 1.2 | $\mathbf{D}^{\ast}$ 的定义、引理 1.2.4、内射/投射消解的等价 |
| :91–125 | 525 | 1.2 | $\mathbf{R}^nF$、$\mathbf{L}_nF$、右伴随与限制、右适应子范畴、右 $F$-零调、引理 1.2.5、左适应 |
| :126–144 | 525 末–526 | 1.3 | $\cO_X$-Mod、$\Qcoh(X)$、$\coh(X)$ 三范畴 |
| :145–177 | 526–527 | 1.3 | 命题 1.3.1、1.3.2、右伴随 $Q$、命题 1.3.3、推论 1.3.4 |
| :178–250 | 527–528 | 1.3 | $\mathbf{L}f^{*}$ 的构造与延拓、$\otimes$ 与 $\otL$、$\mathbf{R}f_{*}$ |
| :251–295 | 529 | 1.3 | 命题 1.3.5、$\mathcal{H}om$、$\mathbf{R}\mathcal{H}om$、$\mathcal{E}xt$、$\mathbf{L}(gf)^{*}$ 与 $\mathbf{R}(gf)_{*}$ |
| :296–329 | 530 | 1.3 | 命题 1.3.6（式 3）、1.3.7（式 4，含纤维积方块）、1.3.8（式 5） |
| :330–341 | — | 章末 | `\chapterreview{}` |

陈述清单（编号全部手工照抄，未用 `\label`/`\ref`）：

| 编号 | 类型 | 书页 | 行 | 一句话 |
| --- | --- | --- | --- | --- |
| 1.2.1 | 引理 | 524 | 44 | $\mathbf{H}(\cA)$ 以标准三角为特异三角是三角范畴 |
| 1.2.2 | 引理 | 524 | 54 | 零调复形子范畴 $\cN$ 是全三角子范畴 |
| 1.2.3 | 定义 | 524 | 60 | $\mathbf{D}(\cA):=\mathbf{H}(\cA)/\cN=\mathbf{H}(\cA)[\mathrm{Quis}^{-1}]$ |
| 1.2.4 | 引理 | 524 | 69 | $\mathbf{D}^{\ast}\to\mathbf{D}$ 与有界部分给出等价；$\mathbf{H}^{\pm}$ 左/右共尾 |
| 1.2.5 | 引理 | 525 | 116 | 有右适应子范畴时 $\mathbf{R}F$ 在 $\mathbf{D}^{+}$ 上有定义 |
| 1.3.1 | 命题 | 526 | 145 | $\mathbf{D}^{+}(\Qcoh)\to\mathbf{D}^{+}(\cO_X\text{-}\Mod)$ 全忠实，像为拟凝聚上同调 |
| 1.3.2 | 命题 | 526 | 155 | 有限维情形下同断言对无界导出范畴成立 |
| 1.3.3 | 命题 | 527 | 168 | $\mathbf{D}^{-}(\coh)\to\mathbf{D}^{-}(\Qcoh)$ 全忠实 |
| 1.3.4 | 推论 | 527 | 178 | 合并 1.3.1–1.3.3 得 $\mathbf{D}^{b}(\coh)\to\mathbf{D}^{b}(\cO_X\text{-}\Mod)$ 等 |
| 1.3.5 | 命题 | 529 | 252 | 紧合态射下 $\mathbf{R}f_{*}$ 保持凝聚上同调 |
| 1.3.6 | 命题 | 530 | 297 | 投影公式（式 3） |
| 1.3.7 | 命题 | 530 | 306 | 平坦基变换（式 4） |
| 1.3.8 | 命题 | 530 | 319 | 式 (5) 的两步同构，$\cE^{\vee}:=\mathbf{R}\mathcal{H}om(\cE,\cO_X)$ |

页标记 `% [原文 p.523]`…`p.530` 共 9 处（p.525 出现两次：一次在 1.2 末段之前，一次在 1.3 标题之前，因原书 1.3 标题正落在 p.525 页脚）。段序按页图左侧缩进逐段对齐；原书在 display 之后不缩进的续段，本译本仍并入同一段，未额外切分。

## 2 公式与图

**编号公式（3 个，全部逐字符核页图）**

- 式 (3)（:298–302）：$\mathbf{R}f_{*}\cE\otL\cF\xrightarrow{\sim}\mathbf{R}f_{*}(\cE\otL\mathbf{L}f^{*}\cF)$，右端括号内先 $\cE\otL$ 再 $\mathbf{L}f^{*}\cF$；页图为 `\big(` 尺寸的圆括号，已用 `\bigl( \bigr)`。
- 式 (4)（:309–313）：$\mathbf{L}g^{*}\mathbf{R}f_{*}\cE\xrightarrow{\sim}\mathbf{R}f'_{*}\mathbf{L}g'^{*}\cE$；注意 $f'$、$g'$ 的撇号位置（$f'_{*}$ 而非 $f_{*}'$），页图为下标带撇。
- 式 (5)（:320–324）：三个 $\mathbf{R}\mathcal{H}om$ 串成的两步同构，中间箭头与两端箭头同为 $\xrightarrow{\sim}$。

**无编号公式**：32 处 `equation*`，按组为——复形与微分条件（2）、平移函子（1）、标准三角与 $d_{Cf}$ 矩阵（2）、$\mathbf{D}^{\pm,b}\to\mathbf{D}$（1）、$\mathbf{H}^{+}(\cI)\to\mathbf{H}^{+}(\cA)\xrightarrow{Q}\mathbf{D}^{+}(\cA)$ 与投射对偶（2）、$\mathbf{R}^nF$（1）、$\mathbf{H}^{+}(\cR)[\mathrm{Quis}^{-1}]\to\mathbf{D}^{+}(\cA)$（1）、命题 1.3.1–1.3.4 的函子（4，其中推论一并列）、$f^{*}$ 与 $\mathbf{L}f^{*}$（2）、$\mathbf{L}f^{*}$ 有界版（1）、$\otimes$ 与 $\otL$ 共 7 处（7）、$\mathbf{R}f_{*}$ 三处（3）、$\mathcal{H}om^{n}$ 与 $\mathcal{H}om$ 双函子（2）、$\mathbf{R}\mathcal{H}om$（1）、$\mathcal{E}xt^{i}$（1）、$\mathbf{L}(gf)^{*}$（1）、$\mathbf{R}(gf)_{*}$（1）。

**交换图**：1 个，命题 1.3.7 的纤维积方块（:308–310），按原书 p.530 页图用 preamble 的 `\diag{}`（内部 tikzcd）重排，不再贴位图、也不用 `\figdiag` 占位框。源码与成图核对如下：

```
\diag{X\times_{Y}Y' \arrow[r,"g'"] \arrow[d,"f'"']
\& X \arrow[d,"f"]\\
Y' \arrow[r,"g"'] \& Y}
```

对应

```
X×_Y Y'  --g'-->  X
   |                |
   f'               f
   v                v
  Y'      --g-->    Y
```

左上 $X\times_{Y}Y'$、右上 $X$、左下 $Y'$、右下 $Y$；上箭头 $g'$、下箭头 $g$、左竖 $f'$（标注在竖线左侧，用 `"f'"'` 的换侧）、右竖 $f$（标注在竖线右侧）。行距与列距沿用 `\diag` 的默认 `row sep=2.2em, column sep=2.6em`，图居中、字号与正文一致，成图未越出页心。页图在方块右下角另有一个句点（原书句读），本译本不收入图内。

**页图与文字层的出入（逐条）**

1. p.523：文字层一律无粗体，页图的 $\mathbf{C}(\cA)$、$\mathbf{H}(\cA)$、$\mathbf{D}(\cA)$ 均为粗体，已按页图排 `\mathbf`。同页标准三角的三支箭头在页图上带横线（同伦类 $\overline{f}$），文字层只给字母。
2. p.523：文字层把 $Cf$ 排成 `Cf`，页图亦为斜体 $Cf$（不是粗体 $\mathbf{C}f$），故与复形范畴 $\mathbf{C}(\cA)$ 不冲突。
3. p.524：文字层把 $\mathcal{N}$、$\mathcal{I}$、$\mathcal{P}$ 排作 `N`、`J`、`P`；页图为花体（"J"其实是花体 $\mathcal{I}$）。已按页图改花体。
4. p.525：Lemma 1.2.5 页图与文字层**一致**，均作 $\mathbf{R}FX\xrightarrow{\sim}X'$ 与 $X'\in\mathbf{H}^{+}(\cA)$——即原书本身的笔误（漏 $F$；$\cA$ 应为 $\cR$），已照录并加 Tutor Note（:119）。
5. p.526：页图印 `etale`（无重音），文字层同；本译本作 étale 并加 Tutor Note（:137）。
6. p.528：页图与文字层均作 $(\cE\otimes\cF)^{n}=\sum_{p+q=n}\cE^{p}\otimes\cF^{q}$，原书用 $\sum$ 记直和，照录（未改 $\bigoplus$）。
7. p.528：页图把两处 $\mathbf{R}f_{*}$ 的目标范畴印成 $\mathbf{D}^{+}(\cO_X\text{-}\Mod)$、$\mathbf{D}^{b}(\cO_X\text{-}\Mod)$，文字层同；应为 $\cO_Y$，分别加 Tutor Note（:240、:247）。
8. p.529：文字层把 $\mathcal{H}om^{n}(\cE,\cF)=\prod_{p}\mathcal{H}om(\cE^{p},\cF^{p+n})$ 的 $\prod_{p}$ 整个抽掉，只剩 `Homn(E, F) = p Hom(Ep, Fp+n)`；页图确为 $\prod_{p}$。这是本块必须核页图的实例之一。
9. p.530：命题 1.3.6 的对象范畴，页图与文字层一致均作 $\cE\in\mathbf{D}^{-}(\cO_Z\text{-}\Mod)$、$\cF\in\mathbf{D}^{-}(\cO_X\text{-}\Mod)_{\Qcoh}$，与式 (3) 的类型不符，照录 + Tutor Note（:304）。
10. p.525：原书印 `Dually,one`（逗号后缺空格），中译无对应位置，未加批注，仅记于此。

## 3 译注

**可见译注 `\yizhu`：6 条**（CJK 92–140 字，均在 60–200 字内，全部以 `【来源：…】` 收尾）

| 行 | 主题 | 来源 |
| --- | --- | --- |
| :41 | 映射锥的微分矩阵与"$f$ 拟同构 ⇔ $Cf$ 零调"的机制；三支箭头带横线说明标准三角只在 $\mathbf{H}(\cA)$ 中有意义 | 原书 pp.523–524；Verdier, Astérisque 239 (1996) |
| :77 | $\mathbf{H}(\cA)[\mathrm{Quis}^{-1}]$ 的含义（为拟同构添逆、Ore 条件、分式写法）；$\mathbf{D}^{\pm,b}$ 是全子范畴而非商 | 原书 pp.524–525；Gabriel–Zisman, *Calculus of Fractions and Homotopy Theory* (1967) |
| :89 | $\mathbf{H}^{+}(\cI)\to\mathbf{H}^{+}(\cA)\xrightarrow{Q}\mathbf{D}^{+}(\cA)$ 为等价 ⇔ 每个对象有内射复形代表，这是"用内射消解算 $\mathbf{R}F$"的根据 | 原书 p.524 及所引 [17]（按 I.4.6、II.5.6 判断为 Hartshorne, *Residues and Duality*, LNM 20） |
| :108 | 适应子范畴是内射对象的公理化（b) 给消解存在、a) 给零调保持）；内射层只是 $\cR=\cI$ 的特例 | 原书 p.525；同 [17] |
| :139 | 三层 $\coh\subset\Qcoh\subset\cO_X\text{-}\Mod$ 的分工：为何 $\coh$ 无足够内射对象、为何在 $\Qcoh$ 里算 | 原书 p.526；Hartshorne, *Algebraic Geometry*, GTM 52, II.5 |
| :280 | $\mathcal{E}xt^{i}$ 是层、取截面才是群；$\mathbf{R}\mathcal{H}om$ 只对第二个变元取内射消解，故定义在 $\mathbf{D}^{\mathrm{op}}\times\mathbf{D}^{+}$ 上 | 原书 p.529；同 [17] |

**校勘批注 `% [Tutor Note: …]`：8 条**（均为注释，不进入排版）

| 行 | 内容 |
| --- | --- |
| :10 | 原书用粗体 $\mathbf{C}/\mathbf{H}/\mathbf{D}$ 区分三类范畴，译本照此，与花体 $\cC/\cH$ 不同 |
| :119 | 引理 1.2.5 页图与文字层均作 $\mathbf{R}FX\to X'$、$X'\in\mathbf{H}^{+}(\cA)$；按理当读作 $FX'$、$\mathbf{H}^{+}(\cR)$，照录原文 |
| :120 | 原书 left/right bounded 取向与部分文献相反（left＝下界、属 $\mathbf{D}^{+}$），译本直译 |
| :137 | 原书印 `etale`，译本作 étale |
| :240 | $\mathbf{R}f_{*}$ 的 $\mathbf{D}^{+}$ 目标范畴印作 $\cO_X$，应为 $\cO_Y$，照录 |
| :247 | 同上的 $\mathbf{D}^{b}$ 版 |
| :264 | 层内 Hom 排花体 $\mathcal{H}om$、$\mathbf{R}\mathcal{H}om$、$\mathcal{E}xt$，本译本不用直立体的 `\RHom`/`\Ext`，以免与整体 Hom 混淆 |
| :304 | 命题 1.3.6 的 $\cO_Z$（应为 $\cO_Y$）与 $\cF$ 所属范畴（应为 $\cO_Y$），照录 |

## 4 术语

- 冻结表（`work/glossary.tsv`）中可用且已用的：三角范畴、特异三角、映射锥、同伦范畴、拟同构、导出范畴、局部化、共尾、内射／投射对象与消解、导出函子、概形、拟凝聚层、凝聚层、局部自由层、紧合、平坦、投影公式、平坦基变换、纤维积方块、诺特、F-adapted（F-适应）。
- 冻结表的三处**衔接问题**（不拟改表，仅登记）：
  1. 表内只有 `F-adapted＝F-适应`，而原书 p.525 用 `right adapted / left adapted`。本块按方位译作「右适应／左适应」，并在提案中登记，避免与表中的 F-适应冲突。
  2. 表内「零调」与「松弛层」均无条目，本块按 Weibel／Hartshorne 汉译惯例用「零调（acyclic）」「松弛层（flabby）」，已提案。
  3. 表内 `distinguished triangle＝特异三角`，而原书 p.523 另有 `standard triangle`（用于"与标准三角同构的类"这一构造性定义）。本块把它单列为「标准三角」，与「特异三角」并存，已提案并说明二者关系。
- 新术语提案 19 条，见 `work/proposals/ch01b.tsv`（shift functor、standard triangle、null-homotopic、acyclic complex、multiplicative system、right/left adapted、F-acyclic、left split、Grothendieck Abelian category、set of generators、direct colimit、flabby sheaf、local Hom、local hyper-Ext、finite Tor-dimension、right/left bounded、étale topology）。
- **记号层面的自主决定（需 Lead 裁定）**：p.529 起原书用花体 $\mathcal{H}om$／$\mathbf{R}\mathcal{H}om$／$\mathcal{E}xt$ 区分层内与整体，而 preamble 提供的 `\RHom`、`\Ext` 是直立体。本块为忠实于原书的这一区分，改用 `\mathbf{R}\mathcal{H}om`、`\mathcal{E}xt^{i}`、`\mathcal{H}om`，并在 :264 加批注说明。若全书统一要求走宏，只需把这三处替换为 `\RHom`、`\Ext`、`\Hom`，语义不受影响。

## 5 存疑

1. **引理 1.2.5 的类型问题（最重要）**：原书印 $\mathbf{R}FX\xrightarrow{\sim}X'$、$X'\in\mathbf{H}^{+}(\cA)$。$\mathbf{R}FX$ 与 $X'$ 分属 $\mathbf{D}(\cB)$ 与 $\mathbf{H}(\cA)$，字面读不通。应是 $\mathbf{R}FX\xrightarrow{\sim}FX'$ 且 $X'\in\mathbf{H}^{+}(\cR)$。已照录 + 批注，未擅自改字；若 Lead 决定"径改"策略，此处是最该改的一处。
2. 命题 1.3.6：原书 $\cE\in\mathbf{D}^{-}(\cO_Z\text{-}\Mod)$、$\cF\in\mathbf{D}^{-}(\cO_X\text{-}\Mod)_{\Qcoh}$，与式 (3) 的 $f:X\to Y$ 不符，应为 $\cO_X$／$\cO_Y$。已照录。
3. p.528 两处 $\mathbf{R}f_{*}$ 的目标范畴印作 $\cO_X$，应为 $\cO_Y$。已照录。
4. 文献 [17] 的身份是**推断**：正文所引 `[17], I.4.6`、`II.5.6`、`II.5.12`、`II.5.16` 与 Hartshorne, *Residues and Duality*（LNM 20, 1966）的章节编号吻合，译注中据此写成"按所引章节编号判断"。若参考文献块（refs.tex）最终给出不同答案，需回改 :89 与 :89 附近一条。
5. p.525 `Dually,one` 缺空格：原书排印问题，中译无法体现，未加批注。
6. 编译自检（`lualatex -interaction=nonstopmode -output-directory=build_ch01b main.tex`，121 页）：`file=src/chunks/ch01b.tex fatal=0 undefined=0 overfull=0 underfull=0 missingchar=0`。本块在日志中的区段是 `(./chunks/ch01b.tex` 到 `(./chunks/ch02a.tex` 之间，段内四类问题计数全为 0。全库汇总同为 `bang=0 undef=0 overfull=0 underfull=0`，仅剩 3 条 `Missing character: There is no α (U+03B1) in font lmroman10-regular`，定位在 `chunks/ch05b.tex`（日志 3394 行附近），不是本块引入，按分工未改他人文件。
7. 副作用警告：本块 3 个 `\tag` 公式与全库其余 `\tag` 共用同一个 equation 计数器，pdf 后端报 `ignoring duplicate destination with the name 'equation.1…'` 共 15 条。这是项目在 `\begin{equation}` 内手工 `\tag` 的固有现象，不影响阅读与编号显示，未处理。
8. 编译时 `main.pdf` 曾被其他会话的并发编译覆盖导致读不出（`ReplaceFileW EIO` 与 `invalid key in dict`），因此自检统一用 `-jobname=ch01bcheck` 输出到独立 PDF；`main.pdf` 本身的状态请以 Lead 的串行编译为准。
9. 一处版式小瑕疵（非本块可修）：p.523 的正文页（印张 11）页眉印作「1.2 导出范畴与导出函子」，但该页上部仍是 1.1 的引理 1.1.10 与式 (2)。原因是 `\section` 在 shipout 前已改写页眉标记，属 `\markboth` 的常规行为；若要求页眉严格随页内首个小节，需要改 preamble（本块无权动），故仅登记。

## 6 与邻块边界

- **首**：ch01a 在 p.523 上半仍有 Lemma 1.1.12、`enough F-split objects` 一段与式 (2)（伴随函子），这些**不在本块**。本块第一行即 `% [原文 p.523]` + `\section{导出范畴与导出函子}` + `\takeaway{}`，正文起于「设 $\cA$ 是加性范畴。我们用 $\mathbf{C}(\cA)$ 记微分复形的范畴。」——对应原书 1.2 标题后的第一句 `Let A be an additive category. We write C(A) to denote the category of differential complexes.`，未重复 ch01a 的内容。
- **末**：本块最后一条陈述是命题 1.3.8 与式 (5)（:321–327），其后是 `\chapterreview{}`（:330）。原书 p.530 下半的 `CHAPTER 2` / `2.1. Basic properties…` / 式 (6)（$\Hom(\cE,\cF)=\Hom(\cF,\cE\otimes\omega_X[n])^{*}$）**全部归 ch02a**，本块未译一字。
- 与 ch02a 的接口：ch02a 应从 `\chapter{凝聚层范畴及其间函子}` 起；本块的最后一句正文是「要使右导出函子在凝聚层的导出范畴之间有定义，需要对态射添加额外条件。」（:249），它正是引出命题 1.3.5 的过渡句，不是章末句——章末已由 `\chapterreview` 收住。
- 多译／漏译核查：把 `work/src/ch01b.txt` 的 p.523–530 共 8 页逐段与译文对照一遍（含 p.526 页首续句 `colimits, and has a set of generators.` 的挂接位置、p.528 `Note that if E is in …` 一段、p.529 末 `The other relations that we use fairly frequently…` 一句），未发现整句漏译或整段多译。段数比页图多出 3 处，均因原书在 display 后不缩进、译本仍按语义另起段（p.523 标准三角、p.528 左分裂与拟同构两句），属可接受的段界差异，已在此声明。
