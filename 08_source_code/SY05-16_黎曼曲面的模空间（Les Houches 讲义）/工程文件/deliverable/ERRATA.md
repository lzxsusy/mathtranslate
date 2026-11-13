# ERRATA.md — 原文笔误 / 排版瑕疵登记表

> 规则：正文**照原文译**，此处登记并给出正确形式与判断依据。
> 表中"位置"用原文页码 + 公式/环境编号定位。由各块负责人上报，Lead 汇总核对。

## 一、确定的笔误（正文照排，批注指出）

| # | 页码 | 位置 | 原文写法 | 正确写法 | 判断依据 |
|---|---|---|---|---|---|
| 1 | p.10 | (2.19) 之后那句 | "Since taking **cap** products in cohomology (i.e. wedges of differential forms) corresponds to taking **cup** products in homology (i.e. intersection of subvarieties)…" | 应为 "**cup** products in cohomology（即微分形式的外积）对应 **cap** products in homology（即子簇相交）" | ①同页 (2.17) 后的括注已写明 cap↔子簇相交、cup↔形式外积；②上同调的乘法是 cup 积，cap 积是上同调与同调的配对。原文把两者互换了 |
| 2 | p.10 | 末段 | "…the preimages of the nodes on $\Sigma_i$" | 应为 $\Sigma_v$ | 同一句前半已定义 $g(v)$ 是 $\Sigma_v$ 的亏格，指标 $v$ 遍历分支 $\Sigma_1,\dots,\Sigma_k$；$\Sigma_i$ 未定义 |
| 3 | p.14 | "The easiest case is that of a stable graph $\Gamma$ with a single edge $e$…" 段末 | "…the edge is non-separating (i.e. a loop) or it is." | 缺宾语，应为 "or it is separating." | 紧接的两小节标题正是 "Non-separating edge" 与 "Separating edge" |
| 4 | p.14 | 倒数第二段 | "Notice how the above terms correspond**s** to the terms…" | correspond | 复数主语，主谓一致 |
| 5 | p.16 | (2.36) 前一段 | 局部写法 $(\Sigma,h)\mapsto(\Sigma,h)$ 的记号里 $r$ 事先未定义 | 同原文（$r=m-n$ 在 (2.37) 下方才给出） | "先用后定义"的写法，非笔误 |
| 6 | p.36 | (3.52) | 分母 $(t^{\mu_i})^{2g-2+n}$：$t$ 上标 $\mu$、下标 $i$ 并列 | 严格应作 $t^{\mu_1}$（或 $t^\mu$） | $\delta_{\mu_1,\dots,\mu_n}$ 已强制诸 $\mu_i$ 相等，无实质歧义，属记号疏忽 |
| 7 | p.30 | (3.24) | 同一符号 $\mathcal{V}^{g,\ell}_{g;\mu_1,\dots,\mu_n}$ 既表示 Verlinde 丛、又表示其 Chern 特征（等号左端） | 丛可另记 $\mathbb{V}$ 以示区别 | 同一个式子左右两端应是不同对象 |
| 8 | p.30 | (3.23)/(3.24) | 上标 "$g,\ell$" 中的 $g$ 与下标 $g$ 重复 | 文献通常只在上标标 level $\ell$ | 记号冗余，疑为笔误 |

## 二、原文排印 / 拼写问题（不构成数学错误，仅记录）

| # | 页码 | 情况 | 处理 |
|---|---|---|---|
| 9 | p.9 | 原文用 "smoothening"（非标准拼法，通常作 smoothing） | 统一译"光滑化"，批注说明 |
| 10 | p.37 | (3.60) 下方 "$B_{m+1}(0)=B_{m+1}(1)=B_{m+1}$" 仅对 $m+1\ge 2$ 成立（$B_1(0)=-\tfrac12$，$B_1(1)=+\tfrac12$） | 求和自 $m=1$ 起，不影响 (3.60)；批注说明 |
| 11 | p.36 | (3.57) 末尾原文无句点、(3.58) 有句点 | 照原文 |
| 12 | p.43–46 | [EGGGL] 标题 "asymtotics" 为原文拼写；[Mum83] 的 doi 原文缺 "10." 前缀 | 照录，不擅改 |
| 13 | p.12 | "…$h^1(\Gamma)$ denotes the first Betti number (i.e. the number of faces) of $\Gamma$" 措辞不严（一般图没有"面"，只有平面嵌入才有） | 照译，批注给出判据：$h^1(\Gamma)=|E|-|V|+1$ 即独立圈数 |
| 14 | p.7 | Exercise 2.2 后的 Riemann 德文引文，底本未注出处 | 译为中文并批注说明 | 
| 15 | p.7 | "Hint." 前原文有一个小灯泡图形符号 | 以"提示."代之，不造图标 |

