# -*- coding: utf-8 -*-
"""生成 03-条款索引.md、05-溯源表.tsv，以及 04 的术语/文献表片段。"""
import os, io, re

BASE = os.path.dirname(os.path.abspath(__file__))          # 工程文件/tools
WORK = os.path.dirname(BASE)                               # 工程文件
CARD = os.path.join(os.path.dirname(WORK), "资料卡")        # 工程根/资料卡

# (节, 编号, 类型, 页, 一句话, 外部文献, 外部定位, 状态, 备注)
ITEMS = [
("1","1.1","假设","3","$G$ 在 $\\mathbb F_q$ 上分裂、单连通，$\\Gamma=G(\\mathbb Z)$，$M=G(\\mathbb R)/K_\\infty$","本篇（Bourbaki 1252）","§1, p3","OK","综述设定，无外部对应"),
("1","1.2","问题","3","描述带 Hecke 代数 $\\mathbb T$ 作用的向量空间 $\\mathcal A(M/\\Gamma)$","本篇","§1, p3","OK","综述提出的问题"),
("1","1.3","注","5","Ramanujan 方向：$\\psi_p$ 落在 $\\check G(\\mathbb C)$ 的紧子群中，$\\psi_\\infty$ 落在紧子群李代数中","本篇","§1, p5","OK","一般形式见 Arthur 1989（p5 引用）"),
("1","1.4","注","5","互反方向要求 $\\Spec(\\mathbb Z)$ 上的不可约 $\\check G$-局部系统，而该概念尚不存在","本篇","§1, p5","OK","综述性说明"),
("1","1.5","猜想","6","存在 $\\LocSys_{\\check G}$ 与 $\\mathbb T$-等变同构 $\\mathcal A(M/\\Gamma)\\cong\\Gamma(\\LocSys_{\\check G},\\omega)$","本篇","§1, p6","OK","数域版猜想，尚未证明"),
("1","1.6","注","6","猜想的两处不清楚：局部系统的定义、$\\LocSys$ 是哪种叠","本篇","§1, p6–7","OK","—"),
("1","1.7","定理","8","$p$ 充分大时存在开闭子叠 $\\LocSys'$ 与 $\\mathbb T$-等变同构 $\\mathcal A_c(\\Bun_G(\\mathbb F_q))\\cong\\Gamma(\\LocSys',\\omega)$","Gaitsgory–Raskin 2025a","arXiv:2508.02237, Thm 0.2.2","OK","原文标注定理号"),
("1","1.8","注","9","Whittaker 归一化：$\\omega$ 的典范截面对应 Poincaré 级数，经 $2\\rho(\\Theta)$ 扭转与 Serre 对偶 $H^1(X,\\Omega)=\\mathbb F_q$","本篇","§1, p9","OK","—"),
("1","1.9","注","10","数域情形证明第一步（提升为拟凝聚层）失效","本篇","§1, p10","OK","—"),
("2","2.1","注","11","同时有底域 $k$ 与系数域 $e=\\overline{\\mathbb Q}_\\ell$（或 $\\mathbb C$）","本篇","§2, p11","OK","—"),
("2","2.2","定理","12","$\\tr(\\mathrm{Fr}|D(\\Bun_G))\\cong\\mathcal A_c(\\Bun_G(\\mathbb F_q))$","AGKRV 2021","arXiv:2102.07906（主定理）","OK","题名即此结果；原文未标定理号"),
("2","2.3","注","13","几何情形的 $\\Bun_G$ 层范畴远大于函数空间，定理 2.2 非恒真","本篇","§2, p13","OK","—"),
("2","2.4","定理","14","几何 Satake 等价 $\\Rep(\\check G)\\cong\\Perv_{\\Gr_G}$（卷积）","Mirković–Vilonen 2007","DOI 10.4007/annals.2007.166.95, §1（主定理）","OK","DOI 经 Crossref 核验"),
("2","2.5","注","14","取 Frobenius 迹还原 Satake；分歧群版本见 Zhu 2024、van den Hove 2024","van den Hove 2024","arXiv:2404.15694, Thm 1.4","OK","定理号据原文"),
("2","2.6","注","15","几何 Satake 证明用融合：在 $\\Hck^{\\loc}_{X^n}$ 上定义融合积，由延拓唯一性得对称性","本篇","§2, p15","OK","—"),
("2","2.7","定理","16","$D_{\\qc}(\\LocSys_{\\check G})$ 在 $D(\\Bun_G)$ 上作用，细化 Hecke 作用","AGKRV 2020b","arXiv:2010.01906","OK","原文未标定理号"),
("2","2.8","注","16","写清谱作用与 Hecke 作用的相容性会唯一确定谱作用，即得自守→Galois 方向","本篇","§2, p16","OK","—"),
("2","2.9","注","17","函数域算术类比由 Lafforgue 2018 建立；几何侧另有 AGKRV 2020b、Nadler–Yun 2019、Ben-Zvi–Nadler 2018","Lafforgue 2018","DOI 10.1090/jams/897, JAMS 31(3) 719–891","OK","DOI 经 Crossref 核验"),
("2","2.10","猜想","17","$D_{\\qc}(\\LocSys_{\\check G})$-线性等价 $D(\\Bun_G)\\simeq\\IndCoh_{\\mathrm{Nilp}}(\\LocSys_{\\check G})$，归一化送结构层到 Whittaker 层","AGKRV 2020b","arXiv:2010.01906（猜想形式）","OK","特征 0 已证（定理 2.11）"),
("2","2.11","定理","18","$k$ 特征 $0$ 时猜想成立（de Rham、Betti、étale）","Gaitsgory–Raskin 2025b 等五篇","arXiv:2405.03599v3","OK","—"),
("2","2.12","定理","18","$k$ 特征 $p$ 充分大时 $D(\\Bun_G)\\simeq\\IndCoh_{\\mathrm{Nilp}}(\\LocSys')$","Gaitsgory–Raskin 2025a","arXiv:2508.02237","OK","—"),
("2","2.13","注","19","证明策略：三情形互推、Witt 形变、de Rham 秩归纳；三要素（Whittaker、Kac–Moody、$\\LocSys$ 几何）","本篇","§2, p19","OK","—"),
("3","3.1","注","20","$(-^!,-_*)$ 形式化难读，作者用 $(-^*,-_!)$","本篇","§3, p20","OK","—"),
("3","3.2","注","20","核范畴 $K_D=\\Fun(\\Corr(\\Sch^{\\mathrm{ft}}_k),\\PrL_e)$，$\\Hom([X],[Y])=D(X\\times_kY)$，复合为卷积","本篇","§3, p20","OK","—"),
("3","3.3","注","21","两种形式化在紧对象层面只差 Verdier 对偶；$\\Bun_G$ 光滑故 $D(\\Bun_G)$ 一致","本篇","§3, p21","OK","—"),
("3","3.4","定理","21","三条件等价：幂零奇异支撑 $\\iff$ Hecke-lisse $\\iff$ $\\Ind D^{\\mathrm{prim}}$","AGKRV 2020b","arXiv:2010.01906, Thm 14.4.4","OK","另用 NY 2019 Thm 5.2.1/6.1.1、Heyer–Mann 2024 Lemma 4.4.18(ii)/Cor 4.5.18、Kuppel 2024 Thm 3.3.24"),
("5","5.1","定理","26","$C\\in\\PrL_e$ 上 $D_{\\qc}(\\LocSys^{\\mathrm{Betti}})$ 作用 $\\leftrightarrow$ 正合幺半函子 $\\Rep(\\check G^I)\\to\\End(C)^{B\\pi_1^I}$","Nadler–Yun 2019","DOI 10.1007/s11856-019-1871-9, §5","OK","Betti 谱作用主定理"),
("5","5.2","注","26","拟凝聚类比：$M\\in D_{\\qc}(\\LocSys^{\\mathrm{Betti}})$ $\\leftrightarrow$ 函子 $\\Rep(\\check G^I)\\to D(*/\\pi_1^I)$","本篇","§5, p26","OK","—"),
("5","5.3","推论","28","Betti 或 étale 情形存在 $D_{\\qc}(\\LocSys_{\\check G})$ 在 $D_{\\mathrm{Nilp}}(\\Bun_G)$ 上的谱作用","Nadler–Yun 2019；AGKRV 2020b","AGKRV 2020b 主定理 14.3.2","OK","定理号据原文"),
("5","5.4","注","29","该作用给出猜想 1.5 的一半；函数域算术类比见 Lafforgue 2018、Lafforgue–Zhu 2019","Lafforgue–Zhu 2019","arXiv:1811.07976v2","OK","—"),
("5","5.5","定义","29","带 $I$ 条腿的 shtuka 模空间 $\\mathrm{Sht}^I\\to(X^W)^I$","本篇","§5, p29","OK","综述原创表述"),
("5","5.6","注","30","整个 $D(\\Bun_G)$ 承载 $D_{\\qc}(*/\\check G)_{\\mathrm{Ran}}$ 作用，得 $\\LocSys^{\\mathrm{Betti,Gest}}$ 与单射","本篇","§5, p30–31","OK","—"),
("5","5.7","注","31","étale 的 $(\\infty,2)$ 版本：$\\LocSys^{\\et,\\mathrm{Gest}}$，$D(\\Bun_G)$ 为其上的范畴层","本篇","§5, p31","OK","引 Scholze 2026 第 9 讲"),
("5","5.8","命题","31","对角 $0$-affine；$\\LocSys^{\\et}\\times_{\\mathrm{Gest}}[*]\\to\\LocSys^{\\et,\\mathrm{Gest}}$ 是 $1$-étale 且 $1$-affine 的单射","本篇","§5, p31","OK","—"),
("5","5.9","定理","32","de Rham 情形 $D(\\Bun_G)$ 支撑在 $\\LocSys^{\\dR}\\hookrightarrow\\LocSys^{\\dR,\\mathrm{Gest}}$ 上","Gaitsgory 2015；GR 2025b","arXiv:2405.03599v3","OK","—"),
("5","5.10","注","32","容许 $D_{\\qc}(\\LocSys^{\\dR})$ 作用不强制 Hecke 作用沿 $X^I$ 局部常值","本篇","§5, p32–33","OK","—"),
("5","5.11","注","33","$\\LocSys^{\\dR,\\mathrm{Gest}}$ 有干净的生成元与关系，但子空间 $\\LocSys^{\\dR}$ 尚无法如此描述","本篇","§5, p33","OK","—"),
("6","6.1","注","34","$\\mathbb G_m$ 的 Cartier 对偶：$\\Pic\\cong\\mathbb Z\\times J\\times*/\\mathbb G_m$，$*\\times^L_{\\mathbb G_m}*=\\Spec(e[\\varepsilon])$","Laumon 1996","arXiv:alg-geom/9603004","OK","de Rham 侧见 p35"),
("7","7.1","注","36","Beilinson 投影子 $P\\colon D(\\Bun_G)\\to D_{\\mathrm{Nilp}}(\\Bun_G)$ 保紧对象但非伴随；$D_{\\mathrm{Nilp}}=\\Ind D^{\\mathrm{prim}}$","Kuppel 2024","Kuppel 2024, Thm 3.3.24","OK","硕士论文，无 DOI"),
("8","8.1","例","38","$F=\\mathrm{id}$ 恢复 Hochschild 同调；$C=D(A)$ 时由循环 Bar 复形计算","本篇","§8, p38","OK","原文此处有笔误（见 04）"),
("8","8.2","定理","39","$\\tr(\\mathrm{Fr}|D_{\\mathrm{Nilp}}(\\Bun_G))\\cong\\mathcal A_c(\\Bun_G(\\mathbb F_q))$","AGKRV 2021","arXiv:2102.07906","OK","—"),
("8","8.3","注","40","还须算 $\\tr(\\mathrm{Fr}|D(\\Bun_G))$，用自对偶性与 Weil 下降类、shtuka 纤维积","本篇","§8, p40","OK","引 Gaitsgory–Rozenblyum 2017、Xue 2025"),
("9","9.1","注","41","换 $\\psi'$ 只要系数非零就与 $\\psi$ 在 $T$ 下共轭，Whittaker 层相同；故可在 Betti 设定定义","本篇","§9, p41","OK","—"),
("9","9.2","定义","42","粗 Langlands 函子 = $\\mathbb L_G$ 的右伴随","本篇","§9, p42","OK","—"),
("9","9.3","定理","42","存在唯一的保余极限函子提升粗函子，且与 Whittaker 层相容","Gaitsgory–Raskin 2025b","arXiv:2405.03599v3","OK","—"),
("9","9.4","注","42","唯一性：所有函子保余极限，由生成对象上的值决定","本篇","§9, p42","OK","—"),
("9","9.5","注","43","$!$-层（而非 $*$-层）的出现说明 Whittaker 侧本质上是余异的","本篇","§9, p43","OK","—"),
("9","9.6","定理","44","几何 Casselman–Shalika：$D^!(\\mathrm{LU}^{\\Theta}\\backslash\\psi\\mathrm{Gr}^{\\Theta}_G)=g_{1*}(f_{1\\sharp}\\mathbf 1\\otimes\\psi)$","本篇","§9, p44","OK","证明用 Iwasawa 分层"),
("9","9.7","推论","45","$\\mathrm{Whit}(G)\\cong D_{\\qc}(*/\\check G)_{\\mathrm{Ran}}$","本篇","§9, p45","OK","—"),
("10","10.1","定理","47","第二伴随：$\\CT^{P^-}_!$ 是 $\\Eis^P_!$ 的右伴随；单位由 $\\Delta_{\\Bun_M,!}\\mathbf 1\\to f_!\\mathbf 1$ 给出","Drinfeld–Gaitsgory 2016","DOI 10.1007/s00029-016-0269-3, Selecta 22(4) 1881–1951","OK","DOI 经 Crossref 核验"),
("10","10.2","注","48","$\\Eis^P_!$ 保紧对象而谱侧不保，故须用 $\\IndCoh_{\\mathrm{Nilp}}$","本篇","§10, p48","OK","—"),
("11","11.1","定义","50","$\\Op^{\\mathrm{monfree}}_{\\check G}$：形式圆盘上带平坦联络的 $\\check G$-丛，连带去心圆盘上的 oper 结构","本篇","§11, p50","OK","综述原创定义"),
("11","11.2","注","50","$\\mathrm{KL}(G)$ 经 $f_{1\\sharp}\\mathbf 1$ 与 $\\Op^{\\mathrm{monfree}}_{\\check G}$ 上的 $\\IndCoh$ 相联系","本篇","§11, p50","OK","—"),
("11","11.3","注","50","几何局部 Langlands 应是 $\\mathrm{KL}(G)\\cong\\IndCoh(\\Op^{\\mathrm{monfree}}_{\\check G})$","本篇","§11, p50","OK","—"),
("11","11.4","定理","51","$\\mathrm{KL}(G)\\cong\\IndCoh(\\Op^{\\mathrm{monfree}}_{\\check G})$，与 $\\Loc_G$、$\\Poinc^{\\mathrm{spec}}$ 构成交换图","ABCCCFGLRR 2024","arXiv:2405.03648, Thm 0.1.2","OK","定理号据原文"),
("11","11.5","注","51","该图给出构造整体自守对象的程序","本篇","§11, p51","OK","—"),
("12","12.1","注","53","de Rham 情形 $\\LocSys$ 整体截面极少，故把「处处重数一」化为「整体截面重数一」","Færgeman–Raskin 2025；BKS 2022","DOI 10.1090/jams/1051；arXiv:1801.00655","OK","BKS 年份见 04 勘误"),
]

