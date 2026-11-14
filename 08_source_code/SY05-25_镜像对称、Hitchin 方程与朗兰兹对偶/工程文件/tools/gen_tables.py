# -*- coding: utf-8 -*-
"""从 notes_data.py + nLab 索引生成：

  源码/gen/notes_macros.tex        译注正文与来源的宏定义（供 \\zhnt 使用）
  源码/sections/appendix_notes.tex 附录 B 译注汇编
  源码/sections/appendix_glossary.tex 附录 A 术语与记号对照表
  工程文件/译注清单.tsv            人读的清单（审校用）

不手改生成物；要改先改 notes_data.py / 本文件的 GLOSSARY、SYMBOLS。
"""
import io
import os
import re
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))            # 工程文件\tools
PKG = os.path.dirname(os.path.dirname(HERE))                 # SY05-25
SRC = os.path.join(PKG, "源码")
WORK = r"C:\Users\admin\Desktop\数译发布\_pilot_0802\work\nlab_index.tsv"
VISIT = "2026-11-15"

sys.path.insert(0, HERE)
from notes_data import NOTES  # noqa: E402

# ---------------------------------------------------------------- nLab 索引
nlab = {}
if os.path.exists(WORK):
    for line in io.open(WORK, encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) >= 3 and parts[0] != "slug":
            nlab[parts[0]] = parts[2].strip()


def slug_title(slug):
    return urllib.parse.unquote(slug.replace("+", " "))


def slug_url(slug):
    # URL 里的 % 在 TeX 读入时会被当作注释符，故转义成 \%（\url 内仍显示为 %）
    return "https://ncatlab.org/nlab/show/" + slug.replace("%", r"\%")


def src_inline(n):
    """脚注里的来源串。"""
    if n["kind"] == "I":
        ref = n["ref"]
        return "[译者按（%s）]" % ref if ref and ref != "—" else "[译者按（无外部依据）]"
    parts = ["来源：%s" % n["kind"]]
    for s in n["nlab"]:
        d = nlab.get(s, "")
        if d:
            parts.append("nLab 词条「%s」（Last revised %s；%s 访问）" % (slug_title(s), d, VISIT))
        else:
            parts.append("nLab 词条「%s」（%s 访问）" % (slug_title(s), VISIT))
    if n["ref"] and n["ref"] != "—":
        parts.append(n["ref"])
    return "[%s]" % "；".join(parts)


def src_appendix(n):
    """附录里的来源串（带完整 URL）。"""
    if n["kind"] == "I":
        ref = n["ref"]
        return "译者按（%s）" % ref if ref and ref != "—" else "译者按（无外部依据）"
    parts = ["%s" % n["kind"]]
    for s in n["nlab"]:
        d = nlab.get(s, "")
        d = "，Last revised %s" % d if d else ""
        parts.append("nLab 词条「%s」（%s 访问%s）" % (slug_title(s), VISIT, d) +
                     "，\\url{%s}" % slug_url(s))
    if n["ref"] and n["ref"] != "—":
        parts.append(n["ref"])
    return "；".join(parts)


def key(n):
    return (n["sec"], int(n["id"].split(".")[1]))


NOTES.sort(key=key)
ids = [n["id"] for n in NOTES]
assert len(ids) == len(set(ids)), "译注编号重复"

# ---------------------------------------------------------------- 宏
out = [r"% 由 工程文件\tools\gen_tables.py 生成，勿手改。", r"% 译注数据：工程文件\tools\notes_data.py", ""]
for n in NOTES:
    i = n["id"]
    out.append(r"\expandafter\def\csname zhnlab@%s\endcsname{%s}" % (i, i))
    out.append(r"\expandafter\def\csname zhnbody@%s\endcsname{%s}" % (i, n["text"]))
    out.append(r"\expandafter\def\csname zhnsrc@%s\endcsname{%s}" % (i, src_inline(n)))
    out.append("")
io.open(os.path.join(SRC, "gen", "notes_macros.tex"), "w", encoding="utf-8", newline="\n").write("\n".join(out))

