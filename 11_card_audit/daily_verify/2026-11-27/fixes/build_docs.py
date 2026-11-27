#!/usr/bin/env python3
"""生成 2026-11-27 修卡的案例集、施工说明与 TRACE。

只读 fix_log.json，写本目录下的 markdown/json。运行：
    python 11_card_audit/daily_verify/2026-11-27/fixes/build_docs.py
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIX_LOG = HERE / "fix_log.json"
CASEBOOK = HERE / "casebook"

CASES = [
    dict(
        key="siebert/correction/prop-3-12-lci",
        set="siebert", typ="correction", slug="prop-3-12-lci",
        title="命题 3.12：Gysin 拉回定义的起始页",
        severity="minor", modes="出处定位漂移",
        why="""`pitfalls[1]` 想提醒读者「Gysin 拉回只为 lci 嵌入定义」，却把统一定义的起点写成「p.51 起」。
讲义里 (3.58) 是 Definition 3.4，在 **p.50**；p.51 才出现 (3.64)。作者大概率是按 (3.64) 所在页概括了整组公式，
没有逐页核对 (3.58)——这是「按最后一个公式的页概括整段」的典型漂移。
另按本卡自己的要求，写成「p.50–51 + 两个编号各自页码」比只给起点更抗回查。""",
        disc="""当日核验第 1 张（lead 亲自核）。用 `siebert.txt` 按 `\\f` 定位 Prop 3.12 时顺手核了 pitfalls 里的 (3.58)(3.64)，
发现 (3.58) 在 PDF 58 页之前的 p.50，与「p.51 起」矛盾。""",
        ev=["`datasets/_audit/third_party_2026-11-26/tmp/sources/siebert.pdf` p.50：「Definition 3.4.」及 (3.58) `\\iota^![V]:=s_0^*[C_{W/V}]`；PDF p.51 为 (3.64)。",
            "卡内 `provenance_note` 写「原书 p.58…对照片 p.50–52 的 Gysin 拉回 (3.58)(3.64)」，本来就承认 50–52，与 pitfalls 的「p.51 起」自相矛盾。"],
        lean="不涉及定理形式化。若以后把 Gysin 拉回写成 Lean 定义，假设应是 `IsLci`（局部完全交态射），并在 docstring 引 (3.58) 的定义而不是页码。",
    ),
    dict(
        key="gtgl15/concept/eigenbranes",
        set="gtgl15", typ="concept", slug="eigenbranes",
        title="本征膜：把定义登记成了定理",
        severity="minor", modes="定理 / 猜想层级混淆",
        why="""eq (4.3)「LB ≅ B⊗V for some vector space V」在原文 §4.1 是**定义**，卡却把它单独列成 `theorems[0]`，
还标 `proof.status = "gap"`、gap_note 自认「未从第一原理证明本征值必为向量空间」。
这是把「定义的一部分」升级成「待证命题」：读者/形式化系统会去找证明，而原文根本没有这条定理。
同时 `definition.text` 说「固定向量空间」、theorem 说「有限维向量空间」，两处措辞也不一致。
本批按最小改动删除 `theorems[0]`（内容已被 `definition.text` 与 `key_points[1]` 覆盖），保留定义原样。""",
        disc="""当日核验第 3 张（lead 亲自核）。核对 §4.1 时发现 eq (4.3) 紧跟在「We say that…」之后，是定义句式；
再读 `theorems[0]`，其 statement 与 `definition.text` 同义，且 gap_note 自述「原文直接以定义形式给出」。""",
        ev=["`gtgl15.pdf` 印刷/PDF p.37：「We say that the brane B is an eigenbrane of the line operator L if LB = B ⊗ V (4.3) for some vector space V.」",
            "卡内 `theorems[0].proof.gap_note`：「原文 §4.1 直接以定义形式给出 eq (4.3)…未从第一原理证明本征值必为向量空间。」"],
        lean="Lean 里应写成 `def IsEigenbrane (L : LineOp) (B : Brane) : Prop := ∃ V : Type, …`；不要 `theorem … := by sorry`，否则定义被误当开放问题。",
    ),
    dict(
        key="kw/concept/n4-sym-theory",
        set="kw06", typ="concept", slug="n4-sym-theory",
        title="N=4 超杨–米尔斯：(2.14) 的页号（第二次修改）",
        severity="minor", modes="出处定位漂移",
        why="""`theorems[0].source` 原写「B p.7–11（eq (2.14) 在 p.11）」，但 (2.14) 在 PDF 第 11 页、页脚印的是 **10**；
