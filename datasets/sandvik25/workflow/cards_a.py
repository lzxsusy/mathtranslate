#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cards_a.py —— 轨道 A：中心层与 Wakimoto 层（§2）。"""
from gen_cards import CARDS, card, src, PKG, write_cards

A = {}

A["concepts/antispherical-module"] = card(
    "concepts", "antispherical-module",
    title="反球模 $M^{\\mathrm{asph}}$",
    aliases=["antispherical module", "符号诱导模", "M^asph"],
    track="A",
    summary="把 $\\mathbb Z$ 沿 $W$ 的符号表示诱导到延长仿射 Weyl 群：$M^{\\mathrm{asph}}=\\mathbb Z\\otimes_{\\mathbb Z[W]}\\mathbb Z[W_{\\mathrm{ext}}]$。它是整篇文章的「靶子」。",
    question="反球模是怎么由符号表示诱导出来的，为什么叫「反球」？",
    definition={
        "text": "$G$ 是 $\\mathbb F_p$ 上的连通约化群，$B\\subset G$ 为 Borel，$T$ 为极大环面，$W_{\\mathrm{ext}}=W\\ltimes X^\\vee$ 为延长仿射 Weyl 群。令 $\\mathbb Z[W]$ 通过符号表示作用在 $\\mathbb Z$ 上，定义右 $\\mathbb Z[W_{\\mathrm{ext}}]$-模 $M^{\\mathrm{asph}}:=\\mathbb Z\\otimes_{\\mathbb Z[W]}\\mathbb Z[W_{\\mathrm{ext}}]$。",
        "notation": "$W$ 有限 Weyl 群，$X^\\vee$ 余根格；$\\ell$ 是 $W_{\\mathrm{ext}}$ 上准 Coxeter 结构的长度函数。",
    },
    key_points=[
        "「反球」指的是取符号表示（而非平凡表示）：球（spherical）情形用平凡表示，反球用符号表示，两者的 Hecke 模对偶。",
        "这个模的 $K_0$ 同时作用于三个几何对象（反球 Hecke 范畴、Springer 解消上的凝聚层、IW 层），所以它是三条范畴化路线的公共骨架。",
        "式 (2) 的 $[\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})]\\cong M^{\\mathrm{asph}}$ 不是显然的：它把「符号表示」翻成「$\\wedge$-幂的符号」，再靠 Springer 解消的几何把它实现。",
        "模层面只有一个对象，范畴化之后变成「每个 $V\\in\\mathrm{Rep}(G^\\vee)$ 一个对象」；从模到范畴的这一步正是 [ArBe] 的工作。",
    ],
    formulas=[
        "$M^{\\mathrm{asph}}:=\\mathbb Z\\otimes_{\\mathbb Z[W]}\\mathbb Z[W_{\\mathrm{ext}}]$",
        "$[\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})]\\cong M^{\\mathrm{asph}}$",
    ],
    theorems=[
        {
            "name": "式 (2)：$K$ 群同构",
            "statement": "$G^\\vee$-等变 Springer 解消上凝聚层的 Grothendieck 群同构于 $M^{\\mathrm{asph}}$。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文只引用，不证；这是 [ArBe] 与几何表示论的既有结果，本译本未补。",
            },
            "source": "A p.1",
        }
    ],
    pitfalls=[
        "不要把 $M^{\\mathrm{asph}}$ 与仿射 Hecke 代数混为一谈：前者是 $\\mathbb Z[W_{\\mathrm{ext}}]$ 上的模，后者是 $W_{\\mathrm{ext}}$ 的群代数本身。",
        "$\\mathbb Z$ 上的符号表示要求 $W$ 的生成元都作用为 $-1$，若误用平凡表示会得到球模而不是反球模。",
    ],
    related=[
        f"{PKG}/concept/three-categorifications",
        f"{PKG}/concept/springer-resolution",
        f"{PKG}/concept/wakimoto-sheaves",
    ],
    sources=[src([1, 1], "A p.1", "§1")],
    provenance_note="定义与式 (2) 出自 p.1；「反球=符号诱导」的解读见原文 §2.6 反球商的构造。",
)

