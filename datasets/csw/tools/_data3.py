# -*- coding: utf-8 -*-
"""概念卡数据（三）：Wilson 线、WZW 与对偶。"""
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
  "id": "csw/concept/puncture-gauss-law", "type": "concept", "track": "D",
  "title": "穿刺点上的高斯定律",
  "aliases": ["puncture constraint", "带标记点的高斯约束"],
  "summary": "在标记点 $P_s$ 处，高斯定律的右端多出算符值源 $T^a_{(s)}$：$(k/8\\pi)\\varepsilon^{ij}F^a_{ij}(x)=\\sum_s\\delta^2(x-P_s)T^a_{(s)}$。",
  "question": "为什么这个约束不能像普通高斯定律那样“解出”经典联络？",
  "definition": {
    "text": "把 Wilson 线穿过 $\\Sigma$ 的交点看成标记点 $P_s$。对沿 $\\Sigma$ 的变分，作用量的边界项要求约束为 $(k/8\\pi)\\varepsilon^{ij}F^a_{ij}(x)=\\sum_s\\delta^2(x-P_s)T^a_{(s)}$，其中 $T^a_{(s)}$ 是表示 $R_s$ 的生成元，作用在 $P_s$ 处的态空间上。",
    "notation": "$T^a_{(s)}$ 是第 $s$ 个标记点上表示 $R_s$ 的生成元；$\\varepsilon^{ij}F_{ij}$ 在二维只有一个独立分量。"
  },
  "key_points": [
    "没有标记点时右端为零，约束就是 $F=0$；有标记点时右端是 $\\delta$ 函数源，联络在 $P_s$ 处有奇点。",
    "右端是算符值：$T^a_{(s)}$ 互相不对易，约束是量子约束而不是经典方程。",
    "直接把它当经典方程解，得到的“联络”依赖表示的选取，不是普通联络。",
    "Witten 的替代方案：不“解”约束，而是把表示 $R_s$ 本身量子化（Borel–Weil–Bott），把相空间扩大。",
    "这个约束与共形场论中“插入顶点算子”的 Ward 恒等式是同一件事。"
  ],
  "formulas": ["$(k/8\\pi)\\varepsilon^{ij}F^a_{ij}(x)=\\sum_s\\delta^2(x-P_s)T^a_{(s)}$", "$F=0$（无标记点时）"],
  "theorems": [T("约束的算符性",
    "带标记点时的高斯定律右端是算符值分布，因此不能在经典层面解出联络；把它当作经典方程会得到依赖表示且非单值的“联络”。",
    "sketch",
    [S("对 $\\Sigma$ 上的变分，作用量的边界项给出 $(k/8\\pi)\\varepsilon^{ij}F^a_{ij}=\\sum_s\\delta^2T^a_{(s)}$。", "边界项来自 Wilson 线在交点处的变分。"),
     S("$T^a_{(s)}$ 是表示 $R_s$ 的生成元，彼此不对易（非阿贝尔）。", "右端是算符，不是 $c$-数。"),
     S("故约束是量子约束；经典解的尝试会得到“q-数联络”，即量子群的萌芽。", "Witten 明确说这条路只给出量子群，不作构造。")],
    "witten1989/sections/s05-hilbert.tex（§3.3，原文 p.371–372）",
    "本文没有把“量子群”路线做完；Borel–Weil–Bott 是替代路线。")
  ],
  "pitfalls": [
    "不要把 $\\delta^2$ 源当成普通点电荷：它的“荷”是算符，不是数。",
    "约束的奇点意味着平坦性只在 $\\Sigma\\setminus\\{P_s\\}$ 上成立，模空间是“带奇点的平坦联络模空间”。",
    "标记点位置不能随便移动：移动会改变约束的解空间（除非同时做规范变换）。"
  ],
  "related": ["csw/concept/gauss-law-constraint", "csw/concept/borel-weil-bott", "csw/concept/conformal-blocks"],
  "sources": [src(W, "§3.3 Incorporation of Wilson Lines", [371, 373], [21, 23], "witten1989/sections/s05-hilbert.tex（§3.3）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/borel-weil-bott", "type": "concept", "track": "D",
  "title": "Borel–Weil–Bott 与表示的几何化",
  "aliases": ["Borel–Weil–Bott", "BWB", "Borel–Weil"],
  "summary": "不可约表示 $R_\\lambda$ 就是旗流形 $G/T$ 上全纯线丛 $\\cL_\\lambda$ 的全纯截面空间：$H^0(G/T,\\cL_\\lambda)=R_\\lambda$（$\\lambda$ 支配整）。",
  "question": "$G/T$ 上的全纯截面为什么正好给出表示 $R_\\lambda$？这里为什么 $\\lambda$ 不加 $\\rho$？",
  "definition": {
    "text": "设 $G$ 紧连通单群，$T$ 极大环面，$G/T$ 旗流形（复结构由正根决定）。对支配整权 $\\lambda$，取 $G/T$ 上辛形式 $\\omega_\\lambda$（其 de Rham 类为 $\\lambda$）与预量子化线丛 $\\cL_\\lambda$。Borel–Weil–Bott 定理：$H^0(G/T,\\cL_\\lambda)=R_\\lambda$（最高权 $\\lambda$ 的不可约表示），其它上同调为零。",
    "notation": "$\\lambda$ 是最高权；$\\rho$ 是 Weyl 向量（正根和的一半）；$\\cL_\\lambda=G\\times_T\\mathbb{C}_\\lambda$。"
  },
  "key_points": [
    "表示论被翻译成复几何：$R_\\lambda$ 是某个线丛的全纯截面空间。",
    "指标是 $\\lambda$ 而不是 $\\lambda+\\rho$：$\\cL_\\lambda=G\\times_T\\mathbb{C}_\\lambda$，权重直接是 $\\lambda$。",
    "$\\rho$ 出现在半形式修正里：$K_{G/T}^{1/2}=\\cL_{-\\rho}$，所以“带半形式的量子化”给出 $\\lambda+\\rho$ 的指标。",
    "Witten 用它把 Wilson 线的表示“量子化”：把 $R_s$ 换成 $G/T$ 上一层几何量子化数据，从而把穿刺点约束变成经典可解的约束。",
    "可积性（$2j\\le k$ 等）不是 BWB 的推论，而来自仿射代数（见 integrable-representation 卡）。"
  ],
  "formulas": ["$H^0(G/T,\\cL_\\lambda)=R_\\lambda$", "$K_{G/T}^{1/2}=\\cL_{-\\rho}$", "$\\dim R_\\lambda=\\prod_{\\alpha>0}\\frac{(\\lambda+\\rho,\\alpha)}{(\\rho,\\alpha)}$"],
  "theorems": [T("Borel–Weil–Bott",
    "对支配整权 $\\lambda$，$H^0(G/T,\\cL_\\lambda)\\cong R_\\lambda$，且 $H^q(G/T,\\cL_\\lambda)=0$（$q>0$）；若 $\\lambda+\\rho$ 落在 Weyl 壁另一侧，则上同调只在某个 $q$ 次非零，给出相应的对偶表示。",
    "sketch",
    [S("$G/T$ 上的全纯线丛由 $T$ 的特征 $\\lambda$ 分类。", "线丛的转移函数是 $T$-值上闭链。"),
     S("对支配整 $\\lambda$，$H^0$ 的维数由 Weyl 维数公式给出，且 $G$ 作用不可约。", "这是 BWB 的标准证明（用 Weyl 群与上同调消没）。"),
     S("一般 $\\lambda$ 时，非零上同调出现在 $q=\\ell(w)$（$w$ 使 $w(\\lambda+\\rho)$ 支配整）。", "这就是“Bott”部分：上同调的跳变。")],
    "witten1989/sections/s05-hilbert.tex（§3.3，原文 p.372）",
    "本文只引用 BWB 的结论（$H^0=R_\\lambda$），不证明；一般 $\\lambda$ 的 Bott 部分本文不用。")
  ],
  "pitfalls": [
    "不要写 $\\lambda+\\rho$ 当指标：$\\cL_\\lambda$ 的权重是 $\\lambda$，$\\rho$ 属于 $K^{1/2}$。",
    "BWB 给的是全纯截面，不是“所有截面”；全纯性由复结构决定。",
    "可积性 $2j\\le k$ 不来自 BWB，而来自仿射代数的表示论。"
  ],
  "related": ["csw/concept/puncture-gauss-law", "csw/concept/flag-orbit-symplectic", "csw/concept/integrable-representation"],
  "sources": [src(W, "§3.3（用 BWB 把表示量子化）", [371, 372], [21, 22], "witten1989/sections/s05-hilbert.tex（§3.3）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/flag-orbit-symplectic", "type": "concept", "track": "D",
  "title": "旗流形上的辛形式与轨道方法",
  "aliases": ["flag manifold symplectic form", "coadjoint orbit", "轨道方法"],
  "summary": "$G/T$ 上的辛形式 $\\omega_\\lambda(X,Y)=\\frac12\\langle\\lambda,[X,Y]\\rangle$ 由最高权给出；$G/T$ 就是这个权对应的余伴随轨道。",
  "question": "$G/T$ 上的辛形式为什么由 $\\lambda$ 决定？为什么 $G/T$ 是余伴随轨道？",
  "definition": {
    "text": "把 $G/T$ 等同于余伴随轨道 $\\mathcal{O}_\\lambda=G/T$（$\\lambda$ 支配整）。其 Kirillov–Kostant–Souriau 辛形式在单位元处为 $\\omega_\\lambda(X,Y)=\\frac12\\langle\\lambda,[X,Y]\\rangle$，并 $G$-不变地延拓。积分归一化后 $[\\omega_\\lambda]=\\lambda$。",
    "notation": "$\\mathcal{O}_\\lambda$ 是 $\\lambda$ 的余伴随轨道；$\\langle\\cdot,\\cdot\\rangle$ 是 $\\mathfrak{g}$ 与 $\\mathfrak{g}^*$ 的配对。"
  },
  "key_points": [
    "$G/T$ 是旗流形，也是“最大”的余伴随轨道；$\\lambda$ 决定辛形式。",
    "轨道方法（Kirillov–Kostant–Souriau）说：不可约表示 = 轨道的几何量子化。",
    "这就是 Witten 把“表示 $R$”看作“辛流形 $G/T$ 的量子化”的依据。",
    "整性条件：$\\lambda$ 为整权时 $[\\omega_\\lambda]$ 才整，才有预量子化线丛。",
    "在 CS 里把 $G/T$ 的相空间与 $\\Sigma$ 的相空间做直积（并做辛商），就得到扩大后的模空间 $M_{P_s,R_s}$。"
  ],
  "formulas": ["$\\omega_\\lambda(X,Y)=\\tfrac12\\langle\\lambda,[X,Y]\\rangle$", "$[\\omega_\\lambda]=\\lambda\\in H^2(G/T,\\mathbb{Z})$", "$\\mathcal{O}_\\lambda\\cong G/T$"],
  "theorems": [T("轨道与表示的对应",
    "对支配整权 $\\lambda$，余伴随轨道 $\\mathcal{O}_\\lambda\\cong G/T$ 的几何量子化给出不可约表示 $R_\\lambda$。",
    "sketch",
    [S("$\\mathcal{O}_\\lambda$ 上的辛形式由 $\\lambda$ 给出，且 $[\\omega_\\lambda]$ 整。", "支配整权保证整性。"),
     S("预量子化线丛是 $\\cL_\\lambda$，Kähler 极化取 $G/T$ 的复结构。", "$G/T$ 有自然的 $G$-不变复结构。"),
     S("BWB 给出 $H^0=R_\\lambda$，几何量子化与轨道方法一致。", "这是轨道方法在紧群情形的经典结论。")],
    "witten1989/sections/s05-hilbert.tex（§3.3，p.372）；Moore TASI 附录 B",
    "本文只说“$R$ 可看成某辛流形的量子化”，未逐条验证整性与极化。")
  ],
  "pitfalls": [
    "不要把 $G/T$ 的辛形式与 $\\Sigma$ 的辛形式混淆：前者是表示的“内空间”，后者是规范场的相空间。",
    "$\\lambda$ 必须支配且整，否则既无预量子化也有上同调跳变。",
    "轨道方法的“量子化”在奇轨道上有额外选择（半形式），与 CS 主问题的半形式修正同源。"
  ],
  "related": ["csw/concept/borel-weil-bott", "csw/concept/puncture-gauss-law", "csw/concept/symplectic-quotient"],
  "sources": [src(W, "§3.3 旗流形与辛形式", [371, 372], [21, 22], "witten1989/sections/s05-hilbert.tex（§3.3）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/integrable-representation", "type": "concept", "track": "D",
  "title": "可积表示与 $2j\\le k$ 截断",
  "aliases": ["integrable representation", "可积表示", "level truncation"],
  "summary": "只有“可积”的表示才给出非零共形块：$SU(2)$ 时 $2j\\le k$；一般 $G$ 时 $\\lambda$ 属 level $k$ 的仿射 Weyl 群基本域。",
  "question": "为什么表示要满足 $2j\\le k$？这个截断是 Borel–Weil–Bott 给的，还是别的？",
  "definition": {
    "text": "仿射 Lie 代数 $\\hat{\\mathfrak{g}}_k$ 的最高权表示称为可积的，如果 $\\lambda$ 满足 $(\\lambda,\\theta)\\le k$（$\\theta$ 是最高根）。对 $SU(2)$，$\\lambda=2j$，条件为 $2j\\le k$。只有可积表示对应的共形块才非零；其它表示在 CS 中“退耦”。",
    "notation": "$k$ 是 level；$\\theta$ 是最高根；$j$ 是 $SU(2)$ 自旋。"
  },
  "key_points": [
    "截断来自仿射代数：$\\hat{\\mathfrak{g}}_k$ 的可积最高权表示有限多个。",
    "它等价于“量子群 $U_q(\\mathfrak{g})$ 在 $q$ 为 $k+h^\\vee$ 次单位根时的可积表示”。",
    "在 CS 里表现为：可积表示之外，穿刺点上的共形块维数为零。",
    "这不是 BWB 的推论：BWB 对任意支配整权都成立，截断是额外的仿射结构。",
    "截断使维数有限；否则共形块空间会无限维。"
  ],
  "formulas": ["$(\\lambda,\\theta)\\le k$", "$SU(2):\\ 2j\\le k$", "$\\dim\\cH(S^2;R_1,R_2,R_3)=N_{ijk}$（仅可积 $i,j,k$ 非零）"],
  "theorems": [T("可积性判据",
    "对 $\\hat{\\mathfrak{su}}(2)_k$，自旋 $j$ 的最高权表示可积当且仅当 $2j\\le k$；此时共形块空间维数有限且由 Verlinde 公式给出。",
    "sketch",
    [S("仿射 Weyl 群的基本域由 $(\\lambda,\\theta)\\le k$ 刻画。", "这是 Kac–Weyl 特征标公式的标准结论。"),
     S("可积表示的特征标在模变换下封闭（模不变性）。", "只有可积表示才构成模不变量。"),
     S("非可积表示给出发散或退耦的共形块。", "Witten p.372 说“其它表示退耦”。")],
    "witten1989/sections/s05-hilbert.tex（p.372 括号）；Kac, Infinite Dimensional Lie Algebras",
    "本文只说“只有可积表示有非零截面”，未给证明；河野 §1.2 与上野 §3 有系统处理。")
  ],
  "pitfalls": [
    "不要把它当成“$k$ 截断就是取前 $k$ 个表示”：$SU(2)$ 的可积表示是 $j=0,\\frac12,\\dots,\\frac{k}2$，共 $k+1$ 个。",
    "有效 level 是 $k+h^\\vee$：写 $q=e^{2\\pi i/(k+2)}$ 时截断是 $2j\\le k$，别把两个 $k$ 混了。",
    "一般群的可积条件用最高根，不是用 $\\dim G$。"
  ],
  "related": ["csw/concept/borel-weil-bott", "csw/concept/affine-lie-algebra", "csw/concept/verlinde-formula"],
  "sources": [src(W, "§3.3（可积表示，p.372）", [372, 372], [22, 22], "witten1989/sections/s05-hilbert.tex（§3.3 末）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/wzw-action", "type": "concept", "track": "E",
  "title": "Wess–Zumino–Witten 作用量与 level",
  "aliases": ["WZW action", "Wess–Zumino–Witten", "WZ 项"],
  "summary": "$S_{WZW}=S_\\sigma+k\\Gamma$：动能项 $S_\\sigma$ 与拓扑项 $\\Gamma$（Wess–Zumino 项）；$e^{iS}$ 单值要求 $k\\in\\mathbb{Z}$。",
  "question": "WZ 项为什么只有在 $k$ 整数时才有定义？它为什么是拓扑项？",
  "definition": {
    "text": "设 $g:\\Sigma\\to G$ 是场。$S_{WZW}[g]=S_\\sigma[g]+k\\Gamma[g]$，其中 $S_\\sigma=\\frac1{8\\pi}\\int_\\Sigma\\operatorname{Tr}(g^{-1}\\partial_ig\\,g^{-1}\\partial^ig)$，$\\Gamma=\\frac1{24\\pi^2}\\int_B\\operatorname{Tr}(g^{-1}dg)^3$（$B$ 是 $\\Sigma$ 的三维延拓）。$\\Gamma$ 在 $g$ 的延拓改变时平移 $2\\pi i\\mathbb{Z}$ 的整数倍，故 $e^{iS}$ 单值要求 $k\\in\\mathbb{Z}$。",
    "notation": "$g$ 取值于紧单群 $G$；$\\Gamma$ 是 WZ 项；$k$ 是 level（整数）。"
  },
  "key_points": [
    "$\\Gamma$ 是三维的，虽然理论是二维的：它只依赖 $g$ 在三维延拓上的值（拓扑项）。",
    "延拓不唯一，但改变延拓只改变 $\\Gamma$ 的 $2\\pi i$ 整数倍，因此 $e^{ik\\Gamma}$ 只需 $k\\in\\mathbb{Z}$。",
    "这与 CS 的 $k\\in\\mathbb{Z}$ 是同一件事的两面：三维拓扑项的边界就是二维的 WZ 项。",
    "WZW 是“有质量”的二维理论，但有共形对称性；其中心荷 $c=k\\dim G/(k+h^\\vee)$。",
    "CS 与 WZW 的关系不只是“边界”：CS 在 $\\Sigma\\times\\mathbb{R}$ 上的态空间就是 WZW 的共形块空间。"
  ],
  "formulas": ["$S_{WZW}=S_\\sigma+k\\Gamma$", "$\\Gamma=\\frac1{24\\pi^2}\\int_B\\operatorname{Tr}(g^{-1}dg)^3$", "$c=\\frac{k\\dim G}{k+h^\\vee}$"],
  "theorems": [T("WZ 项的整性",
    "$\\Gamma$ 在两个延拓上的差为 $2\\pi i$ 的整数倍；因此 $e^{ik\\Gamma}$ 逐点定义当且仅当 $k\\in\\mathbb{Z}$。",
    "sketch",
    [S("两个三维延拓 $B_1,B_2$ 拼成闭三维流形，$\\int_{B_1}-\\int_{B_2}$ 是整周期。", "$(g^{-1}dg)^3$ 是闭形式，其周期整。"),
     S("周期为 $2\\pi i\\mathbb{Z}$ 倍（归一化后）。", "这是 Wess–Zumino 项的标准计算。"),
     S("故 $e^{ik\\Gamma}$ 单值 iff $k\\in\\mathbb{Z}$。", "$k$ 整数才能吸收相位。")],
    "witten1989/sections/s01-cs-action.tex（与 (1.4) 同源，p.354）",
    "本文把 WZ 项当作已知背景；推导在 Witten 1984 与河野 §1.3。")
  ],
  "pitfalls": [
    "不要把 $S_\\sigma$ 与 $\\Gamma$ 的归一化混用：不同书的 $k$ 归一化差因子 2，比较前先对齐。",
    "WZW 的 level $k$ 与 CS 的 level $k$ 相等，但 $SU(2)$ 的有效 level 是 $k+2$（半形式修正）。",
    "$\\Gamma$ 不是“边界项”，它是三维延拓上的积分；二维理论里它只是记号。"
  ],
  "related": ["csw/concept/cs-action", "csw/concept/level-quantization", "csw/concept/affine-lie-algebra", "csw/concept/sugawara-construction"],
  "sources": [src(W, "§1（WZ 项与 k 整性）、§3–4", [354, 396], [4, 46], "witten1989/sections/s01-cs-action.tex（(1.4)）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/affine-lie-algebra", "type": "concept", "track": "E",
  "title": "仿射 Lie 代数与 OPE",
  "aliases": ["affine Lie algebra", "Kac–Moody", "current algebra"],
  "summary": "WZW 的对称代数是 $\\hat{\\mathfrak{g}}_k$：$[J^a_n,J^b_m]=if^{abc}J^c_{n+m}+kn\\delta^{ab}\\delta_{n+m,0}$；$k$ 就是 level。",
  "question": "中心扩张的项 $kn\\delta$ 从哪来？它为什么决定了 $c$ 与 $h$？",
  "definition": {
    "text": "由 WZW 的 Noether 流 $J^a(z)$ 的 Laurent 模式 $J^a_n$ 生成仿射代数 $\\hat{\\mathfrak{g}}_k$：$[J^a_n,J^b_m]=if^{abc}J^c_{n+m}+kn\\delta^{ab}\\delta_{n+m,0}$。等价地，OPE $J^a(z)J^b(w)\\sim\\frac{k\\delta^{ab}}{(z-w)^2}+\\frac{if^{abc}J^c(w)}{z-w}$。",
    "notation": "$k$ 是 level（整数）；$f^{abc}$ 是结构常数；$J^a_n$ 是流模式。"
  },
  "key_points": [
    "中心项 $kn\\delta^{ab}$ 是量子修正：经典流代数没有它。",
    "它由 WZW 作用量的 level $k$ 决定，所以“中心扩张的系数 = level”。",
    "对易关系的 $\\delta_{n+m,0}$ 说明模式 $n$ 与 $-n$ 配对；真空模不变要求 $k$ 整。",
    "Virasoro 代数由 $J$ 的双线性（Sugawara）构造，中心荷 $c=k\\dim G/(k+h^\\vee)$。",
    "表示论：可积最高权表示由 $(\\lambda,\\theta)\\le k$ 截断。"
  ],
  "formulas": ["$[J^a_n,J^b_m]=if^{abc}J^c_{n+m}+kn\\delta^{ab}\\delta_{n+m,0}$", "$J^a(z)J^b(w)\\sim\\frac{k\\delta^{ab}}{(z-w)^2}+\\frac{if^{abc}J^c(w)}{z-w}$"],
  "theorems": [T("WZW 的流代数",
    "WZW 理论的 Noether 流满足 level $k$ 的仿射代数；其真空表示是可积最高权表示，$k$ 由作用量的 WZ 项系数给出。",
    "sketch",
    [S("从 $S_{WZW}$ 变分得守恒流 $J^a$。", "WZW 的对称群是 $G_L\\times G_R$。"),
     S("计算 $J^a(z)J^b(w)$ 的 OPE，单极点给结构常数，双极点给 $k\\delta^{ab}$。", "双极点来自作用量的动能项归一化。"),
     S("故流代数是 $\\hat{\\mathfrak{g}}_k$。", "中心项系数就是 $k$。")],
    "河野《场论与拓扑学》§1.1–1.2；Witten 1984",
    "本文不证明流代数，只把它作为 WZW 的已知结构引用（p.360 附近）。")
  ],
  "pitfalls": [
    "不要把 $k$ 与中心荷 $c$ 混淆：$c$ 由 $k$ 与 $\\dim G$、$h^\\vee$ 共同决定。",
    "OPE 的系数约定因书而异（$2\\pi$ 因子）；比较前对齐。",
    "模式指标 $n$ 的符号约定（$J^a_n$ 是 $z^{n+1}$ 还是 $z^{-n-1}$）影响公式外观。"
  ],
  "related": ["csw/concept/wzw-action", "csw/concept/sugawara-construction", "csw/concept/conformal-blocks"],
  "sources": [src(W, "§2–3（WZW 流与仿射代数）", [359, 371], [9, 21], "witten1989/sections/s03-knots.tex（§2.1）与 s05-hilbert.tex")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/sugawara-construction", "type": "concept", "track": "E",
  "title": "Sugawara 构造与中心荷",
  "aliases": ["Sugawara construction", "Virasoro from currents"],
  "summary": "$T(z)=\\frac1{2(k+h^\\vee)}\\sum_a:J^aJ^a:$ 给出 Virasoro 代数，中心荷 $c=k\\dim G/(k+h^\\vee)$。",
  "question": "为什么分母是 $k+h^\\vee$ 而不是 $k$？$h^\\vee$ 从哪里来？",
  "definition": {
    "text": "设 $J^a(z)$ 是 level $k$ 的仿射流。定义 $T(z)=\\frac{1}{2(k+h^\\vee)}\\sum_a{:}J^a(z)J^a(z){:}$（正规序）。则 $T$ 满足 Virasoro 代数，中心荷 $c=k\\dim G/(k+h^\\vee)$，且 $J^a$ 是权 $1$ 的初级场。",
    "notation": "$h^\\vee$ 是对偶 Coxeter 数（$SU(N)$ 为 $N$，$SU(2)$ 为 2）；$k+h^\\vee$ 是有效 level。"
  },
  "key_points": [
    "经典 Sugawara 是 $T\\propto\\sum J^aJ^a$；量子化时双收缩产生额外项，把 $k$ 修正为 $k+h^\\vee$。",
    "$h^\\vee$ 来自双收缩的一次收缩：$\\sum_a f^{abc}f^{abd}=h^\\vee\\delta^{cd}$（适当归一化）。",
    "中心荷 $c=k\\dim G/(k+h^\\vee)$ 在 $k\\to\\infty$ 时趋于 $\\dim G$（半经典极限）。",
    "Virasoro 的中心荷与 CS 的标架反常是同一件事：$c$ 出现在标架相位 $e^{2\\pi i(n-m)c/24}$ 里。",
    "表示的最高权 $h_\\lambda=(\\lambda,\\lambda+2\\rho)/(2(k+h^\\vee))$，$\\lambda$ 是可积最高权。"
  ],
  "formulas": ["$T(z)=\\frac1{2(k+h^\\vee)}\\sum_a{:}J^aJ^a{:}$", "$c=\\frac{k\\dim G}{k+h^\\vee}$", "$h_\\lambda=\\frac{(\\lambda,\\lambda+2\\rho)}{2(k+h^\\vee)}$"],
  "theorems": [T("Sugawara 公式",
    "由 level $k$ 的仿射流按上式构造的 $T(z)$ 满足 Virasoro 代数，中心荷 $c=k\\dim G/(k+h^\\vee)$，且流的共形权为 1。",
    "sketch",
    [S("计算 $T(z)T(w)$ 的 OPE：四流项用 Wick 收缩，双收缩给出 $k$ 与 $h^\\vee$ 的组合。", "双收缩 $\\sum_a:J^aJ^a:$ 的系数来自 $f^{abc}f^{abd}=h^\\vee\\delta^{cd}$。"),
     S("要求 $T$ 的 OPE 形状为标准 Virasoro，解出归一化 $1/(2(k+h^\\vee))$。", "归一化由 $T$ 的 $1/(z-w)^4$ 系数（即 $c/2$）确定。"),
     S("故 $c=k\\dim G/(k+h^\\vee)$。", "把 $k$ 换成 $k+h^\\vee$ 的修正来自双收缩。")],
    "河野 §1.3；上野 §3.4",
    "本文不推导 Sugawara，只在 §2 用 $c$ 的公式（(2.25)）；细节见教材。")
  ],
  "pitfalls": [
    "分母写成 $k$ 是错的：会丢掉 $h^\\vee$，$k=1$ 时甚至给出 $c=\\dim G$ 而不是 $\\dim G/(1+h^\\vee)$。",
    "$h_\\lambda$ 公式里的 $\\lambda+2\\rho$ 常被误写成 $\\lambda+\\rho$；展开 $(\\lambda,\\lambda)+2(\\lambda,\\rho)$。",
    "有效 level $k+h^\\vee$ 与截断用的 $k$ 是两个不同的 $k$，别混。"
  ],
  "related": ["csw/concept/affine-lie-algebra", "csw/concept/conformal-blocks", "csw/concept/half-form-correction"],
  "sources": [src(W, "§2（(2.25) 的 c）与 §4 (4.21)", [361, 382], [11, 32], "witten1989/sections/s02-weak-coupling.tex（(2.25)）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/conformal-blocks", "type": "concept", "track": "E",
  "title": "共形块",
  "aliases": ["conformal blocks", "共形块空间"],
  "summary": "带标记点 $(\\Sigma;P_i,R_i)$ 的共形块空间 $\\cH_\\Sigma$ 是 WZW 的手征态空间；在 CS 里它就是 $H^0(\\cM_J,\\cL^{\\otimes k})$。",
  "question": "共形块与 CS 的量子 Hilbert 空间是什么关系？为什么说它们“是同一个空间”？",
  "definition": {
    "text": "固定复结构 $J$，带标记点 $(P_i,R_i)$ 的 WZW 共形块空间是 $z_i$ 处插入表示 $R_i$ 的手征场的多点函数空间（模去零模态）。Segal 的模函子把“曲面+标记+表示”映到有限维向量空间。CS 在 $\\Sigma\\times\\mathbb{R}$ 上的量子 Hilbert 空间按 $\\cH_\\Sigma=H^0(\\cM_J,\\cL^{\\otimes k})$ 计算，两者作为向量空间典范同构。",
    "notation": "$\\cH_\\Sigma$ 随 $J$ 是射影平坦丛；不带标记点时 $\\cH_\\Sigma$ 是一维（空曲面）。"
  },
  "key_points": [
    "共形块的维数是有限的（可积表示与紧曲面）。",
    "CS 的 $\\cH_\\Sigma$ 与 WZW 的共形块空间是“对象级同构”：都是 $H^0(\\cM_J,\\cL^{\\otimes k})$。",
    "这个同构的证明不是本文给的：Witten 只给物理论证，严格处理由 Segal 与 TUY 给出。",
    "函子性（缝合）只在原文 §5 用一句“It is obvious at this point”带过，没有证明。",
    "共形块随复结构变化构成射影平坦丛；联络即 Hitchin/KZ，单值性给出映射类群表示。"
  ],
  "formulas": ["$\\cH_\\Sigma=H^0(\\cM_J,\\cL^{\\otimes k})$", "$\\dim\\cH_{S^2;R_1,R_2,R_3}=N_{R_1R_2R_3}$"],
  "theorems": [T("CS/WZW 的对象级等同",
    "在固定复结构 $J$ 下，CS 的量子 Hilbert 空间 $\\cH_\\Sigma$ 与 WZW 共形块空间作为向量空间同构；两边都等于 $H^0(\\cM_J,\\cL^{\\otimes k})$。",
    "sketch",
    [S("CS 侧：正则量子化给出 $H^0(\\cM_J,\\cL^{\\otimes k})$（§3.1）。", "全纯截面是量子态。"),
     S("WZW 侧：共形块由 Ward 恒等式与 KZ 方程刻画，其解空间也是 $H^0$。", "共形块是手征场的相关函数，KZ 把它们与全纯截面联系起来。"),
     S("两边维数一致且都由模空间上的同一线丛给出，故同构。", "本文把这一步当作物理论证，未严格证明。")],
    "witten1989/sections/s09-applications.tex（§5，p.396–397）",
    "本文只说“can be interpreted as”与“It is obvious at this point”；严格性由 Segal/TUY 补。")
  ],
  "pitfalls": [
    "不要把“同构”升级成“范畴等价”：函子性与缝合要额外证明。",
    "共形块依赖复结构（$J$），但射影化后不依赖；别把 $J$ 依赖性说成物理依赖性。",
    "标记点表示必须可积，否则维数为零。"
  ],
  "related": ["csw/concept/holomorphic-sections", "csw/concept/cs-wzw-duality", "csw/concept/knizhnik-zamolodchikov", "csw/concept/fusion-rules"],
  "sources": [src(W, "§3.4 与 §5（共形块）", [373, 397], [23, 47], "witten1989/sections/s05-hilbert.tex（§3.4）与 s09-applications.tex（§5）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/knizhnik-zamolodchikov", "type": "concept", "track": "E",
  "title": "Knizhnik–Zamolodchikov 方程",
  "aliases": ["KZ equation", "Knizhnik–Zamolodchikov"],
  "summary": "共形块作为 $z_i$ 的函数满足 $\\kappa\\partial_{z_i}\\Psi=\\sum_{j\\ne i}\\frac{\\Omega_{ij}}{z_i-z_j}\\Psi$，$\\kappa=k+h^\\vee$。",
  "question": "KZ 方程怎么从 WZW 的 Ward 恒等式推出来？为什么分母是 $k+h^\\vee$？",
  "definition": {
    "text": "设 $\\Psi(z_1,\\dots,z_n)$ 是带插入 $(R_i)$ 的共形块。由 $\\bar\\partial$ 的零模条件与 Sugawara 的 $T$ 的 Ward 恒等式，得 KZ 方程 $\\kappa\\partial_{z_i}\\Psi=\\sum_{j\\ne i}\\frac{\\Omega_{ij}}{z_i-z_j}\\Psi$，其中 $\\Omega_{ij}=\\sum_aT^a_{(i)}T^a_{(j)}$，$\\kappa=k+h^\\vee$。",
    "notation": "$\\Omega_{ij}$ 是第 $i,j$ 个标记点表示上的 Casimir 双线性；$\\kappa$ 是有效 level。"
  },
  "key_points": [
    "KZ 是“全纯性 + 共形 Ward 恒等式”的联合结果：手征场只依赖 $z$，$T$ 的极点给出 $\\partial_z$。",
    "$\\kappa=k+h^\\vee$ 来自 Sugawara 的归一化；把 $\\kappa$ 写成 $k$ 是常见错误。",
    "两点函数：$\\Psi=(z_1-z_2)^{-2h_j}$，指数正是共形权（$SU(2)$、$k=1$ 时 $h_{1/2}=1/4$）。",
    "KZ 是平坦联络的方程：$\\nabla\\Psi=0$，其单值性给出共形块的表示（与 Hitchin 联络一致）。",
    "在 $g=0$ 有显式形式；高亏格要加更多项，但仍是射影平坦联络。"
  ],
  "formulas": ["$\\kappa\\partial_{z_i}\\Psi=\\sum_{j\\ne i}\\frac{\\Omega_{ij}}{z_i-z_j}\\Psi$", "$\\kappa=k+h^\\vee$", "$n=2:\\ \\Psi=(z_1-z_2)^{-2h_j}$"],
  "theorems": [T("KZ 方程的来源",
    "WZW 共形块满足 KZ 方程，$\\kappa=k+h^\\vee$；该方程在 $g=0$ 时是共形块空间的射影平坦联络的显式形式。",
    "sketch",
    [S("共形块是全纯的：$\\bar\\partial\\Psi=0$。", "手征场只依赖 $z$。"),
     S("用 Sugawara 的 $T$ 与初级场 OPE，得到 $\\partial_{z_i}\\Psi$ 的表达式。", "Ward 恒等式把 $T$ 的插入写成 $\\partial_z$。"),
     S("整理得 $\\kappa\\partial_{z_i}\\Psi=\\sum\\Omega_{ij}/(z_i-z_j)\\Psi$，$\\kappa=k+h^\\vee$。", "Sugawara 的归一化决定 $\\kappa$。")],
    "河野 §1.5；Knizhnik–Zamolodchikov 1984；本文 §3.2 间接引用（BPZ [32]）",
    "本文正文没有出现 KZ 方程；只说“带标记点时联络显式”，严格形式见河野。")
  ],
  "pitfalls": [
    "分母写 $k$ 会破坏 $SU(2)$、$k=1$ 的 $h_{1/2}=1/4$ 检验。",
    "$\\Omega_{ij}$ 的符号取决于 $T^a$ 的厄米性与 $\\bar\\partial$ 的约定，数值检验前先对齐。",
    "KZ 只给全纯部分的方程；反全纯部分由共轭给出。"
  ],
  "related": ["csw/concept/conformal-blocks", "csw/concept/hitchin-connection", "csw/concept/sugawara-construction"],
  "sources": [src(W, "§3.2（射影平坦联络，BPZ [32]）", [369, 370], [19, 20], "witten1989/sections/s04-canonical.tex（§3.2）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/fusion-rules", "type": "concept", "track": "E",
  "title": "融合规则与 Verlinde 公式",
  "aliases": ["fusion rules", "融合规则", "Verlinde formula"],
  "summary": "融合规则 $R_i\\otimes R_j=\\bigoplus_kN_{ij}^kR_k$ 的系数由 $S$ 矩阵给出：$N_{ij}^k=\\sum_l\\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$。",
  "question": "融合系数为什么可以用 $S$ 矩阵“对角化”？这个公式的物理意义是什么？",
  "definition": {
    "text": "对可积表示 $R_i$，融合规则 $R_i\\otimes R_j=\\bigoplus_kN_{ij}^kR_k$ 定义非负整数 $N_{ij}^k$。Verlinde 公式：$N_{ij}^k=\\sum_l\\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$，其中 $S$ 是模 S 矩阵（$S^2=(ST)^3=C$）。等价地，Verlinde 代数 $v_iv_j=\\sum_kN_{ij}^kv_k$ 在基 $w_i=S_{0i}\\sum_mS_i^mv_m$ 下对角化。",
    "notation": "$S_{ij}$ 是模 S 矩阵；$N_{ij}^k$ 是融合系数；下标 $0$ 是真空。"
  },
  "key_points": [
    "融合系数是 S² 上三点函数的维数：$N_{ij}^k=\\dim\\cH(S^2;R_i,R_j,R_k)$。",
    "Verlinde 公式把“融合”（代数）与“模变换”（几何）联系起来。",
    "它给出 CS 中 $S^3$ 配分函数与手术公式的闭合形式，是“可计算性”的核心。",
    "公式在 WZW 里是定理（TUY、Faltings），在 CS 里是“物理推导 + 数学证明”。",
    "截断（可积性）让求和有限，否则公式发散。"
  ],
  "formulas": ["$R_i\\otimes R_j=\\bigoplus_kN_{ij}^kR_k$", "$N_{ij}^k=\\sum_l\\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$", "$v_iv_j=\\sum_kN_{ij}^kv_k$"],
  "theorems": [T("Verlinde 公式",
    "对可积表示，融合系数由 $N_{ij}^k=\\sum_lS_{il}S_{jl}S_{kl}/S_{0l}$ 给出；等价地，Verlinde 代数在对角基下是幂等的。",
    "sketch",
    [S("在 $S^2\\times S^1$ 上做手术，把 $\\Sigma$ 换成 $S^3$，用两种方式算配分函数。", "这是 Witten §4.5 的路线。"),
     S("手术关系给出 $\\sum_kS_i{}^kN_{kl}{}^m=S_{il}S_i{}^m/S_{0i}$，即 $S$ 对角化融合矩阵。", "两种算法相等给出该关系。"),
     S("把该关系写成特征值形式即 Verlinde 公式。", "$S$ 的行是融合矩阵的共同特征向量。")],
    "witten1989/sections/s08-calculability-c.tex（§4.5，原文 p.388–393）",
    "Witten 的推导是物理的（依赖手术与量子化自洽性）；严格数学证明由 TUY/Faltings 给出。")
  ],
  "pitfalls": [
    "不要把 $S$ 与融合矩阵 $N$ 混淆：$S$ 是模变换矩阵，$N$ 是融合系数张量。",
    "公式里的求和必须只对可积表示；否则不收敛。",
    "归一化：$S_{0l}$ 的分母与 $S$ 的归一化绑定，换约定要整体改。"
  ],
  "related": ["csw/concept/s-matrix", "csw/concept/verlinde-formula", "csw/concept/conformal-blocks", "csw/example/su2-k2-s-matrix"],
  "sources": [src(W, "§3.4（(3.6)）与 §4.5（(4.51)）", [374, 393], [24, 43], "witten1989/sections/s05-hilbert.tex（§3.4）与 s08-calculability-c.tex（§4.5）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/cs-wzw-duality", "type": "concept", "track": "F",
  "title": "CS/WZW 对偶：态空间的等同",
  "aliases": ["CS/WZW duality", "3d/2d correspondence", "CS/WZW 对偶"],
  "summary": "三维 CS 在 $\\Sigma\\times\\mathbb{R}$ 上的量子 Hilbert 空间等于二维 WZW 在 $\\Sigma$ 上的共形块空间；这是“态空间等同”，不是动力学等价。",
  "question": "这个“对偶”到底是什么级别的等同？与 AdS₃/CFT₂ 有什么区别？",
  "definition": {
    "text": "固定曲面 $\\Sigma$（可带标记点与表示），CS 理论在 $\\Sigma\\times\\mathbb{R}$ 上正则量子化给出 $\\cH_\\Sigma$；WZW 理论在 $\\Sigma$ 上的共形块空间也是 $\\cH_\\Sigma$。两者作为向量空间（更精确：射影平坦丛的纤维）等同。三维配分函数只在 $X\\times S^1$ 上以 $Z=\\dim\\cH_X$ 的方式接触二维数据，**没有**体/边界配分函数的等式。",
    "notation": "$\\cH_\\Sigma$ 是态空间；$Z(X\\times S^1)=\\dim\\cH_X$；本文没有 AdS/全息的语言。"
  },
  "key_points": [
    "等同的是“态空间”，不是“配分函数”：没有边界 CFT 的动力学。",
    "原文用 “are”（p.370），不是 “isomorphic to”；只到对象级，函子性在 §5 一句带过。",
    "三维理论无度规、无局域自由度，态空间有限维；这与引力对偶的“体有引力子”根本不同。",
    "“3d 引力 = CS”只是经典相空间层面的改写（非紧群），不是本文的结论。",
    "这是“拓扑量子场论”的典型结构：拓扑不变量 = 态空间的维数/迹。"
  ],
  "formulas": ["$\\cH^{CS}_\\Sigma\\cong\\cH^{WZW}_\\Sigma=H^0(\\cM_J,\\cL^{\\otimes k})$", "$Z_{CS}(X\\times S^1)=\\dim\\cH_X$"],
  "theorems": [T("态空间等同",
    "对紧曲面 $\\Sigma$ 与可积表示，CS 的量子 Hilbert 空间与 WZW 的共形块空间作为向量空间同构，且都带同一个射影平坦联络。",
    "sketch",
    [S("CS 侧由几何量子化给出 $H^0(\\cM_J,\\cL^{\\otimes k})$。", "这是本文 §3 的主要结果。"),
     S("WZW 侧的共形块由 Ward 恒等式与 KZ 刻画，其空间也是 $H^0$。", "KZ 是 Hitchin 联络在 $g=0$ 的显式形式。"),
     S("两边维数一致（Verlinde 公式）且由同一线丛给出，故同构。", "本文把它当作物理等同，严格证明由 Segal/TUY 补。")],
    "witten1989/sections/s09-applications.tex（§5，p.396–397）；等同句在 p.370",
    "函数性/缝合只在 p.397 用 “It is obvious” 带过；不是范畴等价。")
  ],
  "pitfalls": [
    "不要说“CS 理论 = WZW 理论”：等同只在态空间层面，三维理论还有手术不变量等额外结构。",
    "不要把它与 AdS₃/CFT₂ 混为一谈：后者是动力学对偶（体引力 + 边界 CFT），前者是拓扑态空间等同。",
    "原文没有“全息”字样；1988 年也没有 AdS/CFT。"
  ],
  "related": ["csw/concept/conformal-blocks", "csw/concept/mapping-class-group", "csw/concept/cs-vs-ads3-cft2", "csw/concept/verlinde-formula"],
  "sources": [src(W, "§5 Applications to Physics（p.396–397）与 §3.2（p.370）", [370, 397], [20, 47], "witten1989/sections/s09-applications.tex（§5）")],
  "rights": "rewritten", "status": "draft"
},
{
  "id": "csw/concept/mapping-class-group", "type": "concept", "track": "F",
  "title": "映射类群与模函子",
  "aliases": ["mapping class group", "MCG", "modular functor"],
  "summary": "$\\operatorname{MCG}(\\Sigma)$ 通过“剪开-扭转-粘回”作用于 $\\Sigma$，得到 $\\cH_\\Sigma$ 上的射影表示；Segal 的模函子把这套结构公理化。",
  "question": "为什么映射类群的作用只到射影？它与三维手术有什么关系？",
  "definition": {
    "text": "映射类群 $\\operatorname{MCG}(\\Sigma)=\\pi_0\\operatorname{Diff}^+(\\Sigma)$ 作用在 $\\Sigma$ 上；把它看成 $\\Sigma\\times[0,1]$ 的边界粘合，得到三维流形 $M_\\phi$。CS 的量子化给出 $\\operatorname{MCG}(\\Sigma)$ 在 $\\cH_\\Sigma$ 上的射影表示（因为 $\\cH_\\Sigma$ 只是射影平坦丛的纤维）。Segal 的模函子把“曲面→向量空间、粘合→配对、映射类→射影自同构”公理化。",
    "notation": "$\\phi\\in\\operatorname{MCG}(\\Sigma)$；$M_\\phi=\\Sigma\\times[0,1]/(x,1)\\sim(\\phi(x),0)$；$\\rho:\\operatorname{MCG}\\to\\mathrm{PGL}(\\cH_\\Sigma)$。"
  },
  "key_points": [
    "映射类群的作用是射影的：整体相位不可消除（共形反常）。",
    "三维手术 = 沿环面粘合，其“粘合映射”就是 $\\operatorname{MCG}(T^2)=SL(2,\\mathbb{Z})$ 的元素。",
    "把 $\\Sigma$ 剪开再粘回得到 $M_\\phi$，其配分函数 $Z(M_\\phi)=\\operatorname{Tr}_{\\cH_\\Sigma}\\rho(\\phi)$（TQFT 的迹公式）。",
    "模函子（Segal）是“共形场论 = 函子”的严格版本；CS 给出它的构造。",
    "单值性 = 映射类群表示；这正是“共形块为什么是三维的”的答案。"
  ],
  "formulas": ["$\\rho:\\operatorname{MCG}(\\Sigma)\\to\\mathrm{PGL}(\\cH_\\Sigma)$", "$Z(M_\\phi)=\\operatorname{Tr}_{\\cH_\\Sigma}\\rho(\\phi)$", "$\\operatorname{MCG}(T^2)=SL(2,\\mathbb{Z})$"],
  "theorems": [T("映射类群表示与手术",
    "CS 量子化给出 $\\operatorname{MCG}(\\Sigma)$ 在 $\\cH_\\Sigma$ 上的射影表示；对 $\\phi\\in\\operatorname{MCG}$，$Z(M_\\phi)=\\operatorname{Tr}\\rho(\\phi)$ 且与手术描述一致。",
    "sketch",
    [S("$\\operatorname{MCG}$ 作用在 $\\Sigma$ 上，逐点作用在态空间上，得射影表示。", "射影性来自 $\\cH_\\Sigma$ 的射影平坦性。"),
     S("把 $\\phi$ 看成 $\\Sigma\\times[0,1]$ 的边界粘合，得 $M_\\phi$。", "这是映射环面的构造。"),
     S("沿边界收缩给出迹公式 $Z(M_\\phi)=\\operatorname{Tr}\\rho(\\phi)$。", "这是 TQFT 的“态-配分函数”对应。")],
    "witten1989/sections/s04-canonical.tex（§3.2）与 s09-applications.tex（§5）",
    "本文只说“模函子可在三维量子化中得到”，未系统展开；Segal 的严格版见其 1988/2004 讲义。")
  ],
  "pitfalls": [
    "射影表示不是线性表示：不要忽略相位，它影响手术不变量。",
    "$\\operatorname{MCG}(T^2)=SL(2,\\mathbb{Z})$ 作用在 $\\cH(T^2)$ 上就是 $S,T$ 矩阵；这是 Verlinde 公式的几何来源。",
    "不同亏格的映射类群差别很大；别把环面的结论直接搬到高亏格。"
  ],
  "related": ["csw/concept/cs-wzw-duality", "csw/concept/projective-flat-connection", "csw/concept/s-matrix", "csw/concept/surgery-formula"],
  "sources": [src(W, "§3.2 与 §5（模函子）", [369, 397], [19, 47], "witten1989/sections/s04-canonical.tex（§3.2）与 s09-applications.tex（§5）")],
  "rights": "rewritten", "status": "draft"
}
]
