# -*- coding: utf-8 -*-
"""概念卡数据（一）：总览、三维理论、相空间。"""
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
  "id": "csw/concept/overview-cs-wzw", "type": "concept", "track": "O",
  "title": "总览：从 Chern–Simons 作用量到共形块",
  "aliases": ["Chern–Simons / WZW 路线图", "overview"],
  "summary": "三维 CS 理论只有作用量、没有度规；把它沿曲面切开正则量子化，相空间是平坦联络模空间，几何量子化后得到共形块的有限维空间，Jones 多项式是其可计算推论。",
  "question": "为什么一个不含度规的三维作用量，能给出二维共形场论的整个态空间？这条链上每一步的条件是什么？",
  "definition": {
    "text": "本库把 Witten 1989 的主线拆成五步：①写作用量 $L=\\frac{k}{4\\pi}\\int_M\\operatorname{Tr}(A\\wedge dA+\\frac{2}{3}A^3)$ 并证明 $k\\in\\mathbb{Z}$；②沿 $\Sigma$ 切开，读出辛形式与高斯约束，相空间是 $M=\\operatorname{Hom}(\\pi_1\\Sigma,G)/G$；③预量子化（行列式线丛）、极化（Kähler），得 $\cH_\\Sigma=H^0(M_J,\\cL^{\\otimes k})$；④穿刺点上的 Wilson 线由 Borel–Weil–Bott 实现为旗流形的几何量子化；⑤证明 $\cH_\\Sigma$ 与 WZW 共形块空间等同，由此算手术公式与 Verlinde 公式。",
    "notation": "$M$ 三维流形，$\\Sigma$ 二维曲面，$G$ 紧单 Lie 群，$d=\\dim G$，$h^\\vee$ 对偶 Coxeter 数；$\\cM$ 与 $\\cM_J$ 分别指平坦联络模空间与选复结构 $J$ 后的 Kähler 模空间；$\\cL$ 行列式线丛。"
  },
  "key_points": [
    "链条的入口是“作用量不含量规”：$g$ 只出现在 Yang–Mills 项里，而 CS 项是 3-形式积分，只需要定向。",
    "链条的中段是“约束 + 辛商”：$A_0$ 是拉格朗日乘子，高斯约束 $F=0$ 是第一类约束，辛商给出平坦联络模空间。",
    "链条的出口是“几何量子化”：预量子化给线丛，极化砍掉一半变量，半形式修正把 $k$ 平移为 $k+h^\\vee$。",
    "每个出口的严格程度不同：$k\\in\\mathbb{Z}$ 是作者证明；$\\cH_\\Sigma$ 与共形块的等同是对象级论证（原文用 are）；函子性只到“可以想见”的纲领。",
    "算出来的数可以独立核对：$Z(S^3)=S_{00}=\\sqrt{2/(k+2)}\\sin\\frac{\\pi}{k+2}$，$k=1$ 给 $1/\\sqrt2$。"
  ],
  "formulas": [
    "$L=\\frac{k}{4\\pi}\\int_M\\operatorname{Tr}(A\\wedge dA+\\tfrac23A\\wedge A\\wedge A)$",
    "$\\cH_\\Sigma=H^0(\\cM_J,\\cL^{\\otimes k})$",
    "$N_{ijk}=\\sum_l\\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$"
  ],
  "theorems": [T("主线（形式陈述）",
    "设 $M=\\Sigma\\times\\mathbb{R}$。CS 理论的正则量子化给出有限维 Hilbert 空间 $\\cH_\\Sigma$，它与 $\\Sigma$ 上 WZW 模型的共形块空间在对象层面等同；带穿刺点的版本由 BWB 实现，整条链给出 $S^3$ 上的 Jones 多项式与三维流形的手术不变量。",
    "sketch",
    [S("作用量层面：写出 $L$，用大规范变换单值性得 $k\\in\\mathbb{Z}$。", "这一步是严格计算，见 level-quantization 卡。"),
     S("相空间层面：切 $M=\\Sigma\\times\\mathbb{R}$，$A_0=0$ 后作用量对时间一阶，读出辛形式；高斯定律作辛商。", "只有第一类约束才能做辛商，见 gauss-law-constraint 与 symplectic-quotient。"),
     S("量子化层面：预量子化 + Kähler 极化 + 半形式，得到 $H^0(\\cM_J,\\cL^{\\otimes k})$。", "这里用到 Narasimhan–Seshadri 把平坦联络换成稳定全纯丛。"),
     S("等同层面：把 $\\cH_\\Sigma$ 与共形块空间都实现为同一组全纯截面，比较 Ward 恒等式。", "原文只到对象级，函子性未证。")],
    "witten1989/sections/s03..s05（原文 p.366–397）",
    "函子性与缝合只在原文 §5 用 “It is obvious at this point” 带过；本卡不把它升级为定理。")
  ],
  "pitfalls": [
    "不要把“等同”读成“范畴等价”：原文只证明向量空间同构，且带射影平坦丛；函子性未证。",
    "$k$ 在作用量、Wilson 线、Verlinde 公式里是同一个整数，但共形场的“有效 level”是 $k+h^\\vee$；两套记号混用会差 $h^\\vee$。",
    "弱耦合极限是大 $k$（作用量振荡），不是小耦合；不要照搬 Yang–Mills 的 $1/g^2$ 展开。"
  ],
  "related": ["csw/concept/cs-action", "csw/concept/flat-connection-moduli", "csw/concept/cs-wzw-duality", "csw/concept/verlinde-formula"],
  "sources": [src(W, "引言与 §1–§5（主线）", [351, 397], [1, 47], "witten1989/sections/s00-front..s09-applications")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/cs-action", "type": "concept", "track": "A",
  "title": "Chern–Simons 作用量",
  "aliases": ["CS action", "陈–西蒙斯作用量"],
  "summary": "在三维流形上积一个 3-形式 $\\operatorname{Tr}(A\\wedge dA+\\frac23A^3)$：只依赖定向、不依赖度规，变分给出 $F=0$。",
  "question": "为什么不能直接用 Yang–Mills 作用量？CS 作用量对联络的变分为什么是 $\\int\\operatorname{Tr}(\\delta A\\wedge F)$？",
  "definition": {
    "text": "设 $M$ 是紧致定向三维流形，$A$ 是 $G$-联络（Lie 代数值 1-形式），$F=dA+A\\wedge A$。Chern–Simons 作用量定义为 $L=\\frac{k}{4\\pi}\\int_M\\operatorname{Tr}\\left(A\\wedge dA+\\frac{2}{3}A\\wedge A\\wedge A\\right)$，其中 $\\operatorname{Tr}$ 取 $G$ 的某个表示上的迹，$k$ 是耦合常数。",
    "notation": "$\\operatorname{Tr}$ 的归一化必须固定：本文取基本表示、长根平方 $=2$，此时 $k\\in\\mathbb{Z}$；换表示或换 Killing 型，$k$ 要跟着换算。"
  },
  "key_points": [
    "Yang–Mills 作用量 $\\int\\sqrt g\\,g^{ik}g^{jl}\\operatorname{Tr}(F_{ij}F_{kl})$ 有两处度规依赖：体积元 $\\sqrt g\\,d^3x$ 与指标缩并 $g^{ik}g^{jl}$；前者可以靠“不积分体积”绕过，后者绕不过。",
    "CS 项是 3-形式在 3-流形上的积分，只需要定向，因此天然是“拓扑场论”的作用量。",
    "变分时 $\\delta(A\\wedge dA)=\\delta A\\wedge dA+A\\wedge d\\delta A$，第二项分部积分并用 $dA=-\\frac12[A,A]$ 变成 $A\\wedge[\\delta A,A]$，三段合并为 $2\\operatorname{Tr}(\\delta A\\wedge F)$。",
    "驻点条件 $F=0$：三维 CS 理论的经典解是平坦联络，这正是相空间是平坦联络模空间的来源。",
    "三维 CS 不是“有质量矢量”的理论：它没有局域自由度，只有拓扑自由度；这才使 Hilbert 空间有限维。"
  ],
  "formulas": [
    "$L=\\frac{k}{4\\pi}\\int_M\\operatorname{Tr}(A\\wedge dA+\\tfrac23A\\wedge A\\wedge A)$",
    "$F=dA+A\\wedge A$",
    "$\\delta L=\\frac{k}{2\\pi}\\int_M\\operatorname{Tr}(\\delta A\\wedge F)$",
    "$F=0\\iff A$ 平坦"
  ],
  "theorems": [T("变分公式",
    "对任意变分 $\\delta A$（在边界上为零），$\\delta L=\\frac{k}{2\\pi}\\int_M\\operatorname{Tr}(\\delta A\\wedge F)$。",
    "complete",
    [S("展开 $\\delta L=\\frac{k}{4\\pi}\\int\\operatorname{Tr}(\\delta A\\wedge dA+A\\wedge d\\delta A+2\\delta A\\wedge A\\wedge A)$。", "把 $\\delta(A\\wedge A\\wedge A)$ 的三项都写出来，再合并。"),
     S("对第二项分部积分：$\\int\\operatorname{Tr}(A\\wedge d\\delta A)=-\\int\\operatorname{Tr}(dA\\wedge\\delta A)$，边界项因 $\\delta A|_{\\partial M}=0$ 消失。", "分部积分给出的负号被 $\\delta A$ 与 $A$ 的交换子吸收。"),
     S("用 $dA=F-A\\wedge A$，把 $-\\operatorname{Tr}(dA\\wedge\\delta A)+2\\operatorname{Tr}(\\delta A\\wedge A\\wedge A)$ 合并成 $2\\operatorname{Tr}(\\delta A\\wedge F)$，再乘 $\\frac{k}{4\\pi}$ 得 $\\frac{k}{2\\pi}\\int\\operatorname{Tr}(\\delta A\\wedge F)$。", "关键是 $\\operatorname{Tr}(A\\wedge A\\wedge\\delta A)$ 与 $\\operatorname{Tr}(\\delta A\\wedge A\\wedge A)$ 只差循环置换，正好补上 $-\\operatorname{Tr}(A\\wedge A\\wedge\\delta A)$。")],
    "witten1989/sections/s01-cs-action.tex §1（原文 p.353–354）")
  ],
  "pitfalls": [
    "系数 $1/4\\pi$ 与 $\\frac23$ 依赖 $\\operatorname{Tr}$ 的归一化；河野书用 $\\frac{1}{8\\pi^2}\\int\\operatorname{Tr}(A\\wedge dA+\\frac23A^3)$，与本文差一个常数因子 $2\\pi k$。",
    "不要给 CS 作用量补一个 $\\sqrt g$：那会破坏拓扑不变性。",
    "$\\int A\\wedge dA$ 在规范变换下变一个边界项，这是下一张卡（level-quantization）的入口。"
  ],
  "related": ["csw/concept/level-quantization", "csw/concept/gauss-law-constraint", "csw/concept/wilson-line"],
  "sources": [src(W, "§1 The Chern–Simons Action", [353, 354], [3, 4], "witten1989/sections/s01-cs-action.tex §1")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/level-quantization", "type": "concept", "track": "A",
  "title": "$k$ 的整性：大规范变换",
  "aliases": ["level quantization", "大规范变换", "large gauge transformation"],
  "summary": "绕数为 $m$ 的大规范变换把作用量平移 $2\\pi km$；量子理论要求 $e^{iL}$ 单值，于是 $k$ 必须是整数。",
  "question": "为什么 CS 的耦合常数必须量子化？充分性为什么原文只说一句？",
  "definition": {
    "text": "设 $g:M\\to G$ 是规范变换，$A\\mapsto A^g=g^{-1}Ag+g^{-1}dg$。当 $\\pi_3(G)\\cong\\mathbb{Z}$ 时，$g$ 有绕数 $m=\\frac{1}{24\\pi^2}\\int_M\\operatorname{Tr}(g^{-1}dg)^3\\in\\mathbb{Z}$。作用量在 $A^g$ 下的平移为 $L(A^g)=L(A)+2\\pi k\\,m$。",
    "notation": "$m$ 也叫 $g$ 的度数；对 $SU(N)$，$m$ 就是映射 $M\\to SU(N)$ 的拓扑度数。"
  },
  "key_points": [
    "小规范变换（可连续形变到恒等）让作用量不变；大规范变换（不同同伦类）让它平移。",
    "平移量正比于 $k$ 与绕数 $m$，比例系数 $2\\pi$ 来自 Wess–Zumino 项的归一化，不是约定。",
    "量子配分函数是 $\\int\\mathcal{D}A\\,e^{iL}$，被积函数必须规范不变，因此 $e^{2\\pi ikm}=1$ 对一切 $m$ 成立，即 $k\\in\\mathbb{Z}$。",
    "必要性是严格论证；充分性（$k$ 整数就够）原文只用一句带过，严格说还需要测度与相位的整体定义。",
    "同一量子化也出现在仿射 Lie 代数的中心荷上：$k$ 就是 level。"
  ],
  "formulas": ["$L(A^g)=L(A)+2\\pi k\\,m$", "$m=\\frac{1}{24\\pi^2}\\int_M\\operatorname{Tr}(g^{-1}dg)^3\\in\\mathbb{Z}$", "$e^{2\\pi ikm}=1\\ \\forall m\\ \\Longrightarrow\\ k\\in\\mathbb{Z}$"],
  "theorems": [T("必要性：$k\\in\\mathbb{Z}$",
    "若 $\\pi_3(G)\\cong\\mathbb{Z}$ 且 $e^{iL}$ 在规范变换下不变，则 $k$ 为整数。",
    "complete",
    [S("取绕数 $m=1$ 的大规范变换 $g$，作用量平移 $\\Delta L=2\\pi k$。", "绕数 $m$ 的平移由 Wess–Zumino 项的拓扑性质给出。"),
     S("量子理论要求 $e^{iL}$ 规范不变，即 $e^{i\\Delta L}=e^{2\\pi ik}=1$。", "$e^{iL}$ 是路径积分的权重，相位不可是新物理。"),
     S("于是 $k\\in\\mathbb{Z}$；对任意 $m$ 同理。", "取 $m=1$ 已足够，其他绕数给出的是同一个条件。")],
    "witten1989/sections/s01-cs-action.tex（原文 p.354–355，式 (1.4)）")
  ],
  "pitfalls": [
    "$k$ 的整性依赖 $\\operatorname{Tr}$ 的归一化；若把长根平方取为 2 的倍数，整性条件会变成别的格。",
    "在带边流形上，大规范变换还会在边界上产生一个 WZW 项，$k$ 的整性条件与边界 CFT 的 level 是同一件事。",
    "不要把它和“规范群的中心荷”混淆：中心荷是 $c=k\\dim G/(k+h^\\vee)$，与 $k$ 的单位不同。"
  ],
  "related": ["csw/concept/cs-action", "csw/concept/wzw-action", "csw/concept/affine-lie-algebra"],
  "sources": [src(W, "§1 大规范变换与 $k$ 的整性", [354, 355], [4, 5], "witten1989/sections/s01-cs-action.tex（式 1.4）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/wilson-line", "type": "concept", "track": "A",
  "title": "Wilson 线",
  "aliases": ["Wilson loop", "威尔逊线"],
  "summary": "沿闭曲线 $C$ 取联络的路径序指数再取迹：不需要度规，只依赖曲线的同伦类与表示，是三维理论的“可观测量”。",
  "question": "Wilson 线为什么是 CS 理论里最自然的观测量？它的期望值为什么给纽结不变量？",
  "definition": {
    "text": "设 $C\\subset M$ 是闭曲线，$R$ 是 $G$ 的表示。Wilson 线定义为 $W_R(C)=\\operatorname{Tr}_R\\,\\mathrm{P}\\exp\\oint_C A$，其中 $\\mathrm{P}$ 表示沿 $C$ 的路径序。链环配分函数为 $Z(M;C_i,R_i)=\\int\\mathcal{D}A\\,e^{iL}\\prod_iW_{R_i}(C_i)$。",
    "notation": "$\\mathrm{P}\\exp$ 是路径序指数；$\\operatorname{Tr}_R$ 在表示 $R$ 的空间上取迹。"
  },
  "key_points": [
    "路径序指数是沿曲线的平行移动，取迹后与起点无关，因此只依赖同伦类与表示。",
    "它不需要度规：曲线、联络、表示都是拓扑/微分几何数据。",
    "在 CS 理论里，Wilson 线的期望值是三维流形中链环的不变量；$S^3$ 上取 $G=SU(N)$、定义表示，得到 Jones 多项式的两变量推广。",
    "标架进入相位：带扭转的 Wilson 线乘 $e^{2\\pi i t h_R}$，这是标架反常的物理来源。",
    "在正则量子化里，Wilson 线变成穿刺点上的算符，对应表示 $R$ 的插入。"
  ],
  "formulas": ["$W_R(C)=\\operatorname{Tr}_R\\,\\mathrm{P}\\exp\\oint_CA$", "$Z(M;C_i,R_i)=\\int\\mathcal{D}A\\,e^{iL}\\prod_iW_{R_i}(C_i)$", "$W_R(C\\text{ 带扭转 }t)=e^{2\\pi ith_R}W_R(C)$"],
  "theorems": [T("规范不变性",
    "设 $g:M\\to G$ 是规范变换，则 $W_R(C)$ 在 $A\\mapsto A^g$ 下不变（对闭曲线）。",
    "complete",
    [S("沿 $C$ 的平行移动在规范变换下共轭：$U_C(A^g)=g(x_0)^{-1}U_C(A)g(x_0)$，$x_0$ 是起点。", "路径序指数是平行移动的合成，规范变换逐点共轭作用。"),
     S("取迹后共轭消失：$\\operatorname{Tr}_R(g^{-1}Ug)=\\operatorname{Tr}_R(U)$。", "迹对共轭不变。"),
     S("闭曲线起点可以取同一点，因此 $W_R(C)$ 规范不变。", "对开曲线，两端点处的共轭不抵消，Wilson 线变成两端点表示空间的张量。")],
    "witten1989/sections/s01-cs-action.tex（原文 p.355，式 (1.5)）")
  ],
  "pitfalls": [
    "开曲线的 Wilson 线不是规范不变的，它带两个端点的表示指标。",
    "路径序在非阿贝尔情形不可省；把 $\\exp\\oint A$ 当成普通指数会漏掉沿曲线的排序。",
    "$\\operatorname{Tr}$ 取哪个表示（定义表示还是伴随表示）决定它对应哪个不变量：$SU(N)$ 定义表示 ↔ Jones，$SO(N)$ ↔ Kauffman。"
  ],
  "related": ["csw/concept/cs-action", "csw/concept/puncture-gauss-law", "csw/concept/jones-from-cs", "csw/concept/borel-weil-bott"],
  "sources": [src(W, "§1 Wilson 线与配分函数", [355, 355], [5, 5], "witten1989/sections/s01-cs-action.tex（式 1.5–1.6）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/gauss-law-constraint", "type": "concept", "track": "B",
  "title": "高斯定律作为第一类约束",
  "aliases": ["Gauss law constraint", "高斯约束"],
  "summary": "$A_0$ 是拉格朗日乘子，对它的变分给出 $\\varepsilon^{ij}F_{ij}=0$；这条约束是第一类约束，生成规范变换。",
  "question": "为什么 $A_0=0$ 不是规范选择而是约束？约束为什么是第一类？",
  "definition": {
    "text": "在 $M=\\Sigma\\times\\mathbb{R}$ 上取 $A=A_0dt+A_i dx^i$。作用量对 $A_0$ 不含时间导数，$A_0$ 是拉格朗日乘子；对 $A_0$ 变分得约束 $\\varepsilon^{ij}F^a_{ij}=0$，即 $F=0$。约束函数的泊松括号（在约束面上）正比于约束本身，故为第一类。",
    "notation": "$i,j=1,2$ 是 $\\Sigma$ 上的指标；$\\varepsilon^{ij}$ 是 $\\Sigma$ 的面积形式；$a$ 是 Lie 代数指标。"
  },
  "key_points": [
    "作用量对 $A_0$ 线性：$\\int A_0\\,\\varepsilon^{ij}F_{ij}$，所以 $A_0$ 是乘子，不是动力学变量。",
    "约束 $F=0$ 在二维曲面 $\Sigma$ 上只有一个独立分量（$\\varepsilon^{ij}F_{ij}$），不是三个。",
    "约束是第一类：它的泊松括号生成规范变换，因此不能直接当方程解，而要做辛商。",
    "经典处理分两步：先限制到 $F=0$（约束面），再按规范群取商。",
    "量子化时不能先解约束再量子化，也不能先量子化再解约束——两种顺序给出同构的 Hilbert 空间（Dirac 方案与辛商等价），但技术难度不同。"
  ],
  "formulas": ["$S=\\frac{k}{8\\pi}\\int dt\\int_\\Sigma\\varepsilon^{ij}\\operatorname{Tr}A_i\\partial_tA_j+\\int A_0\\,\\varepsilon^{ij}F_{ij}$", "$\\varepsilon^{ij}F^a_{ij}=0$", "$\\{G(\\epsilon),G(\\epsilon')\\}=G([\\epsilon,\\epsilon'])$"],
  "theorems": [T("约束生成规范变换",
    "令 $G(\\epsilon)=\\int_\\Sigma\\varepsilon^{ij}\\operatorname{Tr}(\\epsilon F_{ij})$。在泊松括号下，$\\{G(\\epsilon),A_i\\}=D_i\\epsilon$，即约束生成无穷小规范变换；约束之间闭合，故为第一类。",
    "complete",
    [S("由泊松括号 $\\{A_i^a(x),A_j^b(y)\\}=\\frac{4\\pi}{k}\\varepsilon_{ij}\\delta^{ab}\\delta^2(x-y)$ 计算 $\\{G(\\epsilon),A_k\\}$。", "辛形式给出基本括号，见 symplectic-quotient 卡。"),
     S("用 $\\delta F_{ij}=D_i\\delta A_j-D_j\\delta A_i$ 与反对称性 $\\varepsilon^{ij}$，只剩一项 $\\varepsilon^{ij}D_i\\epsilon$，即 $D_i\\epsilon$（二维）。", "$\\varepsilon^{ij}$ 把 $D_i\\delta A_j$ 的对称部分杀掉。"),
     S("两个约束的括号给出 $\\{G(\\epsilon),G(\\eta)\\}=G([\\epsilon,\\eta])$，仍是约束，故第一类。", "结构常数反对称，闭合在约束理想内。")],
    "witten1989/sections/s04-canonical.tex §3.1（原文 p.366–367，式 3.3）")
  ],
  "pitfalls": [
    "不要写 $F_{ij}=0$ 三个分量：二维只有一个独立分量；写成三维会多出两个虚假约束。",
    "约束是第一类意味着规范不是物理自由度，必须商掉；第二类约束才用 Dirac 括号。",
    "$A_0=0$ 只是把乘子固定，不是解掉约束；固定 $A_0$ 后约束仍在。"
  ],
  "related": ["csw/concept/symplectic-quotient", "csw/concept/flat-connection-moduli", "csw/concept/cs-action"],
  "sources": [src(W, "§3.1 The Holomorphic Viewpoint（正则形式）", [366, 367], [16, 17], "witten1989/sections/s04-canonical.tex（式 3.1–3.3）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/symplectic-quotient", "type": "concept", "track": "B",
  "title": "辛商（Marsden–Weinstein 约化）",
  "aliases": ["symplectic quotient", "辛约化", "Marsden–Weinstein reduction"],
  "summary": "相空间 $P$ 带第一类约束时，物理相空间是约束面 $\\mu^{-1}(0)$ 模掉约束生成的群作用，辛形式自动下降。",
  "question": "为什么“先限制到约束面再取商”能得到一个辛流形？辛形式为什么能下降？",
  "definition": {
    "text": "设 $(P,\\omega)$ 是辛流形，紧 Lie 群 $K$ 通过辛作用作用于 $P$，矩映射 $\\mu:P\\to\\mathfrak{k}^*$。若 $0$ 是正则值且 $K$ 在 $\\mu^{-1}(0)$ 上自由作用，则辛商 $P/\\!/K:=\\mu^{-1}(0)/K$ 是辛流形，其辛形式 $\\omega_{\\mathrm{red}}$ 由 $\\omega$ 拉回后在商上良定义。",
    "notation": "$\\mu^{-1}(0)$ 是约束面；$K$ 是规范群；$\\mathfrak{k}$ 是它的 Lie 代数。"
  },
  "key_points": [
    "两步：先解约束（限制到 $\\mu^{-1}(0)$），再按规范群取商；顺序不能反。",
    "辛形式能下降，是因为 $\\omega$ 在约束面上拉回后沿群轨道为零（矩映射的性质），而沿轨道方向的内积由 $d\\mu$ 控制。",
    "在 CS 里，$P$ 是 $\\Sigma$ 上所有联络的空间，$K$ 是规范群，$\\mu=0$ 就是 $F=0$ 的弱形式。",
    "商空间可能有奇点：可约联络处稳定化子非平凡，商是轨形而非流形。",
    "辛商与“先固定规范再解约束”给出同一个相空间，但辛商的构造是无歧义的。"
  ],
  "formulas": ["$\\mu:P\\to\\mathfrak{k}^*,\\quad d\\langle\\mu,X\\rangle=\\iota_{X^\\#}\\omega$", "$P/\\!/K=\\mu^{-1}(0)/K$", "$\\omega_{\\mathrm{red}}=\\iota^*\\omega$ 的商下降"],
  "theorems": [T("辛商定理（Marsden–Weinstein）",
    "在 $K$ 自由作用、$0$ 为正则值的假设下，$\\mu^{-1}(0)/K$ 是辛流形，$\\iota^*\\omega$ 下降到其上。",
    "sketch",
    [S("$\\mu^{-1}(0)$ 是余维 $\\dim K$ 的子流形（$0$ 正则值）。", "正则值定理。"),
     S("群轨道切于 $\\mu^{-1}(0)$ 且在 $\\omega$ 下迷向：$\\iota^*\\omega$ 沿轨道为零。", "矩映射方程 $d\\langle\\mu,X\\rangle=\\iota_{X^\\#}\\omega$ 与 $\\mu=0$ 一起给出。"),
     S("迷向且自由⇒轨道是 $\\iota^*\\omega$ 的核，商空间继承非退化 2-形式。", "商流的辛形式良定义，且闭性继承。")],
    "标准辛几何（本文引 Atiyah–Bott [33]）；CS 情形见 witten1989 §3.1 p.367",
    "自由作用只在不可约联络上成立；可约联络的奇点处理（相交上同调/抛物丛）超出本文范围。")
  ],
  "pitfalls": [
    "不要先取商再解约束：商掉规范后 $F=0$ 变成非局部方程，反而更难。",
    "矩映射是 $\\mathfrak{k}^*$ 值；对非阿贝尔群，$\\mu=0$ 是向量方程，分量个数是 $\\dim G$。",
    "商空间在可约联络处是轨形，维数公式 $(2g-2)d$ 在一般位置成立。"
  ],
  "related": ["csw/concept/gauss-law-constraint", "csw/concept/flat-connection-moduli", "csw/concept/holomorphic-sections"],
  "sources": [src(W, "§3.1 辛商与相空间", [367, 367], [17, 17], "witten1989/sections/s04-canonical.tex（式 3.3 后一段）")],
  "rights": "rewritten", "status": "draft"
}
]
