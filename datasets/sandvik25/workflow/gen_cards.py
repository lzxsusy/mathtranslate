#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_cards.py —— 生成 sandvik25 资料卡 JSON（单一事实源，避免手写转义）。
生成后跑 tools/lint_cards.py、tools/build_index.py、tools/render_md.py。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PKG = "sandvik25"


def card(kind, slug, **kw):
    c = {
        "id": f"{PKG}/{'concept' if kind == 'concepts' else 'deriv'}/{slug}",
        "type": "concept" if kind == "concepts" else "derivation",
        "rights": "rewritten",
        "status": "dev",
    }
    c.update(kw)
    return c


def src(pages, anchor, section, text="A"):
    return {"text": text, "section": section, "pages": pages, "anchor": anchor}


CARDS = {}

# ---------------------------------------------------------------- O 总览
CARDS["concepts/three-categorifications"] = card(
    "concepts", "three-categorifications",
    title="反球模的三种描述与三种范畴化",
    aliases=["三种描述", "three categorifications", "候选范畴化"],
    track="O",
    summary="反球模 $M^{\\mathrm{asph}}$ 有 $K$ 群、$q$-形变 Whittaker、Iwahori–Whittaker 函数三种描述，各给一个候选范畴化；主定理说三者其实是同一个三角范畴。",
    question="反球模有哪三种描述，为什么每一种都能被提升成一个范畴？",
    definition={
        "text": "原文把三条路线并列：(1) 模 $M^{\\mathrm{asph}}$ 本身；(2) 对偶侧的 $G^\\vee$-等变 Springer 解消上凝聚层之 $K$ 群，$[\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})]\\cong M^{\\mathrm{asph}}$；(3) $q$-形变的 Whittaker 模，即 $G^\\circ(\\mathbb F_q((x)))$ 上的 Iwahori–Whittaker 函数。三条路线分别范畴化为 $\\mathcal P_I^{\\mathrm{asph}}$（仿射旗簇上反常层取商）、$\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})$、$\\mathcal P_{\\mathrm{IW}}$（Iwahori–Whittaker 反常层）。",
        "notation": "$M^{\\mathrm{asph}}=\\mathbb Z\\otimes_{\\mathbb Z[W]}\\mathbb Z[W_{\\mathrm{ext}}]$；$\\mathcal P_I^{\\mathrm{asph}}$ 记反球 Hecke 范畴，$\\mathcal P_{\\mathrm{IW}}$ 记 IW 反常层范畴。",
    },
    key_points=[
        "$K$ 群只记得 $M^{\\mathrm{asph}}$ 的加法结构；要把它变成范畴，就得让每个 $M^{\\mathrm{asph}}$ 的元素是一个复形、每个关系是一条正合三角。",
        "三条路线给出的范畴在 $K_0$ 上一致，但这只保证有**意义**，不保证有函子——主定理的实质是造出三向等价函子。",
        "三种范畴化所处的几何底不同：仿射旗簇（层论）、Springer 解消（凝聚层）、IW 范畴（étale 层），因此「等价」不是同一空间上的重述，而是跨几何的比较。",
        "原文提纲 1.0.2 把证明分成四步：中心层与 Wakimoto 层 → Springer 几何与函子 → IW 侧的构造 → 最后的等价。这四步就是本包 A–D 四条轨。",
    ],
    formulas=[
        "$M^{\\mathrm{asph}}:=\\mathbb Z\\otimes_{\\mathbb Z[W]}\\mathbb Z[W_{\\mathrm{ext}}]$",
        "$[\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})]\\;\\cong\\;M^{\\mathrm{asph}}$",
        "$\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\simeq\\mathcal D^b\\mathcal P_I^{\\mathrm{asph}}\\simeq\\mathcal D^b\\mathcal P_{\\mathrm{IW}}$",
    ],
    theorems=[
        {
            "name": "三种描述",
            "statement": "反球模同时是 $\\mathrm{Rep}(G^\\vee)$ 的 $K$ 群、$G^\\vee$-等变凝聚层的 $K$ 群、以及 $q$-形变 Whittaker 模；三条路线各产生一个范畴化候选。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "把 $M^{\\mathrm{asph}}$ 写成诱导表示，$\\mathbb Z[W]$ 通过符号表示作用在 $\\mathbb Z$ 上。", "why": "原文式 (1) 的定义就是这样写的。"},
                    {"no": 2, "text": "用 $K$ 群同构把 $M^{\\mathrm{asph}}$ 与 Springer 解消上的凝聚层联系起来。", "why": "原文式 (2)；这是 B 轨一切构造的出发点。"},
                    {"no": 3, "text": "$q$-形变到 Whittaker 模后，用函数–层字典把它提升成 IW 反常层范畴。", "why": "原文 §4.1–§4.2 的构造；要求先离开 Betti 设置。"},
                ],
                "gap_note": "原文只作陈述，未给三条描述等价的证明，把历史归给 [ArBe] 与 [Gai2]。",
            },
            "source": "A p.1",
        }
    ],
    pitfalls=[
        "「同一 $K$ 群」不等于「同一范畴」：$\\mathcal P_I^{\\mathrm{asph}}$ 与 $\\mathcal P_{\\mathrm{IW}}$ 的 $K_0$ 相同，但它们的 $\\mathrm{Hom}$ 与 $t$-结构都不是显然对齐的。",
        "不要把第三条描述读成「$q$-形变是技术手段」：它是把 $p$ 进函数论翻成几何的入口，没有它就没有 IW 侧。",
    ],
    related=[
        f"{PKG}/concept/ab-equivalence-theorem",
        f"{PKG}/concept/antispherical-module",
        f"{PKG}/concept/iw-category",
    ],
    sources=[src([1, 1], "A p.1", "§1")],
    provenance_note="三条描述与「三种范畴化」出自原文 §1（p.1）；提纲四步取自 p.1–2 的 Outline 1.0.2。",
)

