# -*- coding: utf-8 -*-
"""生成 datasets/sy0530 的资料卡（概念卡 + 书目卡）。一次性脚本，留档可重跑。"""
import json, os, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARD_DIR = os.path.join(ROOT, "cards", "concepts")
os.makedirs(CARD_DIR, exist_ok=True)

BOOK = "《模空间的几何与量子化》（Geometry and Quantization of Moduli Spaces）中译本，SY05-30"
SRC = "08_source_code/SY05-30_模空间的几何与量子化（Álvarez-Cónsul、Andersen、Mundet 编）/源码/chapters/"
CHECKED = "2026-11-24"
CHECKS = ["逐句对照底本 PDF 页面图像录入", "公式与编号回原书核对", "术语按本卷 work/术语表.tsv 统一"]

def src(section, pages, pdf_pages, anchor, note=None):
    d = {"book": BOOK, "section": section, "pages": pages, "pdf_pages": pdf_pages, "anchor": SRC + anchor}
    if note:
        d["page_note"] = note
    return d

TERMS = {
    "real-riemann-surface": [{"en": "Real Riemann surface", "zh": "Real 黎曼面"},
                             {"en": "real structure", "zh": "实结构"},
                             {"en": "antiholomorphic involution", "zh": "反全纯对合"},
                             {"en": "real point", "zh": "实点"}],
    "klein-surface-dianalytic": [{"en": "Klein surface", "zh": "克莱因曲面"},
                                 {"en": "dianalytic", "zh": "双解析"},
                                 {"en": "folding map", "zh": "折叠映射"}],
    "analytic-double": [{"en": "analytic double", "zh": "解析 double"},
                        {"en": "Alling-Greenleaf", "zh": "Alling-Greenleaf"}],
    "real-curve-topological-type": [{"en": "Harnack inequality", "zh": "Harnack 不等式"},
                                    {"en": "dividing curve", "zh": "分离曲线"},
                                    {"en": "M-curve", "zh": "M-曲线"},
                                    {"en": "topological type", "zh": "拓扑型"}],
    "real-fundamental-group": [{"en": "fundamental group of a real curve", "zh": "实曲线基本群"},
                               {"en": "real covering", "zh": "实覆盖"},
                               {"en": "augmentation", "zh": "增广"}],
    "semidirect-splitting": [{"en": "semidirect product", "zh": "半直积"},
                             {"en": "splitting", "zh": "分裂"}],
    "gamma-model": [{"en": "Gamma model", "zh": "Γ 模型"},
                    {"en": "homotopy class of paths", "zh": "道路同伦类"}],
    "galois-real-covers": [{"en": "Galois theory of real covers", "zh": "实覆盖的 Galois 理论"},
                           {"en": "fibre functor", "zh": "纤维函子"}],
    "unitary-representation-variety": [{"en": "unitary representation variety", "zh": "酉表示簇"},
                                       {"en": "linear real structure", "zh": "线性实结构"},
                                       {"en": "real structure kappa", "zh": "实结构 κ"}],
}

cards = []

def card(slug, **kw):
    c = {"id": "sy0530/concept/" + slug, "type": "concept", "track": "第2章"}
    c.update(kw)
    c.setdefault("terms", TERMS.get(slug, []))
    c.setdefault("rights", "rewritten")
    c.setdefault("status", "reviewed")
    c["verification"] = {"status": "source-verified", "checked_on": CHECKED, "checks": CHECKS}
    cards.append(c)

card("real-riemann-surface",
     title="Real 黎曼面与实结构",
     aliases=["Real Riemann surface", "real structure on a Riemann surface", "反全纯对合"],
     summary="紧黎曼面连同一个反全纯对合 τ 叫 Real 黎曼面；τ 的不动点集是实点集，商是带边或不可定向曲面。",
     question="为什么要求 τ 是反全纯对合，而不是普通的自同构？",
     definition={"text": "紧黎曼面 $\\Sigma$ 上的\\emph{实结构}是一个反全纯对合 $\\tau:\\Sigma\\to\\Sigma$，满足 $\\tau^2=\\Id$ 且 $\\tau\\neq\\Id$；此时 $T_x\\tau$ 是 $\\C$-反线性的。偶对 $(\\Sigma,\\tau)$ 称为 Real 黎曼面。两个 Real 黎曼面之间的同态是满足 $f\\circ\\tau=\\tau'\\circ f$ 的全纯映射。",
                 "notation": "$\\Sigma^{\\tau}:=\\Fix(\\tau)$ 是实点集；$p:\\Sigma\\to\\Sigma/\\tau$ 是商映射。Real 大写是 Atiyah 的专名约定。"},
     key_points=["$\\Sigma^{\\tau}$ 是有限个圆周之并（命题 2.1.3），这是反全纯（而非全纯）对合的直接后果。",
                 "商 $\\Sigma/\\tau$ 是带边（有实点时）或不可定向（无实点时）的曲面，$p$ 在 $\\Sigma^{\\tau}$ 与 $\\partial(\\Sigma/\\tau)$ 上是同胚。",
                 "$\\CP^1$ 上只有两种实结构：$z\\mapsto\\bar z$（$\\Fix=\\RP^1$）与 $z\\mapsto-1/\\bar z$（无实点）。"],
     formulas=["\\tau^2=\\Id,\\quad T_x\\tau\\ \\text{为}\\ \\C\\text{-反线性}", "f\\circ\\tau=\\tau'\\circ f", "X_P(\\R)=\\Fix(\\sigma|_{X_P(\\C)})"],
     theorems=[{"name": "命题 2.1.2",
                "statement": "$p$ 限制在 $\\Sigma^{\\tau}$ 上是到 $\\partial(\\Sigma/\\tau)$ 的同胚；$(p_*\\calO_\\Sigma)^{\\tau}$ 的截面在边界上取实值，且它是连续函数层的子层。",
                "proof": {"status": "full", "steps": [{"no": 1, "text": "在实点处取局部坐标把 $\\tau$ 化为共轭，$p$ 局部即折叠映射。", "why": "折叠映射在实轴上是同胚。"},
                                                        {"no": 2, "text": "用折叠映射的像 $\\C^+$ 描述商，边界即实轴。", "why": "$\\C^+$ 的边界点正是 $\\C$ 中实轴上的点。"}], "gap_note": ""},
                "source": "§2.1.1，印刷页 70–71"}],
     pitfalls=["把反全纯对合误写成全纯对合：全纯对合的不动点集是离散点集，不是圆周。",
               "把 Real 译成「实」：Real 是 Atiyah 的专名，与「实（real）曲线」不是一回事。"],
     annotations=[{"type": "术语", "title": "Real 大写", "text": "底本定义 2.1.1 自注 Real 是大写专名；译文保留 Real，普通形容词仍作「实」。"}],
     related=["sy0530/concept/klein-surface-dianalytic", "sy0530/concept/real-curve-topological-type"],
     sources=[src("§2.1.1", [68, 70, 71], [79, 81, 82], "ch02a.tex:84-183")])

