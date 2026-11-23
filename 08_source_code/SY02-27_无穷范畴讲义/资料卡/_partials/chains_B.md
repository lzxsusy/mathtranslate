### 链：滤过性为何恰好等价于"余极限与有限极限交换"

**问题**　第 10 讲把"滤过"定义为任意有限图都能延拓出余锥，随后断言小 ∞-范畴 $\cC$ 滤过当且仅当 $\colim\colon\Fun(\cC,\Grpd_\infty)\to\Grpd_\infty$ 保持有限极限。为什么"延拓余锥"这种组合条件，恰好刻画了余极限与有限极限的交换？

**起点**　`SY02-27.stmt.10.2.1`（第 10 讲 p3）：$\cC$ 滤过指任意有限图 $u\colon K\to\cC$ 都能延拓为 $K^{\triangleright}\to\cC$；概念卡 `SY02-27.concept.filtered-infinity-category`（第 10 讲 p3）。

**步骤**

1. 先把"任意有限图"约化为"任意球面边界图"：`SY02-27.stmt.10.2.5`（第 10 讲 p3，Ker.02Q0）断言 $\cC$ 滤过当且仅当任意 $u\colon\partial\Delta^{n}\to\cC$ 都能延拓为 $(\partial\Delta^{n})^{\triangleright}\to\cC$。**warrant**：有限单纯集由有限个单形粘成（`SY02-27.concept.finite-simplicial-set`，第 10 讲 p1），粘接时的相容性正是一次次填球面；故只需检验球面这一族图。
2. 再把"保持有限极限"约化为"保持纤维积与终对象"：`SY02-27.stmt.10.1.11` 与 `SY02-27.stmt.10.1.13`（第 10 讲 p1–p2）给出 (i) 容许有限极限 ⇔ (ii) 有纤维积与终对象 ⇔ (iii) 有有限积与等化子。**warrant**：有限极限由这两类基本极限生成，逐点检验即得全称情形。
3. 用球面延拓逐点检验上述两类极限的交换性，得 `SY02-27.stmt.10.3.1`（第 10 讲 p4，Ker.05XS）：小 $\cC$ 滤过 ⇔ $\colim$ 保持有限极限。**warrant**：球面 $\partial\Delta^{n}$ 正是 $\Fun(\cC,\Grpd_\infty)$ 中表达"纤维积锥"的指标，延拓存在性等价于相应的极限锥在 $\Grpd_\infty$ 中仍为极限锥。
4. 把"有限极限"减弱为"有限积"，得到筛性：`SY02-27.stmt.10.4.1`（第 10 讲 p5）定义 $K$ 筛为对角函子 $K\to K^{I}$ 对任意有限集 $I$ 终结，`SY02-27.stmt.10.5.1`（第 10 讲 p6，HTT.5.5.8.11）断言小 $\cC$ 筛 ⇔ $\colim$ 保持有限积。**warrant**：对角函子终结 ⇔ 常值图 $K\to\cC$ 的余极限是终对象，即 $\colim$ 把常值有限积图送到积。
5. 对照两个结论：滤过要求所有有限图，筛只要求有限集指标的对角图，故滤过 ⇒ 筛（第 10 讲 p5 例 4.4）；反向不成立的例子是 $\Delta_{\le1}^{\op}$：它是经典筛的普通范畴，作为 ∞-范畴却不筛（第 10 讲 p5 练习 4.8）。**warrant**：该例说明"经典筛"与"∞-筛"严格弱于滤过，因而两个交换性定理不能互相替代。

**收口**　两条定理合起来给出"滤过 ⇔ 与有限极限交换、筛 ⇔ 与有限积交换"的精确对偶；这正是第 10 讲附录 A（命题 A.1 及其后的三个口号：$\text{small colimits}=\text{small filtered}+\text{finite}$ 等，第 10 讲 p6–p7）的技术核心。

**反事实**　若只要求 $\cC$ 是"有向偏序集"（普通范畴的滤过），而不要求高阶连通性，则球面 $\partial\Delta^{2}$ 之类的二维延拓可能失败，$\colim$ 会在纤维积处失效——第 10 讲 p4 Warning 3.2 指出把 $\Grpd_\infty$ 换成一般 ∞-范畴后 Thm 3.1 可能不成立，正是这一反事实的实例。

### 链：从"展示可表"到 Yoneda 引理，再到余完备化

**问题**　第 11 讲先给出可表函子的 $\eta\in F(x)$ 定义，随后把可表性重述为左 Kan 扩张，再证明 Yoneda 引理，最后断言预层 ∞-范畴 $\PShv(\cC)$ 是 $\cC$ 的自由余完备化。这四步为什么是同一条论证，而不是四个独立命题？