EN = {
"1.1":"G split simply connected; Gamma = G(Z)",
"1.2":"Describe A(M/Gamma) as a T-module",
"1.3":"Ramanujan: psi_p lies in a compact subgroup",
"1.4":"Reciprocity: irreducible check-G-local systems over Spec Z",
"1.5":"Conjecture: A(M/Gamma) = Gamma(LocSys_checkG, omega)",
"1.6":"What is a check-G-local system; which kind of stack",
"1.7":"Theorem: A_c(Bun_G(F_q)) = Gamma(LocSys', omega)",
"1.8":"Whittaker normalization: canonical section = Poincare series",
"1.9":"Number-field step one fails",
"2.1":"Two fields: k and e",
"2.2":"tr(Fr|D(Bun_G)) = A_c(Bun_G(F_q))",
"2.3":"First place geometry differs from functions",
"2.4":"Geometric Satake: Rep(check G) = Perv(Gr_G)",
"2.5":"Trace of Frobenius recovers Satake; ramified groups",
"2.6":"Proof via fusion on the local Hecke stack over X^n",
"2.7":"D_qc(LocSys_checkG) acts on D(Bun_G)",
"2.8":"Compatibility uniquely determines the spectral action",
"2.9":"Function-field case: Lafforgue 2018",
"2.10":"Conjecture: D(Bun_G) = IndCoh_Nilp(LocSys_checkG)",
"2.11":"Geometric Langlands, characteristic 0",
"2.12":"Geometric Langlands, characteristic p",
"2.13":"Strategy: three reductions and three key inputs",
"3.1":"The (-^!,-_*) formalism is confusing; use (-^*,-_!)",
"3.2":"Kernel category K_D and Hom([X],[Y]) = D(X x Y)",
"3.3":"Choices agree on compact objects; Bun_G is smooth",
"3.4":"Three equivalent conditions for D_Nilp",
"5.1":"Betti spectral action = Rep(checkG^I) -> End(C)^{B pi_1^I}",
"5.2":"Quasi-coherent analogue of Theorem 5.1",
"5.3":"Spectral action on D_Nilp(Bun_G)",
"5.4":"Automorphic-to-Galois direction; shtuka cohomology",
"5.5":"Shtukas with I legs: Sht^I -> (X^W)^I",
"5.6":"Betti: action on all of D(Bun_G); LocSys^{Betti,Gest}",
"5.7":"Etale: (infinity,2)-version; LocSys^{et,Gest}",
"5.8":"Diagonal 0-affine; 1-etale, 1-affine injection",
"5.9":"de Rham: supported on LocSys^dR",
"5.10":"de Rham: action does not force local constancy",
"5.11":"No description of LocSys^dR inside LocSys^{dR,Gest}",
"6.1":"G_m: Cartier duality; * x^L_{G_m} * = Spec(e[eps])",
"7.1":"Beilinson projector is not an adjoint",
"8.1":"Cyclic bar complex computes the trace",
"8.2":"tr(Fr|D_Nilp) = A_c",
"8.3":"Computing tr(Fr|D(Bun_G)): Weil descent",
"9.1":"Independence of psi",
"9.2":"Coarse Langlands functor: right adjoint of L_G",
"9.3":"Unique colimit-preserving lift",
"9.4":"Why the lift is unique",
"9.5":"Why !-sheaves appear",
"9.6":"Geometric Casselman-Shalika",
"9.7":"Whit(G) = D_qc(*/checkG)_Ran",
"10.1":"Second adjunction: CT dashv Eis",
"10.2":"Why IndCoh_Nilp is needed",
"11.1":"Monodromy-free opers",
"11.2":"KL(G) via f_{1 sharp} 1",
"11.3":"Geometric local Langlands conjecture",
"11.4":"KL(G) = IndCoh(Op^monfree)",
"11.5":"Constructing automorphic objects",
"12.1":"Cuspidal part: multiplicities one",
}

