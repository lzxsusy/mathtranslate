# -*- coding: utf-8 -*-
"""cards_deriv.py —— 6 张推导卡（id 前缀 yao17/deriv/）。"""


def add(mk):
    mk(
        id="yao17/deriv/wd-from-galois",
        type="derivation",
        track="A",
        aliases=["引理 1.5 的构造", "N = log ρ(σ)", "mod-l 归约"],
        title="从 ℓ 进表示造出 (ρ, N)：引理 1.5 的构造五步",
        summary="把 ℓ 进表示先模 ℓ、再沿惯性群的 ℓ 进商分解，取 N=log ρ(σ) 即得 Weil–Deligne 表示。",
        question="给定 ρ:G_K→GL_n(Q̄_ℓ)，具体怎么变出一对 (ρ, N)？N 为什么一定幂零、又为什么满足 ρ(τ)Nρ(τ)^{-1}=q^{-n}N？",
        goal="对任意 ρ:G_K→GL_n(Q̄_ℓ)，构造 $N$ 使 $(\\rho,N)$ 是 Weil–Deligne 表示，即引出理 1.5 的满性。",
        setup=[
            "$K$ 是 $p$ 进局部域，$p\\neq\\ell$，$q$ 为剩余域大小；$G_K$ 是绝对 Galois 群，$I_K$ 是惯性群，$P_K$ 是野惯性群。",
            "$\\rho\\colon G_K\\to\\GL_n(\\overline{\\mathbb Q}_\\ell)$ 是连续表示；$t_\\ell\\colon I_K\\to\\mathbb Z_\\ell(1)$ 是惯性群的驯商同构。",
        ],
        steps=[
            {
                "no": 1,
                "text": "取 $G_K$ 在 $\\overline{\\mathbb Q}_\\ell^n$ 中的稳定 $\\mathcal O_L$ 格 $\\Lambda$（$L/\\mathbb Q_\\ell$ 充分大，$\\mathcal O_L$ 是其整数环），模 $\\ell$ 得 $\\rho_\\Lambda\\colon G_K\\to\\Aut_{\\mathbb F_\\ell}(\\Lambda/\\ell)$。",
                "why": "模 $\\ell$ 把「$\\ell$ 进」信息压成有限域上作用，使后面的核与商都是 pro-$\\ell$ 群，从而可以由 $t_\\ell$ 参数化。",
                "locator": "A p.7",
                "provenance": "A",
            },
            {
                "no": 2,
                "text": "置 $G_{K''}=\\ker\\rho_\\Lambda$。它是指标有限的闭正规子群，故 $K''/K$ 是有限扩张；记 $q_{K''}$ 为 $K''$ 的剩余域大小。",
                "why": "指标有限保证「模 $\\ell$ 的核」仍是一个开子群，后续的惯性群 $I_{K''}$ 才有意义。",
                "locator": "A p.7",
                "provenance": "A",
            },
            {
                "no": 3,
                "text": "由 $\\rho_\\Lambda|_{I_{K''}}$ 的核是 pro-$\\ell$ 群，得 $\\rho\\colon I_{K''}\\to\\GL_n(\\overline{\\mathbb Q}_\\ell)$ 通过 $t_\\ell\\colon I_{K''}\\to\\mathbb Z_\\ell(1)$ 分解，即存在 $g\\in\\GL_n(\\overline{\\mathbb Q}_\\ell)$ 与 $a\\in\\mathbb Z_\\ell$ 使 $\\rho|_{I_{K''}}=\\exp(t_\\ell\\cdot g)$。",
                "why": "这一步是全部构造的核心：惯性群在 $\\ell$ 进表示上的作用由单个幂零「生成元」$g$ 决定，$N$ 就取它。",
                "locator": "A p.7",
                "provenance": "A",
            },
            {
                "no": 4,
                "text": "取 $t_\\ell$ 的一个拓扑生成元 $\\sigma\\in I_{K''}$（即 $t_\\ell(\\sigma)=1$），令 $N=\\log\\rho(\\sigma)$。由于 $\\rho(\\sigma)$ 幂幺，$N$ 是幂零矩阵。",
                "why": "$\\sigma$ 的选取不唯一，但换一个生成元只差整数倍，$N$ 相应乘标量；配合下面的共轭关系可证 $(\\rho,N)$ 良定。",
                "locator": "A p.8",
                "provenance": "A",
            },
            {
                "no": 5,
                "text": "对 $\\sigma\\in I_{K''}$ 与 $\\tau\\in G_K$，由 $\\tau\\sigma\\tau^{-1}$ 的 $t_\\ell$ 像得 $\\rho(\\tau)N\\rho(\\tau)^{-1}=|\\Art\\tau|^{-1}N$；把 $\\rho$ 用半单部分 $r$ 与局部类域论 $\\Art$ 改写，即得 $r(\\tau)N r(\\tau)^{-1}=q^{-n}N$，其中 $n$ 由 $r(\\tau)$ 在 $|\\cdot|$ 上的取值决定。",
                "why": "这条共轭关系正是定义 1.1.3 的 (iii)；它保证了 $N$ 落在 $r$ 的「$-2$ 权重」部分，是 Weil–Deligne 表示定义中不可省的一环。",
                "locator": "A p.8",
                "provenance": "A",
            },
        ],
        result="每给一个 $\\rho\\colon G_K\\to\\GL_n(\\overline{\\mathbb Q}_\\ell)$ 就能造出 $(\\rho,N)$：$\\rho$ 取半单部分、$N=\\log\\rho(\\sigma)$，且 $N$ 幂零并满足 $\\rho(\\tau)N\\rho(\\tau)^{-1}=q^{-n}N$。故引理 1.5 的映射 $\\rho\\mapsto(\\rho,N)$ 是满的，配合引理 1.2 的单性即得 $\\WD$ 是范畴等价（推论 1.7）。",
        gaps=[
            "第 5 步的 $|\\Art\\tau|^{-1}$ 到 $q^{-n}$ 的换算底本只写「由此得到」，未逐步展开 $\\Art$ 与 $|\\cdot|$ 的相容性。",
            "$N$ 与生成元选取的无关性（换 $\\sigma$ 只改标量）底本作显然处理。",
        ],
        pitfalls=[
            "第 3 步的核「是 pro-$\\ell$ 群」用的是 $\\Lambda/\\ell$ 上作用为平凡，而非 $\\rho$ 本身；若一开始就对 $\\rho$ 取核会得到平凡群，什么都推不出来。",
            "$N=\\log\\rho(\\sigma)$ 需要 $\\rho(\\sigma)$ 幂幺（即 $\\equiv1\\bmod\\ell$ 的 $\\ell$ 元素），这一步依赖第 3 步的分解，不能对任意 $\\rho(\\sigma)$ 直接取对数。",
            "共轭关系里出现的是半单部分 $r$ 而不是 $\\rho$ 本身；底本在 p.8 明说「$\\rho$ 换成其半单化不影响 $N$ 的共轭关系」。",
        ],
        related=[
            "yao17/concept/wd-representation",
            "yao17/concept/wd-functor",
            "yao17/concept/frobenius-semisimple",
        ],
        sources=[
            {
                "text": "A",
                "section": "§1.2.1（引理 1.5 的证明）",
                "pages": [7, 8],
                "quote": "we may reduce rho modulo l, the kernel is a pro-l group",
                "anchor": "A p.7",
            }
        ],
        provenance_note="五步构造依底本引理 1.5 的证明整理（p.7–p.8）；底本证明较简，第 3、5 步的细节由我们补足并标注为「我们的整理」。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/deriv/supercuspidal-criterion",
        type="derivation",
        track="B",
        aliases=["引理 2.10", "Jacquet 函子判据", "超尖点性判据"],
        title="超尖点判据：π 非超尖点 ⇒ 可嵌入某真抛物诱导（引理 2.10 的证明链）",
        summary="若 J_P π ≠ 0，取不可约商 σ 并用伴随性把 π 嵌进 I_P σ；σ 非超尖点则再降，直到 σ 超尖点。",
        question="为什么「对一切真抛物 P 都有 J_P π = 0」等价于「π 是某个超尖点表示的抛物诱导的子商」？",
        goal="证明引理 2.10：$\\pi$ 超尖点 $\\iff$ 对一切真抛物子群 $P$ 都有 $J_P\\pi=0$。",
        setup=[
            "$G=\\GL_n(K)$，$P=LU$ 是真抛物子群，$J_P$ 是 Jacquet 函子（$U$-余不变量），$I_P$ 是正规化抛物诱导，二者伴随：$\\Hom_G(\\pi,I_P\\sigma)\\cong\\Hom_L(J_P\\pi,\\sigma)$。",
            "超尖点的定义（§2.2.4）：$\\pi$ 不可约容许且不出现为任何真抛物诱导的子商。",
        ],
        steps=[
            {
                "no": 1,
                "text": "设存在真抛物 $P$ 使 $J_P\\pi\\neq0$。因 $J_P\\pi$ 是 $L$ 上的光滑表示，取它的一个非零不可约商 $\\sigma$。",
                "why": "把「$J_P\\pi$ 非零」换成「有一个不可约商」，才能用伴随性与不可约性做文章。",
                "locator": "A p.19",
                "provenance": "A",
            },
            {
                "no": 2,
                "text": "由伴随性，$0\\neq\\Hom_L(J_P\\pi,\\sigma)\\cong\\Hom_G(\\pi,I_P\\sigma)$，故 $\\pi$ 嵌入 $I_P\\sigma$（作为 $G$-表示的子表示）。",
                "why": "这是整条链的枢纽：非零的 $L$-同态被转成非零的 $G$-同态，从而 $\\pi$ 成为抛物诱导的子表示。",
                "locator": "A p.19",
                "provenance": "A",
            },
            {
                "no": 3,
                "text": "若 $\\sigma$ 仍非超尖点，对 $\\sigma$ 重复第 1–2 步，得到更小的 Levi $L'\\subsetneq L$ 与 $\\sigma'$ 使 $\\sigma\\hookrightarrow I_{P'}^{L}\\sigma'$。逐次下降，Levi 维数严格减小。",
                "why": "这一步保证过程终止：Levi 因子的半单秩每次严格下降，不可能无限进行。",
                "locator": "A p.19",
                "provenance": "A",
            },
            {
                "no": 4,
                "text": "终止时得到某个 Levi $M$ 上的超尖点 $\\sigma_0$ 与抛物 $Q=MN$，使 $\\pi\\hookrightarrow I_Q\\sigma_0$：即 $\\pi$ 是某个超尖点表示的抛物诱导的子表示（进而是其子商）。",
                "why": "这正是「超尖点性的反面」：只要 $\\pi$ 不是超尖点，它必是某个真抛物诱导的子商，与定义矛盾。",
                "locator": "A p.20",
                "provenance": "A",
            },
        ],
        result="反向（$\\pi$ 超尖点 $\\Rightarrow$ 一切 $J_P\\pi=0$）由伴随性立即得到：若 $J_P\\pi\\neq0$ 则 $\\pi$ 嵌入 $I_P\\sigma$，与非超尖点矛盾。故引理 2.10 成立，它把「超尖点」这个看似用诱导定义的性质，化成了「所有真抛物 Jacquet 函子为零」这一可计算的条件。",
        gaps=[
            "「逐次下降必终止」底本只说「重复此过程」，未给出 Levi 半单秩严格下降的论证。",
            "第 4 步用的是「子表示 ⇒ 子商」，底本直接写子商，未区分嵌入与商。",
        ],
        pitfalls=[
            "伴随性给的是「$\\pi$ 嵌入 $I_P\\sigma$」（子表示），而超尖点定义禁止的是「$\\pi$ 出现为子商」；由子表示推子商需要 $\\pi$ 不可约，这一步底本默认了。",
            "第 1 步必须取「非零不可约商」而不是「非零子表示」：只有商才能让 $\\Hom_L(J_P\\pi,\\sigma)\\neq0$ 由 $\\sigma\\hookrightarrow J_P\\pi$ 的满射得到。",
            "$J_P$ 用的是 $U$-余不变量（不取正规化），与 $I_P$ 的伴随性要求 $I_P$ 用模特征标 $\\delta_P^{1/2}$ 正规化；两者要配套，否则伴随性差一个扭转。",
        ],
        related=[
            "yao17/concept/jacquet-supercuspidal",
            "yao17/concept/parabolic-induction",
            "yao17/concept/llc-statement",
        ],
        sources=[
            {
                "text": "A",
                "section": "§2.2.2–§2.2.4（引理 2.10）",
                "pages": [19, 20],
                "quote": "The following are equivalent: (1) π is supercuspidal; (2) J_P π = 0 for all proper parabolic subgroups",
                "anchor": "A p.19",
            }
        ],
        provenance_note="四步依底本引理 2.10 及其证明整理（p.19–p.20）；「Levi 秩下降保证终止」「子表示 vs 子商」两处是我们补的，已在 gaps 标出。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/deriv/gl2-llc-cases",
        type="derivation",
        track="C",
        aliases=["GL(2) 的 LLC", "四类表示", "Sp_2(χ)"],
        title="GL₂ 的四类表示如何对应到 Weil–Deligne 表示",
        summary="超尖点↦不可约 (ρ,0)；主序列↦(χ₁⊕χ₂,0)；triv⊗χ↦(χ⊕χ(1),0)；St₂(χ)↦(χ⊕χ(1),N)。",
        question="GL₂ 的四类不可约容许表示分别对应哪一类 Weil–Deligne 表示？Sp₂(χ) 里的那个 N 作用在哪个向量上？",
        goal="在 $n=2$ 时把定理 2.13 的对应写全，验证四类 $\\pi$ 恰好覆盖 $\\WD_2$ 的四类对象。",
        setup=[
            "$K$ 是 $p$ 进局部域，$\\chi,\\chi_1,\\chi_2$ 是 $K^\\times$ 的特征标（经 $\\Art$ 也看成 $W_K$ 的特征标）。",
            "$\\rec_2\\colon\\mathcal G_2^{\\mathrm{irr}}\\to\\WD_2$ 是 LLC 的逆；$\\WD_2$ 是 $\\dim=2$ 的 Weil–Deligne 表示类。",
        ],
        steps=[
            {
                "no": 1,
                "text": "第一类：$\\pi$ 不可约超尖点 $\\iff$ $\\rec_2(\\pi)=(\\rho,0)$ 且 $\\rho$ 不可约。",
                "why": "超尖点对应「不可约的 $\\rho$ 配 $N=0$」，这是 LLC 在 $n=2$ 时最干净的一半。",
                "locator": "A p.25",
                "provenance": "A",
            },
            {
                "no": 2,
                "text": "第二类：$\\pi=\\chi_1\\times\\chi_2$（主序列，$\\chi_1/\\chi_2\\neq|\\cdot|^{\\pm1}$）$\\iff$ $\\rec_2(\\pi)=(\\chi_1\\oplus\\chi_2,0)$，两个特征标都不可约。",
                "why": "主序列不可约时 $N=0$，而 $\\rho$ 可约（两个特征标直和）；这给出「可约 $\\rho$、$N=0$」的一类。",
                "locator": "A p.25",
                "provenance": "A",
            },
            {
                "no": 3,
                "text": "第三类：$\\pi=\\mathrm{triv}\\otimes\\chi=Q(\\chi|\\cdot|^{1/2},\\chi|\\cdot|^{-1/2})$（特殊表示，主序列的不可约商）$\\iff$ $\\rec_2(\\pi)=(\\chi\\oplus\\chi(1),0)$，即 Frobenius 半单、$N=0$ 但 $\\rho$ 是同一个特征标的两个不同扭转直和。",
                "why": "这是「$\\rho$ 不可分解但 $N=0$」的情形：$\\chi$ 与 $\\chi(1)$ 在 $W_K$ 作用下不能分开，却都在 $\\rho$ 里出现一次。",
                "locator": "A p.25",
                "provenance": "A",
            },
            {
                "no": 4,
                "text": "第四类：$\\pi=\\St_2(\\chi)=Q([\\chi|\\cdot|^{-1/2},\\chi|\\cdot|^{1/2}])$（Steinberg 扭转）$\\iff$ $\\rec_2(\\pi)=\\Sp_2(\\chi)=(\\chi\\oplus\\chi(1),N)$，其中 $N\\colon\\chi\\to\\chi(1)$ 是唯一非零的 $W_K$-映射，$N^2=0$。",
                "why": "$N\\neq0$ 正是「平方可积但非超尖点」在 Galois 侧的标志：$\\Sp_2$ 的 $N$ 把 $\\chi$ 打到 $\\chi(1)$，两端各出现一次。",
                "locator": "A p.26",
                "provenance": "A",
            },
            {
                "no": 5,
                "text": "核对覆盖：四类 $\\pi$ 的 $\\rec_2(\\pi)$ 分别落在「$\\rho$ 不可约」「$\\rho$ 半单可约」「$\\rho$ 不可分、$N=0$」「$N\\neq0$」四格，穷尽 $\\dim=2$ 的 Weil–Deligne 表示；且脚注 10 提醒更准确的写法是 $(\\Art^{-1}\\chi_1\\oplus\\Art^{-1}\\chi_2,0)$。",
                "why": "这一步把「四类」与「$\\WD_2$ 的全部分类」对齐，说明定理 2.13 在 $n=2$ 时确实是双射而不是单射。",
                "locator": "A p.26",
                "provenance": "A",
            },
        ],
        result="四类 $\\GL_2$ 的不可约容许表示与 $\\WD_2$ 的四类对象一一对应；$\\Sp_2(\\chi)$ 的 $N$ 把 $\\chi$ 送到 $\\chi(1)$，是「平方可积非超尖点」的 Galois 侧标志。",
        gaps=[
            "第三、四类的「$\\iff$」底本只写括号说明，未逐个验证双向；核对覆盖一步是我们补的。",
            "$Q([\\chi|\\cdot|^{-1/2},\\chi|\\cdot|^{1/2}])$ 作为唯一不可约商的论证底本略去，引 Zelevinsky。",
        ],
        pitfalls=[
            "$\\mathrm{triv}\\otimes\\chi$ 与 $\\St_2(\\chi)$ 都来自同一段 $[\\chi|\\cdot|^{-1/2},\\chi|\\cdot|^{1/2}]$，区别只在取子还是取商；对应到 WD 侧则是 $N=0$（子）与 $N\\neq0$（商）。",
            "写 $\\chi$ 还是 $\\Art^{-1}\\chi$ 要看把 $\\chi$ 放在 $K^\\times$ 侧还是 $W_K$ 侧；底本脚注 10 专门纠正这一点，混用会让 $\\rho$ 少一个扭转。",
            "$\\Sp_2(\\chi)$ 里 $N$ 的定义依赖 $\\chi(1)$ 与 $\\chi$ 的同构选取；换生成元只改标量，故 $\\Sp_2(\\chi)$ 作为同构类良定。",
        ],
        related=[
            "yao17/concept/llc-statement",
            "yao17/concept/wd-representation",
            "yao17/concept/square-integrable-tempered",
            "yao17/deriv/induction-to-supercuspidal",
        ],
        sources=[
            {
                "text": "A",
                "section": "§3.1.5–§3.1.6",
                "pages": [25, 26],
                "quote": "π = St_2(χ) if and only if rec_2(π) = Sp_2(χ)",
                "anchor": "A p.26",
            }
        ],
        provenance_note="四类对应与脚注 10 取自 p.25–p.26；「覆盖四格」的核对表是我们据 $\\WD_2$ 分类补的。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/deriv/induction-to-supercuspidal",
        type="derivation",
        track="C",
        aliases=["3.1.7", "rec_n 的拼接", "Zelevinsky 段归纳"],
        title="把 LLC 从超尖点归纳到一般表示：rec_n = ⊕ Sp_{m_i} ∘ rec_{n_i}",
        summary="由 BZ 把 π 写成 Q(Δ₁,…,Δ_r)，再对每个段用 Sp_{m_i}(rec_{n_i}(π_i))，底层 ρ 是 rec_{n_i}(π_i)(j) 的直和。",
        question="定理 2.13 为什么只需在超尖点上验证？一般 π 的 rec_n(π) 是怎么由各段的超尖点数据拼出来的？",
        goal="证明 §3.1.7：只需在 $\\Asc_n\\to\\mathcal G_n^{\\mathrm{irr}}$ 上构造 $\\rec_n$，一般情形由 BZ 分类唯一确定。",
        setup=[
            "$\\pi=Q(\\Delta_1,\\dots,\\Delta_r)$ 是 BZ 分类下的标准表示，$\\Delta_i=\\Delta_i(\\pi_i,m_i)$ 是 Zelevinsky 段，$\\pi_i$ 是 $\\GL_{n_i}(K)$ 的超尖点表示，$n=\\sum_i n_i m_i$。",
            "$\\Sp_m$ 是 $\\GL_m$ 的 Steinberg 表示在 LLC 下的像；$\\rec_{n_i}(\\pi_i)=\\rho_i$。",
        ],
        steps=[
            {
                "no": 1,
                "text": "由定理 3.1（BZ 分类），每个 $\\pi\\in\\mathcal G_n^{\\mathrm{irr}}$ 唯一写成 $Q(\\Delta_1,\\dots,\\Delta_r)$，其中 $\\Delta_i=\\Delta_i(\\pi_i,m_i)$ 且 $\\pi_i$ 超尖点、$n_i m_i=n$ 分配。",
                "why": "这一步把「一般表示」化归为「超尖点 + 段长」的有限数据，是归纳的出发点。",
                "locator": "A p.26",
                "provenance": "A",
            },
            {
                "no": 2,
                "text": "定义 $\\rec_n(\\pi):=\\bigoplus_i\\Sp_{m_i}(\\rec_{n_i}(\\pi_i))$。右边只依赖超尖点的 $\\rec_{n_i}(\\pi_i)$ 与段长 $m_i$。",
                "why": "这是「把 $\\Sp_m$ 看成 $W_K\\times\\SL_2$ 的表示」的直接用法：段长 $m$ 变成 $\\Sp_m$ 的维数。",
                "locator": "A p.26",
                "provenance": "A",
            },
            {
                "no": 3,
                "text": "写出底层 $W_K$ 表示：$\\rho=\\bigoplus_i\\bigoplus_{j=0}^{m_i-1}\\rec_{n_i}(\\pi_i)(j)$，即每个 $\\rec_{n_i}(\\pi_i)$ 取 $j=0,\\dots,m_i-1$ 的全部整数扭转。",
                "why": "$\\Sp_m$ 作为 $W_K\\times\\SL_2$ 表示在 $W_K$ 上正是 $\\bigoplus_{j=0}^{m-1}$ 的扭转链，这一步把 $\\rec_n(\\pi)$ 从「$\\SL_2$ 的表示」落回「一对 $(\\rho,N)$」。",
                "locator": "A p.26",
                "provenance": "A",
            },
            {
                "no": 4,
                "text": "验证与引理 2.11/2.12 相容：若各段两两不相连（$\\Delta_i$ 与 $\\Delta_j$ 不 linked），$Q(\\Delta_1,\\dots,\\Delta_r)$ 不可约，$\\rec_n$ 的直和分解与不可约性一致；若相连，则取唯一不可约商，对应取 $\\Sp_{m}$ 的更大段。",
                "why": "这一步保证归纳定义与「诱导是否不可约」的判据不冲突——即 $\\rec_n$ 在 $\\pi$ 不可约时确实给出不可约的 $(\\rho,N)$。",
                "locator": "A p.26",
                "provenance": "A",
            },
        ],
        result="$\\rec_n(\\pi)=\\bigoplus_i\\Sp_{m_i}(\\rec_{n_i}(\\pi_i))$，底层 $\\rho=\\bigoplus_i\\bigoplus_{j=0}^{m_i-1}\\rec_{n_i}(\\pi_i)(j)$。故定理 2.13 的构造只需在 $\\Asc_n$（超尖点）上给出 $\\rec_n$，一般情形由 BZ 分类唯一延拓。",
        gaps=[
            "第 4 步「相连时取更大段」底本只作一句带过，未给 $\\Sp_m$ 与 Zelevinsky 段的逐项对应。",
            "「唯一延拓」的相容性（与 BZ 分类的唯一性一致）底本未证，只说「由 BZ 分类唯一确定」。",
        ],
        pitfalls=[
            "底层 $\\rho$ 的扭转取 $j=0,\\dots,m_i-1$，而 p.25 的超尖点支撑排版只写到 $j=1,\\dots,m_i-1$（漏了 $j=0$）；按定义应为 $j=0$ 起，译本已在译注中点明。",
            "$\\Sp_{m_i}(\\rec_{n_i}(\\pi_i))$ 是 $W_K\\times\\SL_2$ 的表示，不是 $W_K$ 的；写成 $\\rho$ 时必须把 $\\SL_2$ 的权展开成扭转链，否则会少算因子。",
            "$n=\\sum_i n_i m_i$ 是对全部段求和，不是对 $i$ 取 $n_i$ 之和；漏掉 $m_i$ 会让 $\\dim\\rho$ 与 $n$ 对不上。",
        ],
        related=[
            "yao17/concept/bz-classification",
            "yao17/concept/zelevinsky-segment",
            "yao17/concept/llc-statement",
            "yao17/deriv/gl2-llc-cases",
        ],
        sources=[
            {
                "text": "A",
                "section": "§3.1.7",
                "pages": [26, 26],
                "quote": "rec_n(π) = ⊕_i Sp_{m_i}(rec_{n_i}(π_i))",
                "anchor": "A p.26",
            }
        ],
        provenance_note="公式与底层 $\\rho$ 的扭转链取自 p.26 的 3.1.7；第 4 步的相容性是我们的整理。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/deriv/depth-zero-chain",
        type="derivation",
        track="C",
        aliases=["深度 0", "Iwahori-球面", "驯分歧"],
        title="深度 0 的五条等价链：从 π^K ≠ 0 一路推到 N = 0",
        summary="非分歧↔π^K≠0↔rec 非分歧↔ρ|I_K=0 且 N=0；Iwahori-球面↔ρ|I_K=0；深度 0↔驯分歧。",
        question="深度 0、Iwahori-球面、非分歧这三种「越来越弱」的条件，在 Galois 侧分别对应什么？中间的等价为什么不能跳过？",
        goal="把 §3.5 的五条等价串成一条推理链，说明每一步用到哪条引理。",
        setup=[
            "$K=\\GL_n(\\mathcal O_K)$，$K_0$ 是 Iwahori 子群（$\\mathcal O_K$ 上的上三角模 $\\varpi$），$I_K$ 是惯性群，$P_K$ 是野惯性群。",
            "深度 $\\mathrm{depth}(\\pi)=\\min\\{m:\\pi^{G_m}\\neq0\\}$，$G_m$ 为 $\\GL_n$ 的 $m$ 级主同余子群；深度 0 即 $\\pi^K\\neq0$ 与 $\\pi$ 非分歧之间的广义化。",
        ],
        steps=[
            {
                "no": 1,
                "text": "$\\pi$ 非分歧 $\\iff\\pi^K\\neq0$：由定理 2.5（$G/K$ 上的 Iwasawa 分解与 Hecke 代数作用），非分歧表示恰是那些有 $K$-不变向量的。",
                "why": "这是整条链的锚点，把「表示论条件」与「$K$-不变向量」直接连起来。",
                "locator": "A p.30",
                "provenance": "A",
            },
            {
                "no": 2,
                "text": "$\\pi$ 非分歧 $\\iff$ $\\rec_n(\\pi)=(\\rho,N)$ 中 $\\rho|_{I_K}=0$ 且 $N=0$：非分歧表示对应 $G_K$ 经 $W_K/I_K\\cong\\mathbb Z$ 分解的表示，惯性群作用平凡，故 $N=\\log\\rho(\\sigma)=0$。",
                "why": "这一步是 LLC 与「惯性作用」的铰链：$I_K$ 作用平凡 $\\Rightarrow$ 无野惯性信息 $\\Rightarrow$ $N=0$。",
                "locator": "A p.30",
                "provenance": "A",
            },
            {
                "no": 3,
                "text": "$\\pi$ Iwahori-球面（即 $\\pi^{K_0}\\neq0$）$\\iff$ $\\rho|_{I_K}=0$。",
                "why": "Iwahori 子群 $K_0$ 是 $K$ 与 $I_K$ 之间「最小」的紧开子群，故它的不动向量恰好探测「惯性群是否平凡作用」；这一步比第 1 步弱，因为 $K_0\\subset K$。",
                "locator": "A p.30",
                "provenance": "A",
            },
            {
                "no": 4,
                "text": "$\\rec_n(\\pi)$ 为 $I_K$-球面（即 $\\rho|_{I_K}=0$ 但 $N$ 可非零）$\\iff$ $\\pi$ 的深度为 0 的「驯分歧」侧；$\\pi$ 深度 0 $\\iff$ $\\rec_n(\\pi)$ 驯分歧，即 $P_K$ 在 $\\rho$ 上作用平凡。",
                "why": "驯分歧 = 野惯性群 $P_K$ 作用平凡；深度 0 = 第一个非零不变向量出现在 $G_0=K$ 层，二者通过「$P_K$ 是可解的 pro-$p$ 群、$\\ell\\neq p$」对齐。",
                "locator": "A p.30",
                "provenance": "A",
            },
            {
                "no": 5,
                "text": "用引理 3.8（$c(\\pi)=c(\\rec_n\\pi)$）把「导子」串进来：$c(\\pi)=0\\iff\\pi$ 非分歧 $\\iff c(\\rec_n\\pi)=0$，与第 1–2 步闭环。",
                "why": "导子是深度的定量版本；引理 3.8 保证自守侧与 Galois 侧的导子相等，于是「深度 0」与「导子 0」在两侧同时成立。",
                "locator": "A p.30",
                "provenance": "A",
            },
        ],
        result="五条等价构成一条从强到弱的链：非分歧（$\\pi^K\\neq0$，$\\rho|_{I_K}=0,N=0$）$\\Rightarrow$ Iwahori-球面（$\\rho|_{I_K}=0$）$\\Rightarrow$ 深度 0（$\\rho$ 驯分歧，$P_K$ 作用平凡），反向的每一条都用到「$K_0\\subset K$、$P_K\\subset I_K$」的包含关系。",
        gaps=[
            "第 3 步「Iwahori-球面 $\\iff$ $\\rho|_{I_K}=0$」底本只列在图里，未给证明。",
            "第 4 步「深度 0 $\\iff$ 驯分歧」底本写作「$\\mathrm{rec}_n(\\pi)$ 驯分歧」，未展开 $G_m$ 层级与 $P_K$ 的对应。",
        ],
        pitfalls=[
            "「深度 0」不是「非分歧」：深度 0 允许 $\\pi$ 有 $K_0$-不变向量但无 $K$-不变向量（如 $\\St_2$ 的某些扭转），对应 $\\rho|_{I_K}=0$ 但 $N\\neq0$。",
            "$I_K$-球面说的是 $\\rec_n(\\pi)$ 作为 $W_K$-表示有 $I_K$-不变向量，不是 $\\pi$ 有 $I_K$-不变向量（$\\pi$ 是 $G$ 的表示，$I_K$ 不是 $G$ 的子群）；底本图里两侧的主语不同，读图时容易串。",
            "深度用 $G_m$ 层级定义时依赖 $\\GL_n$ 的整结构；换一个紧开子群滤波会改变「深度 0」的含义，故这条链只在标准 $G_m$ 下成立。",
        ],
        related=[
            "yao17/concept/conductor-depth",
            "yao17/concept/satake",
            "yao17/concept/wd-representation",
        ],
        sources=[
            {
                "text": "A",
                "section": "§3.5（深度 0 的等价图）",
                "pages": [30, 30],
                "quote": "π is unramified ⟺ π^K ≠ 0 ⟺ rec_n(π) is unramified",
                "anchor": "A p.30",
            }
        ],
        provenance_note="五条等价取自 p.30 的对照图；每一步「为什么」与 pitfalls 由我们补充，底本未给证明。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/deriv/inertia-from-bernstein",
        type="derivation",
        track="D",
        aliases=["引理 4.4 的证明", "惯性类型", "Bernstein 中心"],
        title="惯性对应怎么从 Bernstein 分量推出来：BZ 分类 → 超尖点 → 引理 4.3",
        summary="把 π 写成 Q(Δ₁..Δ_r) 后限制到 I_K，只剩各段超尖点的 rec，再用引理 4.3 逐个分离分量。",
        question="引理 4.4 的「同分量 ⇔ rec(π)|I_K 同构」是怎么从 BZ 分类与引理 4.3 一步步得到的？",
        goal="复现引理 4.4 的证明：把 $\\rec_n(\\pi)|_{I_K}$ 化成各超尖点块的直和，再用引理 4.3 的注分离。",
        setup=[
            "$\\pi=Q(\\Delta_1,\\dots,\\Delta_r)$，$\\Delta_i=\\Delta_i(\\pi_i,m_i)$，$\\pi_i$ 超尖点，$n=\\sum n_i m_i$；对应 Levi $L=\\prod_i\\GL_{n_i}(K)^{m_i}$。",
            "引理 4.3：$H\\triangleleft G$、$G/H$ 交换、$\\rho_1|_H\\cong\\rho_2|_H$ $\\Rightarrow$ $\\rho_2\\cong\\rho_1\\otimes\\psi$；注：只需 $\\Hom_H(\\rho_1,\\rho_2)\\neq0$。",
        ],
        steps=[
            {
                "no": 1,
                "text": "由 BZ 分类，$\\pi=Q(\\Delta_1,\\dots,\\Delta_r)$ 给出 $L=\\prod_i\\GL_{n_i}(K)^{m_i}$ 与 $\\sigma=\\bigotimes_{i,j}\\pi_i|\\cdot|^j$（$j=0,\\dots,m_i-1$），使 $\\pi$ 是 $I_L^{\\GL_n}(\\sigma)=I_P^{\\GL_n}(\\sigma)$ 的子商。",
                "why": "这一步把「$\\pi$ 在哪个 Bernstein 分量」翻译成「$\\sigma$ 的超尖点块 $\\pi_i$ 与段长 $m_i$」的显式数据。",
                "locator": "A p.33",
                "provenance": "A",
            },
            {
                "no": 2,
                "text": "由引理 1.9 与 3.1.7，$\\rec_n(\\pi)|_{I_K}=\\bigoplus_i\\rec_{n_i}(\\pi_i)^{m_i}|_{I_K}$：$\\SL_2$ 部分 $\\Sp_{m_i}$ 在 $I_K$ 上平凡，只剩各 $\\rec_{n_i}(\\pi_i)$ 重复 $m_i$ 次。",
                "why": "$P_K\\subset I_K$ 上 $\\Sp_m$ 平凡是这里的关键——惯性群看不到段长，只看到「哪些超尖点块、各几次」。",
                "locator": "A p.33",
                "provenance": "A",
            },
            {
                "no": 3,
                "text": "于是问题归到超尖点情形：$\\pi_i$ 超尖点时 $\\rec_{n_i}(\\pi_i)|_{I_K}$ 不可约（若 $\\pi_i$ 非超尖点则其 $\\rec$ 在 $I_K$ 上可约），两个超尖点的 $I_K$-限制同构 $\\iff$ 二者惯性等价。",
                "why": "超尖点 $\\Leftrightarrow$ $I_K$ 上不可约，这使「同构」变成「逐块配对」，避免了不可约分解的歧义。",
                "locator": "A p.33",
                "provenance": "A",
            },
            {
                "no": 4,
                "text": "对两个分量 $\\pi=Q(\\Delta_1..\\Delta_r)$、$\\pi'=Q(\\Delta'_1..\\Delta'_{r'})$，若 $\\rec_n(\\pi)|_{I_K}\\cong\\rec_n(\\pi')|_{I_K}$，则第 2–3 步给出块的多重集相同，即 $(L,\\sigma)$ 与 $(L',\\sigma')$ 惯性等价。",
                "why": "多重集相同正是惯性等价的定义（允许非分歧扭转与共轭），这一步完成「$\\Rightarrow$」。",
                "locator": "A p.34",
                "provenance": "A",
            },
            {
                "no": 5,
                "text": "反向：若惯性等价，取 $H=I_K$、$G=W_K$（$G/H\\cong\\mathbb Z$ 交换），引理 4.3 给出 $\\rec_n(\\pi')|_{I_K}\\cong\\rec_n(\\pi)|_{I_K}\\otimes\\psi$（$\\psi$ 为 $W_K/I_K$ 的特征标）；对每个块反复用「只需 $\\Hom_H(\\rho_1,\\rho_2)\\neq0$」的注把 $\\psi$ 吸收掉，得同构。",
                "why": "这是证明中最技术的一步：$\\psi$ 是非分歧扭转，在 $I_K$ 上平凡，故「吸收」不改变 $I_K$-限制——但也正因为如此，引理 4.4 才只能给出 $I_K$ 上的同构，而不能给出 $W_K$ 上的同构。",
                "locator": "A p.34",
                "provenance": "A",
            },
        ],
        result="$\\pi,\\pi'$ 同 Bernstein 分量 $\\iff$ $\\rec_n(\\pi)|_{I_K}\\cong\\rec_n(\\pi')|_{I_K}$。Bernstein 中心 $\\mathcal B(\\GL_n)$ 因此被 Weil–Deligne 惯性类型（$\\rho|_{I_K}$ 连同各块的重复数）索引。",
        gaps=[
            "第 3 步「超尖点 $\\Leftrightarrow$ $I_K$ 上不可约」底本未证，只引用。",
            "第 5 步「反复用注分离分量」底本写作一句断言，未给逐块的归纳。",
        ],
        pitfalls=[
            "第 2 步 $\\Sp_{m_i}$ 在 $I_K$ 上平凡，故 $m_i$ 只以「重复次数」出现；若把 $\\rec_n(\\pi)|_{I_K}$ 误算成含 $\\SL_2$ 结构就会多出 $m_i$ 的信息，与「Bernstein 中心不含段长」矛盾。",
            "第 5 步用引理 4.3 需要 $G/H$ 交换；$W_K/I_K\\cong\\widehat{\\mathbb Z}$ 确实交换，但 $W_K/P_K$ 不交换，换成野惯性群就不成立。",
            "$gL_1g^{-1}=L_2$ 中的 $g$ 是 $\\GL_n(K)$ 的元素（共轭），不是 $W_K$ 的元素；两个并存的「共轭」层次容易混。",
        ],
        related=[
            "yao17/concept/inertial-correspondence",
            "yao17/concept/bernstein-decomposition",
            "yao17/concept/bz-classification",
            "yao17/deriv/induction-to-supercuspidal",
        ],
        sources=[
            {
                "text": "A",
                "section": "§4.2.1（引理 4.4 的证明）",
                "pages": [33, 34],
                "quote": "Now we use the classification result of Bernstein–Zelevinsky",
                "anchor": "A p.33",
            }
        ],
        provenance_note="证明链依 p.33–p.34 的引理 4.4 整理；第 3 步的等价与第 5 步的逐块归纳是我们补的，已在 gaps 标出。",
        rights="rewritten",
        status="dev",
    )