card("klein-surface-dianalytic",
     title="克莱因曲面与双解析结构",
     aliases=["Klein surface", "dianalytic structure", "双解析图册"],
     summary="克莱因曲面是带双解析图册的曲面：转移映射只在每个连通分支上解析或反解析；它是 Real 黎曼面的商，也是带边黎曼面的推广。",
     question="为什么克莱因曲面不能直接用全纯图册定义？",
     definition={"text": "克莱因曲面是一个曲面 $\\Sigma$（可带边、可不可定向）连同一族双解析图册 $\\{\\phi_i:U_i\\to V_i\\subset\\C^+\\}$，转移映射双解析。$\\Sigma$ 的开集上的函数若在每个连通分支上解析或反解析，称\\emph{双解析}。",
                 "notation": "$\\C^+=\\{\\Im z\\geq 0\\}$；折叠映射 $\\psi:\\C\\to\\C^+,\\ x+iy\\mapsto x+i|y|$；图的像落在 $\\C^+$ 里。"},
     key_points=["双解析函数的边界情形要用 Schwarz 反射原理延拓到 $\\C$ 上的开集再定义。",
                 "紧连通拓扑曲面（可非可定向、可带边）总有双解析图册（定理 2.1.13，Alling–Greenleaf）；可定向时还可取解析图册。",
                 "克莱因曲面范畴与 Real 黎曼面范畴等价（定理 2.1.15），等价由解析 double 给出。"],
     formulas=["\\psi:\\C\\to\\C^+,\\quad x+iy\\mapsto x+i|y|", "\\psi\\circ F=\\phi'\\circ f"],
     theorems=[{"name": "定理 2.1.11（Schwarz 反射原理）",
                "statement": "设 $A\\subset\\C^+$ 是开集，$f:A\\to\\C$ 连续、在内部解析，且 $f(A\\cap\\R)\\subset\\R$；则 $f$ 唯一地延拓为 $A\\cup\\bar A$ 上的解析函数 $F$，满足 $F(\\bar z)=\\overline{F(z)}$。",
                "proof": {"status": "sketched", "steps": [{"no": 1, "text": "在 $A$ 内取 $F=f$。", "why": "已给。"},
                                                         {"no": 2, "text": "在 $\\bar A$ 上用 $F(z):=\\overline{f(\\bar z)}$ 定义。", "why": "边界实值条件保证两侧在实轴上接得上。"}], "gap_note": "原书只给陈述与用法，未展开证明。"},
                "source": "§2.1.3，印刷页 76"},
               {"name": "定理 2.1.13（Alling–Greenleaf）",
                "statement": "每个紧连通拓扑曲面（可带边、可非可定向）都容许双解析图册；若曲面可定向，还可取解析图册。",
                "proof": {"status": "cited", "steps": [], "gap_note": "原书引 [1]，未给证明。"},
                "source": "§2.1.3，印刷页 77"}],
     pitfalls=["把双解析当成「既解析又反解析」：定义是「每个连通分支上任选其一」。",
               "以为带边黎曼面与克莱因曲面是同一范畴：前者要求解析图册，只存在于可定向曲面。"],
     annotations=[{"type": "背景直觉", "title": "为什么是 C⁺", "text": "折叠映射把上半平面与下半平面粘成 C⁺，反解析的那一半被「折」过去；克莱因曲面的图册就活在这个折叠后的模型里。"}],
     related=["sy0530/concept/real-riemann-surface", "sy0530/concept/analytic-double"],
     sources=[src("§2.1.3", [75, 76, 77], [86, 87, 88], "ch02b.tex:182-255")])

