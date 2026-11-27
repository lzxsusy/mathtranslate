# -*- coding: utf-8 -*-
"""cards_b.py —— 轨 B：自守侧（6 张概念卡）。"""


def add(mk):
    mk(
        id="yao17/concept/smooth-admissible",
        type="concept",
        track="B",
        title="光滑表示、容许表示与反变对偶",
        aliases=["smooth", "admissible", "容许的", "contragradient"],
        summary="光滑指每个向量的稳定子开；容许再要求每个开子群的固定向量空间有限维。反变对偶 V∨ 取「稳定子开」的线性泛函。",
        question="为什么容许性要按「每个开子群 H 的 V^H 有限维」来定义，而不是按「V 有限维」？反变对偶在容许表示上为什么才行为良好？",
        definition={
            "text": "设 $G$ 是 $K$ 上的连通约化群，$G=G(K)$，$V$ 是 $\\mathbb C$-向量空间。(1) $\\pi$ 光滑，若每个 $v\\in V$ 的稳定子 $\\operatorname{Stab}(v)$ 在 $G$ 中开；(2) $\\pi$ 容许，若它光滑且对每个开子群 $H\\subset G$，$V^H$ 有限维。记 $\\Rep^\\infty_G$、$\\Rep^{\\mathrm{adm}}_G$ 为对应范畴。反变对偶：$V^\\vee=\\{\\psi\\in V^\\ast:\\operatorname{Stab}(\\psi)\\ \\text{开}\\}$，即 $\\pi^\\vee$（亦称 $\\tilde V$）。",
            "notation": "$\\pi(g)(\\psi)(v)=\\psi(\\pi(g)^{-1}v)$；$V^H$ 是 $H$-固定向量。",
        },
        key_points=[
            "光滑性的等价说法：$V=\\bigcup_K V^K$，$K$ 跑遍紧开子群；容许性再加「每个 $V^K$ 有限维」。这一步把无穷维表示拆成一族有限维 $K$-表示，是所有局部计算（$K$-型、迹、Hecke 模）的入口。",
            "对固定紧开子群 $C$，$V|_C$ 半单（每个向量落在有限维不可约 $C$-表示里），故 $V=\\bigoplus_{\\sigma\\in E(C)}V_\\sigma$；容许性等价于每个同型分量 $V_\\sigma$ 有限维，此时 $V|_C=\\bigoplus\\Sigma^{m_\\sigma}$ 且重数 $m_\\sigma$ 有限。",
            "反变对偶在一般光滑表示上 $V\\to V^{\\vee\\vee}$ 不是同构；底本 Remark 明确指出容许性正是为此而设：$\\pi$ 容许 $\\iff$ $\\pi^\\vee$ 容许 $\\iff$ $V\\xrightarrow{\\sim}V^{\\vee\\vee}$。",
            "Gelfand–Kazhdan：$G=\\GL_n(K)$、$\\pi$ 不可约光滑时，$\\pi^\\vee\\cong(g\\mapsto\\pi({}^tg^{-1}))$——这就是「反变」（contragradient）这个名字的来源。",
        ],
        formulas=[
            "$\\pi\\ \\text{光滑}\\iff V=\\bigcup_{K}V^K\\quad(K\\ \\text{紧开})$",
            "$\\pi\\ \\text{容许}\\iff V=\\bigoplus_{\\sigma\\in E(C)}V_\\sigma,\\quad \\dim V_\\sigma<\\infty\\ \\forall\\sigma$",
            "$V^\\vee=\\{\\psi\\in V^\\ast:\\operatorname{Stab}(\\psi)\\ \\text{开}\\},\\qquad V\\xrightarrow{\\ \\sim\\ }V^{\\vee\\vee}\\iff \\pi\\ \\text{容许}$",
        ],
        pitfalls=[
            "「容许」不是「有限维」：容许表示一般无穷维（如非分歧主序列），有限维只在不可约且光滑时由引理 2.6 逼出「一维」这一极端情形。",
            "$\\pi^\\vee$ 的不可约性需要另证（底本 Remark 称「$\\pi$ 不可约 $\\iff$ $\\pi^\\vee$ 不可约」），不能从容许性自动得到。",
        ],
        related=[
            "yao17/concept/hecke-modules",
            "yao17/concept/satake",
            "yao17/concept/parabolic-induction",
            "yao17/concept/harish-chandra-character",
        ],
        sources=[
            {
                "text": "A",
                "section": "§2.1.1",
                "pages": [10, 10],
                "quote": "π is admissible if it is smooth, and for every open subgroup H ⊂ G, V^H is finite dimensional",
                "anchor": "A p.10",
            }
        ],
        provenance_note="光滑/容许/反变对偶的定义与四条 Remark 取自 p.10 的 2.1.1；「容许性把表示拆成有限维 K-表示族」的解读是我们的判断。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/hecke-modules",
        type="concept",
        track="B",
        title="Hecke 代数 H(G)、双陪集子代数与 「光滑表示 ≃ 非退化 Hecke 模」",
        aliases=["Hecke algebra", "H(G//K)", "引理 2.1", "Casselman"],
        summary="H(G) 是紧支局部常值函数的卷积代数；引理 2.1 给出 Rep^∞_G ≃ 非退化 H(G)-模，引理 2.2 把容许性换到有限维 H(G//K)-模上。",
        question="H(G) 没有单位元，为什么还能有「非退化模 ≃ 光滑表示」的等价？Casselman 引理 2.2 又需要什么额外条件？",
        definition={
            "text": "取 Haar 测度使 $\\mu(K_0)=1$。(1) $H(G)=\\{f\\colon G\\to\\mathbb C\\ \\text{紧支局部常值}\\}$，卷积 $(f_1\\ast f_2)(h)=\\int_Gf_1(hg^{-1})f_2(g)dg$；(2) 对紧开子群 $K$，$H(G/\\!/K)$ 是左右 $K$-不变的子代数，有双边单位 $e_K=\\frac{1}{\\Vol(K)}\\mathbf 1_K$；(3) $H(G)$ 无单位，但 $H(G)=\\bigcup_K H(G/\\!/K)$，各 $H(G/\\!/K)$ 的单位 $e_K$ 不同。引理 2.1：$\\Rep^\\infty_G\\to\\{\\text{非退化 }H(G)\\text{-模}\\}$ 是范畴等价。",
            "notation": "$f\\star v=\\pi(f)v=\\int_Gf(g)\\pi(g)v\\,dg$；非退化指 $H(G)V=V$；$e_{gK}=\\frac{1}{\\mu(K)}\\mathbf 1_{gK}$。",
        },
        key_points=[
            "引理 2.1 的逆函子靠一件小事：对任一 $m$，总可取足够小的 $K$ 使 $e_K\\star m=m$，然后定义 $g\\cdot m:=e_{gK}\\star m$；良定义性用恒等式 $e_{gK'}\\ast e_K=e_{gK}$（$K'\\subset K$）。",
            "「作用律」是证明里唯一不平凡的地方：要证 $e_{g_1K'}\\ast e_{g_2K}=e_{g_1g_2K}$，其中取 $K'=g_2Kg_2^{-1}\\cap K$ 再缩小到稳定 $m'$；底本在 2.1.4 的注里给了更漂亮的说法：$H(G)\\otimes_{H(G)}M\\xrightarrow{\\sim}M$ 是同构，于是借左作用搬来 $G$-作用。",
            "引理 2.2（Casselman）：固定 $K$，$V\\mapsto V^K$ 给出「所有不可约子商都含 $K$-固定向量」的有限长容许表示与有限维 $H(G/\\!/K)$-模的等价；不可约 $V$ 且 $V^K\\neq 0$ 时 $V^K$ 是不可约 $H(G/\\!/K)$-模。",
            "推论 2.3：若 $V$ 不可约光滑且 $H(G/\\!/K)$ 交换，则 $V^K=0$ 或 $\\dim V^K=1$——这条在 $G=\\GL_n$、$K=\\GL_n(\\mathcal O_K)$ 时直接给出「非分歧表示」的整维性。",
        ],
        formulas=[
            "$(f_1\\ast f_2)(h)=\\int_Gf_1(hg^{-1})f_2(g)\\,dg=\\int_Gf_1(g)f_2(g^{-1}h)\\,dg$",
            "$e_{gK'}\\ast e_K=e_{gK}\\quad(K'\\subset K),\\qquad H(G)=\\bigcup_K H(G/\\!/K)$",
            "$\\Rep^\\infty_G\\ \\simeq\\ \\{\\text{非退化 }H(G)\\text{-模}\\},\\qquad \\Rep^{\\mathrm{adm}}_G|_K\\ \\simeq\\ H(G/\\!/K)\\text{-mod}^{\\mathrm{f.d.}}$",
        ],
        theorems=[
            {
                "name": "引理 2.1（光滑表示与 Hecke 模的等价）",
                "statement": "$\\Rep^\\infty_G\\to\\{H(G)\\text{ 的非退化模}\\}$，$V\\mapsto V$ 配 $f\\star v=\\pi(f)v$，是范畴等价。",
                "proof": {
                    "status": "sketch",
                    "gap_note": "底本给了全忠实性的断言与逆函子的完整构造思路，但「作用律」部分的细节以「有点 tricky」带过（p.13 末给出 $H(G)\\otimes M\\cong M$ 的替代论证）。",
                },
                "source": "A §2.1.4 p.12–p.13",
            },
            {
                "name": "引理 2.2（Casselman）",
                "statement": "固定紧开 $K$：$V\\mapsto V^K$ 从「有限长、所有不可约子商都有 $K$-固定向量」的容许表示等价到有限维 $H(G/\\!/K)$-模；并给出不可约光滑表示与不可约 $H(G/\\!/K)$-模的双射。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本只陈述（Casselman 的标准结果），未给证明。",
                },
                "source": "A §2.1.5 p.13",
            },
        ],
        pitfalls=[
            "$H(G)$ 无单位元，所以「模」必须是非退化的（$H(G)V=V$）；丢掉这条会得到没有对应表示的病态模。",
            "引理 2.2 的条件「所有不可约子商都有 $K$-固定向量」不能省：否则 $V\\mapsto V^K$ 会在含「无 $K$-固定向量」子商的表示上丢信息。",
        ],
        related=[
            "yao17/concept/smooth-admissible",
            "yao17/concept/satake",
            "yao17/concept/harish-chandra-character",
        ],
        sources=[
            {
                "text": "A",
                "section": "§2.1.2–§2.1.5",
                "pages": [11, 13],
                "quote": "There is a natural functor from Rep^∞_G → {non deg. H(G)-modules} which induces an equivalence of categories",
                "anchor": "A p.12",
            }
        ],
        provenance_note="定义与引理 2.1/2.2 取自 p.11–p.13；证明要点（$e_{gK'}\\ast e_K=e_{gK}$、$H(G)\\otimes M\\cong M$）照 p.12–p.13 的观察 (3) 与末段注。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/satake",
        type="concept",
        track="B",
        title="球面 Hecke 代数与 Satake 同构、非分歧表示",
        aliases=["spherical Hecke algebra", "Satake", "unramified", "Gelfand trick"],
        summary="H(G//C) 交换，且 ≅ C[t_1^{±1},…,t_n^{±1}]^{S_n}；故不可约容许 π 的 π^C 或为 0 或一维，「非分歧」即 π^C≠0。",
        question="为什么 H(G//C) 对 GL_n 是交换的？Satake 同构在这个具体情形下写成什么？「非分歧表示」由此得到什么结构？",
        definition={
            "text": "设 $G=\\GL_n(K)$，$C=\\GL_n(\\mathcal O_K)$ 是极大紧开子群，则 $H(G/\\!/C)\\xrightarrow{\\sim}\\mathbb C[t_1^{\\pm1},\\dots,t_n^{\\pm1}]^{S_n}$，特别地交换。更一般地，$G$ 分裂约化、$C$ 超特殊时，经典 Satake 同构为 $H(G/\\!/C)\\xrightarrow{\\sim}(\\mathcal O\\hat T)^W$，其中 $\\hat T=\\Spec\\mathbb C[\\Lambda]$，$\\Lambda$ 是余权格，$W$ 是 Weyl 群。由推论 2.3，不可约容许 $\\pi$ 的 $\\pi^C$ 或为 0 或一维；称 $\\pi$ 非分歧（unramified），若 $\\pi^C\\neq 0$。",
            "notation": "$t_i$ 是 $\\mathrm{diag}(\\varpi,\\dots,\\varpi,1,\\dots,1)$ 型双陪集的像；$\\Lambda$ 是余权格，$\\mathcal O\\hat T=\\mathbb C[\\Lambda]$。",
        },
        key_points=[
            "Gelfand 技巧给出 GL_n 情形的交换性：$C\\backslash G/C\\cong G\\backslash(G/C\\times G/C)$，而 $G/C$ 参数化 $K^n$ 中的格子，故双陪集 = 一对格子的相对位置；$(\\Lambda,\\Lambda')$ 与 $((\\Lambda')^\\vee,\\Lambda^\\vee)$ 相对位置相同，于是卷积可交换——底本说这证明「几乎同义反复」。",
            "Satake 同构的一般形式 $(\\mathcal O\\hat T)^W$ 说明球面 Hecke 代数是「余权环的 Weyl 不变量」，其极大谱是 $\\hat T/W$——这就是 Satake 参数（半单共轭类）的栖身处。",
            "非分歧表示的定义 $\\pi^C\\neq0$ 与「$\\pi$ 有一维 $C$-固定子空间」等价（推论 2.3），故非分歧表示必是某个未分歧主序列的不可约商；底本的原始定义只用到 $\\dim\\pi^C=1$ 这一点。",
            "对 GL_n，$H(G/\\!/C)$ 同构于对称多项式环，故 $\\pi$ 的非分歧性完全由「$\\pi^C$ 上的 $H(G/\\!/C)$-作用给出的 $n$ 个特征标 $t_i$」编码，这组 $t_i$ 就是 Satake 参数。",
        ],
        formulas=[
            "$H(G/\\!/C)\\xrightarrow{\\ \\sim\\ }\\mathbb C[t_1^{\\pm1},\\dots,t_n^{\\pm1}]^{S_n}$",
            "$H(G/\\!/C)\\xrightarrow{\\ \\sim\\ }(\\mathcal O\\hat T)^W,\\qquad \\hat T=\\Spec\\mathbb C[\\Lambda]$",
            "$C\\backslash G/C\\ \\cong\\ G\\backslash(K^n\\text{ 中的格子对}),\\qquad (\\varphi\\ast\\psi)(\\Lambda,\\Lambda')=\\sum_{\\Lambda''}\\varphi(\\Lambda,\\Lambda'')\\psi(\\Lambda'',\\Lambda')$",
        ],
        theorems=[
            {
                "name": "推论 2.3 + 推论-定义（非分歧表示）",
                "statement": "$V\\in\\Rep^\\infty_G$ 不可约且 $H(G/\\!/K)$ 交换 $\\Rightarrow$ $V^K=0$ 或 $\\dim V^K=1$；取 $K=C=\\GL_n(\\mathcal O_K)$ 时称 $V^C\\neq0$ 的 $\\pi$ 为非分歧。",
                "proof": {
                    "status": "complete",
                    "steps": [
                        {
                            "no": 1,
                            "text": "由引理 2.2(2)，不可约 $V$ 且 $V^K\\neq0$ 时 $V^K$ 是不可约 $H(G/\\!/K)$-模。",
                            "why": "Casselman 引理把 $K$-固定向量上的作用精确化为 $H(G/\\!/K)$-模结构，且不可约性传递。",
                        },
                        {
                            "no": 2,
                            "text": "若 $H(G/\\!/K)$ 交换，则其任一不可约模都是一维的（Schur 引理：交换代数的不可约模 = 其特征标）。",
                            "why": "允许用 Schur 引理，因为 $V^K$ 已是有限维 $H(G/\\!/K)$-模，不依赖定理 2.5。",
                        },
                    ],
                },
                "source": "A §2.1.6 p.14",
            }
        ],
        pitfalls=[
            "Satake 同构的交换性依赖 $C$ 是超特殊（hyperspecial）的；换成一般极大紧子群 $K$，$H(G/\\!/K)$ 未必交换，推论 2.3 也就用不上。",
            "非分歧是「存在非零 $C$-固定向量」，不是「$\\pi$ 本身非分歧扩张」；对应到 Galois 侧是 $\\rec_n(\\pi)$ 在 $I_K$ 上平凡（$N=0$ 且 $\\rho|_{I_K}=0$），两者不可混淆。",
        ],
        related=[
            "yao17/concept/hecke-modules",
            "yao17/concept/smooth-admissible",
            "yao17/concept/llc-statement",
        ],
        sources=[
            {
                "text": "A",
                "section": "§2.1.6",
                "pages": [14, 14],
                "quote": "H(G//C) ≅ C[t_1^{±1}, ..., t_n^{±1}]^{S_n}",
                "anchor": "A p.14",
            }
        ],
        provenance_note="Satake 同构、Gelfand 技巧与推论-定义照 p.14；「Satake 参数 = 双陪集代数的特征标 $t_i$」的解释是我们的判断（底本未在 §2.1 展开 Satake 参数）。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/harish-chandra-character",
        type="concept",
        track="B",
        title="定理 2.5（光滑不可约 ⇒ 容许）、引理 2.6 与 Harish-Chandra 特征标",
        aliases=["定理 2.5", "定理 2.8", "distribution character", "椭圆表示"],
        summary="光滑不可约必容许；GL_n 的光滑不可约表示或一维或无穷维，一维者必为 χ∘det；Θ_π(f)=Tr π(f) 由正则半单处的局部常值函数 χ_π 表示。",
        question="「光滑 + 不可约 ⇒ 容许」这条定理为什么只能用 Jacquet 函子证？Harish-Chandra 特征标 χ_π 在什么集合上局部常值，椭圆表示又怎么定义？",
        definition={
            "text": "定理 2.5：$G$ 的光滑不可约表示必容许（证明用 Jacquet 函子把 $\\pi$ 嵌入容许（超尖点）表示的抛物诱导，底本略）。引理 2.6：$G=\\GL_n(K)$ 的光滑不可约表示或一维或无穷维；一维者必形如 $\\chi\\circ\\det$。引理 2.7：两两不同构的不可约容许表示的特征标 $\\Theta_{\\pi_i}$ 线性无关。定理 2.8（Harish-Chandra；正特征时属 Lemaire）：存在局部可积函数 $\\chi_\\pi$，在正则半单集 $G^{\\mathrm{r.s.}}$ 上局部常值、在补集上为 0，使 $\\Theta_\\pi(f)=\\int_Gf(g)\\chi_\\pi(g)dg$。定义：$\\pi$ 椭圆，若 $\\chi_\\pi$ 在正则椭圆集 $G^{\\mathrm{r.e.}}$ 上不恒为 0。",
            "notation": "$\\Theta_\\pi\\colon H(G)\\to\\mathbb C$，$f\\mapsto\\Tr\\pi(f)$；$g$ 正则半单指特征多项式 $P_g$ 在 $K$ 上可分；正则椭圆指 $P_g$ 不可约。每本质平方可积表示都是椭圆的。",
        },
        key_points=[
            "定理 2.5 的证明被底本整段略去，理由很实在：它需要 Jacquet 函子 + 超尖点表示的存在性（§2.2），而这两样在 §2.1 还没讲；底本还特意在脚注里提醒「不能反过来用定理 2.5 去证 Schur 引理，因为定理 2.5 的证明本身用 Schur 引理」。",
            "引理 2.6 的论证只用了 $G$ 的结构：$\\ker\\pi$ 开，含 $1+\\varpi^m\\GL_n(\\mathcal O_K)$，共轭后含上三角幂幺群 $U$，正规性给出 $\\SL_n(K)\\subset\\ker\\pi$，故 $\\pi$ 过 $\\det$。",
            "引理 2.7（特征标线性无关）是 Harish-Chandra 特征标理论的基本引理，配合定理 2.8 就把「表示」变成「正则半单集上的函数」，这是 Jacquet–Langlands 与迹公式的出发点。",
            "椭圆表示的定义刻意用「$\\chi_\\pi$ 在 $G^{\\mathrm{r.e.}}$ 上不恒为 0」而不是「矩阵系数紧支」，因为后者只在超尖点时成立（引理 2.11）；椭圆是比超尖点更宽、比一般更窄的类。",
        ],
        formulas=[
            "$\\Theta_\\pi(f)=\\Tr\\pi(f)=\\int_Gf(g)\\chi_\\pi(g)\\,dg,\\qquad \\chi_\\pi\\ \\text{在}\\ G^{\\mathrm{r.s.}}\\ \\text{上局部常值}$",
            "$\\pi\\ \\text{光滑不可约}\\ \\Longrightarrow\\ \\pi\\ \\text{容许}$",
            "$\\pi\\ \\text{一维}\\ \\Longleftrightarrow\\ \\pi\\cong\\chi\\circ\\det$",
        ],
        theorems=[
            {
                "name": "定理 2.5（光滑不可约表示容许）",
                "statement": "$G$ 的任一光滑不可约表示都是容许的。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本整段略去，只说证明用 Jacquet 函子把 $\\pi$ 嵌入容许（超尖点）表示的抛物诱导，并引 Jacquet 的处理或 Bernstein–Zelevinsky。",
                },
                "source": "A §2.1.8 p.15",
            },
            {
                "name": "定理 2.8（Harish-Chandra 特征标）",
                "statement": "存在局部可积的 $\\chi_\\pi$，在 $G^{\\mathrm{r.s.}}$ 上局部常值、补集为 0，且 $\\Theta_\\pi(f)=\\int_Gf\\chi_\\pi$。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本只陈述（称 $K$ 特征 0 时属 Harish-Chandra、正特征属 Lemaire），未给证明；前一段只给了 $\\Theta_\\pi$ 的显式计算式。",
                },
                "source": "A §2.1.9 p.16",
            },
        ],
        pitfalls=[
            "定理 2.8 里的 $\\chi_\\pi$ 只在正则半单集上局部常值，在奇异元素上可以爆掉；把它当成 $G$ 上的连续函数会出错。",
            "「椭圆」不等于「超尖点」：超尖点 $\\Rightarrow$ 椭圆，反之不成立；底本只说「每本质平方可积表示是椭圆的」。",
        ],
        related=[
            "yao17/concept/smooth-admissible",
            "yao17/concept/hecke-modules",
            "yao17/concept/jacquet-supercuspidal",
        ],
        sources=[
            {
                "text": "A",
                "section": "§2.1.8–§2.1.9",
                "pages": [15, 16],
                "quote": "There is a locally integrable function χ_π on G, which is locally constant on the regular semi-simple set G^{r.s.} and 0 on the complement",
                "anchor": "A p.16",
            }
        ],
        provenance_note="定理 2.5、引理 2.6/2.7、定理 2.8 与椭圆定义照 p.15–p.16；「椭圆比超尖点宽」一句依据 p.16 的 Remark (2)。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/parabolic-induction",
        type="concept",
        track="B",
        title="抛物诱导、Jacquet 函子与模特征标 δ 的正规化",
        aliases=["parabolic induction", "Jacquet functor", "δ", "Ind/ind/Res"],
        summary="朴素 J~ 与 I~ 由 ψ_! 与 ind∘ψ* 给出且伴随；乘上模特征标 δ^{±1/2} 得到正规化的 J、I，保证幺正性不被破坏。",
        question="为什么朴素抛物诱导与朴素 Jacquet 函子必须乘 δ^{1/2} 才叫「正规化」？δ 在 GL_2 的 Borel 上具体等于什么？",
        definition={
            "text": "对 $H<G$ 与 $\\psi\\colon G\\to M=G/N$：$\\Ind_H^G(W)=\\{f\\colon G\\to W\\ \\text{一致局部常值},\\ f(hx)=hf(x)\\}$，$\\ind$ 是其中「模 $H$ 紧支」的子函子；$\\Res$ 是限制；$\\psi_!V=V/[N-1]V$ 是 $N$-余不变量，配 $\\psi_!\\dashv\\psi^\\ast$，且 $\\Res\\dashv\\Ind$、$\\ind\\dashv\\Res$（引理 2.9）。朴素抛物诱导与 Jacquet：$\\tilde I_P^G:=\\ind_P^G\\circ\\phi^\\ast$，$\\tilde J_P^G:=\\phi_!\\circ\\Res_P^G$。正规化：$J_P^G:=\\delta^{-1/2}\\tilde J_P^G$，$I_P^G:=\\tilde I_P^G\\cdot\\delta^{1/2}$，其中 $\\delta$ 是 $P$ 的模特征标，$(L_x)^\\ast\\mu^r_P=\\delta(x)\\mu^r_P$。",
            "notation": "$P=P_{\\underline n}$ 是标准抛物，$\\underline n=(n_1,\\dots,n_r)$ 是 $n$ 的有序分拆；$U_{\\underline n}$ 是幂幺根、$L_{\\underline n}$ 是 Levi；$I_P^G(W)=\\{f:\\ f(uhg)=\\delta^{1/2}_n(h)\\pi_L(h)f(g)\\}$。",
        },
        key_points=[
            "两条伴随是全部结构的骨架：$\\Res\\dashv\\Ind$（Frobenius 互反，Cartier 称「对偶 Frobenius 互反」）与 $\\psi_!\\dashv\\psi^\\ast$，合起来得 $\\tilde J\\dashv\\tilde I$；证明只用 Hom 的自然同构 $\\Hom_L(\\tilde J\\sigma_G,\\sigma_L)\\cong\\Hom_G(\\sigma_G,\\tilde I\\sigma_L)$。",
            "δ 的定义来自「右 Haar 测度在左平移下怎么变」：对 $\\GL_2$ 的标准 Borel，$d\\mu^l=\\frac{1}{|x|^2|z|}dx\\,dy\\,dz$、$d\\mu^r=\\frac{1}{|x||z|^2}dx\\,dy\\,dz$，算得 $\\delta\\begin{pmatrix}a&b\\\\&d\\end{pmatrix}=|a\\cdot d^{-1}|$。",
            "一般地 $\\delta_n(x)=|\\det(\\ad_{U_{\\underline n}}(x))|$（$x\\in L_{\\underline n}$）：模特征标就是 Levi 在幂幺根上的行列式，这一步把 δ 变成可计算的对象。",
            "正规化的意义：朴素 $\\tilde J$、$\\tilde I$ 不把幺正表示送到幺正表示，因为抛物子群一般非幺模；乘 $\\delta^{\\pm1/2}$ 后 $I$ 保留幺正性，这是「正规化」三个字的全部内容。",
            "注记（2.2.4 末）：若 $\\pi_1,\\dots,\\pi_r$ 不可约超尖点、$\\pi_1\\times\\dots\\times\\pi_r:=I_{P_{\\underline n}}(\\pi_L)$，则它不可约当且仅当任两 $\\pi_i\\neq|\\det|\\cdot\\pi_j$；$\\GL_2$ 情形即 $\\chi_1/\\chi_2\\neq|\\cdot|^{\\pm1}$。",
        ],
        formulas=[
            "$\\tilde I_P^G=\\ind_P^G\\circ\\phi^\\ast,\\qquad \\tilde J_P^G=\\phi_!\\circ\\Res_P^G,\\qquad \\tilde J\\dashv\\tilde I$",
            "$J_P^G=\\delta^{-1/2}\\tilde J_P^G,\\qquad I_P^G=\\tilde I_P^G\\cdot\\delta^{1/2}$",
            "$\\delta_{\\underline n}(x)=|\\det(\\ad_{U_{\\underline n}}(x))|,\\qquad \\delta\\begin{pmatrix}a&b\\\\&d\\end{pmatrix}=|a\\,d^{-1}|\\ (n=2)$",
        ],
        theorems=[
            {
                "name": "引理 2.9（两条伴随）",
                "statement": "$\\Res\\dashv\\Ind$；若 $H<G$ 开，则 $\\ind\\dashv\\Res$；对 $\\psi\\colon G\\to M=G/N$ 有 $\\psi_!\\dashv\\psi^\\ast$。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本只陈述，并提到与 $f_!,f^\\ast,f_\\ast$ 的类比（引 Ngo 的笔记）；伴随的具体构造未写。",
                },
                "source": "A §2.2.1 p.17",
            }
        ],
        pitfalls=[
            "δ 只依赖 $P$（以及 Levi 的选取），但 $\\delta^{1/2}$ 需要取平方根：底本在复系数下取 $\\delta^{1/2}=|\\det|^{1/2}$ 型实值函数，换成一般系数域时这条要小心。",
            "朴素 $\\tilde I$ 与正规化 $I$ 只差一个特征标扭转，所以「$\\pi_1\\times\\dots\\times\\pi_r$」的记号在不同文献里可能指 $\\tilde I$ 也可能指 $I$；底本明确用正规化的 $I$。",
        ],
        related=[
            "yao17/concept/jacquet-supercuspidal",
            "yao17/concept/zelevinsky-segment",
            "yao17/concept/smooth-admissible",
        ],
        sources=[
            {
                "text": "A",
                "section": "§2.2.1–§2.2.3",
                "pages": [16, 19],
                "quote": "J^G_P := δ^{-1/2} · J̃^G_P,  I^G_P := Ĩ^G_P · δ^{1/2}",
                "anchor": "A p.19",
            }
        ],
        provenance_note="Ind/ind/Res 与 $\\psi_!$、朴素 $\\tilde I/\\tilde J$、δ 的 $\\GL_2$ 计算与正规化定义取自 p.16–p.19；「正规化的意义」一段是我们的解释，底本只一句「不保持幺正性」。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/jacquet-supercuspidal",
        type="concept",
        track="B",
        title="超尖点表示：J_P(π)=0 与矩阵系数的紧支性",
        aliases=["supercuspidal", "超尖点", "引理 2.10", "引理 2.11"],
        summary="π 超尖点指对所有真抛物 P 有 J_P(π)=0；等价地所有矩阵系数在 G⁰ 上紧支（模中心紧支）。它们是容许表示的积木。",
        question="为什么「所有真抛物上的 Jacquet 函子为零」能刻画超尖点？它与「矩阵系数紧支」的等价是怎么来的？",
        definition={
            "text": "设 $(\\pi,V)\\in\\Rep^{\\mathrm{adm}}_G$ 不可约。$\\pi$ 称超尖点（supercuspidal），若对任一真抛物 $P<G$ 有 $J_P^G(\\pi)=0$。引理 2.10：任一不可约 $\\pi$ 或超尖点，或是某个 $I_P^G(\\sigma)$ 的子表示，$P$ 真抛物、$\\sigma$ 为 $L$ 的不可约超尖点表示。引理 2.11：$\\pi$ 不可约容许，则 TFAE：(1) $\\pi$ 超尖点；(2) 每个矩阵系数 $C_{v,\\lambda}(g)=\\lambda(\\pi(g)v)$ 在 $G^0=\\{g:\\det g\\in\\mathcal O_K^\\times\\}$ 上紧支；(3) 每个矩阵系数模中心 $Z$ 紧支。若 $\\pi^\\vee$ 也不可约，还可加 (4) 存在一个模中心紧支的矩阵系数。",
            "notation": "$G^0=\\{g\\in\\GL_n(K):\\det g\\in\\mathcal O_K^\\times\\}$，$ZG^0$ 在 $G$ 中有限指数（$\\GL_n$ 时为 $n$）；引理 2.12：对紧开 $K_0$，带 $K_0$-固定向量的不可约超尖点表示只有有限多个同构类。",
        },
        key_points=[
            "引理 2.10 的证明就是一个伴随：$\\pi$ 非超尖点 $\\Rightarrow$ 存在极小抛物 $P$ 使 $J_P\\pi\\neq0$；取不可约商 $\\sigma$，则 $0\\neq\\Hom_L(J_P\\pi,\\sigma)=\\Hom_G(\\pi,I_P\\sigma)$，即 $\\pi\\hookrightarrow I_P\\sigma$，且可证 $\\sigma$ 超尖点。",
            "于是「超尖点」= 不为任何真抛物诱导的子表示，这正是「积木」的意思：所有不可约表示都由超尖点经诱导（以及取子商）搭出来（§3 的 BZ 分类把这个直觉变成定理）。",
            "矩阵系数刻画（引理 2.11）把「超尖点」变成可检验的分析条件：$\\pi$ 超尖点 $\\iff$ 其矩阵系数模中心紧支。底本脚注说这「也许就是超尖点性最初的定义」。",
            "引理 2.12（带 $K_0$-固定向量的超尖点表示只有有限多个）是把超尖点侧「局部有限」的关鍵：它保证了 §3.3 的 BZ 参数化在每一层都是有限集。",
        ],
        formulas=[
            "$\\pi\\ \\text{超尖点}\\iff J_P^G(\\pi)=0\\ \\ \\forall P\\lneq G$",
            "$0\\neq\\Hom_L(J_P\\pi,\\sigma)=\\Hom_G(\\pi,I_P\\sigma)\\quad\\Longrightarrow\\quad \\pi\\hookrightarrow I_P^G\\sigma$",
            "$\\pi\\ \\text{超尖点}\\iff C_{v,\\lambda}\\ \\text{在}\\ G^0\\ \\text{上紧支}\\iff C_{v,\\lambda}\\ \\text{模}\\ Z\\ \\text{紧支}$",
        ],
        theorems=[
            {
                "name": "引理 2.10（不可约表示或超尖点或嵌入抛物诱导）",
                "statement": "不可约 $\\pi$ 或超尖点，或是某真抛物 $P$ 上某不可约超尖点 $\\sigma$ 的 $I_P^G(\\sigma)$ 的子表示。",
                "proof": {
                    "status": "complete",
                    "steps": [
                        {
                            "no": 1,
                            "text": "若 $\\pi$ 非超尖点，取极小抛物 $P$ 使 $J_P\\pi\\neq0$；$J_P\\pi$ 有限长，取不可约商 $\\sigma$。",
                            "why": "非超尖点的定义保证这样的 $P$ 存在；$J_P$ 保有限长（§2.2.2 Remark (3)）。",
                        },
                        {
                            "no": 2,
                            "text": "由伴随 $\\tilde J\\dashv\\tilde I$ 得 $0\\neq\\Hom_L(J_P\\pi,\\sigma)=\\Hom_G(\\pi,I_P\\sigma)$，故 $\\pi$ 嵌入 $I_P\\sigma$。",
                            "why": "同构的左边非零推出右边非零，而不为零的 $G$-同态在不可约 $\\pi$ 上必单。",
                        },
                        {
                            "no": 3,
                            "text": "由 $P$ 极小可证 $\\sigma$ 超尖点。",
                            "why": "底本只写「由构造可证」（By construction one can show），未展开；这是本引理唯一的缺口。",
                        },
                    ],
                },
                "source": "A §2.2.4 p.19–p.20",
            }
        ],
        pitfalls=[
            "定义里要求「所有真抛物」，而引理 2.11 的紧支性是在 $G^0$（或模中心）上；这两个条件等价需要 $ZG^0$ 有限指数这一结构事实，不能逐字推广到任意约化群。",
            "引理 2.11 的第 (4) 条（存在一个模中心紧支的矩阵系数）额外要求 $\\pi^\\vee$ 不可约，底本明确标了这个条件，不能省。",
        ],
        related=[
            "yao17/concept/parabolic-induction",
            "yao17/concept/harish-chandra-character",
            "yao17/deriv/supercuspidal-criterion",
            "yao17/concept/supercuspidal-support",
        ],
        sources=[
            {
                "text": "A",
                "section": "§2.2.4",
                "pages": [19, 20],
                "quote": "(π, V) is called supercuspidal if for any proper parabolic P < G, J^G_P(π) = 0",
                "anchor": "A p.19",
            }
        ],
        provenance_note="超尖点定义、引理 2.10 的证明、引理 2.11 的 (1)–(4)、引理 2.12 与 2.2.4 末的注记取自 p.19–p.20；「积木」的解读依据同一页的 Supercuspidal representations form building blocks。",
        rights="rewritten",
        status="dev",
    )