# ---------------------------------------------------------------- 附录 B
secnames = {1: "A-模型与 B-模型", 2: "镜像对称与 Hitchin 方程", 3: "Hitchin 纤维化",
            4: "分歧", 5: "野分歧", 6: "四维规范场论与叠"}
ab = [r"% 由 工程文件\tools\gen_tables.py 生成，勿手改。", r"\section{译注汇编}", "",
      r"以下按节次汇总全书译注。每条给出注文与完整来源；源级别的含义见「译者凡例」："
      r"A 为原文自身或经典原始文献，B 为 nLab 等百科与综述（社区来源，均与 A 级交叉核对过），"
      r"I 为译者按（仅由原文可推得，无外部依据）。", ""]
for sec in sorted(secnames):
    ab.append(r"\subsection*{第 %d 节　%s}" % (sec, secnames[sec]))
    for n in [m for m in NOTES if m["sec"] == sec]:
        ab.append(r"\appnote{译注 %s}{%s}{%s}" % (n["id"], n["text"], src_appendix(n)))
    ab.append("")
io.open(os.path.join(SRC, "sections", "appendix_notes.tex"), "w", encoding="utf-8", newline="\n").write("\n".join(ab))

# ---------------------------------------------------------------- 附录 A
GLOSSARY = [
    ("A-模型 / B-模型", "A-model / B-model", "二维拓扑场论的两族：前者依赖辛结构（计数伪全纯曲线），后者依赖复结构（复结构变形的积分）。"),
    ("镜像对称", "mirror symmetry", "一对流形上 A-模型与 B-模型之间的等价；不是经典几何的等同。"),
    ("拓扑扭转", "topological twist", "把超对称理论的 Lorentz 群换成与 R-对称的对角子群，使某个超荷成为标量，从而得到拓扑场论。"),
    ("复辛流形", "complex symplectic manifold", "带全纯非退化闭 2-形式的复流形；典范线丛自动平凡。"),
    ("超凯勒流形", "hyper-Kähler manifold", "带三个满足四元数关系的复结构、且三个 Kähler 形式均闭的流形。"),
    ("平坦丛", "flat bundle", "带可积联络的丛；等价于基本群的表示（模共轭）。"),
    ("Higgs 丛 / Higgs 场", "Higgs bundle / Higgs field", "全纯丛 $E$ 连同 $\\phi\\in H^{0}(C,K\\otimes\\ad(E))$；$\\phi$ 称 Higgs 场。"),
    ("Hitchin 方程", "Hitchin's equations", "$F-\\phi\\wedge\\phi=0$、$D\\phi=D\\star\\phi=0$；解模空间 $\\MH$ 超凯勒。"),
    ("Hitchin 纤维化", "Hitchin fibration", "$\\MH\\to B$，$(E,\\phi)\\mapsto\\phi$ 的特征多项式；纤维是阿贝尔簇。"),
    ("谱曲线", "spectral curve", "特征方程 $\\det(\\lambda-\\phi)=0$ 在 $K$ 的全纯线丛中所定义的曲线，用于把 Hitchin 纤维实现为 Prym 簇。"),
    ("可积系统", "integrable system", "此处指复意义下的 Liouville 可积：$\\MH\\to B$ 的纤维是环面、$B$ 是作用量变量空间。"),
    ("特殊拉格朗日子流形", "special Lagrangian submanifold", "$\\omega|_L=0$ 且 $\\operatorname{Im}(e^{i\\vartheta}\\Omega)|_L=0$ 的实子流形；在 Kähler 流形中面积最小。"),
    ("T-对偶", "T-duality", "环面纤维化上的对偶：把每个纤维换成对偶环面，底不变。"),
    ("SYZ 猜想", "SYZ conjecture", "镜像对称 = 同一底上互为对偶的特殊拉格朗日环面纤维化。"),
    ("广义复几何", "generalized complex geometry", "在 $TM\\oplus T^{*}M$ 上定义复结构，把复结构与辛结构放在同一个 $S^{2}$ 族中插值。"),
    ("D-模", "D-module", "微分算子层 $\\mathcal{D}$ 上的（准）凝聚模；是带平坦联络的丛的无穷小版本。"),
    ("Hecke 算子", "Hecke operator", "在一点处对丛作基本修改所得的对应，作用在 D-模上。"),
    ("Hecke 特征层", "Hecke eigensheaf", "在 Hecke 算子下按张量倍（各不可约表示）作用的 D-模。"),
    ("膜", "brane", "拓扑场论中的边界条件；A-膜依赖辛结构，B-膜依赖复结构。"),
    ("稳定 / 半稳定", "stable / semistable", "按斜率（$\\deg/\\operatorname{rk}$）定义的丛的稳定性；稳定 $\\Leftrightarrow$ 存在 Hitchin 解。"),
    ("分歧", "ramification", "平坦丛在穿刺点处有非平凡单值性的情形。"),
    ("驯顺分歧", "tame ramification", "单极点（留数可能非半单）的情形。"),
    ("野分歧", "wild ramification", "极点阶数大于 1 的情形；需用扩张单值性刻画。"),
    ("穿刺点", "puncture", "从 $C$ 中挖去的点 $p$；$C'=C\\setminus p$ 上允许有单值性。"),
    ("单值性", "monodromy", "绕闭链平行移动所得的变换；对平坦丛即基本群表示。"),
    ("扩张单值性", "extended monodromy", "普通单值性连同 Stokes 矩阵，是非正则奇点的完整拓扑数据。"),
    ("Stokes 矩阵", "Stokes matrix", "跨过 Stokes 射线时渐近展开所乘的常数矩阵。"),
    ("等单值形变", "isomonodromic deformation", "保持（扩张）单值数据不变、只改变高阶极点系数的形变。"),
    ("辫群", "braid group", "$\\mathfrak{t}_{\\C}^{\\mathrm{reg}}$（或其 Weyl 商）的基本群；控制 $T_{n}$ 的绕行单值性。"),
    ("映射类群", "mapping class group", "$C$ 的定向保持微分同胚模同伦；与辫群一起作用在野分歧的模空间上。"),
    ("叠", "stack", "局部可描述为商的空间；承载不稳定对象，使 Hecke 算子可作用。"),
    ("模叠", "moduli stack", "参数化对象的叠（如 $\\Bun_{G}(C)$），与粗模空间相对。"),
    ("辛商 / 超凯勒商", "symplectic quotient / hyper-Kähler quotient", "取矩映射零点再模去群作用；后者同时取三个矩映射。"),
    ("矩映射", "moment map", "Hamilton 群作用的生成元；其平方项出现在 $\\sigma$ 模型作用量中。"),
    ("Bogomolny 方程", "Bogomolny equations", "三维规范场论中的单极子方程 $F=\\star d_{A}\\phi$。"),
    ("Wilson / 't Hooft 线算子", "Wilson / 't Hooft line operators", "沿一条曲线的电 / 磁探针；在对偶下互换。"),
    ("Montonen–Olive 对偶", "Montonen–Olive duality", "$\\mathcal{N}=4$ 理论的 S-对偶：$g\\leftrightarrow1/g$、$G\\leftrightarrow{}^{L}G$。"),
    ("Langlands 对偶群", "Langlands dual group", "根数据取对偶所得的群 ${}^{L}G$；环面情形即对偶环面。"),
    (r"$\sigma$ 模型", "sigma model", "从世界面 $\\Sigma$ 到目标 $X$ 的映射的量子场论。"),
]