card("analytic-double",
     title="解析 double 与范畴等价",
     aliases=["analytic double", "Alling–Greenleaf double", "解析加倍"],
     summary="每个克莱因曲面都有唯一的解析 double：一个 Real 黎曼面，其商就是原曲面；这给出克莱因曲面与 Real 黎曼面的范畴等价。",
     question="拓扑上「加倍」与解析上「double」差在哪里？",
     definition={"text": "克莱因曲面 $\\Sigma$ 的解析 double 是 Real 黎曼面 $(\\tilde\\Sigma,\\tau)$ 连同映射 $p:\\tilde\\Sigma\\to\\Sigma$，满足 $p\\circ\\tau=p$ 且诱导同胚 $\\bar p:\\tilde\\Sigma/\\tau\\to\\Sigma$。",
                 "notation": "$\\tilde\\Sigma$ 无边；$\\tau$ 是反全纯对合；$p$ 在 $\\Sigma$ 无边时就是 $\\Sigma\\sqcup\\bar\\Sigma\\to\\Sigma$。"},
     key_points=["构造：把每张图 $V_i\\subset\\C^+$ 换成 $W_i=V_i\\cup\\bar V_i$，按转移映射解析/反解析两种粘法拼起来，再除以 $\\tau$。",
                 "double 在同构意义下唯一：另一个 double 与它只差一个与 $\\tau$ 交换的解析同构。",
                 "由此克莱因曲面范畴与 Real 黎曼面范畴等价；之后可直接把连通 $(\\Sigma,\\tau)$ 叫作克莱因曲面（原书 Remark 2.1.16）。"],
     formulas=["\\bar p:\\tilde\\Sigma/\\tau\\ \\xrightarrow{\\ \\simeq\\ }\\ \\Sigma", "f\\circ\\tau'=\\tau\\circ f"],
     theorems=[{"name": "定理 2.1.15（Alling–Greenleaf）",
                "statement": "克莱因曲面 $\\Sigma$ 有解析 double $(\\tilde\\Sigma,\\tau,p)$，且 $(-)^\\sim$ 给出克莱因曲面范畴与 Real 黎曼面范畴之间的范畴等价。",
                "proof": {"status": "sketched", "steps": [{"no": 1, "text": "局部：$V\\subset\\C^+$ 的 double 是 $V\\cup\\bar V$。", "why": "折叠映射的纤维恰好是 $\\{z,\\bar z\\}$。"},
                                                         {"no": 2, "text": "整体：把各 $W_i$ 按转移映射（双解析者取其解析一侧、反解析者取反解析一侧）粘成 $\\Omega$，再令 $\\tilde\\Sigma=\\Omega/\\sim$。", "why": "粘法唯一由双解析性决定。"},
                                                         {"no": 3, "text": "$\\tau$ 局部取共轭，$p(a+\\sqrt{-1}b)=a+\\sqrt{-1}|b|$。", "why": "$p$ 的纤维即 $\\tau$-轨道。"}], "gap_note": ""},
                "source": "§2.1.3，印刷页 78–79；译注见 Q005"}],
     pitfalls=["把 double 的对象记错：是 $\\tilde\\Sigma'\\to\\tilde\\Sigma$（$f\\circ\\tau'=\\tau\\circ f$），不是 $\\Sigma\\to\\tilde\\Sigma$（原书此处笔误，见 Q005）。"],
     annotations=[{"type": "易错预警", "title": "原书笔误", "text": "定理 2.1.15 证明里 $f$ 的定义域与上下文不合，译文按本意写出并加译注（Q005）。"}],
     related=["sy0530/concept/klein-surface-dianalytic", "sy0530/concept/real-riemann-surface"],
     sources=[src("§2.1.3", [78, 79], [89, 90], "ch02c.tex:1-54")])

card("real-curve-topological-type",
     title="实曲线的拓扑型与 (g,k,a) 不变量",
     aliases=["topological type of a real curve", "Weichold theorem", "Harnack inequality", "分离/非分离"],
     summary="实曲线的拓扑型由亏格 g、实点圆周数 k、分离性 a 完全决定；可行三元组由 Harnack 界与奇偶条件给出。",
     question="为什么 k 与 g 的奇偶性要被 a 限制？",
     definition={"text": "设 $(\\Sigma,\\tau)$ 是亏格 $g$ 的连通 Real 黎曼面，$k$ 是 $\\Sigma^{\\tau}$ 的连通分支数，$a=0$ 若 $\\Sigma\\setminus\\Sigma^{\\tau}$ 不连通（分离），$a=1$ 若连通（非分离）。三元组 $(g,k,a)$ 称为拓扑型。",
                 "notation": "$k=0$ 时必有 $a=1$；$k=g+1$ 且 $a=0$ 的曲线称 M-曲线。"},
     key_points=["Harnack 不等式：$k\\leq g+1$（定理 2.1.5）。",
                 "$\\chi(\\Sigma/\\tau)=\\frac12\\chi(\\Sigma)=1-g$（引理 2.1.6）。",
                 "可行三元组：$a=0$ 时 $1\\leq k\\leq g+1$ 且 $k\\equiv g+1\\pmod 2$；$a=1$ 时 $0\\leq k\\leq g$（定理 2.1.8）。",
                 "每个可行三元组都由某个实曲线实现；$\\RP^1$ 上的实结构给出 $k=g+1$ 的情形。"],
     formulas=["k\\leq g+1", "\\chi(\\Sigma/\\tau)=\\tfrac12\\chi(\\Sigma)=1-g", "a=0:\\ 1\\leq k\\leq g+1,\\ k\\equiv g+1\\ (\\mathrm{mod}\\ 2)"],
     theorems=[{"name": "定理 2.1.5（Harnack 不等式）",
                "statement": "亏格 $g$ 的连通 Real 黎曼面上，$k\\leq g+1$；等号时 $\\Sigma/\\tau$ 同胚于球面挖去 $g+1$ 个开圆盘。",
                "proof": {"status": "sketched", "steps": [{"no": 1, "text": "对 $\\Sigma/\\tau$ 作三角剖分，把三角形按边界情形分三类拉回 $\\Sigma$。", "why": "每一类对 $\\chi$ 的贡献可逐一算出。"},
                                                         {"no": 2, "text": "由 $\\chi(\\Sigma/\\tau)=1-g$ 与 $k$ 个边界分支反解不等式。", "why": "边界越多，$\\chi$ 越小，而 $\\chi$ 固定为 $1-g$。"}], "gap_note": "原书脚注说明 Harnack 只对平面曲线证明，一般情形属 Klein。"},
                "source": "§2.1.2，印刷页 73"},
               {"name": "定理 2.1.8（Weichold）",
                "statement": "对连通 Real 黎曼面 $(\\Sigma,\\tau)$、$(\\Sigma',\\tau')$，以下等价：(a) 存在与 $\\tau,\\tau'$ 交换的同胚；(b) $\\Sigma/\\tau\\cong\\Sigma'/\\tau'$；(c) $(g,k,a)=(g',k',a')$。且每个满足上述条件的三元组都被实现。",
                "proof": {"status": "sketched", "steps": [{"no": 1, "text": "先证 (b)$\\Leftrightarrow$(c)：由 $\\chi(\\Sigma/\\tau)$ 与边界数、可定向性读出 $(g,k,a)$。", "why": "曲面分类定理。"},
                                                         {"no": 2, "text": "再证 (a)$\\Leftrightarrow$(b)：用 double 的唯一性（定理 2.1.15）把同胚提升。", "why": "double 只依赖原曲面。"},
                                                         {"no": 3, "text": "实现：从 $(g,k,a)$ 出发拼出 double，再取商。", "why": "构造是显式的。"}], "gap_note": "原书给出证明主线；细节留给读者。"},
                "source": "§2.1.2，印刷页 74–75"}],
     pitfalls=["把 $a$ 当成「实点集是否连通」：$a$ 说的是补集 $\\Sigma\\setminus\\Sigma^{\\tau}$ 是否连通。",
               "以为任意 $k\\leq g+1$ 都能实现：分离情形还要奇偶条件 $k\\equiv g+1\\pmod 2$。"],
     annotations=[{"type": "背景直觉", "title": "为什么奇偶受限", "text": "分离时 $\\Sigma\\setminus\\Sigma^{\\tau}$ 分成两半，每半的边界都是同一族圆周，粘回去时亏格的分配迫使奇偶条件。"}],
     related=["sy0530/concept/real-riemann-surface", "sy0530/concept/analytic-double"],
     sources=[src("§2.1.2", [71, 72, 73, 74, 75], [82, 83, 84, 85, 86], "ch02b.tex:1-181")])