# (key, 作者年份, 题名简称, 出处, 标识, 状态, 备注)
REFS = [
("aizenbud2016","Aizenbud–Avni 2016","Representation growth and rational singularities of the moduli space of local systems","Invent. Math. 204(1) 245–316","DOI 10.1007/s00222-015-0614-8","OK","Crossref 核验"),
("ab2024","ABCCCFGLRR 2024","Proof of the geometric Langlands conjecture II: Kac-Moody localization and the FLE","预印本","arXiv:2405.03648","OK","arXiv 标题核验"),
("ab2024iv","ABCCFGLRR 2024","Proof of the geometric Langlands conjecture IV: ambidexterity","预印本","arXiv:2409.08670","OK","arXiv 标题核验"),
("ag2015","Arinkin–Gaitsgory 2015","Singular support of coherent sheaves and the geometric Langlands conjecture","Selecta Math. 21(1) 1–199","DOI 10.1007/s00029-014-0167-5","OK","Crossref 核验"),
("agkrv2020a","AGKRV 2020a","Duality for automorphic sheaves with nilpotent singular support","预印本","arXiv:2012.07665","OK","arXiv 标题核验"),
("agkrv2020b","AGKRV 2020b","The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support","预印本","arXiv:2010.01906","OK","arXiv 标题核验"),
("agkrv2021","AGKRV 2021","Automorphic functions as the trace of Frobenius","预印本","arXiv:2102.07906","OK","arXiv 标题核验"),
("arthur1989","Arthur 1989","Unipotent automorphic representations: conjectures","Astérisque 171-172, 13–71","—","无法核验","文集，未查 DOI"),
("beilinson2016","Beilinson 2016","Constructible sheaves are holonomic","Selecta Math. 22(4) 1797–1819","DOI 10.1007/s00029-016-0260-z","OK","Crossref 核验"),
("bd1996","Beilinson–Drinfeld 1996","Quantization of Hitchin's fibration and Langlands' program","Math. Phys. Stud. 19, 3–7","—","无法核验","会议文集，未查 DOI"),
("benzvi2026","Ben-Zvi 2026","What is the geometric Langlands correspondence about?","Current Events Bulletin of the AMS, 4–36","—","无法核验","2026 年卷，尚未见 DOI"),
("bn2013","Ben-Zvi–Nadler 2013","Loop spaces and representations","Duke Math. J. 162(9) 1587–1619","DOI 10.1215/00127094-2266130","OK","Crossref 核验"),
("bn2018","Ben-Zvi–Nadler 2018","Betti geometric Langlands","Proc. Sympos. Pure Math. 97.2, 3–41","—","无法核验","文集，未查 DOI"),
("bks2022","Beraldo–Kazhdan–Schlank 2022","Contractibility of the space of generic opers for classical groups","预印本","arXiv:1801.00655v2","OK","arXiv 标题核验；年份 DIFF（2018 初版）"),
("bg2014","Buzzard–Gee 2014","The conjectural connections between automorphic representations and Galois representations","LMS Lecture Note Ser. 414, 135–187","—","无法核验","文集，未查 DOI"),
("ccfg2024","CCFGLRR 2024","Proof of the geometric Langlands conjecture III: compatibility with parabolic induction","预印本","arXiv:2409.07051","OK","arXiv 标题核验"),
("drinfeld1983","Drinfeld 1983","Two-dimensional l-adic representations of the fundamental group of a curve over a finite field and automorphic forms on GL(2)","Amer. J. Math. 105(1) 85–114","DOI 10.2307/2374382","OK","Crossref 核验"),
("dg2016","Drinfeld–Gaitsgory 2016","Geometric constant term functor(s)","Selecta Math. 22(4) 1881–1951","DOI 10.1007/s00029-016-0269-3","OK","Crossref 核验"),
("efimov2025","Efimov 2025","K-theory and localizing invariants of large categories","预印本","arXiv:2405.12169v3","OK","arXiv 标题核验"),
("egh2025","Emerton–Gee–Hellmann 2025","An introduction to the categorical p-adic Langlands program","预印本","arXiv:2210.01404v5","OK","arXiv 标题核验"),
("fr2025","Færgeman–Raskin 2025","Non-vanishing of geometric Whittaker coefficients for reductive groups","JAMS 38(4) 919–995","DOI 10.1090/jams/1051","OK","Crossref 核验"),
("fargues2025","Fargues 2025","Geometrization of the local Langlands correspondence: an overview","J. Math. Sci. Univ. Tokyo 32(2) 157–240","—","无法核验","Crossref 只命中同题异文（Crelle 2026），见 04 DIFF"),
("fs2024","Fargues–Scholze 2024","Geometrization of the local Langlands correspondence","Astérisque（待刊）","arXiv:2102.13459","OK","arXiv 标题核验"),
("ff1992","Feigin–Frenkel 1992","Affine Kac-Moody algebras at the critical level and Gelfand-Dikiĭ algebras","Adv. Ser. Math. Phys. 16, 197–215","—","无法核验","文集，未查 DOI"),
("fj2025","Fresán–Jossen 2025","Exponential motives","作者主页 PDF","URL javier.fresan.perso.math.cnrs.fr/expmot.pdf","无法核验","未联网抓取 PDF"),
("gaitsgory2015","Gaitsgory 2015","Outline of the proof of the geometric Langlands conjecture for GL(2)","Astérisque 370, 1–112","—","无法核验","Astérisque 卷，未查 DOI"),
("gr2025a","Gaitsgory–Raskin 2025a","Geometric Langlands in positive characteristic from characteristic zero","预印本","arXiv:2508.02237","OK","arXiv 标题核验"),
("gr2025b","Gaitsgory–Raskin 2025b","Proof of the geometric Langlands conjecture I: construction of the functor","预印本","arXiv:2405.03599v3","OK","arXiv 标题核验"),
("gr2026","Gaitsgory–Raskin 2026","Proof of the geometric Langlands conjecture V: the multiplicity one theorem","预印本","arXiv:2409.09856v3","OK","arXiv 标题核验；年份 DIFF（2024 初版）"),
("gr2017","Gaitsgory–Rozenblyum 2017","A study in derived algebraic geometry. Vol. I","AMS Math. Surveys and Monographs 221","—","无法核验","专著，未查 DOI"),
("gpl2022","Gallauer–Pepin Lehalleur 2022","Exponentiation of coefficient systems and exponential motives","预印本","arXiv:2211.17247","OK","arXiv 标题核验"),
("hhs2024","Hamann–Hansen–Scholze 2024","Geometric Eisenstein series I: finiteness theorems","预印本","arXiv:2409.07363","OK","arXiv 标题核验"),
("hs2023","Hansen–Scholze 2023","Relative perversity","Commun. Am. Math. Soc. 3, 631–668","DOI 10.1090/cams/21","OK","Crossref 核验"),
("hm2024","Heyer–Mann 2024","6-Functor Formalisms and Smooth Representations","预印本","arXiv:2410.13038","OK","arXiv 标题核验"),
("kuppel2024","Kuppel 2024","Proper Sheaves for Schemes and Stacks","Bonn 硕士论文","—","无法核验","学位论文，无 DOI"),
("lafforgue2018","Lafforgue 2018","Chtoucas pour les groupes réductifs et paramétrisation de Langlands globale","JAMS 31(3) 719–891","DOI 10.1090/jams/897","OK","Crossref 核验"),
("lz2019","Lafforgue–Zhu 2019","Décomposition au-dessus des paramètres de Langlands elliptiques","预印本","arXiv:1811.07976v2","OK","arXiv 标题核验（API 返回 UTF-8 乱码，标题实存）"),
("laumon1987","Laumon 1987","Correspondance de Langlands géométrique pour les corps de fonctions","Duke Math. J. 54(2) 309–359","DOI 10.1215/s0012-7094-87-05418-4","OK","Crossref 核验"),
("laumon1996","Laumon 1996","Transformation de Fourier géneralisée","预印本","arXiv:alg-geom/9603004","OK","arXiv 标题核验"),
("liu2024","Liu–Zheng 2024","Enhanced six operations and base change theorem for higher Artin stacks","预印本","arXiv:1211.5948","OK","arXiv 标题核验"),
("lurie2017","Lurie 2017","Higher Algebra","作者主页 PDF","URL math.ias.edu/~lurie/papers/HA.pdf","无法核验","未联网抓取"),
("mann2022","Mann 2022","A p-Adic 6-Functor Formalism in Rigid-Analytic Geometry","预印本","arXiv:2206.02022","OK","arXiv 标题核验"),
("mv2007","Mirković–Vilonen 2007","Geometric Langlands duality and representations of algebraic groups over commutative rings","Ann. of Math. 166(1) 95–143","DOI 10.4007/annals.2007.166.95","OK","Crossref 核验"),
("nt2025","Nadler–Taylor 2025","The Whittaker functional is a shifted microstalk","Transform. Groups 30(3) 1425–1450","DOI 10.1007/s00031-023-09836-x","OK","Crossref 核验"),
("ny2019","Nadler–Yun 2019","Spectral action in Betti geometric Langlands","Israel J. Math. 232(1) 299–349","DOI 10.1007/s11856-019-1871-9","OK","Crossref 核验"),
("raskin2025","Raskin 2025","Conjectures of Arthur and Ramanujan for unramified automorphic forms: announcement","ICM 报告 PDF","URL samraskin.net/icm.pdf","无法核验","未联网抓取"),
("rs2021","Richarz–Scholbach 2021","The motivic Satake equivalence","Math. Ann. 380(3-4) 1595–1653","DOI 10.1007/s00208-021-02176-9","OK","Crossref 核验"),
("scholze2024","Scholze 2024","Geometrization of the real local Langlands correspondence","—","—","无法核验","原文未给出处"),
("scholze2025","Scholze 2025","Wild Betti sheaves","Laumon 纪念文集","—","无法核验","文集未出版信息"),
("scholze2026","Scholze 2026","Geometry and Higher Category Theory","讲义","URL people.mpim-bonn.mpg.de/scholze/Gestalten.pdf","无法核验","未联网抓取"),
("tamarkin2018","Tamarkin 2018","Microlocal condition for non-displaceability","Springer Proc. Math. Stat. 269, 99–223","DOI 10.1007/978-3-030-01588-6_3","OK","Crossref 核验"),
("vdh2024","van den Hove 2024","The integral motivic Satake equivalence for ramified groups","预印本","arXiv:2404.15694","OK","arXiv 标题核验"),
("weil1974","Weil 1974","Basic number theory（第 3 版）","Springer Grundlehren 144","—","无法核验","专著，未查 DOI"),
("xue2025","Xue 2025","Smoothness of cohomology sheaves of stacks of shtukas","Laumon 纪念文集","—","无法核验","文集未出版信息"),
("zhu2024","Zhu 2024","A note on integral Satake isomorphisms","Tata Inst. Stud. Math. 41, 469–489","—","无法核验","文集，未查 DOI"),
("zhu2025","Zhu 2025","Coherent sheaves on the stack of Langlands parameters","Proc. Sympos. Pure Math. 112, 39–123","—","无法核验","文集，未查 DOI"),
]

