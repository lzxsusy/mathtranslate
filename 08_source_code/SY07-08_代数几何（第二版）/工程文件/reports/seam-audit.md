# 接缝审计（seam audit）

审计对象：`源码/main.tex` 实际拼装的 20 个块（c01a→c19；c20 不在 main.tex 内）之间的 **19 个接缝**。
方法：逐块取首 / 末段（`工程文件/work/_seam_dump.txt` 每块首末 16 行），再对照 `工程文件/work/en/pNNN.txt` 的 OCR 原文与 `工程文件/pages/pNNN.png` 页图像，核对「上块末页 + 下块首页」是否连续；另整读 p026、p037、p066、p098、p155、p174、p187、p202、p216、p217、p229、p230 及空白页 p123。
判定规则按 BRIEF §57–59：「一个段落／一个编号条目整体归属于它**起始页**所在的块」；下块不得重译上块后半截，上块须把跨页的段落／条目译完。

**结论：19 个接缝中 17 处通，2 处必须修（1 处丢 2 条完整习题，1 处习题被截断丢 4 个子项），无重复翻译。**

| 接缝（A\|B） | A 末页 / B 首页（原书页） | 结论 | 证据（原书原文 ↔ 译文） |
|---|---|---|---|
| c01a\|c01b | p.4 / p.5（PDF 11\|12） | 通 | p.11 末 "If a" → p.12 "morphism is both injective and surjective, we say it is bijective. … But a bijective morphism may not be an isomorphism."；c01a 末「…若态射既单又满，则称它为双射。…但双射态射未必是同构。」；c01b 首「设 $A_i$（$i\in I$）是 $\sC$ 中一族对象」↔ p.12 "Let $A_i$ ($i\in I$) be a family of objects in $\mathcal C$." |
| c01b\|c02 | p.9 / p.10（16\|17） | 通 | p.9 末 "Note that the category of abelian groups is an abelian category. We leave to the reader to prove the following proposition." ↔ c01b 末「注意交换群范畴是阿贝尔范畴。我们把以下命题的证明留给读者。」；p.10 首 "Proposition 1.1.4." ↔ c02 首「命题 1.1.4」 |
| **c02\|c03** | p.18 / p.19（25\|26） | **丢句（丢 2 条完整习题）** | 原书 p.19 顶部有 §1.1 习题 9、10：*"9. Let $u\colon\mathcal C\to\mathcal D$ be a functor. Suppose that for each object $D\in\mathrm{ob}\,\mathcal C$, the functor $\mathcal C\to(\mathrm{Sets})$, $C\mapsto\Hom(u(C),D)$ is representable by an object $v(D)\in\mathrm{ob}\,\mathcal C$. Then $v\colon\mathcal D\to\mathcal C$ is a functor right adjoint to $u$."*、*"10. … faithful (resp. fully faithful) … essentially surjective … equivalence of categories … quasi-inverse of $u$."*，其后才是 "1.2 Schemes and Morphisms"。译文：c02 末条为 `\label{ex:1.1.8}`（p.18 末），c03 首行即 `\subsection{概形与态射}`；两文件均无对应文字（grep「忠实／本质满／准逆／右伴随于」在 c02、c03 无命中，c02.tex:182 仅为正文）。 |
| c03\|c04 | p.29 / p.30（36\|37） | 通 | p.30 末 §1.2 习题 7 "Let $A=R[x_1,\dots,x_n]$ … Prove that $\phi$ induces an isomorphism $\operatorname{Proj}S\cong\operatorname{Proj}A[y_1,\dots,y_n]/J$" ↔ c03 末 `ex:1.2.7`（§1.2 共 7 题，全译）；p.30 下半 "1.3 Properties of Schemes and Morphisms" ↔ c04 首「命题 1.3.1」 |
| c04\|c05 | p.44 / p.45（51\|52） | 通 | p.44 末 "… Hence $V(\ker\varphi)\subset\overline{f(\Spec B)}$"（第二证明未完）→ p.45 "Let's prove the claim. $\fp'/\ker\varphi$ is a minimal prime ideal …"；c04 把该证明（含第三证明）译至 `\end{proof}`；c05 首「命题 1.3.18」 |
| c05\|c06 | p.58 / p.59（65\|66） | 通 | p.59 顶部 "be a commutative diagram in $\mathcal C$. …" 是习题 7 的续文，c05 的 `ex:1.3.7` 已收（「证明第一个图表在 $\cC$ 中是笛卡尔图…」）；p.59 末 "1.4 Coherent Sheaves" ↔ c06 首「1.4 凝聚层」 |
| c06\|c07 | p.74 / p.75（81\|82） | 通 | p.74 末命题 1.4.13 陈述；p.75 为其证明；c06 译完 `\end{proof}`；c07 首「设 $X$ 是环层空间，$\cF$ 是 $\cO_X$-模。定义 $\cF$ 的支集…」↔ p.75 "Let $X$ be a ringed space and $\cF$ an $\cO_X$-module. We define the support of $\cF$" |
| c07\|c08 | p.90 / p.91（97\|98） | 通 | p.90 末习题 3(3)(4)、习题 4 爆破 (1)；p.91 有 4(2)、5（向量丛）、6（整闭包／正规化）；c07 末含 5、6 两题后 `\end{exercises}`；c08 首「本节的主要内容只在本书的最后一节用到。」↔ p.91 "The main part of this section is used only in the last section of this book." |
| c08\|c09 | p.103 / p.104（110\|111） | 通 | p.103 末 "is the canonical morphism. The following diagram commutes:"；c08 末「…是典范态射。下图交换：［图］」；p.104 首 "For every $\cO_X$-module $\cF$, we define the formal completion …" ↔ c09 首「对每个 $\cO_X$-模 $\cF$，定义 $\cF$ 关于 $\cI$ 的形式完全化…」。（c08 末条译注贴在接缝前，排版略挤，非丢句） |
| c09\|c10 | p.116 / p.117（122\|123\|124） | 通 | p.116 是**空白页**（`pages/p123.png` 全页仅 27 个暗像素；书版式：第 1 章止于 p.115，第 2 章自 p.117 右页起，p.116 留白）；c09 末 `ex:1.5.2` 第 (6) 项「……在 $IA[t]$-进拓扑下收敛到 $0$，当且仅当……且关于 $n$ 一致」↔ p.115 "(6) … converges to $0$ … uniformly in $n$"，随后 `\end{exercises}`；p.117 首 "Chapter 2 / Cohomology / 2.1 Derived Functors" ↔ c10 首 `\section{上同调}` + `\subsection{导出函子}` |
| c10\|c11 | p.132 / p.133（139\|140） | 通 | p.132 末 "If no such $i-1$ exists, we" → p.133 "define $Z_i(F)=\varinjlim_{j<i}Z_j(F)$ … Let $n$ be the smallest element …"；c10 把 2.1.6 的证明（含极限情形与基数论证）译完并 `\end{proof}`；c11 首「设 $(X,\cO_X)$ 是环层空间。由 \ref{it:2.1.6}……下面是一些例子。」↔ p.133 "Let $(X,\cO_X)$ be a ringed space. By 2.1.6 …" |
| c11\|c12 | p.148 / p.149（155\|156） | 通 | p.148 末 §2.1 习题 3、4；c11 有 `ex:2.1.1`–`ex:2.1.4` 后 `\end{exercises}`（§2.1 共 4 题）；p.149 首 "2.2 Spectral Sequences" ↔ c12 首 `\subsection{谱序列}` |
| c12\|c13 | p.161 **同页**（168） | 通 | 接缝在同一页中段：c12 末「这给出了谱序列的另一种构造。细节留给读者。」↔ p.161 上半 "This provides another construction of the spectral sequence. We leave the details to the reader."；c13 首「命题 2.2.7」↔ 同页 "Proposition 2.2.7"（p.168 OCR 显示 2.2.7 及其证明都在该页） |
| c13\|c14 | p.167 / p.168（174\|175） | 通 | p.167 末 §2.2 习题 4 的 (1)(2)(3)（奇异同调谱序列）↔ c13 末 `ex:2.2.4` 全译（§2.2 共 4 题）；p.168 首 "2.3 Cech Cohomology" ↔ c14 首 `\subsection{\v{C}ech 上同调}` |
| c14\|c15 | p.180 / p.181（187\|188） | 通 | p.180 末 习题 2 的 (9)(10)(11) + 习题 3 开头 "Let $X$ be a noetherian integral scheme and let $\eta$ be the generic point … (For example, $X$ is a smooth algebraic" → p.181 "curve.) Let $v_P\colon K^*\to\bZ$ …"；c14.tex:594–617 的 `ex:2.3.3` 全译（「（例如 $X$ 是光滑代数曲线。）设 $v_P\colon K^{*}\to\bZ$……」，并含 (1)(2) 及「$\mathrm{Cl}(X)\cong\mathrm{CaCl}(X)$」）；c15 首 `\subsection{仿射概形与射影概形的上同调}` |
| **c15\|c16** | p.194 / p.195（201\|202） | **缺半句／丢内容（习题被截断）** | 原书 p.195 顶部是 §2.4 **习题 3 的 (1)–(4)**：*"(1) Prove that the complex … is isomorphic to the Koszul complex $K(\xi,\partial/\partial t_i;R)$. (2) Prove that $(\theta d+df\wedge)^2(\omega)=0$ … (3) Let $F$ be the filtration … $E_1^{pq}=H^{p+q}(\Omega^\cdot,df\wedge)\Rightarrow H^{p+q}(\Omega^\cdot[\theta],\theta d+df\wedge)$ … (4) Let $K^{pq}=\Omega^p\Omega^{q+1}[\theta]$, $d_1=df\wedge$, $d_2=(-1)^p\theta d$ … Describe another spectral sequence of this bicomplex."* 译文：c15 末止于「$\mathrm d\colon\Omega^k\to\Omega^{k+1}$ 是外微分」及其公式，随后直接 `\end{exercises}\endgroup`——上述 (1)–(4) 与 "The canonical morphism … can be identified with …" 整段缺失（c15、c16 均无对应文字）。c16 头注释已注明「p.202 顶部为 §2.4 习题续文（属 c15），按接缝规则跳过」，即本应由 c15 收尾。 |
| c16\|c17 | p.209 / p.210（216\|217） | 通 | p.209 末 "By 1.3.25 (i)," → p.210 "$\cO_X(U_1\cap U_2)$ is affine, and as an $\cO_Y(V)$-algebra, … So we have $x_1=x_2=x$ and hence $f$ is injective. □"；c16 末「…故 $x_1=x_2=x$，从而 $f$ 是单射。`\end{proof}`」+ 译注（依据 p.209 命题 2.5.15）；p.210 下半 "2.6 Local Freeness of Higher Direct Images" ↔ c17 首 `\subsection{高阶直接像的局部自由性}` |
| c17\|c18 | p.222 / p.223（229\|230） | 通 | p.222 末 推论 2.6.10 证明 (i)；p.223 首 "(ii) By (i), … (iii) We know $H^i(X_y,\cF_y)=0$ …"；c17 末含 (i)(ii)(iii) 至「$H^{i-1}(X_y,\cF_y)\cong(R^{i-1}f_*\cF)_y\tensor_{\cO_{Y,y}}k(y)=0$」+ `\end{proof}` + 译注；p.223 下半 "2.7 Grothendieck's Existence Theorem" ↔ c18 首 |
| c18\|c19 | p.235 / p.236（242\|243） | 通 | p.235 末 引理 2.7.13 陈述 + 证明开头；p.236 "So $\Ext^1$ … By 2.1.15 … Lemma 2.7.14. Let $u\colon\cF\to\cG$ …"；c18 译完 2.7.13 的证明；c19 首「引理 2.7.14」↔ "Lemma 2.7.14" |

