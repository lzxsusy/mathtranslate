#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cards_c.py —— 轨道 C：Iwahori–Whittaker 侧（§2.6、§4）。"""
from gen_cards import CARDS, card, src, PKG, write_cards

C = {}

C["concepts/antispherical-quotient"] = card(
    "concepts", "antispherical-quotient",
    title="反球商 $\\mathcal P_I^{\\mathrm{asph}}$",
    aliases=["antispherical Hecke category", "Serre 商", "P_I^asph"],
    track="C",
    summary="把 $\\mathcal P_I=\\mathrm{Perv}(I\\backslash\\mathrm{Fl}_G)$ 按那些 $w\\notin\\widetilde W_{\\mathrm{ext}}$ 的单对象 $\\mathrm{IC}_w$ 生成的 Serre 子范畴作商，得反球 Hecke 范畴，带商函子 $\\mathcal P_I\\to\\mathcal P_I^{\\mathrm{asph}}$。",
    question="反球 Hecke 范畴是对哪些对象作商得到的，为什么恰是「非极小代表元」那一批？",
    definition={
        "text": "记 $\\mathcal P_I:=\\mathrm{Perv}(I\\backslash\\mathrm{Fl}_G)$；令 $\\widetilde W_{\\mathrm{ext}}\\subseteq W_{\\mathrm{ext}}$ 为在双边陪集 $Ww$ 中取极小的元素集。反球 Hecke 范畴 $\\mathcal P_I^{\\mathrm{asph}}$ 定义为 $\\mathcal P_I$ 对由 $\\{\\mathrm{IC}_w\\mid w\\notin\\widetilde W_{\\mathrm{ext}}\\}$ 生成的 Serre 子范畴的商，附带商函子 $\\mathcal P_I\\to\\mathcal P_I^{\\mathrm{asph}}$。",
        "notation": "$\\mathrm{IC}_w$ 为 $\\mathrm{Fl}_{G,w}$ 上的反常上同调单层；$\\widetilde W_{\\mathrm{ext}}$ 是每个双边胞腔的最小长度代表元。",
    },
    key_points=[
        "「反球」在几何侧的体现就是这一步：球情形保留 $L^+G$-等变（即 $\\mathrm{Gr}_G$ 上的层），反球情形则把 $I$-等变层里「非极小」的那些单层全部杀掉，只留下与 $\\mathrm{Gr}_G$ 同构对应的那一片。",
        "商掉的是 Serre 子范畴而非厚子范畴，所以商仍是 Abel 范畴，才能谈反常 $t$-结构与滤链。",
        "定理 4.4.1(2) 说 $\\mathrm{Av}^{\\mathrm{IW}}$ 限制到 $\\mathcal P_I$ 上会穿过 $\\mathcal P_I^{\\mathrm{asph}}$ 并成为全忠实函子——反球商存在的意义就是让这句话有意义。",
        "它与模论侧的反球模 $M^{\\mathrm{asph}}$ 共用一套下标：模是 $\\mathbb Z\\otimes_{\\mathbb Z[W]}\\mathbb Z[W_{\\mathrm{ext}}]$，范畴是「按 $W$-胞腔取极小」。",
    ],
    formulas=[
        "$\\mathcal P_I^{\\mathrm{asph}}:=\\mathcal P_I\\big/\\langle \\mathrm{IC}_w\\mid w\\notin\\widetilde W_{\\mathrm{ext}}\\rangle_{\\mathrm{Serre}}$",
    ],
    theorems=[],
    pitfalls=[
        "把 $\\widetilde W_{\\mathrm{ext}}$ 与 $W_{\\mathrm{ext}}$ 混淆：前者是极小代表元集，每个双边胞腔取一个，元素个数一般远少于 $W_{\\mathrm{ext}}$。",
        "「商」在这里是 Serre 商（Abel 范畴层面），不是 Verdier 商（三角范畴层面）；两者不可互换。",
    ],
    related=[
        f"{PKG}/concept/antispherical-module",
        f"{PKG}/concept/iw-category",
        f"{PKG}/concept/iw-averaging",
    ],
    sources=[src([6, 6], "A p.6", "§2.6")],
    provenance_note="§2.6 只在 p.6 出现一段，定义与记号 $\\mathcal P_I$ 同页给出。",
)