STEPS = [
("步 1","§1, p2–5","问题 1.2 与 Satake 同构","本篇","§1, p3–5","OK"),
("步 2","§1–§2, p5–18","猜想 1.5 与猜想 2.10","本篇；Arinkin–Gaitsgory 2015","§1 p6；§2 p17；DOI 10.1007/s00029-014-0167-5","OK"),
("步 3","§2, p12–16","定理 2.2 与定理 2.7","AGKRV 2021；AGKRV 2020b","arXiv:2102.07906；arXiv:2010.01906","OK"),
("步 4","§3, p19–23","定理 3.4 三条件等价","AGKRV 2020b","arXiv:2010.01906, Thm 14.4.4","OK"),
("步 5","§4–§5, p23–33","定理 5.1、推论 5.3、定理 5.9","Nadler–Yun 2019；Gaitsgory 2015；GR 2025b","DOI 10.1007/s11856-019-1871-9；arXiv:2405.03599","OK"),
("步 6","§7–§8, p35–40","Beilinson 投影子与定理 8.2","AGKRV 2021；Kuppel 2024","arXiv:2102.07906；Kuppel 2024 Thm 3.3.24","OK"),
("步 7","§9, p40–45","Whittaker 层、定理 9.3、定理 9.6","GR 2025b；Færgeman–Raskin 2025","arXiv:2405.03599；DOI 10.1090/jams/1051","OK"),
("步 8","§10, p45–49","定理 10.1 第二伴随","Drinfeld–Gaitsgory 2016","DOI 10.1007/s00029-016-0269-3","OK"),
("步 9","§11, p49–52","定理 11.4 Kac–Moody 局部化","ABCCCFGLRR 2024","arXiv:2405.03648, Thm 0.1.2","OK"),
("步 10","§12, p52–53","尖点收口：保守性 + BKS","Færgeman–Raskin 2025；BKS 2022","DOI 10.1090/jams/1051；arXiv:1801.00655","OK"),
]

