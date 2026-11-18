# 第 I 章（chap1.tex）校订日志

- 译文：`C:\Users\admin\Downloads\Dmod_work\src\D-modules-zh\chapters\chap1.tex`（校订后 1935 行）
- 原文：`C:\Users\admin\Downloads\Dmod_work\en_pages\p007.txt`–`p060.txt`（PDF 页 = 印刷页 + 6）
- 范围：§1–§13 全部条目（定理/命题/引理/推论/例/注）的陈述与证明逐句对读，展示公式逐符号核对；术语按《校订方案》§4 统一。
- 编号体系为 LaTeX 计数器给出的「节.序号」，未加任何 `\label`、未手写编号；改后各节条目序与原文一致（§1 7、§2 11、§3 10、§4 8、§5 14、§6 4、§7 13、§8 7、§9 8、§10 10、§11 7、§12 6、§13 6），故自动编号等于原书编号。

## 一、漏译补译（印刷 p.43–46）

| 位置 | 原文（英文，截 60 字内） | 原译 | 改为 | 理由 | 级别 |
|---|---|---|---|---|---|
| chap1.tex:1516 / p.43 | Now we consider two simple examples | （缺；1516 行原直接接 `\section{正像}`） | `现在考虑两个简单的例子。首先设 $p$ 是 $X\times Y$ 到 $Y$ 的投影……` + `$$p^+(N)=R(X)\boxtimesext N.$$` | 整段漏译 | P1 |
| chap1.tex:1522 / p.43 | 10.5. Proposition. Let p : X × Y −→ Y be the canonical projection | （缺） | `\begin{proposition}`：`(i) $p^+$ 是从 $\mathcal{M}^L(D_Y)$ 到 $\mathcal{M}^L(D_{X\times Y})$ 的正合函子；`…`(iv) 对任意有限生成左 $D_Y$-模 $N$，$d(p^+(N))=d(N)+n$。` + `特别地，有限生成左 $D_Y$-模 $N$ 是完整的当且仅当 $p^+(N)$ 是完整的。` | 10.5 整条漏译（4 项 + In particular） | P1 |
| chap1.tex:1533 / p.43 | Now consider the other example. Let i be the canonical injection | （缺） | `$$D_{X\to X\times Y}=i^*(D_{X\times Y})=R(X)\otimes_{R(X)\boxtimesext R(Y)}(D_X\boxtimesext D_Y)=D_X\boxtimesext D_Y/\bigl((y_1,y_2,\dots,y_m)D_Y\bigr),$$` + `$$0\longrightarrow D_Y\xrightarrow{\ y_1\ }D_Y\longrightarrow D_Y/y_1D_Y\longrightarrow 0,$$` + `$$0\longrightarrow D_{X\times Y}\xrightarrow{\ y_1\ }D_{X\times Y}\longrightarrow D_{X\to X\times Y}\longrightarrow 0.$$` + `$$0\longrightarrow N\xrightarrow{\ y_1\ }N\longrightarrow 0$$` | 该例及导出逆像的复形漏译 | P1 |
| chap1.tex:1545 / p.43 | 10.6. Lemma. … (i) i+(N) = coker y1 … In particular, the left cohomological dimension of i+ is ≤ 1 | （缺） | `(i) $i^+(N)=\operatorname{coker}y_1$；` `(ii) $L^{-1}i^+(N)=\ker y_1$；` `(iii) 对 $p\ne0,-1$ 有 $L^pi^+(N)=0$。` + `特别地，$i^+$ 的左同调维数 $\le1$。` | 10.6 整条漏译（3 项 + In particular） | P1 |
| chap1.tex:1557 / p.43–44 | The last statement has an obvious generalization for arbitrary Y | （缺） | `最后一句对任意 $Y$ 有显然的推广。` + `\begin{lemma}` `设 $i:X\longrightarrow X\times Y$ 是典范浸入。则 $i^+$ 的左同调维数 $\le\dim Y$。` + 证明（对 $\dim Y$ 归纳，$i=j\circ i'$，用 10.6 与 10.3.(ii) 的谱序列） | 10.7 整条（含证明）漏译 | P1 |
| chap1.tex:1560 / p.44–45 | Now let F : X −→ X be an isomorphism … α(f) = f ◦ F … | （缺） | `现在设 $F:X\longrightarrow X$ 是 $X$ 的同构`…`$$\tilde\beta(T)(f)=\beta\bigl(T\alpha(f)\bigr)$$`…`$$\beta(\partial_i)(f)=\beta\Bigl(\sum_{j=1}^n\bigl((\partial_jf)\circ F\bigr)\partial_iF_j\Bigr)=\sum_{j=1}^n\bigl((\partial_iF_j)\circ G\bigr)\partial_jf$$`…`$$\varphi\bigl(\partial_i(1\otimes T)\bigr)=\sum_{j=1}^n\beta(\partial_iF_j)\partial_jT=\beta(\partial_i)\varphi(1\otimes T).$$` | 同构情形的 $\tilde\beta$、$\beta(\partial_i)$、$\varphi$ 计算整段漏译 | P1 |
| chap1.tex:1592 / p.45 | 10.8. Lemma. Let F : X −→ X be an isomorphism … | （缺） | `\begin{lemma}`：`(i)`…`(iii) 函子 $F^+$ 把有限生成 $D_X$-模映为有限生成 $D_X$-模。若 $M$ 是有限生成 $D_X$-模，则 $d(F^+(M))=d(M)$。` + `特别地，$F^+$ 把完整模映为完整模。` | 10.8 整条漏译（3 项 + In particular） | P1 |
| chap1.tex:1610 / p.45 | 10.9. Lemma. Ch(F +(M )) = γ(Ch(M )) | （缺） | `\begin{lemma}` `设 $M$ 是有限生成 $D_X$-模。则` `$$\operatorname{Ch}(F^+(M))=\gamma(\operatorname{Ch}(M)).$$`（前有 $\gamma(x,\xi)=\bigl(G(x),T_{G(x)}(F)^*\xi\bigr)$ 与 $(\Gr\beta)(P)=P\circ\gamma$ 两段） | 10.9 整条漏译 | P1 |
| chap1.tex:1617 / p.46 | 10.10. Theorem. Let F : X −→ Y be a polynomial map … ≤ dim Y | （缺） | `\begin{theorem}` `则 $F^+$ 的左同调维数 $\le\dim Y$。` + 证明：`为证明此陈述，我们使用图像构造。`…`$F=p\circ\Phi\circ i$`…`由 10.3，$F^+=i^+\circ\Phi^+\circ p^+$。`…`由 10.7 断定，当 $q<-\dim Y$ 时 $L^qF^+=0$。` | 10.10 整条（含图像构造证明）漏译；补后 §10 恰为 10 条 | P1 |