C["concepts/whittaker-sheaves"] = card(
    "concepts", "whittaker-sheaves",
    title="Whittaker 层与 $(H,\\chi^*\\mathcal L_{\\mathrm{AS}})$-等变范畴",
    aliases=["Whittaker sheaves", "Artin–Schreier 局部系统", "χ-等变"],
    track="C",
    summary="固定 $\\chi\\colon H\\to\\mathbb G_m$ 与 $\\mathbb G_a$ 上的 Artin–Schreier 局部系统 $\\mathcal L_{\\mathrm{AS}}$，把 $\\chi^*\\mathcal L_{\\mathrm{AS}}$ 当作 $H$ 的乘法局部系统，得等变导出范畴；其对象常被上同调消没死死约束。",
    question="Whittaker 层的「等式 $a^*\\mathcal F\\cong\\chi^*\\mathcal L_{\\mathrm{AS}}\\boxtimes\\mathcal F$」为什么只是直观而非定义？",
    definition={
        "text": "设 $X$ 是代数群 $H$ 作用的 $H$-簇，$a\\colon H\\times X\\to X$ 为作用映射，固定同态 $\\chi\\colon H\\to\\mathbb G_m$。取 $\\mathbb G_a$ 上的 Artin–Schreier 局部系统 $\\mathcal L_{\\mathrm{AS}}$，则 $\\chi^*\\mathcal L_{\\mathrm{AS}}$ 是 $H$ 上的乘法局部系统。定义 $(H,\\chi^*\\mathcal L_{\\mathrm{AS}})$-等变可构造层导出范畴 $\\mathcal D^b_c(H\\backslash^{\\chi^*\\mathcal L_{\\mathrm{AS}}}X)$。",
        "notation": "$\\mathcal L_{\\mathrm{AS}}$ 由 $x\\mapsto x^p-x$ 的伽罗瓦覆盖中取一个直和项、使 $\\mathbb Z/p$ 以 $[n]\\mapsto\\zeta^n$ 作用得到（$\\zeta$ 为本原 $p$ 次单位根）。",
    },
    key_points=[
        "等变性在这里是「乘性局部系统」意义的：$a^*\\mathcal F\\cong\\chi^*\\mathcal L_{\\mathrm{AS}}\\boxtimes\\mathcal F$，比通常的 $H$-等变多了个扭曲。",
        "原文脚注 13 明确说这个等式「直观但不精确」：精确定义要纳入乘性映射 $H^k\\times X\\to X$ 的高阶余herence 关系（引 [Gai2]）。",
        "关键的消没 $H^\\bullet(\\mathbb G_a,\\mathcal L_{\\mathrm{AS}})\\cong H^\\bullet_c(\\mathbb G_a,\\mathcal L_{\\mathrm{AS}})=0$：这正是 Whittaker 层「被约束得很紧」的来源。",
        "例 4.1.1 是最小模型：$\\mathbb G_a$ 作用 $\\mathbb P^1$，点轨道太小无法承载 Whittaker 层，于是 $\\mathcal D^b_c(\\mathbb G_a\\backslash^\\chi\\mathbb P^1)\\cong\\mathcal D^b_c(\\mathbb G_a\\backslash^\\chi\\mathbb A^1)\\cong\\mathcal D^b(\\mathbb Q_\\ell\\text{-mod})$（由 $0$ 处取茎给出）。",
        "这一节只是「热身」：真正的 IW 范畴把一个具体的 $I_u^+\\to\\mathbb G_a$ 代进去。",
    ],
    formulas=[
        "$a^*\\mathcal F\\cong\\chi^*\\mathcal L_{\\mathrm{AS}}\\boxtimes\\mathcal F$",
        "$H^\\bullet(\\mathbb G_a,\\mathcal L_{\\mathrm{AS}})\\cong H^\\bullet_c(\\mathbb G_a,\\mathcal L_{\\mathrm{AS}})=0$",
    ],
    theorems=[
        {
            "name": "例 4.1.1（$\\mathbb P^1$ 上的最小模型）",
            "statement": "$\\mathbb G_a$ 以 $t\\cdot[x:y]=[x+yt:y]$ 作用 $\\mathbb P^1$，则 $\\mathcal D^b_c(\\mathbb G_a\\backslash^\\chi\\mathbb P^1)\\cong\\mathcal D^b_c(\\mathbb G_a\\backslash^\\chi\\mathbb A^1)\\cong\\mathcal D^b(\\mathbb Q_\\ell\\text{-mod})$。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "点轨道上任何层都 $\\mathbb G_a$-等变，无法带 Whittaker 扭曲，故该层在范畴中为零；于是范畴等价于去掉点轨道后的 $\\mathbb A^1$ 部分。", "why": "这是「轨道太小」的具体含义。"},
                    {"no": 2, "text": "$\\mathbb A^1$ 上取 $0$ 处茎，得与 $\\mathbb Q_\\ell$-模的等价。", "why": "原文说「容易验证」，实际上是 Whittaker 消没的初等练习。"},
                ],
                "gap_note": "两步都未给细节。",
            },
            "source": "A p.9",
        }
    ],
    pitfalls=[
        "把 $\\chi^*\\mathcal L_{\\mathrm{AS}}$ 当成常局部系统：它是秩一但**非平凡**的，正是 Whittaker 扭曲的全部来源。",
        "忽略「必须换到 étale 设置」（注 4.0.1）：Betti 情形下的 Whittaker 层需要 Krillov 模型，超出本文范围。",
    ],
    related=[
        f"{PKG}/concept/iw-category",
        f"{PKG}/concept/iw-highest-weight",
    ],
    sources=[src([9, 9], "A p.9", "§4.1")],
    provenance_note="§4.1 全在 p.9；$\\mathcal L_{\\mathrm{AS}}$ 的具体构造见脚注 12。",
)

