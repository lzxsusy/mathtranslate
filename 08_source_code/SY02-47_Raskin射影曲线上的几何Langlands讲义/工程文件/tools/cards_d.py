# -*- coding: utf-8 -*-
"""五张 correction 卡：把底本笔误的原文、修正、理由与外部佐证拆成可检索单元。

与 cards_c.py 里的 abel-jacobi-fiber、perverse-lisse-swap 同属一套，
但每张只处理一处笔误，便于资料卡层面单独引用。
"""

from __future__ import annotations

SRC = (
    "Sam Raskin (lecturer), Lin Chen (notes), "
    "Notes for ``Geometric Langlands for Projective Curves'', "
    "July 07--11, 2025, 18 pp."
)

CARDS = [
    {
        "id": "raskin_glc/correction/bh1-vs-bh0",
        "type": "correction",
        "track": "B",
        "title": "常数项证明中的 $BH^1$ 应为 $BH^0$",
        "aliases": ["BH1 vs BH0", "classifying stack erratum"],
        "summary": "命题 2.1.5 的证明说 $q_d$ 的纤维是 $BH^1(X,L)$，又说 $H^1(X,L)$ 可缩；但 $d>2g-2$ 时 $H^1=0$，正确纤维是 $R\\Gamma(X,L)[1]\\simeq H^0(X,L)[1]$，即 $BH^0(X,L)$。把 $H^1$ 与 $H^0$ 混为一谈会让读者以为扩张空间平凡，实际上扩张仍有 $H^0$ 的自同构。",
        "question": "为什么 $BH^1$ 与 $BH^0$ 的差别不影响 $q_{d,*}$ 是等价这一结论？",
        "location": "§2.1，命题 2.1.5 的证明，原文 p.6（译文 p.8）",
        "original": "the fiber of $q_d$ at a point $L\\in\\Bun^d_{\\Gm}$ can be identified with the classifying stack $BH^1(X,L)$.",
        "corrected": "the fiber is the vector stack $R\\Gamma(X,L)[1]\\simeq H^0(X,L)[1]$ for $d>2g-2$, i.e. $BH^0(X,L)$.",
        "why": "对 $0\\to L\\to\\cE\\to\\cO\\to0$，自同构群为 $\\Hom(\\cO,L)=H^0(X,L)$，所以分类叠的连通分量由 $H^0$ 给出；用 $\\Ext^1(\\cO,L)=H^1(X,L)$ 描述的是扩张的切空间，不是纤维的群。$d>2g-2$ 时 $H^1(X,L)=0$，故 $R\\Gamma(X,L)[1]\\simeq H^0(X,L)[1]$。$BH^1$ 若按字面理解则为 $B0=\\mathrm{pt}$，这会把「扩张空间」误读成单点；原文脚注 1 写的 $R\\Gamma(X,L)[1]$ 才是正确的一般陈述。结论仍对：$H^0$ 是向量空间，$\\Shv(BH^0)\\simeq\\Vect$，故 $q_{d,*}$ 仍是等价。",
        "note": "译文正文照录 $BH^1$ 并保留「$H^1$ 可缩」的原文措辞，脚注给出 $BH^0$ 与 $R\\Gamma[1]$ 两种正确写法；这是「照录原文 + 批注」而非静默改字。",
        "sources": [
            {
                "book": SRC,
                "section": "§2.1，命题 2.1.5 的证明",
                "pages": [6],
                "anchor": "源码/sections/s02-cusp.tex:L65-L80（正文与译注）",
                "quote": "the fiber of qd at a point L ∈Bund Gm can be identified1 the classifying stack BH1(X,L).",
            }
        ],
        "related": [
            "raskin_glc/concept/cuspidal-sheaf",
            "raskin_glc/derivation/cuspidal-vanishing",
        ],
        "rights": "rewritten",
        "status": "dev",
        "verification": {
            "status": "partial",
            "checked_on": "2026-11-27",
            "checks": [
                {
                    "source": "底本脚注 1（A）",
                    "entry": "命题 2.1.5 的脚注",
                    "asserts": "对任意 d，纤维可典范地等同于向量叠 RΓ(X,L)[1]；d>2g-2 时它等于 H^0[1]=BH^0。",
                    "verdict": "supports",
                },
                {
                    "source": "Drinfeld–Gaitsgory, Geometric constant term functor(s), Selecta Math. 22 (2016)",
                    "entry": "§2",
                    "url": "https://doi.org/10.1007/s00029-016-0269-3",
                    "asserts": "常数项函子的纤维计算与第二伴随的框架；支持「纤维是 RΓ[1] 型向量叠」而不是 BH^1。",
                    "verdict": "supports",
                },
                {
                    "source": "标准事实 Ext^1(O,L)=H^1(X,L)",
                    "entry": "扩张的分类",
                    "asserts": "H^1 描述扩张的切空间；H^0 描述自同构群，故纤维的分类叠由 H^0 给出。",
                    "verdict": "supports",
                },
            ],
            "note": "结论「q_{d,*} 为等价」不变；错的是纤维的群，不是证明的走向。",
        },
    },
    {
        "id": "raskin_glc/correction/b-vs-e-borel-sequence",
        "type": "correction",
        "track": "B",
        "title": "Borel 正合列中的 $B$ 应为 $\\cE$",
        "aliases": ["B vs E", "0 to L to B to O"],
        "summary": "命题 2.1.5 的证明写 $0\\to L\\to B\\to\\cO\\to0$ 分裂，其中 $B$ 应为秩 2 向量丛 $\\cE$。$B$ 在同页是 Borel 子群，不能充当正合列的中项；同页定义 2.1.1 与脚注都用 $\\cE$。",
        "question": "为什么把 $\\cE$ 写成 $B$ 不是无害的排版问题？",
        "location": "§2.1，命题 2.1.5 的证明，原文 p.6（译文 p.8）",
        "original": "the corresponding sequence $0\\to L\\to B\\to\\cO\\to0$ splits.",
        "corrected": "the corresponding sequence $0\\to L\\to\\cE\\to\\cO\\to0$ splits.",
        "why": "此处 $B$ 已在同页被定义为 $\\mathrm{PGL}_2$ 的标准 Borel 子群 $B\\subset\\mathrm{PGL}_2$，是群而非向量丛；正合列的中项是 $B$-约化所对应的秩 2 向量丛 $\\cE$（定义 2.1.1 记作 $\\cE$）。若把 $B$ 读成 Borel 子群，正合列 $0\\to L\\to B\\to\\cO\\to0$ 在类型上就不成立。",
        "note": "译文正文照录 $B$，脚注说明应为 $\\cE$；这是同一符号在一页内承担两个对象的典型冲突。",
        "sources": [
            {
                "book": SRC,
                "section": "§2.1，命题 2.1.5 的证明",
                "pages": [6],
                "anchor": "源码/sections/s02-cusp.tex:L62-L64（正文与译注）",
                "quote": "the corresponding sequence 0 →L →B →O →0 splits.",
            }
        ],
        "related": [
            "raskin_glc/concept/cuspidal-sheaf",
        ],
        "rights": "rewritten",
        "status": "dev",
        "verification": {
            "status": "partial",
            "checked_on": "2026-11-27",
            "checks": [
                {
                    "source": "底本 §2.1（A）",
                    "entry": "定义 2.1.1 与命题 2.1.5 同页",
                    "asserts": "定义 2.1.1 用 E 记 Bun_B 上的秩 2 向量丛；B 在同页被定义为 Borel 子群。",
                    "verdict": "supports",
                },
            ],
            "note": "符号冲突由同页上下文即可判定，不需要外部文献。",
        },
    },
    {
        "id": "raskin_glc/correction/holonomic-vs-holomorphic",
        "type": "correction",
        "track": "B",
        "title": "「holonomic 模形式」应为「holomorphic 模形式」",
        "aliases": ["holonomic vs holomorphic", "modular form erratum"],
        "summary": "原文写「a (holonomic) modular form」，括号里的 holonomic 应为 holomorphic（全纯）。holonomic 是 D-模的有限性条件，与模形式的全纯性无关；上下文正在定义权 k、级 1 的模形式，只能是全纯。",
        "question": "holonomic 与 holomorphic 只差一个字母，为什么不能算拼写瑕疵？",
        "location": "§2.2，模形式动机，原文 p.7（译文 p.8）",
        "original": "Recall a (holonomic) modular form (of weight $k$ and level 1) is a sum ...",
        "corrected": "Recall a holomorphic modular form (of weight $k$ and level 1) is a sum ...",
        "why": "模形式按全纯性分为全纯模形式与非全纯（Maass）情形；这里要的是 $q$-展开 $f=\\sum a_nq^n$、$f(g\\tau)=(c\\tau+d)^kf(\\tau)$ 的全纯模形式。holonomic 是 $D$-模的术语（holonomic $D$-module），指解的有限维性，与「模形式是否全纯」不是同一层面的性质。",
        "note": "译文正文照录 holonomic 并加注；这是「术语误植」而非普通拼写错误，因为两个词各自都有确定含义。",
        "sources": [
            {
                "book": SRC,
                "section": "§2.2，模形式动机",
                "pages": [7],
                "anchor": "源码/sections/s02-cusp.tex:L147（正文与译注）",
                "quote": "Recall a (holonomic) modular form (of weight k and level 1) is a sum f =",
            }
        ],
        "related": [
            "raskin_glc/concept/coefficient-functor",
        ],
        "rights": "rewritten",
        "status": "dev",
        "verification": {
            "status": "partial",
            "checked_on": "2026-11-27",
            "checks": [
                {
                    "source": "nLab, modular form",
                    "entry": "Definition",
                    "url": "https://ncatlab.org/nlab/show/modular+form",
                    "last_revised": "2025-04-10",
                    "asserts": "模形式是上半平面上的全纯函数，并满足 SL_2(Z) 的变换规则；支持 holomorphic。",
                    "verdict": "supports",
                },
                {
                    "source": "Diamond–Shurman, A First Course in Modular Forms, GTM 228",
                    "entry": "Ch. 1",
                    "asserts": "全纯模形式的定义与 q-展开；holonomic 不在模形式的标准术语中。",
                    "verdict": "supports",
                },
            ],
            "note": "holonomic 作为 D-模术语本身另有含义，故本条不是纯拼写表能覆盖的。",
        },
    },
    {
        "id": "raskin_glc/correction/rep-g-vs-rep-gdual",
        "type": "correction",
        "track": "B",
        "title": "$\\Gd$-局部系统的函子定义误写 $\\Rep(G)$",
        "aliases": ["Rep(G) vs Rep(Gdual)", "dual group erratum"],
        "summary": "原文把 $\\Gd$-局部系统定义为右 t-正合对称幺半函子 $\\Rep(G)\\to\\Shv(X)$；按上下文（$\\Gd$-局部系统、$V_\\sigma$、下一句 $V\\in\\Rep(\\Gd)$）应为 $\\Rep(\\Gd)\\to\\Shv(X)$。$\\Rep(G)$ 是 $G$-丛的表示，方向正好相反。",
        "question": "为什么 $\\Rep(G)$ 与 $\\Rep(\\Gd)$ 不能互换？",
        "location": "§4.1，$\\Gd$-局部系统的定义，原文 p.12（译文 p.14）",
        "original": "$\\Rep(G)\\to\\Shv(X),\\quad V\\mapsto V_\\sigma$.",
        "corrected": "$\\Rep(\\Gd)\\to\\Shv(X),\\quad V\\mapsto V_\\sigma$.",
        "why": "$G$-丛 $P_G$ 给出函子 $\\Rep(G)\\to\\QCoh(S)$，$V\\mapsto V_{P_G}$；对偶地，$\\Gd$-局部系统给出函子 $\\Rep(\\Gd)\\to\\Shv(X)$，$V\\mapsto V_\\sigma$。原文上一段刚用 $\\Rep(G)\\to\\QCoh(S)$ 定义 $G$-丛，紧接着的 $\\Gd$-局部系统若仍写 $\\Rep(G)$，就把两个方向混同了；下一句「若 $V\\in\\Rep(\\Gd)$ 有限维，则 $V_\\sigma$ 是 lisse 的」也证明这里应是 $\\Rep(\\Gd)$。",
        "note": "译文正文照录 $\\Rep(G)$，脚注给出 $\\Rep(\\Gd)$；这是「对偶群写漏 check」的典型，不是排版。",
        "sources": [
            {
                "book": SRC,
                "section": "§4.1，$\\Gd$-局部系统的定义",
                "pages": [12],
                "anchor": "源码/sections/s04-hecke.tex:L35-L38（正文与译注）",
                "quote": "Rep(G) →Shv(X), V ↦Vσ.",
            }
        ],
        "related": [
            "raskin_glc/concept/geometric-satake",
            "raskin_glc/concept/hecke-eigensheaf",
        ],
        "rights": "rewritten",
        "status": "dev",
        "verification": {
            "status": "partial",
            "checked_on": "2026-11-27",
            "checks": [
                {
                    "source": "底本 §4.1 上下文（A）",
                    "entry": "紧邻的上一段与下一句",
                    "asserts": "上一段用 Rep(G)→QCoh(S) 定义 G-丛；下一句写 V∈Rep(Ĝ)，V_σ lisse。",
                    "verdict": "supports",
                },
                {
                    "source": "Gaitsgory–Raskin, GLC I, arXiv:2405.03599",
                    "entry": "§1.2",
                    "url": "https://arxiv.org/abs/2405.03599",
                    "asserts": "Ĝ-局部系统是 Rep(Ĝ)→Shv(X) 的对称幺半函子；确认方向。",
                    "verdict": "supports",
                },
            ],
            "note": "修正不涉及任何定理内容，只恢复对偶群记号。",
        },
    },
    {
        "id": "raskin_glc/correction/vilonon-spelling",
        "type": "correction",
        "track": "B",
        "title": "作者名 Vilonen 被拼成 Vilonon",
        "aliases": ["Vilonon", "Vilonen spelling"],
        "summary": "定理 5.1.7 的标题把作者之一 Vilonen 拼成 Vilonon。这是人名排印错误，不影响定理内容；正确拼写见 FGV 的两篇原始论文。",
        "question": "人名拼错为什么仍值得单列一张 correction 卡？",
        "location": "§5.1，定理 5.1.7 的标题，原文 p.16（译文 p.18）",
        "original": "Theorem 5.1.7 (Beraldo, Frenkel–Gaitsgory–Vilonon).",
        "corrected": "Theorem 5.1.7 (Beraldo, Frenkel–Gaitsgory–Vilonen).",
        "why": "Vilonen 是 FGV 三篇的核心作者之一；把名字写错会妨碍读者按作者检索原始文献。底本在其他位置也写作 Vilonen（如定理 3.3.1 的署名），只有 p.16 这一处误作 Vilonon。",
        "note": "译文正文保留原文拼写并加脚注，属于「原文笔误照录」；人名不译。",
        "sources": [
            {
                "book": SRC,
                "section": "§5.1，定理 5.1.7",
                "pages": [16],
                "anchor": "源码/sections/s05-whittaker.tex:L133-L137（标题与译注）",
                "quote": "Theorem 5.1.7 (Beraldo, Frenkel–Gaitsgory–Vilonon).",
            }
        ],
        "related": [
            "raskin_glc/concept/whittaker-coefficient",
            "raskin_glc/concept/geometric-satake",
        ],
        "rights": "rewritten",
        "status": "dev",
        "verification": {
            "status": "partial",
            "checked_on": "2026-11-27",
            "checks": [
                {
                    "source": "Crossref, DOI 10.2307/2661366",
                    "entry": "Frenkel–Gaitsgory–Vilonen, Whittaker patterns in the geometry of moduli spaces of bundles on curves, Ann. of Math. 153 (2001), 699–748",
                    "url": "https://doi.org/10.2307/2661366",
                    "asserts": "作者名为 Vilonen。",
                    "verdict": "supports",
                },
                {
                    "source": "Crossref, DOI 10.1090/S0894-0347-01-00388-5",
                    "entry": "Frenkel–Gaitsgory–Vilonen, On the geometric Langlands conjecture, J. Amer. Math. Soc. 15 (2002), 367–417",
                    "url": "https://doi.org/10.1090/S0894-0347-01-00388-5",
                    "asserts": "作者名为 Vilonen；arXiv:math/0012255 同。",
                    "verdict": "supports",
                },
            ],
            "note": "纯人名排印错误；不影响任何数学陈述。",
        },
    },
]