## 二、公式与符号（P1）

| 位置 | 原文（英文，截 60 字内） | 原译 | 改为 | 理由 | 级别 |
|---|---|---|---|---|---|
| chap1.tex:1461 / p.47 | H i (For(F +(F i ))) = H i (F ∗ (For F i )) | `H^i(F^*(\operatorname{For}F^i))` | `H^i(F^*(\operatorname{For}F^\cdot))` | 左分解在文中记作 $F^\cdot$（chap1.tex:1453），原译把复形下标抄成了上标 | P1 |
| chap1.tex:1812 / p.50 | sum over j=1..q | `\sum_{j=1}^j[x_n,\partial_n^j]m_j` | `\sum_{j=1}^q[x_n,\partial_n^j]m_j` | 求和上限误作被加项指标 $j$ | P1 |
| chap1.tex:1873 / p.52 | By 10.5, we know that p+ is exact | `由 10.5 知 $p_+$ 是正合的` | `由 10.5 知 $p^+$ 是正合的` | 10.5 陈述的是逆像 $p^+$ 正合（11.3 才是 $i_+$） | P1 |
| chap1.tex:1875 / p.52 | it remains to study the derived functors of i+ and p+ | `$i_+$ 和 $p_+$ 的导出函子` | `$i^+$ 和 $p_+$ 的导出函子` | 下文 13.1–13.2 讨论的正是 $i^+$（13.4 才是 $p_+$） | P1 |
| chap1.tex:1784, 1790, 1831, 1848, 1853, 1878, 1881, 1884, 1890, 1891, 1892, 1900, 1903, 1905, 1906 / p.49–53 | i+(M ) = M1 , L−1 i+(M ) = M0 …（原文上下标在 pdftotext 中一律显示为 “i+”） | 逆像处一律作 `$i_+$`（共 33 处） | 改为 `$i^+$`（如 `$i^+(M)=M_1$，$L^{-1}i^+(M)=M_0$`、`$i^+(\Gamma_{[X]}(N))=0$`、`$i^+(N)\cong L^{-1}i^+(L)$`） | 值域为 $\mathcal{M}(D_Y)$、且原文自称 inverse images，可判定是逆像；直像处（`$i_+(M_0)$`、`$i_+(N_j)$`、Kashiwara 定理中的「直像函子 $i_+$」等）保留不变 | P1 |

## 三、术语统一（P2）

| 位置 | 原文（英文，截 60 字内） | 原译 | 改为 | 理由 | 级别 |
|---|---|---|---|---|---|
| chap1.tex:1135 / p.38 | 8. Holonomic modules | `\section{Holonomic 模}` | `\section{完整模}` | 术语表：holonomic → 完整 | P2 |
| chap1.tex:1860 / p.51 | 13. Preservation of holonomicity | `\section{Holonomic 性的保持}` | `\section{完整性的保持}` | 同上 | P2 |
| chap1.tex:1139 / p.38 | we call it holonomic | `则称它是\emph{holonomic 的}` | `则称它是\emph{完整（holonomic）的}` | 章内首次出现，按方案括注英文 | P2 |
| chap1.tex:1141–1934（约 50 处）/ p.38–53 | holonomic module / holonomic DX -module | `holonomic 模`、`holonomic 的`、`holonomic 性` | `完整模`、`完整的`、`完整性` | 全章统一（grep 复核：全文仅余 1139 行一处括注） | P2 |
| chap1.tex:1629, 1631, 1635, 1654, 1668, 1696, 1728, 1744, 1853, 1862, 1864, 1915 / p.46–53 | direct image | `正像` | `直像` | 术语表：direct image → 直像（共 12 处；grep 复核全文无「正像」） | P2 |
| chap1.tex:1147–1148 / p.38 | holonomic modules have finite length | `\item完整模具有有限长度；` | `\item 完整模具有有限长度；` | 统一替换时丢掉了 `\item` 后的空格（同 1148 行） | P2 |