**起点**　`SY02-27.stmt.11.1.1`（第 11 讲 p1）：$\eta\in F(x)$ 展示 $F$ 被 $x$ 表示，指复合 $\Maps_{\cC^{\op}}(x,y)\to\Maps(F(x),F(y))\xrightarrow{\mathrm{ev}_\eta}F(y)$ 对任意 $y$ 是等价；概念卡 `SY02-27.concept.exhibits-representation`、`SY02-27.concept.representable-functor`（第 11 讲 p1）。

**步骤**

1. 把"展示"翻译成左 Kan 扩张：`SY02-27.stmt.11.2.2`（第 11 讲 p3）断言 $\eta$ 展示 $F$ 被 $x$ 表示 ⇔ (i) 每个 $\Maps_{\cC}(x,y)$ 本质小，(ii) $\eta$ 展示 $F$ 为常值 $\{*\}$ 沿 $x\colon\Delta^{0}\to\cC^{\op}$ 的左 Kan 扩张，即 $(\LKE_x\{*\})(y)\simeq\colim_{\Maps(x,y)}\{*\}$。**warrant**：$\colim_{\Maps(x,y)}\{*\}$ 就是 $\Maps(x,y)$ 的 $\pi_0$-型对象，逐点等价即定义中的复合可逆；概念卡 `SY02-27.concept.left-kan-extension`（第 11 讲 p3）。
2. 由左 Kan 扩张的泛性读出 Yoneda 引理：`SY02-27.stmt.11.3.1`（第 11 讲 p4）给出等价 $\Maps_{\Fun(\cC^{\op},\Grpd_\infty)}(h_x,G)\xrightarrow{\simeq}\Maps(h_x(x),G(x))\xrightarrow{\mathrm{ev}_{\id_x}}G(x)$，其中 $h_x=\Maps_{\cC}(-,x)$。**warrant**：$h_x$ 是 $\{*\}$ 沿 $x$ 的左 Kan 扩张（`SY02-27.concept.yoneda-lemma`，第 11 讲 p4），从 $h_x$ 到 $G$ 的自然变换由 $h_x$ 的泛性唯一决定，取值在 $\id_x$ 处。
3. 固定 $G=h_y$ 得 Yoneda 嵌入全忠实：`SY02-27.stmt.11.4.8`（第 11 讲 p6）断言 $\cC\to\Fun(\cC^{\op},\Grpd_\infty)$，$x\mapsto\Maps_{\cC}(-,x)$ 全忠实、本质像恰为可表预层。**warrant**：把步骤 2 的等价两边取 $G=h_y$，再用 $h_y(x)=\Maps(x,y)$ 即得 $\Maps(h_x,h_y)\simeq\Maps(x,y)$。
4. 用"每个预层都是可表预层的余极限"完成延拓：`SY02-27.stmt.11.5.2`（第 11 讲 p7，Ker.04BE）断言 Yoneda 嵌入 $\iota\colon\cC\to\PShv(\cC)$ 展示 $\PShv(\cC)$ 为 $\cC$ 的余完备化，即任意有小余极限的 $\cD$，$\LFun(\PShv(\cC),\cD)\to\Fun(\cC,\cD)$ 是等价。**warrant**：每个 $M\in\PShv(\cC)$ 有典范分解 $M\simeq\colim_{(h_x\to M)}\iota(x)$（第 11 讲 p7 注 5.5），故保持小余极限的函子被其在 $\iota$ 的像上的取值唯一决定，存在性由逐点左 Kan 扩张给出（`SY02-27.concept.cocompletion`，第 11 讲 p7）。
5. 顺带得到生成性：`SY02-27.stmt.11.5.2` 的证明同时说明 $\PShv(\cC)$ 由 $\iota$ 的像在小余极限下生成（第 11 讲 p7 推论 5.4）。**warrant**：步骤 4 的分解式对每个对象成立，故生成性自动成立。

**收口**　"展示可表（定义）→ 左 Kan 扩张（重述）→ Yoneda 引理（泛性）→ 全忠实（特例）→ 余完备化（延拓）"构成一条完整的推理链：可表性是 Yoneda 嵌入的像，而 Yoneda 嵌入的泛性就是自由余完备化。

**反事实**　若 $\cC$ 不本质小，则注 5.5 的余极限 $\colim_{(h_x\to M)}$ 不是小余极限，步骤 4 的"逐点左 Kan 扩张"构造失效，`SY02-27.stmt.11.5.2` 的假设（$\cC$ 本质小）不可去掉。

### 链：稳定 ∞-范畴如何同时产出三角结构与同调代数

**问题**　第 15 讲用"纤维序列 = 余纤维序列"定义稳定 ∞-范畴，第 16 讲在其上装 t-结构、心与同调函子，第 17 讲又断言链复形的 $\mathrm{D}(A)$ 是稳定 ∞-范畴且其心就是 $A$。稳定性这一条公理，凭什么能同时支撑三角运算与长正合序列？