card("real-fundamental-group",
     title="实曲线的基本群 π^R_1",
     aliases=["fundamental group of a real curve", "pi^R_1", "实覆盖"],
     summary="π^R_1((X,σ);x) 是覆盖 σ 的全纯或反全纯自同构组成的群，它分类 (X,σ) 的实覆盖，并落在 1→π1→π^R_1→Z/2Z→1 中。",
     question="π^R_1 为什么必须用「覆盖 σ 的自同构」来定义，而不能像 π1 那样用环路？",
     definition={"text": "设 $(X,\\sigma)$ 是连通 Real 黎曼面，$x\\in X$，$p:(\\tilde X,\\tilde x)\\to(X,x)$ 是万有覆盖。令 $\\pi^R_1((X,\\sigma);x):=\\{f:\\tilde X\\to\\tilde X\\mid \\exists\\sigma_f\\in\\{\\Id_X,\\sigma\\},\\ p\\circ f=f\\circ\\sigma_f\\}^{\\mathrm{op}}$，群结构为 $(f\\cdot g):=g\\circ f$。",
                 "notation": "$\\sigma_f$ 是 $f$ 的「增广」；$\\alpha(f)=\\sigma_f$ 给出到 $\\{\\Id,\\sigma\\}^{\\mathrm{op}}\\cong\\Z/2\\Z$ 的满同态。"},
     key_points=["$\\pi^R_1$ 是 $\\Aut^{\\pm}(\\tilde X)^{\\mathrm{op}}$ 的子群（命题 2.2.8）。",
                 "$\\ker\\alpha=\\pi_1(X;x)$，于是有同伦正合列 $1\\to\\pi_1\\to\\pi^R_1\\to\\Z/2\\Z\\to1$（命题 2.2.12）。",
                 "克莱因曲面范畴一般没有连通万有覆盖，但 $\\pi^R_1$ 仍左作用于 $\\tilde X$（通过全纯或反全纯变换）。",
                 "实覆盖的 Galois 理论：$\\Cov^R_{(X,\\sigma)}\\simeq\\pi^R_1$-集（定理 2.2.21）。"],
     formulas=["\\pi^R_1=\\{f\\mid p\\circ f=f\\circ\\sigma_f\\}^{\\mathrm{op}}", "1\\to\\pi_1(X;x)\\to\\pi^R_1((X,\\sigma);x)\\xrightarrow{\\ \\alpha\\ }\\Z/2\\Z\\to1"],
     theorems=[{"name": "命题 2.2.8",
                "statement": "$\\pi^R_1((X,\\sigma);x)$ 是 $\\Aut^{\\pm}(\\tilde X)^{\\mathrm{op}}$ 的子群；$\\alpha:\\pi^R_1\\to\\{\\Id,\\sigma\\}^{\\mathrm{op}}\\cong\\Z/2\\Z$ 是满同态，$\\ker\\alpha=\\pi_1(X;x)$ 正规。",
                "proof": {"status": "full", "steps": [{"no": 1, "text": "对 $f,g$ 分别有 $\\sigma_f,\\sigma_g$；由 $p\\circ(f\\circ g)=f\\circ\\sigma_f\\circ g\\circ\\sigma_g$ 得 $\\sigma_{f\\circ g}=\\sigma_f\\sigma_g$。", "why": "复合保持子群。"},
                                                        {"no": 2, "text": "$\\sigma_f=\\Id$ 的 $f$ 恰好是覆盖 $X$ 的全纯自同构，即 $\\pi_1(X;x)$。", "why": "$\\Aut(\\tilde X/X)\\cong\\pi_1$。"}], "gap_note": ""},
                "source": "§2.2.2，印刷页 87"},
               {"name": "定理 2.2.21",
                "statement": "实覆盖范畴与离散左 $\\pi^R_1((X,\\sigma);x)$-集范畴等价，准逆为纤维函子 $\\Fib_x$ 与 $Q(F)=(\\tilde X\\times_{\\pi_1}F,\\ \\pi^R_1/\\pi_1)$。",
                "proof": {"status": "sketched", "steps": [{"no": 1, "text": "用定理 2.2.6 把实覆盖视为带 $\\tau$ 的 $\\pi_1$-集。", "why": "实覆盖的底是 $\\pi_1$-集。"},
                                                        {"no": 2, "text": "取 $h\\in\\pi^R_1$ 映到非平凡元，令 $\\Phi(y,v)=(y\\cdot h^{-1},h\\cdot v)$。", "why": "$\\Phi$ 保持 $\\pi_1$-轨道且平方为恒等（因 $h^2\\in\\pi_1$），于是给出 $\\tau$。"}], "gap_note": ""},
                "source": "§2.2.3，印刷页 98–100"}],
     pitfalls=["把 $\\pi^R_1$ 写成 $\\Aut(\\tilde X)$ 的子群：必须取反群，因为群结构是 $f\\cdot g=g\\circ f$。",
               "以为 $x$ 非实点时不能用半直积：仍可，但要用 $\\Gamma$ 模型（命题 2.2.17）。"],
     annotations=[{"type": "术语", "title": "增广", "text": "augmentation 指到 $\\Z/2\\Z$ 的满同态 $\\alpha$；实曲线基本群就是绝对 Galois 群 $\\Gal(\\C/\\R)$ 的增广。"}],
     related=["sy0530/concept/semidirect-splitting", "sy0530/concept/gamma-model", "sy0530/concept/galois-real-covers"],
     sources=[src("§2.2.2", [86, 87, 88], [96, 97, 98], "ch02e.tex:127-150")])

