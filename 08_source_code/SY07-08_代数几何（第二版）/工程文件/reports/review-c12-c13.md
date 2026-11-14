# c12 + c13 校勘报告（§2.2 谱序列，原书 p.149–167 / PDF p.156–174）

校勘人：tr-ch1a　　日期：2026-11-14　　范围：`源码/chunks/c12.tex`（647 行）、`源码/chunks/c13.tex`（402 行），对照 `工程文件/pages/p156.png`–`p174.png` 十九页页面图逐页逐句核对。

## 结论

**未发现实质数学错误（0 条）。**

谱序列的 $(p,q,r)$ 三重指标、$d_r$ 的指标漂移 $E_r^{pq}\to E_r^{p+r,q-r+1}$、滤过链与 $Z/B$ 的包含关系、双复形 $sK^{\cdot\cdot}$ 的求和与符号、Cartan–Eilenberg 分解的分裂短正合序列、Grothendieck/Leray/Ext/Tor 各谱序列的条件与方向、条目环境类型与编号 $2.2.1$–$2.2.17$ 全部与原书一致；14 + 1 张交换图的形状、箭头方向、标签亦一致。仅 2 条非数学的小建议（见文末），另有 3 条译注所指的原书笔误经核对全部属实。

## 覆盖范围与接缝

- **c12**：原书 p.149–160（PDF p.156–167）＋ p.161 页首「另一种构造」段（PDF p.168 上半）。含 §2.2 标题、谱序列定义 (a)–(f)、态射定义 (i)–(iv)、双正则/正则、命题 2.2.1–2.2.5、引理 2.2.6，以及「由过滤复形构造谱序列」全段与 $E_1/E_0$ 两种替代构造。
- **c13**：原书 p.161–167（PDF p.168–174）。含命题 2.2.7（双正则性判据）、双复形、命题 2.2.8–2.2.10、引理 2.2.11、推论 2.2.12–2.2.13、引理 2.2.14、命题 2.2.15–2.2.17、习题 1–4。
- **接缝**：c12 末句「这给出了谱序列的另一种构造。细节留给读者。」（原书 p.161 第 1 段末）与 c13 开头「命题 2.2.7」同处 PDF p.168，**无重复、无遗漏**。
- **编译**：`xelatex -interaction=nonstopmode _check_c12.tex`（临时输出目录）exit 0、11 页；`_check_c13.tex` exit 0、7 页。两日志均无 `!` 错误、无 Overfull/Underfull。c13 单独编译时 `it:2.1.1` 显示 `??`（该 label 在 c10 内定义），主文件合并后正常，非错误。渲染抽查 c12 第 3、9、10、11 页与 c13 第 1、2、3 页，图形与版面正常。

## 已核对的关键公式清单（31 条）

下表中「原书」列为书上的公式，「位置」列为 c12/c13 的对应行号。

