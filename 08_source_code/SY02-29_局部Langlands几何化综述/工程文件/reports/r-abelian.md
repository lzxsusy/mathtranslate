# r-abelian —— §9 交换的情形 + 文献表（原文 p.42–p.46）

译手：abelian　｜　底本：`fargues_ov/Fargues_Geometrization_overview.pdf` p.42–p.46

## 1. 交付

| 文件 | 内容 |
|---|---|
| `源码/sections/s11-abelian.tex` | 原文 §9 全文（9.1 GL₁ 情形 + 9.2 环面情形），248 行 |
| `源码/sections/s99-bibliography.tex` | 文献表框架（`thebibliography`，[1]–[32] 逐条照抄英文，只加 `\bibitem`），47 行 |
| `工程文件/reports/r-abelian.md` | 本报告 |
| `工程文件/work/trace-abelian.md` | 逐段译法 trace、公式清单、笔误登记 |

**编译自检**

```
cd 源码 && build.bat check sections/s11-abelian.tex g   → [OK] _check_g.pdf（5 页，0 error，0 overfull）
cd 源码 && build.bat check sections/s99-bibliography.tex b → [OK] _check_b.pdf（3 页，0 error，0 overfull）
```

`_check_g.pagemarks` = `42 43 44 45 46`（5 个锚全部登记）；两个文件均无 `??`。

**页锚**（5 个，正好覆盖 p.42–p.46）

| 页 | 形式 | 落点 |
|---|---|---|
| p.42 | `\leavevmode\srcpage{42}` | `\subsection` 后正文首句「本节对 p-进域 E 上的 GL₁ 验证该猜想」之前 |
| p.43 | `\leavevmode\srcpage{43}` | 命题 9.1 证明结束之后、p.43 正文首句「现在设 $\varphi:W_E\to\Ql^\times$ 是连续特征」之前（原文 42/43 的页界正在证毕与下一段之间） |
| p.44 | `\srcpageinl{44}` | §9.2 括号注「……也许我们该在整个猜想中都这样做）」内，p.43→p.44 的断句处 |
| p.45 | `\srcpageinl{45}` | 「只依赖于〔p.45〕这个 Weil 反常层……」句中，p.44→p.45 的断句处 |
| p.46 | `\leavevmode\srcpage{46}` | 末段「由此推出」之前（文献表前） |

p.42 页首即 "9. THE ABELIAN CASE"，页面上半无 §8 残余；故 42 号锚放在 §9 正文首句，未另设 §8 结束标记。

**统计**：`\section` 1，`\subsection` 2，`proposition` 4（9.1/9.2/9.3/9.5），`example` 1（9.4），`proof` 3，`tikzcd` 2，编号公式 2（(10)(11)，用 `\tag` 硬保原文号），`\yizhu` 6 + `\yizhuw` 4 = 10 条译注。

**文献表**：`\begin{thebibliography}{32}` 内 32 条 `\bibitem`，条目文字英文原样（作者、年份、卷期页、期刊名一律不改），仅把原文的斜体（期刊/丛书/预印本/网址）转成 `\textit`，网址用 `\url`；原文 p.46 末尾的作者通讯地址作为「非文献条目」排在 `\end{thebibliography}` 之后，若 Lead 认为多余可整段删除（见 §4 疑点 D9）。

## 2. 编号对齐表

| 原文 | 译文 | 标签 | 备注 |
|---|---|---|---|
| 9. The abelian case | `\section{交换的情形}` | — | |
| 9.1. The GL₁-case | `\subsection{\texorpdfstring{$\mathrm{GL}_1$}{GL1} 情形}` | — | |
| Proposition 9.1 (1)(2) | `proposition` | `prop:9.1` | 两条 enumerate，编号 (1)(2) 照原文 |
| Proposition 9.2 | `proposition` | `prop:9.2` | |
| (10) | `\begin{equation}\tag{10}` | `eq:9.10` | 两行 `aligned`，等号对齐 |
| 9.2. The case of tori | `\subsection{环面情形}` | — | |
| Proposition 9.3 | `proposition` | `prop:9.3` | |
| (11) | `\begin{equation}\tag{11}` | `eq:9.11` | |
| Example 9.4 | `example` | `ex:9.4` | 与 proposition 共用一个计数器，验算得 9.4 后 9.5 顺延（见下） |
| Proposition 9.5 | `proposition` | `prop:9.5` | 计数器实测 1.5 = 原文 9.5，编号自动对齐 |