C["concepts/iw-category"] = card(
    "concepts", "iw-category",
    title="Iwahori–Whittaker 范畴 $\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$",
    aliases=["Iwahori-Whittaker category", "D^b_IW", "IW 范畴"],
    track="C",
    summary="取 $I_u^+$（$I^+$ 的幂幺根）经 $\\chi\\colon I_u^+\\to\\mathbb G_a$ 的 Whittaker 扭曲，定义 $\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$；反常 $t$-结构限制其上，且 $\\mathcal D^b_c(I\\backslash\\mathrm{Fl}_G)$ 从右侧卷积作用于它。",
    question="IW 范畴是怎么从仿射旗簇的等变范畴里切出来的，它为什么自带一个右作用？",
    definition={
        "text": "令 $I_u^+$ 为 $I^+$ 的幂幺根（$LG\\to G$ 下 $U^+$ 的原像）。固定 $U^+$ 的 pinning 得 $U^+/[U^+,U^+]\\cong\\prod\\mathbb G_a$，定义 $\\chi\\colon I_u^+\\to U^+\\to U^+/[U^+,U^+]\\cong\\prod\\mathbb G_a\\xrightarrow{\\text{sum}}\\mathbb G_a$。IW 范畴定义为 $\\mathrm{Fl}_G$ 上 $(I_u^+,\\chi^*(\\mathcal L_{\\mathrm{AS}}))$-等变 $\\mathbb Q_\\ell$-层导出范畴，记 $\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$。",
        "notation": "$\\mathcal P_{\\mathrm{IW}}$ 为限制在其上的反常层子范畴；$\\star_I$ 为右卷积 $\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)\\times\\mathcal D^b_c(I\\backslash\\mathrm{Fl}_G)\\to\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$。",
    },
    key_points=[
        "「右作用」而非双模结构：$\\star_I$ 只从右边作用于 IW 侧，因为 $I$ 与 $I_u^+$ 的等变性只在右侧相容——这决定了 §5 里 $\\mathrm{Av}^{\\mathrm{IW}}$ 只能写成 $\\Delta^{\\mathrm{IW}}_0\\star_I(-)$。",
        "反常 $t$-结构限制到 IW 范畴上不是自动的：正因为 Whittaker 层的消没性质，才有命题 4.3.1 的最高权结构。",
        "此范畴同时是 §4 的目标与 §5 的起点：$F^{\\mathrm{IW}}$ 的终点就是它，而定理 5.0.1 说整个几何侧等价于它。",
        "讲义在这里换了设置（注 4.0.1）：从 Betti 换到 étale、$\\mathbb Q_\\ell$-层、$\\ell\\neq p$；此前所有讨论都有显然的 étale 类比。",
    ],
    formulas=[
        "$\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G):=\\mathcal D^b_{(I_u^+,\\chi^*\\mathcal L_{\\mathrm{AS}})}(\\mathrm{Fl}_G)$",
        "$(-)\\star_I(-)\\colon\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)\\times\\mathcal D^b_c(I\\backslash\\mathrm{Fl}_G)\\to\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$",
    ],
    theorems=[],
    pitfalls=[
        "把 $I_u^+$ 与 $I$ 搞混：$I_u^+$ 是 pro-unipotent 根，$\\chi$ 定义在它上面；$I$ 是完整的 Iwahori，只出现在右侧卷积因子里。",
        "IW 范畴里的对象不是「$I$-等变层」：它是「$I_u^+$ 等变、但带 Whittaker 扭曲」，所以不能直接套用 $\\mathcal P_I$ 的结论。",
    ],
    related=[
        f"{PKG}/concept/whittaker-sheaves",
        f"{PKG}/concept/iw-highest-weight",
        f"{PKG}/concept/functor-fiw",
    ],
    sources=[src([9, 9], "A p.9", "§4.2")],
    provenance_note="§4.2 全在 p.9；$\\chi$ 的合成与 $\\star_I$ 同页定义。",
)