1. 谱序列定义 $d_r^{pq}\colon E_r^{pq}\to E_r^{p+r,q-r+1}$；$Z_{r+1}=\Ker d_r^{pq}$，$B_{r+1}=\Image d_r^{p-r,q+r-1}$，$B\subset Z\subset E$ — p.149｜c12.tex:8–12
2. 归纳链 $Z_k(E_r^{pq})/B_k(E_r^{pq})\cong\cdots\cong Z_k(E_{k-1}^{pq})/B_k(E_{k-1}^{pq})\cong E_k^{pq}$；$0=B_r\subset B_{r+1}\subset\cdots$，$\cdots\subset Z_{r+1}\subset Z_r=E_r$ — p.149｜c12.tex:23–40
3. $\alpha_r^{pq}\colon Z_{r+1}/B_{r+1}\cong E_{r+1}^{pq}$ — p.149｜c12.tex:15
4. $B_k(E_2^{pq})\subset B_\infty\subset Z_\infty\subset Z_k$（$\forall k\ge2$），$E_\infty^{pq}=Z_\infty/B_\infty$ — p.149–150｜c12.tex:44–48
5. $\beta^{pq}\colon E_\infty^{pq}\cong F^pH^{p+q}/F^{p+1}H^{p+q}$；记 $E_2^{pq}\Rightarrow H^{p+q}$ — p.150｜c12.tex:55、59
6. 态射条件 (i)–(iv)：$u^n(F^pH^n)\subset F^pH'^n$、$\bar u_r^{pq}$、$u_r^{pq}(B_k)\subset B_k$、$u_2^{pq}(B_\infty)\subset B_\infty$、$u_\infty^{pq}$ 及三张交换图 — p.150｜c12.tex:63–93
7. 双正则 (i)(ii) 与正则 (i)(ii)（$B_\infty=\varinjlim_{2\le k<\infty}B_k$、$Z_\infty=Z_k$；$H^n=\dlim_pF^pH^n$） — p.151｜c12.tex:98–118
8. 2.2.1 证明：$u_2^{pq}(B_k)=B_k$、$u_2^{pq}(Z_k)=Z_k$ ⟹ $B_\infty/Z_\infty$ 同构，再用 $0\to F^pH^n\to F^{p-1}H^n\to F^{p-1}H^n/F^pH^n\to0$ 作递降归纳 — p.151｜c12.tex:126–149
9. 2.2.2：$E_r^{n-q_0,q_0}\cong H^n$（resp. $E_r^{p_0,n-p_0}\cong H^n$），$B/Z$ 稳定 ⟹ $E_\infty\cong E_r$ — p.152｜c12.tex:152–195
10. 2.2.3 证明中的 $d_r^{i-r,r-1},d_r^{i,0}$ 全零；$B_2=\cdots=B_\infty$，$Z_\infty=\cdots=Z_2$；$E_\infty^{i,0}\cong E_2^{i,0}$ — p.153｜c12.tex:209–235
11. 2.2.3：(1) $0\to E_\infty^{n,0}\to H^n\to E_\infty^{0,n}\to0$；(2) $0\to E_\infty^{n+1,0}\to H^{n+1}$ — p.153｜c12.tex:249–263
12. 2.2.3：(3) $E_\infty^{n,0}\cong E_2^{n,0}$；(4) $E_\infty^{0,n}\cong Z_{n+2}(E_2^{0,n})/B_{n+1}(E_2^{0,n})$；(5) $E_2^{0,n}\cong E_{n+1}^{0,n}$；(6) $E_\infty^{n+1,0}\cong Z_{n+1}(E_2^{n+1,0})/B_{n+2}(E_2^{n+1,0})$；(7) $E_2^{n+1,0}\cong E_{n+1}^{n+1,0}$ — p.154–155｜c12.tex:277–317
13. 2.2.3 结论：$0\to E_2^{n,0}\to H^n\to E_2^{0,n}\to E_2^{n+1,0}\to H^{n+1}$ — p.155｜c12.tex:336
14. 2.2.4：$p_2-p_1=1$ 时 $0\to E_2^{p_2,n-p_2}\to H^n\to E_2^{p_1,n-p_1}\to0$；$p_2-p_1\ge2$ 时长正合序列；$E_\infty^{p_1,n-p_1}\cong Z_{p_2-p_1+1}/B_{p_2-p_1}$、$E_\infty^{p_2,n+1-p_2}\cong Z_{p_2-p_1}/B_{p_2-p_1+1}$ — p.155–156｜c12.tex:341–441
15. 2.2.5（$q$ 方向版本）与 2.2.6 引理 $\Image\gamma/\Image\alpha\to\Image(\beta\gamma)$ — p.157｜c12.tex:447–465
16. 过滤复形：$Z_r^{pq}=\Image(H^{p+q}(F^pK^{\cdot}/F^{p+r}K^{\cdot})\to H^{p+q}(F^pK^{\cdot}/F^{p+1}K^{\cdot}))$；$B_r^{pq}=\Image(H^{p+q-1}(F^{p-r+1}K^{\cdot}/F^pK^{\cdot})\to\cdots)$ — p.157–158｜c12.tex:476、484
17. $Z_\infty^{pq}=\Image(H^{p+q}(F^pK^{\cdot})\to H^{p+q}(F^p/F^{p+1}))$、$B_\infty^{pq}=\Image(H^{p+q-1}(K^{\cdot}/F^pK^{\cdot})\to\cdots)$；$B_\infty\subset Z_\infty$ — p.158｜c12.tex:492–516
18. $Z_r^{pq}/Z_{r+1}^{pq}\cong B_{r+1}^{p+r,q-r+1}/B_r^{p+r,q-r+1}$；$d_r^{pq}$ 为 $Z_r/B_r\to Z_r/Z_{r+1}\cong B_{r+1}/B_r\to Z_r^{p+r,q-r+1}/B_r^{p+r,q-r+1}$ 的复合；$\Ker d_r^{pq}=Z_{r+1}^{pq}/B_r^{pq}$ — p.159｜c12.tex:527–567
19. $F^pH^n=\Image(H^n(F^pK^{\cdot})\to H^n(K^{\cdot}))$；$F^pH^{p+q}/F^{p+1}H^{p+q}\cong Z_\infty^{pq}/B_\infty^{pq}$；$B_\infty(E_2^{pq})=B_\infty^{pq}/B_2^{pq}$ — p.159–160｜c12.tex:571、598、600
20. $E_1^{pq}=H^{p+q}(F^pK^{\cdot}/F^{p+1}K^{\cdot})$，$d_1^{pq}\colon E_1^{pq}\to E_1^{p+1,q}$，$E_2^{pq}=\Ker d_1^{pq}/\Image d_1^{p-1,q}$ — p.160｜c12.tex:604–616
21. $E_0^{pq}=F^pK^{p+q}/F^{p+1}K^{p+q}$；$Z_r^{pq}=(F^pK^{p+q}\cap d^{-1}(F^{p+r}K^{p+q+1})+F^{p+1}K^{p+q})/F^{p+1}K^{p+q}$，$B_r^{pq}=(F^pK^{p+q}\cap d(F^{p-r+1}K^{p+q-1})+F^{p+1}K^{p+q})/\cdots$，及 $d_r$ 的大分式复合 — p.161｜c12.tex:624–641
22. 2.2.7：$r>\max(g(p+q-1),g(p+q),g(p+q+1))-p$ 时 $Z_r^{pq}\cong Z_\infty^{pq}$；$r>p+1-\min(f(p+q-2),f(p+q-1),f(p+q))$ 时 $B_r^{pq}\cong B_\infty^{pq}$ — p.161｜c13.tex:10–26
23. 双复形：$d_1^{i+1,j}d_1^{ij}=0$、$d_2^{i,j+1}d_2^{ij}=0$、$d_1^{i,j+1}d_2^{ij}=d_2^{i+1,j}d_1^{ij}$；$(sK^{\cdot\cdot})^n=\bigoplus_{i+j=n}K^{ij}$，$dx=d_1x+(-1)^id_2x$ — p.162｜c13.tex:31–47
24. $F_I^p(sK^{\cdot\cdot})^n=\bigoplus_{i+j=n,\,i\ge p}K^{ij}$、$F_{II}^p=\bigoplus_{i+j=n,\,j\ge p}K^{ij}$；$E_{I1}^{pq}\cong H_{II}^q(K^{p,\cdot})$、$E_{I2}^{pq}=H_I^pH_{II}^q$、$E_{II2}^{pq}=H_{II}^pH_I^q$ — p.162｜c13.tex:70–89
25. 2.2.8 四条件 (i)–(iv)（$K^{pq}$ 支集在 $p\ge p_0,q\ge q_0$／$p\le p_0,q\le q_0$／$p_1\le p\le p_2$／$q_1\le q\le q_2$） — p.163｜c13.tex:96–99
26. 2.2.9：$I^{\cdot,q},Z_{II}^q,B_{II}^q,H_{II}^q$ 均为内射分解，及两条分裂短正合序列 $0\to B_{II}^q\to Z_{II}^q\to H_{II}^q\to0$、$0\to Z_{II}^q\to I^{i,q}\to B_{II}^{q+1}\to0$ — p.163｜c13.tex:105–110
27. 2.2.10：$E_2^{pq}=\R^pG(\R^qF(A))\Rightarrow\R^{p+q}(GF)(A)$；证明中 $H_{II}^q(G(J^{\cdot\cdot}))\cong G(H_{II}^q(J^{\cdot\cdot}))$、$E_{I2}^{pq}=\R^pG(\R^qF(A))$ 与退化的第二谱序列 — p.163–164｜c13.tex:148、168–208
28. 2.2.11 $\Hom(\cG,f_*\cI)\cong\Hom(f^{-1}\cG,\cI)$ ⟹ $f_*\cI$ 内射；2.2.12 Leray：$E_2^{pq}=H^p(Y,\R^qf_*\cF)\Rightarrow H^{p+q}(X,\cF)$ — p.165｜c13.tex:218、226
29. 2.2.13：$E_2^{pq}=\R^pg_*\R^qf_*\cF\Rightarrow\R^{p+q}(gf)_*\cF$；2.2.14 $\Hom_{\cO_X}(\cF,\cI)$ 松弛（$j_!$ 的伴随与延拓）；2.2.15：$E_2^{pq}=H^p(X,\Ext^q(\cF,\cG))\Rightarrow\Ext^{p+q}(\cF,\cG)$ — p.165–166｜c13.tex:238、243–259、264
30. 2.2.16：双复形 $(K^{pq})=(\Hom_{\cO_X}(\cE_p,\cI^q))$，$H_{II}^q=\{0\,(q\ge1);\ \Hom(\cE,\cG)\,(q=0)\}$、$H_I^q=\{0\,(q\ge1);\ \Hom(\cF,\cI)\,(q=0)\}$，得 (1)(2) 与 $\Ext^n\cong H^n(\Hom(\cE,\cI))\cong H^n(\Hom(\cE,\cG))$；2.2.17：$\Tor_n^A(M,N)\cong H^{-n}(M\otimes_AF^{\cdot})\cong H^{-n}(E^{\cdot}\otimes_AN)\cong H^{-n}(E^{\cdot}\otimes_AF^{\cdot})$ — p.166｜c13.tex:282–346
31. 习题 1–4：$\Ext^i_{A_U}(M_U,N_U)\cong\Ext^i_{\cO_U}(M^{\sim}|_U,N^{\sim}|_U)$；$0\to H^n(K)\otimes N\to H^n(K\otimes N)\to\Tor_1^R(H^{n+1}(K),N)\to0$ 与 $0\to\Ext_R^1(H^{-(n-1)}(K),N)\to H^n(\Hom_R(K,N))\to\Hom_R(H^{-n}(K),N)\to0$；$H^i(X,\Hom(\cF,\cG))\cong\Ext^i(\cF,\cG)$；$E_1^{pq}\Rightarrow H^n$ 且 $H^n=H_{-n}(X)$、$E_1^{pq}=H_{p-q}(X_{-p},X_{-p-1})$ — p.167｜c13.tex:351–399

