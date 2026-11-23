# A06 校对报告

## 一、范围与工作量

| 文件 | 原书印刷页 | 行数 | 修订 | 译者注 |
|---|---|---|---|---|
| `src\chapters\section-11-a.tex` | 150–151 | 51 | 1 | 1 |
| `src\chapters\section-11-bd.tex` | 152–157 | 163 | 0 | 2 |
| `src\chapters\section-11-ef.tex` | 158–161 | 129 | 1 | 2 |
| `src\chapters\section-11-gh.tex` | 162–166 | 118 | 1 | 3 |
| `src\chapters\section-11-i.tex` | 167–169 | 61 | 0 | 4 |
| `src\chapters\section-11-jl.tex` | 170–174 | 105 | 1 | 3 |
| 合计 | 150–174（25 页） | 727 | 4 | 15 |

工作方式：逐段对照 `work\en\bundles\A06.txt`（印刷页 150–174）；对含公式的段落回到 `work\pages\pNNN.png` 原页图核对符号、上下标、$\mp$ 约定与正负号；术语一律对照 `术语表.csv`。全部 15 条注均以 nLab 页面为来源，已用 web_fetch 实际打开（HTTP 200，2026-11-15 访问），未引任何二手博客或 AI 摘要。

六个文件均通过 `work\tools\check.ps1`，输出 `OK`：

```
OK section-11-a.tex
OK section-11-bd.tex
OK section-11-ef.tex
OK section-11-gh.tex
OK section-11-i.tex
OK section-11-jl.tex
```

## 二、译文修订表

| # | 文件:行 | 原文 | 改文 | 理由 |
|---|---|---|---|---|
| 1 | `section-11-a.tex`:46–48 | 提一下另一种可能的约定，也许有助于理解：将\eref{11.2}右侧换成<br>`\[(-1)^{\dim(\operatorname{coker}D_2)\cdot\operatorname{index}(D_1)}\bigwedge_iw_{1,i}^\vee\wedge\cdots\]` | 提一下另一种可能的约定，也许有助于理解：将\eref{11.2}右侧换成（即去掉符号）<br>`\[\bigwedge_iw_{1,i}^\vee\wedge\bigwedge_iw_{2,i}^\vee\otimes\bigwedge_iv_{1,i}\wedge\bigwedge_iv_{2,i}\]` | 原书此处说的是「改用另一约定（removing the sign）」，即把式 (11.2) 的符号因子去掉。旧译既保留 $(-1)^{\cdots}$ 因子，又未译出「去掉符号」，与「另一种约定」自相矛盾，读者无法判断到底改了哪里。补出「（即去掉符号）」并删去符号因子后，与下文「这样得到另一个线丛 $\underline{\det}'$」逻辑一致。 |
| 2 | `section-11-gh.tex`:32 | 类对 $(\mu,\allowbreak w_2)$ 由一个到 Eilenberg–MacLane 空间乘积的映射表示： | 这一对类 $(\mu,\allowbreak w_2)$ 由一个到 Eilenberg–MacLane 空间乘积的映射表示： | 「类对」在中文里不成词（原文 the pair $(\mu,w_2)$），且与后半句「由一个……映射表示」衔接生硬。改为「这一对类」后句子成立，指代也明确了是上两句刚定义的两个类。 |
| 3 | `section-11-ef.tex`:123 | 更确切地说，来自 $\alpha(s)$ 的零空间非零的时刻 $s$。 | 更确切地说，来自使 $\alpha(s)$ 的零空间非平凡的那些 $s$。 | 原文为 those $s$ where $\alpha(s)$ has a nonempty null space。零空间是子空间，「非零」不适用于子空间（零空间永远含零向量），应为「非平凡（非零维）」；主语也应是 $s$ 而非「时刻」。 |
| 4 | `section-11-jl.tex`:26 | 这在同伦层面回答了我们的问题，虽大体令人满意，却并不完全令人满意。 | 这在同伦层面回答了我们的问题，虽大体令人满意，但并不完全。 | 原文 mostly but not entirely satisfactory。旧译「虽……却并不完全令人满意」重复「令人满意」两次，语感滞涩；删去重复后与原文的让步结构一致，且「并不完全」保留了原文留有余地的语气。 |

## 三、译者注表