**起点**　`SY02-27.stmt.15.1.5`（第 15 讲 p1）：$\cC$ 稳定指它是带点的、每个态射有纤维与余纤维、且一个三角是纤维序列当且仅当它是余纤维序列；概念卡 `SY02-27.concept.stable-infinity-category`（第 15 讲 p1）。

**步骤**

1. 稳定性给出三角结构：`SY02-27.stmt.15.1.8`（第 15 讲 p1）断言 $\Sigma$ 全忠实 ⇔ 任一余纤维序列都是纤维序列 ⇔ 任一推出方块都是拉回方块；`SY02-27.stmt.15.2.10`（第 15 讲 p4）进一步断言 $\mathrm{h}\cC$ 连同 $[1]=\Sigma$ 与特异三角（`SY02-27.stmt.15.2.9`，第 15 讲 p4）构成三角范畴。**warrant**：纤维—余纤维序列重合使 $X\to Y\to Z\to X[1]$ 的提升唯一到同伦，逐条验证三角公理即得（概念卡 `SY02-27.concept.triangulated-category`，第 15 讲 p4）。
2. 在稳定 $\cC$ 上装 t-结构：`SY02-27.stmt.16.1.2`（第 16 讲 p1）定义 $(\cC^{\le0},\cC^{\ge0})$ 满足四条公理，并给出 $\cC^{\le n}=\cC^{\le0}[-n]$ 与对象沿两层的纤维—余纤维分解；概念卡 `SY02-27.concept.t-structure`（第 16 讲 p1）。**warrant**：分解公理用的正是步骤 1 中"纤维序列 = 余纤维序列"，故截断 $\tau^{\le n},\tau^{\ge n}$ 有函子性。
3. 心是 Abel 范畴：`SY02-27.stmt.16.1.9`（第 16 讲 p2）断言心 $\cC^{\heartsuit}$ 是通常的 Abel 范畴，且短正合序列恰是含于心中的纤维—余纤维序列。**warrant**：先在引理 1.7 中把心化约为通常范畴 $\mathrm{h}\cC^{\le0}\cap\mathrm{h}\cC^{\ge0}$，再引用三角范畴的心的熟知结论（概念卡 `SY02-27.concept.heart`，第 16 讲 p2）。
4. 同调长正合序列：`SY02-27.stmt.16.2.15`（第 16 讲 p4）断言对任意纤维—余纤维序列 $X'\to X\to X''$，有长正合序列 $\cdots\to H^{n}(X')\to H^{n}(X)\to H^{n}(X'')\xrightarrow{\delta}H^{n+1}(X')\to\cdots$。**warrant**：把序列逐次截断平移成特异三角，用步骤 3 的心的正合性得逐段正合，连接态射 $\delta$ 由 $X''\to X'[1]$ 诱导（概念卡 `SY02-27.concept.cohomology-functor`，第 16 讲 p3）。
5. 两个计算性收口：谱 $\infty$-范畴 $\mathrm{Sptr}$ 的 t-结构紧生成、左右完备，且 Eilenberg–MacLane 谱函子给出 $\Ab\simeq\mathrm{Sptr}^{\heartsuit}$（`SY02-27.stmt.16.5.2`，第 16 讲 p7）；导出 ∞-范畴 $\mathrm{D}(A)$ 上由 $H^{n}$ 的消没条件确定的 t-结构可及、右完备，且 $H^{0}$ 诱导 $\mathrm{D}(A)^{\heartsuit}\simeq A$（`SY02-27.stmt.17.3.1`，第 17 讲 p5）。**warrant**：前者用 $\Spc_{*}$ 紧生成与 $\Omega^{\infty}$ 检测零对象；后者用截断与 $H^{n}$ 有界性验证四条公理（概念卡 `SY02-27.concept.derived-infinity-category`，第 17 讲 p2）。

**收口**　稳定性（纤维列 = 余纤维列）→ 三角结构（步骤 1）→ t-结构与截断（步骤 2）→ Abel 心与长正合序列（步骤 3–4）→ 具体计算 $\mathrm{Sptr}^{\heartsuit}\simeq\Ab$、$\mathrm{D}(A)^{\heartsuit}\simeq A$（步骤 5）。同调代数不是额外结构，而是稳定性加 t-结构的产物。

**反事实**　若 $\cC$ 仅有三角结构而非稳定 ∞-范畴（例如只在 $\mathrm{h}\cC$ 层面工作），则截断 $\tau^{\le n}$ 不再是函子性的、纤维—余纤维分解不唯一到同伦，步骤 4 的连接态射 $\delta$ 无从定义；这正是第 16 讲坚持在 ∞-范畴层面而非同伦范畴层面陈述 t-结构公理的原因。
