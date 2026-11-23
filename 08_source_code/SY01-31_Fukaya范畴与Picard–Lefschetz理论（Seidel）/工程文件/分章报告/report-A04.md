# 分章校对报告 A04：§6（后半）、第二章引言、§7、§8（含 8i–8l）

## 一、范围与工作量

| 项目 | 内容 |
| --- | --- |
| 文件 | `src/chapters/section-6.tex`（145 行）、`src/chapters/chapter-ii.tex`（7 行）、`src/chapters/section-7.tex`（118 行）、`src/chapters/section-8.tex`（179 行）、`src/chapters/section-8-il.tex`（124 行） |
| 原书印刷页 | 88–112（对应 `\SourcePage` 96–120；按 Lead 通知，`\SourcePage{n}` 记 PDF 页，印刷页 = n − 8） |
| 英文对照材料 | `work/en/pages/p088.txt`–`p112.txt`；英文合订本 `work/en/bundles/A04.txt` |
| 通读遍数 | 中文全文 2 遍；与英文逐段对照 1 遍；对 3 处印刷符号（p090 的 (6.4) 与 $Z_j$、p099 的符号与记号）另用 `work/tools/render_page.py` 渲染 PNG 并裁图放大核对 |
| 译文修订 | 1 处 |
| 译者注 | 16 条（`grep -c '\\znote'` 合计 16，与 `notes-A04.tsv` 条数一致） |
| 编译自检 | `check.ps1` 五个文件全部 `OK` |

## 二、译文修订表

| # | 文件:行 | 原文 | 改文 | 理由 |
| --- | --- | --- | --- | --- |
| 1 | `section-6.tex:7` | 事实上，它只由对象上的对合…… | 具体地说，它只由对象上的对合…… | 英文 p087 原文以 "Concretely," 起句，是「具体地说」而非「事实上」；「事实上」会把一句限定说明读成让步，与下文列举「对合 + 态射映射」的语意不合 |

除上表外，逐段对照未见确凿误译。三处曾疑似有误、经核查不成立，明确记录以备复核：

1. `section-6.tex:91` 的 $X\cong Y\oplus\epsilon_{\A}Y\cong U$：书 p090 的 (6.4) 印刷确为两个 $\cong$，与中文一致（裁图 `work/pages/crop_zj.png` 核对）。
2. `section-7.tex:102` 的 $dh_M(du(I_S\xi))\geq0$：书 p099 印刷即 `≥ 0`（裁图 `work/pages/crop_omega2.png` 核对），OCR 文本把它识别成空白/「3」，不能据 OCR 改。
3. `section-7.tex:95,98` 用 $\omega_M=\iota^*\omega_N$、$u^*\omega_N$ 而非全书通用的 $\varpi$：书 p099 该处印刷本就用 $\omega$，译文属忠实照搬，不算误译（见第四节）。

## 三、译者注表

