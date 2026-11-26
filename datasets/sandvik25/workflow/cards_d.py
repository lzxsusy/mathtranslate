#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cards_d.py —— 轨道 D：主等价（§5）。"""
from gen_cards import CARDS, card, src, PKG, write_cards

D = {}

D["concepts/functor-fiw"] = card(
    "concepts", "functor-fiw",
    title="主函子 $F^{\\mathrm{IW}}$ 与 Arkhipov–Bezrukavnikov 等价（定理 5.0.1）",
    aliases=["F^IW", "AB equivalence", "主定理"],
    track="D",
    summary="$F^{\\mathrm{IW}}=\\mathrm{Av}^{\\mathrm{IW}}\\circ F\\colon\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\to\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$ 是等价：$V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}\\mapsto Z^{\\mathrm{IW}}(V)$、$\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)\\mapsto\\mathrm{Av}^{\\mathrm{IW}}(\\mathbb W_\\lambda)$。",
    question="主函子怎么把几何侧的对象送到 IW 侧，等价性由哪两步合成？",
    definition={
        "text": "定义 $F^{\\mathrm{IW}}\\colon\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\xrightarrow{F}\\mathcal D^b\\mathcal P_I\\xrightarrow{\\mathrm{Av}^{\\mathrm{IW}}}\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$；由定理 4.4.1 与推论 4.3.2 也可写成 $\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\xrightarrow{F}\\mathcal D^b\\mathcal P_I\\xrightarrow{\\mathrm{Av}^{\\mathrm{IW}}}\\mathcal D^b\\mathcal P_{\\mathrm{IW}}\\cong\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$。对象对应见式 (7)：$V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}\\mapsto Z(\\mathrm{Sat}(L_\\lambda))\\mapsto T^{\\mathrm{IW}}(V)$、$\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)\\mapsto\\mathbb W_\\lambda\\mapsto\\mathrm{Av}^{\\mathrm{IW}}(\\mathbb W_\\lambda)$。",
        "notation": "$T^{\\mathrm{IW}}(V):=F^{\\mathrm{IW}}(L_\\lambda\\otimes\\mathcal O_{\\widetilde{\\mathcal N}})$ 是倾斜层（定理 4.5.1）；$\\mathrm{Av}^{\\mathrm{IW}}(\\mathbb W_\\lambda)$ 与 $\\Delta^{\\mathrm{IW}}_\\lambda$ 不同构，但 $K_0$ 中同类。",
    },
    key_points=[
        "式 (7) 的两行是整篇文章的「字典」：几何侧的自由对象对应倾斜层，线丛对应平均后的 Wakimoto 层。",
        "一个重要提醒（原文明确）：$\\mathrm{Av}^{\\mathrm{IW}}(\\mathbb W_\\lambda)$ **不是**标准层 $\\Delta^{\\mathrm{IW}}_\\lambda$，两者只在 Grothendieck 群里相等——所以等价不是把生成元逐个送到标准层的「显然」对应。",
        "证明分两半：本质满射靠式 (7) 加常规同调代数；全忠实靠把 (8) 用五引理化到 $\\mathcal F=\\mathcal O_{\\widetilde{\\mathcal N}}$、$\\mathcal G=V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)[n]$ 并显式计算 $\\mathrm{Hom}$。",
        "脚注 14：$T^{\\mathrm{IW}}(L_\\lambda)\\cong T^{\\mathrm{IW}}_\\lambda$（$\\lambda\\in X^\\vee_+$）不是构造出来的，而是定理 5.0.1 的**推论**——这是等价强于「对象逐一对应」的直接证据。",
    ],
    formulas=[
        "$F^{\\mathrm{IW}}=\\mathrm{Av}^{\\mathrm{IW}}\\circ F\\colon\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\to\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$",
        "$F^{\\mathrm{IW}}(V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}})\\cong Z^{\\mathrm{IW}}(V),\\qquad F^{\\mathrm{IW}}(\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda))\\cong\\mathrm{Av}^{\\mathrm{IW}}(\\mathbb W_\\lambda)$",
    ],
    theorems=[
        {
            "name": "定理 5.0.1（Arkhipov–Bezrukavnikov）",
            "statement": "$F^{\\mathrm{IW}}\\colon\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\to\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$ 是范畴等价。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "本质满射：由式 (7) 描述的对象像，加上常规同调代数（生成元的像生成目标范畴）。", "why": "引理 3.1.1 已给出源范畴的生成元，故只需验像生成。"},
                    {"no": 2, "text": "全忠实：对 (8) 式用五引理化归到 $\\mathcal F=\\mathcal O_{\\widetilde{\\mathcal N}}$、$\\mathcal G=V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)[n]$。", "why": "这两类对象已生成源范畴，五引理把一般情形退回生成元。"},
                    {"no": 3, "text": "左边 $\\dim\\mathrm{Hom}(\\mathcal O_{\\widetilde{\\mathcal N}},V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)[n])=\\dim V_{-\\lambda}$（$n=0$）或 $0$（$n\\neq0$）。", "why": "这是几何侧的直接计算：截面即 $V$ 在权 $-\\lambda$ 的分量。"},
                    {"no": 4, "text": "右边用 $\\mathrm{Hom}(\\Delta^{\\mathrm{IW}}_0,Z^{\\mathrm{IW}}(V)\\star_I\\mathbb W_\\lambda[n])\\cong\\mathrm{Hom}(\\Delta^{\\mathrm{IW}}_0\\star_I\\mathbb W_{-\\lambda},Z^{\\mathrm{IW}}(V)[n])\\cong\\mathrm{Hom}(\\Delta^{\\mathrm{IW}}_{-\\lambda},Z^{\\mathrm{IW}}(V)[n])$，再由定理 4.5.1 得同一数值。", "why": "把目标侧的 $\\mathrm{Hom}$ 化成标准层与倾斜层的重数，正是定理 4.5.1 的用途。"},
                ],
                "gap_note": "第 1、2 步原文各一句「routine / 5-lemma」，第 3 步的「mostly straightforward」也未展开；本卡把它们拆成可核对的四步。",
            },
            "source": "A p.12",
        }
    ],
    pitfalls=[
        "把 $F^{\\mathrm{IW}}$ 与「$F$ 复合实现函子」混同：后者落在 $\\mathcal D^b(I\\backslash\\mathrm{Fl}_G)$，而 $F^{\\mathrm{IW}}$ 落在 IW 范畴，中间差一个平均。",
        "由 $\\mathrm{Av}^{\\mathrm{IW}}(\\mathbb W_\\lambda)$ 与 $\\Delta^{\\mathrm{IW}}_\\lambda$ 在 $K_0$ 中相等，推出它们同构——这是原文特意警告的错误。",
    ],
    related=[
        f"{PKG}/concept/functor-f3",
        f"{PKG}/concept/iw-averaging",
        f"{PKG}/concept/central-tilting",
        f"{PKG}/deriv/fully-faithful-hom",
    ],
    sources=[src([11, 12], "A p.12", "§5")],
    provenance_note="式 (7) 在 p.11，定理 5.0.1 的证明与脚注 14 在 p.12。",
)

