# -*- coding: utf-8 -*-
"""Build the Ben-Zvi GLC concept cards (bzg/concept/*)."""
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "cards", "concepts")
BOOK = ("David Ben-Zvi, What is the Geometric Langlands Correspondence about? "
        "(arXiv:2605.23167v1, 2026-05-22, 34 pp., CC BY 4.0)")
SECTION_PAGES = {}

SUMMARY_OVERRIDES = {
    "glc-statement": "无分歧情形下，Bun_G 上的层范畴等价于 Loc_Ǧ 上的 IndCoh_N，并保持 QCoh 作用。",
    "betti-mellin": "Z-表示等价于 C^×_t 上凝聚层；C^×_z 上局部系统也等价于 QCoh(C^×_t)。",
    "gl1-betti-glc": "GL_1 的 Betti GLC：Jac(C) 上的局部系统等价于 (C^×)^{2g} 上的凝聚层，由 Fourier–Mukai 实现。",
    "gl1-derham-glc": "GL_1 的 de Rham GLC：Jac(C) 上的 D-模等价于 Loc^{dR}_{GL_1} 上的凝聚层。",
    "picard-jacobian": "Pic(C) ≅ Z × Jac(C)；Jac(C) 是 2g 维复环面，实同构于 (S^1)^{2g}。",
    "spectral-action": "QCoh(Loc_Ǧ) 作用在 Shv(Bun_G) 上，特征值由 Ǧ-局部系统给出。",
    "dolbeault-glc": "Dolbeault GLC：Higgs_G 与 Higgs_Ǧ 上的凝聚层等价，即 Hitchin 系统的 SYZ 镜像。",
}


def T(name, statement, steps, gap_note, source):
    return {
        "name": name,
        "statement": statement,
        "proof": {
            "status": "sketch",
            "steps": [
                {"no": i + 1, "text": text, "why": why}
                for i, (text, why) in enumerate(steps)
            ],
            "gap_note": gap_note,
        },
        "source": source,
    }


def C(slug, track, title, aliases, summary, question, definition, notation,
      key_points, formulas, theorems, pitfalls, related, section, pages):
    summary = SUMMARY_OVERRIDES.get(slug, summary)
    if len(summary) > 120:
        print("WARN summary %s: %d" % (slug, len(summary)))
    assert question.rstrip().endswith("？"), slug
    assert len(key_points) >= 3, slug
    assert len(formulas) >= 1, slug
    assert len(pitfalls) >= 1, slug
    assert len(related) >= 2, slug
    assert len(set(pages)) == len(pages), slug
    return {
        "id": "bzg/concept/" + slug,
        "type": "concept",
        "track": track,
        "title": title,
        "aliases": aliases,
        "summary": summary,
        "question": question,
        "definition": {"text": definition, "notation": notation},
        "key_points": key_points,
        "formulas": formulas,
        "theorems": theorems,
        "pitfalls": pitfalls,
        "related": related,
        "sources": [{
            "book": BOOK,
            "section": section,
            "pages": pages,
            "pdf_pages": pages,
            "anchor": "arXiv:2605.23167 %s, p.%d" % (section, pages[0]),
        }],
        "rights": "rewritten",
        "status": "reviewed",
        "verification": {
            "status": "source-only",
            "checked_on": "2026-11-26",
            "checks": [{
                "source": "arXiv",
                "entry": "Ben-Zvi 2026, %s" % section,
                "url": "https://arxiv.org/abs/2605.23167",
                "last_revised": "2026-05-22",
                "asserts": "本卡内容逐句对齐该节；尚未在 nLab / Stacks Project 找到逐字对应的外部核验页。",
                "verdict": "source-only",
            }],
        },
    }


cards = []

# ---------------------------------------------------------------- O 总览
cards.append(C(
    "glc-overview", "O", "几何 Langlands 对应：非阿贝尔的范畴 Fourier 变换",
    ["geometric Langlands correspondence", "几何 Langlands 纲领", "GLC"],
    "曲线 \\(C\\) 上 \\(G\\)-丛的自守层范畴与对偶群 \\(\\check G\\) 的谱侧范畴之间的等价，是 Fourier 变换的非阿贝尔、范畴化版本。",
    "几何 Langlands 对应到底把什么和什么对应起来，为什么说它是非阿贝尔 Fourier 变换？",
    r"设 \\(C\\) 是光滑射影曲线（或紧 Riemann 面），\\(G\\) 是约化群，\\(\\check G\\) 是其 Langlands 对偶群。几何 Langlands 对应（GLC）预测自守侧 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\)（de Rham 或 Betti 层范畴）与谱侧 \\(\\operatorname{IndCoh}_{\\mathcal N}(\\operatorname{Loc}_{\\check G})\\) 之间的等价；Hecke 算子的作用对应 \\(\\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})\\) 的张量作用。",
    r"\\(\\operatorname{Bun}_G\\)：\\(C\\) 上 \\(G\\)-丛的模叠；\\(\\operatorname{Loc}_{\\check G}\\)：\\(\\check G\\)-局部系统的特征簇；\\(\\mathcal N\\)：整体幂零锥，用来标记允许的奇异支撑。",
    [
        "自守侧是“函数/层”的一侧，谱侧是“特征值/局部系统”的一侧，对应把 Hecke 算子对角化。",
        "它是 Fourier 变换的范畴化：平移、微分、卷积分别变成张量、Hecke 作用与谱侧乘法。",
        "当 \\(G=GL_1\\) 时退化为 Jacobian 与 \\(\\operatorname{Loc}_{GL_1}\\) 之间的 Fourier–Mukai 变换。",
        "2024 年五篇论文证明了特征零、无分歧情形；分歧、量子与 Dolbeault 变体仍未解决。",
    ],
    [
        r"\\operatorname{Shv}(\\operatorname{Bun}_G)\\simeq \\operatorname{IndCoh}_{\\mathcal N}(\\operatorname{Loc}_{\\check G})",
        r"\\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})\\curvearrowright \\operatorname{Shv}(\\operatorname{Bun}_G)",
    ],
    [],
    [
        "不要把 GLC 说成“自守表示与 Galois 表示的逐一对应”：几何版本对应的是范畴，不是单个表示。",
        "完整陈述必须用 \\(\\operatorname{IndCoh}_{\\mathcal N}\\)，不能用朴素 \\(\\operatorname{QCoh}\\)；后者在奇异点处不够。",
    ],
    ["bzg/concept/glc-statement", "bzg/concept/categorical-harmonic-analysis", "bzg/concept/dual-group"],
    "§1", [3],
))

cards.append(C(
    "glc-statement", "O", "无分歧几何 Langlands 主定理（精确形式）",
    ["unramified geometric Langlands theorem", "GLC 主定理", "Theorem 2.5"],
    "在特征零、无分歧情形，\\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\simeq \\operatorname{IndCoh}_{\\mathcal N}(\\operatorname{Loc}_{\\check G})\\)，且保持 \\(\\operatorname{QCoh}\\) 作用。",
    "2024 年被证明的几何 Langlands 定理的精确陈述是什么，它比“\\(\\operatorname{Shv}\\simeq \\operatorname{QCoh}\\)”多了什么修正？",
    r"对光滑射影曲线 \\(C\\) 与约化群 \\(G\\)，存在范畴等价 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\simeq \\operatorname{IndCoh}_{\\mathcal N}(\\operatorname{Loc}_{\\check G})\\)（de Rham 与 Betti 两种 flavor），它把 \\(\\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})\\) 在右边的自然张量作用对应到左边的谱作用。对每个 \\(E\\in \\operatorname{Loc}_{\\check G}\\)，特征层 \\(\\operatorname{Aut}_E\\) 满足 \\(F*\\operatorname{Aut}_E\\simeq F|_E\\otimes \\operatorname{Aut}_E\\)。",
    r"\\(\\operatorname{Shv}\\)：de Rham 时是 \\(\\operatorname{DMod}\\)，Betti 时是 \\(\\operatorname{Shv}_{\\mathcal N}\\)；\\(\\mathcal N\\) 是 \\(\\operatorname{Loc}_{\\check G}\\) 的整体幂零锥；\\(F|_E\\) 是 \\(F\\) 在点 \\(E\\) 的纤维。",
    [
        "这是定理，不再是猜想：五篇论文（GR24a、ABC+24b、CCF+24、ABC+24a、GR24b）合起来证明。",
        "两边都是导出/\\(\\infty\\)-范畴；等价的“函数”版本必须换成 \\(\\operatorname{IndCoh}_{\\mathcal N}\\) 才成立。",
        "等价保持谱作用，因此把 Hecke 特征层送到谱侧的肌层；这是“对角化”的精确含义。",
        "Betti 与 de Rham 两个版本通过 étale 版本相互等价。",
    ],
    [
        r"\\operatorname{Shv}(\\operatorname{Bun}_G)\\simeq \\operatorname{IndCoh}_{\\mathcal N}(\\operatorname{Loc}_{\\check G})",
        r"F*\\operatorname{Aut}_E\\simeq F|_E\\otimes \\operatorname{Aut}_E",
    ],
    [T(
        "定理 2.5（无分歧几何 Langlands）",
        r"存在保持谱作用的等价 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\simeq \\operatorname{IndCoh}_{\\mathcal N}(\\operatorname{Loc}_{\\check G})\\)。",
        [
            ("用谱作用把 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\) 分解为 Hecke 特征值。", "谱作用定理给出 \\(\\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})\\) 的作用，特征值由 \\(\\check G\\)-局部系统给出。"),
            ("用 Eisenstein 归纳把问题约化到尖点层。", "抛物诱导与 Langlands 函子相容，Eisenstein 部分可被“减掉”。"),
            ("用 Whittaker 层证明单射性，用 Kac–Moody 局部化构造足够多的尖点层。", "Whittaker 系数不消灭尖点层；opers 给出足够多的 Langlands 参数。"),
            ("用 ambidexterity 与重数一收尾。", "GR24b 证明所有特征空间重数一，从而得到等价。"),
        ],
        "Ben-Zvi 的 survey 只给证明架构，完整证明在五篇论文中；尚未形式化。",
        "§2.5 主定理 / p.13",
    )],
    [
        "朴素猜测 \\(\\operatorname{Shv}\\simeq \\operatorname{QCoh}\\) 是错的：谱侧要允许“广义函数”，即 \\(\\operatorname{IndCoh}\\)，并限制幂零奇异支撑。",
        "de Rham 与 Betti 不是同一个范畴；它们通过 étale 版本比较，不能混用。",
    ],
    ["bzg/concept/glc-overview", "bzg/concept/indicoh-nilpotent-support", "bzg/concept/spectral-action"],
    "§2.5", [13],
))

cards.append(C(
    "proof-map", "O", "五篇论文的证明架构",
    ["five papers", "GLC proof architecture", "GR24a ABC+24b CCF+24 ABC+24a GR24b"],
    "无分歧 GLC 的证明由五篇论文组成：构造 Langlands 函子、Kac–Moody 构造尖点层、Eisenstein 归纳、ambidexterity、重数一。",
    "几何 Langlands 的五篇证明论文各自负责什么，为什么按这个顺序拼起来才能得到主定理？",
    r"证明的主线是：先构造 Langlands 函子 \\(\\mathbb L_G:\\operatorname{Shv}(\\operatorname{Bun}_G)\\to \\operatorname{IndCoh}_{\\mathcal N}(\\operatorname{Loc}_{\\check G})\\)（GR24a）；用 Kac–Moody 局部化构造尖点自守层（ABC+24b）；用 Eisenstein 级数做归纳、约化到尖点情形（CCF+24）；证明函子满足 ambidexterity（ABC+24a）；最后证明所有特征空间重数一（GR24b）。",
    r"\\(\\mathbb L_G\\)：Langlands 函子；ambidexterity：函子同时保持 \\(*\\) 与 \\(!\\) 的极限/余极限性质；尖点层：Eisenstein 周期的正交补。",
    [
        "GR24a：构造 \\(\\mathbb L_G\\)，并证明它在 Whittaker 层上的性质。",
        "ABC+24b：用临界水平 Kac–Moody 表示与 Beilinson–Bernstein 局部化构造尖点层。",
        "CCF+24：证明 Eisenstein 级数与抛物诱导兼容，把一般情形归约到尖点情形。",
        "ABC+24a：证明 \\(\\mathbb L_G\\) 的 ambidexterity，给出足够好的函子性质。",
        "GR24b：证明重数一，从而 \\(\\mathbb L_G\\) 是等价。",
    ],
    [
        r"\\operatorname{Shv}(\\operatorname{Bun}_G)\\xrightarrow{\\mathbb L_G}\\operatorname{IndCoh}_{\\mathcal N}(\\operatorname{Loc}_{\\check G})",
        r"\\mathbb L_G\\ \\text{is an equivalence}\\ \\Longleftarrow\\ \\text{Eisenstein}+\\text{Whittaker}+\\text{Kac--Moody}+\\text{ambidexterity}",
    ],
    [],
    [
        "五篇论文不是按 arXiv 编号顺序读就能懂：survey 建议先读综述性引言，再按“函子—构造—归纳—收尾”的顺序。",
        "不要把“ambidexterity”当成技术细节；它是把单射性提升为等价的关键。",
    ],
    ["bzg/concept/glc-statement", "bzg/concept/eisenstein-series", "bzg/concept/whittaker-period", "bzg/concept/kac-moody-opers"],
    "§5", [20, 26],
))

cards.append(C(
    "categorical-harmonic-analysis", "O", "范畴调和分析：从函数到层",
    ["categorical harmonic analysis", "范畴化调和分析", "six functors"],
    "把 Hilbert 空间换成导出范畴、算子换成函子、函数换成层，得到几何 Langlands 所需的“范畴调和分析”。",
    "为什么几何 Langlands 可以看成调和分析，它把普通调和分析的哪些对象替换成了什么？",
    r"普通调和分析研究函数空间上的算子；范畴调和分析把函数空间换成层/导出范畴，把积分核换成函子，把乘法换成张量积。六函子形式体系 \\(f^*,f_*,f_!,f^!,\\otimes,\\operatorname{Hom}\\) 提供了“推前、拉回、积分、乘法”的范畴对应物。",
    r"\\(f_!\\)：紧支撑推前，类比积分；\\(f^*\\)：拉回，类比限制；\\(\\otimes\\)：张量，类比逐点乘法；\\(\\operatorname{Hom}\\)：内 Hom，类比配对。",
    [
        "向量空间 \\(\\rightsquigarrow\\) 范畴，线性算子 \\(\\rightsquigarrow\\) 函子。",
        "积分核 \\(K(x,y)\\) \\(\\rightsquigarrow\\) 核层 \\(\\mathcal K\\)，积分变换 \\(\\rightsquigarrow\\) Fourier–Mukai 型函子。",
        "逐点乘法 \\(\\rightsquigarrow\\) 张量积；内积/配对 \\(\\rightsquigarrow\\) 内 Hom 与对偶。",
        "紧支撑与增长条件在范畴侧变成 \\(!\\) 与 \\(*\\) 的选择，这正是 \\(\\operatorname{IndCoh}_{\\mathcal N}\\) 出现的原因。",
    ],
    [
        r"\\operatorname{FM}_{\\mathcal K}:\\operatorname{Shv}(X)\\to\\operatorname{Shv}(Y),\\quad F\\mapsto p_{Y!}(p_X^*F\\otimes \\mathcal K)",
        r"\\text{function space}\\rightsquigarrow \\text{derived category},\\quad \\text{operator}\\rightsquigarrow \\text{functor}",
    ],
    [],
    [
        "不要把“范畴化”理解成把每个公式逐字替换：紧支撑、增长条件、导出完各性都会改变陈述。",
        "六函子不是六个独立操作；\\(f_!\\) 与 \\(f_*\\) 的差别正是“积分”与“整体截面”的差别。",
    ],
    ["bzg/concept/spectral-theorem", "bzg/concept/categorical-fourier", "bzg/concept/glc-overview"],
    "§2.1", [8],
))

