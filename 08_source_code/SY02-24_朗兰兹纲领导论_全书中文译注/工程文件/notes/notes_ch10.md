# 第 10 章通读笔记 · Cogdell, "Langlands Conjectures for GL_n"

底本：J. W. Cogdell, *Langlands Conjectures for GL_n*, in Bernstein–Gelbart (eds.),
*An Introduction to the Langlands Program*, Birkhäuser 2004, pp. 229–249。
页图：`work/pages/c10_p231.png`–`c10_p252.png`（150 dpi，含前一章末页与本章全部页）。

**页码校正**：本 PDF 的印刷页 = PDF 页 − 3（PDF 231 页眉为 "228"，是第 9 章末页）。
故章首页 PDF 232 即印刷页 229。现行抽件页标记为 `===== PDF PAGE n (BOOK m) =====`，
其中 BOOK 列已是印刷页（旧格式 `===== BOOK PAGE n =====` 的标号曾比印刷页大 1，勿再沿用）。
正文止于印刷页 245（PDF 248）；参考文献 [1]–[60] 自同页下半起始，至印刷页 249（PDF 252）止。

## 一、三句话主旨

1. 本章是一篇综述：以 $\mathrm{GL}_n$ 为例，说明 Langlands 猜想如何把 $\mathcal{G}_k$ 的
   $n$ 维表示与 $\mathrm{GL}_n$ 的自守（局部为容许）表示对应起来，并使两侧的 $L$ 函数与
   $\varepsilon$ 因子逐项相等。
2. 局部情形有两条路线：表示论形式（Langlands 1973 解决阿基米德情形）与 $L$ 函数形式
   （Laumon–Rapoport–Stuhler 1993 处理正特征，Harris–Taylor 1999、Henniart 2000 处理特征零），
   三条证明共用"单射—计数—唯一性—存在性"四步约化，只在存在性构造上分道。
3. 整体情形只在函数域上完全解决（Drinfeld $n=2$、Lafforgue 一般 $n$），数域上只有零散特例；
   其障碍在于 $\mathrm{GL}_n$ 在数域上没有自然的模问题，而整体 Weil–Deligne 群并不存在，
   只能代之以猜想中的 Langlands 群 $\mathcal{L}_k$。

## 二、逐节内容地图