## 必须修的 2 处

1. **c02\|c03（原书 p.19 顶部）——丢了 §1.1 习题 9、10（2 条完整习题，含「忠实／本质满／范畴等价／准逆」整段定义）**
   - 定位：c02 的 `\end{exercises}` 之前（或 c03 首行 `\subsection{概形与态射}` 之前，二者取一，按「条目归起始页」应由 c03 补；建议由 c02 补以保持习题环境完整）。
   - 首句片段：`\item \label{ex:1.1.9} 设 $u\colon\cC\to\cD$ 是函子。假设对每个对象 $D\in\ob\cC$，函子 $\cC\to(\mathrm{Sets})$，$C\mapsto\Hom(u(C),D)$ 可由某个对象 $v(D)\in\ob\cC$ 表示。则 $v\colon\cD\to\cC$ 是 $u$ 的右伴随函子。`
   - 末句片段：`……这个函子称为 $u$ 的\emph{准逆}。`（原文 "It is called a quasi-inverse of $u$."）
   - 原文全文见 `工程文件/work/en/p026.txt` 第 2–16 行。

2. **c15 末页截断（原书 p.195 顶部）——§2.4 习题 3 的 (1)–(4) 缺失，文件在题干中间就 `\end{exercises}`**
   - 定位：c15 习题 3 题干（`\mathrm d` 的外微分公式）之后、`\end{exercises}` 之前。
   - 首句片段：`(1) 证明复形 $R\to(\Omega^\cdot,\mathrm d f\wedge)$ …… 同构于 Koszul 复形 $K(\xi,\partial/\partial t_i;R)$。`
   - 末句片段：`(4) ……描述该双复形的另一个谱序列。`
   - 原文全文见 `工程文件/work/en/p202.txt` 第 2–21 行（p.195 页图像 `工程文件/pages/p202.png` 顶部）。