p.11（PDF 12）才是 (2.15)。这是 PDF/印刷页偏移（+1）导致的 off-by-one。
需要说明：2026-11-26 批次已把该字段从 `B p.6` 改成 `B p.7–11（…p.11）`，当时把 (2.14) 记到了 p.11；
本批核对页脚后改为 p.10。按 WORKFLOW §9，这属于同一张卡的第二次修改，历史 fix_log 不改，
`datasets/_audit/third_party_2026-11-26/tools/verify_final.py` 因此会对本条报 1 个 STALE（预期，见施工说明）。""",
        disc="""当日核验第 4 张。子代理报「定理 source 疑似 off-by-one」，lead 用 `kw06.txt` 抽 PDF 10/11/12 三页页脚与
(2.14)(2.15) 位置复核：PDF 11 页脚 10 且 (2.14) 在该页，PDF 12 页脚 11 且 (2.15) 在该页。""",
        ev=["`kw06.pdf` PDF p.11（页脚 10）：`(2, 1, 4) ⊕ (1, 2, 4). (2.14)`；PDF p.12（页脚 11）：`(2.15)`。",
            "卡内 `theorems[1].source` 写「B p.11 eq (2.15)」，与本条修正后自洽。"],
        lean="与 Lean 无关；若把 (2.14) 写成表示分解，注意源是 (2,1,4̄)⊕(1,2,4)（本卡 11-26 已修 statement）。",
    ),
    dict(
        key="functoriality/concept/strip-shrinking",
        set="functoriality", typ="concept", slug="strip-shrinking",
        title="带收缩：定理页码整体后移两页",
        severity="minor", modes="出处定位漂移",
        why="""两处 `source` 与一处 `provenance_note` 都按 §3.5 的**起始页**（p.25–26）填，而两个定理分别在 p.27（定理 1.0.1 / eq (62)）
和 p.28（[WW15, Theorem 5.1] 的转述）。作者很可能只看了节标题页就概括整节，没有翻到定理正文。
`provenance_note` 又原样复制了同一个错范围，属「同一错误在多个字段重复」——修的时候必须一起改，否则两个版本并存。""",
        disc="""当日核验第 5 张。子代理逐条比对 arXiv:2210.11159v1 的 §3.5.2，发现 eq (62) 在 p.27；
lead 复核 p.28 的 [WW15, Theorem 5.1] 段，并发现 `provenance_note` 仍写 p.25–26（子代理只报了 theorems[].source）。""",
        ev=["arXiv:2210.11159v1 p.27：「3.5.2. Categorification commutes with composition.」",
            "同文 p.28：「Woodward showed in [WW15, Theorem 5.1] that under the same hypotheses of (62), and assuming …」"],
        lean="形式化带收缩时要显式「复合嵌入」前提（卡 pitfalls 已述）；定理本身的页号不影响陈述。",
    ),
    dict(
        key="ggl09/deriv/descent-to-xi",
        set="ggl09", typ="deriv", slug="descent-to-xi",
        title="下降给出 x_i(S)：边界的「差」取反了",
        severity="major", modes="逻辑方向反转 / 出处定位漂移",
        why="""原文说：S²×I 的**左（Neumann）与右（Dirichlet）边界之差**同调于环绕 w 的小 S²，且右边界上 x_i=0，
