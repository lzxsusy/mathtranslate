# ERRATA — 原文笔误与可疑之处登记

> 只登记**原文本身**的笔误/矛盾，不登记翻译问题。每条格式：`| 位置 | 原文 | 应是 | 依据 |`
> 另需在对应块的 .tex 里写 `% [Tutor Note: 原文笔误 …]` 批注。

| 位置 | 原文 | 应是 | 依据 |
|---|---|---|---|
| p2（§1.1 第 5 段） | "Borcherd's proof of monstrous moonshine [Bor92]" | "Borcherds' proof" | Richard Borcherds 于 1992 年证明魔群月光猜想（[Bor92] 即 Borcherds, *Monstrous moonshine and monstrous Lie superalgebras*）；姓氏拼写漏 s。页面上清楚可见 Borcherd's。 |
| p2（§1.1 第 6 段） | "has lead to some incredibly rich objects" | "has led to" | 动词 lead 的过去分词为 led；页面可见 "has lead to"。 |
| p5（定义 1.10 之后） | "and (at present) it unclear which one to take" | "it is unclear" / "it is not clear" | 缺系动词，句子不成立；页面可见 "it unclear"。 |
| p6（§1.4 概述段） | "before translating these structure into the bordism framework" | "this structure" 或 "these structures" | 指示词与名词数不一致；页面可见 "these structure"。 |
| p1（猜想 1.1 图注 式 (1)） | 箭头标签 "cocycle_{-n}"，而紧邻正文写作 "cocycle_n" | 二者用法自洽（下标随 degree $-n$ 变号），非笔误，仅记备查 | 900 dpi 裁图确认图内下标带负号、正文下标无负号。 |
| p3（例 1.3） | "isometry group $\R^d\rtimes\mathrm{Spin}(d)$ acting on $\R^n$" | 疑为 $\R^d$（刚性几何定义在 $\R^d$ 上） | 沿 ST11 记法 $n$ 可指环境维数，故仅登记为可疑，译文照排并加批注。 |
| p25（式 (51)） | 右式下指标印作 $k=-1$ | 疑为 $k\in\Z$（求和遍历所有 $k$，且 $H(k)$ 的定义与 $k$ 无关） | 页面图确认下指标为 "$k=-1$"；同段求和下标为 $k$ 遍历 $\Z$。 |
| p25（式 (51) 与紧接正文） | 式内 $(\mathrm{Cl}_2\C^{1|1})^{\otimes n/2}$，正文写 $\mathrm{Cl}_2(\C^{1|1})_\C$ | 同一双模的两种记号，原文本就不统一 | 页面图确认两处写法不同。 |
| p26（假设 4.18） | "There are map of stacks" | "There are maps of stacks" | 主谓数不一致。 |
| p27（注 4.15 后的 Sketch 段） | "Clifford algebra of loops with of Fourier numbers $k$ and $-k$" | 去掉多余的 "of" | 连写两个 of。 |
| p27（例 4.20 与 §1 末尾） | "For $X=X$ a smooth manifold"；"$H(M;\mathrm{MF})$" | 疑为 "$H(X;\mathrm{MF})$"（$M$ 未定义） | 同段其它式子均以 $X$ 为变量；仅登记可疑，照排。 |
| p16（式 (30)） | 动能项印作 $\|\dot x\|$（未平方） | 通常应为 $\|\dot x\|^2$（作用量里是动能） | 页面图确认没有平方号；译文照排并加批注。 |
| p18（注 3.19） | "with reflection structure inherited the $*$-structure" | "inherited from the $*$-structure"（缺 from） | 语法不成立。 |
| p19（注 3.24） | "it would suffice **to to** construct" | 去掉重复的 to | 连写两个 to。 |
| p22（式 (48) 及紧随正文） | 印作 $W_n(TM)$ | 按上下文应为 $W_k(TM)$（$W_k$ 是 (47) 中 $q^k$ 的系数，求和指标为 $k$） | 页面图确认字面是 $W_n$；否则被求和项与 $k$ 无关。照排 + 批注。 |
| p23 | 算子 "$rP=H^{(r)}_++H^{(r)}_-$" | 应为减号（由 (40) 得 $H^{(r)}_++H^{(r)}_-=rH^{(r)}$、$H^{(r)}_+-H^{(r)}_-=rP^{(r)}$） | 700 dpi 裁图逐字确认原文是「+」。照排 + 批注。 |
| p25（推论 4.13 证明） | $\bigl(\prod_{k>0}(1-q^k)\bigr)^{n}$ | 疑应为负指数 $-n$（由 $\eta(q)=q^{1/24}\prod(1-q^k)$ 代入得 $\prod(1-q^k)^{-n}$） | 1200 dpi 复核确无负号；两种写法系数均为整数，$\Z((q))$ 结论不变，仅登记可疑。 |
| p24（原文脚注 10） | "$\bar L_k=0$ for $k\in\Z$" | 字面过强，常见约定为 $k>0$（或 $L_k=\bar L_k=0$ 于 $k<0$） | 照排 + 批注。 |
| p12（式 (19) 第四行） | 第二个 $\alpha_A(\cup^{+}_t)$ | 按同一行第一个及对称性，应为 $\alpha_A(\cup^{-}_t)$ | 同行已有 $\cup^{+}_t\mapsto{}_{A\otimes\ol{A}}A$，第二个应配 $\cup^{-}_t$；照原样排 + 批注。 |
| 记号不一致（多处，非笔误） | 3.4/3.7 用上标 $\sHam^n,\SQM^n$，3.12 证明与式 (31) 用下标；式 (35) 写 $\mathrm{PU}^\pm(\cH)$、紧接正文写 $\mathrm{PU}^\pm(\cH_n)$；式 (21) 正文说 "the only spin manifold" 而图中是 spin$^c$；$\{\cH_\lambda\}_{\lambda\ge0\in\R}$；Thom 类次数 $w_1+W_3$（大写 W） | 原文自相矛盾，无法统一 | 均照原文排，批注说明。 |
| p7（图 1 图注） | \"colliding labels adds dimensions\" | \"add dimensions\"（主谓一致） | 复数主语加 adds 不通。 |
| p12 | \"the image of (17) are the topological field theories\" | \"is\" | 主语 image 为单数。 |
| p10（式 (11) 末两处） | $E(\cup^{+})$、$E(\cup^{+})$（无下标 $t$） | 依生成元记号应为 $E(\cup^{\pm}_t)$；同行 $E(\cap^{+}_t)$ 带下标 | 同式内记号不对称，照原文排。 |
| p13（式 (20) 第四行） | 第二个 $E(\cup^{+}_t)$ | 应为 $E(\cup^{-}_t)$（与式 (19) 同型） | 同一行第一个已用 $\cup^{+}_t$，第二列应配 $\cup^{-}_t$。 |
| p13（式 (20) 的 2-胞图） | 扭标作 $\alpha_n$ | 按本节正文应为 $\alpha_A$（同页写「$\alpha_A$-扭场论」） | 页面图确认图中下标为 $n$；照原文排 + 批注。 |
| p13（例 2.24） | \"a twisted spin field theory theory\" | 去掉重复的 theory | 连写两个 theory。 |
| p9（命题 2.7 的证明） | 先写 $\mathrm{BPU}(H)$（斜体 $H$）、后写 $\mathrm{BPU}(\cH)$ | 同一对象两种写法 | 非笔误，照原文排；统一用 $\cH$ 读。 |