card("semidirect-splitting",
     title="半直积分解与正合列的分裂",
     aliases=["semidirect product", "splitting of the exact sequence", "sigma-tilde"],
     summary="当基点 x 是实点时，取定 σ 的提升 σ̃，π^R_1 分裂为 π1 ⋊_σ̃ Z/2Z；分裂与否等价于存在二阶反全纯提升。",
     question="为什么 σ̃ 一般不是二阶元，却仍能给出半直积？",
     definition={"text": "设 $x\\in\\Fix(\\sigma)$，$\\tilde\\sigma$ 是 $\\sigma$ 的提升（$\\tilde\\sigma(\\tilde x)=\\tilde x$，$p\\circ\\tilde\\sigma=\\sigma\\circ p$）。则 $\\tilde\\sigma^2=\\Id$，共轭 $f\\mapsto\\tilde\\sigma f\\tilde\\sigma^{-1}$ 给出 $\\pi_1$ 上的 $\\Z/2\\Z$-作用，$\\pi^R_1\\cong\\pi_1(X;x)\\rtimes_{\\tilde\\sigma}\\Z/2\\Z$。",
                 "notation": "$\\sigma$ 也记 $\\sigma_*$；$\\tilde\\sigma$-作用记 $\\Ad_{\\tilde\\sigma}$。"},
     key_points=["$\\tilde\\sigma^2=\\Id$ 只在 $x$ 是实点且取 $\\tilde x$ 为实点上的点时成立（引理 2.2.11）。",
                 "同伦正合列在 $x$ 实点时分裂，分裂的像由 $\\tilde\\sigma$ 给出（命题 2.2.13）。",
                 "分裂等价于正合列 (2.17) 分裂，也等价于 $x$ 非实点情形下存在 $x\\to\\sigma(x)$ 的阶 2 道路（习题 2.2.30）。",
                 "$\\Fix(\\sigma)=\\varnothing$ 时正合列必不分裂。"],
     formulas=["\\pi^R_1\\cong\\pi_1(X;x)\\rtimes_{\\tilde\\sigma}\\Z/2\\Z", "\\tilde\\sigma\\cdot f=\\tilde\\sigma f\\tilde\\sigma^{-1}", "(f,\\varepsilon)\\mapsto f\\varepsilon"],
     theorems=[{"name": "命题 2.2.13",
                "statement": "若 $x\\in\\Fix(\\sigma)$，则 $\\{\\Id,\\tilde\\sigma\\}^{\\mathrm{op}}\\cong\\Z/2\\Z$ 经共轭左作用于 $\\pi_1(X;x)$，且 $\\pi^R_1((X,\\sigma);x)\\cong\\pi_1(X;x)\\rtimes_{\\tilde\\sigma}\\Z/2\\Z$。",
                "proof": {"status": "full", "steps": [{"no": 1, "text": "每个 $f\\in\\pi^R_1$ 唯一写成 $f\\varepsilon$，其中 $f\\in\\pi_1$、$\\varepsilon\\in\\{1,\\tilde\\sigma\\}$。", "why": "由增广 $\\alpha$ 的核与像分解。"},
                                                        {"no": 2, "text": "验 $\\tilde\\sigma f\\tilde\\sigma^{-1}\\in\\pi_1$ 并算乘积规则。", "why": "$\\tilde\\sigma$ 的反全纯性使共轭落回全纯侧。"}], "gap_note": ""},
                "source": "§2.2.2，印刷页 89–90"},
               {"name": "推论 2.2.14",
                "statement": "用环路表示：$\\pi^R_1\\cong\\pi_1\\rtimes_\\sigma\\Z/2\\Z$，其中 $\\sigma_*\\gamma=\\sigma^{-1}\\circ\\gamma$。",
                "proof": {"status": "full", "steps": [{"no": 1, "text": "把 $\\sigma$ 作用翻译成环路的前复合。", "why": "由 $\\tilde\\sigma$ 覆盖 $\\sigma$ 的函子性。"}], "gap_note": ""},
                "source": "§2.2.2，印刷页 90"}],
     pitfalls=["以为 $\\tilde\\sigma$ 一定二阶：$x$ 非实点时 $\\tilde\\sigma^2\\neq\\Id$（引理 2.2.16），此时不能用半直积。",
               "把 $\\rtimes_{\\tilde\\sigma}$ 的作用方向写反：作用是左作用，$\\tilde\\sigma\\cdot f=\\tilde\\sigma f\\tilde\\sigma^{-1}$。"],
     annotations=[],
     related=["sy0530/concept/real-fundamental-group", "sy0530/concept/gamma-model"],
     sources=[src("§2.2.2", [89, 90], [99, 100], "ch02f.tex:42-176")])