## 四、原文笔误（按方案登记，不改动译文）

| 位置 | 原文（英文，截 60 字内） | 原译 | 改为 | 理由 | 级别 |
|---|---|---|---|---|---|
| 英文 p.23 / §5.3 证明 | 证明末段标号 (iv) | 未标号（已并入 (iii) 段） | — | 5.3 只有 (i)–(iii)，原文标号笔误 | 原文笔误 |
| 英文 p.28 / §5.14 后 | this ends the proof of 4.6 | `这也结束了 5.6 的证明` | — | 原文把 5.6 误作 4.6，译文已按实际条目写 5.6 | 原文笔误 |
| 英文 p.38 / 例 8.2 | π is a bijection of Ch(On ) onto O | `$\pi$ 是 $\operatorname{Ch}(\mathcal{O}_n)$ 到 $\mathcal{O}$ 上的双射` | — | 原文 “onto O” 本身笔误（应为 onto $k^n$），译文照原文 | 原文笔误 |
| 英文 p.49 / 10.5(iv) | d(p+(N )) = d(M ) + n | `$d(p^+(N))=d(N)+n$` | — | 原文误用 $M$，译文按本意写 $N$，保留 | 原文笔误 |
| 英文 p.50 | β(TS) = β(T )β(S) 同一行重复；ω(T ) ∈ DX | `$\tilde\beta(T)\in D_X$` | — | 原文重复一行、且把 $\tilde\beta$ 误作 $\omega$，译文只保留一次并写 $\tilde\beta$ | 原文笔误 |
| 英文 p.54 / 11.5 | the canonical injection of X × Y onto Y | `$p$ 是 $X\times Y$ 到 $Y$ 的典范投影` | — | 原文 “injection … onto” 应为 projection，译文用「投影」正确 | 原文笔误 |
| 英文 p.54 / 11.5 证明 | Lq p+(M ) = 0 for q < − dim X | `对 $q<-\dim X$ 有 $L^q p_+(M)=0$` | — | 原文该式漏写 $0$，译文补全 | 原文笔误 |
| 英文 p.56 / 11.4(ii)(iii) | p+(N ) = coker y1 … | `$p_+(N)=\operatorname{coker}\partial_1$`（chap1.tex:1712–1713） | — | 陈述用 $M$、(ii)(iii) 用 $N$，原文自相矛盾，译文照原文 | 原文笔误 |
| 英文 p.59 / 13.4 证明 | all other derived inverse images vanish | `其余导出逆像全为零` | — | 此处讲的是 $p_+$（直像），原文 “inverse” 为笔误，译文照原文 | 原文笔误 |

## 五、存疑

| 位置 | 原文（英文，截 60 字内） | 原译 | 改为 | 理由 | 级别 |
|---|---|---|---|---|---|
| chap1.tex:1461 / p.47 | For F i（pdftotext 上下标散架） | `\operatorname{For}F^i` | `\operatorname{For}F^\cdot` | 无法从纯文本判定原式是 $F_i$ 还是 $F^\cdot$；按文中 1453 行的记法取 $F^\cdot$，若复核发现原书用下标应改回 $F_i$ | 存疑 |
| chap1.tex:1873 / p.52 | p+ is exact and maps holonomic modules … | `$p_+$` | `$p^+$` | 依 10.5 的陈述判定为 $p^+$；但 pdftotext 不能区分上下标。若原书此句确写 $p_+$，则该句对 10.5 的引用本身有误（10.5 只讲 $p^+$） | 存疑 |

## 统计

| 级别 | 条数 |
|---|---|
| P1 | 14（漏译补译 9 条：10.5–10.10 六个编号结果及其间散文、公式；公式/符号 5 条：1461、1812、1873、1875、§12–13 上下标 33 处） |
| P2 | 6（术语 4 条 + 两个标题 + `\item` 空格） |
| P3 | 1（chap1.tex:1578 补译句润色：「即 $\tilde\beta$ 是扩充 $R(X)$ 的自同构 $\beta$ 的 $D_X$ 的自同构」→「即 $\tilde\beta$ 是 $D_X$ 的自同构，它扩充了 $R(X)$ 的自同构 $\beta$」） |
| 原文笔误（登记，未改） | 9 |
| 存疑 | 2 |

补充说明：§10 补译后条目序列为 prop, lemma, theorem, corollary, prop, lemma, lemma, lemma, lemma, theorem，共 10 条，与原文 10.1–10.10 的类型序列逐一对齐；全章 111 个定理类环境成对闭合，插入段无未配对 `$`。未运行 xelatex（按分工由主控编译）。
