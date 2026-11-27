# -*- coding: utf-8 -*-
"""cards_o.py —— 轨 O：总览与主陈述（3 张概念卡）。"""


def add(mk):
    mk(
        id="yao17/concept/llc-statement",
        type="concept",
        track="O",
        title="局部 Langlands 对应：定理 2.13 的五条性质",
        aliases=["LLC", "定理 2.13", "rec_n", "局部朗兰兹对应"],
        summary="rec_n 把 GL_n(K) 的不可约容许表示双射到 n 维 Frobenius 半单 Weil-Deligne 表示，由五条性质唯一刻画。",
        question="底本把局部 Langlands 对应陈述成什么？五条性质各自钉住了 rec_n 的哪一面？",
        definition={
            "text": "存在唯一一族集合双射 $\\rec_n$：$\\GL_n(K)$ 的不可约容许表示的同构类 $\\to$ $W_K$ 的 $n$ 维 Frobenius 半单 Weil–Deligne 表示的同构类，满足：(1) 对 $K^\\times$ 的每个不可约拟特征标 $\\chi$，$\\rec_1(\\chi)=\\chi\\circ\\Art_K^{-1}$；(2) 对任意 $\\pi_1,\\pi_2$，$L(\\pi_1\\times\\pi_2,s)=L(\\rec_{n_1}(\\pi_1)\\otimes\\rec_{n_2}(\\pi_2),s)$，$\\epsilon$ 因子同；(3) $\\rec_n(\\pi\\chi)=\\rec_n(\\pi)\\otimes\\rec_1(\\chi)$；(4) $\\det\\circ\\rec_n(\\pi)=\\rec_1(\\omega_\\pi)$；(5) $\\rec_n(\\pi^\\vee)=\\rec_n(\\pi)^\\vee$。",
            "notation": "$\\Art_K\\colon K^\\times\\xrightarrow{\\sim}W_K^{\\mathrm{ab}}$ 是局部类域论的同构；$\\omega_\\pi$ 是 $\\pi$ 的中心特征标；$\\pi^\\vee$ 是反变对偶。",
        },
        key_points=[
            "性质 (1) 把 $n=1$ 的情形钉死为局部类域论，整族 $\\rec_n$ 由此才有确定的归一化；没有 (1) 就无法排除大量「差一个非分歧扭转」的候选。",
            "(2) 是唯一一条把自守侧的 Rankin–Selberg $L$/$\\epsilon$ 因子与 Galois 侧的张量积因子绑在一起的公理，也是 Henniart 证明唯一性的主武器。",
            "(3)(4)(5) 分别固定扭转、行列式、对偶三条函子性，它们保证 $\\rec_n$ 与表示论的标准操作交换；底本把它们和 (1)(2) 并列，是因为证明唯一性时这些全都要用。",
            "两条守恒量由对应自动保持：导子 $c(\\pi)=c(\\rec_n(\\pi))$（(2) 的副产品）与 Moy–Prasad 深度 $d(\\pi)=d(\\rec_n(\\pi))$。",
            "底本在此处尚未定义 $L$/$\\epsilon$ 因子、平方可积、缓增、一般表示，也照实提醒了读者「虽然如此，仍值得先把 LLC 精确陈述出来」。",
        ],
        formulas=[
            "$\\rec_n\\colon\\{\\pi\\in\\Repadm_{\\GL_n(K)}\\text{ 不可约}\\}/\\cong\\;\\xrightarrow{\\ \\sim\\ }\\{(\\rho,N)\\in\\wd_K:\\dim\\rho=n,\\ \\text{Frobenius 半单}\\}/\\cong$",
            "$L(\\pi_1\\times\\pi_2,s)=L(\\rec_{n_1}(\\pi_1)\\otimes\\rec_{n_2}(\\pi_2),s),\\qquad \\epsilon(\\pi_1\\times\\pi_2,s)=\\epsilon(\\rec_{n_1}(\\pi_1)\\otimes\\rec_{n_2}(\\pi_2),s)$",
            "$c(\\pi)=c(\\rec_n(\\pi)),\\qquad d(\\pi)=d(\\rec_n(\\pi))$",
        ],
        theorems=[
            {
                "name": "定理 2.13（局部 Langlands 对应）",
                "statement": "存在唯一一族双射 $\\rec_n$（$n\\ge 1$）从 $\\GL_n(K)$ 的不可约容许表示的同构类到 $W_K$ 的 $n$ 维 Frobenius 半单 Weil–Deligne 表示的同构类，满足 (1)–(5)。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本只陈述不证明；证明归于 Harris–Taylor（$K/\\mathbb Q_p$）与 Henniart，Scholze 的进路可绕开数值 LLC，底本未展开。",
                },
                "source": "A §2.3.1 p.21–p.22",
            },
            {
                "name": "Henniart 的归约（底本 Remark）",
                "statement": "只需在超尖点表示上造出一族满足 (1)–(5) 的映射 $\\rec_n$，则它自动是双射且唯一。",
                "proof": {
                    "status": "sketch",
                    "gap_note": "底本只给策略 (i)–(iv)：BZ 归约到超尖点；$\\epsilon$ 因子归约到「存在」；Henniart 数值 LLC 由单射得满射；$L$ 因子性质证单射。四步均未写出细节。",
                },
                "source": "A §2.3.1 p.21–p.22",
            },
        ],
        pitfalls=[
            "定理里要求的是 Frobenius 半单的 Weil–Deligne 表示，不是全体 Weil–Deligne 表示；$\\wd_K$ 里带 $N\\neq 0$ 的对象对应的是「非半单」的自守侧数据（见 Steinberg 与 $\\Sp_m$）。",
            "性质 (2) 里的 $\\pi_1\\times\\pi_2$ 是抛物诱导的（可能可约的）表示，$L$/$\\epsilon$ 因子按 §3.6 对容许表示定义，不能读成不可约张量积。",
        ],
        related=[
            "yao17/concept/llc-finer-properties",
            "yao17/concept/bz-classification",
            "yao17/concept/wd-invariants",
            "yao17/deriv/gl2-llc-cases",
            "yao17/concept/conductor-depth",
        ],
        sources=[
            {
                "text": "A",
                "section": "§2.3.1",
                "pages": [21, 22],
                "quote": "There exists a unique collection of bijections of sets rec_n ... satisfying the following list of properties",
                "anchor": "A p.21",
            }
        ],
        provenance_note="定义与 (1)–(5) 逐条取自 p.21 定理 2.13；两条守恒量见同页 Remark，Henniart 策略见 p.21–p.22。摘要中「五条性质」的归属（哪条管哪一面）是我们的判断。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/llc-finer-properties",
        type="concept",
        track="O",
        title="定理 2.14：超尖点、本质平方可积、一般表示在对应下的像",
        aliases=["定理 2.14", "finer correspondence"],
        summary="rec_n 把超尖点送成不可约、把本质平方可积送成不可分解、把一般表示送成 ad 的 L 因子在 s=1 无极点。",
        question="除了定理 2.13 的五条公理，底本还给 LLC 补了哪三条更细的性质？它们各对应自守侧的哪一类表示？",
        definition={
            "text": "在定理 2.13 的 $\\rec_n$ 之下：(1) $\\pi\\in\\Repadm_G$ 不可约且超尖点，当且仅当 $\\rec_n(\\pi)$ 不可约；(2) $\\pi$ 本质平方可积，当且仅当 $\\rec_n(\\pi)$ 不可分解；(3) $\\pi$ 一般（generic），当且仅当 $L(\\ad\\circ\\rec_n(\\pi),s)$ 在 $s=1$ 处无极点。",
            "notation": "$\\ad$ 指 $\\GL_n$ 的伴随表示 $\\mathfrak{gl}_n$，故 $\\ad\\circ\\rec_n(\\pi)$ 是 $W_K\\times\\SL_2$ 表示在 $\\mathfrak{gl}_n$ 上的作用；底本记 $\\rec$ 为 $r_n$（同为 $\\rec_n$）。",
        },
        key_points=[
            "这三条不是用来保证唯一性的公理（底本明说定理 2.13 的五条才是），而是「更精细的信息」：它们把自守侧的三类表示与 $\\rec_n(\\pi)$ 的三个结构性质（不可约、不可分解、$\\ad$ 的 $L$ 因子无极点）一一对上。",
            "(1) 与 (2) 的区别就是「不可约」与「不可分解」的区别：$\\rec_n(\\pi)$ 可以分解成若干块而仍不可约化；$\\Sp_m(r)$ 正是这种块的模型。",
            "(3) 的 $\\ad$ 是 $\\GL_n$ 的 Lie 代数，$L(\\ad\\circ\\rho,s)$ 的极点位置读出 $\\rho$ 里有没有「单值块」；$s=1$ 处的极点恰对应一般的自守侧失败（无 Whittaker 模型）。",
            "三条都能用 $N$ 的幂零性直接检验：$N=0$ 且 $\\rho'$ 不可约给 (1)，$N$ 非零给 (2) 的「可分解」，$\\mathfrak{gl}_n^{\\rho'}$ 中不变向量的重数给 (3)。",
        ],
        formulas=[
            "$\\pi\\ \\text{超尖点}\\iff \\rec_n(\\pi)\\ \\text{不可约}$",
            "$\\pi\\ \\text{本质平方可积}\\iff \\rec_n(\\pi)\\ \\text{不可分解}$",
            "$\\pi\\ \\text{一般}\\iff L(\\ad\\circ\\rec_n(\\pi),s)\\|_{s=1}\\ \\text{无极点}$",
        ],
        theorems=[
            {
                "name": "定理 2.14",
                "statement": "在 $\\rec_n$ 为 LLC 下，(1) 超尖点 $\\leftrightarrow$ 不可约；(2) 本质平方可积 $\\leftrightarrow$ 不可分解；(3) 一般 $\\leftrightarrow$ $L(\\ad\\circ\\rec_n(\\pi),s)$ 在 $s=1$ 无极点。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本不证，且把这三条「视为额外性质」；它们分别需要超尖点判据（§2.2）、本质平方可积的定义（§3.2）与 Whittaker 模型理论（§3.2.2）。",
                },
                "source": "A §2.3.2 p.22",
            }
        ],
        pitfalls=[
            "「不可分解」不等同于「不可约」：定理 2.14(2) 说的是 $\\rec_n(\\pi)$ 作为 $W_K\\times\\SL_2$ 表示不可分解，允许它有可约的 Jordan–Hölder 因子链。",
            "定理 2.13 已把目标范畴限制在 Frobenius 半单对象上，所以 (1)(2) 的差别全落在 $N$ 上，而不是落在 $\\rho'$ 的半单性上。",
        ],
        related=[
            "yao17/concept/llc-statement",
            "yao17/concept/square-integrable-tempered",
            "yao17/concept/generic-whittaker",
            "yao17/concept/jacquet-supercuspidal",
        ],
        sources=[
            {
                "text": "A",
                "section": "§2.3.2",
                "pages": [22, 22],
                "quote": "The following ones can be regarded as extra properties (and they provide finer information on rec_n)",
                "anchor": "A p.22",
            }
        ],
        provenance_note="三条性质逐条取自 p.22 定理 2.14；key_points 中对「不可约 vs 不可分解」「$\\ad$ 的极点读什么」的解释是我们的判断，底本未展开。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/bz-classification",
        type="concept",
        track="O",
        title="定理 3.1：Bernstein–Zelevinsky 对 GL_n 容许表示的七条分类",
        aliases=["定理 3.1", "BZ 分类", "Q(Δ)", "Z(Δ)"],
        summary="用段 Δ 造出 Q(Δ) 与 Z(Δ)，任何不可约表示唯一地是 Q(Δ_1,…,Δ_r)，且 Q 侧对 (∗)-置换不变。",
        question="定理 3.1 的七条各说了什么？为什么它可以被读成「GL_n 的不可约表示由段的有序组唯一决定」？",
        definition={
            "text": "$\\Delta=\\Delta(\\pi,m)=[\\pi,\\pi(1),\\dots,\\pi(m-1)]$ 是段，$\\pi(\\Delta)=\\pi_1\\times\\dots\\times\\pi_m$ 是抛物诱导。定理 3.1：(1) $\\pi(\\Delta)$ 的长度为 $2^{m-1}$；(2) 有限长段 $\\Delta$ 的 $\\pi(\\Delta)$ 有唯一不可约子表示 $Z(\\Delta)$ 与唯一不可约商 $Q(\\Delta)$；(3) 满足 $(\\ast)$ 的 $\\Delta_1,\\dots,\\Delta_r$，$Q(\\Delta_1)\\times\\dots\\times Q(\\Delta_r)$ 有唯一不可约商 $Q(\\Delta_1,\\dots,\\Delta_r)$，且在 $(\\ast)$-置换下不变；(4) 任一不可约 $\\pi\\cong Q(\\Delta_1,\\dots,\\Delta_r)$，$n=\\sum n_im_i$，且该段组在 $(\\ast)$-置换下唯一；(5) $Q(\\Delta_1)\\times\\dots\\times Q(\\Delta_r)$ 不可约当且仅当任两段不 linked；(6) $Q(\\Delta^\\vee)=Q(\\Delta)^\\vee$；(7) $Z$ 侧有对偶的 (3)–(6)。",
            "notation": "$\\pi(s)$ 是 $\\pi$ 用 $|\\det|^s$ 的扭转；$\\Asc_n$ 是超尖点表示按「$\\pi\\le\\pi(s)$，$s\\in\\mathbb Z_{\\ge 0}$」排序的偏序集；(∗) 条件：对 $i<j$，$\\Delta_i$ 不 precede $\\Delta_j$。",
        },
        key_points=[
            "整条定理的枢纽是 (2)：$\\pi(\\Delta)$ 有唯一不可约商 $Q(\\Delta)$，这才是可乘的「原子」；(1) 的长度 $2^{m-1}$ 说明一个段诱导出来的是 $2^{m-1}$ 个 Jordan–Hölder 因子，故 (5) 的不可约判据（无 linked）是极强条件。",
            "(3)(4) 合起来说：不可约表示与「满足 $(\\ast)$ 的段组”一一对应，而 $(\\ast)$-置换不改变 $Q$——所以真正的不变量是无序段组，注记里正是这么说的。",
            "(6)(7) 是对偶性：取反变对偶把 $Q$ 侧换成 $Q$ 侧（$\\Delta^\\vee=[\\pi(m-1)^\\vee,\\dots,\\pi^\\vee]$），而 $Z$ 侧的自反性给出 Buchsbaum 型对偶陈述。",
            "Grothendieck 群 $R_K=\\oplus_nR_n(K)$ 用 $[\\pi_1]\\cdot[\\pi_2]=[\\pi_1\\times\\pi_2]$ 成为分次交换环，$Q(\\Delta)\\mapsto Z(\\Delta)$ 在其上给出对合——这是底本注记里的第二条结构性结论。",
        ],
        formulas=[
            "$\\Delta(\\pi,m)=[\\pi,\\pi(1),\\dots,\\pi(m-1)],\\qquad \\pi(\\Delta)=\\pi_1\\times\\dots\\times\\pi_m=I_{\\GL_{mn}}^{P(n,\\dots,n)}(\\pi_1\\otimes\\dots\\otimes\\pi_m)$",
            "$\\operatorname{length}\\pi(\\Delta)=2^{m-1}$",
            "$\\pi\\cong Q(\\Delta_1,\\dots,\\Delta_r)\\iff \\text{段组在 }(\\ast)\\text{-置换下唯一}$",
            "$\\Delta^\\vee=[\\pi(m-1)^\\vee,\\dots,\\pi^\\vee],\\qquad Q(\\Delta_1^\\vee,\\dots,\\Delta_r^\\vee)=Q(\\Delta_1,\\dots,\\Delta_r)^\\vee$",
        ],
        theorems=[
            {
                "name": "定理 3.1（Bernstein–Zelevinsky）",
                "statement": "上述 (1)–(7) 全部成立。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本只陈述；(1) 来自 BZ 的「长度 = 段长减一的 2 的幂」，(2)–(7) 来自 BZ 的 Langlands 型分类与几何引理，底本未给证明。",
                },
                "source": "A §3.1.3 p.24",
            }
        ],
        pitfalls=[
            "$(\\ast)$ 条件只对 $n_i=n_j$ 的段对起作用（段不 linked 时该条为空），所以它看起来「宽松」，但 (3) 的商 $Q(\\Delta_1,\\dots,\\Delta_r)$ 仍依赖顺序给出唯一的不可约商，不能把顺序随便换。",
            "$Q(\\Delta)$ 是商、$Z(\\Delta)$ 是子表示，二者一般不同构；只有当 $\\Delta$ 长度为 1（即 $\\pi$ 本身超尖点）时 $Q=Z=\\pi$。",
            "(5) 的「不可约」是在问 $Q(\\Delta_1)\\times\\dots\\times Q(\\Delta_r)$ 这个抛物诱导本身，而不是它的某个商。",
        ],
        related=[
            "yao17/concept/zelevinsky-segment",
            "yao17/concept/supercuspidal-support",
            "yao17/concept/llc-statement",
            "yao17/deriv/induction-to-supercuspidal",
        ],
        sources=[
            {
                "text": "A",
                "section": "§3.1.3",
                "pages": [24, 25],
                "quote": "For each Zelevinsky segment Δ of length m, the representation π(Δ) has length 2^{m−1}",
                "anchor": "A p.24",
            }
        ],
        provenance_note="(1)–(7) 逐条照抄 p.24 定理 3.1；$R_K$ 的环结构与对合见 p.24 第二条 Remark；key_points 中「枢纽是 (2)」「(∗) 只对同维段对起作用」是我们的判断。",
        rights="rewritten",
        status="dev",
    )
