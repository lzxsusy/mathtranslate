# Chapter I · 块 C（p.39–p.44）

译手：fs-tr-c　底本：arXiv:2102.13459v4　译文文件：`源码/sections/s03-chI-3.tex`
编译：`build.bat check sections/s03-chI-3.tex c` → `[OK] _check_c.pdf`，6 页，0 error，0 overfull，0 missing character。

## 1. 完成范围

| 节 | 原文标题 | 原文页 | 译文内容 |
| --- | --- | --- | --- |
| §I.10（承接） | The spectral action | p.39 | Remark I.10.3 全文 + 原脚注 7（1 段 + 1 脚注；本块不开 `\section`，节头与 Thm I.10.1 / Conj I.10.2 均在块 B 的 s02） |
| §I.11 | The origin of the ideas | p.39–p.42 | 12 段 + Problem I.11.1（question 环境） |
| §I.12 | Acknowledgments | p.43–p.44 | 2 段（长致谢段 + 经费段） |
| §I.13 | Notation | p.44 | 5 段 + 译者整理记号表 19 条 |

p.39 起首句为 I.10 的承接句（Remark I.10.3），已照原文译出并冠以 `\srcpage{39}`；p.37–p.38 的 I.10 正文归块 B，本文件不重复。

## 2. 编号对象对齐

| 原文 | 译文 label | 一致 | 备注 |
| --- | --- | --- | --- |
| Remark I.10.3 | `\begin{remark}` | 是 | 整书内应为「注 1.10.3」；单文件 check 显示「注 0.0.1」属正常（节号从 0 起、计数器为全章共用） |
| Problem I.11.1 | `\begin{question}` | 编号一致，环境名不同 | preamble 未定义 `problem` 环境，SPEC 的映射表亦无此条；暂用 question（显示「问题 1.11.1」），见 §7 |
| p.44 记号条目 19 条 | `description` 列表 | 见下表 | 原文为分号连缀的散文式列举，译文改为逐条 markdown 式列表，逐条对应、无增删语义 |

### I.13 记号条目（单列表）

| # | 原文记号/术语 | 译文条目 | 原文页 |
| --- | --- | --- | --- |
| 1 | $E$ | 非阿基米德局部域，剩余域 $\mathbb{F}_q$（$q=p^f$，$p>0$） | p.44 |
| 2 | $k$ | $\mathbb{F}_q$ 的代数闭包 $k=\bar{\mathbb{F}}_q$ | p.44 |
| 3 | $\breve E$ | $E$ 的完全无分歧扩的完备化，其剩余域为 $k$ | p.44 |
| 4 | $\bar E$ | $E$ 的可分闭包 | p.44 |
| 5 | $\Gamma$ | 绝对 Galois 群 $\Gamma=\Gal(\bar E\mid E)$ | p.44 |
| 6 | $W_E$ | Weil 群 | p.44 |
| 7 | $I_E$ | 惯性子群 | p.44 |
| 8 | $P_E$ | 野惯性子群 | p.44 |
| 9 | $P$ | 通常指 $P_E$ 的开子群；偶尔也指有限 $p$-群，或更一般地指阶与 $\ell$ 互素的有限可解群 | p.44 |
| 10 | $G$ | $E$ 上的约化群（一律假定连通） | p.44 |
| 11 | $\underline X$ | 把 $S$ 送到连续映射 $\lvert S\rvert\to X$ 的层（$S$ 取在相关测试范畴中，通常是完满空间） | p.44 |
| 12 | $\lvert S\rvert$ | 空间 $S$ 的 underlying 拓扑空间（配合 $\underline X$ 使用） | p.44 |
| 13 | anima | 即 [Lur09] 中的「空间」、$\infty$-群胚或同伦型；此词不译 | p.44 |
| 14 | $A[X_1,\dots,X_n]$ | 多项式代数；animated $A$-代数在筛余极限下由它们自由生成 | p.44 |
| 15 | $\mathcal{C}^{BG}$ | $\mathcal{C}$ 中 $G$-等变对象的（$\infty$-）范畴，即函子 $BG\to\mathrm{Cat}_\infty$ 的极限 | p.44 |
| 16 | $\ast/G$ | 分类叠（即常记作 $BG$ 者）；用此写法是为避与 Borel 子群 $B$ 混淆 | p.44 |
| 17 | $\ast$ | 单点，即 $\mathrm{Spd}\,\mathbb{F}_q$（据 `symbols.tsv` 补足，原文未显式定义） | p.44 |
| 18 | $B(G)$ | Kottwitz 集 | p.44 |
| 19 | $B$ | 亦表示 Borel 子群，故分类叠写作 $\ast/B$ 而非 $BB$ | p.44 |

