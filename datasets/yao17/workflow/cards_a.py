# -*- coding: utf-8 -*-
"""cards_a.py —— 轨 A：Weil–Deligne 侧（6 张概念卡）。"""


def add(mk):
    mk(
        id="yao17/concept/weil-group",
        type="concept",
        track="A",
        title="Weil 群 W_K、惯性群、野惯性群与驯特征标",
        aliases=["W_K", "Weil 群", "tame character", "驯特征标"],
        summary="W_K 是 I_K 与 Frobenius 整数幂的半直积；t 把 I_K/P_K 同构到 ∏_{l≠p} Z_l，共轭作用即分圆特征标。",
        question="底本怎么定义 W_K？驯特征标 t 与 l 进分圆特征标 χ_l 之间是什么关系？",
        definition={
            "text": "设 $K$ 是非阿基米德局部域，剩余特征 $p$，$q=\\#k=p^f$，$G_K=\\Gal(K^s/K)$。$W_K$ 由短正合列 $0\\to I_K\\to W_K\\to\\operatorname{Frob}^{\\mathbb Z}\\to 0$ 刻画，拓扑取成 $I_K$ 为开子群、$\\operatorname{Frob}^{\\mathbb Z}\\cong\\mathbb Z$ 离散——注意这不是从 $G_K$ 继承的子空间拓扑。野惯性 $P_K=G(K^s/K^t)$ 是 $I_K$ 唯一的 pro-$p$ Sylow 子群；驯特征标是 $t\\colon I_K/P_K\\xrightarrow{\\sim}\\prod_{l\\neq p}\\mathbb Z_l$，$\\sigma\\mapsto t(\\sigma)$ 由 $\\sigma(\\varpi_K^{1/n})/\\varpi_K^{1/n}=\\zeta_n^{t(\\sigma)}$ 确定（依赖单位根系统的选取）。",
            "notation": "$\\varpi_K$ 是素元，$K^{\\mathrm{nr}}=\\bigcup_{p\\nmid n}K(\\zeta_n)$，$K^t=\\bigcup_{p\\nmid n}K^{\\mathrm{nr}}(\\varpi_K^{1/n})$；$t_l$ 是 $t$ 投到 $\\mathbb Z_l$ 的分量。",
        },
        key_points=[
            "W_K 的拓扑是「人为」的：$I_K$ 开、$\\operatorname{Frob}^{\\mathbb Z}$ 离散，因此 W_K 不紧而只是局部紧；这一点决定了 W_K 的连续表示一定是「$I_K$ 上有限像 + Frobenius 可无限阶」，与 $G_K$ 的连续表示完全不同。",
            "$P_K$ 是 pro-$p$ 群，故任何 $l\\neq p$ 的 $\\mathbb Z_l$-模上 $P_K$ 的像都平凡——这就是驯特征标商掉 $P_K$ 的全部理由。",
            "$G_K$ 共轭作用保持 $P_K$（唯一 pro-$p$ Sylow），在每个 $\\mathbb Z_l$ 分量上给出 $l$ 进分圆特征标：$t_l(\\sigma\\tau\\sigma^{-1})=\\chi_l(\\sigma)t_l(\\tau)$，即 $I_{K,l}/P_K\\cong\\mathbb Z_l(1)$。",
            "底本 Remark 给了公理化定义：W_K 由三元组 $(W_K,\\iota,\\{r_E\\})$ 刻画，$\\iota$ 像稠密、$r_E\\colon C_E\\xrightarrow{\\sim}W_E^{\\mathrm{ab}}$，非阿局部情形下 $\\iota$ 就是自然包含、$r_E$ 来自局部类域论。",
        ],
        formulas=[
            "$0\\to I_K\\to W_K\\to\\operatorname{Frob}^{\\mathbb Z}\\to 0$",
            "$t\\colon I_K/P_K\\xrightarrow{\\ \\sim\\ }\\prod_{l\\neq p}\\mathbb Z_l,\\qquad t_l\\colon I_{K,l}/P_K\\xrightarrow{\\ \\sim\\ }\\mathbb Z_l$",
            "$t_l(\\sigma\\tau\\sigma^{-1})=\\chi_l(\\sigma)\\,t_l(\\tau)\\quad(\\sigma\\in G_K,\\ \\tau\\in I_{K,l})$",
        ],
        pitfalls=[
            "$W_K\\to G_K$ 的像稠密但不闭，故 W_K 的连续表示不一定给出 $G_K$ 的连续表示；把两者混同会丢掉「$I_K$ 上有限像」这一条。",
            "驯特征标依赖单位根系统 $\\{\\zeta_n\\}_{p\\nmid n}$ 的选取；换一套 $\\zeta_n$ 相当于乘一个 $\\widehat{\\mathbb Z}^{(p)}$ 中的单位，底本在 §1.2.2 明确说不同选取给出自然同构的 WD 函子。",
        ],
        related=[
            "yao17/concept/wd-representation",
            "yao17/concept/wd-functor",
            "yao17/concept/frobenius-semisimple",
        ],
        sources=[
            {
                "text": "A",
                "section": "§1.1.1–§1.1.2",
                "pages": [2, 2],
                "quote": "here W_K is topologized such that I_K ⊂ W_K is open with its usual topology and Frob^Z ≅ Z has the discrete topology",
                "anchor": "A p.2",
            }
        ],
        provenance_note="正合列、拓扑、$K^{\\mathrm{nr}}$/$K^t$ 与 $t$ 的定义照 p.2 的 1.1.1–1.1.2；「$W_K$ 的拓扑是人为的」这一句解释是我们的判断。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/wd-representation",
        type="concept",
        track="A",
        title="Weil–Deligne 表示 (ρ, N) 及其基本性质",
        aliases=["Weil-Deligne representation", "wd_K", "单值算子 N"],
        summary="(ρ,N) 中 ρ 是 I_K 上有限像的连续表示，N 满足 σNσ^{-1}=q^{-v_K(σ)}N；N 必幂零，半单情形下 (ρ,N)≅⊕Sp_m(r)。",
        question="Weil–Deligne 表示的定义里 N 的相容条件为什么会迫使 N 幂零？半单的 (ρ,N) 为什么一定是 Sp_m(r) 的直和？",
        definition={
            "text": "设 $L$ 特征 0，$V$ 是有限维 $L$-向量空间。$W_K$ 上的 Weil–Deligne 表示是一对 $(\\rho,N)$：(1) $\\rho$ 是 $W_K$ 的连续表示（$L$ 上离散拓扑，等价于 $\\rho(I_K)$ 有限像）；(2) $N\\in\\End(V)$ 满足 $\\sigma N\\sigma^{-1}=q^{-v_K(\\sigma)}N$，其中 $v_K$ 由 $\\sigma\\mapsto\\operatorname{Frob}_K^{v_K(\\sigma)}\\in W_K/I_K\\xrightarrow{\\sim}\\operatorname{Frob}^{\\mathbb Z}$ 定义。态射是兼容 $N$ 的表示态射，由此得到范畴 $\\wd=\\wd_L(W_K)$。",
            "notation": "对 Frobenius 提升 $\\phi\\in W_K$，条件化为 $\\phi N\\phi^{-1}=q^{-1}N$；$V(-1)$ 记 $V$ 用非分歧特征标 $\\epsilon\\colon G_K\\to L^\\times$（$\\phi\\mapsto q$）的扭转。",
        },
        key_points=[
            "N 幂零是「算出来」的：特征多项式满足 $f(X)=\\det(XI_n-N)=\\det(XI_n-q^{-1}N)=q^{-n}f(qX)$，比较次数与首项迫使 $f(X)=X^n$。",
            "N 不是 Galois 等变的，但它给出一个 Galois 等变的映射 $N(-1)\\colon V\\to V(-1)$——这是把「Frobenius 把 N 缩放 $q^{-1}$」翻译成「N 降低一个 Tate 扭转」的正确写法。",
            "$\\Sp_m(r)=r\\oplus r(1)\\oplus\\dots\\oplus r(m-1)$，$N$ 把 $r(i)$ 同构送到 $r(i+1)$、在 $r(m-1)$ 上为 0；等价地 $N(-1)$ 在 $r\\oplus\\dots\\oplus r(m-2)$ 上是恒等、在 $r(m-1)$ 上是 0。",
            "对 $N$ 的幂零指数做归纳可得：$\\rho$ 半单时 $(\\rho,N)\\cong\\bigoplus_i\\Sp_{m_i}(r_i)$，$r_i$ 是不可约表示且 $r_i(I_K)$ 有限。这是「$\\wd$ 里的对象 = Steinberg 块的直和」的原型。",
            "张量积 $(\\rho_1\\otimes\\rho_2,\\ N_1\\otimes\\mathrm{id}+\\mathrm{id}\\otimes N_2)$；$\\Hom(\\rho_1,\\rho_2)$ 上 $N\\phi=N_2\\phi-\\phi N_1$，即 $\\wd$ 是张量范畴。",
        ],
        formulas=[
            "$\\sigma N\\sigma^{-1}=q^{-v_K(\\sigma)}N,\\qquad \\phi N\\phi^{-1}=q^{-1}N$",
            "$\\Sp_m(r)=r\\oplus r(1)\\oplus\\dots\\oplus r(m-1)$",
            "$(\\rho,N)\\ \\text{半单}\\ \\Longrightarrow\\ (\\rho,N)\\cong\\bigoplus_i\\Sp_{m_i}(r_i)$",
            "$(\\rho_1\\otimes\\rho_2,\\ N_1\\otimes\\mathrm{id}+\\mathrm{id}\\otimes N_2)$",
        ],
        pitfalls=[
            "「$\\rho$ 连续」在底本的约定里等价于「$\\rho(I_K)$ 有限」，因为 $W_K$ 的拓扑不是子空间拓扑；若按一般拓扑群定义会把条件想放松。",
            "$\\wd$ 的半单对象不是「$\\rho$ 半单」的对象：$\\wd$ 的半单对象是那些 $N=0$ 且 $\\rho$ 半单的；$\\rho$ 半单但 $N\\neq 0$ 的 $\\Sp_m(r)$ 是「$\\phi$-半单但非半单」。",
        ],
        related=[
            "yao17/concept/weil-group",
            "yao17/concept/frobenius-semisimple",
            "yao17/concept/wd-invariants",
            "yao17/concept/wd-functor",
        ],
        sources=[
            {
                "text": "A",
                "section": "§1.1.3–§1.1.7",
                "pages": [3, 3],
                "quote": "A Weil-Deligne representation of W_K on V is a pair (ρ, N)",
                "anchor": "A p.3",
            }
        ],
        provenance_note="定义与基本性质 (1)–(4)、张量积与 Hom 取自 p.3 的 1.1.3–1.1.4 与 p.5 的 1.1.7；「N 幂零是算出来的」等解释是我们的判断。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/frobenius-semisimple",
        type="concept",
        track="A",
        title="φ-半单（Frobenius 半单）与引理 1.2",
        aliases=["φ-semisimple", "Frobenius-semisimple", "引理 1.2"],
        summary="在 ρ(I_K) 有限时，ρ 半单 ⇔ 任一 Frobenius 提升的半单性；由此把「φ-半单」定为 LLC 目标范畴的条件。",
        question="为什么「ρ 半单」可以换成「ρ(φ) 半单」来检验？这个等价用到了哪两条引理？",
        definition={
            "text": "引理 1.1：(1) $H\\triangleleft G$ 正规、$V$ 有限维，$\\rho$ 半单 $\\Rightarrow$ $\\rho|_H$ 半单；(2) $[G:H]=r$ 在系数域中可逆时，$\\rho$ 半单 $\\iff$ $\\rho|_H$ 半单。引理 1.2：设 $\\rho(I_K)$ 有限、$L$ 代数闭，则 (1) 所有 $\\rho(\\sigma)$ 半单；(2) 任一 Frobenius 提升 $\\rho(\\phi)$ 半单；(3) $\\rho$ 半单，三者等价。定义：$(\\rho,N)\\in\\wd_K$ 称 $\\phi$-半单（Frobenius 半单），若 $\\rho$ 半单（等价地 $\\rho(\\phi)$ 半单）。",
            "notation": "$\\rho^{\\mathrm{ss}}$ 是 $\\rho$ 的半单化；$(\\rho^{\\mathrm{ss}},N)$ 称 $(\\rho,N)$ 的 $\\phi$-半单化。",
        },
        key_points=[
            "引理 1.2 的关键一步是：$\\operatorname{im}\\rho(I_K)$ 有限，故对每个 $\\sigma$ 存在 $m>0$ 使 $\\rho(\\sigma^m)$ 落在 $\\rho(W_K)$ 的中心——于是 $\\rho(\\sigma^{n'})=\\rho(\\phi^n)$，把问题归到 $\\rho(\\phi)$ 上。",
            "「$T^{m}$ 半单 ⇔ $T$ 半单」只在特征 0 成立，底本特意点明：这正是引理要求 $\\operatorname{char}L=0$ 的原因，正特征下会失败。",
            "第二半用引理 1.1(2)：$\\langle\\rho(\\phi)\\rangle$ 在 $\\rho(W_K)$ 中有限指数，指数在特征 0 中可逆，故 $\\rho(W_K)$ 半单 ⇔ $\\langle\\rho(\\phi)\\rangle$ 半单。",
            "底本 Remark：$L$ 不必代数闭，此时把 (3) 换成「潜在半单」（换基后可对角化）；这也是为什么定义里写「$\\rho$ 半单」而实际检验用 $\\rho(\\phi)$。",
            "注记 (1)：$\\rho$ 不可约 $\\Rightarrow N=0$（$\\ker N$ 在 $W_K$ 下稳定）；注记 (2)：$\\phi$-半单的对象一般不是 $\\wd$ 的半单对象。",
        ],
        formulas=[
            "$\\rho\\ \\text{半单}\\iff \\rho(\\phi)\\ \\text{半单}\\iff \\rho(\\sigma)\\ \\text{半单}\\ \\forall\\sigma\\in W_K$",
            "$\\rho|_H\\ \\text{半单}\\ \\Longleftarrow\\ \\rho\\ \\text{半单}\\quad(H\\triangleleft G)$",
            "$\\rho(\\sigma^{n'})=\\rho(\\phi^{n})\\quad(\\text{用 }\\operatorname{im}\\rho(I_K)\\text{ 有限})$",
        ],
        theorems=[
            {
                "name": "引理 1.2（φ-半单的三等价）",
                "statement": "$\\rho(I_K)$ 有限、$L$ 代数闭时，$\\{\\rho(\\sigma)\\}_{\\sigma}$ 全半单、$\\rho(\\phi)$ 半单、$\\rho$ 半单三者等价。",
                "proof": {
                    "status": "sketch",
                    "gap_note": "底本只给 Sketch：先证每个 $\\sigma$ 的某次幂落在中心（用 $\\rho(I_K)$ 有限），再归到 $\\rho(\\phi)$，最后用引理 1.1(2)；「$T^m$ 半单 ⇔ $T$ 半单」的论证也略。",
                },
                "source": "A §1.1.6 p.4–p.5",
            }
        ],
        pitfalls=[
            "引理 1.2 要求 $L$ 代数闭；不代数闭时 (3) 要改成「潜在半单」，否则反例来自不可对角化的不可约 $L$-表示。",
            "$\\phi$-半单时 $N$ 可以非零（$\\Sp_m(r)$ 就是），所以「$\\phi$-半单」不是「$N=0$」；两个条件在定理 2.13 的说法里分别由「Frobenius 半单」与「$N=0$」承担。",
        ],
        related=[
            "yao17/concept/wd-representation",
            "yao17/concept/wd-functor",
            "yao17/concept/llc-statement",
        ],
        sources=[
            {
                "text": "A",
                "section": "§1.1.5–§1.1.6",
                "pages": [4, 5],
                "quote": "A Weil-Deligne representation (ρ, N) ∈ wd_K is ϕ-semisimple (Frobenius-semisimple) if ρ is semisimple, or equivalently, if ρ(ϕ) is semisimple",
                "anchor": "A p.5",
            }
        ],
        provenance_note="引理 1.1/1.2 与 $\\phi$-半单的定义照 p.4–p.5；「为什么要求特征 0」与中心化论证的要点见 p.4 的 Sketch，解释部分是我们的判断。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/tate-epsilon",
        type="concept",
        track="A",
        title="Tate 的局部 L 因子与 ε 因子、定理 1.3 的存在唯一性",
        aliases=["Tate's thesis", "ε-factor", "L-factor", "定理 1.3"],
        summary="Tate 对拟特征标给出 L(χ) 与显式 ε(χ,ψ,dx)；Langlands 把它唯一延拓到 W_K 的表示上，要求对特征是 Tate 的、短正合列乘性、0 次归纳。",
        question="Tate 的 ε 因子显式公式长什么样？定理 1.3 用哪三条公理把特征标情形唯一地延拓到高维表示？",
        definition={
            "text": "对拟特征标 $\\chi\\colon K^\\times\\to\\mathbb C$，Tate 定义 $L(\\chi)=(1-\\chi(\\varpi))^{-1}$（$\\chi$ 非分歧），否则 $1$。固定非平凡加性特征标 $\\psi$ 与 Haar 测度 $dx$，令 $d^\\ast x=\\|x\\|^{-1}dx$、$\\chi^\\vee=\\chi^{-1}\\|\\cdot\\|$，则 Fourier 变换给出函数方程 $\\int\\hat f\\chi^\\vee d^\\ast x/L(\\chi^\\vee)=\\epsilon(\\chi,\\psi,dx)\\int f\\chi\\,d^\\ast x/L(\\chi)$。显式地，取 $c\\in K^\\times$ 使 $v(c)=n(\\psi)+c(\\chi)$，则 $\\epsilon(\\chi,\\psi,dx)=\\|c\\|^{-1}\\chi(c)\\operatorname{Vol}_{dx}(\\mathcal O_K)$（非分歧）或 $\\int_{c^{-1}\\mathcal O_K^\\times}\\chi^{-1}(x)\\psi(x)dx$（分歧）。",
            "notation": "$n(\\psi)$ 是使 $\\psi(\\varpi^{-n}\\mathcal O_K)=1$ 的最大整数（导子指数），$c(\\chi)$ 是 $\\chi$ 的导子；定理 1.3 的 $\\epsilon(\\cdot,\\psi,dx)$ 在 $R(W_K)=K_0(\\Rep W_K)$ 上有定义。",
        },
        key_points=[
            "Tate 的定理只管 $\\GL_1$（即特征标）；高维时的 $\\epsilon$ 不能靠积分显式写出，只能由公理刻画——这就是定理 1.3 的角色：Langlands 证明存在、Deligne 给短证明。",
            "公理 (2)「短正合列乘性」说明 $\\epsilon$ 其实只依赖 $R(W_K)$ 里的类；这条加上 (1) 就足以把 $\\epsilon$ 从特征标推到所有可约表示，是整套构造的引擎。",
            "公理 (3)「0 次归纳性」$\\epsilon(\\mathrm{ind}_{E/L}[r],\\psi\\circ\\Tr_{L/K},\\mu_L)=\\epsilon([r],\\psi\\circ\\Tr_{E/K},\\mu_E)$ 是唯一性最吃劲的一条：它把不同扩域上的构造钉在一起。",
            "$n(\\psi)$ 与 $c(\\rho)$ 一起出现的那条公式 $\\epsilon(\\rho\\omega_s,\\psi,dx)=(\\#k)^{-(c(\\rho)+n(\\psi)\\dim V)s}\\epsilon(\\rho,\\psi,dx)$ 是后面 §3.6 里 JPPS 公式的原型。",
        ],
        formulas=[
            "$L(\\chi)=(1-\\chi(\\varpi))^{-1}\\ (\\chi\\ \\text{非分歧}),\\qquad L(\\chi)=1\\ (\\chi\\ \\text{分歧})$",
            "$\\frac{\\int\\hat f\\chi^\\vee\\,d^\\ast x}{L(\\chi^\\vee)}=\\epsilon(\\chi,\\psi,dx)\\cdot\\frac{\\int f\\chi\\,d^\\ast x}{L(\\chi)}$",
            "$\\epsilon(\\chi,\\psi,dx)=\\|c\\|^{-1}\\chi(c)\\operatorname{Vol}_{dx}(\\mathcal O_K)\\ (\\text{非分歧}),\\qquad \\int_{c^{-1}\\mathcal O_K^\\times}\\chi^{-1}(x)\\psi(x)\\,dx\\ (\\text{分歧})$",
        ],
        theorems=[
            {
                "name": "定理 1.3（Langlands；Deligne 有短证明）",
                "statement": "存在唯一函数 $\\epsilon$ 把 $(K,\\rho,\\psi,dx)$ 送成 $\\epsilon(\\rho,\\psi,dx)\\in\\mathbb C^\\times$，使得 (1) 对特征是 Tate 的 $\\epsilon$；(2) 对 $W_K$ 表示的短正合列乘性，从而下降到 $R(W_K)\\to\\mathbb C^\\times$；(3) 对 0 次类满足归纳性。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本引 [10] 只给存在性定理，未写证明；Deligne 的短证明也未展开。",
                },
                "source": "A §1.1.10 p.6",
            }
        ],
        pitfalls=[
            "$\\epsilon$ 依赖 $\\psi$ 与 $dx$；底本在 (3) 里连测度一起变换（$\\mu_L$ 对 $\\mu_E$），否则归纳性不成立。",
            "底本 Remark 明确说它的 $\\epsilon$ 与 [10]（Tate）差一个因子 $q^{n(\\psi)\\dim V\\cdot s}$：Tate 把它叫 $\\epsilon$，本文的约定与 [11] 一致。读文献时必须先对齐这个惯例，否则 $\\epsilon$ 差一个 $q$ 的幂。",
        ],
        related=[
            "yao17/concept/wd-invariants",
            "yao17/concept/conductor-depth",
            "yao17/concept/weil-group",
        ],
        sources=[
            {
                "text": "A",
                "section": "§1.1.10",
                "pages": [6, 6],
                "quote": "There exists a unique function ϵ which associates a number ϵ(ρ, ψ, dx) ∈ C^× to each choice of local field K, a representation ρ of W_K",
                "anchor": "A p.6",
            }
        ],
        provenance_note="Tate 的 $L$/$\\epsilon$ 与显式公式、定理 1.3 的三条公理照 p.6；「公理 (2) 是引擎」「(3) 是唯一性最吃劲的一条」是我们的判断。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/wd-invariants",
        type="concept",
        track="A",
        title="Weil–Deligne 表示的导子 c(ρ)、L 因子与 ε 因子",
        aliases=["c(ρ)", "Artin conductor", "推论 1.4"],
        summary="c(ρ)=c(ρ')+dim V^{I_K}−dim(ker N)^{I_K}；L 与 ε 只用 (ker N)^{I_K} 与 V^{I_K}/(ker N)^{I_K} 上的 Frobenius 作用。",
        question="N 怎样进入导子、L 因子与 ε 因子的定义？为什么 ε 的显式因子只依赖 (ker N)^{I_K} 与 V^{I_K}/(ker N)^{I_K}？",
        definition={
            "text": "设 $\\rho=(\\rho',N)$ 是 $W_K$ 的 Weil–Deligne 表示，$q=\\#k$。(1) 导子 $c(\\rho):=c(\\rho')+\\dim V^{I_K}-\\dim(\\ker N)^{I_K}$，其中 $c(\\rho')$ 是 Artin 导子 $c(\\chi_{\\rho'})=\\sum_i\\frac{1}{[G_0:G_i]}(\\dim V-\\dim V^{G_i})$；(2) 取几何 Frobenius $\\Phi$，$L(\\rho,s):=\\det\\big(1-q^{-s}\\Phi|_{(\\ker N)^{I_K}}\\big)^{-1}$；(3) $\\epsilon(\\rho,s,\\psi):=q^{-(c(\\rho)+n(\\psi)\\dim V)s}\\cdot\\det\\big(-\\Phi|_{V^{I_K}/(\\ker N)^{I_K}}\\big)\\cdot\\epsilon(\\rho',\\psi,dx)$。",
            "notation": "$G_i$ 是 $I_K$ 的第 $i$ 个分歧子群；$n(\\psi)$ 是 $\\psi$ 的导子指数；$\\epsilon(\\rho',\\psi,dx)$ 是定理 1.3 对 $W_K$ 表示给的因子。",
        },
        key_points=[
            "N 的作用被「夹在 $I_K$-不变量与 $\\ker N$ 之间」：导子只数 $V^{I_K}$ 比 $(\\ker N)^{I_K}$ 多出的部分，L 因子只看 $(\\ker N)^{I_K}$，$\\epsilon$ 的显式行列式因子只在商 $V^{I_K}/(\\ker N)^{I_K}$ 上。",
            "推论 1.4 把这个定义压成一行：$\\epsilon(\\rho,s,\\psi)=q^{-(c(\\rho)+n(\\psi)\\dim V)s}\\epsilon(\\rho,0,\\psi)$，即 $\\epsilon$ 关于 $s$ 是纯指数——这正是 §3.6 里 JPPS 公式的来源。",
            "对 $\\rho'$ 用 Artin 导子公式时，$\\dim V-\\dim V^{G_i}$ 的权 $1/[G_0:G_i]$ 是 Artin 的原始归一化；底本在 Remark 里把它和 $\\epsilon$ 的指数因子并排写出，正是为了说明两者指数相同。",
            "当 $(\\rho,N)$ 来自 $\\ell$ 进表示时，这套 $c,L,\\epsilon$ 与定理 1.3 给 $\\rho'$ 的因子相容——所以 LLC 的性质 (2) 可以直接在这套量上陈述。",
        ],
        formulas=[
            "$c(\\rho)=c(\\rho')+\\dim V^{I_K}-\\dim(\\ker N)^{I_K}$",
            "$L(\\rho,s)=\\det\\big(1-q^{-s}\\Phi|_{(\\ker N)^{I_K}}\\big)^{-1}$",
            "$\\epsilon(\\rho,s,\\psi)=q^{-(c(\\rho)+n(\\psi)\\dim V)s}\\det\\big(-\\Phi|_{V^{I_K}/(\\ker N)^{I_K}}\\big)\\epsilon(\\rho',\\psi,dx)$",
            "$\\epsilon(\\rho,s,\\psi)=q^{-(c(\\rho)+n(\\psi)\\dim V)s}\\epsilon(\\rho,0,\\psi)$",
        ],
        theorems=[
            {
                "name": "推论 1.4",
                "statement": "$\\epsilon(\\rho,s,\\psi)=q^{-(c(\\rho)+n(\\psi)\\dim V)s}\\epsilon(\\rho,0,\\psi)$。",
                "proof": {
                    "status": "complete",
                    "steps": [
                        {
                            "no": 1,
                            "text": "把 $\\epsilon(\\rho,s,\\psi)$ 的定义代入，只需认出显式因子 $q^{-(c(\\rho)+n(\\psi)\\dim V)s}$ 之外的部分正是 $s=0$ 时的表达式。",
                            "why": "定义里只有指数因子带 $s$；$\\det(-\\Phi|_{\\cdot})$ 与 $\\epsilon(\\rho',\\psi,dx)$ 都与 $s$ 无关。",
                        },
                        {
                            "no": 2,
                            "text": "故 $\\epsilon(\\rho,s,\\psi)=q^{-(c(\\rho)+n(\\psi)\\dim V)s}\\cdot\\epsilon(\\rho,0,\\psi)$。",
                            "why": "底本称其为「从定义直接读出的平凡推论」（Corollary）。",
                        },
                    ],
                },
                "source": "A §1.1.11 p.7",
            }
        ],
        pitfalls=[
            "这里用的是「几何 Frobenius」$\\Phi$；若换成算术 Frobenius，$L$ 因子里的 $q^{-s}$ 要改成 $q^{s}$，符号会翻转。",
            "$c(\\rho)$ 里第二项是 $\\dim V^{I_K}-\\dim(\\ker N)^{I_K}$，不是 $\\dim V-\\dim\\ker N$；$I_K$-不变子空间这一限制不能省，否则与 $\\ell$ 进侧不兼容。",
        ],
        related=[
            "yao17/concept/tate-epsilon",
            "yao17/concept/wd-representation",
            "yao17/concept/conductor-depth",
            "yao17/concept/llc-statement",
        ],
        sources=[
            {
                "text": "A",
                "section": "§1.1.11",
                "pages": [7, 7],
                "quote": "c(ρ) := c(ρ′) + dim V^{I_K} − dim(ker N)^{I_K}",
                "anchor": "A p.7",
            }
        ],
        provenance_note="(1)–(3) 与推论 1.4 逐条照 p.7；Artin 导子公式见 p.6 Remark；key_points 中「N 的作用被夹在…之间」是我们的概括。",
        rights="rewritten",
        status="dev",
    )

    mk(
        id="yao17/concept/wd-functor",
        type="concept",
        track="A",
        title="Grothendieck 单值化定理、WD 函子与惯性类型",
        aliases=["WD(ρ)", "引理 1.5", "推论 1.7", "inertia type"],
        summary="引理 1.5 把 ℓ 进表示化成 exp(t_ℓ(σ)N)；推论 1.7 的 WD 函子给出 Rep_L(G_K)≃wd^{ℓ-int}，惯性类型则丢掉 N 只留 I_K 上的结构。",
        question="Grothendieck 的准单值化定理怎么把 l 进表示变成 Weil–Deligne 表示？「惯性类型」为什么要分成 WD 型与 Galois 型两种？",
        definition={
            "text": "引理 1.5：$\\rho\\colon G_K\\to\\GL(V)$ 是 $\\ell$ 进表示（$L/\\mathbb Q_\\ell$ 有限，$\\ell\\neq p$），则 (1) 存在开子群 $I_K'\\subset I_K$（对应有限扩张 $K'/K$）与唯一幂零 $N\\in\\End(V)$，使 $\\rho(\\sigma)=\\exp(t_\\ell(\\sigma)N)$ 对 $\\sigma\\in I_K'$ 成立；(2) 对 $\\tau=\\sigma\\phi^n$，$\\rho(\\tau)N\\rho(\\tau)^{-1}=q^{-n}N$。推论 1.7：$\\WD=\\WD_{\\zeta,\\phi}\\colon\\Rep_L(G_K)\\to\\wd^{\\ell\\text{-int}}_L(W_K)$ 是范畴等价，$\\WD(\\rho)=(\\rho',N)$，$\\rho'(\\sigma\\phi^n)=\\rho(\\sigma\\phi^n)\\exp(-t_\\ell(\\sigma)N)$。",
            "notation": "$\\ell$ 整（$\\ell$-bounded）指 $r(\\phi)$ 的特征多项式系数在 $\\mathcal O_L$ 中、$\\det r(\\phi)\\in\\mathcal O_L^\\times$；惯性类型见下。",
        },
        key_points=[
            "引理 1.5 的证明骨架：$G_K$ 连续地稳定一个 $\\mathcal O_L$ 格 $\\Lambda$，模 $\\ell$ 得 $\\rho\\colon G_K\\to\\Aut(\\Lambda/\\ell)$，核 $G_{K''}$ 有限指数；模 $\\ell$ 的核是 pro-$\\ell$，故 $\\rho|_{I_{K''}}$ 经 $t_\\ell\\colon I_{K''}\\to\\mathbb Z_\\ell(1)$ 分解，取拓扑生成元 $\\sigma$ 后 $N=\\log\\rho(\\sigma)$。",
            "推论 1.6：$\\rho$ 半单 $\\Rightarrow$ $\\rho(I_K)$ 有限——用引理 1.1(1) 把 $\\rho|_{I_K}$ 化到 $\\rho|_{I_K'}$，后者既半单又幂幺故为恒等。",
            "推论 1.8：$\\rho$（可能换基后）半单 $\\iff$ $\\rho$ $\\phi$-半单且 $\\rho(I_K)$ 有限 $\\iff$ $\\rho'$ $\\phi$-半单且 $N=0$。这把 §1.1 的抽象定义与 §1.2 的 $\\ell$ 进侧接上。",
            "惯性类型是「丢掉 $N$」的产物：WD 惯性类型 $\\tau=\\rho'|_{I_K}$ 有有限像、不含单值信息；Galois 惯性类型 $\\xi=\\rho|_{I_K}$ 要求 $\\rho$ 连续延拓到 $W_K$。引理 1.9：(1) $\\tau\\cong\\tau'$ $\\iff$ 不可约分量（带重数）在非分歧扭转下一致；(2) $\\xi\\cong\\xi'$ $\\iff$ 块重数 $m_i=m_i'$ 且 $r_i\\cong r_i'\\otimes\\eta_i$。",
        ],
        formulas=[
            "$\\rho(\\sigma)=\\exp(t_\\ell(\\sigma)N)\\quad(\\sigma\\in I_K'),\\qquad \\rho(\\tau)N\\rho(\\tau)^{-1}=q^{-n}N$",
            "$\\WD(\\rho)=(\\rho',N),\\qquad \\rho'(\\sigma\\phi^n)=\\rho(\\sigma\\phi^n)\\exp(-t_\\ell(\\sigma)N)$",
            "$\\rho\\ \\text{半单}\\iff \\rho\\ \\phi\\text{-半单且}\\ \\rho(I_K)\\ \\text{有限}\\iff \\rho'\\ \\phi\\text{-半单且}\\ N=0$",
        ],
        theorems=[
            {
                "name": "引理 1.5（Grothendieck 准单值化）",
                "statement": "任一 $\\ell$ 进表示 $\\rho\\colon G_K\\to\\GL(V)$ 在某个开子群 $I_K'$ 上单值化：$\\rho(\\sigma)=\\exp(t_\\ell(\\sigma)N)$，且 $N$ 在 $W_K$ 共轭下按 $q^{-n}$ 缩放。",
                "proof": {
                    "status": "sketch",
                    "gap_note": "底本只给 Sketch（模 $\\ell$ 把像化到有限群、再用分圆特征标定出 $N$）；唯一性与「$\\log$ 良定义」的细节未写。",
                },
                "source": "A §1.2.1 p.7–p.8",
            },
            {
                "name": "推论 1.7（WD 函子的范畴等价）",
                "statement": "$\\WD_{\\zeta,\\phi}\\colon\\Rep_L(G_K)\\to\\wd^{\\ell\\text{-int}}_L(W_K)$ 是范畴等价。",
                "proof": {
                    "status": "cited",
                    "gap_note": "底本只说「由上两条推论」，未写逆函子的构造与自然同构的验证。",
                },
                "source": "A §1.2.2 p.8",
            },
        ],
        pitfalls=[
            "WD 依赖 $\\zeta$ 与 $\\phi$ 的选取，但底本 Remark (1) 说不同选取给出自然同构的函子——所以「等价」是函子意义下的，不能取某个具体 $\\WD$ 当唯一。",
            "引理 1.9(1) 的「非分歧扭转下一致」是在段 $r_i$ 这一层比较，而不是在 $\\tau$ 上比较；WD 惯性类型不区分 $\\Sp_m$ 的块结构，Galois 惯性类型才区分。",
        ],
        related=[
            "yao17/concept/wd-representation",
            "yao17/concept/frobenius-semisimple",
            "yao17/deriv/wd-from-galois",
            "yao17/concept/inertial-correspondence",
        ],
        sources=[
            {
                "text": "A",
                "section": "§1.2.1–§1.2.3",
                "pages": [7, 9],
                "quote": "WD(ρ) = (ρ′, N),  ρ′(σϕ^n) := ρ(σϕ^n) exp(−t_l(σ)N)",
                "anchor": "A p.8",
            }
        ],
        provenance_note="引理 1.5、推论 1.6/1.7/1.8 与惯性类型定义、引理 1.9 取自 p.7–p.9；证明骨架拆自 p.7 的 Sketch，属我们的归纳。",
        rights="rewritten",
        status="dev",
    )
