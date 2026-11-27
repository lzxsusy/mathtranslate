# -*- coding: utf-8 -*-
"""cards_d.py —— 轨 D：惯性 Langlands 与类型（3 张概念卡）。"""


def add(mk):
    mk(
        id="yao17/concept/bernstein-decomposition",
        type="concept",
        track="D",
        title="Bernstein 分量、惯性等价与定理 4.2 的直积分解",
        aliases=["Bernstein component", "Bernstein center", "定理 4.2"],
        summary="Rep^∞_n 直积分解为各 Bernstein 分量 R(L,ς)；分量相等 ⇔ 惯性等价，Bernstein 中心就是 (L,ς) 的惯性等价类。",
        question="Bernstein 分量按什么划分？为什么它的定义既要用超尖点 ς 又要允许非分歧扭转 η？",
        definition={
            "text": "设 $L\\subset\\GL_n(K)$ 是 Levi，$P$ 是以为 $L$ 为 Levi 因子的抛物，$\\varsigma$ 是 $L$ 的不可约超尖点表示。Bernstein 分量 $R(L,\\varsigma)=R(L,\\varsigma)(\\GL_n(K))\\subset\\Rep^\\infty_n$ 是由所有「其每个不可约子商都是某个 $I_L^{\\GL_n}(\\varsigma\\otimes\\eta)$ 的子商」的 $\\pi$ 构成的全子范畴，$\\eta$ 跑遍 $L$ 的非分歧特征标，$I_L^{\\GL_n}:=\\Ind_P^{\\GL_n(K)}\\circ j^\\ast$ 是正规化抛物诱导。引理 4.1：$R(L_1,\\varsigma_1)=R(L_2,\\varsigma_2)$ $\\iff$ 二者惯性等价：存在 $L_2$ 的非分歧特征标 $\\eta$ 与 $g\\in\\GL_n(K)$ 使 $gL_1g^{-1}=L_2$、$g\\varsigma_1=\\varsigma_2\\eta$。定义 Bernstein 中心 $\\mathcal B=\\mathcal B(\\GL_n(K)):=\\{(L,\\varsigma)\\}/\\text{惯性等价}$。定理 4.2：$\\Rep^\\infty_n=\\prod_{(L,\\varsigma)\\in\\mathcal B}R(L,\\varsigma)$。",
            "notation": "$j\\colon P\\to L$ 是到 Levi 商的映射；$\\varsigma\\otimes\\eta$ 通过 $j^\\ast$ 拉回成 $P$ 的表示；底本注：判断 $\\pi$ 落在哪个分量，只需看它的超尖点支撑。",
        },
        key_points=[
            "分量的定义用「$\\varsigma\\otimes\\eta$（$\\eta$ 非分歧）诱导出的所有子商」，而不是「$\\varsigma$ 本身」：这一步把「同一个超尖点表示沿 $|\\det|$ 的整数次幂」全部并进一个分量，否则 $\\varsigma$ 与 $\\varsigma(1)$ 会落在不同分量里。",
            "引理 4.1 的两个条件缺一不可：只要求 $gL_1g^{-1}=L_2$ 会漏掉 $\\varsigma$ 的非分歧扭转，只要求 $\\varsigma$ 相等会漏掉共轭。惯性等价正是这两个作用的商。",
            "定理 4.2 是「直积」而非「直和」：每个分量 $R(L,\\varsigma)$ 里可以有任意长的诱导表示，但不同分量之间没有非零同态——这是 Bernstein 分解最有力的地方。",
            "$\\GL_2$ 的三类分量（底本例）恰好对上超尖点支撑的三种形状：$\\{\\pi\\}$（超尖点自己）、$\\{\\chi,\\chi\\}$（$\\St_2(\\chi)$ 型）、$\\{\\chi_1,\\chi_2\\}$（$\\chi_1\\chi_2^{-1}$ 分歧的主序列）。",
        ],
        formulas=[
            "$R(L,\\varsigma)=\\big\\{\\pi:\\ \\text{每个不可约子商都是 }I_L^{\\GL_n}(\\varsigma\\otimes\\eta)\\ \\text{的子商},\\ \\eta\\ \\text{非分歧}\\big\\}$",
            "$R(L_1,\\varsigma_1)=R(L_2,\\varsigma_2)\\iff \\exists\\eta,\\ g:\\ gL_1g^{-1}=L_2,\\ g\\varsigma_1=\\varsigma_2\\eta$",
            "$\\Rep^\\infty_n=\\prod_{(L,\\varsigma)\\in\\mathcal B}R(L,\\varsigma)$",
        ],
        theorems=[
            {
                "name": "定理 4.2（Bernstein 分解）",
                "statement": "光滑表示范畴按 Bernstein 中心直积分解：$\\Rep^\\infty_n=\\prod_{(L,\\varsigma)\\in\\mathcal B}R(L,\\varsigma)$。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本只陈述（§4.1.4 的「Proof of the Bernstein decomposition」只有标题、正文空缺），引理 4.1 亦只陈述。",
                },
                "source": "A §4.1.1 p.32",
            }
        ],
        pitfalls=[
            "「$R(L,\\varsigma)$ 里的不可约表示都是 $I_L(\\varsigma\\otimes\\eta)$ 的子商」不是「都是它的商」：既有子也有商，故 $Q$ 侧与 $Z$ 侧的表示可以同分量。",
            "Bernstein 中心是集合 $\\mathcal B$，不是环；名字里的「中心」来自它与 Bernstein 中心的代数对象（$\\mathcal Z$）的对应，底本未展开。",
        ],
        related=[
            "yao17/concept/inertial-correspondence",
            "yao17/concept/supercuspidal-support",
            "yao17/concept/bz-classification",
        ],
        sources=[
            {
                "text": "A",
                "section": "§4.1.1–§4.1.2",
                "pages": [32, 33],
                "quote": "The category Rep^∞_n of smooth representations of GL_n(K) decomposes as a direct product",
                "anchor": "A p.32",
            }
        ],
        provenance_note="分量定义、引理 4.1、Bernstein 中心与定理 4.2 取自 p.32；$\\GL_2$ 三类分量与支撑对应取自 p.32–p.33；「直积而非直和」的解读是我们的判断。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/inertial-correspondence",
        type="concept",
        track="D",
        title="惯性对应：Bernstein 中心 ↔ Weil–Deligne 惯性类型（引理 4.3–4.5）",
        aliases=["inertia correspondence", "引理 4.4", "引理 4.5", "Galois inertia type"],
        summary="π 与 π′ 同 Bernstein 分量 ⇔ rec(π)|I_K ≅ rec(π′)|I_K；generic 时更强：同一 Galois 惯性类型 ⇒ π|K ≅ π′|K。",
        question="为什么 Bernstein 中心能被 Weil–Deligne 惯性类型索引？引理 4.5 里 generic 这个条件为什么删不掉？",
        definition={
            "text": "引理 4.3：$H\\triangleleft G$、$G/H$ 交换，$\\rho_1,\\rho_2$ 不可约有限维且 $\\rho_1|_H\\cong\\rho_2|_H$，则存在特征标 $\\psi\\colon G/H\\to\\mathbb C^\\times$ 使 $\\rho_2\\cong\\rho_1\\otimes\\psi$；注：只需 $\\Hom_H(\\rho_1,\\rho_2)\\neq0$。引理 4.4：$\\pi,\\pi'$ 在同一个 Bernstein 分量 $R(L,\\sigma)(G)$ 中 $\\iff$ 其 LLC 像的底层 $W_K$ 表示满足 $\\rec_n(\\pi)|_{I_K}\\cong\\rec_n(\\pi')|_{I_K}$——即 Bernstein 中心 $\\mathcal B(\\GL_n)$ 由 Weil–Deligne 惯性类型索引。引理 4.5：$\\pi,\\pi'$ 一般不可约且 $r_n(\\pi)|_{I_K}\\cong r_n(\\pi')|_{I_K}$（$r_n=\\WD^{-1}\\circ\\rec_n$），则 $\\pi|_K\\cong\\pi'|_K$。",
            "notation": "$K$ 在此指 $\\GL_n(\\mathcal O_K)$（底本用同一字母，译本改用 $\\mathcal K$ 区分）；$\\WD$ 是推论 1.7 的函子；引理 4.5 的证明用 Iwasawa 分解与 Mackey 分解 $ (\\Ind_P^{\\GL_n(K)}\\sigma)|_K=\\Ind_{P\\cap K}^{K}(\\sigma|_{P\\cap K})$。",
        },
        key_points=[
            "引理 4.4 的证明把 BZ 分类代进去：$\\pi=Q(\\Delta_1,\\dots,\\Delta_r)$ 给出 $L=\\prod\\GL_{n_i}(K)^{m_i}$、$\\sigma=\\bigotimes_{i,j}\\pi_i|\\cdot|^j$，而 $\\rec_n(\\pi)=\\bigoplus\\Sp_{m_i}(\\rec_{n_i}(\\pi_i))$，限制到 $I_K$ 得 $\\bigoplus\\rec_{n_i}(\\pi_i)^{m_i}|_{I_K}$——于是只剩超尖点情形，而那正由引理 4.3（取 $H=I_K$、$G=W_K$、$G/H\\cong\\mathbb Z$ 交换）给出。",
            "引理 4.3 的注（只需 $\\Hom_H(\\rho_1,\\rho_2)\\neq0$）在这里是关键：$\\bigoplus\\rec_{n_i}(\\pi_i)^{m_i}$ 与另一侧同构是「和」层面的，要逐个分量分离就得反复用这条注，底本在证明末尾明确点了这一步。",
            "引理 4.5 用 Iwasawa 与 Mackey 把「$\\pi|_K$」化成「$P\\cap K$ 上的诱导」，再比较 $\\Sp_{m_i}$ 的类型；它说的比 4.4 强：不只同分量，而是限制到 $K$ 后完全同构。",
            "generic 条件不能删（底本 Remark）：$\\GL_2$ 中 $\\mathrm{triv}$ 与 $\\St_2$ 同属一个 Bernstein 分量（都来自 $\\{\\chi,\\chi\\}$ 型支撑），但 $\\mathrm{triv}|_K$ 与 $\\St_2|_K$ 不同构——非 generic 的那些表示在 $K$ 上的型会把它们区分开。",
        ],
        formulas=[
            "$\\rho_1|_H\\cong\\rho_2|_H,\\ G/H\\ \\text{交换}\\ \\Longrightarrow\\ \\rho_2\\cong\\rho_1\\otimes\\psi$",
            "$\\pi,\\pi'\\ \\text{同 Bernstein 分量}\\iff \\rec_n(\\pi)|_{I_K}\\cong\\rec_n(\\pi')|_{I_K}$",
            "$\\pi,\\pi'\\ \\text{generic},\\ r_n(\\pi)|_{I_K}\\cong r_n(\\pi')|_{I_K}\\ \\Longrightarrow\\ \\pi|_K\\cong\\pi'|_K$",
            "$(\\Ind_P^{\\GL_n(K)}\\sigma)|_K=\\Ind_{P\\cap K}^{K}(\\sigma|_{P\\cap K})$",
        ],
        theorems=[
            {
                "name": "引理 4.4（Bernstein 分量 ↔ WD 惯性类型）",
                "statement": "$\\pi,\\pi'$ 同 Bernstein 分量 $\\iff$ $\\rec_n(\\pi)|_{I_K}\\cong\\rec_n(\\pi')|_{I_K}$。",
                "proof": {
                    "status": "sketch",
                    "gap_note": "底本给了完整思路（BZ 分类 + 归纳到超尖点 + 引理 4.3 及其注），但最后一步「反复用注逐个分离分量」只作断言。",
                },
                "source": "A §4.2.1 p.33–p.34",
            },
            {
                "name": "引理 4.5（generic 时 Galois 惯性类型决定 K-限制）",
                "statement": "一般的 $\\pi,\\pi'$ 若 $r_n(\\pi)|_{I_K}\\cong r_n(\\pi')|_{I_K}$，则 $\\pi|_K\\cong\\pi'|_K$。",
                "proof": {
                    "status": "complete",
                    "steps": [
                        {
                            "no": 1,
                            "text": "用 Iwasawa $\\GL_n(K)=B\\cdot\\GL_n(\\mathcal O_K)$ 与 Mackey，把 $\\Ind_P^{\\GL_n(K)}$ 限制到 $K$ 化成 $\\Ind_{P\\cap K}^{K}$。",
                            "why": "这一步把 $G$ 上的诱导换成紧子群上的诱导，使泛性（generic ⇒ $\\pi=Q(\\Delta_1)\\times\\dots$）可以直接逐项比较。",
                        },
                        {
                            "no": 2,
                            "text": "由定理 3.6，generic 给出 $\\pi=Q(\\Delta_1)\\times\\dots\\times Q(\\Delta_r)$，故 $\\rec_n(\\pi)=\\bigoplus\\rec_{n_i m_i}(Q(\\Delta_i))$。",
                            "why": "generic 保证 $\\pi$ 是诱导的（无 linked），从而 $\\rec_n$ 按块分解。",
                        },
                        {
                            "no": 3,
                            "text": "由引理 1.9，两侧 Galois 惯性类型相同 $\\iff$ 块数、块长 $m_i$ 与 $\\rho_i|_{I_K}$ 逐项相同。",
                            "why": "引理 1.9 正是「惯性类型相同」的判据。",
                        },
                        {
                            "no": 4,
                            "text": "归到 $\\pi=Q(\\Delta(\\lambda,m))$、$\\pi'=Q(\\Delta(\\lambda',m))$，$\\lambda'=\\lambda\\otimes\\eta$（$\\eta=\\chi\\circ\\det$ 非分歧），故 $\\rec_n(\\pi')=\\rec_n(\\pi)\\otimes\\rec_1(\\chi)$，即 $\\pi'=\\pi\\chi$。",
                            "why": "非分歧扭转在 $K$ 上平凡，故 $\\pi|_K\\cong\\pi'|_K$ 成立。",
                        },
                    ],
                },
                "source": "A §4.2.2 p.34–p.35",
            },
        ],
        pitfalls=[
            "引理 4.5 的结论是 $\\pi|_K\\cong\\pi'|_K$（限制到 $\\GL_n(\\mathcal O_K)$ 同构），不是 $\\pi\\cong\\pi'$；非分歧扭转在 $K$ 上不可见，这正是差别所在。",
            "引理 4.4 用的是 $\\rec_n(\\pi)|_{I_K}$（Weil–Deligne 表示的底层 $W_K$ 表示限制到 $I_K$），引理 4.5 用的是 $r_n(\\pi)|_{I_K}$（$\\ell$ 进表示）；两者经 $\\WD$ 对应，但记号不能混。",
        ],
        related=[
            "yao17/concept/bernstein-decomposition",
            "yao17/concept/wd-functor",
            "yao17/concept/generic-whittaker",
            "yao17/deriv/inertia-from-bernstein",
        ],
        sources=[
            {
                "text": "A",
                "section": "§4.2.1–§4.2.2",
                "pages": [33, 35],
                "quote": "Two irreducible admissible representations π and π′ of G belong to the same Bernstein component R(L,σ)(G) if and only if the underlying W_K representations satisfy rec_n(π)|_{I_K} ≅ rec_n(π′)|_{I_K}",
                "anchor": "A p.33",
            }
        ],
        provenance_note="引理 4.3 及其注、引理 4.4 的证明、引理 4.5 与 generic 反例取自 p.33–p.35；引理 4.5 的四步拆解是我们的整理，底本证明较简。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/type-and-k-type",
        type="concept",
        track="D",
        title="类型（type）、K-型与极小 K-型；Bushnell–Kutzko 型的区别",
        aliases=["type", "K-type", "minimal K-type", "Bushnell-Kutzko"],
        summary="σ 是 (L,ς) 的类型，若「π|_K 含 σ ⇔ π∈R(L,ς)」；只要求单向的是 K-型，π 上维数最小者为极小 K-型。",
        question="类型与 K-型的差别只在一个「当且仅当」上，为什么这个差别是本质的？Bushnell–Kutzko 型又放宽了什么？",
        definition={
            "text": "设 $\\sigma$ 是 $K$ 的光滑不可约表示，$s=(L,\\varsigma)\\in\\mathcal B(\\GL_n)$。(1) $\\sigma$ 是 $(L,\\varsigma)$ 的类型（type），若对所有光滑不可约 $\\pi$：$\\pi|_K$ 含 $\\sigma$ $\\iff$ $\\pi\\in R(L,\\varsigma)$；(2) $\\sigma$ 是 $(L,\\varsigma)$ 的 $K$-型，若对所有光滑不可约 $\\pi$：$\\pi|_K$ 含 $\\sigma$ $\\Rightarrow$ $\\pi\\in R(L,\\varsigma)$；(3) 对 $\\pi\\in R(L,\\varsigma)$，$\\pi$ 的极小 $K$-型是出现在 $\\pi|_K$ 中的、维数最小的 $K$-型。",
            "notation": "$K=\\GL_n(\\mathcal O_K)$；底本注：本文的 type 与 [9]（Paskunas）一致，而与 [4]（Bushnell–Kutzko）不同；后者称 Bushnell–Kutzko 型，是一对 $(J,\\sigma)$，$J$ 为更一般的紧开子群。",
        },
        key_points=[
            "「类型」是双向判据，等价于「分量 $R(L,\\varsigma)$ 由单个不可约 $K$-表示 $\\sigma$ 探测」；「$K$-型」只有单向，故一个分量可以有多个 $K$-型，但类型（若存在）唯一决定分量。",
            "两个概念都只依赖 $(L,\\varsigma)\\in\\mathcal B$，与具体的 $\\pi$ 无关；只有「极小 $K$-型」依赖 $\\pi$ 本身——同一分量里不同的 $\\pi$ 可以有不同维数的极小 $K$-型。",
            "Bushnell–Kutzko 型把 $K=\\GL_n(\\mathcal O_K)$ 换成更一般的紧开子群 $J$，这才能覆盖「深度 $>0$」的分量；底本的 type 定义钉死在 $\\GL_n(\\mathcal O_K)$ 上，只能处理「$K$-型」层级。",
            "底本把类型理论放在 §4.3「最后简要讨论」，且只在 $K=\\GL_n(\\mathcal O_K)$ 上定义，这与 §4.2 的惯性对应形成对照：惯性类型（Galois 侧）由 $I_K$ 给出，类型（自守侧）由 $\\GL_n(\\mathcal O_K)$ 给出。",
        ],
        formulas=[
            "$\\sigma\\ \\text{是}\\ (L,\\varsigma)\\ \\text{的类型}\\iff \\big[\\pi|_K\\ni\\sigma\\iff\\pi\\in R(L,\\varsigma)\\big]\\ \\forall\\pi$",
            "$\\sigma\\ \\text{是}\\ (L,\\varsigma)\\ \\text{的}\\ K\\text{-型}\\iff \\big[\\pi|_K\\ni\\sigma\\Rightarrow\\pi\\in R(L,\\varsigma)\\big]\\ \\forall\\pi$",
            "$\\sigma_{\\min}\\ \\text{是}\\ \\pi\\ \\text{的极小}\\ K\\text{-型}\\iff \\dim\\sigma_{\\min}=\\min\\{\\dim\\sigma:\\sigma\\subset\\pi|_K,\\ \\sigma\\ \\text{为}\\ K\\text{-型}\\}$",
        ],
        pitfalls=[
            "「$\\pi|_K$ 含 $\\sigma$」用的是 $K$ 上的表示包含，不是 $G$ 上的同态；$\\sigma$ 可以完全不含 $G$-结构。",
            "极小 $K$-型不是「所有 $K$-型里维数最小的」，而是「出现在这个具体 $\\pi|_{K}$ 里的 $K$-型中维数最小的」；跨分量比较没有意义。",
        ],
        related=[
            "yao17/concept/bernstein-decomposition",
            "yao17/concept/inertial-correspondence",
            "yao17/concept/satake",
        ],
        sources=[
            {
                "text": "A",
                "section": "§4.3.1",
                "pages": [35, 35],
                "quote": "σ is a type for (L, ς) if for all smooth irreducible representations π ∈ Rep^∞_n, π|_K contains σ ⇔ π ∈ R(L,ς)",
                "anchor": "A p.35",
            }
        ],
        provenance_note="类型/Ｋ-型/极小 $K$-型三条定义与 Bushnell–Kutzko 的对照取自 p.35 的 4.3.1；「单向 vs 双向」的解释是我们的判断。",
        rights="rewritten",
        status="dev",
    )