## 三、底本结构上的特殊情况（已在正文处理，非笔误）

| # | 情况 | 处理 |
|---|---|---|
| 16 | (3.9)–(3.12)、(3.15) 五处"编号公式"在原文中是**图示**（曲面粘合图 / 配边图）而非代数式 | 保留 `equation`+`\tag` 以维持编号真值，式内以〔原文此处为图示：…〕文字转述 |
| 17 | (2.26)(2.27)(2.28)(2.29)(2.31) 同样是带编号的**图示** | 同上，式内文字转述稳定图内容 |
| 18 | 原文上同调次数一贯写**实次数**（$H^{2\bullet}$、$H^{2(2g-2+n)}$ 等），而 $D^r_{g;\mu}$ 是复次数 | 照原文，勿误判为错；批注说明 |
| 19 | §2.2、§2.3、§3.1、§3.2、§3.3 五个小节标题在原文中落在页面中部（其后紧跟正文，其前是上一小节的收尾） | 由对应块在正文流中就地排版，与原文位置一致 |


## 四、补充登记（第二批上报）

| # | 页码 | 位置 | 原文写法 | 正确写法 | 判断依据 |
|---|---|---|---|---|---|
| 20 | p.16 | §2.3 标题后第 2 段 | "we shall always omit the **cap** product since the **cap** product of even-degree cohomology classes is commutative" | 两处均应为 **cup** product | 上同调类之间只有杯积（cap 积是同调与上同调的配对，无"交换性"可言）；同页前文刚说推前 "does not respect the cup product"。与第 1 条 p.10 的 cap/cup 互换是同一处系统性笔误 |
| 21 | p.21 | (2.62) 三行、p.23 (2.74)、p.25 (2.75)(2.77) | 公式末尾的逗号在 PDF 中印在右上角（形如 1/(λ_i+λ_j)′ ,） | 普通逗号 | 疑为源文件遗留的 `\prime` 或标点抬高；译文排普通逗号，未复制抬高位 |
| 22 | p.22 | "…Bouchard's course [Bou26]!!" | 结尾两个感叹号 | 单个感叹号 | 修辞性冗余，照录并批注 |

## 五、未声明的约定（非笔误，仅批注）

| # | 页码 | 情况 | 处理 |
|---|---|---|---|
| 23 | p.20 | (2.61) 求和项 $(|\eps|-2)!$ 在 $|\eps|<2$ 时无定义 | 须把这类项视为零（否则 $n=1$ 算不出 $1/24$）；批注给出 3 组数值核验 |
| 24 | p.22 | 双阶乘只给出 $0!!=1!!=1$，但 (2.67) 的 $k=0$ 项与 (2.73)/(2.78) 的 $d=0$ 项用到 $(-1)!!=1$ | 由 $m!!=m(m-2)!!$ 在 $m=1$ 处即得；批注说明 |
| 25 | p.36 | 脚注 "In the remaining part of this section, we work over $\C$ rather than $\Q$." 是原文全文第 4 条脚注 | 译本 footnotes 自动编号与原文不同，批注说明 |


## 六、第三批上报（Block G / Block I）

| # | 页码 | 位置 | 原文写法 | 正确写法 | 判断依据 |
|---|---|---|---|---|---|
| 26 | p.31–32 | §3.2 首段 | "…but should involve specific combinations **ψ-classes**." | "specific combinations **of** ψ-classes" | combinations 后须接 of（脱漏介词） |
| 27 | p.38 | (4.1) 集合条件第二行 | "with $n$ labelled geodesics boundaries" | "with $n$ labelled **geodesic** boundaries" | 名词作定语用单数 |
| 28 | p.39 | Figure 15 图注 | "$\alpha_p$ **intersect** $\partial_1\Sigma$ and itself respectively" | "$\alpha_p$ **intersects** …" | 主谓一致（单数主语） |
| 29 | p.42 | 正文 | "remodelling"（英式）与文献 [BKMP09] 标题 "Remodeling"（美式）不一致 | — | 拼写变体，非笔误；批注说明 |
