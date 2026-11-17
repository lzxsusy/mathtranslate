# -*- coding: utf-8 -*-
"""概念卡数据（四）：计算与边界。"""
def S(text, why): return {"text": text, "why": why}
def T(name, statement, status, steps, source, gap=""):
    return {"name": name, "statement": statement,
            "proof": {"status": status, "steps": steps, "gap_note": gap},
            "source": source}
W = "威腾 1989，Commun. Math. Phys. 121 (1989) 351–399"
def src(book, section, pages, pdf, anchor):
    return {"book": book, "section": section, "pages": pages, "pdf_pages": pdf, "anchor": anchor}

DATA = [
{
  "id": "csw/concept/surgery-formula", "type": "concept", "track": "G",
  "title": "手术公式：沿环面切开-粘合",
  "aliases": ["surgery formula", "surgery on links", "Dehn surgery"],
  "summary": "沿环面上的 $K$ 个 Wilson 线做手术，配分函数由 $S$ 矩阵与链环不变量给出：$Z_k(M)=S_{00}C^{\\sigma(L)}\\sum_\\lambda S_{0\\lambda}J$。",
  "question": "为什么任意三维流形都能用手术从 $S^3$ 得到？手术公式为什么只依赖 $S$ 矩阵与链环？",
  "definition": {
    "text": "任一定向闭三维流形可由 $S^3$ 沿链环 $L$ 做 Dehn 手术得到（Lickorish–Wallace）。CS 的手术公式给出 $Z_k(M)$ 用 $S^3$ 上链环 $L$ 的 Wilson 线期望值表示：$Z_k(M)=\\sum_\\lambda S_{0\\lambda}^{(1)}\\cdots S_{0\\lambda}^{(K)}\\langle\\prod_iW_{R_i}(K_i)\\rangle_{S^3}$（带标架修正相位）。",
    "notation": "$K$ 是手术链环的分量数；$S_{0\\lambda}$ 是真空到 $\\lambda$ 的 S 矩阵元；$\\sigma(L)$ 是标架修正相位。"
  },
  "key_points": [
    "手术把“任意流形”化为“$S^3$ + 链环”，所以 CS 的计算归结为链环不变量。",
    "公式的两种算法：先在 $S^3$ 算链环，再乘以 $S_{0\\lambda}$ 求和；或先在挖空的流形上算，再粘合。",
    "两种算法相等就是手术一致性；它给出 $S$ 矩阵的幺正性与 Verlinde 公式。",
    "标架修正（扭转相位）来自 Wilson 线的标架与流形的标架。",
    "Verlinde 公式正是“$S^2\\times S^1$ 手术到 $S^3$”的两算法对比。"
  ],
  "formulas": ["$Z_k(M)=\\sum_\\lambda S_{0\\lambda}\\langle\\prod W_{R_i}(K_i)\\rangle_{S^3}$", "$Z_k(M)=\\sum_\\lambda S_{0\\lambda}^{(1)}\\cdots S_{0\\lambda}^{(K)}\\langle\\cdots\\rangle$"],
  "theorems": [T("手术公式",
    "沿链环 $L$ 做 Dehn 手术得到的流形 $M$ 的 CS 配分函数，等于 $S^3$ 上该链环的 Wilson 线期望值按 $S_{0\\lambda}$ 加权求和（带标架相位），这与在挖空流形上量子化再粘合的结果一致。",
    "sketch",
    [S("在挖空的 $S^3$ 上，边界环面 $T^2$ 的态空间由 $S$ 矩阵基给出。", "$\\cH(T^2)$ 的基是 $|\\lambda\\rangle$，内积由 $S$ 给出。"),
     S("粘合映射 $\\phi\\in SL(2,\\mathbb{Z})$ 作用在态空间上，给出 $\\phi$ 的矩阵元。", "$\\operatorname{MCG}(T^2)=SL(2,\\mathbb{Z})$。"),
     S("把链环的 Wilson 线插入并收缩，得 $\\sum S_{0\\lambda}\\langle W\\rangle$ 的形式。", "收缩用了 $S$ 的幺正性。")],
    "witten1989/sections/s07-calculability-b.tex 与 s08-calculability-c.tex（§4.2–4.3，p.383–388）",
    "本文对一般手术的标架修正只给规则，未处理所有边界情形（p.391 留白）。")
  ],
  "pitfalls": [
    "不要漏掉标架相位：不同标架的链环期望值差一个 $e^{2\\pi i\\cdot(\\text{标架})\\cdot h_R}$ 因子。",
    "手术链环的分量数与 $S$ 的指标要对齐，否则求和错位。",
    "Kirby 移动不改变流形，但改变链环表示；公式必须在 Kirby 移动下不变（这是 $S^2=(ST)^3$ 的来源）。"
  ],
  "related": ["csw/concept/s-matrix", "csw/concept/verlinde-formula", "csw/concept/jones-from-cs", "csw/concept/mapping-class-group"],
  "sources": [src(W, "§4.2–4.3（手术，原文 p.383–388）", [383, 388], [33, 38], "witten1989/sections/s07-calculability-b.tex（§4.2）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/s-matrix", "type": "concept", "track": "G",
  "title": "模 S 矩阵与 T 矩阵",
  "aliases": ["modular S-matrix", "S matrix", "T matrix"],
  "summary": "$S$ 与 $T$ 是 $SL(2,\\mathbb{Z})$ 在共形块空间上的表示；$T$ 对角，$S$ 由正弦公式给出（$SU(2)$）。",
  "question": "$S$ 矩阵为什么是模变换？它的矩阵元为什么正好是正弦函数？",
  "definition": {
    "text": "环面 $T^2$ 的模群 $SL(2,\\mathbb{Z})$ 由 $S:\\tau\\mapsto-1/\\tau$ 与 $T:\\tau\\mapsto\\tau+1$ 生成，作用在环面共形块空间 $\\cH(T^2)$ 上。$T$ 对角（相位 $e^{2\\pi i(h_j-c/24)}$），$S$ 是“傅里叶变换”。对 $SU(2)_k$，$S_{jl}=\\sqrt{\\frac{2}{k+2}}\\sin\\frac{\\pi(2j+1)(2l+1)}{k+2}$，$j,l=0,\\frac12,\\dots,\\frac k2$。",
    "notation": "$j,l$ 标可积表示；$c=k\\dim G/(k+h^\\vee)$；$S^2=(ST)^3=C$。"
  },
  "key_points": [
    "$S$ 是模变换 $\\tau\\to-1/\\tau$ 的表示矩阵；它是幺正且对称的。",
    "模关系 $S^2=(ST)^3=C$（$C$ 是电荷共轭）是 $SL(2,\\mathbb{Z})$ 的呈现。",
    "$T$ 的相位含 $-c/24$：这是标架反常的模块化形式。",
    "$S$ 的矩阵元给出融合系数（Verlinde）与 $S^3$ 配分函数（$Z(S^3)=S_{00}$）。",
    "正弦形式来自 $SU(2)$ 的特征标（Weyl 特征标公式在 $A_1$ 的情形）。"
  ],
  "formulas": ["$S_{jl}=\\sqrt{\\frac{2}{k+2}}\\sin\\frac{\\pi(2j+1)(2l+1)}{k+2}$", "$T_{jj}=e^{2\\pi i(h_j-c/24)}$", "$S^2=(ST)^3=C$"],
  "theorems": [T("SU(2) 的 S 矩阵",
    "对 $SU(2)_k$，$S_{jl}=\\sqrt{\\frac{2}{k+2}}\\sin\\frac{\\pi(2j+1)(2l+1)}{k+2}$ 满足 $S^2=(ST)^3=C$，其中 $T=\\mathrm{diag}(e^{2\\pi i(h_j-c/24)})$。",
    "complete",
    [S("$SU(2)_k$ 的特征标在 $S$ 变换下由 Weyl 特征标公式给出。", "$\\chi_j(-1/\\tau)=\\sum_lS_{jl}\\chi_l(\\tau)$。"),
     S("$A_1$ 的 Weyl 特征标是正弦之比，化简得正弦公式。", "$\\chi_j(\\tau)=\\frac{\\sin(\\pi(2j+1)z/\\ldots)}{\\sin(\\pi z/\\ldots)}$，在 $z$ 的特殊值取极限。"),
     S("直接验证 $S^2=(ST)^3=C$ 与 $C_{jl}=\\delta_{j,\\bar l}$。", "有限矩阵，可逐项验算。")],
    "witten1989/sections/s04-canonical.tex（§3.4 与 (4.21)）；河野 §2.2；Moore TASI §3.3",
    "一般群的 $S$ 用 Weyl 特征标公式；本文只写 $SU(N)$ 的框架。")
  ],
  "pitfalls": [
    "归一化：$\\sqrt{2/(k+2)}$ 与 $\\sqrt{2/(k+h^\\vee)}$ 在 $SU(2)$ 是同一个，但一般群要换成 $k+h^\\vee$。",
    "$T$ 的相位约定（是否含 $-c/24$）影响 $S^2=(ST)^3$ 的验证：取拓扑自旋 $T=\\mathrm{diag}(e^{2\\pi ih_j})$ 时 $(ST)^3=e^{2\\pi ic/8}$。",
    "$S$ 的指标是可积表示（$j\\le k/2$），不是所有 $j$。"
  ],
  "related": ["csw/concept/verlinde-formula", "csw/concept/surgery-formula", "csw/concept/mapping-class-group", "csw/example/su2-k2-s-matrix"],
  "sources": [src(W, "§3.4（(3.6)）与 §4（(4.21)）", [374, 382], [24, 32], "witten1989/sections/s04-canonical.tex（§3.4）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/verlinde-formula", "type": "concept", "track": "G",
  "title": "Verlinde 公式",
  "aliases": ["Verlinde formula", "Verlinde 猜想"],
  "summary": "$N_{ijk}=\\sum_l\\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$：融合系数 = 三点共形块维数 = $S$ 矩阵的组合。",
  "question": "为什么三点函数的维数能用 $S$ 矩阵算出来？这个公式在 CS 里怎么“物理推导”？",
  "definition": {
    "text": "对可积表示 $i,j,k$，融合系数 $N_{ijk}$（三点共形块维数）由 Verlinde 公式给出：$N_{ijk}=\\sum_l\\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$。等价地，Verlinde 代数 $v_iv_j=\\sum_kN_{ij}^kv_k$ 在基 $w_i=S_{0i}\\sum_mS_i^mv_m$ 下变成 $w_iw_j=\\delta_{ij}w_j$（幂等元）。",
    "notation": "$S$ 是模 S 矩阵；$N_{ijk}=\\dim\\cH(S^2;R_i,R_j,R_k)$。"
  },
  "key_points": [
    "这是“融合 = 模变换”的定量形式：$S$ 的行是融合矩阵的共同特征向量。",
    "在 CS 里它由手术一致性推出（$S^2\\times S^1$ 的两种算法）。",
    "在 WZW 里它是定理（TUY 1989、Faltings 1994）；在 CS 里 Witten 给物理推导。",
    "$N_{ijk}$ 是非负整数，公式给的是整数（非平凡事实）。",
    "它是“可计算性”的核心：$S^3$ 配分函数、手术不变量都归结为 $S$。"
  ],
  "formulas": ["$N_{ijk}=\\sum_l\\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$", "$v_iv_j=\\sum_kN_{ij}^kv_k$", "$w_i=S_{0i}\\sum_mS_i^mv_m,\\ w_iw_j=\\delta_{ij}w_j$"],
  "theorems": [T("Verlinde 公式（CS 版本）",
    "在 CS 中，$S^2$ 上三点函数的维数 $N_{ijk}$ 由 $S$ 矩阵给出：$N_{ijk}=\\sum_lS_{il}S_{jl}S_{kl}/S_{0l}$；等价地，融合代数被 $S$ 对角化。",
    "sketch",
    [S("在 $S^2\\times S^1$ 上沿一个 $S^1$ 做手术，得到 $S^3$ 上的链环。", "$S^2\\times S^1$ 的边界环面被手术。"),
     S("两种算法（先手术 vs 先在 $S^2\\times S^1$ 上算）给出等式 $\\sum_kS_i{}^kN_{kl}{}^m=S_{il}S_i{}^m/S_{0i}$。", "这是 Witten (4.51) 的推导。"),
     S("该等式即 $S$ 对角化融合矩阵，写成特征值形式即 Verlinde 公式。", "线性代数改写。")],
    "witten1989/sections/s08-calculability-c.tex（§4.5，p.388–393）",
    "Witten 的推导依赖手术与量子化的自洽性；严格证明见 TUY 1989 与 Faltings 1994。")
  ],
  "pitfalls": [
    "求和只对可积表示；否则发散。",
    "$N_{ijk}$ 对称但公式里的 $S$ 不是对称指标：$S$ 对称矩阵，但 $N$ 是三重对称张量。",
    "归一化：$S_{0l}$ 与 $S$ 的整体归一化绑定，换书要重算。"
  ],
  "related": ["csw/concept/fusion-rules", "csw/concept/s-matrix", "csw/concept/surgery-formula", "csw/concept/conformal-blocks"],
  "sources": [src(W, "§3.4（(3.6)）与 §4.5（(4.51)）", [374, 393], [24, 43], "witten1989/sections/s08-calculability-c.tex（§4.5）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/jones-from-cs", "type": "concept", "track": "G",
  "title": "Jones 多项式从 CS 来",
  "aliases": ["Jones polynomial from Chern-Simons", "两变量 Jones", "HOMFLY"],
  "summary": "$S^3$ 上沿链环 $L$ 的 Wilson 线期望值 $\\langle\\prod W_{R_i}(K_i)\\rangle$ 在 $G=SU(N)$ 定义表示时给出两变量 Jones 多项式（变量 $N$ 与 $k$）。",
  "question": "为什么 CS 的 Wilson 线期望值等于 Jones 多项式？$q$ 是怎么从 $k$ 来的？",
  "definition": {
    "text": "取 $M=S^3$，链环 $L$ 的各分量取 $SU(N)$ 的定义表示，Wilson 线期望值 $Z(S^3;L)=\\langle\\prod_iW_{R_i}(K_i)\\rangle$ 等于 Jones 多项式的两变量推广（变量为 $N$ 与 $q$，$q=e^{2\\pi i/(N+k)}$）。取 $N=2$ 得经典 Jones 多项式。",
    "notation": "$q=e^{2\\pi i/(N+k)}$（有效 level）；$R$ 为定义表示；$K_i$ 为链环分量。"
  },
  "key_points": [
    "纽结不变量 = 拓扑量子场论的 Wilson 线期望值：这是本文的中心论断。",
    "$q$ 来自 $k$ 与 $N$：$q=e^{2\\pi i/(N+k)}$；$q\\to1$ 对应 $k\\to\\infty$（半经典）。",
    "拆接关系与 Kauffman bracket 是同一结构的组合影子；CS 给了它三维解释。",
    "推广到任意三维流形需要手术公式（不是每个流形都嵌入 $S^3$）。",
    "Kauffman 多项式对应 $SO(N)$ 与 $N$ 维表示。"
  ],
  "formulas": ["$Z(S^3;L)=\\langle\\prod_iW_{R_i}(K_i)\\rangle$", "$q=e^{2\\pi i/(N+k)}$", "$V_L(t)=Z(S^3;L)|_{N=2,\\ t=q}$"],
  "theorems": [T("CS 与 Jones",
    "对 $SU(N)$ 与定义表示，CS 在 $S^3$ 上的 Wilson 线期望值是 Jones 多项式的两变量推广；$N=2$ 给出经典 Jones 多项式。",
    "sketch",
    [S("用正则量子化把 $S^3$ 上的链环期望值化为手术/共形块计算。", "把 $S^3$ 看成 $S^2\\times S^1$ 的手术或辫闭合。"),
     S("共形块的三点函数由 $S$ 矩阵给出（Verlinde）。", "链环的每个交叉对应融合系数。"),
     S("整理得 $q=e^{2\\pi i/(N+k)}$ 的 Jones 多项式。", "$q$ 由有效 level 给出。")],
    "witten1989/sections/s01-cs-action.tex（(1.6)）与 s06–s08（§4）",
    "本文给出的是物理推导与若干例子，未给完整的组合证明；严格化见 RT 与后续文献。")
  ],
  "pitfalls": [
    "不要把 $q$ 写成 $e^{2\\pi i/k}$：$SU(N)$ 的分母是 $N+k$，$SU(2)$ 是 $k+2$。",
    "不同文献的 Jones 变量 $t$ 与 $q$ 差符号/幂次，比较前对齐。",
    "Wilson 线要有标架（ribbon），否则链环不变量不完整。"
  ],
  "related": ["csw/concept/wilson-line", "csw/concept/s-matrix", "csw/concept/surgery-formula", "csw/example/trefoil-jones"],
  "sources": [src(W, "§1（(1.6)）与 §4.6（p.394）", [356, 394], [6, 44], "witten1989/sections/s01-cs-action.tex（(1.6)）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/cs-vs-ads3-cft2", "type": "concept", "track": "H",
  "title": "CS/WZW 与 AdS₃/CFT₂：两码事",
  "aliases": ["holography comparison", "AdS3/CFT2", "全息对偶对比"],
  "summary": "CS/WZW 是“态空间等同”（拓扑理论，无引力子）；AdS₃/CFT₂ 是“动力学等价”（体引力 + 边界 CFT + 全息字典）。两者不是同一种对偶。",
  "question": "为什么不能说“CS/WZW 就是全息”？它们的接触点在哪里、边界在哪里？",
  "definition": {
    "text": "CS/WZW：三维 CS 在 $\\Sigma\\times\\mathbb{R}$ 上的态空间 = 二维 WZW 的共形块空间；三维理论无度规、无局域自由度，配分函数是拓扑不变量。AdS₃/CFT₂：三维量子引力（含度规，渐近 AdS₃）与边界二维 CFT 的动力学等价，有引力子、BTZ 黑洞、全息字典（体场↔边界算子）。",
    "notation": "$c_{CS}=k\\dim G/(k+h^\\vee)$ 由 $k$ 离散决定；$c_{AdS}=3l/2G$ 连续。"
  },
  "key_points": [
    "维度相同（3d/2d），结构完全不同：一个是拓扑态空间，一个是动力学对偶。",
    "CS 无引力子（无度规自由度）；AdS₃ 有引力子与 BTZ 黑洞。",
    "中心荷来源不同：CS 的 $c$ 由 level $k$（整数）给出；AdS₃ 的 $c$ 由 $l/G$（连续）给出。",
    "唯一接触点：三维引力可写成 CS（非紧群 $ISO(2,1)$ 或 $SL(2,\\mathbb{R})\\times SL(2,\\mathbb{R})$），但这是经典相空间层面的改写，不是本文的结论。",
    "原文没有 AdS、没有“全息”字样；AdS/CFT 是 1997 年后的事。"
  ],
  "formulas": ["$c_{CS}=\\frac{k\\dim G}{k+h^\\vee}$", "$c_{AdS}=\\frac{3l}{2G}$", "$Z_{CS}(X\\times S^1)=\\dim\\cH_X$"],
  "theorems": [T("两者的区别（判据）",
    "CS/WZW 的等同是态空间层面的对象等同，不涉及体引力；AdS₃/CFT₂ 是含引力的动力学对偶。二者不能互相推出。",
    "sketch",
    [S("CS 作用量不含度规，理论无引力子；AdS₃ 的体理论含度规与引力子。", "这是定义层面的差别。"),
     S("CS 的中心荷由离散 level 给出；AdS₃ 的中心荷连续。", "$c_{CS}=k\\dim G/(k+h^\\vee)$ vs $c=3l/2G$。"),
     S("CS 的“边界”只是态空间的载体，没有边界动力学；AdS 的边界有完整的 CFT 动力学。", "全息字典要求体场与边界算子对应。")],
    "本文 §5（p.396–397）；对照 AdS₃/CFT₂ 文献（Brown–Henneaux 1986、Maldacena 1997）",
    "“3d 引力=CS”的精确层级（经典/量子、渐进边界条件）需要额外讨论，超出本文。")
  ],
  "pitfalls": [
    "不要写“Witten 1989 预言了全息”：原文无此内容，1988 年也没有 AdS/CFT。",
    "不要把 $c_{CS}$ 与 $c_{AdS}$ 的数值相等当成对偶证据：它们来源不同。",
    "“3d 引力 = CS”只在特定群与边界条件下成立，不是普遍等同。"
  ],
  "related": ["csw/concept/cs-wzw-duality", "csw/concept/conformal-blocks", "csw/concept/mapping-class-group"],
  "sources": [src(W, "§5 Applications to Physics（p.396–397）", [396, 397], [46, 47], "witten1989/sections/s09-applications.tex（§5）")],
  "rights": "rewritten", "status": "draft"
}
]