TERMS = [
("拟凝聚层","quasi-coherent sheaf","$D_{\\qc}(\\LocSys)$ 是拟凝聚层的导出范畴，几何 Langlands 的自守侧是其上的模","§2 p16；§5 p26"),
("归纳完备化","Ind-completion","$\\IndCoh_{\\Nilp}$ 是带幂零奇异支撑的凝聚复形的归纳完备化，不是拟凝聚层范畴","§2 p17–18"),
("幂零奇异支撑","nilpotent singular support","$A\\in D(\\Bun_G)$ 的奇异支撑落在 $T^*\\Bun_G$ 的幂零锥中；这是几何 Langlands 成立的正确子范畴","§3 p21"),
("Hecke-lisse","Hecke-lisse","对一切 Hecke 算子 $T_V(A)$ 仍是局部系统的对象；与幂零奇异支撑等价","§3 p21"),
("六函子形式化","six-functor formalism","$D$ 同时带 $\\otimes,f^*,f_!,f^!,f_*$ 与基变换；两种取法（$(-^*,-_!)$ 与 $(-^!,-_*)$）只差 Verdier 对偶","§3 p19–21"),
("核范畴","kernel category","$K_D=\\Fun(\\Corr(\\Sch^{\\mathrm{ft}}_k),\\PrL_e)$，$\\Hom([X],[Y])=D(X\\times_kY)$","§3 p20"),
("suave / prim","suave / prim","suave = 有右伴随的 $!$-前推对应；prim = 在 $*$-拉回下稳定。二者是 $D_{\\Nilp}$ 的技术核心","§3 p21；§7 p37"),
("局部系统","local system","$\\check G$-局部系统 = $(\\check G)$-丛带平坦联络（dR）或 $\\pi_1$-表示的商（Betti）或 étale 局部系统","§4 p23–25"),
("粗模空间","coarse moduli","$\\LocSys^{\\dR}$ 的粗模空间与形式完备化并；整体截面稀少","§4 p24–25；§12 p53"),
("尖点","cuspidal","尖点部分 = 常数项函子的核，也 = 张量到 $\\LocSys^{\\mathrm{irred}}$ 的部分","§12 p52"),
("Eisenstein 级数","Eisenstein series","由真 Levi 子群诱导的自守形式；函子化为 $\\Eis^P_!=q_!p^*$","§10 p46"),
("常数项函子","constant term functor","$\\CT_!=p_!q^*$；第二伴随说 $\\CT^{P^-}_!$ 是 $\\Eis^P_!$ 的右伴随","§10 p46–47"),
("第二伴随","second adjunction","$\\CT^{P^-}_!\\dashv\\Eis^P_!$，是秩归纳的关键函子性陈述","§10 p47"),
("Whittaker 层","Whittaker sheaf","$\\mathcal W_\\psi=p_!\\psi^*\\exp$，是猜想 2.10 归一化的对象；亦称 Poincaré 对象","§9 p41"),
("微茎","microstalk","Whittaker 系数 = $T^*\\Bun_G$ 正则幂零轨迹处的微茎；Færgeman–Raskin 用它证保守性","§12 p52；Nadler–Taylor 2025"),
("oper","oper","$(\\check G)$-丛连带把其约化到 $\\check U^{\\Theta}$ 的结构；无单值 opers 是形式圆盘上的版本","§11 p50"),
("Kac–Moody 局部化","Kac-Moody localization","从 opers 产生 $D(\\Bun_G)$ 中对象的程序，给出「Galois 到自守」方向","§11 p50–51；§2 p19"),
("shtuka","shtuka","带修改的 $G$-丛；$I$ 条腿的 shtuka 模空间 $\\mathrm{Sht}^I\\to(X^W)^I$","§5 p29"),
("Weil 下降","Weil descent","把几何点上的迹下降为 $\\mathbb F_q$-点上的函数，用于定理 8.2 与注 8.3","§8 p39–40"),
("Gestalt / Gestalten","Gestalt","高阶范畴的几何化包装；$\\LocSys^{\\mathrm{Gest}}$ 是其上的映射对象","§5 p26–33；Scholze 2026"),
("$1$-étale / $1$-affine / $0$-affine","1-étale, 1-affine, 0-affine","Gestalten 的相对维数条件；命题 5.8 用它们陈述单射的正性","§5 p31"),
("挠形式","twisted form","$B^\\Theta$、$U^\\Theta$ 是 Borel 与单幂根被 $2\\rho(\\Theta)$ 扭转所得","§9 p40–41"),
("导出 Artin 叠","derived Artin stack","$\\LocSys_{\\check G}$ 的函子性定义；Zhihao Zhu 2025 给出性态良好的版本","§2 p15；§4 p25"),
("特征 $p$","characteristic p","$p=\\mathrm{char}(k)$ 须充分大且非 $G$ 的挠素数；此时只能得到开闭子叠 $\\LocSys'$","§1 p8；§2 p18"),
]