# ---------------------------------------------------------------- A 谱定理 / Mellin
cards.append(C(
    "spectral-theorem", "A", "谱定理：自伴算子与直积分",
    ["spectral theorem", "谱定理", "direct integral"],
    "Hilbert 空间上的自伴算子可以西等价于“乘以 \\(t\\)”的算子，空间分解为 \\(\\mathbb R\\) 上的直积分。",
    "谱定理如何把自伴算子对角化，直积分在其中的作用是什么？",
    r"设 \\(H\\) 是 Hilbert 空间，\\(A:H\\to H\\) 是有界自伴算子。谱定理断言存在 \\(\\mathbb R\\) 上的测度 \\(\\mu\\) 与可测 Hilbert 场 \\(t\\mapsto \\mathcal H_t\\)，使得 \\(H\\cong \\int_{\\mathbb R}^{\\oplus}\\mathcal H_t\\,d\\mu(t)\\)，且 \\(A\\) 在这个分解下是“乘以 \\(t\\)”。",
    r"\\(\\int^\\oplus\\)：直积分；\\(\\mu\\)：谱测度；\\(\\mathcal H_t\\)：特征空间（可能重数 \\(>1\\)）。",
    [
        "谱定理是 Fourier 变换的抽象版本：它把算子变成乘法算子。",
        "直积分允许连续谱，因此不能只写成离散特征向量之和。",
        "函数演算 \\(f(A)\\) 通过 \\(f(t)\\) 逐点作用得到。",
        "几何 Langlands 把它范畴化：算子 \\(\\rightsquigarrow\\) Hecke 函子，特征值 \\(\\rightsquigarrow\\) 局部系统。",
    ],
    [
        r"H\\cong \\int_{\\mathbb R}^{\\oplus}\\mathcal H_t\\,d\\mu(t)",
        r"A\\ \\longleftrightarrow\\ (t\\mapsto t)",
    ],
    [T(
        "谱定理（有界自伴版本）",
        r"有界自伴算子 \\(A\\) 西等价于某个直积分上的乘法算子。",
        [
            ("用连续函数演算构造投影值测度 \\(E(\\Delta)\\)。", "自伴性保证 \\(E\\) 是正交投影值测度。"),
            ("把 \\(H\\) 分解为关于 \\(E\\) 的直积分。", "投影值测度给出可测 Hilbert 场。"),
            ("在此分解下 \\(A\\) 对应乘以 \\(t\\)。", "函数演算把 \\(A\\) 写成 \\(\\int t\\,dE(t)\\)。"),
        ],
        "survey 只引用标准谱定理；完整证明见泛函分析教材。",
        "§1.1 / p.3",
    )],
    [
        "无界算子需要定义域与自伴扩张，不能直接套有界版本。",
        "直积分不是直和；连续谱没有可数特征基。",
    ],
    ["bzg/concept/fourier-transform", "bzg/concept/algebraic-spectral-theorem", "bzg/concept/categorical-harmonic-analysis"],
    "§1.1", [3],
))

cards.append(C(
    "fourier-transform", "A", "Fourier 变换：平移与微分的对角化",
    ["Fourier transform", "Fourier 变换", "Plancherel"],
    "Fourier 变换把平移变成乘法、把微分变成乘以 \\(t\\)，从而同时对角化这些算子。",
    "Fourier 变换为什么能对角化平移与微分，Plancherel 定理在其中起什么作用？",
    r"对 \\(f\\in L^2(\\mathbb R_x)\\)，定义 \\(\\hat f(t)=\\int_{\\mathbb R} f(x)e^{-2\\pi ixt}\\,dx\\)。则 \\(\\widehat{f'(x)}=2\\pi i t\\,\\hat f(t)\\)，\\(\\widehat{f(x+a)}=e^{2\\pi iat}\\hat f(t)\\)，且 \\(\\|\\hat f\\|_2=\\|f\\|_2\\)。",
    r"\\(x\\)：位置变量；\\(t\\)：频率变量；归一化取 \\(e^{-2\\pi ixt}\\)，所以微分多出 \\(2\\pi i\\)。",
    [
        "平移算子与微分算子交换，Fourier 变换同时把它们变成乘法。",
        "卷积在 Fourier 侧变成逐点乘法，这是“积分算子对角化”的原型。",
        "Plancherel 说明变换是西的，因此是 Hilbert 空间的等价。",
        "几何 Langlands 把“函数 \\(\\rightsquigarrow\\) 层、积分 \\(\\rightsquigarrow\\) 推前”范畴化。",
    ],
    [
        r"\\hat f(t)=\\int_{\\mathbb R} f(x)e^{-2\\pi ixt}\\,dx",
        r"\\widehat{f'}(t)=2\\pi i t\\,\\hat f(t),\\qquad \\widehat{f*g}=\\hat f\\,\\hat g",
    ],
    [T(
        "Fourier 反演与 Plancherel",
        r"\\(f\\mapsto \\hat f\\) 延拓为 \\(L^2(\\mathbb R)\\) 上的酉算子，且 \\(f(x)=\\int \\hat f(t)e^{2\\pi ixt}\\,dt\\)。",
        [
            ("先在 Schwartz 函数上证明反演公式。", "Schwartz 空间使积分与求导都可交换。"),
            ("用稠密性延拓到 \\(L^2\\)。", "Plancherel 估计给出等距，稠密子空间上的等距唯一延拓。"),
        ],
        "survey 只把它作为动机；标准证明见调和分析教材。",
        "§1.2 / p.4",
    )],
    [
        "归一化不统一：有的教材用 \\(e^{-ixt}\\)，此时微分多出 \\(i\\) 而不是 \\(2\\pi i\\)。",
        "把 \\(L^2\\) 函数逐点求值没有意义；反演公式要在几乎处处或分布意义下理解。",
    ],
    ["bzg/concept/spectral-theorem", "bzg/concept/categorical-fourier", "bzg/concept/betti-mellin"],
    "§1.2", [4],
))

cards.append(C(
    "algebraic-spectral-theorem", "A", "代数谱定理：自同态与 \\(\\operatorname{QCoh}(\\mathbb C_t)\\)",
    ["algebraic spectral theorem", "代数谱定理", "C[t]-module"],
    "有限维向量空间加上一个自同态，等价于 \\(\\mathbb C[t]\\)-模，也就是 \\(\\mathbb A^1_t\\) 上的拟凝聚层。",
    "为什么“向量空间 + 一个算子”可以翻译成 \\(\\mathbb C[t]\\)-模，这个翻译保留了哪些信息？",
    r"设 \\(V\\) 是有限维复向量空间，\\(H:V\\to V\\) 是线性算子。令 \\(t\\cdot v=H(v)\\)，则 \\(V\\) 成为 \\(\\mathbb C[t]\\)-模；反之，任何有限生成 \\(\\mathbb C[t]\\)-模都给出一个算子。于是 \\(\\{V,H\\}\\) 的范畴等价于 \\(\\operatorname{QCoh}(\\mathbb C_t)\\) 的有限支持部分。",
    r"\\(t\\)：形式变量，作用为 \\(H\\)；\\(\\mathbb C[t]\\)：多项式环；\\(\\operatorname{QCoh}(\\mathbb C_t)\\)：\\(\\mathbb C[t]\\)-模的层化。",
    [
        "算子的特征值对应 \\(\\mathbb C[t]\\) 的极大理想 \\((t-\\lambda)\\)。",
        "Jordan 块对应 \\(\\mathbb C[t]\\) 的局部化/广义特征空间。",
        "这个等价是“谱定理”的代数原型：把算子变成乘法。",
        "几何 Langlands 把它升级为：向量空间 \\(\\rightsquigarrow\\) 范畴，算子 \\(\\rightsquigarrow\\) 函子。",
    ],
    [
        r"\\{V,H\\}\\ \\simeq\\ \\mathbb C[t]\\text{-}\\operatorname{Mod}\\ \\simeq\\ \\operatorname{QCoh}(\\mathbb C_t)",
        r"t\\cdot v=H(v)",
    ],
    [T(
        "代数谱定理",
        r"有限维 \\(\\mathbb C\\)-向量空间与自同态的范畴，等价于有限生成 \\(\\mathbb C[t]\\)-模的范畴。",
        [
            ("把 \\(V\\) 看成 \\(\\mathbb C[t]\\)-模：\\(t\\) 作用为 \\(H\\)。", "多项式作用由 \\(H\\) 的幂与线性组合给出。"),
            ("反过来，\\(\\mathbb C[t]\\)-模限制为 \\(\\mathbb C\\)-向量空间，\\(t\\) 的作用给出算子。", "这两个构造互为逆。"),
        ],
        "survey 只陈述等价；完整证明是线性代数。",
        "§1.3.1 / p.4",
    )],
    [
        "这里要求有限维/有限生成；无限维情形需要拓扑或完各化。",
        "\\(\\mathbb C[t]\\)-模不是 \\(\\mathbb C(t)\\)-向量空间；不要局部化掉多项式。",
    ],
    ["bzg/concept/spectral-theorem", "bzg/concept/betti-mellin", "bzg/concept/derham-mellin"],
    "§1.3", [4],
))

cards.append(C(
    "betti-mellin", "A", "Betti Mellin：\\(\\operatorname{Rep}(\\mathbb Z)\\) 与 \\(\\operatorname{QCoh}(\\mathbb C^\\times)\\)",
    ["Betti Mellin", "Betti Mellin transform", "Rep(Z)"],
    "\\(\\mathbb Z\\)-表示等价于 \\(\\mathbb C^\\times_t\\) 上的拟凝聚层；\\(\\mathbb C^\\times_z\\) 上的局部系统也等价于 \\(\\operatorname{QCoh}(\\mathbb C^\\times_t)\\)。",
    "Betti Mellin 变换如何把单值性（\\(\\mathbb Z\\)-作用）变成 \\(\\mathbb C^\\times\\) 上的拟凝聚层？",
    r"令 \\(V\\) 是 \\(\\mathbb Z\\)-表示，\\(T:V\\to V\\) 是生成元的作用。把 \\(V\\) 分成年权空间 \\(V_n=\\{v\\mid T v=n v\\}\\)（广义情形用 Jordan 分解），则 \\(V\\mapsto \\bigoplus_n V_n t^n\\) 给出 \\(\\operatorname{Rep}(\\mathbb Z)\\simeq \\operatorname{QCoh}(\\mathbb C^\\times_t)\\)。几何版本：\\(\\mathbb C^\\times_z\\) 上的局部系统由单值性给出，等价于 \\(\\operatorname{QCoh}(\\mathbb C^\\times_t)\\)。",
    r"\\(t\\)：\\(\\mathbb C^\\times\\) 的坐标；\\(T\\)：单值性算子；\\(n\\in\\mathbb Z\\)：单值性的特征值。",
    [
        "这是 \\(\\mathbb Z\\) 的“Fourier 变换”：角色 \\(z\\mapsto z^n\\) 对应 \\(t^n\\)。",
        "局部系统的单值性矩阵被对角化/约当化，得到 \\(t\\)-方向的层。",
        "rank-one 情形给出 \\(\\operatorname{Loc}_{GL_1}(\\mathbb C^\\times)\\simeq \\operatorname{QCoh}(\\mathbb C^\\times)\\)。",
        "它是 §1.3 三个 Mellin 变体中最“拓扑”的一个。",
    ],
    [
        r"\\operatorname{Rep}(\\mathbb Z)\\simeq \\operatorname{QCoh}(\\mathbb C^\\times_t)",
        r"\\operatorname{Loc}(\\mathbb C^\\times_z)\\simeq \\operatorname{QCoh}(\\mathbb C^\\times_t)",
    ],
    [T(
        "Betti Mellin 等价",
        r"\\(\\mathbb Z\\)-表示范畴与 \\(\\mathbb C^\\times_t\\) 上的拟凝聚层范畴等价。",
        [
            ("把 \\(V\\) 按 \\(T\\) 的广义特征值分解。", "有限维时用 Jordan 分解；无限维时用完各化。"),
            ("把特征值 \\(n\\) 对应到 \\(t^n\\) 的单项。", "角色 \\(n\\mapsto t^n\\) 给出 \\(\\mathbb Z\\) 与 \\(\\mathbb C^\\times\\) 的对偶。"),
        ],
        "survey 只给等价陈述；技术细节（完各化、无限维）从略。",
        "§1.3.2 / p.5",
    )],
    [
        "\\(\\mathbb C^\\times\\) 不是 \\(\\mathbb C\\)：\\(t=0\\) 被挖掉，所以只允许 Laurent 多项式。",
        "单值性可能有 Jordan 块；不能只写对角矩阵。",
    ],
    ["bzg/concept/derham-mellin", "bzg/concept/gl1-betti-glc", "bzg/concept/algebraic-spectral-theorem"],
    "§1.3", [5],
))