计数器实测（隔离自检）：prop 1.1 / 1.2 / 1.3 / 例 1.4 / prop 1.5，与原文 9.1 / 9.2 / 9.3 / 例 9.4 / 9.5 一一对应；整书内为 9.x。正文交叉引用「由命题~\ref{prop:9.1}」隔离时印 1.1、整书印 9.1；「即得 9.1 中的结果」「由式 (10)」按原文文字写死。

## 3. 译注（10 条）

| # | 位置 | 内容 | 类型 |
|---|---|---|---|
| 1 | p.42 `\mathcal{T}_d` 后 | 原文用下划线 $\ul{E}^\times$、$\ul{T}(E)$、$\ul{\QQ}_p^\times$、$\ul{Hecke}$ 标常值群/Hecke 叠，译文照留 | A+I |
| 2 | p.42 同句 | torsor 保留英文原词（glossary 未收） | I |
| 3 | p.43 χ 定义后 | 「Art」= 算术 Artin 互反映射，一致化元 ↦ Frobenius；$\chi(\pi)$ 未必是 ℓ-进单位，正是 Weil 层不能下降的原因 | A+B |
| 4 | p.43 「按特征层性质」 | glossary 把 character sheaf 与 eigensheaf 都译「特征层」，此处指 character sheaf property，与 Hecke 特征层不是一回事 | I+A |
| 5 | p.43 证明中 | 原文「this is an isomorphic」缺名词（`\yizhuw`） | 笔误 |
| 6 | p.43 Kottwitz | κ: B(T)≅X_*(T)_Γ 的来源与 Bun 的分块约定 | A+B |
| 7 | p.44–45 | 原文此处说「Weil 反常层」，而 ℱ 按定义是秩一 Weil 局部系统；作者混用，译文照原文 | A+I |
| 8 | p.45 「晶体表示」 | 原文「cristalline」（法语拼法）= crystalline（`\yizhuw`） | 笔误 |
| 9 | p.45 「余特征」 | 原文「The chocaracter」= cocharacter（`\yizhuw`），按 glossary 译「余特征」 | 笔误 |

第 10 条（p.42 $Rf_*\mathcal{E}$ 前）：原文把「$\cO(i)$ 与 $\mathcal{T}$ 之间同构构成的 torsor」中的两个对象都记作 $\mathcal{T}$，自指不通（`\yizhuw`，照字面保留）。

## 4. 疑点

| # | 位置 | 原文 | 类型 | 处理 | 状态 |
|---|---|---|---|---|---|
| D1 | p.43 | "this is an **isomorphic**" | 语法笔误 | 按 an isomorphism 读出，`\yizhuw` 说明，不改 | 待 Lead 定夺 |
| D2 | p.45 | "The **chocaracter** $\mu'$" | 拼写笔误（cocharacter） | 译「余特征」，`\yizhuw` 说明 | 待 Lead 定夺 |
| D3 | p.45 | "**cristalline** representation" | 法语拼法 | 译「晶体表示」，`\yizhuw` 说明 | 待 Lead 定夺 |
| D4 | p.45 | "if $b \in T(E)$ … is never effective **unless** $b$ is a root of unity" | 语义反了？原文意为「除非 b 是单位根，否则绝不有效」，字面照译；按数学应有「若 b 是单位根则有有限阶、下降数据可能有效」 | 照字面译出 | 记录，不改 |
| D5 | p.45 | "For $b \in T(L)$ **here is** an isomorphism" | 笔误（there is） | 中文「有……同构」，笔误在译文中不可见；登记于此 | 记录 |
| D6 | p.44 | "the n-th iterate of the **descente** datum (11)" | 法语词混入（descent） | 译「下降数据」，不另注 | 记录 |
| D7 | p.43 | Frobenius 下降数据落在 $\Bun^d_{\ol{\FF}_p}$ 上，而同页其他位置都写 $\ol{\FF}_q$ | 原文 $\mathbb{F}_p$ / $\mathbb{F}_q$ 不一致 | 照原文排 $\ol{\FF}_p$（两处：$\Bun^d_{\ol{\FF}_p}\times\Spa(\breve E)^\diamond$ 与 $\mathcal{F}_\varphi\|_{\Bun^d_{\ol{\FF}_p}}$） | 待 Lead 定夺 |
| D8 | p.42 | 「$\mathcal{T}$ 是 $\cO(i)$ 与 $\mathcal{T}$ 之间同构构成的 torsor」 | 自指，应为 $\mathcal{E}$ | 照字面译，`\yizhuw` 说明 | 待 Lead 定夺 |
| D9 | p.46 | 文献表后作者地址 | 非条目的版式内容 | 已按 `\textsc`/`\textit` 排在 `\end{thebibliography}` 后；可整段删 | 待 Lead 决定 |
| D10 | p.46 | [2] "compact unitary **shimura** varieties"、[7] "**langlands**"、[19] "J. Amer. Math. Soc**,**"、[29] "**witt** vector affine **grassmannian**"、[32] "geometric **satake**"、[14] "**l**-packets" | 原文大小写/标点不规范 | 一律照抄，不改正 | 记录 |
| D11 | p.46 | [11][20] 的法文卷名、[12] 作者间用逗号（非 and） | 原文体例不一 | 照抄 | 记录 |
| D12 | 全节 | 原文 $X_*(T)_\Gamma$（p.43）与 $X_*(T)_\Gamma$（p.44，写法相同但上下文作上标） | 记号下标/上标在原文两页间不统一 | 统一照页面图像：两页都印下标 $\Gamma$ | 记录 |