| # | 文件:行 | 原书页 | 主题 | 来源级别 |
| --- | --- | --- | --- | --- |
| A04-01 | `section-6.tex:22` | 88 | 障碍类 $y=\epsilon_A(x^{-1})x$ 的验算与扭曲共轭 | C |
| A04-02 | `section-6.tex:50` | 89 | 特征标 $\check X$ 与「只有 $(\Tw^{\mathrm{eq}}\A)^{\mathrm{inv}}$ 三角化」 | A |
| A04-03 | `section-6.tex:110` | 91 | 记号 $\epsilon_{\A}^*\M$（拉回模）与逐分量模同态 | A |
| A04-04 | `section-6.tex:142` | 93 | 朴素严格对合 vs 同伦相干；Maschke 与不变部分正合 | A |
| A04-05 | `chapter-ii.tex:5` | 95 | Floer–Viterbo 相对分次 vs Kontsevich 绝对分次 | A |
| A04-06 | `section-7.tex:4` | 96 | 余维 $l$ 角点属于 $2^l-1$ 个边界面 | B |
| A04-07 | `section-7.tex:18` | 96 | $\operatorname{Aut}(M)$ 中同痕自动是 Hamilton 同痕 | B |
| A04-08 | `section-7.tex:23` | 96 | 正合 Lagrangian：$[\theta|_L]=0$ 与同痕不变性 | B |
| A04-09 | `section-7.tex:59` | 97 | $h_M$ 作为「到边界的 Liouville 距离」与锥上延拓 | A |
| A04-10 | `section-8.tex:31` | 101 | $HF$ 的反变约定与 TQFT 复合 | B |
| A04-11 | `section-8.tex:45` | 102 | 为何保留入向/出向的区分 | A |
| A04-12 | `section-8.tex:69` | 103 | 取 $W^{1,p}$（$p>2$）的分析理由 | A |
| A04-13 | `section-8.tex:131` | 105 | (8.8) 为 $A_H$ 的负梯度流与能量恒等式 | B |
| A04-14 | `section-8-il.tex:46` | 109 | 「上链群」命名与 $\partial$ 降次、char 2 下无分次 | A |
| A04-15 | `section-8-il.tex:88` | 111 | (8.21) 的恰当一形式与边界项抵消 | A |
| A04-16 | `section-8-il.tex:113` | 112 | 边界求值、$H^*(L)$ 与 PSS 的来源 | A |

来源级别：A = 原书前后文/经典教材自洽（注中给出原书节号或式号）；B = nLab 实际抓取核对（URL 见 TSV 的 `source` 列与注文末尾的来源串）；C = 上下文推断（仅 A04-01，纯代数验算，已在注中声明无外部依据）。

## 四、存疑未改

| 位置 | 原文 | 疑点 | 已查证 | 建议 |
| --- | --- | --- | --- | --- |
| `section-8-il.tex:36` | 注 8.1 中「$K$ 及其一阶导数在 $x$ 处为零……$D^2K$ 可视为 $\Omega^1(S,\operatorname{sym}^2(TM_x)^\vee)$ 的元素」 | 英文 p109 写的是 $Y$（Hamilton 向量场）及其 $D^2Y$，中文改写成 $K$ | 英文 p109 原文：$u\equiv x$ 常值、"$Y$ together with its first derivatives vanishes at the point $x$. The second derivatives $D^2Y$…"；因 $Y$ 是 $K$ 的 Hamilton 向量场，两种写法在 $Y=0$ 的常值解处等价，且 $K$ 版本更贴近「扰动项」的语言 | 保留中文，不改；若 Lead 要统一与原书字面一致，可回改为 $Y$，但需同时改 $D^2Y$ 与「$Y$ 的一阶导数」两处 |
| `section-7.tex:95,98` | $\omega_M=\iota^*\omega_N$、$u^*\omega_N$ | 全书其余部分一律用 $\varpi$ 表示辛形式，此处用 $\omega$ | 书 p099 印刷确为 $\omega_M=\iota^*\omega_N,\ \theta_M=\iota^*\theta_N$，译文照搬原书 | 建议保留（属原书记号不统一，见第五节）；若全稿统一改用 $\varpi$，应作全局记号决定，不宜在本区段单独改 |

## 五、原书可疑处 / 笔误

1. **p090，引理 6.3 证明中的 $Z_j$。** 书印作
   $$Z_j=\bigoplus \hom_{\A}(Y_{j_{r-1}},Y_{j_r})\otimes\cdots\otimes\hom_{\A}(Y_j,Y_{j_2}),$$
   求和为「all $r$ and $j_2<\cdots<j_r$ with $j_2\geq j$」，既没有 $\hom_{\A}(Y_{j_r},Y)$ 因子，也没有 $[r-1]$ 平移。对照 (6.3)，$C$ 的每个张量积因子都以 $\hom_{\A}(Y_{j_r},Y)[1]$ 开头、以 $Y_{j_1}$ 结尾，对角项 $\partial_{Z_j}\otimes e_{Y_j}$ 应作用在「首项 $\hom_{\A}(Y_{j_r},Y)[1]$、末项 $\hom_{\A}(Y_j,Y_{j_2})[1]$」这一段上；又因 $C$ 是 $U\to Y$ 的锥，$U$ 相对 $C$ 整体反向平移一次，$Z_j$ 的每项正应带 $[r-1]$。中文版 `section-6.tex:82-85` 已按此补齐（并加「$r=1$ 时该项理解为 $\hom_{\A}(Y_j,Y)$」的说明），与 bar 复形的通常形式一致。判断：原书公式漏印一项平移与一个因子，中文版是正确的，故不改中文，仅记录。