C["concepts/iw-highest-weight"] = card(
    "concepts", "iw-highest-weight",
    title="IW 反常层的最高权结构（命题 4.3.1）",
    aliases=["highest weight category", "标准层 Δ^IW", "倾斜层 T^IW"],
    track="C",
    summary="$I_u^+$-轨道由 $W_{\\mathrm{ext}}$ 参数化，其中只有 $\\widetilde W_{\\mathrm{ext}}$ 上的轨道承载非零 Whittaker 局部系统；据此定义 $\\Delta^{\\mathrm{IW}}_\\lambda,\\nabla^{\\mathrm{IW}}_\\lambda,\\mathrm{IC}^{\\mathrm{IW}}_\\lambda$，得权偏序集为 $X^\\vee$ 的最高权范畴，从而有不可分解倾斜层 $T^{\\mathrm{IW}}_\\lambda$。",
    question="最高权结构是怎么从轨道参数化得到的，倾斜层为什么必须存在？",
    definition={
        "text": "$I_u^+$ 在 $\\mathrm{Fl}_G$ 上的轨道由 $W_{\\mathrm{ext}}$ 参数化，且有双射 $X^\\vee\\leftrightarrow\\widetilde W_{\\mathrm{ext}}$，$\\lambda\\mapsto w_\\lambda$。记 $\\mathrm{Fl}^{\\mathrm{IW}}_{G,\\lambda}$ 为对应轨道、$j^{\\mathrm{IW}}_\\lambda$ 为其嵌入。只有 $\\lambda\\in X^\\vee$ 对应的轨道承载唯一秩一 Whittaker 局部系统 $\\mathcal L_{\\chi,\\lambda}$。定义 $\\Delta^{\\mathrm{IW}}_\\lambda:=j^{\\mathrm{IW}}_{\\lambda!}\\mathcal L_{\\chi,\\lambda}[\\dim\\mathrm{Fl}^{\\mathrm{IW}}_{G,\\lambda}]$、$\\nabla^{\\mathrm{IW}}_\\lambda:=j^{\\mathrm{IW}}_{\\lambda*}\\mathcal L_{\\chi,\\lambda}[\\dim]$；$\\mathrm{IC}^{\\mathrm{IW}}_\\lambda$ 为 $\\Delta^{\\mathrm{IW}}_\\lambda\\to\\nabla^{\\mathrm{IW}}_\\lambda$ 的像。",
        "notation": "$\\mathcal P_{\\mathrm{IW}}$ 的权偏序集是 $X^\\vee$；$T^{\\mathrm{IW}}_\\lambda$ 为唯一的不可分解倾斜层。",
    },
    key_points=[
        "「只有 $\\widetilde W_{\\mathrm{ext}}$ 上的轨道有非零 Whittaker 局部系统」是整节的技术核心：其它轨道上的秩一层被消没性质杀掉，于是 $\\mathcal P_{\\mathrm{IW}}$ 的权集恰好是 $X^\\vee$，与几何侧的线丛下标完全一致。",
        "偏序集是 $X^\\vee$（余根格），不是 $W_{\\mathrm{ext}}$：这是把「仿射 Weyl 群的组合」压成「格上的最高权理论」，也是与 $\\mathrm{Rep}(G^\\vee)$ 的权分解对齐的关键。",
        "最高权范畴 ⇒ 每个权有一个不可分解倾斜层（Ringel 对偶的范畴化）；推论 4.3.2 又给出 $\\mathcal D^b\\mathcal P_{\\mathrm{IW}}\\cong\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$，于是「倾斜」可以搬到导出范畴里用。",
        "标准层与余标准层都用 $!$/$*$ 扩张加 $[\\dim]$ 位移：位移常数必须与 §2.5 的 $\\Delta_w$、$\\nabla_w$ 一致，否则定理 4.4.1(6) 的匹配会差一个平移。",
    ],
    formulas=[
        "$\\Delta^{\\mathrm{IW}}_\\lambda=j^{\\mathrm{IW}}_{\\lambda!}\\mathcal L_{\\chi,\\lambda}[\\dim\\mathrm{Fl}^{\\mathrm{IW}}_{G,\\lambda}],\\qquad \\nabla^{\\mathrm{IW}}_\\lambda=j^{\\mathrm{IW}}_{\\lambda*}\\mathcal L_{\\chi,\\lambda}[\\dim\\mathrm{Fl}^{\\mathrm{IW}}_{G,\\lambda}]$",
        "$\\mathrm{IC}^{\\mathrm{IW}}_\\lambda=\\mathrm{im}(\\Delta^{\\mathrm{IW}}_\\lambda\\to\\nabla^{\\mathrm{IW}}_\\lambda)$",
    ],
    theorems=[
        {
            "name": "命题 4.3.1 与推论 4.3.2",
            "statement": "$\\mathcal P_{\\mathrm{IW}}$ 是以 $X^\\vee$ 为权偏序集的最高权范畴，故对每个 $\\lambda$ 有唯一不可分解倾斜层 $T^{\\mathrm{IW}}_\\lambda$；且实现函子诱导等价 $\\mathcal D^b\\mathcal P_{\\mathrm{IW}}\\cong\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文只给「关键观察」，证明留给 [ArBe]；最高权结构的验证依赖轨道上的 Whittaker 局部系统分类。",
            },
            "source": "A p.10",
        }
    ],
    pitfalls=[
        "把 $\\lambda\\mapsto w_\\lambda$ 当成 $X^\\vee\\cong W_{\\mathrm{ext}}$：它只是到极小代表元集 $\\widetilde W_{\\mathrm{ext}}$ 的双射，陪集信息被丢掉了。",
        "倾斜层 $T^{\\mathrm{IW}}_\\lambda$ 与标准层 $\\Delta^{\\mathrm{IW}}_\\lambda$ 不同构：前者同时有标准滤链与余标准滤链，后者只有一侧。",
    ],
    related=[
        f"{PKG}/concept/iw-category",
        f"{PKG}/concept/iw-averaging",
        f"{PKG}/concept/central-tilting",
    ],
    sources=[src([10, 10], "A p.10", "§4.3")],
    provenance_note="§4.3 全在 p.10；命题 4.3.1、推论 4.3.2 同页。",
)