所以 x_i(Neumann)=x_i(S²)。推导步骤 5 却写成「Neumann 边界与小 S² 之差」——这个差恰好同调于**右边界**，
而右边界的 x_i=0，不可能「该差给出 x_i」。方向一取反，整步论证就断了。
失效点在于把「A 与 B 之差 ≅ C」误读成「A 与 C 之差 ≅ B」；三个对象两两成链时，谁减谁决定了 nonzero 落在哪。
另外 `steps[4].locator` 原写「A p.16 eq (2.10)」，只覆盖该步开头（取固定时刻的曲面）；
左/右边界与小 S² 的论证在 p.17，故本轮把 locator 一并扩为 p.16–17。""",
        disc="""当日核验第 6 张。子代理核对 arXiv:0905.4795v2 p.16–17 的相对同调论证时发现边界顺序与卡相反；
lead 用 `ggl09.txt` 重读 p.16「the left and right boundaries … is homologous to a small two-sphere」确认。
本轮独立复核顺手核 `steps[4].locator`：它只写到 p.16（该步开头的固定时刻曲面），而左/右边界论证已跨到 p.17，
故同批把 locator 扩为 p.16–17。""",
        ev=["`ggl09.pdf`/arXiv p.16：「the difference between the left and right boundaries of S² × I is homologous to a small two-sphere that links w」；p.16 另述右边界 Dirichlet 上 x_i=0。"],
        lean="形式化时用相对同调 `H_2(S²×I, ∂) ≅ H_1(S¹)` 或链群 `C_2(S²×I)/C_2(∂)`；边界条件进入相对链群，`x_i(right)=0` 应作为假设显式写出。",
    ),
    dict(
        key="siebert/concept/gromov-witten-invariant",
        set="siebert", typ="concept", slug="gromov-witten-invariant",
        title="GW 不变量的形变不变性：lci 被换成了「连通」",
        severity="major", modes="适用范围遗漏 / 条件替换",
        why="""Prop 3.12 的假设是「S is lci」，结论是对**所有** s, s′ 有代数等价——不要求 S 连通。
`pitfalls[4]` 写成「只在『连通基底 + 代数等价』下成立」：删掉了 lci，加入了源里没有的连通。
更要命的是同批第 1 张卡（prop-3-12-lci 勘误）明确写「讲义原文也没有『同一连通分支』这一条」，
两卡对同一命题给出相反读法——这是跨卡一致性检查能抓到的典型冲突。""",
        disc="""当日核验第 12 张。子代理报 major 后，lead 用 `siebert.txt` p.58 逐字复核 Prop 3.12 原文，
并把它与第 1 张勘误卡的陈述对照，确认「连通」是新增条件、lci 是丢失条件。""",
        ev=["`siebert.pdf` p.58：「Proposition 3.12. If S is lci, then for all s, s′ we get an algebraic equivalence (3.121) [Ms]virt ∼ [Ms′]virt in A∗(M).」",
            "同批 `siebert/correction/prop-3-12-lci` 的 corrected 文本亦写「讲义原文也没有『同一连通分支』这一条」。"],
        lean="形式化 Prop 3.12 需要 `IsLci`（或 `Smooth ⇒ IsLci`）假设；连通性不在假设里，不要为了「同分支」再加 `ConnectedSpace`。",
    ),
    dict(
        key="lbook04/concept/ch9-langlands-spectral",
        set="lbook04", typ="concept", slug="ch9-langlands-spectral",
        title="Langlands 谱：带扭时的极点位置",
        severity="minor", modes="内部不一致 / 证据归属错误",
        why="""`key_points[2]` 说「反过来该条件也保证 s=1 处有极点」，但带 |det|^{iσ} 扭时 Thm 4.2 的极点在
s=−iσ 与 s=1−iσ，只有 σ=0 才退化成 s=1（卡自己的 `definition` 写的就是这对位置）。
另外它把「留数非零 ⇒ π ≅ π̃′⊗|det|^{iσ} 的反向」挂到「Thm 4.2 后的两条观察」，
而那两条观察是未扭情形（s=0,1 的单极点、以及 π≅π′ 的判据），反向陈述出自 Thm 2.2 的证明（印刷 p.210）。""",
        disc="""当日核验第 13 张。子代理对照 PDF p.225（印刷 222）Thm 4.2 的极点句与紧随的两条观察，lead 复核了