cards.append(C(
    "derham-mellin", "A", "de Rham Mellin：\\(D\\)-模与 \\(\\operatorname{QCoh}(\\mathbb C_s/\\mathbb Z)\\)",
    ["de Rham Mellin", "D-module Mellin", "Riemann-Hilbert"],
    "\\(\\mathbb C^\\times_z\\) 上的 \\(D\\)-模等价于 \\(\\mathbb C_s/\\mathbb Z\\) 上的拟凝聚层；微分算子 \\(z\\partial_z\\) 对应乘以 \\(s\\)。",
    "de Rham Mellin 变换如何把 \\(D\\)-模的微分方程变成 \\(\\mathbb C_s/\\mathbb Z\\) 上的代数数据？",
    r"\\(\\mathbb C^\\times_z\\) 上的 \\(D\\)-模由向量空间加上一个算子 \\(\\nabla:V\\to V\\)（或 \\(z\\partial_z\\) 的作用）描述。令 \\(z\\partial_z\\) 的特征值为 \\(s\\)，则 \\(D\\)-模对应于 \\(\\mathbb C_s/\\mathbb Z\\) 上的拟凝聚层；指数映射 \\(s\\mapsto e^{2\\pi i s}\\) 解释周期 \\(\\mathbb Z\\)。Riemann–Hilbert 对应在正则奇异情形给出局部系统与 \\(D\\)-模的等价。",
    r"\\(z\\)：\\(\\mathbb C^\\times\\) 的坐标；\\(s\\)：\\(z\\partial_z\\) 的特征值；\\(\\mathbb C_s/\\mathbb Z\\)：周期为 \\(1\\) 的商。",
    [
        "\\(z\\partial_z\\) 的特征函数是 \\(z^s\\)，特征值 \\(s\\) 只在模 \\(\\mathbb Z\\) 意义下确定。",
        "Riemann–Hilbert 把正则奇异 \\(D\\)-模与局部系统联系起来。",
        "de Rham 版本比 Betti 版本更“代数”，但需要处理完各化与正则性。",
        "它是 §2.4 中 \\(GL_1\\) de Rham 对应的局部模型。",
    ],
    [
        r"\\operatorname{DMod}(\\mathbb C^\\times_z)\\simeq \\operatorname{QCoh}(\\mathbb C_s/\\mathbb Z)",
        r"(z\\partial_z-s)\\cdot z^s=0",
    ],
    [T(
        "de Rham Mellin 等价",
        r"\\(\\mathbb C^\\times_z\\) 上的 \\(D\\)-模（正则奇异、完各化后）等价于 \\(\\mathbb C_s/\\mathbb Z\\) 上的拟凝聚层。",
        [
            ("把 \\(D\\)-模写成 \\(z\\partial_z\\) 的作用。", "\\(\\mathbb C^\\times\\) 上的 \\(D\\)-模由 \\(\\mathcal O\\) 与 \\(\\partial_z\\) 生成；\\(z\\partial_z\\) 是欧拉算子。"),
            ("按 \\(z\\partial_z\\) 的广义特征值 \\(s\\) 分解。", "特征值在 \\(s\\mapsto s+1\\) 下不变，因此得到 \\(\\mathbb C_s/\\mathbb Z\\)。"),
        ],
        "survey 只给对应；Riemann–Hilbert 的完整陈述需要正则奇异性与完各化。",
        "§1.3.3 / p.5",
    )],
    [
        "\\(s\\) 只在模 \\(\\mathbb Z\\) 意义下确定；不要把它当成单值。",
        "Riemann–Hilbert 需要正则奇异； irregular 情形要加 Stokes 结构。",
    ],
    ["bzg/concept/betti-mellin", "bzg/concept/gl1-derham-glc", "bzg/concept/algebraic-spectral-theorem"],
    "§1.3", [5],
))

cards.append(C(
    "gl1-betti-glc", "A", "\\(GL_1\\) 的 Betti 几何 Langlands",
    ["GL1 Betti GLC", "abelian Betti GLC", "Fourier-Mukai"],
    "\\(GL_1\\) 的 Betti GLC 是 \\(\\operatorname{Loc}(\\operatorname{Jac}(C))\\simeq \\operatorname{QCoh}((\\mathbb C^\\times)^{2g})\\)，由 Fourier–Mukai 实现。",
    "当 \\(G=GL_1\\) 时，几何 Langlands 对应具体是什么，为什么它是 Fourier–Mukai 变换？",
    r"对 \\(G=GL_1\\)，\\(\\operatorname{Bun}_{GL_1}=\\operatorname{Pic}(C)\\cong \\mathbb Z\\times \\operatorname{Jac}(C)\\)。Betti 谱侧是 \\(\\operatorname{Loc}_{GL_1}(C)\\cong (\\mathbb C^\\times)^{2g}\\)。GLC 断言 \\(\\operatorname{Loc}(\\operatorname{Jac}(C))\\simeq \\operatorname{QCoh}((\\mathbb C^\\times)^{2g})\\)；其核由 Abel–Jacobi 与 Poincaré 丛给出，因此是 Fourier–Mukai 型。",
    r"\\(g\\)：\\(C\\) 的亏格；\\(\\operatorname{Jac}(C)\\)：度数为零的线丛；\\(\\operatorname{Loc}_{GL_1}(C)\\)：秩一局部系统，同构于 \\((\\mathbb C^\\times)^{2g}\\)。",
    [
        "这是 GLC 的 Abel 情形，也是唯一有经典傅里叶–Mukai 解释的情形。",
        "\\(\\operatorname{Pic}(C)\\) 的度数部分给出 \\(\\mathbb Z\\)，在谱侧对应 \\((\\mathbb C^\\times)^{2g}\\) 的连通部分。",
        "Fourier–Mukai 核来自 Poincaré 丛，因此是“积分核”的几何版本。",
        "它是非阿贝尔 GLC 的模型：Hecke 算子对应张量积。",
    ],
    [
        r"\\operatorname{Loc}(\\operatorname{Jac}(C))\\simeq \\operatorname{QCoh}((\\mathbb C^\\times)^{2g})",
        r"\\operatorname{Loc}_{GL_1}(C)\\cong (\\mathbb C^\\times)^{2g}",
    ],
    [T(
        "\\(GL_1\\) 的 Betti GLC",
        r"存在 Fourier–Mukai 等价 \\(\\operatorname{Loc}(\\operatorname{Jac}(C))\\simeq \\operatorname{QCoh}(\\operatorname{Loc}_{GL_1}(C))\\)。",
        [
            ("用 Abel–Jacobi 映射把 \\(\\operatorname{Jac}(C)\\) 与 \\(H^1(C,\\mathbb R)/H^1(C,\\mathbb Z)\\) 联系起来。", "Abel–Jacobi 给出复环面与上同调格的关系。"),
            ("取 Poincaré 丛作为核，构造 Fourier–Mukai 函子。", "Poincaré 丛参数化线丛与其对偶，正是傅里叶对偶的几何核。"),
        ],
        "survey 只给陈述；Fourier–Mukai 的细节见 Laumon–Rothstein 等。",
        "§2.4 / p.12",
    )],
    [
        "\\(\\operatorname{Loc}(\\operatorname{Jac})\\) 是 \\(\\operatorname{Jac}\\) 上的局部系统，不是 \\(\\operatorname{Jac}\\) 上的拟凝聚层；两者通过 Fourier–Mukai 对偶。",
        "度数 \\(\\mathbb Z\\) 不能被丢掉；谱侧要包含所有秩一局部系统。",
    ],
    ["bzg/concept/gl1-derham-glc", "bzg/concept/betti-mellin", "bzg/concept/picard-jacobian"],
    "§2.4", [12],
))

cards.append(C(
    "gl1-derham-glc", "A", "\\(GL_1\\) 的 de Rham 几何 Langlands",
    ["GL1 de Rham GLC", "abelian de Rham GLC", "Laumon-Rothstein"],
    "\\(GL_1\\) 的 de Rham GLC 是 \\(\\operatorname{DMod}(\\operatorname{Jac}(C))\\simeq \\operatorname{QCoh}(\\operatorname{Loc}^{dR}_{GL_1}(C))\\)。",
    "\\(GL_1\\) 的 de Rham 版本与 Betti 版本有什么不同，为什么需要 \\(D\\)-模？",
    r"de Rham 侧用 \\(\\operatorname{DMod}(\\operatorname{Jac}(C))\\) 代替 \\(\\operatorname{Loc}(\\operatorname{Jac}(C))\\)，谱侧用平坦线丛的模叠 \\(\\operatorname{Loc}^{dR}_{GL_1}(C)\\)。对应由 Laumon–Rothstein 的 Fourier–Mukai 型变换给出；在代数情形，\\(\\operatorname{Loc}^{dR}_{GL_1}\\) 与 Betti 的 \\((\\mathbb C^\\times)^{2g}\\) 点相同但代数结构不同。",
    r"\\(\\operatorname{DMod}\\)：\\(D\\)-模；\\(\\operatorname{Loc}^{dR}_{GL_1}\\)：平坦线丛；\\(\\operatorname{Jac}(C)\\)：线丛模叠。",
    [
        "de Rham 版本把“函数”换成“\\(D\\)-模”，把“局部系统”换成“平坦联络”。",
        "在 \\(GL_1\\) 情形，Fourier–Mukai 核是 Poincaré 丛的 \\(D\\)-模版本。",
        "Betti 与 de Rham 通过 Riemann–Hilbert 在解析 setting 下相容，但代数上不同。",
        "它是 §5.1 中 \\(\\operatorname{IndCoh}_{\\mathcal N}\\) 修正的 Abel 先例。",
    ],
    [
        r"\\operatorname{DMod}(\\operatorname{Jac}(C))\\simeq \\operatorname{QCoh}(\\operatorname{Loc}^{dR}_{GL_1}(C))",
        r"\\operatorname{Loc}^{dR}_{GL_1}(C)=\\{(\\mathcal L,\\nabla)\\}/\\sim",
    ],
    [T(
        "\\(GL_1\\) 的 de Rham GLC",
        r"存在等价 \\(\\operatorname{DMod}(\\operatorname{Jac}(C))\\simeq \\operatorname{QCoh}(\\operatorname{Loc}^{dR}_{GL_1}(C))\\)。",
        [
            ("把 \\(\\operatorname{Jac}(C)\\) 上的 \\(D\\)-模看成带联络的层。", "de Rham 侧的对象是 \\(D\\)-模，等价于带可积联络的 \\(\\mathcal O\\)-模（正则奇异时）。"),
            ("用 Poincaré 丛的联络版本构造 Fourier–Mukai 核。", "核的联络给出从 \\(D\\)-模到平坦线丛侧的函数。"),
        ],
        "survey 只给陈述；Laumon–Rothstein 的完整构造从略。",
        "§2.4 / p.12",
    )],
    [
        "de Rham 与 Betti 的点相同，但范畴不同；不能把 \\(\\operatorname{DMod}\\) 直接换成 \\(\\operatorname{Loc}\\)。",
        "平坦联络的模叠不是仿射的；\\(\\operatorname{QCoh}\\) 在奇异点处需要小心。",
    ],
    ["bzg/concept/gl1-betti-glc", "bzg/concept/derham-mellin", "bzg/concept/picard-jacobian"],
    "§2.4", [12],
))

cards.append(C(
    "categorical-fourier", "A", "范畴化 Fourier 与 Fourier–Mukai 核",
    ["categorical Fourier transform", "Fourier-Mukai", "integral kernel"],
    "把积分核换成核层，积分变换就变成 Fourier–Mukai 函子；这是几何 Langlands 中“对偶”的技术原型。",
    "Fourier–Mukai 函子如何把“积分核”范畴化，六函子在其中怎么用？",
    r"给定核 \\(\\mathcal K\\in \\operatorname{Shv}(X\\times Y)\\)，Fourier–Mukai 函子定义为 \\(\\operatorname{FM}_{\\mathcal K}(F)=p_{Y!}(p_X^*F\\otimes \\mathcal K)\\)。当 \\(X,Y\\) 是对偶环面时，Poincaré 丛给出核，\\(\\operatorname{FM}\\) 就是 Fourier 变换的范畴化。",
    r"\\(p_X,p_Y\\)：两个投影；\\(p_{Y!}\\)：紧支撑推前（积分）；\\(\\otimes\\)：张量（乘法）。",
    [
        "核层 \\(\\mathcal K\\) 是积分核 \\(K(x,y)\\) 的几何版本。",
        "推前 \\(p_{Y!}\\) 对应积分，拉回 \\(p_X^*\\) 对应限制。",
        "Fourier–Mukai 是几何 Langlands 中 Hecke 对应与谱侧张量作用的共同原型。",
        "在奇异情形，\\(!\\) 与 \\(*\\) 的差别导致 \\(\\operatorname{IndCoh}\\) 修正。",
    ],
    [
        r"\\operatorname{FM}_{\\mathcal K}(F)=p_{Y!}(p_X^*F\\otimes \\mathcal K)",
        r"\\operatorname{FM}_{\\mathcal K}:\\operatorname{Shv}(X)\\to\\operatorname{Shv}(Y)",
    ],
    [],
    [
        "不要把 \\(p_{Y!}\\) 写成 \\(p_{Y*}\\)：紧支撑推前才对应积分。",
        "核层不是普通函数；在导出范畴中要处理完各化与奇异支撑。",
    ],
    ["bzg/concept/categorical-harmonic-analysis", "bzg/concept/fourier-transform", "bzg/concept/gl1-betti-glc"],
    "§2.1", [8],
))

# ---------------------------------------------------------------- B Bun_G / Hecke
cards.append(C(
    "bun-g", "B", "\\(\\operatorname{Bun}_G\\)：\\(G\\)-丛的模叠",
    ["Bun_G", "moduli of G-bundles", "G-丛模叠"],
    "\\(\\operatorname{Bun}_G(C)\\) 是曲线 \\(C\\) 上 \\(G\\)-丛的模叠；它不是拟紧的，按度数有无穷多个连通分支。",
    "为什么 \\(\\operatorname{Bun}_G\\) 是叠而不是簇，它的非拟紧性对几何 Langlands 意味着什么？",
    r"\\(\\operatorname{Bun}_G(C)\\) 的对象是 \\(C\\) 上的 \\(G\\)-torsor（等价地，\\(G\\)-丛），态射是丛同构。它是一个代数叠；当 \\(G=GL_1\\) 时 \\(\\operatorname{Bun}_{GL_1}=\\operatorname{Pic}(C)\\)。由于丛的度数可以任意大，\\(\\operatorname{Bun}_G\\) 不是拟紧的。",
    r"\\(G\\)-torsor：局部平凡、转移函数取在 \\(G\\) 中的丛；\\(\\operatorname{Pic}(C)\\)：线丛模叠。",
    [
        "\\(\\operatorname{Bun}_G\\) 是叠：对象有自同构，不能只用粗模空间。",
        "非拟紧性来自度数无界，导致自守侧需要增长条件/完各化。",
        "\\(GL_1\\) 情形给出 \\(\\operatorname{Pic}(C)\\)，是 Abel 对应的几何舞台。",
        "\\(\\operatorname{Bun}_G\\) 的几何与 Yang–Mills 方程、Narasimhan–Seshadri 定理相关。",
    ],
    [
        r"\\operatorname{Bun}_G(C)=\\{G\\text{-torsors on }C\\}",
        r"\\operatorname{Bun}_{GL_1}\\cong \\operatorname{Pic}(C)",
    ],
    [],
    [
        "不要把 \\(\\operatorname{Bun}_G\\) 当成有限维簇；它有无限多个分支与自同构群。",
        "非拟紧性不是技术细节；它导致 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\) 需要完各化。",
    ],
    ["bzg/concept/picard-jacobian", "bzg/concept/hecke-operators", "bzg/concept/glc-overview"],
    "§2.2", [9],
))

