# 乙组卡片交付报告（ch2 + ch7）

- 交付张数：**22 张**（概念 17 + 例子 5），与任务书清单逐条对齐，id/type/track 未改。
  - ch2（track `2`）：14 张 = 概念 11 + 例子 3
  - ch7（track `7`）：8 张 = 概念 6 + 例子 2
- 落盘位置：`_cards_grassmann/cards/concepts/*.json`（17）与 `_cards_grassmann/cards/examples/*.json`（5）。
- 校验：`python tools/validate_cards.py` 全库 65 张卡，我的 22 张 **0 error / 0 warn**；剩余 17 error 全属甲/丙/丁组（`gv-sheaf`、`affine-grassmannian`、`gerbe-banded-by-mu-n`、`root-stack` 等未解析 id），未修改、未引用。
- 页码一律用中译 PDF 页 `pages_zh` 与英文 PDF 页 `pages_en`（ch2：en = zh + 4；ch7 同）；anchor 全部回读 `source/chapters/chNN.tex` 对应行号确认非空且内容相符。

## 一、每卡一句话

### ch2（14）

| # | id | 一句话 |
|---|---|---|
| 1 | `concept/clifford-index` | 曲线所有「有贡献」线性系的 $\deg L-2h^0(L)+2$ 的最小值，衡量曲线离超椭圆有多远，也是 Green 猜想中 Koszul 上同调开始消没的临界下标。 |
| 2 | `concept/graded-minimal-resolution-and-betti-numbers` | 把射影簇的齐次坐标环写成极小自由 $S$-模分解，各阶重数 $\beta_{pj}$ 就是 Betti 数；它们完全决定 Hilbert 函数，也是 Koszul 上同调 $K_{p,q}$ 的代数原型。 |
| 3 | `concept/greens-conjecture` | 预言典范曲线的 Koszul 上同调恰在 Clifford 指标处开始消没：$K_{p,2}(C,K_C)=0\iff p<\mathrm{Cliff}(C)$；它把曲线的外在方程与内在线性系连成一句话。 |
| 4 | `concept/greens-dimension-formula` | 非特殊线丛 $L$ 上 $\dim K_{p,1}-\dim K_{p-1,2}$ 有只依赖 $g,d,p$ 的闭形式，给出 $K_{p,1}$ 非消没的数值阈值，是 Green 猜想最优性的计算基础。 |
| 5 | `concept/kernel-bundle` | 截面求值映射的核 $M_L$ 是秩 $h^0(L)-1$ 的向量丛，把 Koszul 上同调写成它的外幂的上同调，是从 Betti 数走向族上计算的转换器。 |
| 6 | `concept/koszul-cycle` | 把「$K_{p,2}\neq0$」写成两向量丛间限制映射的退化轨迹，用秩相等保证它是除子，于是可用虚类算出 $\overline{\mathcal{M}}_g$ 上的新除子。 |
| 7 | `concept/koszul-duality` | 把 $K_{p,q}(X,L)$ 与 $K_{r-n-p,n+1-q}(X,K_X,L)$ 配对的对偶定理，使非消没与消没成为同一事实的两种写法，是 Green 猜想两种形式的桥梁。 |
| 8 | `concept/maximal-rank-conjecture` | 预言 $\mathfrak{I}_{d,g,r}$ 的一般嵌入曲线各次限制映射 $\nu_n$ 都有极大秩（单射或满射），统一了超曲面计数与 Green 猜想。 |
| 9 | `concept/minimal-syzygy-conjecture` | 在 $\rho=0$ 的临界 $(r,s)$ 下预言一般曲线每个 $g^r_d$ 的 $K_{p,2}$ 在 $p\le\frac{r-2s}{s+1}$ 时消没；$s=1$ 退化为 Green 猜想，$p=0$ 退化为定理 5.3。 |
| 10 | `concept/property-np` | 充裕线丛的 $p$ 阶线性合冲条件 $K_{i,q}=0\ (i\le p,\ q\ge2)$，把「理想由二次式生成、直到 $p$ 阶合冲线性」压成一个上同调消没。 |
| 11 | `concept/slope-of-effective-divisor` | 把 $\overline{\mathcal{M}}_g$ 上有效除子写成 $a\lambda$ 与边界除子的组合并取最小比值 $a/b$；斜率猜想预言它 $\ge 6+12/(g+1)$，而 Koszul 闭链正是造反例的机器。 |
| 12 | `example/degree-6-genus-3-quadric` | 在 $\mathfrak{I}_{6,3,3}$ 里 $\nu_2$ 失效当且仅当曲线落在二次曲面上；二次曲面上的曲线必为 $(2,4)$ 型、从而超椭圆，这是一个真除子条件。 |
| 13 | `example/enriques-babbage-petri` | Green 猜想 $p=1$ 的情形：非超椭圆曲线的 $K_{1,2}$ 消没等价于典范曲线由二次超曲面切出，即 EBP 定理；例外恰是超椭圆、三棱与光滑平面五次。 |
| 14 | `example/max-noether-theorem` | Green 猜想 $p=0$ 的情形：非超椭圆曲线的 $K_{0,2}$ 消没等价于典范曲线射影正规，即经典 Max Noether 定理。 |