## 顺带发现（非接缝问题，供 Lead 取舍）

- **c16.tex 并未损坏**：先前 `_seam_dump.txt` 里出现的乱码是 PowerShell 控制台编码造成的显示现象，用 `read` 工具／UTF-8 解码读出的正文完好（文件头注释、`\subsection{固有态射的上同调研究}`、定理 2.5.1 均正常）。审计期间该文件行数由 577 变为 581，说明仍在改动。
- **c17.tex 在我开始审计时不存在，审计中途出现**（现 589 行，末为推论 2.6.10 的证明 + 译注，无 `%EOF` 结束标记）。c16\|c17、c17\|c18 两处已按其当时内容核对为通；若 c17 仍在校改，定稿后建议复扫其首末段。
- **c15.tex 首行带 UTF-8 BOM**（`% c15 原书 p.181–194`），其余块无 BOM，BRIEF 要求无 BOM，建议去掉。
- **c07.tex 的 §1.4 六条习题全部没有 `\label{ex:1.4.N}`**（c07 内 `label{ex:` 计数 0），影响交叉引用与习题编号核对；其余带习题的块 c02(8)、c03(7)、c05(8)、c09(2)、c11(4)、c13(4)、c14(3)、c15(3) 均已加 label。
- **c16 无 exercises 环境属正常**（§2.5 无习题，p.209/210 之间直接进 §2.6）；c04／c06／c08／c10／c12／c18 无 exercises 环境亦与各自页范围相符。
- 章节标题归属全部正确：`\subsection`（及 c10 的 `\section{上同调}`）只出现在起始块，分布与 `work/chunks.tsv` 的 `new_subsection` 一致（c01a、c03、c04、c06、c08、c10、c12、c14、c15、c16、c17、c18），无重复标题、无跨块重写标题。
- c19 末条译注已声明「原书 p.246 在 2.7.21 的证明后即止，§2.7 没有配习题」，与 p.253 页图像一致，故 c19 之后接 `refs.tex` 无接缝问题。