| # | 文件:行 | 原书页 | 主题 | 来源级别 |
|---|---|---|---|---|
| A06-01 | `section-11-a.tex`:11 | 150 | 行列式线 / 行列式线丛（$\lambda(\ker D)\otimes\lambda(\operatorname{coker}D)^\vee$） | A |
| A06-02 | `section-11-bd.tex`:34 | 152 | 谱流（自伴 Fredholm 族的整值不变量，APS 1975） | A |
| A06-03 | `section-11-bd.tex`:71 | 153 | 谱流 = Maslov 指标（Robbin–Salamon 两文） | B |
| A06-04 | `section-11-ef.tex`:2 | 158 | Maslov 类 = 万有类 $u\in H^1(\mathrm{LGrass})$ 的拉回 | A |
| A06-05 | `section-11-ef.tex`:91 | 160 | 穿越型（crossing form）与路径 Maslov 指标 | B |
| A06-06 | `section-11-gh.tex`:36 | 163 | 抽象膜：$K(\Z,1)$ 记 $\mu$、$K(\Z/2,2)$ 记 $w_2$，纤维 $\Z\times\RP^\infty$ | A |
| A06-07 | `section-11-gh.tex`:64 | 164 | 定向空间 $o$ = 行列式线 + 定向 | A |
| A06-08 | `section-11-gh.tex`:113 | 165 | 膜结构使环路的 $\Z$ 与 $\Z/2$ 障碍同时为零 | A |
| A06-09 | `section-11-i.tex`:2 | 167 | $\operatorname{Pin}_\pm$ 两种约定（$q_\pm=\pm\sum(x^i)^2$） | A |
| A06-10 | `section-11-i.tex`:2 | 167 | Pin 群的定义：Clifford 单位群中单位向量之积生成 | B |
| A06-11 | `section-11-i.tex`:18 | 168 | Pin 结构的障碍 $w_2$ 与 $H^1(B;\Z/2)$ 仿射空间 | A |
| A06-12 | `section-11-i.tex`:35 | 169 | 扭曲 Pin / 扭曲 spin 结构：障碍、$(\infty,1)$-拉回、gerbe | A |
| A06-13 | `section-11-jl.tex`:11 | 170 | 平方相位与 $\det^2:U(n)\to U(1)$（$\Z/2$ 与 $\Z$ 信息） | A |
| A06-14 | `section-11-jl.tex`:48 | 172 | 平移 $S^\sigma$ 与 $\Z$ 分次（绝对指标） | A |
| A06-15 | `section-11-jl.tex`:104 | 174 | 定向算子：指标 = 绝对指标，行列式线 = 定向空间 | B |

注文均 121–180 汉字，一段，无 `%`、无 `\begin/\end`、无行间公式；同段最多 2 条（`section-11-i.tex` 第 2 段），无「连续三句各一条」的情况。

## 四、存疑未改

| 位置 | 原文 | 疑点 | 已查证 | 建议 |
|---|---|---|---|---|
| `section-11-i.tex`:60 | $\det(D_{D,\rho})\cong\lambda^{\mathrm{top}}(\Lambda_+)\otimes(\Lambda_-)^{\otimes(1+k)}$ | 第二个因子缺 $\lambda^{\mathrm{top}}$，与 $k=-1$ 时 $\det\cong\lambda^{\mathrm{top}}(\Lambda)=\lambda^{\mathrm{top}}(\Lambda_+)\otimes\lambda^{\mathrm{top}}(\Lambda_-)$ 不符 | 英文原文同一处亦作 `λ^top(Λ_+) ⊗ (Λ_-)^{⊗(1+k)}`（`bundles/A06.txt` 印刷页 168），非译者所加 | 已列入第五节；若作者有勘误表，应据以补 $\lambda^{\mathrm{top}}$；否则保留原样，勿擅改 |
| `section-11-jl.tex`:21 | 构成 $H^0(B)\times H^1(B;\Z/2)$ 上的仿射空间 | $H^0(B)$ 未标系数，按上下文应为 $H^0(B;\Z)$（整值局部常值函数，作用为给分次加整数） | 英文原文亦作 $H^0(B)\times H^1(B;\Z/2)$ | 已列入第五节；译文从原文，不补 $\Z$ |
| `section-11-ef.tex`:2 | 其无定向线性 Lagrangian 子空间的 Grassmann 流形 | 「无定向」是否宜作「未定向」 | 全书 grep：「无定向」共 2 处（本处与 `section-13-c.tex`），「未定向」0 处，用法自洽 | 保留，保持一致，不擅改 |
| `section-11-i.tex`:40 | 引理 \sr{st:11.7}{11.7}、\sr{st:11.12}{11.12} | 与全文 `\stref{引理}{11.7}` 体例不统一 | 二者渲染结果相同（均为「引理 11.7」超链接），非错误 | 留待统一体例时处理，本次不改，避免无谓 diff |