### ch7（8）

| # | id | 一句话 |
|---|---|---|
| 15 | `concept/brill-noether-number` | 高秩理论的预期维数 $\beta=n^2(g-1)+1-k(k-d+n(g-1))$，给出每个分支的维数下界，但 $\beta\ge0$ 与非空性并不等价。 |
| 16 | `concept/dual-span` | 把 $(E,V)$ 换成 $(D_V(E),V')$（$D_V(E)^*=\ker(V\otimes\mathcal{O}\to E)$）的对合运算，把高秩问题化归为线丛问题，是 §6 处理 $k=n+1$ 的主力。 |
| 17 | `concept/existence-region-d0` | $d_0(n,k)$ 是使 $G(\alpha;n,d,k)$ 非空的最小次数，$U(n,d,k)$ 是其中 $E$ 稳定的部分；模型定理断言存在性只由 $d\ge d_0$ 与式 (1) 决定。 |
| 18 | `concept/model-theorem` | 对固定 $n\ge2,k\ge1$，存在性完全由 $\alpha>0$、$(n-k)\alpha<d$、$d\ge d_0$ 决定；这是整章的「理想图景」，已在若干情形被证明。 |
| 19 | `concept/petri-curve` | 若对每个线丛 $L$，$(L,H^0(L))$ 的 Petri 映射都单射则称 Petri 曲线；一般曲线都是，这类曲线上 $k=n+1$ 的存在性问题几乎完全解决。 |
| 20 | `concept/petri-map` | 由截面乘法给出的 $V\otimes H^0(E^*\otimes K)\to H^0(\mathrm{End}E\otimes K)$；其单射性与「$G$ 光滑且维数 $\beta$」等价，是 Petri 型定理的高秩版本。 |
| 21 | `example/example-genus-10-d0` | 例 7.5：$g=10$、$(2,12,4)$ 时 $d_0$ 只能为 $12$ 或 $13$——一般曲线为 $13$，$K3$ 上的某些 Petri 曲线为 $12$。 |
| 22 | `example/example-non-stability-large-alpha` | 例 5.3：$k$ 落在 $n+\frac{1}{g}(d-n)$ 与 $\frac{ng}{g-1}$ 之间时任何凝聚系对大 $\alpha$ 都不半稳定，而该区间确由 $(rg-r+1,2rg-2r+3,rg+1)$ 型、$E$ 稳定的例子取到。 |

## 二、sketch 清单（12 条）及原因

原则：章内有逐步证明的一律写 `complete`；原文只给引文/「立得」的写 `sketch` 并在 `gap_note` 里点明缺哪一步；只作文献定位的写 `reference`。

| 卡 | 定理 | 缺什么 |
|---|---|---|
| clifford-index | 定理 2.4 的推论 | 原文「由定理 2.4 立得」，未逐项验算 Serre 对偶后 $h^1(L_1)=h^0(K_C\otimes L_1^\vee)\ge2$ 与下标 $r_1+r_2-1=g-\mathrm{Cliff}-2$。 |
| greens-conjecture | 定理 2.4（Green–Lazarsfeld） | 非消没定理本身在 Green 1984，正文只给它在 $L=K_C$ 上的应用。 |
| koszul-cycle | 定理 3.5 | 秩计算与「$K_{p,2}=0\iff\phi$ 单射」原文给了；难的是 $\phi$ 延拓到 $\widetilde{\mathfrak{G}}^r_d$ 边界（极限线性系、容许覆盖、半稳定等价），需第 9 篇。 |
| koszul-duality | 定理 2.7 | 原文称其为定理 2.6 的推论，未写证明；缺逐项取对偶时 $\wedge^pM_L$ 的对偶分解与平移。 |
| property-np | 定理 2.7 的对偶应用 | 两处指标位移 $p\mapsto r-n-p$、$q\mapsto n+1-q$ 各需一次对偶，正文未写。 |
| slope-of-effective-divisor | $\mathcal{K}_{10}$ 是反例 | 类计算引 [FaPo05]；正文只给 $s(\overline{\mathcal{K}}_{10})=7<78/11$ 与 $42=\#W^4_{12}$。 |
| brill-noether-number | 引理 1.8 | 只引 [17]；缺「切空间 = Petri 核、障碍 = 上核」两步。 |
| petri-map | 引理 1.8 | 同上（两卡分工：β 侧讲维数，Petri 侧讲映射）。 |
| dual-span | 引理 6.1 | 只引 [12]；缺对 $D(L,V)$ 的真子系验证 $\mu_\alpha$ 不等式。 |
| existence-region-d0 | 引理 1.3 | 原文「由定义轻易推出」，未展开三条不等式的验证。 |
| max-noether-theorem | Max Noether 定理 | 本章只作经典引文（ACGH p.117），未证 $\mathrm{Sym}^2H^0(K_C)\to H^0(K_C^{\otimes2})$ 满射。 |
| example-non-stability-large-alpha | 例 5.3 前半 | 只引 [19, §7]；缺「由生成性造出更优斜率的真子系」这一步。 |

写 `complete` 的 12 处（供核对）：定理 2.6 的核丛复形、定理 2.8 的五步（对偶→复形→$\wedge^{p+1}M_L$ 对偶→RR→代入）、定理 2.7 的曲线特例位移、定理 3.5 的秩相等数值、例 5.2 的 $(2,4)$ 型论证、例 7.5 的五步判定、例 5.3 的参数代入算术等。

## 三、id / related 冲突与处理

1. **`max-noether-theorem` 的 type**：清单 id 为 `grassmann/example/max-noether-theorem`（例子卡）。初稿在 `property-np` 里误写成 `grassmann/concept/max-noether-theorem`，校验器报「无法解析」，已改为 example id。
2. **跨组 related 只能取磁盘上真实存在的 id**。甲/丙/丁组大量 id（`gv-sheaf`、`affine-grassmannian`、`gerbe-banded-by-mu-n`、`root-stack`、`koszul-cohomology` 等）在 `cards/` 下无文件，我一律不引用；跨组只用了已存在的种子卡 `grassmann/concept/alpha-stable-coherent-system`（例 5.3 卡）。其余跨章互链走 ch2↔ch7 实卡。
3. **`example-genus-10-d0` 被 4 张 ch2 卡引用**（`maximal-rank-conjecture`、`slope-of-effective-divisor`、`degree-6-genus-3-quadric`、`petri-curve`），它在批次 E 落盘前一直报「未解析」，落盘后自动清零——若日后有人改这个 id，这 4 张会同时断链。
4. **校验器的绝对路径正则 `[A-Za-z]:\\`** 会把形如 `$d:\text{…}$`、`$d:\exists…$`、`$\phi:\mathcal{A}$` 的公式误判成「本机绝对路径」。已把相关冒号改成 `\colon`（`existence-region-d0` 两处、`koszul-cycle` 一处），公式语义不变。
5. 例子卡的 `setup`/`computation` 必须是**字符串**而非 `{text: …}` 对象，且例子卡同样要求 `definition.text` 非空；首版按对象写被校验器判缺字段，已改。

## 四、存疑（5 条）

1. **ch02 式 (2) 的二项式**：正文 $h_X(d)=\sum(-1)^p\beta_{pj}\binom{n+d-j}{n}$，译注②认为应为 $\binom{n-1+d-j}{n-1}$。我采信译注（$X\subset\mathbb{P}^{n-1}$ 时 $S(-j)_d$ 的维数是后者），但未回查英文原刊；若原书把 $n$ 定义为 $\dim X+1$，原式自洽。
2. **定理 3.6 的斜率表达式**：$s=a/b_0=6f(s,p)/((p+2)s\,h(s,p))$ 中 $f,h$ 的具体形式在扫描件里较糊，卡里只保留可核对的结论 $6<a/b_0<6+12/(g+1)$ 与式 (5) 的虚类，未逐符号转录 $f,h$。
3. **猜想 5.4 的维数公式** $\dim\Sigma=\rho-1-|\mathrm{rank}\mathcal{E}_n-\mathrm{rank}\mathcal{F}_n|$：$-1$ 与绝对值的位置容易错位（负维数释为「空」），我照原文抄，未独立算例验证。
4. **例 7.5 中 $d_0$ 是否依赖曲线**：原文只说一般曲线上 $G(\alpha;2,12,4)=\emptyset$、$K3$ 上某些 Petri 曲线存在，从而 $d_0=12$ 或 $13$；但 $d_0=d_0(n,k)$ 在 §2 的定义是对某个 $\alpha$ 取最小 $d$，未声明是否随曲线变化。我在卡里按「依赖曲线」写，这正是模型定理不能覆盖 $k\ge n+2$ 的原因，但严格表述需作者澄清。
5. **ch07 定理 7.2 的 $d_2$**：$d_2$ 在 §7 出现，我按上下文称其为「定理 7.1 给出的临界值」并取 $g=10$ 时 $d_2=13$；定理 7.1 的具体形式未逐字核对，若 7.1 的 $d_2$ 定义含 $[\cdot]$ 取整，$g=10$ 的取值仍为 $13$，但一般 $g$ 的公式可能有别。