A["concepts/nearby-cycles"] = card(
    "concepts", "nearby-cycles",
    title="附近循环函子 $\\Psi_f$",
    aliases=["nearby cycles", "特殊化函子", "vanishing cycles 的邻居"],
    track="A",
    summary="对 $f\\colon X\\to\\mathbb C$，把 $X^\\times=f^{-1}(\\mathbb C^\\times)$ 上的层拉回、经万有覆盖、再取特殊纤维：$\\Psi_f\\mathcal F=(i^*j_*\\exp_{X*}\\exp_X^*\\mathcal F)[-1]$。",
    question="附近循环函子怎么定义，它的五条函子性质各自负责后面的哪一步？",
    definition={
        "text": "设 $X$ 为复代数簇，$f\\colon X\\to\\mathbb C$ 为代数映射，$X^\\times=f^{-1}(\\mathbb C^\\times)$、$X^0=f^{-1}(0)$。取指数映射 $\\exp\\colon\\mathbb C\\to\\mathbb C^\\times$ 与纤维积 $\\widetilde X^\\times=X\\times_{\\mathbb C^\\times}\\mathbb C$，得交换图 (3)。定义 $\\Psi_f\\colon\\mathcal D^b_c(X^\\times)\\to\\mathcal D^b_c(X^0)$，$\\mathcal F\\mapsto(i^*j_*\\exp_{X*}\\exp_X^*\\mathcal F)[-1]$。",
        "notation": "$i\\colon X^0\\hookrightarrow X$、$j\\colon X^\\times\\hookrightarrow X$ 为包含；系数取特征 $0$ 代数闭域 $k$。",
    },
    key_points=[
        "定义里三层拉回–推前不是装饰：$\\exp$ 把 $\\mathbb C^\\times$ 的万有覆盖摊开，$j_*$ 把 $X^\\times$ 上的层延到 $X$，$i^*$ 再取到特殊纤维——这正是「局部系统单值」的几何版本。",
        "命题 2.2.2(2) 的 perverse $t$-正合性是中心函子能落在反常层里的唯一原因；没有它，$Z(F)$ 不知落在哪个三角范畴的哪一层。",
        "命题 2.2.2(4) 的紧合基变换是定理 2.4.1(5)（$\\pi_*Z(F)\\cong F$）的全部内容：把 $\\varpi\\colon\\mathrm{Gr}^{\\mathrm{cen}}_G\\to\\mathrm{Gr}_G\\times\\mathbb C$ 当紧合映射用。",
        "命题 2.2.2(5) 说常层沿投影的特殊化是常层，这是计算 $\\Psi_{\\mathrm{pr}_2}$ 的唯一显式工具。",
        "(1) 之所以要单独列出，是因为 $\\exp_X$ 不是代数映射，故「有界可构造」并非自动保持。",
    ],
    formulas=[
        "$\\Psi_f\\mathcal F:=(i^*j_*\\exp_{X*}\\exp_X^*\\mathcal F)[-1]$",
        "$\\Psi_f(\\mathcal F\\boxtimes k_{\\mathbb C^\\times}[1])\\cong\\mathcal F$（$f$ 为投影）",
    ],
    theorems=[
        {
            "name": "命题 2.2.2（五条性质）",
            "statement": "(1) 有界可构造复形映到有界可构造复形；(2) 是 perverse $t$-正合的；(3) 光滑基变换相容；(4) 紧合基变换相容；(5) 沿投影的常层特殊化为原层。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文只列性质并注明「不显然，因为 $\\exp_X$ 不是代数映射」，证明交给 SGA 与 [AcRi]。",
            },
            "source": "A p.3",
        }
    ],
    pitfalls=[
        "定义里的 $[-1]$ 位移不能省：它把「单值的对数」摆到与权格相同的次数上，定理 2.4.1(2) 的 $t$-正合性依赖它。",
        "$\\widetilde X^\\times$ 是解析空间而非代数簇（原文脚注 2）：凡是引用代数几何定理的地方都要绕开它，只能用 $\\exp$ 的解析性质。",
    ],
    related=[
        f"{PKG}/concept/central-affine-grassmannian",
        f"{PKG}/concept/gaitsgory-central-functor",
        f"{PKG}/deriv/nearby-cycles-to-central",
    ],
    sources=[src([2, 3], "A p.2", "§2.2")],
    provenance_note="定义与命题逐条对应 p.2–3；交换图 (3) 在 p.2。",
)

