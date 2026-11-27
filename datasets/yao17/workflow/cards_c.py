# -*- coding: utf-8 -*-
"""cards_c.py —— 轨 C：分类与不变量（5 张概念卡）。"""


def add(mk):
    mk(
        id="yao17/concept/zelevinsky-segment",
        type="concept",
        track="C",
        title="Zelevinsky 段 Δ(π,m)、linked/precedes 与 (∗) 条件",
        aliases=["segment", "段", "Δ(π,m)", "(∗)", "Asc_n"],
        summary="段是 Asc_n 中有限区间 [π,π(1),…,π(m−1)]；两段 linked 指互不包含但并仍是段，precedes 再加 π1<π2；(∗) 禁掉 i<j 的 precede。",
        question="段、linked、precedes 三个概念各自抓住超尖点表示阶梯上的什么信息？(∗) 条件为什么只对同维的段对起作用？",
        definition={
            "text": "$\\pi(s)$ 记 $\\pi$ 用 $|\\det|^s$ 的扭转。在 $\\GL_n(K)$ 的不可约超尖点表示的同构类上定偏序：$\\pi\\le\\pi'$ 当且仅当 $\\pi'=\\pi(s)$，$s\\in\\mathbb Z_{\\ge0}$，得偏序集 $\\Asc_n$。$\\Asc_n$ 的有限区间称 Zelevinsky 段：$\\Delta(\\pi,m)=[\\pi,\\pi(1),\\dots,\\pi(m-1)]$，长 $m$、次数 $mn$。两段 $\\Delta_1,\\Delta_2$ linked，若 $\\Delta_1\\not\\subset\\Delta_2$、$\\Delta_2\\not\\subset\\Delta_1$ 且 $\\Delta_1\\cup\\Delta_2$ 是段（这只能在 $n_1=n_2$ 时发生）。$\\Delta_1$ precedes $\\Delta_2$，若二者 linked 且 $\\pi_1<\\pi_2$。(∗) 条件：对每个 $i<j$，$\\Delta_i$ 不 precede $\\Delta_j$。",
            "notation": "$\\pi(\\Delta):=\\pi_1\\times\\dots\\times\\pi_m=I^{\\GL_{mn}}_{P(n,\\dots,n)}(\\pi_1\\otimes\\dots\\otimes\\pi_m)$；$(\\ast)$-置换指使条件仍成立的置换；底本脚注 9：文献亦称 Bernstein–Zelevinsky 段。",
        },
        key_points=[
            "段是「同一个超尖点表示沿 $|\\det|$ 整数次幂排成的一串」：$\\Delta(\\pi,m)$ 的每个成员都是超尖点，但整段诱导出来一般可约，其长度由定理 3.1(1) 给出 $2^{m-1}$。",
            "linked 只在 $n_1=n_2$ 时可能（不同维的段并起来不是段），所以 (∗) 在「维数互不相同」时是空条件——这点底本在 (∗) 的注 (1) 里明说。",
            "precedes 是有方向的：$\\Delta_1$ precedes $\\Delta_2$ 要求 $\\pi_1<\\pi_2$，即「低端更靠下」；底本的例子 $\\Delta=[\\pi,\\pi(1)]$、$\\Delta'=[\\pi(2),\\pi(3)]$ 里 $(\\Delta,\\Delta')$ 违反 (∗)，而 $(\\Delta',\\Delta)$ 与 $\\Delta\\cup\\Delta'$ 都满足。",
            "(∗) 的作用在定理 3.1(3)(4)：它给出「段的有序组 → 唯一不可约商 $Q(\\Delta_1,\\dots,\\Delta_r)$」，而 (∗)-置换不改变 $Q$——所以 (∗) 是「同一不可约表示的一族等价的书写方式」。",
        ],
        formulas=[
            "$\\Delta(\\pi,m)=[\\pi,\\pi(1),\\dots,\\pi(m-1)],\\qquad \\deg\\Delta=mn$",
            "$\\pi\\le\\pi'\\iff \\pi'=\\pi(s),\\ s\\in\\mathbb Z_{\\ge0}$",
            "$(\\ast):\\ \\forall i<j,\\ \\Delta_i\\ \\text{不 precedes}\\ \\Delta_j$",
            "$\\pi(\\Delta)=\\pi_1\\times\\dots\\times\\pi_m=I^{\\GL_{mn}}_{P(n,\\dots,n)}(\\pi_1\\otimes\\dots\\otimes\\pi_m)$",
        ],
        pitfalls=[
            "段里的 $\\pi(i)$ 是 $\\pi$ 乘 $|\\det|^i$，不是「$i$ 次张量幂」；$\\pi_1\\times\\dots\\times\\pi_m$ 是抛物诱导，不是张量积。",
            "「$\\Delta_1\\cup\\Delta_2$ 是段」要求两个区间在 $\\Asc_n$ 里首尾相接；只按集合包含关系判断会漏掉「有空洞」的情形。",
        ],
        related=[
            "yao17/concept/bz-classification",
            "yao17/concept/supercuspidal-support",
            "yao17/concept/parabolic-induction",
        ],
        sources=[
            {
                "text": "A",
                "section": "§3.1.1–§3.1.2",
                "pages": [23, 23],
                "quote": "A Zelevinsky segment starting from π of length m and degree mn is an ordered finite collection of m irreducible supercuspidal representations",
                "anchor": "A p.23",
            }
        ],
        provenance_note="段、linked、precedes、(∗) 与 $\\pi(\\Delta)$ 的定义照 p.23 的 3.1.1–3.1.2；例子与「(∗) 是同一表示的等价书写」的解释取自同页例子与我们的判断。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/supercuspidal-support",
        type="concept",
        track="C",
        title="超尖点支撑与 Steinberg 表示 St_n",
        aliases=["supercuspidal support", "Steinberg", "St_n", "Supp(π)"],
        summary="超尖点支撑是 Q 与 Z 共有的唯一无序超尖点组；取 Δ=[|·|^{(1−n)/2},…,|·|^{(n−1)/2}] 时 Z(Δ)=triv、Q(Δ)=St_n（自对偶）。",
        question="超尖点支撑为什么是「唯一无序组」？Steinberg 表示是怎么作为一个段诱导的唯一不可约商出现的？",
        definition={
            "text": "对 $\\pi\\cong Q(\\Delta_1,\\dots,\\Delta_r)$，$\\Delta_i=\\Delta(\\pi_i,m_i)$，超尖点支撑是（无序）集合 $\\Supp(\\pi)=\\{\\pi_i(j)\\}_{i=1..r,\\ j=0..m_i-1}$。Zelevinsky 注：$\\Supp(\\pi)$ 是唯一的无序组 $\\sigma_1,\\dots,\\sigma_s$，使 $Q(\\Delta_1,\\dots,\\Delta_r)$ 与 $Z(\\Delta_1,\\dots,\\Delta_r)$ 都是 $\\sigma_1\\times\\dots\\times\\sigma_s$ 的子商。取 $\\Delta=\\Delta(|\\cdot|^{(1-n)/2},n)=[|\\cdot|^{(1-n)/2},|\\cdot|^{(3-n)/2},\\dots,|\\cdot|^{(n-1)/2}]$，则 $\\pi(\\Delta)=|\\cdot|^{(1-n)/2}\\times\\dots\\times|\\cdot|^{(n-1)/2}=\\{B\\backslash G\\ \\text{上的光滑函数}\\}$，$Z(\\Delta)=\\mathrm{triv}$（常函数），$Q(\\Delta)=:\\St_n$ 称（标准）Steinberg 表示，自对偶 $\\St_n^\\vee=\\St_n$。",
            "notation": "模特征标在 $B$ 上：$x=\\mathrm{Diag}(x_1,\\dots,x_n)$ 时 $\\delta(x)=|x_1^{n-1}x_3^{n-3}\\cdots x_n^{1-n}|$；这里 $\\pi_T=|\\cdot|^{(1-n)/2}\\otimes\\dots\\otimes|\\cdot|^{(n-1)/2}=\\delta^{-1/2}$。",
        },
        key_points=[
            "支撑的定义只用到 $Q(\\Delta_i)$ 的段的成员，与排列无关；Zelevinsky 注的力道在于：$Q$ 侧与 $Z$ 侧（商与子）诱导出同一个无序组，故支撑是 $\\pi$ 的内在不变量，而不是某个分解的附属物。",
            "$\\St_n$ 的构造是「把 $\\delta^{-1/2}$ 当成 $T$ 上的特征标诱导上去」：此时 $\\pi(\\Delta)$ 就是 $(B\\backslash G)$ 上的光滑函数空间（未正规化诱导 = 右平移作用），常函数给出唯一不可约子 $\\mathrm{triv}$，商即 $\\St_n$。",
            "$n=2$ 时给出短正合列 $0\\to\\mathrm{triv}\\to|\\cdot|^{-1/2}\\times|\\cdot|^{1/2}\\to\\St_2\\to0$；反过来 $|\\cdot|^{1/2}\\times|\\cdot|^{-1/2}$ 的短正合列是 $0\\to\\St_2\\to\\cdot\\to\\mathrm{triv}\\to0$——两个顺序给出相反的「子/商」，这正是 (∗) 与 linked 的几何内容。",
            "$\\St_n$ 自对偶（$\\St_n^\\vee=\\St_n$）在 $\\GL_2$ 情形对应 $\\Sp_2$ 的 WD 表示，在一般 $n$ 对应 $\\Sp_n$——Steinberg 是「最非半单」的不可约表示，其 $N$ 的幂零指数恰为 $n$。",
        ],
        formulas=[
            "$\\Supp(\\pi)=\\{\\pi_i(j)\\}_{i=1..r,\\ j=0..m_i-1}\\quad(\\text{无序})$",
            "$\\Delta(|\\cdot|^{(1-n)/2},n)=[|\\cdot|^{(1-n)/2},|\\cdot|^{(3-n)/2},\\dots,|\\cdot|^{(n-1)/2}]$",
            "$Z(\\Delta)=\\mathrm{triv},\\qquad Q(\\Delta)=\\St_n,\\qquad \\St_n^\\vee=\\St_n$",
            "$0\\to\\mathrm{triv}\\to|\\cdot|^{-1/2}\\times|\\cdot|^{1/2}\\to\\St_2\\to0\\ (n=2)$",
        ],
        pitfalls=[
            "支撑里的 $\\pi_i(j)$ 含 $j=0$ 到 $m_i-1$ 共 $m_i$ 项，容易只写 $m_i-1$ 项（底本 p.25 的排版也只写到 $j=1,\\dots,m_i-1$，实为漏了 $j=0$，见下条）。",
            "$\\St_n$ 不是 $\\pi(\\Delta)$ 本身而是它的不可约商；$\\pi(\\Delta)$ 的长度为 $2^{n-1}$，只有 $n=2$ 时才只有两个 Jordan–Hölder 因子。",
        ],
        related=[
            "yao17/concept/zelevinsky-segment",
            "yao17/concept/bz-classification",
            "yao17/concept/square-integrable-tempered",
            "yao17/deriv/gl2-llc-cases",
        ],
        sources=[
            {
                "text": "A",
                "section": "§3.1.4–§3.1.5",
                "pages": [25, 26],
                "quote": "The unique quotient Q(Δ) =: St_n is defined to be the (standard) Steinberg representation of GL_n(K)",
                "anchor": "A p.26",
            }
        ],
        provenance_note="支撑定义与 Zelevinsky 注取自 p.25；Steinberg 的构造、δ 公式、$\\mathrm{triv}$/$\\St_2$ 两条短正合列取自 p.25–p.26。第一条 pitfalls 中「底本写作 $j=1,\\dots,m_i-1$」是转录所见，与我们按定义补的 $j=0$ 不一致，已在译本作译注。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/square-integrable-tempered",
        type="concept",
        track="C",
        title="本质 L^r、平方可积、缓增：定理 3.2、3.3 与推论 3.4",
        aliases=["square integrable", "tempered", "定理 3.2", "定理 3.3"],
        summary="本质平方可积 ⇔ π=Q(Δ) 单段；缓增 ⇔ 每段都平方可积；两者之间还有本质 L^{2+ε} 的连续层级。",
        question="«平方可积» 与 «缓增» 在段语言下各自长什么样？为什么定理 3.2 里要额外看 ρ((m−1)/2) 的中心特征标？",
        definition={
            "text": "令 $G^0=\\{g\\in\\GL_n(K):|\\det g|_K=1\\}$。(1) 容许 $\\pi$ 称本质 $L^r$，若对任意 $v,\\lambda$，矩阵系数 $c_{v,\\lambda}$ 在 $G^0$ 上 $L^r$（即 $\\int_{G^0}|c_{v,\\lambda}|^r dg$ 收敛）；(2) 若再加中心特征标 $\\omega_\\pi$ 酉，称 $L^r$；(3) 本质平方可积 = 本质 $L^2$，平方可积 = $L^2$；本质缓增 = 对一切 $\\epsilon>0$ 本质 $L^{2+\\epsilon}$，缓增再加 $\\omega_\\pi$ 酉。定理 3.2（Zelevinsky）：(1) 不可约容许 $\\pi$ 本质平方可积 $\\iff$ $\\pi\\cong Q(\\Delta)$（单个段）；(2) 此 $Q(\\Delta)$ 平方可积 $\\iff$ $Q(\\Delta)=\\Delta(\\sigma,m)$ 时 $\\rho(\\tfrac{m-1}{2})$ 的中心特征标酉。定理 3.3：$\\pi=Q(\\Delta_1,\\dots,\\Delta_r)$ 缓增 $\\iff$ 每个 $Q(\\Delta_i)$ 平方可积。",
            "notation": "层级：$\\text{超尖点}\\subset\\text{平方可积}\\subset\\text{缓增}\\subset\\text{一般}\\subset\\text{容许}$；推论 3.4 与定理 3.6 把「缓增」与「一般且每段中心特征标酉」对上。",
        },
        key_points=[
            "定理 3.2(1) 把「平方可积」变成纯组合条件：$\\pi$ 只由一个段诱导（于是 $\\Supp(\\pi)$ 是单一超尖点的阶梯），而定理 3.2(2) 的 $\\rho(\\frac{m-1}{2})$ 是校正项，确保中心特征标酉——这正是「本质」与「非本质」的差别。",
            "定理 3.3 说缓增性是「逐段」的：$Q(\\Delta_1,\\dots,\\Delta_r)$ 缓增 $\\iff$ 每个 $Q(\\Delta_i)$ 平方可积；配合定理 3.1(5)，推论 3.4 进一步得到任两段不 linked，故 $\\pi\\cong Q(\\Delta_1)\\times\\dots\\times Q(\\Delta_r)$ 本身不可约。",
            "「本质」只是中心特征标不酉；Casselman 80' 的注说任一光滑表示可乘一个正实值拟特征标把中心特征标变酉，故本质 $L^r$ 与 $L^r$ 的差别在 $\\GL_n$ 情形是可控的。",
            "底本 Remark 指出反向的困难：用 Zelevinsky 段去分类「本质缓增」似乎不容易（因为本质缓增的真条件是对所有 $\\epsilon>0$ 的本质 $L^{2+\\epsilon}$），可见这条层级在中间地带并不干净。",
        ],
        formulas=[
            "$\\int_{G^0}|c_{v,\\lambda}(g)|^r\\,dg<\\infty\\quad(\\text{本质 }L^r)$",
            "$\\pi\\ \\text{本质平方可积}\\iff \\pi\\cong Q(\\Delta)\\ (\\text{单个段})$",
            "$\\pi=Q(\\Delta_1,\\dots,\\Delta_r)\\ \\text{缓增}\\iff Q(\\Delta_i)\\ \\text{平方可积}\\ \\forall i$",
            "$\\text{缓增}\\ \\Longrightarrow\\ \\pi\\cong Q(\\Delta_1)\\times\\dots\\times Q(\\Delta_r)\\ (\\text{无 linked})$",
        ],
        theorems=[
            {
                "name": "定理 3.2（Zelevinsky）",
                "statement": "不可约容许 $\\pi$ 本质平方可积 $\\iff$ $\\pi\\cong Q(\\Delta)$ 为单个段；$Q(\\Delta(\\sigma,m))$ 平方可积 $\\iff$ $\\sigma(\\frac{m-1}{2})$ 的中心特征标酉。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本只陈述，未给证明；它依赖 Casselman 的矩阵系数判据与段诱导的显式计算。",
                },
                "source": "A §3.2.1 p.27",
            },
            {
                "name": "定理 3.3（Zelevinsky）",
                "statement": "$Q(\\Delta_1,\\dots,\\Delta_r)$ 缓增 $\\iff$ 每个 $Q(\\Delta_i)$ 平方可积。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本只陈述；推论 3.4 的证明被给出，但其论证只用到「$\\sigma$ 有酉中心特征标时 $\\omega_\\sigma(s)$ 对非零 $s$ 不酉」这一事实。",
                },
                "source": "A §3.2.2 p.27",
            },
        ],
        pitfalls=[
            "本质平方可积（essential）与平方可积差一个中心特征标的酉性；底本在定理 3.2(2) 用 $\\rho(\\frac{m-1}{2})$ 显式写出这个校正，漏掉会误判。",
            "「缓增 + 一般」并不等价于「缓增」：定理 3.6 的另一半需要每段中心特征标酉，底本 Remark 已点明这个差别。",
        ],
        related=[
            "yao17/concept/supercuspidal-support",
            "yao17/concept/generic-whittaker",
            "yao17/concept/llc-finer-properties",
        ],
        sources=[
            {
                "text": "A",
                "section": "§3.2.1–§3.2.2",
                "pages": [27, 27],
                "quote": "An irreducible admissible representation π of GL_n(K) is essentially square integrable if and only if it is of the form Q(Δ) for a (single) Zelevinsky segment Δ",
                "anchor": "A p.27",
            }
        ],
        provenance_note="本质 $L^r$/$L^r$/本质缓增的定义、定理 3.2/3.3 与推论 3.4 取自 p.27；「本质与平方可积只差中心特征标」是我们的解读。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/generic-whittaker",
        type="concept",
        track="C",
        title="一般（generic）表示、Whittaker 模型与定理 3.6",
        aliases=["generic", "Whittaker model", "θ_ψ", "定理 3.6"],
        summary="generic 指 π|U_n 上有非零的 θ_ψ-同态；Zelevinsky 定理说它等价于段两两不 linked，故缓增必 generic。",
        question="θ_ψ 是怎么从加性特征标 ψ 造出来的？为什么「段两两不 linked」正好刻画 generic？",
        definition={
            "text": "取 $K$ 的非平凡加性拟特征标 $\\psi$，$n(\\psi)$ 为使 $\\psi(\\varpi^{-n}\\mathcal O_K)=1$ 的最大整数。$U_n\\subset\\GL_n(K)$ 是严格上三角群，定义一维表示 $\\theta_\\psi(u_{ij})=\\psi(u_{12}+\\dots+u_{n-1,n})$。不可约容许 $\\pi$ 称一般（generic），若 $\\Hom_{U_n}(\\pi|_{U_n},\\theta_\\psi)\\neq0$。取非零 $\\lambda\\in\\Hom_{U_n}(\\pi|_{U_n},\\theta_\\psi)$，Whittaker 模型 $W_\\psi=\\{f\\colon G\\to\\mathbb C: f(ug)=\\theta_\\psi(u)f(g)\\}$，$G$ 右平移作用，$v\\mapsto(g\\mapsto\\lambda(\\pi(g)v))$ 是单 $G$-同态，像记 $W_{\\pi,\\psi}$。",
            "notation": "$\\theta_\\psi$ 是 $U_n$ 的特征标，沿「主对角线之上第一条」求和；引理 3.5：(1) generic 性与 $\\psi$ 选取无关；(2) $\\pi$ generic $\\iff$ $\\pi^\\vee$ generic；(3) 任意拟特征标扭转保持 generic。",
        },
        key_points=[
            "定理 3.6（Zelevinsky）：$Q(\\Delta_1,\\dots,\\Delta_r)$ generic $\\iff$ 任两段不 linked $\\iff$ $\\pi=Q(\\Delta_1)\\times\\dots\\times Q(\\Delta_r)$——最后一步用定理 3.1(5)。于是推论 3.4 可重述为「每个不可约（本质）缓增表示都是 generic」。",
            "Whittaker 模型的构造是「把 $\\lambda$ 卷进右平移」：$v\\mapsto(g\\mapsto\\lambda(\\pi(g)v))$ 自动满足 $f(ug)=\\theta_\\psi(u)f(g)$，且由 $\\pi$ 不可约与 $\\lambda\\neq0$ 保证单射。底本特意点明像与 $\\pi$ 同构。",
            "generic 在整体应用里是主力：Shalika 注说数域上不可约容许尖点自守表示 $\\pi=\\otimes'_v\\pi_v$ 的每个局部分量都 generic——这正是局部理论要单独发展 generic 的原因。",
            "底本脚注 11 说 $\\epsilon$ 因子的定义要靠 Whittaker 模型（「Much more to be added in second draft」），故 §3.6 的 $\\epsilon$ 在底本里其实留了缺口：只有 JPPS 公式而无 Whittaker 侧的定义。",
        ],
        formulas=[
            "$\\theta_\\psi(u_{ij})=\\psi(u_{12}+\\dots+u_{n-1,n})$",
            "$\\pi\\ \\text{generic}\\iff \\Hom_{U_n}(\\pi|_{U_n},\\theta_\\psi)\\neq0$",
            "$v\\mapsto\\big(g\\mapsto\\lambda(\\pi(g)v)\\big)\\colon V\\hookrightarrow W_\\psi$",
            "$Q(\\Delta_1,\\dots,\\Delta_r)\\ \\text{generic}\\iff \\Delta_i,\\Delta_j\\ \\text{不 linked}\\ (i\\neq j)$",
        ],
        theorems=[
            {
                "name": "定理 3.6（Zelevinsky）",
                "statement": "$\\pi=Q(\\Delta_1,\\dots,\\Delta_r)$ generic $\\iff$ 任两段不 linked $\\iff$ $\\pi=Q(\\Delta_1)\\times\\dots\\times Q(\\Delta_r)$。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本只陈述，并引定理 3.1(5) 完成第二个「当且仅当」；Whittaker 侧的计算未写。",
                },
                "source": "A §3.2.3 p.28",
            },
            {
                "name": "引理 3.5",
                "statement": "(1) generic 性与 $\\psi$ 的选取无关；(2) $\\pi$ generic $\\iff$ $\\pi^\\vee$ generic；(3) 拟特征标扭转保持 generic。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本只列三条，未给证明。",
                },
                "source": "A §3.2.3 p.28",
            },
        ],
        pitfalls=[
            "generic 是「$\\pi|_{U_n}$ 上有 $\\theta_\\psi$-同态」，不是「$\\pi$ 有一维 $U_n$-固定向量」；$\\theta_\\psi$ 非平凡，两者完全不同。",
            "定理 3.6 的等价要求段两两不 linked，而不是「段两两不同」：$\\Delta$ 与 $\\Delta'$ linked 时 $Q(\\Delta)\\times Q(\\Delta')$ 可约，$\\pi$ 只能取 $Q(\\Delta,\\Delta')$。",
        ],
        related=[
            "yao17/concept/square-integrable-tempered",
            "yao17/concept/bz-classification",
            "yao17/concept/llc-finer-properties",
            "yao17/concept/inertial-correspondence",
        ],
        sources=[
            {
                "text": "A",
                "section": "§3.2.3",
                "pages": [28, 28],
                "quote": "An irreducible admissible representation π of GL_n(K) is generic if Hom_{U_n}(π|_{U_n}, θ_ψ) ≠ 0",
                "anchor": "A p.28",
            }
        ],
        provenance_note="θ_ψ、generic 与 Whittaker 模型的定义、引理 3.5、定理 3.6 与 Shalika 注取自 p.28；「脚注 11 说 §3.6 留了缺口」是据同页脚注的观察。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/conductor-depth",
        type="concept",
        track="C",
        title="导子 c(π)、深度、JPPS 的 ε 公式与深度 0 对照图",
        aliases=["conductor", "depth", "JPPS", "引理 3.8"],
        summary="ε(π,s,ψ)=q^{−(c(π)+n·n(ψ))s}ε(π,0,ψ)；深度 0 的 π 对应驯分歧的 r_n(π)，非分歧对应 ρ|I_K=0 且 N=0。",
        question="§3.5 的对照图用五条 ⇔ 把自守侧与 Galois 侧的「分歧程度」逐级对应，各条的依据分别是什么？",
        definition={
            "text": "对光滑不可约 $\\pi$，令 $L(\\pi,s)$、$\\epsilon(\\pi,s,\\psi)$ 为 $\\pi'$ 取平凡特征标时的因子。JPPS 定理（及其修正）：$\\epsilon(\\pi,s,\\psi)=q^{-(c(\\pi)+n\\cdot n(\\psi))s}\\epsilon(\\pi,0,\\psi)$，其中 $c(\\pi)$ 是 §3.4 定义的导子；底本指出文献中两种导子定义（§3.4 的与由 $L(\\pi,s)$ 函数方程定义的）一致。引理 3.8：在 LLC 下 $c(\\pi)=c(\\rec_n(\\pi))$。§3.5 对照图：$\\pi$ 非分歧 $\\iff\\pi^K\\neq0$；$r_n(\\pi)$ 非分歧 $\\iff\\rho|_{I_K}=0$ 且 $N=0$；$\\pi$ Iwahori-球面 $\\iff\\pi^{\\Iw}\\neq0$；$\\rec_n(\\pi)$ 为 $I_K$-球面 $\\iff\\rho|_{I_K}=0$；$\\pi$ 深度 0 $\\iff$ $r_n(\\pi)$ 驯分歧。",
            "notation": "$K=\\GL_n(\\mathcal O_K)$，$\\Iw=B_0$ 是 Iwahori 子群（约化模 $\\Bbbk$ 的标准 Borel 的原像）；$r_n=\\WD^{-1}\\circ\\rec_n$ 是 $\\ell$ 进表示；$n=n$ 表示 $\\dim\\pi$。",
        },
        key_points=[
            "引理 3.8 的证明是「比较指数」：由 $\\epsilon$ 相容性 $\\epsilon(\\pi,\\psi,s)=\\epsilon(\\rec_n(\\pi),\\psi,s)$，再用推论 1.4 把两侧都写成 $q^{-(\\cdot)s}$，比较指数即得 $c(\\pi)=c(\\rec_n(\\pi))$。",
            "对照图的三级结构很值得记：非分歧（$K$-固定）对应 $\\rho|_{I_K}=0$ 且 $N=0$；Iwahori-球面对应「$I_K$ 上平凡但 $N$ 可非零」（$I_K$-球面）；深度 0 对应驯分歧（$\\rho|_{P_K}$ 的像落在更小群，且 $N$ 无约束）。",
            "深度概念由 Moy–Prasad 引入，底本在 §2.3.1 的 Remark 里就把它与导子并列为 LLC 保持的两大量；§3.4「导子与新向量」与 §3.5.1「导子与深度」在底本里都只留标题，正文空缺。",
            "JPPS 公式的形式与推论 1.4 完全同构：一侧是 $c(\\rho)+n(\\psi)\\dim V$，一侧是 $c(\\pi)+n\\cdot n(\\psi)$——所以「导子守恒」几乎是这个形式对应的直接推论。",
        ],
        formulas=[
            "$\\epsilon(\\pi,s,\\psi)=q^{-(c(\\pi)+n\\,n(\\psi))s}\\,\\epsilon(\\pi,0,\\psi)$",
            "$c(\\pi)=c(\\rec_n(\\pi))\\quad(\\text{LLC 下})$",
            "$\\pi\\ \\text{非分歧}\\iff\\pi^K\\neq0,\\qquad r_n(\\pi)\\ \\text{非分歧}\\iff\\rho|_{I_K}=0\\ \\&\\ N=0$",
            "$\\pi\\ \\text{深度}\\ 0\\iff r_n(\\pi)\\ \\text{驯分歧}$",
        ],
        theorems=[
            {
                "name": "引理 3.8（导子被 LLC 保持）",
                "statement": "在 LLC 下 $c(\\pi)=c(\\rec_n(\\pi))$。",
                "proof": {
                    "status": "complete",
                    "steps": [
                        {
                            "no": 1,
                            "text": "取 $\\pi'$ 为平凡特征标，由 LLC 性质 (2) 的 $\\epsilon$ 相容性得 $\\epsilon(\\pi,\\psi,s)=\\epsilon(\\rec_n(\\pi),\\psi,s)$。",
                            "why": "这是定理 2.13(2) 在 $n_2=0$（平凡特征标）时的特例。",
                        },
                        {
                            "no": 2,
                            "text": "两侧分别用 JPPS 公式与推论 1.4 写成 $q^{-(c(\\pi)+n n(\\psi))s}\\epsilon(\\pi,0,\\psi)$ 与 $q^{-(c(\\rec_n\\pi)+n n(\\psi))s}\\epsilon(\\rec_n\\pi,0,\\psi)$。",
                            "why": "两个公式的指数结构相同，故可直接比较。",
                        },
                        {
                            "no": 3,
                            "text": "比较 $s$ 的系数得 $c(\\pi)=c(\\rec_n(\\pi))$。",
                            "why": "$q\\neq1$，指数相等即系数相等。",
                        },
                    ],
                },
                "source": "A §3.6.4 p.31",
            }
        ],
        pitfalls=[
            "$n(\\psi)$（加性特征标的导子指数）与 $n=\\dim\\pi$ 在 JPPS 公式里并排出现，容易把 $n\\,n(\\psi)$ 误读成向量；它是标量乘积。",
            "「$\\pi$ 深度 0 $\\iff$ $r_n(\\pi)$ 驯分歧」这一条里 $r_n$ 是 $\\ell$ 进表示（$\\rho$ 的半单化），不是 $\\rec_n(\\pi)$ 本身；对 $\\rec_n(\\pi)$ 说「驯分歧」需要先取 $\\WD^{-1}$。",
        ],
        related=[
            "yao17/concept/wd-invariants",
            "yao17/concept/llc-statement",
            "yao17/deriv/depth-zero-chain",
            "yao17/concept/satake",
        ],
        sources=[
            {
                "text": "A",
                "section": "§3.5–§3.6.4",
                "pages": [30, 31],
                "quote": "ϵ(π, s, ψ) = q^{−(c(π)+n·n(ψ))·s} · ϵ(π, 0, ψ)",
                "anchor": "A p.30",
            }
        ],
        provenance_note="深度 0 对照图五条取自 p.30 的 §3.5；JPPS 公式与「两种导子定义一致」见 p.30 §3.6.3；引理 3.8 与其证明见 p.31。§3.4/§3.5.1/§3.6 的正文在底本中空缺（只留标题），已在译本照实标注。",
        rights="rewritten",
        status="dev",
    )