「s = -ia and s = 1- ia」与「simple poles at s = 0 and s = 1」两处引文（该 PDF 文本层把 π 抽成 rr/1i）。""",
        ev=["`bernstein_gelbart_introduction.pdf` p.222（PDF 225）：「then at s = -ia and s = 1- ia.」",
            "同页：「1. L(s, rr x 1i) has simple poles at s = 0 and s = 1.」（rr/1i 为 π 的抽取乱码）"],
        lean="形式化留数配对时，极点位置应参数化为 `s = -iσ` 与 `s = 1 - iσ`；σ=0 只是特例，不能写死 s=1。",
    ),
    dict(
        key="lbook04/concept/ch3-three-motives",
        set="lbook04", typ="concept", slug="ch3-three-motives",
        title="三个动机：定义正文超出所引页码",
        severity="minor", modes="页覆盖不足 / 出处定位漂移",
        why="""`sources[0].pages` 写 [39,40]，但卡自己的 `definition` 正文包含 §2.3 的内容：
τ′ = γτ、g(z;γτ) = (cτ+d)^k g(z;τ)、例 2.1 的 ℘ 函数与 G_k——这些在印刷 42–43（PDF 49–50）。
按 §4.5，卡的定义正文落在 cited 页之外即算错。根因是只按节标题页（§2 起于 39）填范围，没有覆盖定义实际走到的页。""",
        disc="""当日核验第 14 张。子代理发现定义里的模变换与 ℘ 例子在 42–43；lead 用原书 PDF 复核：
印刷 39=PDF 46、40=PDF 47、41=PDF 48、42=PDF 49、43=PDF 50，确认偏移 7。""",
        ev=["`bernstein_gelbart_introduction.pdf` 印刷 p.42（PDF 49）：「Example 2.1. The Weierstrass p-function of the lattice Λ is …」",
            "卡 `definition` 含 τ′ = γτ 与 g(z;γτ) 的变换式，位于 §2.3（印刷 42–43）。"],
        lean="形式化这三个动机时，权 k 与 level 要显式；页号不影响陈述，但 §2.3 的模变换是定义的一部分。",
    ),
    dict(
        key="bzg/concept/categorical-fourier",
        set="benzvi_glc", typ="concept", slug="categorical-fourier",
        title="范畴化 Fourier：被引 §2.1 里没有这条核公式",
        severity="major", modes="出处无法定位 / 证据强度夸大",
        why="""卡把 `FM_𝒦(F) = p_{Y!}(p_X^*F ⊗ 𝒦)` 记在 Ben-Zvi 2026 的 §2.1（p.8）名下。
但 p.8 的 §2.1 是「范畴 / Hilbert 空间」类比（brave new harmonic analysis），既没有这条公式，也没有 Poincaré 丛给出核的说法；
Fourier–Mukai 只在 §1.3（p.6）作为 categorical Fourier transforms 的 general theme 被提到，**不给核公式**（p.13/p.19 的 Mukai transform 是特例）。
这是把「标准定义」挂到了「只谈主题」的节上。修法：section 改 §1.3，加 `page_note` 说明公式按标准 Fourier–Mukai 变换整理，
并把 `verification` 里「逐句对齐该节」的断言改成「依据该节 general theme 整理」。""",
        disc="""当日核验第 17 张。子代理在 benzvi.txt 里搜 FM 公式无果，定位到 §1.3 p.6 的主题句与 §2.1 p.8 的类比段；