A["concepts/central-affine-grassmannian"] = card(
    "concepts", "central-affine-grassmannian",
    title="中心仿射 Grassmann 簇 $\\mathrm{Gr}^{\\mathrm{cen}}_G$",
    aliases=["central affine Grassmannian", "形变到仿射旗簇", "Gr^cen"],
    track="A",
    summary="一个带正则映射 $f\\colon\\mathrm{Gr}^{\\mathrm{cen}}_G\\to\\mathbb C$ 的 ind-概形：一般纤维是 $\\mathrm{Gr}_G$、特殊纤维是 $\\mathrm{Fl}_G$，于是「仿射 Grassmann 簇形变到仿射旗簇」。",
    question="中心仿射 Grassmann 簇的两条纤维各是什么，为什么它能同时承载仿射 Grassmann 簇与仿射旗簇？",
    definition={
        "text": "$\\mathrm{Gr}^{\\mathrm{cen}}_G$ 是带正则映射 $f$ 的 ind-概形，满足 $f^{-1}(\\mathbb C^\\times)=\\mathrm{Gr}_G\\times\\mathbb C^\\times$ 与 $f^{-1}(0)=\\mathrm{Fl}_G$。原文把 $f^{-1}(\\mathbb C^\\times)=\\mathrm{Gr}_G\\times\\mathbb C^\\times$ 与 $f^{-1}(0)=\\mathrm{Fl}_G$ 两式并列（原文第二个 $\\mathrm{Gr}^{\\mathrm{cen},\\times}_G$ 应为 $\\mathrm{Gr}^{\\mathrm{cen},0}_G$ 的排版笔误），并以之作为「$\\mathrm{Gr}_G$ 到 $\\mathrm{Fl}_G$ 的形变」。",
        "notation": "$\\mathrm{Gr}_G=LG/L^+G$、$\\mathrm{Fl}_G=LG/I$（fppf 层化）；$I$ 为对应 $B^-$ 的 Iwahori 子群。",
    },
    key_points=[
        "整个构造的几何直觉：一般纤维上只有 $L^+G$ 的等变性、特殊纤维上多出 $I$ 的等变性，于是「从 $\\mathrm{Gr}$ 走到 $\\mathrm{Fl}$」= 从球等变降到 Iwahori 等变，正是 $p$ 进侧「从球 Hecke 走到 Iwahori Hecke」的几何翻译。",
        "它必须存在为一个**单一** ind-概形，否则附近循环无从谈起；原文脚注 5 说它可写成 $\\mathbb A^1$ 上有限维簇的归纳极限。",
        "一般纤维是乘积 $\\mathrm{Gr}_G\\times\\mathbb C^\\times$ 而不是 $\\mathrm{Gr}_G$：多出的 $\\mathbb C^\\times$ 正是 $\\exp$ 的万有覆盖方向，$\\Psi_f$ 的 $[-1]$ 位移就落在这里。",
        "定理 2.4.1(5) 用的映射 $\\varpi\\colon\\mathrm{Gr}^{\\mathrm{cen}}_G\\to\\mathrm{Gr}_G\\times\\mathbb C$ 不是 $f$：$\\varpi$ 在 $\\mathbb C^\\times$ 纤维上是恒等、在 $0$ 纤维上退化为 $\\pi\\colon\\mathrm{Fl}_G\\to\\mathrm{Gr}_G$。",
    ],
    formulas=[
        "$\\mathrm{Gr}^{\\mathrm{cen},\\times}_G=f^{-1}(\\mathbb C^\\times)=\\mathrm{Gr}_G\\times\\mathbb C^\\times$",
        "$\\mathrm{Gr}^{\\mathrm{cen},0}_G=f^{-1}(0)=\\mathrm{Fl}_G$",
    ],
    theorems=[],
    pitfalls=[
        "原文 p.3 把特殊纤维一行也印成 $\\mathrm{Gr}^{\\mathrm{cen},\\times}_G$，这是笔误；按上下文应为 $f^{-1}(0)=\\mathrm{Fl}_G$。译本已改正并在译注中注明。",
        "别把 $\\mathrm{Gr}^{\\mathrm{cen}}_G$ 当成 $\\mathrm{Gr}_G\\times\\mathbb C$：后者的一般纤维是 $\\mathrm{Gr}_G$、特殊纤维也是 $\\mathrm{Gr}_G$，没有退化到 $\\mathrm{Fl}_G$。",
    ],
    related=[
        f"{PKG}/concept/nearby-cycles",
        f"{PKG}/concept/gaitsgory-central-functor",
    ],
    sources=[src([3, 3], "A p.3", "§2.4")],
    provenance_note="两条纤维式出自 p.3；$\\varpi$ 的构造在 p.4 定理 2.4.1 的证明里。",
)