## 编号、环境与引用

- 条目 17 个，原书顺序与环境类型逐一对应：命题 2.2.1/2.2.2/2.2.3/2.2.4/2.2.5、引理 2.2.6（c12）；命题 2.2.7/2.2.8/2.2.9/2.2.10、引理 2.2.11、推论 2.2.12、推论 2.2.13、引理 2.2.14、命题 2.2.15/2.2.16/2.2.17（c13）。`\label` 全部为 `it:2.2.N`，序号连续无跳号、与原书编号一致。
- 习题 4 条 `ex:2.2.1`–`ex:2.2.4`，编号用 exercises 环境的 (1)(2)(3) 内层 enumerate，与原书一致。
- `\ref` 审计：c12 引用 `it:2.2.6`×4；c13 引用 `it:2.2.7`×1、`it:2.2.8`×1、`it:2.2.2`×3、`it:2.2.10`×2、`it:2.2.11`×1、`it:2.2.14`×1、`it:2.1.1`×2（跨块，c10 定义）——全部指向正确的条目，无错引。
- c12 有 `\subsection{谱序列}\label{sec:2.2}`，c13 无 `\subsection`，符合分块约定。

## 交换图核对

c12.tex 共 14 张 tikzcd：态射定义 3 张（$d_r$ 相容、$\alpha_r$、$\beta$ 与 $\bar u^{p+q}$）、2.2.1 证明 1 张（$F^pH^n$ 五引理式）、构造部分 9 张、$E_0$ 构造 1 张；c13.tex 1 张（Cartan–Eilenberg 大图）。逐张对照原书 p.150、p.151、p.158、p.159、p.160、p.163：形状（横向 →、纵向 ↑ 或 ↓、弯箭头、双线等号）、箭头方向与标签全部一致。特别核过：