| 印刷页 | PDF 页 | 内容 |
|---|---|---|
| 229 | 232 | 章首：作者名；引论 6 段（$\mathcal{G}_k$ 的表示论进路；Artin $L$ 函数；自守侧 $\mathrm{GL}_n(\mathbb{A})$；两类对应的双向解读；1990 年代以来的四大进展；本文结构；Wiles 特例一笔带过） |
| 230 | 233 | 引论末段；§1 起：$\operatorname{Rep}_n(G;F)$、$\operatorname{Rep}_n^0$；$\mathcal{G}_k$、$W_k$；非阿基米德局部域的 $I$、$\Phi$、$\omega^s$、$v(w)$；Galois 型表示 |
| 231 | 234 | $\ell$ 进表示与 $W'_k$：半直积 $W_k\ltimes\mathbb{G}_a$、$F$ 点乘法、$(\rho,N)$ 与 $\rho(w)N\rho(w)^{-1}=\|w\|N$；$\Phi$ 半单化 $u$；$\operatorname{Rep}_n(W'_k;F)$；不可约时 $N=0$；$V_N^I$ 与 $Z(t,V)$ |
| 232 | 235 | $L(s,\rho')=Z(q^{-s},\rho')$；$\varepsilon(s,\rho',\psi)$ 的出处；阿基米德情形 $W_{\mathbb{C}}=\mathbb{C}^\times$、$W_{\mathbb{R}}\cong\mathbb{C}^\times\sqcup j\mathbb{C}^\times$ 与正合列；整体 $\ell$ 进表示的定义；Euler 乘积；三条"良好性质" |
| 233 | 236 | Brauer 定理；函数域情形 Grothendieck / Deligne；§2 起：$\mathcal{A}_n(k)$、$\mathcal{A}_n^0(k)$、Godement–Jacquet、Rankin–Selberg 局部因子；整体 Euler 乘积与三条性质 |
| 234 | 237 | $\mathcal{A}_n(k;\Ql)$、$\mathcal{A}_n^0(k;\Ql)_f$；函数域 $\Ql$ 值尖点形式的四条定义 (i)–(iv)；§3 起：局部 Langlands 猜想的历史（Weil 群版、$\mathrm{GL}_2$ 的特殊表示、Borel–Corvallis） |
| 235 | 238 | 猜想 I 全文 (i)–(vi) |
| 236 | 239 | 猜想 I 的补注；Jacquet–Langlands 书与 Deligne 的 $L$ 函数版；猜想 II 全文 (i)–(v)；两种解读（非 Abel 类域论 / 算术 Langlands 分类） |
| 237 | 240 | §3.1 阿基米德：$\mathcal{G}_k=\mathbb{Z}/2\mathbb{Z}$ 或平凡；定理 3.1；§3.2 非阿基米德：定理 3.2（LRS） |
| 238 | 241 | 定理 3.3（Henniart / Harris–Taylor）；约化第 1 步单射性（$L$ 函数在 $s=0$ 的极点）、第 2 步数值局部 Langlands（$a(\rho)$、$f(\pi)$、$|\operatorname{Rep}|=|\mathcal{A}|$）、第 3 步唯一性（局部逆定理） |
| 239 | 242 | 第 4 步存在性：LRS 用 $\mathcal{D}$-椭圆模的模空间；Harris–Taylor 用 Kottwitz 酉群的简单 Shimura 簇，得 $\pi\otimes JL(\pi)\otimes\rho_\pi$ |
| 240 | 243 | Henniart 的 Brauer 归纳路线（自守诱导、Harris 的整体自守诱导弱情形、Clozel、Kottwitz）；§3.3 补充：去掉中心特征有限阶、Bernstein–Zelevinsky、显式对应问题 |
| 241 | 244 | §4 起：整体 Weil–Deligne 群不存在，代之以 $\mathcal{L}_k$ 与 $\mathcal{M}_k$；§4.1 函数域：Drinfeld、Lafforgue；整体对应的表述 |
| 242 | 245 | 整体猜想 (i)–(vi)；$S(\pi)$、Satake 类 $A_{\pi_x}$、Hecke 特征值 $z_i(\pi_x)$；$S(\rho)$、Frobenius 特征值 $z_i(\rho_x)$；Chebotarev |
| 243 | 246 | 定理 4.1；由特征值相等推出猜想（局部因子比较、函数方程、$\varepsilon$ 分解）；约化：唯一性与互逆；Piatetski-Shapiro–Deligne 归纳；定理 4.2 |
| 244 | 247 | 存在性：双陪集 $\mathrm{GL}_n(k)\backslash\mathrm{GL}_n(\mathbb{A})/\mathrm{GL}_n(\mathcal{O})$；shtuka 栈 $\mathcal{V}$；$H^*_c(\bar k\otimes_k\mathcal{V};\Ql)$；几何 Grothendieck–Lefschetz 与 Arthur–Selberg；定理 4.3（Ramanujan–Petersson）、4.4（Deligne 的权 0 纯性） |
| 245 | 248 | §4.2 数域：$\mathcal{L}_k$ 的正合列与交换图；三类整体对应 (i)(ii)(iii)；已知结果：Deligne（$n=2,k=\mathbb{Q}$）、Deligne–Serre（权 1）、全实域、虚二次域、Clozel（一般 $n$）；反方向：Langlands–Tunnell（强 Artin 猜想）、Wiles、Breuil–Conrad–Diamond–Taylor |
| 246–249 | 249–252 | REFERENCES [1]–[60]（[1]–[10] 自 p.245 下半页起，故书目实占 245–249） |

## 三、体裁

- 会议论文集式的**综述**（survey），不是教材章节：无证明，只有定理陈述＋路线点评。
- 五级结构：无编号引论 → §1 Galois 侧 → §2 自守侧 → §3 局部（含 3.1/3.2/3.3）→ §4 整体（含 4.1/4.2）。
- 编号体：猜想 I/II、定理 3.1–3.3、4.1–4.4；公式全部无编号，一律行内或独立显示。
- 语体：第一人称复数（we），大量 "Note that…"、"Of course…" 的提示句；译文保留这种讲解口吻。
- 参考文献 60 条，正文用 [n] 引用；本章不重排、不迻译书目条目。

## 四、公式与记号风险点（抽取件不可信，均已回页图核对）

| 抽取件乱码 | 实际 | 页 |
|---|---|---|
| `Qfb` | $\mathcal{G}_k^{\mathrm{ab}}$ | 229 |
| `Rep2 (G; F)` | $\operatorname{Rep}_n^0(G;F)$ | 230 |
| `ws`、`<I>`、`<1>` | $\omega^s$、$\Phi$ | 230 |
| `W£`、`W~`、`Wk 1>< Ga` | $W'_k$、$W_k\ltimes\mathbb{G}_a$ | 231 |
| `(w1, XJ)(Ww, xz) = (WJ wz, XJ + llwiiixz)` | $(w_1,x_1)(w_2,x_2)=(w_1w_2,x_1+\|w_1\|x_2)$ | 231 |
| `eaN p(w)u-v(w)` | $e^{aN}\rho(w)u^{-v(w)}$ | 231 |
| `£`（作函数） | $L$ | 全章 |
| `£`/`s`（作因子） | $\varepsilon$ | 全章 |
| `t : Qe ~ C` | $\iota\colon\Ql\to\mathbb{C}$ | 231 起 |
| `Z(t, V) = det(l- tp(<I>)IV£)- 1` | $Z(t,V)=\det(1-t\rho(\Phi)|_{V_N^I})^{-1}$ | 231 |
| `WJR ~ ex jex` | $W_{\mathbb{R}}\cong\mathbb{C}^\times\sqcup j\mathbb{C}^\times$ | 232 |
| `Pir = /i:r`、`p7r = 'ii` | $\rho_{\tilde\pi}=\tilde\rho_\pi$、$\pi'=\tilde\pi$ | 235, 237 |
| `A2(k; «J!e)J` | $\mathcal{A}_n^0(k;\Ql)_f$ | 234 |
| `flv = 7r`、`TI`、`D(.A)` | $\Pi_v=\pi$、$\Pi$、$D(\mathbb{A})$ | 238 |
| `V-elliptic` | $\mathcal{D}$-elliptic（$\mathcal{D}$ 为 $D$ 中的序） | 238 |
| `H;(f ®k V; «Jlt:)` | $H^*_c(\bar k\otimes_k\mathcal{V};\Ql)$ | 244 |
| `1 ---+ .C~ ---+ .Ck ---+ (h ---+ 1` | $1\to\mathcal{L}_k^0\to\mathcal{L}_k\to\mathcal{G}_k\to1$ | 244 |
| `q;s` | $q_x^{-s}$ | 242 |
| `s(s, rr x r, 1/1)` | $\varepsilon(s,\pi\times\tau,\psi)$ | 238 |

其他要点：

- 猜想 I (iv) 的判据用 $\rho(W'_k)$（含 $N$），不是 $\rho(W_k)$；(v) 用 $\rho(W_k)$ 有界。两者不可混。
- 猜想 II (i) 的归一化："一致化子 ↔ 几何 Frobenius"；这是全部 $\varepsilon$ 因子与中心特征的定标点。
- 定理 3.2 / 3.3 的靶是 $\operatorname{Rep}_n^0(\mathcal{G}_k)$（Galois 型），源是 $\mathcal{A}_n^0(k)_f$（中心特征有限阶）。
- 原书两处引文编号疑互换：p.237 "established by Henniart in 1988 [30]" 应为 [28]；p.237 末 "Harris and Taylor [27] and Henniart [28]" 应为 [30]。译文照排，另出译注。
- 整体侧 $L(s,\rho)=\prod_v L(s,\rho_v)$ 中 $\rho_v$ 由 $\mathcal{G}_{k_v}\to\mathcal{G}_k$ 拉回；函数域情形 $q$ 为常数域阶，局部用 $q_x$。

## 五、译注计划（14 条）

1. 易错：引论"一维 $\rho$ ↔ Abel 类域论"的归一化，$\mathcal{G}_k^{\mathrm{ab}}$ 与 Hecke 特征的对应。
2. 易错：$W'_k$ 的 $F$ 点乘法交叉项用 $\|w_1\|$，可验结合律。
3. 点拨：$L$ 因子取 $V_N^I=(\ker N)^{\rho(I)}$ 而非 $V^I$ 的理由。
4. 易错：$W_{\mathbb{R}}$ 不是 $\mathbb{C}^\times\times\mathbb{Z}/2$ 的直积，扩张不分裂；$j^2=-1$。
5. 点拨：函数方程中的 $\tilde\rho$、$\tilde\pi$ 是对偶表示（contragredient），非复共轭。
6. 易错：$\mathcal{A}_n(k)$ 在局部/整体两节所指不同。
7. 点拨：cusp form 条件 (iii) 的 $\deg(a)\neq0$ 何以蕴涵中心特征有限阶。
8. 易错：平方可积判据用 $\rho(W'_k)$，Steinberg 表示不会落在真 Levi 中。
9. 直觉：几何 Frobenius 归一化，若换成算术 Frobenius 的后果。
10. 点拨：局部逆定理中"扭 $L$ 函数恒等于 1"的理由。
11. 校勘：p.237 两处 Henniart 引文编号互换。
12. 直觉：Harris–Taylor 的 $\pi\otimes JL(\pi)\otimes\rho_\pi$ 与内形式。
13. 直觉：双陪集分类向量丛，shtuka 才使 Hecke 对应几何化。
14. 点拨：定理 4.4 "pure of weight 0" 的确切含义（经 $\iota$ 的复绝对值）。

## 六、术语处理

- 沿用 STYLE.md：自守表示、尖点的、无分歧、容许的、Whittaker 模型、L 函数、朗兰兹对偶群等。
- 新增并统一：局部常数（local constant）、几何 Frobenius 元、$\Phi$ 半单化、惯性子群、
  超尖点表示、平方可积、缓增（tempered）、离散序列、特殊表示、导子的指数、数值局部 Langlands 猜想、
  局部逆定理、强重数一定理、Satake 参数、Frobenius 特征值、部分 $L$ 函数、shtuka（保留原文）、
  简单 Shimura 簇、除代数、Hasse 不变量、动机 Galois 群、投射约化（pro-reductive）。
- 人名一律"名 姓"西文原样；定理、猜想、节号照原书。