C["concepts/iw-averaging"] = card(
    "concepts", "iw-averaging",
    title="IW 平均函子 $\\mathrm{Av}^{\\mathrm{IW}}$（定理 4.4.1）",
    aliases=["averaging functor", "Av^IW", "反球商的全忠实嵌入"],
    track="C",
    summary="$\\mathrm{Av}^{\\mathrm{IW}}(\\mathcal F)=\\Delta^{\\mathrm{IW}}_0\\star_I\\mathcal F$ 是反常 $t$-正合的，且在反常层上穿过反球商，给出全忠实函子 $\\mathcal P_I^{\\mathrm{asph}}\\hookrightarrow\\mathcal P_{\\mathrm{IW}}$。",
    question="平均函子为什么是 $t$-正合的，全忠实性又靠什么截面？",
    definition={
        "text": "定义 $\\mathrm{Av}^{\\mathrm{IW}}\\colon\\mathcal D^b(I\\backslash\\mathrm{Fl}_G)\\to\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$，$\\mathcal F\\mapsto\\Delta^{\\mathrm{IW}}_0\\star_I\\mathcal F$。定理 4.4.1（[ArBe]）：(1) $\\mathrm{Av}^{\\mathrm{IW}}$ 是反常 $t$-正合的；(2) 其限制到 $\\mathcal P_I$ 上穿过一个全忠实函子 $\\mathcal P_I^{\\mathrm{asph}}\\to\\mathcal P_{\\mathrm{IW}}$。",
        "notation": "$\\Delta^{\\mathrm{IW}}_0$ 是权 $0$ 的标准层；$\\star_I$ 为 §4.2 的右卷积。",
    },
    key_points=[
        "两条计算式是全部证明的支点：(5) $\\mathrm{Av}^{\\mathrm{IW}}(\\mathrm{IC}_w)=0$ 除非 $w\\in\\widetilde W_{\\mathrm{ext}}$；(6) $\\mathrm{Av}^{\\mathrm{IW}}(\\Delta_w)\\cong\\Delta^{\\mathrm{IW}}_\\lambda$、$\\mathrm{Av}^{\\mathrm{IW}}(\\nabla_w)\\cong\\nabla^{\\mathrm{IW}}_\\lambda$，其中 $\\lambda$ 由 $W\\cdot w=W\\cdot w_\\lambda$ 唯一确定。",
        "(5) 直接给出 (2) 的「穿过反球商」：被杀掉的正是 $w\\notin\\widetilde W_{\\mathrm{ext}}$ 的单层。",
        "(6) 给出 $t$-正合性：标准层与余标准层都映到标准层与余标准层，于是反常 $t$-结构逐层对齐。",
        "全忠实性的证明是「造截面」：从 $I\\cap I_u^+$-等变平均到 $I$-等变、取反常上同调、再套反球商函子；原文只说「直观上如此」。",
    ],
    formulas=[
        "$\\mathrm{Av}^{\\mathrm{IW}}\\colon\\mathcal D^b(I\\backslash\\mathrm{Fl}_G)\\to\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G),\\quad \\mathcal F\\mapsto\\Delta^{\\mathrm{IW}}_0\\star_I\\mathcal F$",
        "$\\mathrm{Av}^{\\mathrm{IW}}(\\mathrm{IC}_w)=0\\ (w\\notin\\widetilde W_{\\mathrm{ext}}),\\qquad \\mathrm{Av}^{\\mathrm{IW}}(\\Delta_w)\\cong\\Delta^{\\mathrm{IW}}_\\lambda,\\ \\mathrm{Av}^{\\mathrm{IW}}(\\nabla_w)\\cong\\nabla^{\\mathrm{IW}}_\\lambda$",
    ],
    theorems=[
        {
            "name": "定理 4.4.1（Arkhipov–Bezrukavnikov）",
            "statement": "$\\mathrm{Av}^{\\mathrm{IW}}$ 反常 $t$-正合；其在 $\\mathcal P_I$ 上的限制穿过全忠实函子 $\\mathcal P_I^{\\mathrm{asph}}\\to\\mathcal P_{\\mathrm{IW}}$。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "由几何与轨道分析得 (5)(6) 两式。", "why": "这是原文唯一给出的实质论证步骤，细节留给 [ArBe]。"},
                    {"no": 2, "text": "用 (5)(6) 与基础同调代数推出反常 $t$-正合性；由 (5) 推出穿过反球商。", "why": "标准层/余标准层的对应保证 $t$-结构两侧对齐。"},
                    {"no": 3, "text": "为证全忠实，构造 $\\mathrm{Av}^{\\mathrm{IW}}$ 的截面：$I\\cap I_u^+$-等变 →平均→ $I$-等变 →取反常上同调→套反球商函子。", "why": "有截面即得全忠实；原文只描述「直观上」，未写验证。"},
                ],
                "gap_note": "第 1、3 步都只有概述；本译本把「截面构造」标为待补细节。",
            },
            "source": "A p.10",
        }
    ],
    pitfalls=[
        "把 $\\mathrm{Av}^{\\mathrm{IW}}$ 当成 $\\mathcal D^b(I\\backslash\\mathrm{Fl}_G)$ 到自身的投影：它的终点是 IW 范畴，等变性被替换掉了。",
        "式 (6) 里的 $\\lambda$ 由「$W\\cdot w=W\\cdot w_\\lambda$」唯一确定，不是 $w$ 本身的下标；同一双边胞腔里的不同 $w$ 会映到同一个 $\\lambda$。",
    ],
    related=[
        f"{PKG}/concept/iw-highest-weight",
        f"{PKG}/concept/antispherical-quotient",
        f"{PKG}/deriv/iw-averaging-t-exact",
    ],
    sources=[src([10, 10], "A p.10", "§4.4")],
    provenance_note="§4.4 与定理 4.4.1 的证明梗概全在 p.10，公式编号 (5)(6) 同页。",
)