## 已修补记录（2026-11-14，tr-ch1a 执行，按 Lead 指示由审计人直接补）

「必须修的 2 处」现已全部修补；两处内容均逐符号对页图像核对（未使用 OCR 公式）。

### 1. c02 补 §1.1 习题 9、10

- **依据页**：`工程文件/pages/p026.png` 上部（原书 p.19），3–6 倍裁切逐句核读。
- **补入位置**：`源码/chunks/c02.tex` 末条习题 `ex:1.1.8` 之后、`\end{exercises}` 之前。
- **补入内容**：
  - `\item \label{ex:1.1.9}`：右伴随函子判据——「设 $u\colon\cC\to\cD$ 是函子。假设对每个对象 $D\in\ob\cC$，函子 $\cC\to(\mathrm{Sets})$，$C\mapsto\Hom(u(C),D)$ 可由某个对象 $v(D)\in\ob\cC$ 表出。则 $v\colon\cD\to\cC$ 是 $u$ 的右伴随函子。」
  - `\item \label{ex:1.1.10}`：忠实／全忠实／本质满／范畴等价／准逆的整段定义与结论（`\emph` 标注术语；无新增 `\idx`，术语在本书首次出现处另行登记）。
  - 1 条译注：原书习题 10 中「对任意对象 $D\in\ob\cC$」与随后「$v(D)\in\ob\cC$ 使 $uv(D)\cong D$」不合（因 $u\colon\cC\to\cD$，$D$ 应属 $\cD$），疑为笔误（应作 $D\in\ob\cD$）；译文照原书印法照录。[依据：原书 p.19 习题 10]
- **习题数**：8 → 10（编号自然接成 9、10，未改任何既有 `\label`）。
- **编译**：`cd 源码; xelatex -interaction=nonstopmode _check_c02.tex` → EXIT=0，**8 页**，日志无 `!`、无 Overfull/Underfull（仅 `it:1.1.1` 未定义，属 c01a 定义、跨块自检的正常现象）。