第 12、17 条为原文未显式定义但正文实际使用的记号（$\lvert S\rvert$ 直接在 $\underline X$ 的定义中出现；$\ast$ 仅由「分类叠写作 $\ast/G$」间接给出），译文补足说明并已在此标明，不属于原文条目外的杜撰。

## 3. 公式核对

核对了 p.39–p.44 共 6 页（`_pg39.png`–`_pg44.png`，pymupdf dpi 150 渲染，核完即删）。`01_pages/pNNN.txt` 的提取有 6 处失真，均已按图像改正：

1. p.40：正文跨页公式实为 $\mathcal{O}_X^n\to\mathcal{O}_X(\frac1n)$；txt 丢上标、误作 `O_n X`。
2. p.42：完满球记号实为 $\widetilde{\mathbb{B}}^n_C$（双线体 B 加宽波浪号、下标 C）；txt 作 `eBn C`，波浪号整体丢失。
3. p.39：系数域有上划线，实为 $\overline{\mathbb{Q}}_\ell$（出现 2 次：Remark 首句、$L$-参数 $\varphi:W_E\to\hat G(\overline{\mathbb{Q}}_\ell)$）；txt 全作 `Q_ℓ`。
4. p.42：$\overline{\mathbb{Q}}_\ell$- 与 $\mathbb{Q}_\ell$-向量空间并列，前者有上划线；txt 二者同形，无法区分。
5. p.41：$D_{\mathrm{ét}}(\mathrm{Bun}_G,\mathbb{Z}/\ell^n\mathbb{Z})$ 的下标为「ét」（带尖音符），非 `D_et`。
6. p.44：$\underline X$ 带下划线（原文用 $\underline{\phantom{X}}$ 表示层），txt 作普通 `X`。

另核对：p.41 $\pi_b:\mathcal{M}_b\to\Bun_G$（花体 M）、`dim. trg`、p.42 $[X/\mathbb{G}_m]$、$A\in D_{\mathrm{ét}}([X/\mathbb{G}_m],\Lambda)$、p.43 $D(\Bun_G,\overline{\mathbb{Q}}_\ell)$、p.44 $\Gamma=\Gal(\bar E\mid E)$、$BG\to\mathrm{Cat}_\infty$、$A[X_1,\dots,X_n]$。

## 4. 译注

共 6 条（全部为 `\yizhu`，无 `\yizhuw`；均 ≤120 字且各自带来源）：

| # | 类别 | 位置 | 内容摘录 |
| --- | --- | --- | --- |
| 1 | 术语 | I.10 p.39 | 「反常—凝聚」(perverse-coherent) $t$-结构：glossary 仅收 perverse $t$-structure，原文加引号表明尚未定名，保留英文原词 |
| 2 | 其他 | I.10 p.39 脚注 7 | hadal 指海洋「深渊带」，是作者对 Hansen 所引入 $t$-结构的戏称；[Han24] 照录不译 |
| 3 | 疑似笔误/套语 | I.11 p.41 | 原文 `etc.pp.` 为拉丁套语 *et cetera perge perge*（等等，不一而足）的缩写，非笔误 |
| 4 | 术语 | I.11 p.42 | 「完满球」即完满空间意义下的 $n$ 维球；glossary 仅收 perfectoid space，本词按词根一致暂译，待并入术语表 |
| 5 | 疑似笔误 | I.11 p.42 | 原文作 "Our attacks on this failing, a third key idea comes in:"，疑脱 "In"（当作 "In our attacks on this failing"），译文按原意补足 |
| 6 | 术语 | I.13 p.44 | sifted colimit 指以筛范畴为指标范畴的余极限；未入 glossary，暂译「筛余极限」并保留英文 |

另：`anima` 一词原文 I.13 自身即给出定义（"for what is variously called spaces … $\infty$-groupoids, or homotopy types"），且裁定「不译」，故未另立译注（决策见 `work/trace-chI-c.md`）。

## 5. 术语新增（待 Lead 并入）

