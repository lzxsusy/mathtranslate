# -*- coding: utf-8 -*-
"""生成 工程文件/work/glossary.tsv：英文 / 中文 / 依据代号 / 首现页码 / 备注
依据代号：L=本库已冻结(TERMS.tsv 或 SY02-41/26 glossary)；A=权威文献通行译法；I=译者按上下文拟定（待裁定）
"""
import io, os, re, json

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
NPG = 56

pages = {}
for i in range(1, NPG + 1):
    p = os.path.join(SRC, "p%03d.txt" % i)
    if os.path.exists(p):
        pages[i] = io.open(p, encoding="utf-8", errors="replace").read()

def first(pat):
    rx = re.compile(pat, re.I)
    for i in range(1, NPG + 1):
        if i in pages and rx.search(pages[i]):
            return i
    return 0

# (英文, 中文, 依据, 检索正则, 备注)
T = [
 ("geometric Langlands", "几何 Langlands", "L", r"geometric Langlands", ""),
 ("automorphic form", "自守形式", "L", r"automorphic form", ""),
 ("automorphic representation", "自守表示", "L", r"automorphic representation", ""),
 ("function field", "函数域", "L", r"function field", ""),
 ("number field", "数域", "L", r"number field", ""),
 ("Langlands dual group", "Langlands 对偶群", "L", r"Langlands dual group", ""),
 ("Borel subgroup", "Borel 子群", "L", r"Borel subgroup", ""),
 ("maximal torus", "极大环面", "A", r"maximal torus", ""),
 ("reductive group", "约化群", "L", r"reductive group", ""),
 ("split", "分裂", "L", r"\bsplit\b", "指 split reductive group"),
 ("simply connected", "单连通", "L", r"simply connected", ""),
 ("unipotent radical", "单幂根", "A", r"unipotent radical", ""),
 ("parabolic", "抛物", "L", r"parabolic", "抛物子群"),
 ("Levi subgroup", "Levi 子群", "L", r"Levi", ""),
 ("cuspidal", "尖点", "L", r"cuspidal", "尖点形式 / 尖点部分"),
 ("tempered", "缓增", "A", r"tempered", ""),
 ("Eisenstein series", "Eisenstein 级数", "L", r"Eisenstein", ""),
 ("constant term", "常数项", "A", r"constant term", ""),
 ("Whittaker coefficient", "Whittaker 系数", "A", r"Whittaker coefficient", ""),
 ("Whittaker sheaf", "Whittaker 层", "A", r"Whittaker sheaf", ""),
 ("Poincaré series", "Poincaré 级数", "A", r"Poincar", ""),
 ("Hecke operator", "Hecke 算子", "L", r"Hecke operator", ""),
 ("Hecke correspondence", "Hecke 对应", "L", r"Hecke correspondence", ""),
 ("Hecke eigensheaf", "Hecke 特征层", "A", r"Hecke eigensheaf", ""),
 ("Hecke-lisse", "Hecke-lisse", "A", r"Hecke-lisse", "不译，作为术语保留"),
 ("geometric Satake equivalence", "几何 Satake 等价", "L", r"geometric Satake", ""),
 ("fusion product", "融合积", "A", r"fusion product|Fusion", ""),
 ("affine Grassmannian", "仿射 Grassmann 簇", "L", r"[Aa]ffine Grassmannian", ""),
 ("loop group", "圈群", "A", r"loop group", ""),
 ("positive loop group", "正圈群", "A", r"positive loop group", ""),
 ("local Hecke stack", "局部 Hecke 叠", "A", r"local Hecke stack", ""),
 ("oper", "oper", "L", r"\boper\b", "不译；复数 opers"),
 ("Kac–Moody localization", "Kac–Moody 局部化", "A", r"Kac.Moody [Ll]ocalization", ""),
 ("critical level", "临界水平", "A", r"critical level", ""),
 ("spherical vector", "球向量", "A", r"spherical vector", ""),
 ("ind-coherent sheaves", "归纳凝聚层", "A", r"ind-coherent|IndCoh", "IndCoh 保留记号"),
 ("coherent sheaf", "凝聚层", "L", r"coherent sheaf", ""),
 ("perfect complex", "完美复形", "L", r"perfect complex", ""),
 ("quasicoherent", "拟凝聚", "L", r"quasicoherent", "记号 Dqc 保留"),
 ("six-functor formalism", "六函子形式化", "A", r"six.functor formalism|six functor", ""),
 ("correspondence", "对应", "L", r"correspondence", ""),
 ("perverse sheaf", "反常层", "L", r"perverse", "严禁「错致层」"),
 ("constructible sheaf", "可构造层", "L", r"constructible", ""),
 ("lisse", "lisse", "A", r"\blisse\b", "与 locally constant 同义，保留英文"),
 ("local system", "局部系统", "L", r"local system", ""),
 ("flat connection", "平坦联络", "L", r"flat connection", ""),
 ("D-module", "D-模", "L", r"D-module|D-mod", ""),
 ("de Rham", "de Rham", "L", r"de Rham", "不译"),
 ("Betti", "Betti", "L", r"Betti", "不译"),
 ("étale", "étale", "L", r"\u00e9tale|etale", "不译"),
 ("pro-étale", "pro-étale", "L", r"pro-\u00e9tale|pro-etale", "不译"),
 ("affinoid", "affinoid", "L", r"affinoid", "不译"),
 ("perfectoid", "完满", "L", r"perfectoid", "完满空间/完满环；禁「完全胚」"),
 ("diamond", "菱形", "L", r"\bdiamond\b", "禁「钻石」"),
 ("prism", "棱镜", "L", r"\bprism", ""),
 ("condensed", "凝聚态", "L", r"condensed", ""),
 ("solid", "固体", "L", r"\bsolid\b", ""),
 ("isocrystal", "等晶体", "L", r"isocrystal", "禁「有理晶体」"),
 ("shtuka", "shtuka", "L", r"shtuka", "不译"),
 ("leg", "leg", "L", r"\bleg\b|\blegs\b", "不译"),
 ("nilpotent singular support", "幂零奇异支撑", "A", r"nilpotent singular support", ""),
 ("singular support", "奇异支撑", "A", r"singular support", ""),
 ("microlocal", "微局部", "A", r"microlocal", ""),
 ("microstalk", "微茎", "I", r"microstalk", ""),
 ("cotangent bundle", "余切丛", "L", r"cotangent bundle", ""),
 ("Hitchin fibration", "Hitchin 纤维化", "A", r"Hitchin", ""),
 ("Higgs bundle", "Higgs 丛", "A", r"Higgs", ""),
 ("moduli stack", "模叠", "A", r"moduli stack", ""),
 ("moduli space", "模空间", "L", r"moduli space", ""),
 ("Artin stack", "Artin 叠", "A", r"Artin stack", ""),
 ("quotient stack", "商叠", "A", r"quotient stack", ""),
 ("descent", "下降", "A", r"descent", ""),
 ("sheafification", "层化", "A", r"sheafification", ""),
 ("presentable", "可表现", "A", r"presentable", ""),
 ("stable (∞,1)-category", "稳定 (∞,1)-范畴", "A", r"stable", ""),
 ("symmetric monoidal", "对称幺半", "A", r"symmetric monoidal", ""),
 ("commutative algebra", "交换代数", "L", r"commutative algebra", ""),
 ("kernel", "核", "A", r"\bkernel", "核范畴 / 核函子"),
 ("adjoint", "伴随", "L", r"adjoint", ""),
 ("dualizable", "可对偶", "A", r"dualizab", ""),
 ("self-dual", "自对偶", "A", r"self-dual", ""),
 ("trace of Frobenius", "Frobenius 迹", "A", r"trace of Frobenius", ""),
 ("Frobenius structure", "Frobenius 结构", "A", r"Frobenius structure", ""),
 ("Weil descent datum", "Weil 下降数据", "A", r"Weil descent", ""),
 ("Weil group", "Weil 群", "A", r"Weil group", ""),
 ("compactly generated", "紧生成", "A", r"compactly generated", ""),
 ("compact object", "紧对象", "A", r"compact object", ""),
 ("derived algebraic geometry", "导出代数几何", "A", r"derived algebraic geometry", ""),
 ("formal completion", "形式完备化", "A", r"formal completion", ""),
 ("formal disc", "形式圆盘", "A", r"formal disc", ""),
 ("punctured formal disc", "去心形式圆盘", "A", r"punctured", ""),
 ("quasitorsor", "拟挠子", "A", r"quasitorsor", ""),
 ("torsor", "挠子", "A", r"\btorsor", ""),
 ("character variety", "特征簇", "A", r"character variety", ""),
 ("local complete intersection", "局部完全交", "A", r"local complete intersection", ""),
 ("Witt vectors", "Witt 向量", "A", r"Witt", ""),
 ("degeneration", "退化", "A", r"degeneration", ""),
 ("specialization map", "特殊化映射", "A", r"specialization map", ""),
 ("profinite", "投射有限", "A", r"profinite", ""),
 ("Cartier duality", "Cartier 对偶", "A", r"Cartier dual", ""),
 ("Fourier–Mukai", "Fourier–Mukai", "A", r"Fourier.Mukai", "不译"),
 ("abelian variety", "阿贝尔簇", "L", r"abelian variet", ""),
 ("Jacobian", "Jacobian", "A", r"Jacobian", "不译"),
 ("principally polarized", "主极化", "A", r"principally polarized", ""),
 ("universal vector extension", "通用向量扩张", "I", r"universal vector extension", ""),
 ("Tannakian", "Tannakian", "A", r"Tannakian", "不译"),
 ("coend", "余端", "A", r"coend", ""),
 ("anima", "anima", "A", r"anima", "不译"),
 ("Gestalt", "Gestalt", "I", r"Gestalt", "不译，首现括注「格式塔」"),
 ("transmutation", "transmutation", "I", r"transmutation", "不译，待裁定"),
 ("eventually coconnective", "最终余连通", "A", r"eventually coconnective", ""),
 ("connective", "连通", "A", r"connective", ""),
 ("suave", "suave", "I", r"\bsuave\b", "Heyer–Mann 术语，不译"),
 ("prim", "prim", "I", r"\bprim\b", "Heyer–Mann 术语，不译"),
 ("universally locally acyclic", "泛局部无环", "A", r"universally locally acyclic", ""),
 ("cohomologically smooth", "上同调光滑", "A", r"cohomologically smooth", ""),
 ("Artin–Schreier sheaf", "Artin–Schreier 层", "A", r"Artin.Schreier", ""),
 ("exponential D-module", "指数 D-模", "A", r"exponential D-module", ""),
 ("wild Betti sheaves", "野 Betti 层", "I", r"wild Betti", ""),
 ("exponential motives", "指数动机", "A", r"exponential motives", ""),
 ("Hochschild homology", "Hochschild 同调", "A", r"Hochschild", ""),
 ("cyclic Bar complex", "循环 Bar 复形", "A", r"Bar complex", ""),
 ("Morita theory", "Morita 理论", "A", r"Morita", ""),
 ("p-adic field", "p 进域", "L", r"p-adic field", ""),
 ("archimedean", "阿基米德", "A", r"archimedean", ""),
 ("twistor-P1", "扭量 P$^1$", "I", r"twistor", ""),
 ("Fargues–Fontaine curve", "Fargues–Fontaine 曲线", "A", r"Fargues.Fontaine", ""),
 ("automorphic-to-Galois", "自守到 Galois", "I", r"automorphic-to-Galois", "方向名"),
 ("Galois-to-automorphic", "Galois 到自守", "I", r"Galois-to-automorphic", "方向名"),
]

rows = []
for en, zh, code, pat, note in T:
    pg = first(pat)
    rows.append((en, zh, code, str(pg) if pg else "", note))

out = os.path.join(ROOT, "glossary.tsv")
with io.open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write("英文\t中文\t依据\t首现页\t备注\n")
    for r in rows:
        f.write("\t".join(r) + "\n")
print("terms=%d" % len(rows))
for r in rows:
    if not r[3]:
        print("!! 未在原文找到:", r[0])