SYMBOLS = [
    ("$C$", "紧致无边界定向二维流形（黎曼面），亏格 $g\\ge2$"),
    ("$\\YC(G,C)$", "平坦 $G_{\\C}$-丛模空间（表示簇）"),
    ("$\\MH(G,C)$", "Hitchin 方程解的模空间，超凯勒"),
    ("$B$", "Hitchin 底，$\\bigoplus_{i}H^{0}(C,K^{d_{i}})$"),
    ("$\\Omega$", "复辛形式；$\\Omega_{I}=\\omega_{J}+i\\omega_{K}$"),
    ("$\\omega=\\operatorname{Im}\\Omega$", "A-模型所用的实辛形式"),
    ("$I,J,K$", "超凯勒三复结构，$IJ=K$"),
    ("$\\star$", "复结构决定的 Hodge 星算子"),
    ("$\\mathcal{A}=A+i\\phi$", "复联络（原文排作粗体 $\\bm{A}$ 的地方）"),
    ("$\\mathfrak{t},\\ \\mathfrak{t}_{\\C}^{\\mathrm{reg}}$", "极大环面的李代数 / 正则元开集"),
    ("$\\alpha,\\beta,\\gamma$", "Simpson 参数（取值于 $\\mathfrak{t}$），刻画穿刺点附近的奇性"),
    ("$U=\\exp(-2\\pi(\\alpha-i\\gamma))$", "绕穿刺点的 holonomy（符号约定见译注 4.5）"),
    ("$\\eta$", "量子参数（$\\theta$-角的伙伴），A-模型侧的复化 Kähler 参数"),
    ("$T_{1},\\dots,T_{n}$", "野分歧极点系数，$T_{n}\\in\\mathfrak{t}_{\\C}^{\\mathrm{reg}}\\otimes K_{p}^{n-1}$"),
    ("$B(G)$", "$G$ 的辫群"),
    ("$\\Bun_{G}(C)$", "所有 $G_{\\C}$-丛的模叠"),
    ("$M(G,C)$ / $M_{\\mathrm{st}}(G,C)$", "半稳定 / 严格稳定丛的模空间"),
    ("${}^{L}G,\\ {}^{L}\\mathcal{C},\\ {}^{L}T_{1}$", "对偶群及对偶侧的相应对象"),
]