CARDS["concepts/ab-equivalence-theorem"] = card(
    "concepts", "ab-equivalence-theorem",
    title="主定理：三向等价（定理 5.0.1 与推论 5.0.2）",
    aliases=["AB 等价", "主定理", "Theorem 5.0.1"],
    track="O",
    summary="梗概：合成函子 $\\mathrm{F}^{\\mathrm{IW}}=\\mathrm{Av}^{\\mathrm{IW}}\\circ\\mathrm{F}$ 给出 $\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\simeq\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$；由此再得五个范畴两两等价。",
    question="主定理说的是哪两个范畴等价，推论 5.0.2 的五个范畴又是怎么串起来的？",
    definition={
        "text": "定理 5.0.1：函子 $\\mathrm{F}^{\\mathrm{IW}}\\colon\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\to\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$ 是范畴等价。推论 5.0.2：$\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})$、$\\mathcal D^b\\mathcal P_I^{\\mathrm{asph}}$、$\\mathcal D^b\\mathcal P_{\\mathrm{IW}}$、$\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$、$\\mathcal D^b\\mathcal P_I$ 五个范畴之间，原文画出的等价关系两两相连。",
        "notation": "$\\mathrm{F}^{\\mathrm{IW}}$ 是 $\\mathrm{Av}^{\\mathrm{IW}}\\circ\\mathrm{F}$；$\\mathrm{F}$ 是 §3.4 从凝聚层到反球侧的全忠实嵌入的上升。",
    },
    key_points=[
        "证明分两半：本质满射由对象对应表（式 (7)）加同调代数得到；全忠实由 $\\mathrm{Hom}$ 计算（式 (8)）落到 $\\mathcal O_{\\widetilde{\\mathcal N}}$ 与 $V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)[n]$ 这两种生成元上。",
        "全忠实那一步的关键是两边的 $\\mathrm{Hom}$ 维数都等于 $\\dim V_{-\\lambda}$（$n=0$）或 $0$（$n\\ne 0$），一边来自凝聚层的直和分解，一边来自定理 4.5.1 的倾斜层重数。",
        "推论 5.0.2 不是把定理重复五遍：它说明反球侧与 IW 侧由 $\\mathrm{Av}^{\\mathrm{IW}}$ 连接，而 $\\mathrm{Av}^{\\mathrm{IW}}$ 在反常层上经反球商分解、并且全忠实。",
        "$\\mathcal D^b\\mathcal P_I$（非反球）也出现在推论里，但 $\\mathrm{Fl}_G\\to\\mathrm{Gr}_G$ 的实现在这种情况下不是等价——原文在 §3.4 末尾特别提醒过。",
    ],
    formulas=[
        "$\\mathrm{F}^{\\mathrm{IW}}:=\\mathrm{Av}^{\\mathrm{IW}}\\circ\\mathrm{F}$",
        "$\\dim\\mathrm{Hom}(\\mathcal O_{\\widetilde{\\mathcal N}},V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)[n])=\\dim V_{-\\lambda}\\ (n=0),\\quad 0\\ (n\\ne 0)$",
    ],
    theorems=[
        {
            "name": "定理 5.0.1（Arkhipov–Bezrukavnikov）",
            "statement": "$\\mathrm{F}^{\\mathrm{IW}}\\colon\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\to\\mathcal D^b_{\\mathrm{IW}}(\\mathrm{Fl}_G)$ 是范畴等价。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "本质满射：用式 (7) 的对象对应，$\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)$ 的像经 $\\mathrm{Av}^{\\mathrm{IW}}$ 落到 $\\Delta^{\\mathrm{IW}}_\\lambda$ 的类，$V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}$ 的像落到倾斜层 $T^{\\mathrm{IW}}(V)$；生成元都在像里，再用同调代数。", "why": "式 (7) 是原文给出的唯一对象级对照；$T^{\\mathrm{IW}}(V)$ 的倾斜性由定理 4.5.1 保证。"},
                    {"no": 2, "text": "全忠实：由 $5$-引理化到 $F=\\mathcal O_{\\widetilde{\\mathcal N}}$、$G=V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)[n]$。", "why": "引理 3.1.1 说这两类生成 $\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})$。"},
                    {"no": 3, "text": "左边直和分解得 $\\dim V_{-\\lambda}$（$n=0$）或 $0$；右边用 $\\mathrm{Hom}(\\Delta^{\\mathrm{IW}}_0,Z^{\\mathrm{IW}}(V)\\star\\mathbb W_\\lambda[n])$ 与定理 4.5.1 的重数公式，得同一答案。", "why": "两边同维，故式 (8) 是同构；这也说明单值性已由倾斜层的重数完全编码。"},
                ],
                "gap_note": "原文只给证明梗概；「本质满射」与 $5$-引理的具体同调代数推演未展开。",
            },
            "source": "A p.12",
        }
    ],
    pitfalls=[
        "定理 5.0.1 的 $\\mathrm{F}^{\\mathrm{IW}}$ 是**合成**（先 §3.4 的 $\\mathrm{F}$，再 $\\mathrm{Av}^{\\mathrm{IW}}$），不是单个几何构造；把两步混为一谈会看不出反球商在哪里起作用。",
        "推论 5.0.2 里的 $\\sim$ 不是「都相等」：$\\mathcal D^b\\mathcal P_I$ 只在中间、且与反球侧的关系是 Serre 商，不是等价。",
    ],
    related=[
        f"{PKG}/concept/functor-fiw",
        f"{PKG}/deriv/fully-faithful-hom",
        f"{PKG}/concept/three-categorifications",
    ],
    sources=[src([11, 12], "A p.12", "§5")],
    provenance_note="定理陈述与证明梗概出自 p.11–12；对象对应表与 $\\mathrm{Hom}$ 计算在 p.11–12 的式 (7)(8)。",
)



def write_cards(cards, only=None):
    n = 0
    for rel, c in cards.items():
        if only and not rel.startswith(only):
            continue
        p = ROOT / "cards" / (rel + ".json")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(c, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n += 1
    return n


if __name__ == "__main__":
    print("wrote", write_cards(CARDS))