- p.158 的 $0\to F^pK^{\cdot}\to K^{\cdot}\to K^{\cdot}/F^pK^{\cdot}\to0$ 与下行商列之间的方形，右端竖箭头为等号（`\arrow[d,equal]`），原书为双线；
- p.159 的 $d_r^{pq}$ 复合四段图：$Z_r/B_r\to Z_r/Z_{r+1}\xrightarrow{\cong}B_{r+1}^{p+r,q-r+1}/B_r\to Z_r^{p+r,q-r+1}/B_r$；
- p.160–161 三处「把 2.2.6 应用于图表」的斜箭头（原书 ↗）在 tikzcd 中用顶格 `\arrow[dl]` 表达，方向一致；
- p.163 Cartan–Eilenberg 大图：列为 $q,q+1$，行为 $K^q$、$I^{0,q}$、$I^{1,q}$、$\vdots$，竖向箭头自下而上、底部两个 $0$，与原书方向一致。

## 译注核对（5 条，来源均属实）

| 位置 | 译注内容 | 核对结果 |
| --- | --- | --- |
| c12.tex:142（原书 p.151） | 原书印 $F^pH^n=F^pH'^p=0$，第二式上标应为 $n$ | 属实：p158 图像确印 $F^pH'^p$，应为 $F^pH'^n$ ✔ |
| c12.tex:242（原书 p.153） | 「$\cdots=F^{-1}H^n=F^0H^n\supset F^{-1}H^n=\cdots$」中第二个 $F^{-1}$ 应为 $F^1$ | 属实：p160 图像确有两处 $F^{-1}$，按递降性应为 $F^1$ ✔ |
| c13.tex:315（原书 p.166） | $H_I^q(K^{\cdot\cdot})$ 按 p.162 记号应为 $H_I^p$（分类条件也该用 $p$） | 属实：p173 图像 3 倍放大确印 $H_I^q$，分类写 `if q≥1 / if q=0` ✔，译文照录并说明，处理得当 |
| c12.tex:117（原书 p.151） | 解释正则 (i) 两式的写法 | 见建议 1（非错误） |
| c13.tex:116（原书 p.163） | 解释 CE 分解两条分裂短正合序列 | 见建议 2（非错误） |