cards.append(C(
    "picard-jacobian", "B", "\\(\\operatorname{Pic}(C)\\)、\\(\\operatorname{Jac}(C)\\) 与度数",
    ["Picard group", "Jacobian", "degree"],
    "\\(\\operatorname{Pic}(C)\\cong \\mathbb Z\\times \\operatorname{Jac}(C)\\)，其中 \\(\\operatorname{Jac}(C)\\) 是度数为零的线丛，作为实环面同构于 \\((S^1)^{2g}\\)。",
    "为什么 \\(\\operatorname{Pic}(C)\\) 会分裂成度数 \\(\\mathbb Z\\) 与 Jacobian 两部分，\\(\\operatorname{Jac}(C)\\) 的 \\(2g\\) 维从哪里来？",
    r"线丛的度数给出满射 \\(\\deg:\\operatorname{Pic}(C)\\to \\mathbb Z\\)，核是 \\(\\operatorname{Jac}(C)=\\operatorname{Pic}^0(C)\\)。作为复环面，\\(\\operatorname{Jac}(C)\\cong H^1(C,\\mathcal O)/H^1(C,\\mathbb Z)\\)，实维数 \\(2g\\)，因此同构于 \\((S^1)^{2g}\\)。",
    r"\\(g\\)：亏格；\\(\\deg\\)：线丛度数；\\(H^1(C,\\mathbb Z)\\)：秩 \\(2g\\) 的格。",
    [
        "度数给出 \\(\\operatorname{Pic}(C)\\) 的 \\(\\mathbb Z\\)-分量。",
        "\\(\\operatorname{Jac}(C)\\) 是紧复环面，不是向量空间。",
        "Abel–Jacobi 映射把 \\(C\\) 嵌入 \\(\\operatorname{Jac}(C)\\)。",
        "在 \\(GL_1\\) 的 GLC 中，\\(\\operatorname{Jac}(C)\\) 是自守侧，\\((\\mathbb C^\\times)^{2g}\\) 是谱侧。",
    ],
    [
        r"\\operatorname{Pic}(C)\\cong \\mathbb Z\\times \\operatorname{Jac}(C)",
        r"\\operatorname{Jac}(C)\\cong H^1(C,\\mathcal O)/H^1(C,\\mathbb Z)\\cong (S^1)^{2g}",
    ],
    [T(
        "Picard–Jacobian 分解",
        r"\\(\\operatorname{Pic}(C)\\cong \\mathbb Z\\times \\operatorname{Jac}(C)\\)。",
        [
            ("取度数映射 \\(\\deg:\\operatorname{Pic}(C)\\to \\mathbb Z\\)。", "线丛的转移函数给出良定义的度数。"),
            ("核为 \\(\\operatorname{Jac}(C)\\)，并选取一个度数为 \\(1\\) 的线丛作为分裂。", "存在度数为 \\(1\\) 的线丛，因此短正合列分裂。"),
        ],
        "经典代数几何；survey 只引用。",
        "§2.2 / p.10",
    )],
    [
        "\\(\\operatorname{Jac}(C)\\) 是复环面，不是 \\(\\mathbb C^g\\)；不要把它当成向量空间。",
        "\\(\\operatorname{Pic}(C)\\) 的分裂不是典范的；选择度数为 \\(1\\) 的线丛才给出分裂。",
    ],
    ["bzg/concept/bun-g", "bzg/concept/gl1-betti-glc", "bzg/concept/affine-grassmannian"],
    "§2.2", [10],
))

cards.append(C(
    "affine-grassmannian", "B", "仿射 Grassmannian \\(\\operatorname{Gr}_G=LG/LG_+\\)",
    ["affine Grassmannian", "仿射 Grassmannian", "loop Grassmannian"],
    "\\(\\operatorname{Gr}_G=LG/LG_+\\) 是环路群的商，参数化 \\(G\\)-丛在一点附近的修改；它是 ind-概形。",
    "仿射 Grassmannian 如何参数化“在一点修改丛”，为什么它是几何 Satake 的舞台？",
    r"令 \\(LG=G((t))\\)，\\(LG_+=G[[t]]\\)。仿射 Grassmannian 定义为 \\(\\operatorname{Gr}_G=LG/LG_+\\)。它的点对应 \\(G\\)-丛在形式圆盘上的平凡化与在穿孔圆盘上的修改；Cartan 分解给出 \\(\\operatorname{Gr}_G=\\bigsqcup_{\\lambda\\in X_*(T)^+}\\operatorname{Gr}_G^\\lambda\\)。",
    r"\\(t\\)：形式变量；\\(G((t))\\)：Laurent 级数；\\(G[[t]]\\)：形式幂级数；\\(X_*(T)^+\\)：优势余权。",
    [
        "\\(\\operatorname{Gr}_G\\) 是 ind-概形，不是有限维概形。",
        "Cartan 分解把 \\(\\operatorname{Gr}_G\\) 分成可数个 Schubert 胞腔。",
        "它参数化 \\(G\\)-丛在一点的修改，因此是 Hecke 算子的几何来源。",
        "几何 Satake 把 \\(\\operatorname{Gr}_G\\) 上的等变层与 \\(\\check G\\) 的表示联系起来。",
    ],
    [
        r"\\operatorname{Gr}_G=LG/LG_+,\\qquad LG=G((t)),\\quad LG_+=G[[t]]",
        r"\\operatorname{Gr}_G=\\bigsqcup_{\\lambda\\in X_*(T)^+}\\operatorname{Gr}_G^\\lambda",
    ],
    [],
    [
        "\\(\\operatorname{Gr}_G\\) 不是 \\(G\\)-丛的模空间本身；它只记录一点附近的修改。",
        "不要把 \\(LG_+\\) 写成 \\(G[t]\\)；这里用的是形式幂级数 \\(G[[t]]\\)。",
    ],
    ["bzg/concept/adelic-uniformization", "bzg/concept/spherical-hecke-category", "bzg/concept/bun-g"],
    "§2.2", [10],
))

cards.append(C(
    "adelic-uniformization", "B", "Adelic 双陪集与 \\(\\operatorname{Bun}_G\\)",
    ["adelic uniformization", "双陪集", "Bun_G as double coset"],
    "在函数域情形，\\(\\operatorname{Bun}_G(C)\\cong G(F)\\backslash G(\\mathbb A_F)/K\\)；这是 adelic 双陪集描述。",
    "如何用 adeles 与双陪集描述 \\(\\operatorname{Bun}_G\\)，这个描述对 Hecke 算子有什么好处？",
    r"设 \\(F\\) 是 \\(C\\) 的函数域，\\(\\mathbb A_F\\) 是其 adele 环，\\(K\\) 是紧开子群。则 \\(\\operatorname{Bun}_G(C)\\cong G(F)\\backslash G(\\mathbb A_F)/K\\)。在一点 \\(x\\) 的局部版本是 \\(G(C\\setminus x)\\backslash LG/LG_+\\)。",
    r"\\(F\\)：函数域；\\(\\mathbb A_F\\)：adele 环；\\(K\\)：紧开子群；\\(LG=G((t))\\)。",
    [
        "双陪集把整体丛的模空间写成局部数据的商。",
        "Hecke 算子在 adelic 描述下是双陪集卷积。",
        "这个描述与仿射 Grassmannian 的局部描述相容。",
        "它是函数域 Langlands 与几何 Langlands 之间的桥梁。",
    ],
    [
        r"\\operatorname{Bun}_G(C)\\cong G(F)\\backslash G(\\mathbb A_F)/K",
        r"G(C\\setminus x)\\backslash LG/LG_+",
    ],
    [T(
        "Adelic 均匀化",
        r"\\(\\operatorname{Bun}_G(C)\\cong G(F)\\backslash G(\\mathbb A_F)/K\\)。",
        [
            ("把 \\(G\\)-丛在 \\(C\\) 的所有点局部平凡化。", "选择足够多的局部平凡化，使得转移函数定义在 adeles 上。"),
            ("模掉整体 \\(G(F)\\) 与紧开 \\(K\\) 的作用。", "整体自同构与局部平凡化的改变给出双陪集。"),
        ],
        "survey 只给类比；完整陈述需要函数域与 adele 的标准构造。",
        "§2.2 / p.11",
    )],
    [
        "这个描述主要适用于函数域；复数曲线情形要用不同的拓扑/代数化。",
        "\\(K\\) 的选择不影响双陪集范畴的等价类，但影响具体模型。",
    ],
    ["bzg/concept/bun-g", "bzg/concept/affine-grassmannian", "bzg/concept/hecke-operators"],
    "§2.2", [11],
))

cards.append(C(
    "hecke-operators", "B", "Hecke 函子：在一点修改丛",
    ["Hecke operators", "Hecke functors", "Hecke correspondence"],
    "Hecke 函子在一点 \\(x\\) 修改 \\(G\\)-丛，并用 \\(\\check G\\) 的表示给出一族作用在 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\) 上的算子。",
    "Hecke 算子如何通过“在一点修改丛”的对应来定义，为什么它作用在自守侧？",
    r"在 \\(x\\in C\\) 处，考虑三元组 \\((\\mathcal E,\\mathcal E',\\phi)\\)，其中 \\(\\phi:\\mathcal E|_{C\\setminus x}\\cong \\mathcal E'|_{C\\setminus x}\\)。这给出对应 \\(\\operatorname{Bun}_G\\xleftarrow{p}\\operatorname{H}_x\\xrightarrow{q}\\operatorname{Bun}_G\\)。对 \\(V\\in\\operatorname{Rep}(\\check G)\\)，Hecke 函子定义为 \\(H_x^V(F)=q_!(p^*F\\otimes \\mathcal V)\\)，其中 \\(\\mathcal V\\) 是与 \\(V\\) 对应的球面层。",
    r"\\(\\operatorname{H}_x\\)：修改的三元组模叠；\\(p,q\\)：两个投影；\\(\\mathcal V\\)：\\(V\\) 对应的球 Hecke 层。",
    [
        "Hecke 算子是“在一点插入/删除”丛的修改。",
        "对应不是函数，而是模叠之间的 correspondence。",
        "\\(V\\) 取遍 \\(\\check G\\) 的表示，给出交换的 Hecke 算子族。",
        "在谱侧，Hecke 算子对应 \\(\\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})\\) 的张量作用。",
    ],
    [
        r"H_x^V(F)=q_!(p^*F\\otimes \\mathcal V)",
        r"\\operatorname{Bun}_G\\xleftarrow{p}\\operatorname{H}_x\\xrightarrow{q}\\operatorname{Bun}_G",
    ],
    [],
    [
        "Hecke 修改只发生在一点 \\(x\\)，其余位置必须同构；不要把它当成整体修改。",
        "\\(V\\) 是 \\(\\check G\\) 的表示，不是 \\(G\\) 的表示；这是 Langlands 对偶的关键。",
    ],
    ["bzg/concept/spherical-hecke-category", "bzg/concept/geometric-satake", "bzg/concept/spectral-action"],
    "§3.1", [14],
))

cards.append(C(
    "spherical-hecke-category", "B", "球 Hecke 范畴 \\(\\operatorname{Sph}_G\\)",
    ["spherical Hecke category", "球 Hecke 范畴", "Sph_G"],
    "\\(\\operatorname{Sph}_G=\\operatorname{Shv}(\\operatorname{Gr}_G)^{LG_+}\\) 是 \\(LG_+\\)-等变层范畴，带卷积 monoidal 结构。",
    "球 Hecke 范畴的卷积结构如何定义，它为什么等价于 \\(\\check G\\) 的表示范畴？",
    r"\\(\\operatorname{Sph}_G=\\operatorname{Shv}(\\operatorname{Gr}_G)^{LG_+}\\) 是 \\(LG_+\\)-等变（或等变导出）层范畴。卷积由 \\(\\operatorname{Gr}_G\\) 的乘法结构给出：\\(\\mathcal F*\\mathcal G=m_!(\\mathcal F\\boxtimes\\mathcal G)\\)。几何 Satake 断言 \\((\\operatorname{Sph}_G,*)\\simeq(\\operatorname{Rep}(\\check G),\\otimes)\\) 为对称 monoidal 等价。",
    r"\\(LG_+\\)：正环路群；\\(\\operatorname{Shv}^{LG_+}\\)：等变层；\\(*\\)：卷积；\\(\\otimes\\)：表示张量。",
    [
        "\\(\\operatorname{Sph}_G\\) 的乘法是卷积，不是逐点张量。",
        "等变性 \\(LG_+\\) 是必要的；没有它得不到 \\(\\check G\\) 的表示。",
        "单位对象对应平凡表示。",
        "几何 Satake 把卷积变成张量，这是 Hecke 算子交换性的来源。",
    ],
    [
        r"\\operatorname{Sph}_G=\\operatorname{Shv}(\\operatorname{Gr}_G)^{LG_+}",
        r"\\mathcal F*\\mathcal G=m_!(\\mathcal F\\boxtimes\\mathcal G)",
    ],
    [],
    [
        "卷积不是交换的逐点乘法；它的交换性来自 \\(\\operatorname{Gr}_G\\) 的几何结构。",
        "等变层要在导出意义下取，否则卷积结构不完整。",
    ],
    ["bzg/concept/geometric-satake", "bzg/concept/hecke-operators", "bzg/concept/affine-grassmannian"],
    "§3.1", [14],
))

cards.append(C(
    "geometric-satake", "B", "几何 Satake 等价",
    ["geometric Satake", "几何 Satake", "Satake equivalence"],
    "几何 Satake 断言 \\(\\operatorname{Sph}_G\\simeq \\operatorname{Rep}(\\check G)\\) 为对称 monoidal 等价，从而由几何数据重构对偶群。",
    "几何 Satake 如何从 \\(\\operatorname{Gr}_G\\) 的等变层重构出 \\(\\check G\\) 的表示范畴，Tannaka 对偶在其中起什么作用？",
    r"几何 Satake（Mirković–Vilonen）断言存在对称 monoidal 等价 \\(\\operatorname{Sph}_G\\simeq \\operatorname{Rep}(\\check G)\\)。因为 \\(\\operatorname{Rep}(\\check G)\\) 是对称 monoidal 范畴，Tannaka 重构可以从它恢复 \\(\\check G\\)。这是“对偶群”在几何 Langlands 中的定义方式之一。",
    r"\\(\\operatorname{Sph}_G\\)：球 Hecke 范畴；\\(\\operatorname{Rep}(\\check G)\\)：有限维表示；Tannaka：从纤维函子重构群。",
    [
        "几何 Satake 把几何对象（等变层）与表示论对象（\\(\\check G\\)-表示）等同。",
        "它解释了为什么 Hecke 算子由 \\(\\check G\\) 的表示参数化。",
        "Tannaka 重构给出 \\(\\check G\\) 本身，而不仅是它的表示范畴。",
        "导出版本（Bezrukavnikov–Finkelberg）把 abelian 等价升级为导出等价。",
    ],
    [
        r"\\operatorname{Sph}_G\\simeq \\operatorname{Rep}(\\check G)",
        r"\\text{Tannaka}:\\ \\operatorname{Rep}(\\check G)\\ \\rightsquigarrow\\ \\check G",
    ],
    [T(
        "几何 Satake 等价",
        r"\\(\\operatorname{Sph}_G\\simeq \\operatorname{Rep}(\\check G)\\) 为对称 monoidal 等价。",
        [
            ("用 \\(\\operatorname{Gr}_G\\) 的 Schubert 胞腔与 MV 循环构造层。", "每个优势余权 \\(\\lambda\\) 给出一个 MV 循环，生成 \\(\\operatorname{Sph}_G\\)。"),
            ("验证卷积对应张量、单位对应平凡表示。", "MV 循环的卷积与 \\(\\check G\\) 表示的张量积有相同的最高权结构。"),
            ("用 Tannaka 重构恢复 \\(\\check G\\)。", "对称 monoidal 范畴的纤维函子给出群概形。"),
        ],
        "survey 只给陈述；完整证明见 Mirković–Vilonen 2007。",
        "§3.3 / p.16",
    )],
    [
        "\\(\\operatorname{Rep}(\\check G)\\) 不是 \\(\\operatorname{Rep}(G)\\)；对偶群可能不同（如 \\(SL_n\\) 与 \\(PGL_n\\)）。",
        "几何 Satake 的 monoidal 结构是卷积/张量，不是逐点乘法；不要混淆。",
    ],
    ["bzg/concept/spherical-hecke-category", "bzg/concept/dual-group", "bzg/concept/hecke-operators"],
    "§3.3", [16],
))