A["concepts/gaitsgory-central-functor"] = card(
    "concepts", "gaitsgory-central-functor",
    title="Gaitsgory 中心函子 $Z$",
    aliases=["中心函子", "Z functor", "central functor"],
    track="A",
    summary="$Z(\\mathcal F)=\\Psi_f(\\mathcal F\\boxtimes k_{\\mathbb C^\\times}[1])$ 把 $L^+G$-等变层送到 $I$-等变层；定理 2.4.1 说它幺半、$t$-正合、像落在中心，且 $\\pi_*Z(\\mathcal F)\\cong\\mathcal F$。",
    question="中心函子怎么定义，「像落在中心」这条性质为什么是整篇文章的枢纽？",
    definition={
        "text": "由中心仿射 Grassmann 簇上的附近循环定义 $Z\\colon\\mathcal D^b_c(\\mathrm{Gr}_G)\\to\\mathcal D^b_c(\\mathrm{Fl}_G)$，$\\mathcal F\\mapsto\\Psi_f(\\mathcal F\\boxtimes k_{\\mathbb C^\\times}[1])$；再升级为等变版本 $Z\\colon\\mathcal D^b_c(L^+G\\backslash\\mathrm{Gr}_G)\\to\\mathcal D^b_c(I\\backslash\\mathrm{Fl}_G)$。$\\mathcal F\\in\\mathrm{Perv}(L^+G\\backslash\\mathrm{Gr}_G)$ 的像 $Z(\\mathcal F)$ 称为中心层。",
        "notation": "$\\star_{L^+G}$、$\\star_I$ 为两边的卷积分；$\\pi\\colon\\mathrm{Fl}_G\\to\\mathrm{Gr}_G$ 为投影。",
    },
    key_points=[
        "「像落在中心」= $Z(\\mathcal F)\\star_I\\mathcal G\\cong\\mathcal G\\star_I Z(\\mathcal F)$ 对一切 $\\mathcal G\\in\\mathcal D^b_c(I\\backslash\\mathrm{Fl}_G)$ 成立；这是定理 2.4.1(3)，也是函子 I 幺半性的来源（引理 3.2.1）。",
        "定理 2.4.1(5) 的 $\\pi_*Z(\\mathcal F)\\cong\\mathcal F$ 说明 $Z$ 在球侧是「单的」：它不丢信息，只是加进了 Iwahori 侧的位置变量。",
        "证明 (5) 的手法值得记住：造 $\\varpi\\colon\\mathrm{Gr}^{\\mathrm{cen}}_G\\to\\mathrm{Gr}_G\\times\\mathbb C$，用紧合基变换 (4) 与常层特殊化 (5) 把 $\\Psi_f$ 化成 $\\pi_*\\Psi_{\\mathrm{pr}_2}$。",
        "旁注 2.4.2 提醒：$Z$ **不是**到中心的等价——仿射 Hecke 范畴的中心比 $\\mathrm{Rep}(G^\\vee)$ 大得多（见 [BNP] 的谱描述）。",
        "注 2.4.3 把 $Z$ 与几何 Satake 复合，得 $\\mathrm{Rep}(G^\\vee)\\to\\mathrm{Perv}(I\\backslash\\mathrm{Fl}_G)$；原文此后常不加区分地写 $Z$。",
    ],
    formulas=[
        "$Z(\\mathcal F)=\\Psi_f(\\mathcal F\\boxtimes k_{\\mathbb C^\\times}[1])$",
        "$Z(\\mathcal F)\\star_I\\mathcal G\\cong\\mathcal G\\star_I Z(\\mathcal F)$",
        "$\\pi_*Z(\\mathcal F)\\cong\\mathcal F$",
    ],
    theorems=[
        {
            "name": "定理 2.4.1（Gaitsgory）",
            "statement": "中心函子 $Z$：(1) 幺半；(2) perverse $t$-正合；(3) 像落在 $\\mathcal D^b_c(I\\backslash\\mathrm{Fl}_G)$ 的中心；(4) 两个反常层卷积后仍反常；(5) $\\pi_*Z(\\mathcal F)\\cong\\mathcal F$。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "(2)：$\\mathcal F\\mapsto\\mathcal F\\boxtimes k_{\\mathbb C}[1]$ 是 perverse $t$-正合的，而 $\\Psi_f$ 由命题 2.2.2(2) 也 $t$-正合，复合即可。", "why": "两步都是「平移不改变反常性」的陈述，原文只写「几乎显然」。"},
                    {"no": 2, "text": "(5)：造 $\\varpi$ 使 $\\varpi|_{\\mathrm{Gr}_G\\times\\mathbb C^\\times}=\\mathrm{id}$、$\\varpi|_{\\mathrm{Gr}_G\\times\\{0\\}}=\\pi$；由命题 2.2.2(4)(5) 得 $\\mathcal F\\cong\\Psi_{\\mathrm{pr}_2}(\\mathcal F\\boxtimes k_{\\mathbb C}[1])\\cong\\pi_*\\Psi_f(\\mathcal F\\boxtimes k_{\\mathbb C}[1])=\\pi_*Z(\\mathcal F)$。", "why": "这是全文唯一给出的完整论证，示范了「用紧合性把中心纤维的计算推回去」。"},
                ],
                "gap_note": "(1)(3)(4) 原文不证；等变性需要 $\\mathbb A^1$ 上的群 ind-概形（脚注 6，引 [AcRi] §2.2、§10.3）。",
            },
            "source": "A p.4",
        }
    ],
    pitfalls=[
        "「幺半」不是「张量等价」：$Z$ 只保证 $Z(\\mathcal F\\star\\mathcal G)\\cong Z(\\mathcal F)\\star Z(\\mathcal G)$，不保证反映同构。",
        "把 $Z$ 与几何 Satake $\\mathrm{Sat}$ 复合之后，$Z$ 的定义域变成 $\\mathrm{Rep}(G^\\vee)$，但这不改变它仍是同一个函子这一事实——原文的记号滥用容易让人以为是两个不同构造。",
    ],
    related=[
        f"{PKG}/concept/central-affine-grassmannian",
        f"{PKG}/concept/wakimoto-filtration",
        f"{PKG}/concept/functor-f1",
    ],
    sources=[src([3, 4], "A p.4", "§2.4")],
    provenance_note="定义在 p.3，定理 2.4.1 与证明在 p.4；旁注 2.4.2、注 2.4.3 同在 p.4。",
)