### 2. c15 补 §2.4 习题 3 的 (1)–(4)

- **依据页**：`工程文件/pages/p202.png` 上部（原书 p.195）+ `工程文件/pages/p201.png` 底部（原书 p.194，习题 3 题干，用于确认 $R=\bC[t_1,\dots,t_n]$ 的设定）。
- **补入位置**：`源码/chunks/c15.tex` 习题 3 的外微分公式之后、`\end{exercises}` 之前；`\endgroup` 保持在 `\end{exercises}` 之后未动，`\subsection` 未动。
- **补入内容**（按图像，非 OCR）：
  - (1) 复形 $\cdots\to\Omega^k\xrightarrow{\mathrm{d}f\wedge}\Omega^{k+1}\to\cdots$ 同构于 Koszul 复形 $K^{\cdot}\bigl(\frac{\partial f}{\partial t_1},\dots,\frac{\partial f}{\partial t_n};R\bigr)$；
  - (2) 对一切 $\omega\in\Omega^{\cdot}[\theta]$ 有 $(\theta\mathrm{d}+\mathrm{d}f\wedge)^2(\omega)=0$，从而 $(\Omega^{\cdot}[\theta],\theta\mathrm{d}+\mathrm{d}f\wedge)$ 是复形；
  - (3) 滤过 $F^p=\theta^p\Omega^{\cdot}_{\mathbb G_m^n/\mathbb C}[\theta]$、$F^p/F^{p+1}\cong(\Omega^{\cdot},\mathrm{d}f\wedge)$、谱序列 $E_1^{pq}=H^{p+q}(\Omega^{\cdot},\mathrm{d}f\wedge)\Rightarrow H^{p+q}(\Omega^n[\theta],\theta\mathrm{d}+\mathrm{d}f\wedge)$，以及「典范态射 $d_1^{pq}\colon E_1^{pq}\to E_1^{p+1,q}$ 等同于 $H^{p+q}(\Omega^{\cdot},\mathrm{d}f\wedge)\to H^{p+q+1}(\Omega^{\cdot},\mathrm{d}f\wedge)$，$[\omega]\mapsto[\mathrm{d}\omega]$」；
  - (4) $K^{pq}=\theta^p\Omega^{p+q}$、$d_1=\mathrm{d}f\wedge$、$d_2=(-1)^p\theta\mathrm{d}$ 的双复形与另一谱序列。
  - 1 条译注：原书 (3) 两处记号照录——$F^p$ 的下标印作 $\mathbb G_m^n/\mathbb C$（与本题由 $R=\bC[t_1,\dots,t_n]$ 定义的 $\Omega^{\cdot}$ 不合）、谱序列右端印作 $\Omega^n[\theta]$（据 (2) 与同段应为 $\Omega^{\cdot}[\theta]$），读者按 $\Omega^{\cdot}[\theta]$ 理解。[依据：原书 p.194 习题 3 开头、p.195 (2)(3)]
- **与原表格转录的差异（重要）**：上表 c15\|c16 行引用的原文片段来自 OCR，其中记号有误——OCR 作 `K(ξ,∂/∂t_i;R)`、`K^{pq}=Ω^pΩ^{q+1}[θ]`、`d_1=df∧`、`d_2=(-1)^pθd`；页图像实际印作 $K^{\cdot}(\frac{\partial f}{\partial t_1},\dots,\frac{\partial f}{\partial t_n};R)$、$K^{pq}=\theta^p\Omega^{p+q}$、$d_1=\mathrm{d}f\wedge$、$d_2=(-1)^p\theta\mathrm{d}$，补译以页图像为准。
- **编译**：`cd 源码; xelatex -interaction=nonstopmode _check_c15.tex` → EXIT=0，**13 页**（补前 12 页），日志无 `!`、无 Overfull/Underfull。

### 3. 修补后的接缝状态

- c02\|c03：由「丢句」改为**通**（§1.1 共 10 题，c02 全覆盖；c03 仍从 §1.2 起，无重复）。
- c15\|c16：由「缺半句／丢内容」改为**通**（§2.4 习题 3 完整，(1)–(4) 齐全；c16 首仍从 §2.5 起）。
- c16\|c17、c17\|c18 两处仍按审计当时的 c16/c17 内容判「通」；c16/c17 定稿后建议再复扫一次首末段（尤其 c17 是否补上 `%EOF` 与最终行数）。