> D12 补充：p.43 的 $\kappa:\mathrm{B}(T)\xrightarrow{\sim}X_*(T)_\Gamma$ 与 $\coprod_{[\mu]\in X_*(T)_\Gamma}$ 经 1400 dpi 复核，$\Gamma$ 均为下标；p.44 的 $[\mu']\in X_*(T)_\Gamma$ 同为下标。

## 5. 新增术语建议

| 原文 | 建议译名 | 依据 |
|---|---|---|
| torsor | torsor（不译，或「主齐性空间」） | 学界通行保留原词；glossary 未收 |
| torsor of isomorphisms | 同构构成的 torsor | 同上的组合用法 |
| crystalline representation | 晶体表示 | 与 glossary「isocrystal=等晶体」配套 |
| admissible (pair) | 可容许（对） | 局部 Langlands 对应通行译法 |
| Weil descent datum | Weil 下降数据 | glossary 有「Weil 群/Weil 限制」，datum 按通译 |
| inertia subgroup | 惯性子群 | 局部类域论通行译法 |
| uniformizing element | 一致化元 | 与 glossary「pseudo-uniformizing element=伪一致化元」一致 |
| Lubin–Tate character | Lubin–Tate 特征 | 与 glossary「Lubin–Tate formal group=Lubin–Tate 形式群」配套 |
| character sheaf property | 特征层性质 | 「character sheaf=特征层」的组合 |
| dual modification | 对偶修正 | 与 glossary「modification=修正」配套 |
| homogeneous space | 齐性空间 | 通行 |
| monodromy | 单值性 | 通行 |
| root of unity | 单位根 | 通行 |
| Artin reciprocity map | Artin 互反映射 | 通行（与「局部类域论」配套） |
| basic (as in basic RZ space) | 基本的 | glossary 已收 |

## 6. 遗留 / 给 Lead 的话

1. `\srcpage` 的可见性依赖 `marginnote`，本机 `_check_g` 里 p.42 / p.43 / p.46 落在页边可见，p.44 / p.45 用的是 `\srcpageinl`（设计如此，行内小号〔p.N〕）。若整书统排后要求全部页边显示，需 Lead 统一处理，我不动 preamble。
2. 文献表与正文分属两个文件；`main.tex` 已按 `s11-abelian` → `s99-bibliography` 顺序 `\input`，整书编译时文献表会另起页，与原文 p.46「§9 末尾紧接 REFERENCES」的版面不同，属全局版式问题。
3. D1–D3、D7、D8 我均未改原文，只加译注/登记；若 Lead 决定改原文，需同步改 `s11-abelian.tex` 对应 5 处（grep `yizhuw` 与 `\ol{\FF}_p` 即可定位）。
