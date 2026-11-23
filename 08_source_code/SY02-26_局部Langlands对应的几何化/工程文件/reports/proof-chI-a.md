# Chapter I · 块 A 校对报告

校对对象：`源码/sections/s01-chI-1.tex`（§I.1–§I.4，PDF p.7–p.22）
底本：Fargues–Scholze, *Geometrization of the local Langlands correspondence*, arXiv:2102.13459v4
校对者：fs-pf-a

## 0. 结论

**可交付**（5 处改动已直接改进 tex，编译 0 error，16 个页码锚点两检全 `[ok]`）。
需 Lead 裁决的遗留事项有三件，都不影响本块文字正确性：①译注第 15 条的出处指向（`§III.2`）在原文其他章节未见该术语定义；②译注与作者脚注共用计数器，作者原注 1–4 现显示为 4/6/10/17（细节与建议见 §4、§6）；③复核 `work/errata.tsv`：已有 **E1**（p.22「is a also consequence」，status=fixed）与 **E4**（p.21 §I.4 的 (iv)/(v) 与 p.87 定理 III.0.2 对调，open），两者本次均回原文确证，无需另行动作；建议增设一条 **E5：p.14「a map $S\to\Spa E$」漏 $\sharp$**（详见 §3、§6）。

## 1. 逐维度结果