cards.append(C(
    "dual-group", "B", "Langlands 对偶群 \\(\\check G\\) 与根数据",
    ["Langlands dual group", "对偶群", "root datum"],
    "对偶群 \\(\\check G\\) 由 \\(G\\) 的根数据对偶得到：交换特征格与余权格，并交换根与余根。",
    "Langlands 对偶群如何从根数据构造，为什么 \\(SL_n\\) 的对偶是 \\(PGL_n\\) 而不是 \\(SL_n\\)？",
    r"设 \\(G\\) 的根数据为 \\((X^*(T),\\Phi,X_*(T),\\Phi^\\vee)\\)。对偶群 \\(\\check G\\) 的根数据是 \\((X_*(T),\\Phi^\\vee,X^*(T),\\Phi)\\)。因此 \\(GL_n\\) 对偶于 \\(GL_n\\)，\\(SL_n\\) 对偶于 \\(PGL_n\\)，环面 \\(T\\) 对偶于 \\(\\check T\\)。",
    r"\\(X^*(T)\\)：特征格；\\(X_*(T)\\)：余权格；\\(\\Phi\\)：根；\\(\\Phi^\\vee\\)：余根。",
    [
        "对偶群不是 \\(G\\) 的同构复制；它交换了特征格与余权格。",
        "\\(GL_n\\) 是自对偶的；\\(SL_n\\) 与 \\(PGL_n\\) 互换。",
        "几何 Satake 把 \\(\\check G\\) 的表示实现为球 Hecke 范畴。",
        "在 GLC 中，谱侧的局部系统取在 \\(\\check G\\) 中，而不是 \\(G\\) 中。",
    ],
    [
        r"(X^*(T),\\Phi,X_*(T),\\Phi^\\vee)\\ \\longleftrightarrow\\ (X_*(T),\\Phi^\\vee,X^*(T),\\Phi)",
        r"\\check{GL}_n=GL_n,\\qquad \\check{SL}_n=PGL_n",
    ],
    [],
    [
        "不要写成 \\(\\check G=G\\)；只有自对偶群才成立。",
        "对偶群依赖于所取的最大环面与根数据；不同内形式可能给出同构的对偶群。",
    ],
    ["bzg/concept/geometric-satake", "bzg/concept/loc-g-betti", "bzg/concept/glc-overview"],
    "§1.4", [6],
))

# ---------------------------------------------------------------- C 谱侧 / Hitchin
cards.append(C(
    "loc-g-betti", "C", "Betti 特征簇 \\(\\operatorname{Loc}_{\\check G}\\)",
    ["Betti character variety", "character variety", "Loc_G"],
    "\\(\\operatorname{Loc}_{\\check G}(C)\\) 是 \\(\\pi_1(C)\\) 到 \\(\\check G\\) 的表示模去共轭，等价于 \\(2g\\) 个矩阵满足乘积关系。",
    "Betti 特征簇如何用 \\(2g\\) 个矩阵与一个关系描述，为什么它是叠而不是簇？",
    r"设 \\(C\\) 是亏格 \\(g\\) 的紧 Riemann 面。\\(\\operatorname{Loc}_{\\check G}(C)=\\{(A_i,B_i)_{i=1}^g\\in \\check G^{2g}\\mid \\prod_i[A_i,B_i]=1\\}/\\check G\\)，其中 \\(\\check G\\) 通过共轭作用。它是特征簇（character stack），一般不是概形。",
    r"\\(A_i,B_i\\)：\\(\\pi_1(C)\\) 的 \\(2g\\) 个生成元；\\([A_i,B_i]=A_iB_iA_i^{-1}B_i^{-1}\\)；商是共轭商。",
    [
        "\\(\\pi_1(C)\\) 有 \\(2g\\) 个生成元与一个关系 \\(\\prod[A_i,B_i]=1\\)。",
        "表示模去共轭得到特征簇；自同构使它是叠。",
        "Betti 版本只依赖 \\(C\\) 的拓扑，不依赖复结构。",
        "GLC 的谱侧就是 \\(\\operatorname{Loc}_{\\check G}\\) 上的 \\(\\operatorname{IndCoh}_{\\mathcal N}\\)。",
    ],
    [
        r"\\operatorname{Loc}_{\\check G}(C)=\\{(A_i,B_i)_{i=1}^g\\in \\check G^{2g}\\mid \\prod_i[A_i,B_i]=1\\}/\\check G",
        r"\\pi_1(C)=\\langle A_1,B_1,\\dots,A_g,B_g\\mid \\prod_i[A_i,B_i]=1\\rangle",
    ],
    [],
    [
        "不要把它写成 \\(\\check G^{2g}\\) 的商而漏掉乘积关系。",
        "它是叠，不是簇；共轭商的稳定化子会带来非平凡自同构。",
    ],
    ["bzg/concept/loc-g-derham", "bzg/concept/glc-statement", "bzg/concept/dual-group"],
    "§2.3", [11],
))

cards.append(C(
    "loc-g-derham", "C", "de Rham 局部系统与平坦联络",
    ["de Rham local systems", "flat connections", "Loc^dR"],
    "de Rham 侧用 \\(\\check G\\)-平坦联络代替 Betti 表示；解析上两者相同，代数上不同。",
    "de Rham 局部系统与 Betti 局部系统在什么意义上相同、在什么意义上不同？",
    r"\\(\\operatorname{Loc}^{dR}_{\\check G}(C)\\) 是 \\(C\\) 上 \\(\\check G\\)-平坦联络的模叠。解析上，Riemann–Hilbert 对应给出平坦联络与局部系统的等价；代数上，de Rham 模叠通常不是仿射的，且与 Betti 特征簇不同。GLC 有两个版本，通过 étale 版本比较。",
    r"\\(\\nabla\\)：联络；平坦：\\(\\nabla^2=0\\)；\\(\\operatorname{Loc}^{dR}\\)：平坦联络模叠。",
    [
        "Betti 版本只依赖拓扑；de Rham 版本依赖复结构。",
        "Riemann–Hilbert 在解析 setting 下连接两者。",
        "代数上 de Rham 模叠更“胖”，\\(\\operatorname{QCoh}\\) 的行为不同。",
        "GLC 的 de Rham 与 Betti 陈述因此需要分别表述。",
    ],
    [
        r"\\operatorname{Loc}^{dR}_{\\check G}(C)=\\{(\\mathcal E,\\nabla)\\}/\\sim",
        r"\\nabla:\\mathcal E\\to \\mathcal E\\otimes \\Omega^1_C,\\qquad \\nabla^2=0",
    ],
    [T(
        "Riemann–Hilbert 对应",
        r"解析情形下，平坦联络的范畴与局部系统的范畴等价。",
        [
            ("从平坦联络取单值性表示。", "沿闭环平行移动给出 \\(\\pi_1(C)\\to \\check G\\)。"),
            ("从局部系统取平坦联络。", "局部系统配上平凡联络的拉回，得到可积联络。"),
        ],
        "survey 只引用；完整陈述需要正则奇异性与解析化。",
        "§2.3 / p.11",
    )],
    [
        "解析等价不等于代数等价；de Rham 与 Betti 的 \\(\\operatorname{QCoh}\\) 不同。",
        "平坦联络的模叠不是有限维仿射簇；不要直接套用 \\(\\operatorname{Loc}_{\\check G}\\) 的矩阵描述。",
    ],
    ["bzg/concept/loc-g-betti", "bzg/concept/gl1-derham-glc", "bzg/concept/glc-statement"],
    "§2.3", [11],
))

cards.append(C(
    "spectral-action", "C", "谱作用定理",
    ["spectral action", "谱作用", "Hecke action"],
    "\\(\\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})\\) 作用在 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\) 上，特征值由 \\(\\check G\\)-局部系统给出。",
    "谱作用定理如何把 Hecke 算子组织成一个 \\(\\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})\\)-作用，为什么它给出“特征值”？",
    r"对每个 \\(x\\in C\\)，Hecke 范畴作用在 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\) 上；把这些局部作用用因子化同调粘起来，得到全局作用 \\(\\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})\\curvearrowright \\operatorname{Shv}(\\operatorname{Bun}_G)\\)。对 \\(E\\in\\operatorname{Loc}_{\\check G}\\)，特征层 \\(\\operatorname{Aut}_E\\) 满足 \\(F*\\operatorname{Aut}_E\\simeq F|_E\\otimes \\operatorname{Aut}_E\\)。",
    r"\\(\\operatorname{Loc}_{\\check G}\\)：谱侧；\\(\\operatorname{Aut}_E\\)：\\(E\\) 对应的特征层；\\(F|_E\\)：\\(F\\) 在 \\(E\\) 的纤维。",
    [
        "谱作用把“算子族”变成“一个范畴作用”。",
        "特征层是 Hecke 算子的联合特征向量。",
        "特征值不是数，而是向量空间/局部系统。",
        "主定理说这个作用在 \\(\\operatorname{IndCoh}_{\\mathcal N}\\) 上自由且重数一。",
    ],
    [
        r"\\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})\\curvearrowright \\operatorname{Shv}(\\operatorname{Bun}_G)",
        r"F*\\operatorname{Aut}_E\\simeq F|_E\\otimes \\operatorname{Aut}_E",
    ],
    [T(
        "谱作用定理",
        r"存在 \\(\\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})\\) 在 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\) 上的作用，局部由 Hecke 函子给出。",
        [
            ("在每个 \\(x\\) 用球 Hecke 范畴作用。", "Hecke 函子 \\(H_x^V\\) 对 \\(V\\in\\operatorname{Rep}(\\check G)\\) 定义。"),
            ("用因子化结构把局部作用粘成全局作用。", "Hecke 范畴的 \\(E_n\\) 结构保证粘合相容。"),
            ("在特征点 \\(E\\) 处取纤维，得到特征层。", "作用的函子性给出 \\(F*\\operatorname{Aut}_E\\simeq F|_E\\otimes \\operatorname{Aut}_E\\)。"),
        ],
        "survey 只给陈述；完整证明见 Gaitsgory 等人的工作。",
        "§3.5 / p.17",
    )],
    [
        "谱作用不是等价；要得到等价还需要 \\(\\operatorname{IndCoh}_{\\mathcal N}\\) 与重数一。",
        "特征值是局部系统，不是标量；不要说“特征值为 \\(\\lambda\\)”。",
    ],
    ["bzg/concept/hecke-operators", "bzg/concept/glc-statement", "bzg/concept/factorization"],
    "§3.5", [17],
))

cards.append(C(
    "higgs-bundles", "C", "Higgs 丛与 \\(T^*\\operatorname{Bun}_G\\)",
    ["Higgs bundles", "Higgs 丛", "cotangent bundle"],
    "Higgs 丛是 \\((E,\\varphi)\\)，其中 \\(\\varphi\\in H^0(C,\\operatorname{ad}E\\otimes K_C)\\)；它参数化 \\(T^*\\operatorname{Bun}_G\\)。",
    "Higgs 丛如何参数化 \\(\\operatorname{Bun}_G\\) 的余切丛，Higgs 场为什么取值为 \\(K_C\\)-值的自同态？",
    r"\\(\\operatorname{Bun}_G\\) 的余切丛 \\(T^*\\operatorname{Bun}_G\\) 参数化 \\((E,\\varphi)\\)，其中 \\(E\\) 是 \\(G\\)-丛，\\(\\varphi\\in H^0(C,\\operatorname{ad}E\\otimes K_C)\\)。这样的 \\((E,\\varphi)\\) 称为 Higgs 丛；\\(\\varphi\\) 称为 Higgs 场。",
    r"\\(K_C\\)：典范丛；\\(\\operatorname{ad}E\\)：伴随丛；\\(\\varphi\\)：Higgs 场。",
    [
        "Higgs 场是 \\(K_C\\)-值的自同态，不是普通自同态。",
        "\\(T^*\\operatorname{Bun}_G\\) 是 Higgs 丛的模叠，带有超凯勒结构。",
        "Hitchin 纤维化从 Higgs 丛映到 Hitchin 基。",
        "Dolbeault GLC 以 Higgs 丛的模叠为舞台。",
    ],
    [
        r"T^*\\operatorname{Bun}_G\\cong \\operatorname{Higgs}_G",
        r"\\varphi\\in H^0(C,\\operatorname{ad}E\\otimes K_C)",
    ],
    [],
    [
        "Higgs 场不是 \\(H^0(C,\\operatorname{ad}E)\\)；必须扭 \\(K_C\\)。",
        "\\(T^*\\operatorname{Bun}_G\\) 是导出/模叠意义下的余切，不是普通向量丛。",
    ],
    ["bzg/concept/hitchin-fibration", "bzg/concept/dolbeault-glc", "bzg/concept/abelianization"],
    "§4.1", [18],
))

cards.append(C(
    "hitchin-fibration", "C", "Hitchin 纤维化与谱曲线",
    ["Hitchin fibration", "Hitchin 纤维化", "spectral curve"],
    "Hitchin 纤维化 \\(h:\\operatorname{Higgs}_G\\to \\mathcal A_G\\) 把 Higgs 丛映到特征多项式，一般纤维是谱曲线的 Picard。",
    "Hitchin 纤维化的底空间是什么，为什么一般纤维可以看成谱曲线的 Picard 簇？",
    r"设 \\(G\\) 的指数为 \\(d_1,\\dots,d_r\\)。Hitchin 基 \\(\\mathcal A_G=\\bigoplus_i H^0(C,K_C^{d_i})\\)。Hitchin 纤维化 \\(h:\\operatorname{Higgs}_G\\to \\mathcal A_G\\) 取 Higgs 场的特征多项式。一般纤维同构于谱曲线 \\(C_\\eta\\) 的 Picard 簇；幂零纤维是整体幂零锥。",
    r"\\(d_i\\)：\\(G\\) 的指数；\\(K_C\\)：典范丛；\\(C_\\eta\\)：谱曲线。",
    [
        "Hitchin 基的维数是 \\(\\dim G\\cdot(g-1)+...\\)，由指数决定。",
        "一般纤维是谱曲线的 Picard，因而是一个环面。",
        "幂零纤维是整体幂零锥，GLC 的奇异支撑就取在这里。",
        "Hitchin 系统是可积系统，SYZ 镜像对称把它与 \\(\\check G\\) 的 Hitchin 系统配对。",
    ],
    [
        r"h:\\operatorname{Higgs}_G\\to \\mathcal A_G,\\qquad \\mathcal A_G=\\bigoplus_i H^0(C,K_C^{d_i})",
        r"h^{-1}(\\eta)\\cong \\operatorname{Pic}(C_\\eta)\\quad\\text{(generic)}",
    ],
    [],
    [
        "一般纤维是 Picard，不是 Jacobian；度数部分不能忽略。",
        "幂零纤维不是一般纤维；奇异支撑条件正是在这里起作用。",
    ],
    ["bzg/concept/higgs-bundles", "bzg/concept/dolbeault-glc", "bzg/concept/abelianization"],
    "§4.1", [18],
))