card("gamma-model",
     title="非实点基点的 Γ 模型",
     aliases=["Gamma model", "classe d'homotopie des chemins", "x non réel"],
     summary="当 x 不是实点时，用「x 处环路 + x 到 σ(x) 的道路」的集合 Γ 配上 ⊠ 乘法，得到与 π^R_1 同构的群。",
     question="为什么要绕一条 x→σ(x) 的道路，而不能直接用 x 处的环路？",
     definition={"text": "设 $x\\notin\\Fix(\\sigma)$，$\\Gamma:=\\{\\text{$x$ 处环路的同伦类}\\}\\sqcup\\{\\text{$x\\to\\sigma(x)$ 道路的同伦类}\\}$。对 $\\gamma,\\gamma'\\in\\Gamma$ 定义 $\\gamma\\boxtimes\\gamma':=\\gamma*\\gamma'$（若 $\\gamma'(1)=x$）或 $(\\sigma\\circ\\gamma)*\\gamma'$（若 $\\gamma'(1)=\\sigma(x)$）。则 $(\\Gamma,\\boxtimes)$ 是群，且 $\\Phi:\\Gamma\\to\\pi^R_1$，$\\gamma\\mapsto f_\\gamma$，是群同构。",
                 "notation": "$\\beta(\\gamma)=\\Id$ 若 $\\gamma(1)=x$，$=\\sigma(x)$ 若 $\\gamma(1)=\\sigma(x)$；方块图与 (2.17) 交换。"},
     key_points=["$\\Gamma$ 的乘法先用 $\\sigma$ 把端点搬回 $x$，这正是「非实点」与「实点」的唯一区别。",
                 "每个 $\\eta_i$（穿过一对 puncture 的道路）在 $\\pi^R_1$ 中阶 2（例 2.2.20）。",
                 "例 2.2.19：$\\Fix(\\sigma)=\\varnothing$ 时 $\\pi^R_1\\cong\\pi_1^{\\mathrm{top}}(X/\\sigma;[x])$。"],
     formulas=["\\gamma\\boxtimes\\gamma'=(\\sigma\\circ\\gamma)*\\gamma'", "\\pi_1=\\langle a_1,a_2,a_3\\mid a_1a_2a_3=1\\rangle,\\quad \\pi^R_1=\\langle b_1,b_2,b_3\\mid b_i^2=1\\rangle"],
     theorems=[{"name": "命题 2.2.17",
                "statement": "$(\\Gamma,\\boxtimes)$ 是群，$\\Phi:\\Gamma\\to\\pi^R_1((X,\\sigma);x)$ 是群同构，且与两个正合列交换。",
                "proof": {"status": "full", "steps": [{"no": 1, "text": "验 $\\boxtimes$ 结合、有单位（常道路类）、有逆（反向道路）。", "why": "每种情形按端点分两类检查。"},
                                                        {"no": 2, "text": "对 $\\gamma\\in\\Gamma$ 取唯一自微分同胚 $f_\\gamma$ 使 $f_\\gamma(\\tilde x)=\\gamma\\curvearrowright\\tilde x$ 且覆盖 $\\Id$ 或 $\\sigma$。", "why": "覆盖的同伦提升唯一。"},
                                                        {"no": 3, "text": "验 $\\Phi$ 保乘法并与 $\\alpha,\\beta$ 交换。", "why": "直接由定义。"}], "gap_note": ""},
                "source": "§2.2.2，印刷页 92–94"}],
     pitfalls=["用 $\\gamma*\\gamma'$ 而忘了在第二个因子的起点是 $\\sigma(x)$ 时先复合 $\\sigma$。",
               "把 $\\Gamma$ 的乘法与 $\\pi_1$ 的乘法混同：$\\Gamma$ 的两个部分各自封闭，跨部分靠 $\\sigma$。"],
     annotations=[{"type": "例子", "title": "CP¹ 挖三点", "text": "例 2.2.20 把 $\\Gamma$ 模型算成 $\\langle b_1,b_2,b_3\\mid b_i^2=1\\rangle$，是本章唯一可以手算到底的例子。"}],
     related=["sy0530/concept/real-fundamental-group", "sy0530/concept/semidirect-splitting"],
     sources=[src("§2.2.2", [92, 93, 94, 95], [102, 103, 104, 105], "ch02g.tex:5-152")])