lead 复核原文两段，并检查 `verification.checks[0]` 仍写着 §2.1，一并改掉（否则旧定位还留在卡里）。""",
        ev=["`benzvi.pdf` p.6 §1.3：「This fits in a general theme of categorical Fourier transforms – these are equivalences of (derived) …」",
            "同文 p.8 §2.1：「2.1. The language: brave new harmonic and functional analysis.」"],
        lean="FM 函子形式化需要 `p_{Y!}` 的 proper 性（或取 `p_{Y*}` 并加额外假设）；核 𝒦 应作为参数，不要硬编码 Poincaré 丛。",
    ),
    dict(
        key="gw06/concept/two-dimensional-defect",
        set="gw06", typ="concept", slug="two-dimensional-defect",
        title="二维缺陷：离散 α,η 的互换在下一页",
        severity="minor", modes="页覆盖不足 / 出处定位漂移",
        why="""`page_note` 声称「印刷页 29–30」覆盖「极大列维情形的离散 α, η」，但 core 陈述
「𝒵(G) 与 Hom(π₁(G),U(1)) 在对偶下互换」在印刷 **31**（PDF 32）；29–30 只到 (2.63) 与「If α=0 … L=G, P=G_C, N=1」。
`pages`/`pdf_pages` 因此各少一页。根因同其他页覆盖问题：按「主要公式结束页」而不是「最后一句定义所在页」填。""",
        disc="""当日核验第 19 张。子代理报 page_note 与 definition 末句不一致；lead 用 `gw06.txt` 复核 PDF 31（印刷 30）
的 `L = G` 句与 PDF 32（印刷 31）的 `are exchanged by` 句，并把 `index.jsonl` 里派生的 pdf_pages 一并更新。""",
        ev=["`gw06.pdf` 印刷 31（PDF 32）：「The finite groups Z(G) and Hom(π1 (G), U (1)) are exchanged by …」",
            "印刷 30（PDF 31）：「If α = 0, we get a special case … L = G, P = G_C, N = 1」"],
        lean="符号约定 L=G、P=G_C、N=1（卡已述）是形式化时要对齐的；页号不影响陈述。",
    ),
    dict(
        key="glc/concept/fundamental-local-equivalence",
        set="glc", typ="concept", slug="fundamental-local-equivalence",
        title="基本局部等价：相对构造在 p.72",
        severity="minor", modes="页覆盖不足",
        why="""`definition.text` 末句与 `formulas[2]` 给出相对构造
`KL ⊗_{QCoh(Op^unr)} QCoh(Op^unr_{Ǧ}(X\\{x})) → DMod_crit(Bun_G)` 及 `Op(X\\{x})^unr` 的定义，
这些在印刷 **72**（PDF 72）；p.71 只到 `KL ≃ IndCoh(Op^unr)` 与 ∗/! 约定。`pages` 与 `pdf_pages` 都只有 [71]，
按 §4.5 属 cited 页覆盖不足。""",
        disc="""当日核验第 20 张。子代理比对 definition 末句与 p.71 末行，发现相对构造落在 p.72；lead 复核 `glc.txt`
p.72「Localization should enhance to a relative construction of the form」与 p.71「up to the usual ∗- versus !-IndCoh convention」。""",
        ev=["`glc.pdf` p.72 §14.6：「Localization should enhance to a relative construction of the form …」",
            "p.71 §14.6 末：「up to the usual ∗- versus !-IndCoh convention」"],
        lean="形式化该等价时要区分 `IndCoh` 与 `QCoh`、∗ 与 ! 的拉回方向；这是卡 pitfalls 里已强调的约定。",
    ),
    dict(
        key="sy38/concept/tamagawa-number",
        set="sy0238", typ="concept", slug="tamagawa-number",
        title="玉河数：Weil 猜想的完成者写成了一个不存在的合作者",
        severity="minor", modes="归因或作者错误",
        why="""`key_points[1]` 想说明 τ(SL_n)=1 是 Weil 猜想的特例，却把「一般情形」的完成者写成「Lai–Künnemann」。
