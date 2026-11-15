# BRIEF —— 分工、边界、接续点（Lead 冻结版，2026-11-04）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，保留权利，仅限非商业学术研读，权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 项目根：`<本地路径>`
> 底本：Robert Hines, *Topological K-theory*, 2016-12-15，**10 页**，**PDF 页号 = 印刷页码（偏移 0）**。
> 原文 **0 条编号公式、0 图、0 表、0 脚注、0 习题**；编号定理类：定义 1–8、命题 1–3、引理 1、定理 1–9。

## 1. 分工总表

| 块 | 负责 | 原文页 | 输出文件 | 编号定理类 |
|---|---|---|---|---|
| c00 | Lead | 封面 / 译者说明 / 目录 | `chunks/c00.tex` | — |
| c01a | Lead | **pp.1–2** | `chunks/c01a.tex` | 定义 1、命题 1、定义 2 |
| tr01a | tr-01 | **pp.3–5** | `chunks/tr01a.tex` | 命题 2、定义 3、定义 4、命题 3 |
| tr02a | tr-02 | **pp.6–7** | `chunks/tr02a.tex` | 引理 1、定理 1、定义 5、定义 6、定理 2 |
| tr03a | tr-03 | **p.8** | `chunks/tr03a.tex` | 定理 3、定理 4、定理 5、定理 6 |
| tr03b | tr-03 | **p.9** | `chunks/tr03b.tex` | 定义 7、定理 7、定理 8、定理 9、定义 8 |
| c-refs | Lead | **p.10** | `chunks/c-refs.tex` | —（参考文献 5 条，保留英文原貌） |

## 2. 各块内容提要

- **c01a（pp.1–2）**：标题与摘要段；§1 向量丛的定义（定义 1，两条 bullet：局部乘积、转移映射线性）；
  clutching 函数构造、例（平凡丛 / 切丛与法丛 / $P^1(\C)$ 上的典范丛 $H$）；
  Möbius 丛；直和与张量积及它们的粘合函数；半环 → 虚拟丛；命题 1（半环的 Grothendieck 群构造）+ 证明（含交换三角形）；定义 2（$K(X)$）。
- **tr01a（pp.3–5）**：$K$ 的函子性与拉回；命题 2（同伦不变性）+ 证明（含 $h_0,h_1$ 分段式）；
  $K(S^2)=\Z[H]/(H-1)^2$ 的论证（含 $f(z),g(z)$ 矩阵、$\alpha_t$ 路径）；约化 $K$ 理论 $\tilde K$；
  §2 分类空间：定义 3（Grassmann 流形 $G_n(\C^N)$、典范丛 $E_n$）、胞腔结构（含大矩阵）、定义 4（$BU_n, BU$）、
  命题 3（$[X,BU_n]\leftrightarrow$ 秩 $n$ 丛）+ 证明（含交换图、Surjectivity bullet）。
- **tr02a（pp.6–7）**：命题 3 证明续（Injectivity、$A_t,B_t$ 同伦）；$\hat K(X)$ 分裂；引理 1 + 证明；定理 1 + 证明；
  §3 广义上同调：定义 5（可加约化上同调理论）、定义 6（$\Omega$-预谱）、定理 2（预谱 ↔ 上同调理论）。
- **tr03a（p.8）**：**定理 3（Bott 周期性：$\Omega^2BU\simeq BU\times\Z$）**、由 $E_{2n}=BU\times\Z$、$E_{2n+1}=\Omega BU$ 得 $\tilde K^n$；
  §3.1 另一版本的 Bott 周期性（外积，定理 4、定理 5）；§4 一个应用（定理 6：$H$-空间只有 $S^0,S^1,S^3,S^7$）。
- **tr03b（p.9）**：定义 7（Adams 运算）+ 4 条性质；定理 7（分裂原理）；§5 其他版本：§5.1 实 $K$ 理论（定理 8、周期 8）；
  §5.2 代数 $K$ 理论（定理 9 Swan、定义 8（$K_0(R)$、$\tilde K_0(R)$）、类群例子）。
- **c-refs（p.10）**：`References` 5 条（[Bott] [VBKT] [AGP] [K] [May]），英文原貌。

**注意**：原文每节标题使用 `\section{}`，**只有下面列出的块写对应标题**，其他块不要写。

## 3. 标题归属（谁写哪个 `\section`/`\subsection`）

| 标题 | 原文页 | 归属 |
|---|---|---|
| `\section{向量丛与 $K(X)$}` | p.1 | c01a |
| `\section{向量丛的分类}` | p.4 | tr01a |
| `\section{Bott 周期性与作为广义上同调理论的 $K$ 理论}` | p.7 | tr02a |
| `\subsection{另一版本的 Bott 周期性}` | p.8 | tr03a |
| `\section{$K$ 理论的一个应用}` | p.8 | tr03a |
| `\section{$K$ 理论的其他版本}` | p.9 | tr03b |
| `\subsection{实 $K$ 理论}` | p.9 | tr03b |
| `\subsection{代数 $K$ 理论}` | p.9 | tr03b |

## 4. 边界锚点（跨页句「开始者写完」）

| 交界 | 上一块的最后一句（英文锚点） | 下一块的第一句（英文锚点） |
|---|---|---|
| c01a → tr01a | Definition 2 末："…the real *K*-theory of $X$, denoted by $KO(X)$.]" | "K-theory is functorial in $X$ as follows. Given $X\xrightarrow{f}Y$ and a vector bundle $E\xrightarrow{p}Y$, we have the pullback $f^*E\xrightarrow{q}X$," |
| tr01a → tr02a | p.5 末 bullet："Putting these together gives a map $g:E\to(\C^n)^m\subseteq\C^\infty$ that is a linear injection on each fiber." | p.6 首："[Injectivity.] If $E\cong f_0^*E_n(\C^\infty)$, $f_1^*E_n(\C^\infty)$, let $g_0,g_1:E\to\C^\infty$ be maps which are linear injections on each fiber $p^{-1}(x)$ …" |
| tr02a → tr02b | p.7 末："…determines an $\Omega$-prespectrum $\{E_n\}_{n\in\Z}$ such that $\tilde E^n=[X,E_n]$." | p.8 首："**Theorem 3** (Bott periodicity…). There is a homotopy equivalence $\Omega^2BU\simeq BU\times\Z$." |
| tr02b → tr03a | p.8 末："…coming from the algebra structure on the norm one elements of $\R,\C,\H$, and $\mathbb{O}$." | p.9 首："The proof uses the existence of the Adams operations in $K$-theory and the splitting principle." |
| tr03a → c-refs | p.9 末："There are definitions for higher $K$-groups, but we will not discuss them here." | p.10："References"（Lead 自动转录） |

**p4→p5 的跨页句**（同一块内，tr-01 自行处理）：
p4 末 "By introducing a column" + p5 首 "of zeros, we have a subcomplex $G_n(\C^N)\subseteq G_n(\C^{N+1})$."

## 5. 再强调三条

1. 原文**没有编号公式**：不要写 `\tag`、不要用 `equation` 编号；展示式一律 `\[ … \]`。
2. 编号定理类**手工给号**，号数照原文（见 §1 表），不得重排、不得缺号；相邻块之间号数必须接上。
3. 展示式一律重排（矩阵 `pmatrix`、分段 `cases`、交换图 `tikzcd`）；**不要截图**，也不需要编译（Lead 统一编译）。