card("galois-real-covers",
     title="实覆盖的 Galois 理论",
     aliases=["Cov^R", "Galois theory of real covers", "pi^R_1-sets"],
     summary="实覆盖范畴与 π^R_1-集范畴等价：纤维函子 Fib_x 与「乘上万有覆盖再取商」互为逆。",
     question="为什么 τ 的构造不依赖 h 的选取？",
     definition={"text": "设 $\\Cov^R_{(X,\\sigma)}$ 是实覆盖 $(Y,\\tau)\\to(X,\\sigma)$ 的范畴。则 $\\Cov^R_{(X,\\sigma)}\\simeq\\pi^R_1((X,\\sigma);x)$-集，准逆为 $\\Fib_x(q)=q^{-1}(\\{x\\})$ 与 $Q(F)=(\\tilde X\\times_{\\pi_1(X;x)}F,\\ \\pi^R_1/\\pi_1(X;x))$。",
                 "notation": "实覆盖：$q\\circ\\tau=\\sigma\\circ q$，$q$ 拓扑覆盖；$\\pi^R_1/\\pi_1\\cong\\Z/2\\Z$ 给出 $Q(F)$ 上的 $\\tau$。"},
     key_points=["$\\pi^R_1$ 左作用于每个实覆盖的纤维（命题 2.2.9），这是函子性的来源。",
                 "$h\\in\\pi^R_1$ 映到非平凡元，$h^2\\in\\pi_1$，故 $\\Phi(y,v)=(y\\cdot h^{-1},h\\cdot v)$ 是良定义的对合。",
                 "实覆盖的连通分支与 $\\pi^R_1$ 的子群对应，正规子群对应 Galois 实覆盖。"],
     formulas=["\\Cov^R_{(X,\\sigma)}\\simeq\\pi^R_1((X,\\sigma);x)\\text{-}\\mathbf{Set}", "Q(F)=(\\tilde X\\times_{\\pi_1(X;x)}F,\\ \\pi^R_1/\\pi_1(X;x))"],
     theorems=[{"name": "定理 2.2.21",
                "statement": "上述两函子互为准逆，给出范畴等价。",
                "proof": {"status": "full", "steps": [{"no": 1, "text": "由定理 2.2.6 有 $\\Cov_X\\simeq\\pi_1$-集；实覆盖相当于带 $\\tau$ 的 $\\pi_1$-集。", "why": "把 $\\tau$ 视为额外的对合数据。"},
                                                        {"no": 2, "text": "取 $h$ 映到非平凡元，定义 $\\Phi(y,v)=(y\\cdot h^{-1},h\\cdot v)$。", "why": "它保持 $\\pi_1$-轨道、平方为恒等。"},
                                                        {"no": 3, "text": "验 $\\tau$ 不依赖 $h$ 的选取（换 $h$ 只差 $\\pi_1$ 中元素）。", "why": "两个选择的差在 $\\pi_1$ 中，被轨道等价吸收。"}], "gap_note": ""},
                "source": "§2.2.3，印刷页 98–100"}],
     pitfalls=["把 $Q(F)$ 的第二个因子写成 $\\pi_1$：必须是 $\\pi^R_1/\\pi_1\\cong\\Z/2\\Z$，否则 $\\tau$ 丢掉。",
               "忘了 $\\Fib_x$ 只对连通覆盖才是纤维的完整信息。"],
     annotations=[],
     related=["sy0530/concept/real-fundamental-group", "sy0530/concept/unitary-representation-variety"],
     sources=[src("§2.2.3", [98, 99, 100], [108, 109, 110], "ch02h.tex:7-65")])