A["concepts/wakimoto-sheaves"] = card(
    "concepts", "wakimoto-sheaves",
    title="Wakimoto 层 $\\mathbb W_\\lambda$",
    aliases=["Wakimoto sheaf", "W_λ", "Mirković 层"],
    track="A",
    summary="把 $\\lambda=\\lambda_1-\\lambda_2$ 写成支配权之差，令 $\\mathbb W_\\lambda=\\nabla_{\\lambda_1}\\star_I\\Delta_{-\\lambda_2}$：与选择无关、支撑在 $\\mathrm{Fl}_{G,\\lambda}$、且对加法幺半。",
    question="Wakimoto 层怎么由标准层与余标准层卷积出来，为什么它必须是「反序」的？",
    definition={
        "text": "对 $\\lambda\\in X^\\vee$ 取 $\\lambda_1,\\lambda_2\\in X^\\vee_+$ 使 $\\lambda=\\lambda_1-\\lambda_2$，定义反常层 $\\mathbb W_\\lambda:=\\nabla_{\\lambda_1}\\star_I\\Delta_{-\\lambda_2}$。其中 $\\Delta_w=j_{w!}k_{\\mathrm{Fl}_{G,w}}[\\ell(w)]$、$\\nabla_w=j_{w*}k_{\\mathrm{Fl}_{G,w}}[\\ell(w)]$ 为 Bruhat 分层上的标准层与余标准层。",
        "notation": "$\\mathrm{Fl}_G=\\bigsqcup_{w\\in W_{\\mathrm{ext}}}\\mathrm{Fl}_{G,w}$ 为 Bruhat 分解，$\\ell$ 是准 Coxeter 长度；$\\lambda\\in X^\\vee$ 与 $w_\\lambda$ 在 §4.3 对应。",
    },
    key_points=[
        "顺序很关键：$\\nabla_{\\lambda_1}\\star\\Delta_{-\\lambda_2}$（余标准在前、标准在后）才使 $\\mathbb W_\\lambda$ 与分解无关；倒过来不成立。",
        "命题 2.5.2(3) 的 $\\mathbb W_\\lambda\\star_I\\mathbb W_\\mu\\cong\\mathbb W_{\\lambda+\\mu}$ 把 $X^\\vee$ 变成「卷积半群」，于是一切 Wakimoto 层都由基本块生成——这是函子 I 能定义在 $\\mathrm{Rep}(T^\\vee)$ 上的根据。",
        "支撑在 $\\mathrm{Fl}_{G,\\lambda}$（不是 $\\mathrm{Fl}_{G,w_\\lambda}$ 的一般并）：这正是 IW 侧的轨道结构，两侧按同一个 $\\lambda$ 对齐，重数公式才可能成立。",
        "命题 2.5.1 的三条卷积公式是 Bruhat 分层的标准性质，但原文把它当作工具直接用，未证。",
    ],
    formulas=[
        "$\\mathbb W_\\lambda:=\\nabla_{\\lambda_1}\\star_I\\Delta_{-\\lambda_2}$（$\\lambda=\\lambda_1-\\lambda_2$，$\\lambda_i\\in X^\\vee_+$）",
        "$\\mathbb W_\\lambda\\star_I\\mathbb W_\\mu\\cong\\mathbb W_{\\lambda+\\mu}$",
        "$\\Delta_x\\star_I\\nabla_{x^{-1}}\\cong\\Delta_e\\cong\\nabla_{x^{-1}}\\star_I\\Delta_x$",
    ],
    theorems=[
        {
            "name": "命题 2.5.1–2.5.2（卷积与 Mirković 性质）",
            "statement": "(2.5.1) 长度可加时标准层/余标准层卷积仍为标准层/余标准层；$\\Delta_x\\star\\nabla_{x^{-1}}\\cong\\Delta_e$；$\\Delta_x\\star\\nabla_y$ 恒反常。(2.5.2) $\\mathbb W_\\lambda$ 与 $\\lambda_i$ 的选取无关、支撑在 $\\mathrm{Fl}_{G,\\lambda}$、且对加法幺半。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文只陈述；语言是 Bruhat 分层与 $!$/$*$ 扩张的常规推演，未展开。",
            },
            "source": "A p.5",
        }
    ],
    pitfalls=[
        "「与选择无关」需要 $\\lambda_i$ 取成支配权；若允许任意 $\\lambda_i$，标准层不一定是余标准层，卷积结果会变。",
        "$\\mathbb W_\\lambda$ 一般不是单层，也不是半单层：它是两个扩张的卷积，故只在 Grothendieck 群里才与 $\\Delta^{\\mathrm{IW}}_\\lambda$ 对齐（定理 4.4.1 证明后的提醒）。",
    ],
    related=[
        f"{PKG}/concept/wakimoto-filtration",
        f"{PKG}/concept/antispherical-module",
        f"{PKG}/concept/functor-f1",
    ],
    sources=[src([5, 5], "A p.5", "§2.5")],
    provenance_note="定义与命题 2.5.1–2.5.2 全在 p.5；$\\lambda\\mapsto w_\\lambda$ 的对应在 §4.3（p.10）。",
)