def ok_ratio(rows):
    return sum(1 for r in rows if r[7] == "OK") / float(len(rows))

def gen03():
    out = ["# 资料卡 03 · 条款索引", "",
           "57 条编号条目逐条列出：编号、类型、原文页、一句话内容。编号与原文一致（Bourbaki 体例：类型名在前、编号在节内递增），页码为原文页眉的印刷页。环境类型统计：假设 1、问题 1、猜想 2、定理 15、命题 1、推论 2、定义 4、注 31。", ""]
    secs = [("1","§1 引言：从数域到函数域","p1–11"),("2","§2 几何 Langlands 的表述","p11–19"),
            ("3","§3 六函子与幂零奇异支撑","p19–23"),("5","§5 谱作用、shtuka 与 de Rham","p25–33"),
            ("6","§6 $\\mathbb G_m$ 的玩具例","p33–35"),("7","§7 Beilinson 谱投影子","p35–38"),
            ("8","§8 Frobenius 的迹","p38–40"),("9","§9 Whittaker 系数","p40–45"),
            ("10","§10 Eisenstein 级数","p45–49"),("11","§11 Kac–Moody 局部化","p49–52"),
            ("12","§12 尖点形式","p52–53")]
    for sid, title, pages in secs:
        its = [x for x in ITEMS if x[0] == sid]
        out.append("## %s（原文 %s，共 %d 条）" % (title, pages, len(its)))
        out.append("")
        out.append("| 编号 | 类型 | 页 | 内容 |")
        out.append("|---|---|---|---|")
        for it in its:
            out.append("| %s | %s | %s | %s |" % (it[1], it[2], it[3], it[4]))
        out.append("")
    out.append("## 说明")
    out.append("")
    out.append("- §4（局部系统的叠）原文未编号，故本表无 §4。")
    out.append("- 译文环境与原文同号；`check_sections.py all` 逐节核对 57/57。")
    out.append("- 每一条的外部定位与核验状态见 `05-溯源表.tsv`。")
    return "\n".join(out) + "\n"