标准史实是：Langlands（1966）证分裂情形，Rapoport（1976）与 Lai（1980）把证明改写到拟分裂情形，
Kottwitz（1988, Annals 127）用 Arthur 迹公式完成数域上的一般情形；函数域情形后来由 Gaitsgory–Lurie（2019）解决。
公开文献里没有「Lai–Künnemann」这条完成链：Künnemann 的公开著作目录（Regensburg）以 Arakelov 几何为主，
未见 Tamagawa 数的工作。这是把两个人名拼成一个不存在的合作者的「归因幻觉」，属历史归属错误，
不影响 τ 的定义与体积公式，故定 minor。""",
        disc="""本轮独立复核第 8 张。首轮核验其实已在 `notes` 里写下「Lai–Künnemann 这一历史归属无法核实」，
但因「本地一手源 p.7 只讲 τ 与体积公式、未给历史」而判 pass。本轮换路径：用 Lurie 的 AWS 课程大纲、
2025 年 Pacific J. Math. 综述的引用链与 Kottwitz 1988 原文的归属交叉核对，三处都给
「Langlands（分裂）→ Rapoport/Lai（拟分裂）→ Kottwitz（数域一般）」，没有 Lai–Künnemann，遂改判 issue。""",
        ev=["`Anschütz 2020` p.7 只给 `τ(G)` 的定义与 `τ(SL_n)=1` 的体积推论，未给完成者；卡的「原文只引 [Col11, Appendix B] 与 [Lur, Lecture 1]」本身不假。",
            "Lurie, *Tamagawa Numbers via Nonabelian Poincaré Duality*（AWS 课程大纲）：「When K is a number field, this conjecture was proven by Kottwitz (building on earlier work of Langlands and Lai).」（math.ias.edu/~lurie/282ynotes/syllabus.pdf）",
            "Pacific J. Math. 338 (2025) 综述：「first proved for split groups over number fields by Langlands [1966] … rewritten … for quasisplit groups by Rapoport [1976] and Lai [1980] … Kottwitz [1988] proved Weil's conjecture over number fields.」（msp.org/pjm/2025/338-1/pjm-v338-n1-p06-p.pdf）",
            "Kottwitz, *Tamagawa numbers*, Ann. of Math. 127 (1988), 629–646。"],
        lean="τ(G) 是体积，不是定理陈述里的对象；若要形式化，陈述写成 `TamagawaNumber G = 1`（G 单连通半单），历史归属放 docstring，不要写进类型或假设。",
    ),
]


def fmt_field(field: list) -> str:
    """['theorems', 0, 'source'] -> theorems[0].source"""
    out = ""
    for x in field:
        if isinstance(x, int):
            out += f"[{x}]"
        else:
            out += ("." if out else "") + str(x)
    return out


def build() -> None:
    log = {e["id"]: e for e in json.loads(FIX_LOG.read_text(encoding="utf-8"))}
    CASEBOOK.mkdir(parents=True, exist_ok=True)
    index = []
    for i, c in enumerate(CASES, 1):
        e = log[c["key"]]
        changes = e["changes"]
        fname = f"{c['set']}__{c['typ']}__{c['slug']}.md"
        lines = [
            "---",
            f"case: D27-{i:02d}",
            f"id: {c['key']}",
            f"set: {c['set']}",
            "group: daily-2026-11-27",
            f"severity: {c['severity']}",
            "confirmed_by: lead（2026-11-27 当日核验）",
            f"modes: {c['modes']}",
            "---",
            "",
            f"# 案例 D27-{i:02d} · {c['title']}",
            "",
            f"> **卡片**：`{e['id']}`<br>",
            f"> **路径**：`{e['path']}`<br>",
            f"> **判定**：{c['severity']}；确认者 lead（当日核验）<br>",
            f"> **失效模式**：{c['modes']}<br>",
            f"> **施工日期**：2026-11-27",
            "",
            "## 1. 正误对比",
            "",
        ]
        for j, ch in enumerate(changes, 1):
            field = fmt_field(ch["field"])
            b = ch["before"] if ch["before"] is not None else "（整段存在）"
            a = ch["after"] if ch["after"] is not None else "（整段删除）"
            lines += [
                f"### 1.{j} 字段 `{field}`",
                "",
                "**错误版本（卡上原文）**",
                "",
                "```text",
                b if isinstance(b, str) else json.dumps(b, ensure_ascii=False, indent=2),
                "```",
                "",
                "**正确版本（已替换）**",
                "",
                "```text",
                a if isinstance(a, str) else json.dumps(a, ensure_ascii=False, indent=2),
                "```",
                "",
            ]
            if ch.get("why"):
                lines += [f"改动理由：{ch['why']}", ""]
        lines += [
            "## 2. 为什么会错",
            "",
            "> 这是从错误形态反推的失效模式，不是原始模型的私有思维链。",
            "",
            c["why"].strip(),
            "",
            "## 3. 怎么发现的",
            "",
            c["disc"].strip(),
            "",
            "## 4. 证据锚点",
            "",
        ]
        lines += [f"- {x}" for x in c["ev"]]
        lines += [
            "",
            "## 5. 对形式化 / Lean 的提示",
            "",
            c["lean"].strip(),
            "",
            "## 6. 防再犯检查",
            "",
            "- [x] 改前在本案例集与 `11_card_audit/casebook/` 搜过同 id / 同字段。",
            "- [x] 页码改动已同时核对 PDF 页与印刷页，并附逐字引文。",
            "- [x] 符号 / 措辞改动已同步 md、生成器与 `verification` 中的旧定位。",
            "- [x] 改后 `json.load` 通过、`verify_final.py` 全量 0 parse error、`git diff --check` 干净。",
            "",
        ]
        (CASEBOOK / fname).write_text("\n".join(lines), encoding="utf-8", newline="\n")
        index.append(dict(case=f"D27-{i:02d}", id=c["key"], set=c["set"],
                          severity=c["severity"], modes=c["modes"],
                          file=f"casebook/{fname}", fix_count=len(changes)))
    (CASEBOOK / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n",
                                         encoding="utf-8", newline="\n")

    rows = "\n".join(
        f"| {e['case']} | [`{e['id']}`]({e['file'].split('/', 1)[1]}) | {e['severity']} | {e['modes']} | {e['fix_count']} |"
        for e in index
    )
    (CASEBOOK / "README.md").write_text(
        f"# 2026-11-27 修卡案例集（{len(index)} 例 / 13 条 issue / {sum(e['fix_count'] for e in index)} 处改动）\n\n"
        "本目录是 `11_card_audit/daily_verify/2026-11-27/` 当日核验的**修卡归档**，独立于\n"
        "`11_card_audit/casebook/` 的 32 例（后者的 `index.json` 被 `check_casebook.py` 硬编码为 32 条，\n"
        "按既有约定不再追加，参见 `11_card_audit/glc_full/` 的先例）。\n\n"
        "卡片本身已在 `datasets/` 原位置修好；这里保留错误版 / 正确版对照，用于追溯与防回归。\n\n"
        "| 案例 | 卡片 | 严重度 | 失效模式 | 改动处 |\n|---|---|---|---|---|\n"
        + rows + "\n\n"
        "## 与 11-26 批次的关系\n\n"
        "- `kw/concept/n4-sym-theory` 是**第二次修改**（11-26 曾把 source 从 `B p.6` 改为 `B p.7–11（…p.11）`；\n"
        "  本批按页脚修正为 p.10）。按 WORKFLOW §9 在此追加，不改 11-26 的历史 fix_log。\n"
        "- `sy38/concept/tamagawa-number` 首轮判 pass（`notes` 里已存疑但未定级），本轮独立复核改判 minor，\n"
        "  属**复审新增**，不是首轮修卡遗漏。\n"
        "- 其余 11 张卡 11-26 均未改过。\n",
        encoding="utf-8", newline="\n")
    print(f"wrote {len(index)} cases")


if __name__ == "__main__":
    build()