2. **p099，引理 7.5 之前的嵌入。** 书在此处写 $\omega_M=\iota^*\omega_N$、$\theta_M=\iota^*\theta_N$，用的是 $\omega$ 而非全书通行的 $\varpi$；同页 (7.5) 又写 $u^*\omega_N$。属记号不统一，不影响数学内容（译文照搬）。
3. **p099 的符号方向。** 书中先由 $u(\partial S)\subset\partial M$ 与 $h_M|_{\partial M}=1$ 得到 $h_M\circ u\geq1$，再断言 $dh_M(du(I_S\xi))\geq0$，与 (7.5) 矛盾；此处书印无误，仅提示读者：OCR 文本把 $\geq$ 丢成空白，不可据 OCR 校符号。

## 六、通读小结

本区段覆盖原书印刷页 88–112，即 §6 后半、第二章引言、§7 与 §8（含 8i–8l），跨度大而性质各异。§6 处理 $Z/2$ 等变结构：先在 $\Ai$ 范畴上取朴素的严格对合，用扭曲共轭定义障碍类并讨论「free」情形，再把等变扭曲复形 $\Tw^{\mathrm{eq}}\A$ 与 $\A^{\mathrm{inv}}$ 的导出范畴联系起来，最后把等变模、等变 Yoneda 嵌入推广到 $\mathrm{mod}^{\mathrm{eq}}(\A)$；注 6.5 明说这只是初步近似，真正的同伦相干处理留到 §10b、§14b。第二章引言交待路线：从 Floer 1988 的原始定义出发，用带标点的 Riemann 曲面族给出 TQFT 型运算，再提升为 Fukaya $\Ai$ 范畴，重点是分次与符号。§7 是技术地基：带角正合辛流形、负 Liouville 向量场、弱 $I$-凸性、接触型边界与锥化、极大值原理与磨圆角点，全为 §8 的服务性准备。§8 最长：8a–8h 建立经典 Floer 理论（条带状端与标记、$HF^{\mathrm{pr}}$ 与 TQFT 公理、PSS、$W^{1,p}$ 框架、Floer 数据与扰动数据、非齐次伪全纯映射、能量恒等式、Cauchy–Riemann 算子的 Fredholm 性）；8i–8l 处理正则性与上链层次，包括线性化算子与 $\overline\partial_\nabla$、延拓映射、移动边界条件、边界求值。

译文整体质量高，逐句对照未发现数学内容上的误译，仅 §6 开头 "Concretely" 被译作「事实上」一处措辞偏差。难点集中在三处：其一，§6 的障碍类与 $\Tw^{\mathrm{eq}}$ 的三角化，纯代数但极易看漏特征标的作用；其二，§7b 的 $h_M$ 与极大值原理，符号方向决定论证成败，而书 p099 印的正是 $\geq$，与 (7.5) 相矛盾的方式依赖 $h_M\circ u\geq1$；其三，§8 的入向/出向约定与 (8.24)(8.25) 的边界求值，须与 §9 的分次一起读，否则「上链/上同调」的命名会与降次的 $\partial$ 冲突。阅读建议：先读 §7a 与 8a–8c 建立几何图像，再回头处理 8h–8l 的解析细节；§6 可留到读 §10b 时回看，那时「朴素 vs 同伦相干」的区别才有对照。