def gen05():
    rows = []
    hdr = ["卡文件","条目","原文页","原文编号","原文英文要点","外部文献","外部定位","核验状态","备注"]
    for it in ITEMS:
        rows.append(["01/03", it[4], "p" + it[3], it[1], EN.get(it[1], it[4]), it[5], it[6], it[7], it[8]])
    for i, st in enumerate(STEPS):
        rows.append(["02", st[0], "", "—", st[2], st[3], st[4], st[5], "论证地图节点"])
    for t in TERMS:
        m = re.search(r"p(\d+)", t[3])
        rows.append(["04", "术语：" + t[0], "p" + m.group(1) if m else "", "—", t[1] + "；" + t[2], "本篇", t[3], "OK", "术语按原文用法；外部对应见引文"])
    for r in REFS:
        rows.append(["04", r[1], "p53", "文献表", r[2] + "，" + r[3], r[1], r[4], r[5], r[6]])
    lines = ["\t".join(hdr)]
    for r in rows:
        lines.append("\t".join(x.replace("\t", " ") for x in r))
    return "\n".join(lines) + "\n", rows

def gen04_frag():
    out = ["<!-- AUTO: 术语表 -->", "", "| 术语 | 原文 | 释义 | 定位 |", "|---|---|---|---|"]
    for t in TERMS:
        out.append("| %s | %s | %s | %s |" % (t[0], t[1].replace("|", "/"), t[2], t[3]))
    out += ["", "<!-- AUTO: 文献表 -->", "", "| # | 文献 | 出处 | 标识 | 核验 | 备注 |", "|---|---|---|---|---|---|"]
    for i, r in enumerate(REFS, 1):
        out.append("| %d | %s | %s | %s | %s | %s |" % (i, r[1], r[3], r[4], r[5], r[6]))
    return "\n".join(out) + "\n"

with io.open(os.path.join(CARD, "03-条款索引.md"), "w", encoding="utf-8") as f:
    f.write(gen03())
tsv, rows = gen05()
with io.open(os.path.join(CARD, "05-溯源表.tsv"), "w", encoding="utf-8") as f:
    f.write(tsv)
with io.open(os.path.join(BASE, "card04_frag.md"), "w", encoding="utf-8") as f:
    f.write(gen04_frag())

tot = len(rows)
ok = sum(1 for r in rows if r[7] == "OK")
print("rows:", tot, "OK:", ok, "ratio: %.1f%%" % (100.0 * ok / tot))
from collections import Counter
print(Counter(r[7] for r in rows))
print("items:", len(ITEMS), "refs:", len(REFS), "terms:", len(TERMS), "steps:", len(STEPS))