cards.append(C(
    "dolbeault-glc", "C", "Dolbeault 几何 Langlands",
    ["Dolbeault GLC", "Dolbeault 几何 Langlands", "SYZ mirror"],
    "Dolbeault GLC 断言 \\(\\operatorname{QCoh}(\\operatorname{Higgs}_G)\\simeq \\operatorname{QCoh}(\\operatorname{Higgs}_{\\check G})\\)，是 Hitchin 系统的 SYZ 镜像。",
    "Dolbeault GLC 与通常 GLC 有什么关系，为什么它只在一般纤维上被证明？",
    r"Dolbeault GLC 是 GLC 的退化版本：把 \\(\\operatorname{Loc}_{\\check G}\\) 换成 \\(\\operatorname{Higgs}_{\\check G}\\)，把 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\) 换成 \\(\\operatorname{QCoh}(\\operatorname{Higgs}_G)\\)。它断言 \\(\\operatorname{QCoh}(\\operatorname{Higgs}_G)\\simeq \\operatorname{QCoh}(\\operatorname{Higgs}_{\\check G})\\)，即 Hitchin 系统的 SYZ 镜像。Donagi–Pantev 在一般纤维上证明；全空间仍 open。",
    r"\\(\\operatorname{Higgs}_G=T^*\\operatorname{Bun}_G\\)；SYZ：Strominger–Yau–Zaslow 镜像；一般纤维：Hitchin 基的稠密开子集。",
    [
        "Dolbeault GLC 关于 \\(G\\) 与 \\(\\check G\\) 完全对称。",
        "它在 Hitchin 基的一般纤维上由 Fourier–Mukai 实现。",
        "全空间版本仍是猜想；幂零纤维是难点。",
        "它也是量子 GLC 的退化极限。",
    ],
    [
        r"\\operatorname{QCoh}(\\operatorname{Higgs}_G)\\simeq \\operatorname{QCoh}(\\operatorname{Higgs}_{\\check G})",
        r"\\operatorname{Higgs}_G=T^*\\operatorname{Bun}_G",
    ],
    [T(
        "Dolbeault GLC（一般纤维）",
        r"在 Hitchin 基的一般纤维上，\\(\\operatorname{QCoh}(\\operatorname{Higgs}_G)\\simeq \\operatorname{QCoh}(\\operatorname{Higgs}_{\\check G})\\)。",
        [
            ("把一般纤维识别为谱曲线的 Picard 簇。", "Hitchin 纤维化的一般纤维是 \\(\\operatorname{Pic}(C_\\eta)\\)。"),
            ("用 Poincaré 丛构造 Fourier–Mukai 核。", "谱曲线与其对偶谱曲线的 Picard 簇通过 Poincaré 丛对偶。"),
        ],
        "Donagi–Pantev 证明一般纤维；全空间仍 open。",
        "§4.1 / p.19",
    )],
    [
        "Dolbeault GLC 不是通常 GLC 的直接推论；它是退化版本。",
        "“一般纤维”不等于全空间；幂零纤维与奇异支撑仍是障碍。",
    ],
    ["bzg/concept/higgs-bundles", "bzg/concept/hitchin-fibration", "bzg/concept/abelianization"],
    "§4.1", [19],
))

cards.append(C(
    "abelianization", "C", "阿贝尔化与 Arinkin 渐近",
    ["abelianization", "阿贝尔化", "Arinkin asymptotics"],
    "阿贝尔化把 \\(D\\)-模送到 Higgs 侧的拟凝聚层，再送到 \\(\\operatorname{Loc}_{\\check G}\\)；它解释了 GLC 的奇异支撑。",
    "阿贝尔化如何把自守侧的 \\(D\\)-模与谱侧的局部系统联系起来，Arinkin 渐近在其中做什么？",
    r"Beilinson–Drinfeld 用整体微分算子构造从 \\(D\\)-模到 Higgs 侧的函数；Arinkin 的渐近分析给出函子 \\(\\operatorname{DMod}(\\operatorname{Bun}_G)\\to \\operatorname{QCoh}(\\operatorname{Higgs}_G)\\simeq \\operatorname{QCoh}(\\operatorname{Higgs}_{\\check G})\\to \\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})\\)。特征层的特征簇落在整体幂零锥上，因此需要 \\(\\operatorname{IndCoh}_{\\mathcal N}\\)。",
    r"\\(\\operatorname{DMod}\\)：\\(D\\)-模；\\(\\operatorname{Higgs}\\)：Higgs 丛；\\(\\mathcal N\\)：整体幂零锥；WKB：半经典渐近。",
    [
        "阿贝尔化是“半经典极限”：把微分算子变成 Higgs 场的乘法。",
        "特征层的奇异支撑落在幂零锥上。",
        "它是 \\(\\operatorname{IndCoh}_{\\mathcal N}\\) 修正的几何来源。",
        "在 \\(GL_1\\) 情形退化为 Fourier–Mukai。",
    ],
    [
        r"\\operatorname{DMod}(\\operatorname{Bun}_G)\\to \\operatorname{QCoh}(\\operatorname{Higgs}_G)\\simeq \\operatorname{QCoh}(\\operatorname{Higgs}_{\\check G})\\to \\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})",
        r"\\operatorname{SS}(\\operatorname{Aut}_E)\\subset \\mathcal N",
    ],
    [],
    [
        "阿贝尔化不是等价；它是半经典极限，会丢失信息。",
        "奇异支撑不是任意子集；必须落在整体幂零锥上。",
    ],
    ["bzg/concept/indicoh-nilpotent-support", "bzg/concept/hitchin-fibration", "bzg/concept/dolbeault-glc"],
    "§4.2", [19],
))

cards.append(C(
    "indicoh-nilpotent-support", "C", "\\(\\operatorname{IndCoh}_{\\mathcal N}\\) 与幂零奇异支撑",
    ["IndCoh", "nilpotent singular support", "IndCoh_N"],
    "\\(\\operatorname{IndCoh}_{\\mathcal N}(\\operatorname{Loc}_{\\check G})\\) 是允许“广义函数”的层范畴，只保留幂零方向上的奇异支撑。",
    "为什么 GLC 的谱侧必须用 \\(\\operatorname{IndCoh}_{\\mathcal N}\\) 而不是 \\(\\operatorname{QCoh}\\)，幂零奇异支撑条件排除了什么？",
    r"\\(\\operatorname{IndCoh}\\) 扩展 \\(\\operatorname{QCoh}\\)，允许像分布一样的广义层；在奇异点上，凝聚层不能由向量丛有限分解。奇异支撑衡量广义层在哪些余切方向上有障碍。GLC 只允许幂零奇异支撑，即排除来自环面方向的奇异；这给出精确陈述 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\simeq \\operatorname{IndCoh}_{\\mathcal N}(\\operatorname{Loc}_{\\check G})\\)。",
    r"\\(\\operatorname{IndCoh}\\)：ind-coherent sheaves；\\(\\operatorname{SS}\\)：奇异支撑；\\(\\mathcal N\\)：整体幂零锥。",
    [
        "\\(\\operatorname{QCoh}\\) 太小：它不包含奇异点处的“δ-函数”型对象。",
        "\\(\\operatorname{IndCoh}\\) 允许这些广义对象，但需要奇异支撑条件。",
        "幂零条件排除环面方向的奇异，正好匹配自守侧的层。",
        "这是 GLC 精确陈述中最容易被忽略的修正。",
    ],
    [
        r"\\operatorname{Shv}(\\operatorname{Bun}_G)\\simeq \\operatorname{IndCoh}_{\\mathcal N}(\\operatorname{Loc}_{\\check G})",
        r"\\operatorname{SS}(\\mathcal F)\\subset \\mathcal N",
    ],
    [T(
        "精确 GLC 陈述",
        r"存在保持谱作用的等价 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\simeq \\operatorname{IndCoh}_{\\mathcal N}(\\operatorname{Loc}_{\\check G})\\)。",
        [
            ("从 \\(\\operatorname{QCoh}\\) 扩展到 \\(\\operatorname{IndCoh}\\)，允许广义层。", "奇异点上的凝聚层没有有限向量丛分解，必须用 \\(\\operatorname{IndCoh}\\)。"),
            ("用 \\(\\operatorname{SS}\\) 限制奇异支撑在 \\(\\mathcal N\\) 上。", "Arinkin–Gaitsgory 证明自守侧的奇异支撑正好落在幂零锥。"),
        ],
        "survey 只给陈述；完整定义与证明见 Arinkin–Gaitsgory。",
        "§5.1 / p.21",
    )],
    [
        "\\(\\operatorname{IndCoh}\\) 不是 \\(\\operatorname{QCoh}\\) 的“更大版本”那么简单；它的 Hom 与张量结构不同。",
        "幂零奇异支撑不是“没有奇异”，而是“只在幂零方向允许奇异”。",
    ],
    ["bzg/concept/glc-statement", "bzg/concept/abelianization", "bzg/concept/spectral-action"],
    "§5.1", [21],
))

# ---------------------------------------------------------------- D 因子化 / 证明
cards.append(C(
    "factorization", "D", "因子化与 \\(E_n\\) 结构",
    ["factorization", "因子化", "E_n operad"],
    "Hecke 范畴在曲线上的不同点之间满足因子化/交换性，用 \\(E_n\\)-operad 与因子化同调组织。",
    "为什么不同点的 Hecke 算子可以交换，因子化结构如何把局部作用粘成全局作用？",
    r"Hecke 范畴在点 \\(x\\) 的局部作用，随 \\(x\\) 变化构成因子化结构：在不相交的圆盘上，Hecke 范畴的卷积同伦交换；用 \\(E_n\\)-operad（\\(n=2\\) 对应曲线）描述。因子化同调把局部 Hecke 作用粘成 \\(\\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})\\) 的全局作用。",
    r"\\(E_n\\)：小 \\(n\\)-圆盘 operad；因子化：对不相交开集的张量分解；\\(\\operatorname{Gr}_G\\simeq \\Omega^2 BG\\)。",
    [
        "因子化是“局部数据可以粘成全局对象”的代数结构。",
        "Hecke 算子的交换性来自 \\(E_2\\) 结构。",
        "因子化同调是谱作用的构造工具。",
        "它也是相对 Langlands 中 \\(\\Theta\\)-级数的技术基础。",
    ],
    [
        r"\\operatorname{Gr}_G\\simeq \\Omega^2 BG",
        r"\\operatorname{Hecke}_x*\\operatorname{Hecke}_y\\simeq \\operatorname{Hecke}_y*\\operatorname{Hecke}_x\\quad(x\\ne y)",
    ],
    [],
    [
        "交换性不是严格的，而是同伦意义下的 \\(E_2\\) 交换。",
        "因子化不是简单的张量积；它要求对不相交开集取值。",
    ],
    ["bzg/concept/spectral-action", "bzg/concept/spherical-hecke-category", "bzg/concept/geometric-satake"],
    "§3.2", [15],
))

cards.append(C(
    "relative-langlands", "D", "相对 Langlands 与 periods",
    ["relative Langlands", "相对 Langlands", "periods"],
    "相对 Langlands 研究自守形式上的“测量”（periods），并把它们与谱侧的对应测量匹配；L-函数只是其中一例。",
    "为什么几何 Langlands 的证明需要 periods，三类 period 分别起什么作用？",
    r"period 是自守形式空间上的线性泛函（或对偶地，与某个向量做内积）。相对 Langlands 预测哪些 period 与谱侧的哪些测量匹配。GLC 证明中的三类关键 period 是：Eisenstein \\(\\leftrightarrow\\) Eisenstein（归纳）、Whittaker \\(\\leftrightarrow\\) 整体截面（归一化/单射）、Kac–Moody \\(\\leftrightarrow\\) opers（构造/满射）。",
    r"period：测量；\\(\\Theta\\)-series：把局部数据在整体对称群上平均；Nahm pole：Whittaker period 的物理名。",
    [
        "period 是“可计算的测量”，比 L-函数更一般。",
        "三类 period 分别对应归纳、单射、满射。",
        "它们满足局部-整体兼容，通常写成 \\(\\Theta\\)-级数。",
        "相对 Langlands 把 GLC 与算术 Langlands 的 L-函数预测联系起来。",
    ],
    [
        r"\\text{period}:\\operatorname{Aut}\\to \\operatorname{Vect}",
        r"\\Theta(f)(g)=\\sum_{\\gamma\\in G(F)\\backslash G(\\mathbb A)} f(\\gamma g)",
    ],
    [],
    [
        "不要把所有 period 都当成 L-函数；L-函数只是特定测量。",
        "period 不是数，而是线性泛函/向量空间；要区分取值与函子性。",
    ],
    ["bzg/concept/eisenstein-series", "bzg/concept/whittaker-period", "bzg/concept/kac-moody-opers"],
    "§5.2", [22],
))

cards.append(C(
    "eisenstein-series", "D", "Eisenstein 级数与抛物诱导",
    ["Eisenstein series", "Eisenstein 级数", "parabolic induction"],
    "Eisenstein 级数从 Levi 子群的抛物诱导构造，提供 GLC 的归纳步骤，把一般情形归约到尖点情形。",
    "Eisenstein 级数如何把 GLC 归约到尖点情形，为什么它是“最难也最容易”的部分？",
    r"设 \\(P=MU\\subset G\\) 是抛物子群。从 \\(M\\) 的表示/层出发，抛物诱导得到 \\(G\\) 的表示/层；Eisenstein 级数是其整体化。CCF+24 证明 Eisenstein 构造与 Langlands 函子兼容：\\(\\mathbb L_G\\) 把 Eisenstein 部分送到谱侧的抛物诱导。于是 GLC 归约到尖点层。",
    r"\\(P\\)：抛物子群；\\(M\\)：Levi；\\(U\\)：幂单根；\\(\\operatorname{Eis}\\)：Eisenstein 函子。",
    [
        "Eisenstein 级数提供“从小子群到大群”的归纳。",
        "它与 Langlands 函子兼容，因此可以两边同时“减掉”。",
        "归约后只剩尖点层，尖点层由 Whittaker 与 Kac–Moody 处理。",
        "解析上 Eisenstein 级数产生连续谱，是难点的来源。",
    ],
    [
        r"\\operatorname{Eis}:\\operatorname{Shv}(\\operatorname{Bun}_M)\\to \\operatorname{Shv}(\\operatorname{Bun}_G)",
        r"\\mathbb L_G\\circ \\operatorname{Eis}_M\\simeq \\operatorname{Eis}_{\\check M}\\circ \\mathbb L_M",
    ],
    [T(
        "Eisenstein 与 Langlands 函子兼容",
        r"\\(\\mathbb L_G\\) 把 \\(M\\) 的 Eisenstein 部分送到 \\(\\check M\\) 的抛物诱导。",
        [
            ("从 \\(M\\) 的层出发做抛物诱导。", "抛物诱导是 \\(G\\) 的表示/层的标准构造。"),
            ("验证 \\(\\mathbb L_G\\) 与诱导交换。", "CCF+24 证明 Langlands 函子在 Eisenstein 部分与抛物诱导相容。"),
            ("取正交补得到尖点层。", "Eisenstein 部分可被“减掉”，剩下尖点层。"),
        ],
        "survey 只给架构；完整证明见 CCF+24。",
        "§5.3 / p.23",
    )],
    [
        "Eisenstein 级数不是尖点形式；它贡献连续谱。",
        "抛物诱导依赖 \\(P\\) 的选择，但 Levi 的共轭类不依赖。",
    ],
    ["bzg/concept/relative-langlands", "bzg/concept/proof-map", "bzg/concept/whittaker-period"],
    "§5.3", [23],
))