card("unitary-representation-variety",
     title="酉表示簇与实结构 κ",
     aliases=["unitary representation variety", "GL^±", "U^±", "kappa"],
     summary="π^R_1 的酉表示簇打到 π1 的酉表示簇，像落在对合 κ（Galois 共轭与 σ̃-共轭的复合）的不动点集内，但一般不满。",
     question="为什么等价关系只许用 U(V) 而不许用 U^±(V)？",
     definition={"text": "线性表示是使方块图 (2.21) 交换的增广同态 $\\rho:\\pi^R_1\\to\\GL^{\\pm}(V)$；酉表示是 $\\rho:\\pi^R_1\\to\\U^{\\pm}(V,h)$。酉表示簇为 $\\Hom_{\\Z/2\\Z}(\\pi^R_1;\\U^{\\pm}(V,h))/\\U(V,h)$，其中 $u\\cdot\\rho=\\Ad_u\\circ\\rho$。",
                 "notation": "$\\GL^{\\pm}(V)=\\GL(V)\\rtimes_\\alpha\\Z/2\\Z$（$\\alpha$ 是线性实结构）；$\\U^{\\pm}(V,h)=\\U(V)\\rtimes_\\alpha\\Z/2\\Z$。"},
     key_points=["$\\GL^{\\pm}(V)$ 含 $\\GL(V)$ 为指数 2 子群，增广把反线性变换送到非平凡元。",
                 "若允许 $\\U^{\\pm}(V)$ 作等价，轨道空间不再有打到普通表示簇的自然映射，故只除 $\\U(V)$。",
                 "$\\kappa([\\rho])=[\\Ad_\\alpha\\circ\\rho\\circ\\Ad_{\\tilde\\sigma}^{-1}]$ 是对合；$\\rho=\\bar\\rho$ 的不动点保持实子空间 $V^\\alpha$。",
                 "映射 $\\Phi:\\mathcal R(\\sigma,\\alpha)\\to\\mathcal R$ 的像落在 $\\Fix(\\kappa)$ 中，但 $\\Im\\Phi\\neq\\Fix(\\kappa)$（定理 2.3.4 后的注）。"],
     formulas=["\\kappa([\\rho])=[\\Ad_\\alpha\\circ\\rho\\circ\\Ad_{\\tilde\\sigma}^{-1}]", "\\mathcal R(\\sigma,\\alpha)=\\Hom_{\\Z/2\\Z}(\\pi^R_1;\\U(V)\\rtimes_\\alpha\\Z/2\\Z)/\\U(V)"],
     theorems=[{"name": "定理 2.3.4",
                "statement": "$\\Phi:\\mathcal R(\\sigma,\\alpha)\\to\\mathcal R$，$[\\rho]\\mapsto[\\rho|_{\\pi_1}]$，把 $\\mathcal R(\\sigma,\\alpha)$ 送入 $\\Fix(\\kappa)$。",
                "proof": {"status": "full", "steps": [{"no": 1, "text": "记 $\\chi=\\rho|_{\\pi_1}$，直接计算 $\\Ad_\\alpha\\circ\\chi\\circ\\Ad_{\\tilde\\sigma}^{-1}(f)$。", "why": "展开共轭。"},
                                                        {"no": 2, "text": "得 $\\bigl(\\alpha\\rho(\\tilde\\sigma)^{-1}\\bigr)\\chi(f)\\bigl(\\alpha\\rho(\\tilde\\sigma)^{-1}\\bigr)^{-1}$。", "why": "中间项整理。"},
                                                        {"no": 3, "text": "$\\alpha$ 与 $\\rho(\\tilde\\sigma)$ 同在增广的非平凡纤维，故其商 $\\in\\U(V)$。", "why": "于是 $\\chi$ 与 $\\kappa(\\chi)$ 模 $\\U(V)$ 等价。"}], "gap_note": ""},
                "source": "§2.3.2，印刷页 106–107"}],
     pitfalls=["把 $\\GL^{\\pm}$ 的 $\\pm$ 当作行列式符号：这里指「线性/反线性」。",
               "以为 $\\Phi$ 是到 $\\Fix(\\kappa)$ 的满射：底本明确说一般不满（引 [16]）。"],
     annotations=[{"type": "易错预警", "title": "反群与 −1 指数", "text": "$\\Ad_{\\tilde\\sigma}^{-1}$ 里的逆不能省：$\\tilde\\sigma$ 一般不是二阶元，省掉会改变 $\\kappa$。"}],
     related=["sy0530/concept/semidirect-splitting", "sy0530/concept/galois-real-covers"],
     sources=[src("§2.3.1", [101, 103], [111, 113], "ch02i.tex:59-126"),
                src("§2.3.2", [106, 107], [116, 117], "ch02j.tex:1-113")])

# 书目卡
work = {
    "id": "sy0530/work", "type": "work", "track": "第2章", "title": "模空间的几何与量子化（SY05-30）",
    "aliases": ["Geometry and Quantization of Moduli Spaces", "CRM Barcelona 2016"],
    "summary": "2012 年 CRM Bellaterra 学期课程的四门讲义：dimer 可积系统、克莱因曲面基本群、TQFT 与配边猜想、Higgs 丛与局部系统。本卷译前言与第 2 章。",
    "question": "四章各自独立，为什么编在一起？",
    "definition": {"text": "Springer/Birkhäuser，Advanced Courses in Mathematics – CRM Barcelona，2016；编者 L. Álvarez-Cónsul、J. E. Andersen、I. Mundet i Riera；四章分别由 Fock–Marshakov、Schaffhauser、Teleman、Wentworth 撰写。",
                   "notation": "底本页码：印刷页 = PDF 页 − 10；第 2 章印刷页 67–108。"},
    "key_points": ["贯穿主线：黎曼面上局部系统模空间的四种语言（dimer / 实结构 / TQFT / Higgs）。",
                   "第 2 章（本卷全译）自含、无插图，是全书最适合做样板章的一章。",
                   "译稿：08_source_code/SY05-30_…/源码/；术语：工程文件/work/术语表.tsv。"],
    "formulas": [],
    "theorems": [],
    "pitfalls": ["把四章当成一条论证链：它们是四门独立课程，只有主题上的呼应。"],
    "annotations": [{"type": "背景直觉", "title": "为什么编在一起", "text": "编者前言的说法：局部系统的模空间在经典与量子两面反复出现，四门课各给一面。"}],
    "related": ["sy0530/concept/real-fundamental-group", "sy0530/concept/unitary-representation-variety"],
    "sources": [{"book": BOOK, "section": "前言、目录", "pages": [], "pdf_pages": [5, 8, 9, 10, 11],
                 "anchor": "08_source_code/SY05-30_模空间的几何与量子化（Álvarez-Cónsul、Andersen、Mundet 编）/源码/chapters/foreword.tex:1-66"}],
    "rights": "rewritten", "status": "reviewed",
    "verification": {"status": "source-verified", "checked_on": CHECKED, "checks": CHECKS},
}

os.makedirs(os.path.join(ROOT, "cards", "work"), exist_ok=True)
with io.open(os.path.join(ROOT, "cards", "work", "work.json"), "w", encoding="utf-8", newline="\n") as f:
    json.dump(work, f, ensure_ascii=False, indent=2)
    f.write("\n")

for c in cards:
    slug = c["id"].split("/")[-1]
    with io.open(os.path.join(CARD_DIR, slug + ".json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(c, f, ensure_ascii=False, indent=2)
        f.write("\n")

print("wrote", len(cards) + 1, "cards")