## 五、原书可疑处

1. `section-11-i.tex`:60（原书印刷页 168，Lemma 11.17 证明末）：$\det(D_{D,\rho})\cong\lambda^{\mathrm{top}}(\Lambda_+)\otimes(\Lambda_-)^{\otimes(1+k)}$。第二个因子应为 $\lambda^{\mathrm{top}}(\Lambda_-)^{\otimes(1+k)}$。理由：$k=-1$ 的特例即 $\Lambda_-$ 的定向给出同构 $\det\cong\lambda^{\mathrm{top}}(\Lambda)=\lambda^{\mathrm{top}}(\Lambda_+)\otimes\lambda^{\mathrm{top}}(\Lambda_-)$；且该式在 $k=0$ 时应回到 Lemma 11.7 的 $\det\cong\lambda^{\mathrm{top}}(\rho(0))$，只有补上 $\lambda^{\mathrm{top}}$ 才两侧次数一致。疑为原书漏排。
2. `section-11-jl.tex`:21（印刷页 170）：膜结构的同构类构成「$H^0(B)\times H^1(B;\Z/2)$ 上的仿射空间」。$H^0(B)$ 应理解为 $H^0(B;\Z)$，因为平移量是整数值的局部常值函数；原文省略系数，易被误读为实值函数。属记号省略，非实质错误。

## 六、通读小结

本区段（原书印刷页 150–174）是第 11 节的技术核心：从行列式线与谱流出发，经 Lagrangian Grassmann 流形的分层与穿越型，建立路径 Maslov 指标 $I_Z$、$I_H$ 与 $\bar\partial$ 算子指标、行列式线之间的对应；随后以抽象膜 $\operatorname{Gr}(V)^\#$ 统一 Maslov 指标与 $w_2$，再用 Pin 结构、扭曲 Pin 结构把定向问题几何化，最后以二次复体积形式、平方相位与平移运算收束，并把命题 11.13 推广为定向算子的一般陈述。译文整体质量高：公式系统（(11.1)–(11.39)）的符号、上下标、$\mp$ 约定、$e_j=|\Sigma^-\cap\hat C_j|$、$\Z\times\RP^\infty$ 与 $\Z\times L\RP^\infty$ 的纤维、$n=1,2$ 的例外群、$(11.33)$ 的 $T(w_2)+kU(\mu)$、$(11.35)$ 的向下取整，都逐条与原书核对无误；术语与术语表一致（分次、穿越型、定向空间、行列式线、谱流、膜结构、扭曲 Pin 结构等）。本次只改 4 处确凿问题：一处符号约定未译出致自相矛盾（a:46），两处中文不成词或主语错位（gh:32「类对」、ef:123「零空间非零」），一处重复冗赘（jl:26）。15 条译注集中在六条主线上：行列式线、谱流与 Maslov 指标、穿越型、抽象膜的两类障碍、Pin 与扭曲 Pin 结构、平方相位与 $\Z$ 分次，全部以 nLab 实取页面为据。原书另有两处疑似笔误（$\lambda^{\mathrm{top}}$ 漏排、$H^0(B)$ 缺系数），已单列而不擅改。另需说明，11f 的 Arnol'd 分层与 11g 的上半平面变体是 11l 的局部模型：正文用 (11.18)–(11.19) 把算子沿 $t$ 拆成 Fourier 分量，再与穿越型的符号逐项对应，这种「把分析问题化为线性代数」的思路在本区段反复出现，译文处理得当；11h 用 Postnikov 覆盖代替「取覆盖」的措辞，也准确传达了原书在低维的例外处理。尚有两点可留待全稿统一：`\sr` 与 `\stref` 体例混用；11i 与 11j 之间 $\rho$（环路）与 $\nu$（边界映射）两个记号并存，读者需自行对照，若后续加索引可在术语表注明。