| 英文 | 建议中文 | 依据 |
| --- | --- | --- |
| perfectoid ball | 完满球 | perfectoid space＝完满空间（glossary）+ 球（ball）；p.42 $\widetilde{\mathbb{B}}^n$ 的原名 |
| sifted colimit | 筛余极限 | sifted category＝筛范畴（Lawvere 理论惯译），余极限沿用 glossary |
| perverse-coherent | 反常—凝聚（保留英文 perverse-coherent） | 原文加引号、未定名；glossary 有 perverse $t$-structure＝反常 $t$-结构 |
| isocrystal | 同晶（isocrystal） | 通行译名「同晶」，首次出现括注原文 |
| minuscule | minuscule（不译） | 与「余特征标」连用，指 minuscule cocharacter，汉语无稳定译名 |
| supercuspidal | 超尖（supercuspidal） | 通行译名，首现括注原文 |
| weight-monodromy | 权—单值猜想 | weight＝权、monodromy＝单值，与 glossary 的权—单值一致 |
| chart | 图卡 | $\pi_b:\mathcal{M}_b\to\Bun_G$ 的覆盖含义，避免与「图表/坐标卡」混淆 |
| sanity check | 健全性结果 | 原文 "basic sanity results on dimensions"，取「健全性」 |
| hadal | 深渊带（保留 hadal） | 原文戏称，见译注 2 |
| excurson operator | （沿用）游走算子 | 已在 glossary / 裁定冻结 |

### 与 `symbols.tsv` 的出入（按任务要求只报告、不改表）

1. `symbols.tsv` 明令「$X_{FF}$ 原文从未使用，请勿引入」——已遵守，全篇未出现 $X_{FF}$，Fargues–Fontaine 曲线一律写全名并首次注原文。
2. $\ast=\mathrm{Spd}\,\mathbb{F}_q$、$q=p^f$、$\lvert S\rvert$ 三条在 `symbols.tsv` 中有、在原文 I.13 中未显式定义，译文在记号表中补足并标注（§2 第 12、17 条）。
3. `symbols.tsv` 记 $\hat G$ 为对偶群并注明「原文 I.13 未用 ${}^L G$」——本块亦未出现 ${}^L G$，`S_\varphi\subset\hat G$` 照原文写 $\hat G$。
4. 术语冲突：`glossary.tsv` 第 148 行 condensed＝「凝聚态」，而 `术语裁定.md` 第 25 行定「凝聚」；按「裁定即冻结」采用**凝聚**（凝聚数学、凝聚集、凝聚语言）。

## 6. 疑点（未解）

1. p.42 $\widetilde{\mathbb{B}}^n_C$ 的下标 $C$ 原文未作说明（正文只说 "$\widetilde{\mathbb{B}}^n$ is a perfectoid ball"，未定义 $C$）。译文照抄记号、不臆断含义；疑指所依赖的完满基域（如 $\mathbb{C}_p$ 的完满化），待查作者其他文献。
2. p.41 "etc.pp." 已判定为拉丁套语而非笔误（译注 3），但若原意确为 "etc." 的重复键入，则该判断可撤回——保留为低置信度条目。
3. p.42 "Our attacks on this failing…" 的脱字判断（译注 5）无法由版本比对证实；若底本 v5 有改动需复核。

（p.37–p.44 在 `疑点清单.tsv` 中的其它条目均已「已解」，本块未新增已解条目。）

## 7. 遗留问题

1. **`\srcpage` 落页不稳定（全局性问题，非本块特有）**：`\srcpage{N}` 由 `\marginpar` 实现，在单文件 check 中 p.39/p.40/p.42/p.44 四处页标未落到页边（p.41、p.43 正常），且同一文件重编译后丢失位置会变；块 B 的 `_check_b.pdf` 亦有同样现象（p.25、p.28、p.32 的页标缺失，p.26/27/29/30/31/33 正常）。源文件中 6 个 `\srcpage` 均在语义正确的位置（39 于 Remark 前、40 于跨页句「两种对偶描述」后、41/42/43 于各页首段前、44 于「Zhiyu Zhang 对第一版的评论」处），建议 Lead 全局改用 `marginnote` 或在书末加「原文页—译本页」对照表。
2. **Problem I.11.1 的环境**：preamble 无 `problem` 环境，SPEC 映射表亦未覆盖；暂用 `question`（显示「问题 1.11.1」）。若整书要区分 Question 与 Problem，需 Lead 在 preamble 增补 `problem` 并同步改本处。
3. **I.13 的呈现形式**：原文是散文式列举，译文保留 5 段正文，另加「记号一览（译者整理）」小节做逐条对照；该小节用 `\subsection*`，不进目录、不占编号。若整书体例要求记号一律入表、正文不再保留，需要 Lead 统一裁量。
4. 本块译文 6 页，公式全部按图核对；`anima` 未单列译注（理由见 §4 末）。