A["concepts/wakimoto-filtration"] = card(
    "concepts", "wakimoto-filtration",
    title="中心层的 Wakimoto 滤链（定理 2.5.3）",
    aliases=["Wakimoto filtration", "滤链与权重数", "P_I^Wak"],
    track="A",
    summary="每个中心层 $Z(\\mathcal F)$ 都有滤链，各项商为 $\\mathbb W_{\\lambda_i}$；且 $\\mathbb W_\\lambda$ 的重数恰是 $\\mathrm{Sat}^{-1}(\\mathcal F)$ 的 $\\lambda$-权空间维数。",
    question="Wakimoto 滤链的存在性与重数公式，分别在整条证明链上兑现了什么？",
    definition={
        "text": "定理 2.5.3：对 $\\mathcal F\\in\\mathrm{Perv}(L^+G\\backslash\\mathrm{Gr}_G)$，(1) $Z(\\mathcal F)$ 有滤链 $0=\\mathcal F_0\\subset\\mathcal F_1\\subset\\dots\\subset\\mathcal F_n=Z(\\mathcal F)$，使每个 $\\mathcal F_i/\\mathcal F_{i-1}$ 形如 $\\mathbb W_{\\lambda_i}$；(2) $\\mathbb W_\\lambda$ 在该滤链中的重数等于 $\\mathrm{Sat}^{-1}(\\mathcal F)$ 的 $\\lambda$-权空间维数。记 $\\mathcal P_I^{\\mathrm{Wak}}$ 为允许 Wakimoto 滤链的反常层构成的全子范畴。",
        "notation": "$\\mathrm{Sat}\\colon\\mathrm{Rep}(G^\\vee)\\xrightarrow{\\sim}\\mathrm{Perv}(L^+G\\backslash\\mathrm{Gr}_G)$ 为几何 Satake；$\\mathcal P_I^{\\mathrm{Wak}}\\subset\\mathcal P_I=\\mathrm{Perv}(I\\backslash\\mathrm{Fl}_G)$。",
    },
    key_points=[
        "这条定理是全文的「转换器」：它把几何侧的 Filtrations 与表示侧的权重数对接，正是「几何化 Bernstein 同构」的具体兑现。",
        "引理 2.5.4 说 $\\mathcal P_I^{\\mathrm{Wak}}$ 对卷积封闭，于是函子 I（$V\\otimes k_{T^\\vee}(\\lambda)\\mapsto Z(\\mathrm{Sat}(V))\\star\\mathbb W_\\lambda$）才有值域；没有这条滤链，$F_1$ 甚至无法定义。",
        "重数公式让「$Z^{\\mathrm{IW}}(V)$ 是倾斜层且重数为 $\\dim V_\\lambda$」（定理 4.5.1）成为可计算的陈述：倾斜层两侧的重数相等，于是上限与下限重合。",
        "滤链的存在性依赖 $V$ 有限维、$Z(\\mathrm{Sat}(V))$ 的反常性，以及 $\\nabla/\\Delta$ 的卷积公式；它不是「任意反常层都有」的普遍事实。",
    ],
    formulas=[
        "$0=\\mathcal F_0\\subset\\mathcal F_1\\subset\\dots\\subset\\mathcal F_n=Z(\\mathcal F),\\qquad \\mathcal F_i/\\mathcal F_{i-1}\\cong\\mathbb W_{\\lambda_i}$",
        "$[Z(\\mathcal F):\\mathbb W_\\lambda]=\\dim(\\mathrm{Sat}^{-1}(\\mathcal F))_\\lambda$",
    ],
    theorems=[
        {
            "name": "定理 2.5.3（Arkhipov–Bezrukavnikov）",
            "statement": "中心层带有 Wakimoto 滤链，且 $\\mathbb W_\\lambda$ 的重数等于对应 $G^\\vee$-表示的 $\\lambda$-权空间维数。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文只陈述、不证。标准证明走「先对 $\\mathrm{Sat}(V)$ 的每个权做归纳，再用 §2.5 的卷积公式」，本译本未补。",
            },
            "source": "A p.5",
        }
    ],
    pitfalls=[
        "滤链不是典范的：对象本身没有「唯一的」Wakimoto 滤链，定理只保证存在性与重数；下游用的也只是 $K_0$ 中的类。",
        "重数公式里的 $\\mathrm{Sat}^{-1}$ 不能省：直接写「$V$ 的权空间」在 $G^\\vee$ 与 $G$ 之间的对偶上会错位（$\\lambda$ 是余根格里的权）。",
    ],
    related=[
        f"{PKG}/concept/wakimoto-sheaves",
        f"{PKG}/concept/gaitsgory-central-functor",
        f"{PKG}/deriv/wakimoto-multiplicity",
    ],
    sources=[src([5, 5], "A p.5", "§2.5")],
    provenance_note="定理 2.5.3 与引理 2.5.4 都在 p.5；重数公式的用途见 §4.5（p.11）。",
)

if __name__ == "__main__":
    CARDS.update(A)
    print("wrote", write_cards(A))