C["concepts/central-tilting"] = card(
    "concepts", "central-tilting",
    title="中心层的 IW 像是倾斜层（定理 4.5.1）",
    aliases=["Z^IW", "central sheaves are tilting", "重数 = dim V_λ"],
    track="C",
    summary="复合 $Z^{\\mathrm{IW}}\\colon\\mathrm{Rep}(G^\\vee)\\xrightarrow{Z}\\mathcal P_I\\xrightarrow{\\mathrm{Av}^{\\mathrm{IW}}}\\mathcal P_{\\mathrm{IW}}$ 把每个 $V$ 送到倾斜层，且 $\\Delta^{\\mathrm{IW}}_\\lambda$ 与 $\\nabla^{\\mathrm{IW}}_\\lambda$ 的重数都等于 $\\dim V_\\lambda$。",
    question="为什么中心层经平均之后变成倾斜层，重数公式又是怎么被证明的？",
    definition={
        "text": "定义 $Z^{\\mathrm{IW}}\\colon\\mathrm{Rep}(G^\\vee)\\xrightarrow{Z}\\mathcal P_I\\xrightarrow{\\mathrm{Av}^{\\mathrm{IW}}}\\mathcal P_{\\mathrm{IW}}$。定理 4.5.1（[ArBe]）：对一切 $V\\in\\mathrm{Rep}(G^\\vee)$，$Z^{\\mathrm{IW}}(V)$ 是倾斜层，且对一切 $\\lambda\\in X^\\vee$ 有 $(Z^{\\mathrm{IW}}(V):\\Delta^{\\mathrm{IW}}_\\lambda)=(Z^{\\mathrm{IW}}(V):\\nabla^{\\mathrm{IW}}_\\lambda)=\\dim V_\\lambda$。",
        "notation": "$(X:\\Delta)$ 表示 $\\Delta$ 在滤链中的重数；倾斜层的标准重数与余标准重数相等。",
    },
    key_points=[
        "倾斜 = 同时有标准滤链与余标准滤链；定理给出两侧重数相等，这正是倾斜性的等价刻画（在最高权范畴中）。",
        "重数公式与定理 2.5.3 的 Wakimoto 重数公式形式一致：都是「几何侧的重数 = 表示侧的权空间维数」，一个在 $\\mathcal P_I$、一个在 $\\mathcal P_{\\mathrm{IW}}$。",
        "证明策略是「化归到极小情形」：先证张量封闭，再约到半单，最后只剩极小与拟极小的单模。",
        "拟极小情形是全文承认最难的一步，需要研究 $\\mathcal P_I$ 的某些商；原文只写一句，没有细节。",
        "这条定理是 §5 整篇文章的动机：$F^{\\mathrm{IW}}$ 把线丛 $\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)$ 送到 $\\mathrm{Av}^{\\mathrm{IW}}(\\mathbb W_\\lambda)$、把 $L_\\lambda\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}$ 送到倾斜层 $T^{\\mathrm{IW}}(L_\\lambda)$。",
    ],
    formulas=[
        "$Z^{\\mathrm{IW}}(V):=\\mathrm{Av}^{\\mathrm{IW}}(Z(\\mathrm{Sat}(V)))$",
        "$(Z^{\\mathrm{IW}}(V):\\Delta^{\\mathrm{IW}}_\\lambda)=(Z^{\\mathrm{IW}}(V):\\nabla^{\\mathrm{IW}}_\\lambda)=\\dim V_\\lambda$",
    ],
    theorems=[
        {
            "name": "定理 4.5.1（Arkhipov–Bezrukavnikov）",
            "statement": "$Z^{\\mathrm{IW}}(V)$ 是倾斜层，且标准/余标准重数均为 $\\dim V_\\lambda$。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "若 $Z^{\\mathrm{IW}}(V)$、$Z^{\\mathrm{IW}}(V')$ 倾斜，则由 $\\mathcal D^b(I\\backslash\\mathrm{Fl}_G)$ 中卷积的性质，$Z^{\\mathrm{IW}}(V\\otimes V')$ 也倾斜。", "why": "张量封闭性把问题从任意 $V$ 收到生成元上。"},
                    {"no": 2, "text": "$G$ 半单时成立 ⇒ $G$ 约化时成立。", "why": "约化 = 半单 × 环面，环面部分由权直接读出。"},
                    {"no": 3, "text": "由 (1)(2) 只须验 $V$ 是极小或拟极小最高权的单模；极小情形直接算，拟极小情形要研究 $\\mathcal P_I$ 的商。", "why": "这两类单模生成整个表示范畴；拟极小是最难处。"},
                ],
                "gap_note": "第 3 步的拟极小情形原文只说「much more difficult」，未给论证；这是本卡标注的主要空白。",
            },
            "source": "A p.11",
        }
    ],
    pitfalls=[
        "把 $Z^{\\mathrm{IW}}(V)$ 与 $Z(\\mathrm{Sat}(V))$ 混同：前者是后者的平均像，一般不再是中心层（等变性被换成 IW）。",
        "重数公式两边都用 $\\dim V_\\lambda$，但下标 $\\lambda\\in X^\\vee$ 是余根格权重；若把 $V$ 理解为 $G$（而非 $G^\\vee$）的表示，下标要对偶化。",
    ],
    related=[
        f"{PKG}/concept/iw-averaging",
        f"{PKG}/concept/wakimoto-filtration",
        f"{PKG}/deriv/wakimoto-multiplicity",
    ],
    sources=[src([11, 11], "A p.11", "§4.5")],
    provenance_note="§4.5 与定理 4.5.1 的三步证明梗概全在 p.11。",
)

if __name__ == "__main__":
    CARDS.update(C)
    print("wrote", write_cards(C))