cards.append(C(
    "whittaker-period", "D", "Whittaker period 与白光",
    ["Whittaker period", "Whittaker sheaf", "white light"],
    "Whittaker period 是 GLC 中的“白光”：它把单位元处的 δ-函数送到谱侧的常数函数，用来归一化并证明单射性。",
    "为什么 Whittaker 层扮演白光，它如何给出 Langlands 函子的单射性？",
    r"在 Fourier 变换中，白光对应 \\(\\delta_0\\)，其变换是常数函数 \\(1\\)。非阿情形用 Whittaker 层 \\(\\operatorname{Whit}_G\\) 代替 \\(\\delta_0\\)：它对应谱侧的 \\(\\mathcal O_{\\operatorname{Loc}_{\\check G}}\\)。用 Hecke 作用得到函子 \\(F\\mapsto F*\\operatorname{Whit}_G\\)，从 \\(\\operatorname{QCoh}(\\operatorname{Loc}_{\\check G})\\) 到 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\)。FrR25/NT25 证明 Whittaker 系数在尖点层上不消灭，从而 \\(\\mathbb L_G\\) 单射。",
    r"\\(\\operatorname{Whit}_G\\)：Whittaker 层；Nahm pole：其物理对应；Hitchin section：其 microlocal 图像。",
    [
        "Whittaker 层是“单位元处的 δ-函数”的非阿类比。",
        "它给出从谱侧到自守侧的函子，是 \\(\\mathbb L_G\\) 的伴随方向。",
        "Whittaker 系数不消灭尖点层，保证单射性。",
        "它的 microlocal 图像是 Hitchin section，横截于 Hitchin 纤维。",
    ],
    [
        r"\\operatorname{Whit}_G\\ \\longleftrightarrow\\ \\mathcal O_{\\operatorname{Loc}_{\\check G}}",
        r"F\\mapsto F*\\operatorname{Whit}_G",
    ],
    [T(
        "Whittaker 单射性",
        r"\\(\\mathbb L_G\\) 在尖点层上是单射；Whittaker 系数不消灭非零尖点层。",
        [
            ("用 Hitchin section 描述 Whittaker 层的奇异支撑。", "Whittaker 层对应 Hitchin 截面，横截于 Hitchin 纤维。"),
            ("证明 Whittaker 系数在尖点层上忠实。", "FrR25/NT25 用 microlocal 分析证明非退化性。"),
            ("结合 Eisenstein 归纳得到整体单射性。", "尖点部分单射，Eisenstein 部分由归纳处理。"),
        ],
        "survey 只给论证线索；完整证明见 FrR25/NT25 与 GR24a。",
        "§5.4 / p.23",
    )],
    [
        "Whittaker 层不是常数层；它带有幂单特征。",
        "Whittaker 系数不消灭尖点层，这与数论中某些 L-函数可能消失的经验相反。",
    ],
    ["bzg/concept/relative-langlands", "bzg/concept/kac-moody-opers", "bzg/concept/proof-map"],
    "§5.4", [23],
))

cards.append(C(
    "kac-moody-opers", "D", "Kac–Moody 局部化与 opers",
    ["Kac-Moody localization", "opers", "Kac-Moody period"],
    "用临界水平 Kac–Moody 表示与 Beilinson–Bernstein 局部化构造尖点层；其对偶参数是 opers。",
    "Kac–Moody 局部化如何构造尖点自守层，opers 为什么是对应的 Langlands 参数？",
    r"临界水平 \\(\\hat{\\mathfrak g}_{\\mathrm{crit}}\\) 的表示通过 Beilinson–Bernstein 局部化给出 \\(\\operatorname{Bun}_G\\) 上的 \\(D\\)-模。Feigin–Frenkel 定理把中心与 opers 联系起来：\\(\\operatorname{Op}_{\\check G}(C)\\subset \\operatorname{Loc}_{\\check G}(C)\\)。ABC+24b 把这套构造做成因子化机器，构造足够多的尖点层，从而证明 Langlands 函子的满射性。",
    r"\\(\\hat{\\mathfrak g}_{\\mathrm{crit}}\\)：临界水平仿射 Kac–Moody 代数；\\(\\operatorname{Op}_{\\check G}\\)：opers；\\(D_{\\operatorname{Bun}_G}\\)：微分算子层。",
    [
        "Kac–Moody 表示提供“写下来”的尖点层。",
        "Beilinson–Bernstein 局部化把表示变成 \\(D\\)-模。",
        "Feigin–Frenkel 把中心/参数识别为 opers。",
        "opers 只是 \\(\\operatorname{Loc}_{\\check G}\\) 的半维子簇，但每个不可约局部系统在有限多个点后可有 oper 结构。",
    ],
    [
        r"\\operatorname{Op}_{\\check G}(C)\\subset \\operatorname{Loc}_{\\check G}(C)",
        r"\\operatorname{Rep}(\\hat{\\mathfrak g}_{\\mathrm{crit}})\\longrightarrow \\operatorname{DMod}(\\operatorname{Bun}_G)",
    ],
    [T(
        "Kac–Moody 构造",
        r"临界水平 Kac–Moody 表示的 Beilinson–Bernstein 局部化给出尖点 \\(D\\)-模，其谱参数由 opers 给出。",
        [
            ("取临界水平的 Kac–Moody 表示。", "临界水平使中心作用与 opers 对应。"),
            ("用 Beilinson–Bernstein 局部化得到 \\(\\operatorname{Bun}_G\\) 上的 \\(D\\)-模。", "局部化把 Lie 代数表示变成微分算子作用。"),
            ("用 Feigin–Frenkel 识别谱参数为 opers。", "中心同构于 opers 上的函数。"),
        ],
        "survey 只给架构；完整构造见 ABC+24b。",
        "§5.5 / p.25",
    )],
    [
        "Kac–Moody 表示不积分到群；这是 de Rham 版本特有的现象。",
        "opers 不是所有局部系统；需要有理 oper 结构，且选择在有限点后。",
    ],
    ["bzg/concept/feigin-frenkel", "bzg/concept/beilinson-bernstein", "bzg/concept/whittaker-period"],
    "§5.5", [25],
))

cards.append(C(
    "feigin-frenkel", "D", "Feigin–Frenkel 定理",
    ["Feigin-Frenkel theorem", "Feigin–Frenkel", "center of Kac-Moody"],
    "临界水平 Kac–Moody 代数的中心同构于 opers 上的函数，从而把表示论参数与 Langlands 参数连接起来。",
    "Feigin–Frenkel 定理为什么能把 Kac–Moody 表示的中心与 opers 等同起来？",
    r"Feigin–Frenkel 定理断言临界水平仿射 Kac–Moody 代数 \\(\\hat{\\mathfrak g}_{\\mathrm{crit}}\\) 的中心 \\(Z(\\hat{\\mathfrak g}_{\\mathrm{crit}})\\) 同构于穿孔圆盘上 \\(\\check G\\)-opers 的函数环。于是临界水平表示给出 opers 上的族，成为 GLC 的谱参数。",
    r"\\(Z\\)：中心；\\(\\operatorname{Op}_{\\check G}(D^\\times)\\)：穿孔圆盘上的 opers；顶点代数：证明工具。",
    [
        "中心是交换代数，因此可以看成 opers 上的函数。",
        "临界水平是唯一使中心足够大的水平。",
        "该定理是 Kac–Moody 构造尖点层的表示论基础。",
        "它把“表示论参数”与“Langlands 参数”直接桥接。",
    ],
    [
        r"Z(\\hat{\\mathfrak g}_{\\mathrm{crit}})\\cong \\operatorname{Fun}(\\operatorname{Op}_{\\check G}(D^\\times))",
        r"\\operatorname{Op}_{\\check G}(D^\\times)\\subset \\operatorname{Loc}_{\\check G}(D^\\times)",
    ],
    [T(
        "Feigin–Frenkel",
        r"临界水平 Kac–Moody 代数的中心同构于 opers 上的函数。",
        [
            ("用顶点代数计算中心。", "临界水平使中心由 Sugawara 构造与 opers 生成。"),
            ("把中心的作用与 opers 的坐标比较。", "中心生成元对应 opers 的系数函数。"),
        ],
        "survey 只给陈述；完整证明见 Feigin–Frenkel 1992。",
        "§5.5 / p.25",
    )],
    [
        "临界水平不是任意水平；非临界时中心太小。",
        "opers 在穿孔圆盘上定义，不是整个紧曲线；全局化需要额外步骤。",
    ],
    ["bzg/concept/kac-moody-opers", "bzg/concept/beilinson-bernstein", "bzg/concept/dual-group"],
    "§5.5", [25],
))

cards.append(C(
    "beilinson-bernstein", "D", "Beilinson–Bernstein 局部化",
    ["Beilinson-Bernstein localization", "BB localization", "D-modules on Bun_G"],
    "Beilinson–Bernstein 局部化把 Lie 代数表示变成旗簇/\\(\\operatorname{Bun}_G\\) 上的 \\(D\\)-模，是 Kac–Moody 构造的执行机制。",
    "Beilinson–Bernstein 局部化如何把表示变成 \\(D\\)-模，为什么它适用于 \\(\\operatorname{Bun}_G\\)？",
    r"Beilinson–Bernstein 局部化把一个半单 Lie 代数 \\(\\mathfrak g\\) 的表示范畴与旗簇上的 \\(D\\)-模联系起来。在 GLC 中，把 \\(\\hat{\\mathfrak g}_{\\mathrm{crit}}\\) 的表示局部化到 \\(\\operatorname{Bun}_G\\) 上，得到整体微分算子 \\(D_{\\operatorname{Bun}_G}\\) 作用下的 \\(D\\)-模；这些 \\(D\\)-模就是尖点层的来源。",
    r"\\(\\mathfrak g\\)：Lie 代数；\\(D_X\\)：微分算子层；\\(\\operatorname{Bun}_G\\)：丛模叠；临界水平：中心作用。",
    [
        "局部化把表示论问题变成几何 \\(D\\)-模问题。",
        "在 \\(\\operatorname{Bun}_G\\) 上，整体微分算子给出 Hecke 特征方程。",
        "它是 Kac–Moody 构造与 opers 之间的桥梁。",
        "局部化的技术难点是中心特征与 twisted \\(D\\)-模。",
    ],
    [
        r"\\operatorname{DMod}(\\operatorname{Bun}_G)\\ \\leftarrow\\ \\operatorname{Rep}(\\hat{\\mathfrak g}_{\\mathrm{crit}})",
        r"\\Gamma(\\operatorname{Bun}_G,D_{\\operatorname{Bun}_G})",
    ],
    [T(
        "Beilinson–Bernstein 局部化",
        r"在适当的中心特征下，\\(\\mathfrak g\\)-表示范畴等价于旗簇上的 twisted \\(D\\)-模。",
        [
            ("取 \\(\\mathfrak g\\) 的表示 \\(V\\)。", "表示给出 \\(U(\\mathfrak g)\\) 的作用。"),
            ("构造 \\(D\\)-模 \\(D_X\\otimes_{U(\\mathfrak g)}V\\)。", "局部化函子把表示变成微分算子作用。"),
            ("验证整体截面/中心特征相容。", "中心特征决定 twisted \\(D\\)-模的扭曲。"),
        ],
        "survey 只给应用；完整陈述与证明见 Beilinson–Bernstein 1981。",
        "§5.5 / p.25",
    )],
    [
        "局部化不是对所有表示都成立；需要中心特征与正则性条件。",
        "在 \\(\\operatorname{Bun}_G\\) 上要做整体化，不能直接套旗簇版本。",
    ],
    ["bzg/concept/kac-moody-opers", "bzg/concept/feigin-frenkel", "bzg/concept/whittaker-period"],
    "§5.5", [25],
))

cards.append(C(
    "theta-series", "D", "\\(\\Theta\\)-级数与局部-整体兼容",
    ["Theta series", "Θ-级数", "local-to-global"],
    "\\(\\Theta\\)-级数把局部数据在整体对称群上平均，是 periods 满足局部-整体兼容/因子化的具体机制。",
    "\\(\\Theta\\)-级数如何把局部数据粘成整体 period，因子化性质为什么关键？",
    r"给定局部数据 \\(f=\\otimes_v f_v\\)，\\(\\Theta\\)-级数定义为 \\(\\Theta(f)(g)=\\sum_{\\gamma\\in G(F)\\backslash G(\\mathbb A)} f(\\gamma g)\\)。它是经典 \\(\\theta\\)-函数的非阿推广。\\(\\Theta\\)-级数满足因子化：当局部点碰撞时，构造相容；这使 periods 可以局部地计算再整体粘合。",
    r"\\(F\\)：整体域；\\(\\mathbb A\\)：adele 环；\\(f_v\\)：局部数据；\\(\\Theta\\)：平均。",
    [
        "\\(\\Theta\\)-级数是“局部数据 \\(\\to\\) 整体自守形式”的显式构造。",
        "因子化保证局部构造在碰撞时相容。",
        "三类 period 都通过 \\(\\Theta\\)-级数实现局部-整体兼容。",
        "技术复杂度是 GLC 证明长的重要原因。",
    ],
    [
        r"\\Theta(f)(g)=\\sum_{\\gamma\\in G(F)\\backslash G(\\mathbb A)} f(\\gamma g)",
        r"\\Theta(f)=\\int_{G(F)\\backslash G(\\mathbb A)} f(g)\\,dg\\quad\\text{(adelic form)}",
    ],
    [],
    [
        "\\(\\Theta\\)-级数不是 Eisenstein 级数；它更一般，Eisenstein 是其中一例。",
        "收敛性需要增长条件；不能对任意局部数据求和。",
    ],
    ["bzg/concept/relative-langlands", "bzg/concept/eisenstein-series", "bzg/concept/factorization"],
    "§5.2", [22],
))