ag = [r"% 由 工程文件\tools\gen_tables.py 生成，勿手改。", r"\section{术语与记号对照表}", "",
      r"下表给出正文中反复出现的术语。中文译名在全书统一；英文术语在正文首次出现时括注，其后从略。", "",
      r"\subsection*{表 A1　术语}", r"\begin{longtable}{p{0.22\textwidth}p{0.27\textwidth}p{0.41\textwidth}}",
      r"\toprule 中文 & 英文 & 说明 \\ \midrule \endfirsthead",
      r"\toprule 中文 & 英文 & 说明 \\ \midrule \endhead",
      r"\bottomrule \endfoot"]
for zh, en, note in GLOSSARY:
    ag.append(r"%s & %s & %s \\" % (zh, en, note))
ag += [r"\end{longtable}", "", r"\subsection*{表 A2　记号}", "",
       r"\begin{longtable}{p{0.34\textwidth}p{0.60\textwidth}}",
       r"\toprule 记号 & 含义 \\ \midrule \endfirsthead",
       r"\toprule 记号 & 含义 \\ \midrule \endhead",
       r"\bottomrule \endfoot"]
for k, v in SYMBOLS:
    ag.append(r"%s & %s \\" % (k, v))
ag += [r"\end{longtable}", ""]
io.open(os.path.join(SRC, "sections", "appendix_glossary.tex"), "w", encoding="utf-8", newline="\n").write("\n".join(ag))

# ---------------------------------------------------------------- TSV（审校用）
tsv = [r"id	sec	kind	nlab	ref	text"]
for n in NOTES:
    tsv.append("\t".join([n["id"], str(n["sec"]), n["kind"], ";".join(n["nlab"]),
                          n["ref"], n["text"]]))
io.open(os.path.join(PKG, "工程文件", "译注清单.tsv"), "w", encoding="utf-8", newline="\n").write("\n".join(tsv) + "\n")

# ---------------------------------------------------------------- 报告
from collections import Counter
c = Counter(n["sec"] for n in NOTES)
print("译注总数:", len(NOTES), "按节:", dict(sorted(c.items())))
missing = sorted({s for n in NOTES for s in n["nlab"] if s not in nlab})
print("nLab 索引缺失:", missing if missing else "无")
nodate = sorted({s for n in NOTES for s in n["nlab"] if not nlab.get(s)})
print("无 Last revised 日期（脚注省略日期）:", nodate if nodate else "无")
print("生成:", os.path.join(SRC, "gen", "notes_macros.tex"))
print("生成:", os.path.join(SRC, "sections", "appendix_notes.tex"))
print("生成:", os.path.join(SRC, "sections", "appendix_glossary.tex"))
print("生成:", os.path.join(PKG, "工程文件", "译注清单.tsv"))