## 建议（2 条，均非数学错误，交由 Lead 决定）

| 位置（原书页 + 行号） | 原书 | 译文 | 建议 |
| --- | --- | --- | --- |
| 原书 p.151 正则定义 (i)｜c12.tex:116–118 | $B_\infty=\varinjlim_{2\le k<\infty}B_k$，$Z_\infty(E_2^{pq})=Z_k(E_2^{pq})$（充分大 $k$） | 译注：「在（双）正则谱序列中，固定 $(p,q)$ 后 $Z_k$ 与 $B_k$ 当 $k$ 足够大时不再变化，故 $Z_\infty$ 就等于某个 $Z_k$」 | 该稳定化只是**双正则**的定义性质；正则情形按惯例应为 $Z_\infty=\bigcap_kZ_k$（逆向极限），原书此处疑为沿用双正则写法未改。建议译注补一句「正则情形 $Z_\infty$ 应理解为 $\bigcap_kZ_k$」，避免读者把「正则」当「双正则」。因下文只对双正则陈述结论，无实质影响。 |
| 原书 p.163 命题 2.2.9 附图｜c13.tex:115–117 | 图排在定义之后 | 译注写「**上附**图表中每一列……」 | 该图实际排在译注之后（下一页页首），建议改为「下图」或「所附图表」。 |

## 未改动声明

本次校勘**未修改** `c12.tex`、`c13.tex`、`preamble.tex`、`main.tex`、`glossary.tsv` 及他人块；工程内仅新增本报告与 `工程文件/work/_crops/` 下的临时渲染图（校勘结束后已清理临时裁切脚本与临时编译目录，`_crops` 里保留的几张 c12/c13 渲染图可供复核）。