# ---------------------------------------------------------------- E 应用
cards.append(C(
    "ramified-glc", "E", "分歧几何 Langlands",
    ["ramified GLC", "分歧几何 Langlands", "tame ramification"],
    "分歧 GLC 允许局部系统在标记点有极点/分歧；Bezrukavnikov 的 tame 几何 Satake 给出部分框架，但一般情形仍 open。",
    "“无分歧”排除了什么，分歧 GLC 目前知道到什么程度？",
    r"无分歧 GLC 只考虑 \\(C\\) 上整体定义的局部系统。分歧版本允许在标记点 \\(x_1,\\dots,x_n\\) 有极点/正则奇异性，即 \\(C\\setminus\\{x_i\\}\\) 上的局部系统。Bezrukavnikov 把几何 Satake 推广到 tame 分歧（抛物丛/正则奇异联络），给出 tame GLC 的精确表述；一般分歧仍 open，需要局部 GLC。",
    r"\\(C\\setminus\\{x_i\\}\\)：穿孔曲线；tame：惰性分歧；parabolic：抛物结构；regular singular：正则奇异。",
    [
        "无分歧是“局部系统整体定义”的情形。",
        "tame 分歧由 Bezrukavnikov 的几何 Satake 处理。",
        "wild 分歧需要局部 GLC 与更复杂的表示论。",
        "分歧版本是当前活跃的研究前沿。",
    ],
    [
        r"\\operatorname{Loc}_{\\check G}(C\\setminus\\{x_1,\\dots,x_n\\})",
        r"\\text{tame GLC}\\ \\subset\\ \\text{ramified GLC}\\ \\subset\\ \\text{open}",
    ],
    [T(
        "Bezrukavnikov 的 tame 几何 Satake",
        r"几何 Satake 等价可以推广到 tame 分歧的抛物/正则奇异 setting。",
        [
            ("把 \\(\\operatorname{Gr}_G\\) 换成仿射旗簇/抛物版本。", "tame 分歧对应抛物结构与正则奇异性。"),
            ("用等变层与 Springer 型理论建立 monoidal 等价。", "Bezrukavnikov 的非交换 Springer 分辨给出推广。"),
        ],
        "survey 只给陈述；完整证明见 Bezrukavnikov 2006/2016。",
        "§6.0.1 / p.26",
    )],
    [
        "tame 不等于 wild；wild 分歧需要完全不同的技术。",
        "分歧 GLC 不是无分歧 GLC 的直接特例；局部系统在标记点的行为必须显式化。",
    ],
    ["bzg/concept/local-langlands", "bzg/concept/geometric-satake", "bzg/concept/glc-statement"],
    "§6.0.1", [26],
))

cards.append(C(
    "local-langlands", "E", "局部 Langlands 与 Fargues–Scholze",
    ["local Langlands", "局部 Langlands", "Fargues-Scholze"],
    "局部 Langlands 把 \\(G(F)\\) 的表示范畴与 Langlands 参数联系起来；Fargues–Scholze 把它实现为 Fargues–Fontaine 曲线上的几何 Langlands。",
    "局部 Langlands 与几何 Langlands 有什么结构上的平行，Fargues–Scholze 如何把前者变成后者的实例？",
    r"局部 Langlands 对应（LLC）预测 \\(G(F)\\) 的表示与 Langlands 参数（\\(\\check G\\)-值的 Weil–Deligne 表示）之间的对应。Fargues–Scholze 在 \\(p\\)-进情形把 LLC 实现为 Fargues–Fontaine 曲线上的几何 Langlands；Scholze 在实情形用 twistor \\(\\mathbb P^1\\) 做类似构造。",
    r"\\(F\\)：局部域；\\(G(F)\\)：局部群；\\(\\check G\\)：对偶群；Fargues–Fontaine 曲线：\\(p\\)-进曲线。",
    [
        "LLC 是“局部”的谱定理；GLC 是“整体曲线”的谱定理。",
        "Fargues–Scholze 把 LLC 变成几何 Langlands 的实例。",
        "这给出 GLC 技术（因子化、谱作用）影响数论的直接路径。",
        "\\(p\\)-进解析表示是新的前沿。",
    ],
    [
        r"\\operatorname{Rep}(G(F))\\ \\longleftrightarrow\\ \\operatorname{Loc}_{\\check G}(\\text{Fargues--Fontaine curve})",
        r"L^2(G(F)\\backslash G(\\mathbb A))",
    ],
    [],
    [
        "局部 Langlands 不是整体 Langlands 的简单限制；参数与表示范畴的结构不同。",
        "Fargues–Fontaine 曲线不是通常的代数曲线；不要把它当成 \\(C\\)。",
    ],
    ["bzg/concept/ramified-glc", "bzg/concept/function-field-langlands", "bzg/concept/glc-overview"],
    "§6.1", [28],
))

cards.append(C(
    "function-field-langlands", "E", "函数域 Langlands 与 Weil 罗塞塔",
    ["function field Langlands", "函数域 Langlands", "Weil Rosetta Stone"],
    "函数域 Langlands 通过 Frobenius 迹把几何 Langlands 的范畴分解退化为经典自守形式分解。",
    "Weil 罗塞塔如何把几何 Langlands 与函数域 Langlands 联系起来，Frobenius 迹起什么作用？",
    r"Weil 罗塞塔把数域与 \\(\\mathbb F_q\\) 上的函数域类比，把 Riemann 面与 \\(\\overline{\\mathbb F}_q\\) 上的曲线类比。对 \\(\\mathbb F_q\\)-曲线，Frobenius 迹（函数-层对应）把几何层范畴的分解退化为自守形式的谱分解。几何 Langlands 的 étale 版本经 Frobenius 迹推出函数域 Langlands 的强化形式。",
    r"\\(\\mathbb F_q\\)：有限域；Frobenius：\\(x\\mapsto x^q\\)；函数-层对应：把点计数写成层的迹。",
    [
        "几何 Langlands 是“范畴版”，函数域 Langlands 是其 Frobenius 迹。",
        "Ngô 的基本引理、Lafforgue 的函数域对应都受几何思想影响。",
        "GR25 证明了正特征无分歧 Langlands 的很大一部分。",
        "Ramanujan/Arthur 猜想仍是前沿。",
    ],
    [
        r"\\operatorname{Tr}(\\operatorname{Frob}_q,\\operatorname{Shv}(\\operatorname{Bun}_G))\\rightsquigarrow \\text{automorphic forms}",
        r"\\mathbb F_q(C)\\ \\longleftrightarrow\\ \\mathbb Q",
    ],
    [T(
        "函数域 Langlands（无分歧）",
        r"几何 Langlands 的 étale 版本经 Frobenius 迹推出函数域上的无分歧 Langlands 对应。",
        [
            ("取 \\(\\mathbb F_q\\)-曲线上的 étale 层。", "étale 版本在任意代数闭域上有意义。"),
            ("对 Frobenius 取迹，得到自守形式。", "Grothendieck 函数-层对应把层的迹写成点计数。"),
        ],
        "survey 只给架构；完整陈述见 AGK+21、GR25。",
        "§6.1 / p.28",
    )],
    [
        "Frobenius 迹不是简单的逐点求值；它需要层的六函子与迹形式。",
        "函数域结果不能直接搬到数域；Weil 罗塞塔只是类比。",
    ],
    ["bzg/concept/local-langlands", "bzg/concept/glc-statement", "bzg/concept/low-genus"],
    "§6.1", [28],
))

cards.append(C(
    "low-genus", "E", "低亏格与可积系统",
    ["low genus GLC", "低亏格", "integrable systems"],
    "在亏格 0/1 时 GLC 的两侧变成显式经典对象，并与 Gaudin、Calogero–Moser 等量子可积系统相连。",
    "为什么低亏格情形特别有价值，GLC 如何给出量子可积系统的解？",
    r"当 \\(g=0\\) 或 \\(1\\) 时，\\(\\operatorname{Loc}_{\\check G}\\) 与 \\(\\operatorname{Bun}_G\\) 都变得显式：亏格 1 时 Langlands 参数是交换矩阵对，亏格 0 带标记点时是 meromorphic ODE/刚性局部系统。GLC 的谱分解对应 Gaudin 自旋链、Calogero–Moser 系统等量子可积系统的联合谱。",
    r"\\(g\\)：亏格；Gaudin：自旋链；Calogero–Moser：粒子系统；rigid local system：刚性局部系统。",
    [
        "低亏格把无限维几何问题变成有限维/经典问题。",
        "亏格 1 的参数是交换矩阵对，仍有丰富模空间。",
        "GLC 给出可积系统联合谱的 Langlands 参数描述。",
        "Yun 用低亏格/刚性局部系统解决了一些逆 Galois 问题。",
    ],
    [
        r"g=1:\\ \\operatorname{Loc}_{\\check G}(E)=\\{(A,B)\\in \\check G^2\\mid [A,B]=1\\}/\\check G",
        r"\\text{joint spectrum of Gaudin}\\ \\longleftrightarrow\\ \\text{Langlands parameters}",
    ],
    [],
    [
        "亏格 1 不是“平凡”；交换矩阵对的模空间仍很复杂。",
        "低亏格的显式描述不能直接推广到高亏格。",
    ],
    ["bzg/concept/function-field-langlands", "bzg/concept/hitchin-fibration", "bzg/concept/physics-s-duality"],
    "§6.0.3", [27],
))

cards.append(C(
    "physics-s-duality", "E", "S-对偶、Kapustin–Witten 与 3-流形",
    ["S-duality", "Kapustin-Witten", "geometric Langlands and physics"],
    "Kapustin–Witten 说明 GLC 来自 4d \\(\\mathcal N=4\\) 超 Yang–Mills 的 S-对偶，经扭曲与降维得到 2d TQFT 的边界条件范畴。",
    "物理上的 S-对偶如何推出几何 Langlands，扭曲与降维各自丢弃了什么信息？",
    r"4d \\(\\mathcal N=4\\) 超 Yang–Mills 的 Montonen–Olive S-对偶断言 \\(G\\) 与 \\(\\check G\\) 的理论等价。Kapustin–Witten 通过拓扑扭曲（取超对称微分上同调）去掉度量依赖，再限制到 \\(C\\times\\Sigma\\) 并取边界条件范畴，得到 \\(\\operatorname{Shv}(\\operatorname{Bun}_G)\\) 与 \\(\\operatorname{Loc}_{\\check G}\\) 的对应。参数 \\(\\Psi\\in\\mathbb P^1\\) 给出 A/B 模型与量子 GLC。",
    r"\\(\\mathcal N=4\\)：最大超对称；S-对偶：强耦合/弱耦合；A-model/B-model：拓扑弦；\\(\\Psi\\)：扭曲参数。",
    [
        "S-对偶是 GLC 的物理起源。",
        "拓扑扭曲去掉动力学，只留下拓扑/全纯数据。",
        "降维到 \\(C\\times\\Sigma\\) 后取边界条件范畴。",
        "证明 GLC 后可得 3-流形上的自守形式与 skein 模的 Langlands 对偶。",
    ],
    [
        r"A_G\\simeq B_{\\check G}",
        r"A_G(C)=\\operatorname{Shv}_{\\mathcal N}(\\operatorname{Bun}_G(C))",
    ],
    [],
    [
        "物理推导不是数学证明；它给出的是猜想与结构。",
        "扭曲后的理论不是原来的 4d 理论；不要把它当成完全等价。",
    ],
    ["bzg/concept/glc-overview", "bzg/concept/low-genus", "bzg/concept/quantum-glc"],
    "§6.2", [29],
))

cards.append(C(
    "quantum-glc", "E", "量子几何 Langlands",
    ["quantum GLC", "量子几何 Langlands", "quantum geometric Langlands"],
    "量子 GLC 是 GLC 的形变：用扭曲 \\(D\\)-模/量子群替换通常层范畴，关于 \\(G\\) 与 \\(\\check G\\) 对称。",
    "量子 GLC 与通常 GLC 的关系是什么，为什么它关于 \\(G\\) 与 \\(\\check G\\) 更对称？",
    r"量子 GLC 是 GLC 的形变：de Rham 侧用扭曲 \\(D\\)-模 \\(\\operatorname{DMod}_\\kappa\\)，Betti 侧用量子群；它关于 \\(G\\) 与 \\(\\check G\\) 对称，且与 4d \\(\\mathcal N=4\\) 理论的 \\(\\Psi\\)-族相关。局部关键是基本局部等价（Fundamental Local Equivalence），联系仿射 Kac–Moody 表示与量子群。",
    r"\\(\\kappa\\)：扭曲水平；\\(\\operatorname{DMod}_\\kappa\\)：扭曲 \\(D\\)-模；FLE：Fundamental Local Equivalence；\\(\\Psi\\)：S-对偶参数。",
    [
        "量子 GLC 是 GLC 的形变，不是另一个无关的猜想。",
        "它关于 \\(G\\) 与 \\(\\check G\\) 对称，这一点比通常 GLC 更明显。",
        "Kac–Moody 与 Whittaker period 有量子版本，并在对偶下互换。",
        "FLE 是量子 GLC 的局部核心。",
    ],
    [
        r"\\operatorname{DMod}_\\kappa(\\operatorname{Bun}_G)\\ \\rightsquigarrow\\ \\operatorname{DMod}_{\\check\\kappa}(\\operatorname{Bun}_{\\check G})",
        r"\\text{FLE}:\\ \\operatorname{Rep}(\\hat{\\mathfrak g}_\\kappa)\\ \\longleftrightarrow\\ \\operatorname{Rep}_q(\\mathfrak g)",
    ],
    [],
    [
        "量子 GLC 仍 open；不要把它当成已证明。",
        "\\(\\kappa\\) 与 \\(\\check\\kappa\\) 是配对水平，不能写成同一个 $\\kappa$。",
    ],
    ["bzg/concept/glc-statement", "bzg/concept/physics-s-duality", "bzg/concept/kac-moody-opers"],
    "§6.0.4", [27],
))

# ---------------------------------------------------------------- write
ids = {c["id"] for c in cards}
for c in cards:
    for r in c["related"]:
        assert r in ids, (c["id"], r)
    assert all(c["id"] != r for r in c["related"])

os.makedirs(OUT, exist_ok=True)
for c in cards:
    path = os.path.join(OUT, c["id"].split("/")[-1] + ".json")
    with io.open(path, "w", encoding="utf-8") as f:
        json.dump(c, f, ensure_ascii=False, indent=2)
        f.write("\n")

with io.open(os.path.join(ROOT, "verification.jsonl"), "w", encoding="utf-8") as f:
    for c in cards:
        rec = {
            "id": c["id"],
            "status": "source-only",
            "note": "逐句对齐 Ben-Zvi 2026 对应节；未做 nLab / Stacks 外部核验。",
            "checks": c["verification"]["checks"],
        }
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print("wrote %d cards" % len(cards))
for t in "OABCDE":
    print(t, sum(1 for c in cards if c["track"] == t))