D["concepts/five-categories"] = card(
    "concepts", "five-categories",
    title="五个范畴的等价图（推论 5.0.2）",
    aliases=["corollary 5.0.2", "五范畴等价", "等价图"],
    track="D",
    summary="主定理连同 §4 的构造把五个范畴串成一个交换图：$\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\sim\\mathcal D^b\\mathcal P_I^{\\mathrm{asph}}\\sim\\mathcal D^b\\mathcal P_{\\mathrm{IW}}\\sim\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)\\sim\\mathcal D^b\\mathcal P_I$。",
    question="这五个范畴之间哪些是等价、哪些只是单向函子，为什么偏偏这五个？",
    definition={
        "text": "推论 5.0.2：存在范畴等价 $\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\sim\\mathcal D^b\\mathcal P_I^{\\mathrm{asph}}\\sim\\mathcal D^b\\mathcal P_{\\mathrm{IW}}\\sim\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$，且 $\\mathcal D^b\\mathcal P_{\\mathrm{IW}}\\cong\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$（推论 4.3.2），另有 $\\mathcal D^b\\mathcal P_I$ 通过全忠实函子嵌入其中。",
        "notation": "$\\mathcal P_I=\\mathrm{Perv}(I\\backslash\\mathrm{Fl}_G)$、$\\mathcal P_I^{\\mathrm{asph}}$ 为其 Serre 商、$\\mathcal P_{\\mathrm{IW}}$ 为 IW 反常层。",
    },
    key_points=[
        "五个范畴分成三类几何来源：Springer 解消（凝聚层）、仿射旗簇（$I$-等变反常层）、IW 侧（Whittaker 扭曲的反常层）；等价把它们焊在一起。",
        "只有反球商与 IW 之间是「真」的等价链；$\\mathcal D^b\\mathcal P_I$ 只是通过全忠实函子参与，它本身更大。",
        "这个图是整篇文章的收束：A 轨给 Wakimoto 与中心层、B 轨给三造函子、C 轨给 IW 侧、D 轨给主等价，全部落在这张图里。",
        "图里没有 $\\mathcal D^b(I\\backslash\\mathrm{Fl}_G)$：实现函子在 Iwahori 情形非等价（§3.4 末的警告），所以它不能进等价图。",
    ],
    formulas=[
        "$\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\ \\sim\\ \\mathcal D^b\\mathcal P_I^{\\mathrm{asph}}\\ \\sim\\ \\mathcal D^b\\mathcal P_{\\mathrm{IW}}\\ \\cong\\ \\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$",
    ],
    theorems=[
        {
            "name": "推论 5.0.2",
            "statement": "上述五个范畴之间的等价关系成立。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "定理 5.0.1 给出 $\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\sim\\mathcal D^b\\mathcal P_{\\mathrm{IW}}$（经由 $\\mathrm{Av}^{\\mathrm{IW}}$）。", "why": "主等价直接给出这一环。"},
                    {"no": 2, "text": "定理 4.4.1(2) 给出 $\\mathcal P_I^{\\mathrm{asph}}\\hookrightarrow\\mathcal P_{\\mathrm{IW}}$ 全忠实，等价性由反向函子补齐（原文列为推论）。", "why": "全忠实 + 生成/维数匹配是标准补法。"},
                    {"no": 3, "text": "推论 4.3.2 给出 $\\mathcal D^b\\mathcal P_{\\mathrm{IW}}\\cong\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$。", "why": "实现函子在 IW 情形恰是等价。"},
                ],
                "gap_note": "原文只画图并列等价，未给每条的独立论证；本卡按引用关系拆解。",
            },
            "source": "A p.12",
        }
    ],
    pitfalls=[
        "把 $\\mathcal D^b\\mathcal P_I$ 也写成等价的一端：它只通过全忠实嵌入参与，本身比反球商大。",
        "误以为图是「同一范畴的五种描述」：五个范畴的底层几何各不相同，等价是跨几何的定理。",
    ],
    related=[
        f"{PKG}/concept/functor-fiw",
        f"{PKG}/concept/antispherical-quotient",
        f"{PKG}/concept/iw-category",
    ],
    sources=[src([12, 12], "A p.12", "§5")],
    provenance_note="推论 5.0.2 的图在 p.12 末；各条等价的出处分别是定理 5.0.1、定理 4.4.1、推论 4.3.2。",
)

if __name__ == "__main__":
    CARDS.update(D)
    print("wrote", write_cards(D))