| 维度 | 检查量 | 问题数 | 说明 |
|---|---|---|---|
| 1 漏段/并段 | 16 页逐段点数：原文 89 个段首 vs 译文 117 个段落块（含 `\noindent` 列表项与定理/定义环境，故多于原文） | 3 | 无漏段、无漏句；**3 处把原文同一段拆成两段**（p.10、p.14、p.21→p.22），已合并。判定依据：pymupdf 逐行取 `bbox.x0`，新段首 x0=82.7pt、续行 x0=64.8pt（显示公式后的续排亦为 64.8） |
| 2 术语不一致 | 47 组 glossary/术语裁定关键词全量 grep（完满空间 15、菱形 13、等晶体 23、纯内形式 13、扩充纯内形式 5、半稳定 10、修正 7、紧合 4、Hecke 叠 7、局部 Hecke 叠 3、局部空间菱形 6、z-扩张 3、泛 Cartan、Newton 点、Kottwitz 集、Schubert 胞腔、几何 Satake 4、融合积、反常层 2、半正交分解 2、丰沛、整体截面 3、Jacobian、Beauville–Laszlo 单值化、Harder–Narasimhan 4、分次环、Krull、部分紧合 2、分类叠 2/分类空间 1、幂幺 2…） | 0 | 无同词异译。反查变体：完美/钻石/固有/修改/同晶体/半稳态/幂零（仅用于「拓扑幂零单位」，符合 nilpotent↔幂零、unipotent↔幂幺的分工）全为 0 或用法正确。`shtuka`(1)、`sousperfectoid`(1)、`pro-étale`(5) 按裁定不译 ✓；`solid`/`anima`/`Hecke eigensheaf`/`excursion operator` 在 p.7–22 原文本身未出现，译文不出现正确 |
| 3 公式错 | 全部 display 与行内公式（p.7–p.22 共 30 余个 display）；其中 p.9 的 $H_\lambda$、p.12 的 $\bar{\mathbb F}_q((t))=\breve E$ vs $\mathbb F_q((t))$、p.14 的 $\bar{\mathbb F}_q$ 上完满空间、p.22 的 $\mathrm{Spd}\,\bar{\mathbb F}_q[[t^{1/p^\infty}]]$ 回图 260–300 dpi 裁剪逐字核对 | 0 | 矩阵 $\mathrm{Diag}$、$\varphi_{\mathcal F}$、$X_S=\mathbb G_m\backslash(\LG\times\Spa\breve E)/\varphi^{\mathbb Z}$、直和分解、$\mathcal M_b=\widetilde{\mathcal M}_b^{\mathrm{perf}}\times_{\widetilde X_{\mathrm{perf}}}X$、$\widetilde X=\Div^1\times_{\Bun_G}\Div^1$、$X_S=\bigoplus\mathrm{BC}(\mathcal O(\lambda))$、$T_V$、Hecke 对应式与原文一致。p.14「连同映射 $S\to\Spa E$」原文确无 $\sharp$（原书笔误，译文忠实，见 §3） |
| 4 编号 | 21 个编号对象（定理/定义/命题/注 I.2.1–I.4.1）逐个与原文对齐；编译 PDF 中 21 个 `\label` 全部解析 | 0 | 与原文一一对应；本块无 `\ref` 交叉引用调用（正文按原书以「定理 I.x.y」直书），故无断链 |
| 5 译注质量 | 15 条译注逐条读，抽查 5 条回溯到 `01_pages` 原文/A 级文献（见 §4） | 1 | 1 条出处事实错（Vogan 论文题名，已改）；1 条出处指向可疑（§III.2，未改，报 §4）；3 条把「译者补证」标成 A 级（性质标注偏强，非错，见 §4）；另有脚注编号被作者注挤压的问题（§4、§6） |
| 6 过度翻译 | 文献标签 ≥20 个（[GL17]、[Gai16, §4.2]、[Zhu20]、[Ans22]、[Kot85]、[Kot97]、[Kal14]、[Vog93]、[SW20]、[XZ17]、[Iva23, Lemma 5.9]、[RR96]、[LS18]、[FS21]、[Ked05]、[Ham22]、[Han20]、[AGLR22]、[Far16]、[RZ96]、[Dri18] 等）；专名 | 0 | 标签全部保留原样，未译；人名、机构名、`Perfect`/`Perf`、`$\Bun_G$`、`$\Div^1$` 未硬译 |
| 7 中文质量 | 全块通读（581 行） | 1 | p.9「它是基本的**恰当**它只有一条斜率」→「当且仅当」（原文 it is basic precisely when…；同文件他处正确作「当且仅当」）。「的的」「了了」0 处；长句可读 |
| 8 体例 | `\srcpage`/`\srcpageinl` 16 个（p.7–p.22 无缺页）；环境类型；`\footnote` 用法；另**逐个核对 16 个锚点与原文页首页界的位置**（不只看是否印出） | 0（1 处随合并调整；2 处标题行级偏差判断为可接受） | 页锚 16/16 齐全，编译后在 PDF 中全部可见；14 处锚点与原页首词逐字对齐（如 p.12 落在「并｜不」之间、p.18 在 (viii) 之前、p.21 在 (iii) 之前），p.7 锚点在章节标题之后、p.19 锚点在定理 I.3.3 正文首句（各差 1–2 个标题行，见 §3，未改）；段落合并后 p.22 的锚点由 `\srcpage{22}` 改为 `\srcpageinl{22}`（段中页界，与其余 9 处段中页界体例一致） |
| 9 编译 | `build.bat check sections/s01-chI-1.tex pa` | 0 | `[OK] _check_pa.pdf`（16 页），0 error，0 Overfull；仅 hyperref 书签警告与 rerun 提示（见 §5） |
| 10 黑名单 | 「显然/众所周知/不难看出/容易看出」0；来源黑名单（知乎/百度百科/CSDN/简书/公众号/博客）0；本机绝对路径（`C:\`、`/Users/`）0 | 0 | 符合 BRIEF §5.4 |

## 2. 改动清单

| 序号 | 位置(页/行) | 原文 | 原译 | 改后 | 依据 | 类型 |
|---|---|---|---|---|---|---|
| 1 | p.9 / L73 | it is basic precisely when it has only one slope $\lambda$ | 它是基本的恰当它只有一条斜率 $\lambda$ | 它是基本的**当且仅当**它只有一条斜率 $\lambda$ | 原文 `precisely when`；同文件 L278 同一句式正确作「当且仅当」 | 错字/中文 |
| 2 | p.10 / L108–L109 | …[$\LG(R)$ display] **Changing the trivialization** of the $G$-torsor amounts to $\sigma$-conjugation on $\LG$…（同一段） | L108 `\]` 之后空行，L109 另起一段「改变 $G$-主丛的平凡化…」 | 删去空行，两段并一 | p.10 段首仅 5 个：117.5 To go further／162.6 There are several ways／306.0 A better perspective／456.0 This definition can be extended／539.6 We will not use the stack；「Changing the trivialization」行 x0=64.8pt（续行） | 并段 |
| 3 | p.14 / L235–L236 | …[display $(\Spa\breve E)^\diamond/\varphi^{\mathbb Z}$] **More generally**, for any $S\in\mathrm{Perf}$…（同一段） | L235「的 $S$-值点一一对应。」后空行，L236 另起一段「更一般地…」 | 删去空行，两段并一 | 「More generally」行 x0=64.8pt（y≈289.8）；p.14 段首仅 6 个（148.1 One sees that／380.8 This ends／551.0 A peculiar／594.5 Again／613.0 Definition I.2.4／674.0 Remark I.2.5） | 并段 |
| 4 | p.21→p.22 / L552–L553 | …$\Aut(\mathcal O\oplus\mathcal O(1))=\begin{pmatrix}E^\times & \mathrm{BC}(\mathcal O(1))\\ 0 & E^\times\end{pmatrix}.$ **Here** $\mathrm{BC}(\mathcal O(1))$ is representable…（跨页同一段） | L552 `\]` 后空行；L553 `\noindent\srcpage{22}这里 …`（另起一段） | 删去空行与 `\noindent`，`\srcpage{22}` 改 `\srcpageinl{22}`，与上段合并 | p.22 首行「Here BC(O(1))…」x0=64.8pt（y=117.5），非段首 | 并段＋锚点类型 |
| 5 | p.8 / L40 | 参考文献 [Vog93]：D. Vogan, Jr., *The local Langlands conjecture*, Contemp. Math. 145 (1993)（`01_pages/p356.txt:37`） | 译注写作 Vogan, *On the local Langlands conjecture*（[Vog93]） | Vogan, *The local Langlands conjecture*（[Vog93]） | 原书参考文献条目（p.356）无「On」 | 译注事实错 |

> 改动统计：5 条（并段 3、错字 1、译注事实 1）。tex 行数 584 → 581（删 3 个空行）。除上述 5 处外未动 tex 的任何字符；preamble/main/build.bat/其他 section/glossary/01_pages 均未触碰；未删除任何译注。

## 3. 未改动但存疑

| 位置 | 疑问 | 为何不改 |
|---|---|---|
| p.14 / L225 | 原文「together with a map $S\to\Spa E$」缺 $\sharp$（按上下文应为 $S^\sharp\to\Spa E$，函子定义处 $f:S^\sharp\to Z$ 可证） | 原文如此（260 dpi 裁剪确证）。译文忠实照译；属**作者笔误**，已在 §6 建议作为 errata **E5** 补登（p.22 的「is a also」即现有 E1） |
| p.14 / L225 | 译文「连同映射 $S\to\Spa E$ 模 Frobenius 作用」——与原文语序一致 | 同上，语序忠实；改则越界 |
| p.10 / L108 | 「改变 $G$-主丛的平凡化…」合并后与上句「…其中我们如下定义环路群」之间隔着 display，中文读来仍顺 | 已按原文合并，不再动 |
| p.15 / L307；p.19 / L461 | 「即便它定义在更 exotic 的测试对象上」「Banach–Colmez 空间是更 exotic 的对象」 | 英文形容词夹中文属译风，非错；报 Lead 备查 |
| p.12 / L149 | 页界落在「并|不」二字之间，`\srcpageinl{12}` 插在词中（原文 p.11 末 does / p.12 首 not，位置精确） | 位置精确无误，仅阅读时略碍眼；不改 |
| p.22 / L552–L553 | 合并后同段出现「这里 …（矩阵）… 这里 $\mathrm{BC}(\mathcal O(1))$…」两次「这里」 | 原文同样两处 Here；重复属原文风格，不改 |
| p.22 / L581 | 文件以「对于」收尾，句子续到 p.23（下一块） | 跨块断句，非本块错误（见 §6） |
| p.7 / L12 | 锚点落在 §I.1 标题之后（原文 p.7 以章标题「CHAPTER I / Introduction」开头），与页首差约两个标题行 | 标题行不是正文，锚点贴首句更好用；若移到 `\chapter` 之后，行内上标会挂在标题末尾，破坏版式 |
| p.19 / L431 | 锚点落在定理 I.3.3 正文首句（原文 p.19 以「Theorem I.3.3.」标题开头），与页首差一个标题行 | 移到 `\begin{theorem}` 前须在竖直模式插 `\leavevmode`，会多出空隙、改变定理上间距；现位置仍指向 p.19 首段，可接受 |
| p.12 / L149；L495 | 正文保留英文缩写「resp.」（`L107` 公式内的 `\text{resp. }` 不在此列） | 中文数学文献通行写法，BRIEF §4 未禁止；属风格非错，统一口径由 Lead 定 |

## 4. 译注抽查

共 **15 条**译注（`\yizhu`），另 4 条作者原注（`\footnote`）。抽查 5 条（并附全体审计结论）：

1. **L19「朗兰兹对偶群」**（来源：I：glossary.tsv；A：原文 §I.1 第 2 段）——**来源成立**。原文 p.7「It is a reductive group over $\mathbb Z$, whose root datum is dual to that of $G$」，与注文「$\mathbb Z$ 上分裂的约化群，其根数据与 $G$ 的根数据对偶」逐字对应；与裁定「朗兰兹对偶群」一致。
2. **L23「本质上是双射」**（来源：A：原文 p.36）——**来源成立**。`01_pages/p036.txt:53–56`：「(ix) For $G=\mathrm{GL}_n$ and supercuspidal $\pi$… Note that parts (viii) and (ix) together say that for $\mathrm{GL}_n$ and general $\pi$, the $L$-parameter $\varphi_\pi$ is what is usually called the semisimple $L$-parameter.」注文所引无误。
3. **L208「经典点」**（来源：A：原文 §I.3 与 pp.51, 56；I：glossary.tsv）——**来源成立**。`p051.txt:5–14` 定义 classical points（$|\mathcal Y_C|^{\mathrm{cl}}$），`p056.txt:33`（Definition/Proposition II.1.22）给出 $|X_C|^{\mathrm{cl}}:=|\mathcal Y_C|^{\mathrm{cl}}/\varphi^{\mathbb Z}$，与「逐点局部定义、完整定义见 pp.51, 56」相符。
4. **L574「is a also」笔误注**（来源：A：原文 p.22）——**来源成立**。p.22 原文印作「Part (iv) / is a also consequence of Theorem I.3.4.」（300 dpi 裁剪逐字核对，行断于「is a」之后），确为语序笔误；译注判断正确，译文按「也是……的推论」处理得当。**已由 `work/errata.tsv` 的 E1 登记（status=fixed）**，无需再动。
5. **L293「幂幺群菱形」**（来源：A：原文 §I.2 与 §III.2）——**来源可疑**。`unipotent group diamond` 在全书 OCR 文本中仅出现于 p.15（本块使用处）；Chapter III 的 §III.2 标题为「The topological space $|\mathrm{Bun}_G|$」，其 §III.2.4 讲 Kottwitz 不变量的局部常性，`p090/p103/p105` 只出现「unipotent group scheme / “unipotent group” / unipotent radical」，未见「unipotent group diamond」的定义。建议 Lead 指派核对 §III.4（semistable locus）或删去「§III.2」这半句——**未擅改**。

其余 10 条审计结论：L21（L-包）、L56（等晶体）、L74（单射性）、L93（完满化）、L146（Hecke 算子）、L154（完满空间）、L230（菱形）、L353（几何 Satake）、L490（$\kappa$）均与原文/术语表相符；其中 L56/L74/L93 三条的正文内容是「译者补证」（原文只给结论或一句理由），却标成 A 级，建议统一改标为「A+译者补证」或「B」，属标注口径问题而非事实错误。L490「其与 $\pi_1$ 的完整对应在 §III.2 中正式建立」与 §III.2.4 相符，成立。

**脚注编号**（实测，编译 PDF 脚注区逐条提取）：译注占 1,2,3,5,7,8,9,11,12,13,14,15,16,18,19；作者原注 1–4 显示为 **4、6、10、17**（译手报告中「4/5/10/19」的说法有误：5 与 19 实为译注）。成因：`preamble.tex:29–31` 的 `\yizhu` 直接调用 `\footnote`，与作者脚注共用计数器；**未改 preamble**。

## 5. 编译与统计

- 编译：`cd 源码 && build.bat check sections/s01-chI-1.tex pa` → `[OK] _check_pa.pdf`，**16 页，0 error**，0 Overfull/Underfull box。
- 警告：仅 hyperref「Token not allowed in a PDF string（line 473，`\section{$\Bun_G$ 的几何}` 中的数学）」与首遍的「Label(s) may have changed. Rerun」提示；不影响正文，整书两遍编译即消。
- 锚点：`python ../工程文件/tools/check_pagemarks.py _check_pa --start 7 --end 22 --pdf` → `[ok] 16 锚点全部在 PDF 中可见`、`[ok] p.7–p.22 锚点齐全`（两个 `[ok]` 均出现）。
- 锚点构成：`\srcpage` 6 个（p.8,11,13,15,19,21，段首）＋ `\srcpageinl` 10 个（p.7,9,10,12,14,16,17,18,20,22，段中页界）＝16。
- 锚点位置复核（`check_pagemarks` 只验「印没印出」，故另做）：16 个锚点逐个对照原文页首页词，14 处与页首词逐字对齐；p.7、p.19 各差 1–2 个标题行，判断为可接受（见 §3），未改。
- 结构统计：`\chapter` 1、`\section` 4（I.1–I.4）、编号对象 21（定理 7／定义 3／命题 1／注 10）、译注 15、作者注 4、文献标签 ≥20。
- 段落：原文 p.7–p.22 共 89 个段首，译文逐页对齐；修正后段落切分与原文一致（3 处多余分段已并）。

## 6. 给 Lead 的建议

1. **errata 台账（不改正文）**：`work/errata.tsv` 已有 **E1**（p.22「is a also consequence」，fixed，依据见 §4-4 与本次 300 dpi 复核）与 **E4**（p.21 的 (iv)/(v) 与 p.87 定理 III.0.2 对调，open），本次均已回原文确证，无需另行动作。建议**增设 E5**：p.14「together with a map $S\to\Spa E$」漏 $\sharp$（同段函子定义处作 $f:S^\sharp\to Z$，可证应为 $S^\sharp\to\Spa E$）；译文照译，不改。
2. **脚注编号方案请裁**：现作者原注显示为 4/6/10/17，与原文 1–4 不符但相对顺序正确，且 `[来源：…]` 标识已足以区分译注／作者注——**我倾向认为可接受**，只需在「凡例」里加一句「楷体灰色加 [来源：…] 者为译注，脚注编号连同作者原注统一编」。若要严格复原 1–4，须动 `preamble`（给作者注单独的 `\footnotemark[1]` 式编号或给译注独立计数器/改用 marginpar），属 Lead 权限，本块未动。
3. **两条译注事务**：①p.15 译注出处「§III.2」在原文未见该术语，建议核对或删半句（§4-5）；②L56/L74/L92 三条把「译者补证」标成 A 级，建议统一口径。另提醒：**p.21 定理 I.4.1 的 (iv)/(v) 与 p.87 定理 III.0.2 编号互换，属原文自身不统一，不是本块译文错误**（即 errata E4），本块译文与 p.21 原文逐条一致，无需返工。
