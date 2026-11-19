# -*- coding: utf-8 -*-
"""生成 leanstmt 三批陈述卡（witten2015 12 + witten2008 14 + gno1977 13）与 README/SCHEMA/MAP。

用法：
  python tools/make_cards.py            # 写文件
  python tools/make_cards.py --check    # 只校验不写（比较现有文件与本文件生成结果）

卡片数据：witten2015 批在 tools/cards15_data.py；witten2008 批在本文件 DATA08；gno1977 批在 tools/gno77_data.py。
index.jsonl 与 md/ 由 build_index.py / render_md.py 生成，勿手改。
"""
from __future__ import annotations

import argparse
import io
import json
import os
import sys

from cards15_data import DATA as DATA15, GAP_KEYS as GAP_KEYS15
from gno77_data import DATA as DATA77, META_GNO

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LEAN_TOOLCHAIN = "leanprover/lean4:v4.36.0"
LEAN_VERSION = "Lean 4.36.0 (x86_64-w64-windows-gnu, commit 611c117bfaf7b7ae1cfcf246ce6fba31e8f509e9)"
MATHLIB_REV = "d33c49ca43873d3746194325da62640cc893c9d9"
CHECKED_AT = "2026-11-19"
REVIEWER = "subagent（未见本卡中文陈述，仅据 Lean 语句回译）"

META = {
    "witten2015": dict(
        id_prefix="leanstmt/witten2015-",
        paper="Witten, More On Gauge Theory And Geometric Langlands",
        arxiv="arXiv:1506.04293v3",
        lean_dir="lean/ShuyiFormal/Witten2015",
        track="W15",
        pages_note="印刷页 = PDF 页 − 1",
    ),
    "witten2008": dict(
        id_prefix="leanstmt/witten2008-",
        paper="Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality",
        arxiv="arXiv:0802.0999v1",
        lean_dir="lean/ShuyiFormal/Witten2008",
        track="W08",
        pages_note="印刷页 = PDF 页",
    ),
}
META["gno1977"] = META_GNO

IMPORTS08 = [
    "Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality",
    "Mathlib.LinearAlgebra.Dimension.Constructions",
    "Mathlib.LinearAlgebra.SpecialLinearGroup",
    "Mathlib.Logic.Equiv.Prod",
]
IMPORTS08_GAP = [
    "Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality",
    "Mathlib.LinearAlgebra.SpecialLinearGroup",
]

DATA08 = [
    dict(
        key="s01",
        title="SU(N) 的中心是 ℤ_N（对偶群 PSU(N) 的核）",
        zh="Langlands 对偶群的基本例子：SU(N) 的对偶群是 PSU(N) = SU(N)/ℤ_N，被商掉的是中心 ℤ(SU(N)) ≅ ℤ_N。"
           "中心元恰是标量矩阵 ζ·1（ζ 为 N 次单位根）；因 mathlib 无紧李群，这里用复化群 SL(N,ℂ) 陈述。",
        en="The dual of SU(N) is PSU(N) = SU(N)/Z_N; the center of SU(N) consists of scalar matrices ζ·1 with ζ^N = 1.",
        section="2",
        pages=[2, 2],
        anchor="§2 开头（the dual of SU(N) is PSU(N) = SU(N)/Z_N）",
        lean_name="Witten2008.center_sl",
        lean_stmt="theorem center_sl (n : ℕ) (g : SpecialLinearGroup ℂ (Fin n → ℂ)) :\n"
                  "    g ∈ Subgroup.center (SpecialLinearGroup ℂ (Fin n → ℂ)) ↔\n"
                  "      ∃ r : ℂ, r ^ n = 1 ∧\n"
                  "        (g : (Fin n → ℂ) →ₗ[ℂ] (Fin n → ℂ)) = r • LinearMap.id",
        imports=IMPORTS08,
        deps=[
            dict(name="SpecialLinearGroup.mem_center_iff", module="Mathlib.LinearAlgebra.SpecialLinearGroup", kind="mathlib"),
            dict(name="Module.finrank_fintype_fun_eq_card", module="Mathlib.LinearAlgebra.Dimension.Constructions", kind="mathlib"),
        ],
        hypotheses=["n 为自然数（n = 0 时 SL(0,ℂ) 平凡，陈述仍成立）"],
        scope="algebraic-core",
        bt="对任意自然数 n 与行列式为 1 的复矩阵 g，g 属于 SL(n,ℂ) 的中心当且仅当 g 是标量乘法、且该标量的 n 次幂为 1。",
        notes="原文只把 SU(N) 与 PSU(N) 作为对偶群的例子点名；此卡把「商掉的离散中心是 μ_N」这一内容固定下来。"
              "同文件另有恒等特例 `residue_invariant`（m = 0 的伸缩律）。",
    ),
    dict(
        key="s02",
        title="有限对偶环面的影子：Hom(ℤ_N, U(1)) 有 N 个元素",
        zh="对偶环面是原环面的字符群；其有限群影子为 Hom(ℤ_N, U(1)) ≅ ℤ_N，"
           "因此「环面与对偶环面同秩」在 ℤ_N 层面表现为字符个数仍为 N。",
        en="The dual torus is the character group; at the finite level Hom(ℤ_N, U(1)) ≅ ℤ_N, so the character count is still N.",
        section="3",
        pages=[2, 4],
        anchor="§2（GNO/Langlands 对偶群）与 §3（special Lagrangian 纤维上的 T-对偶）",
        lean_name="Witten2008.card_dual_zmod",
        lean_stmt="theorem card_dual_zmod (n : ℕ) [NeZero n] :\n"
                  "    Fintype.card (AddChar (ZMod n) ℂ) = n",
        imports=IMPORTS08,
        deps=[
            dict(name="AddChar.card_eq", module="Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality", kind="mathlib"),
            dict(name="ZMod.card", module="Mathlib.Data.ZMod.Basic", kind="mathlib"),
        ],
        hypotheses=["n ≥ 1（`NeZero n`；n = 0 时 ZMod 0 ≅ ℤ，其对偶不是有限群）"],
        scope="discrete-core",
        bt="对任意正整数 n，从 ℤ/n 到复数乘法群的加法字符恰有 n 个。",
        notes="对偶环面 T∨ = Hom(X_*(T), U(1)) 的有限影子。原文 §3 的 T-对偶在 special Lagrangian 纤维上进行，"
              "此卡只形式化其群论骨架；环面/复几何部分见 G06。",
    ),
    dict(
        key="s03",
        title="T-对偶的离散同构：ℤ_N ≅ Hom(ℤ_N, U(1))",
        zh="有限阿贝尔群是 Pontryagin 自对偶的：ℤ_N ≅ Hom(ℤ_N, U(1))，且同构是典范的（不依赖生成元选择）。"
           "这是 SYZ 图像下纤维 T-对偶在有限群情形的对照。",
        en="Finite abelian groups are Pontryagin self-dual: Z_N ≅ Hom(Z_N, U(1)) canonically.",
        section="3",
        pages=[3, 4],
        anchor="§3（special Lagrangian 纤维上的 T-对偶）",
        lean_name="Witten2008.dual_zmod_equiv",
        lean_stmt="theorem dual_zmod_equiv (n : ℕ) [NeZero n] :\n"
                  "    Nonempty (ZMod n ≃+ AddChar (ZMod n) ℂ)",
        imports=IMPORTS08,
        deps=[
            dict(name="AddChar.zmodAddEquiv", module="Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality", kind="mathlib"),
        ],
        hypotheses=["n ≥ 1（`NeZero n`）"],
        scope="discrete-core",
        bt="对任意正整数 n，ℤ/n 与其加法字符群之间存在加法群同构。",
        notes="与 S02 同一节；S02 给基数、本卡给同构本身。对偶环面的连续版本（T ≅ Hom(X_*,U(1))）不在本卡范围。",
    ),
    dict(
        key="s04",
        title="非正则奇点系数在 z = λw 下的伸缩律",
        zh="非正则奇点写成 A = dz·(T_n/z^n + … + T_1/z + …)。在重标度 z = λw（λ≠0）下，"
           "第 (m+1) 重极点的系数变为 T_{m+1}/λ^m：留数 T_1 不变，m ≥ 1 的项随 λ 伸缩。",
        en="Under z = λw (λ≠0), the coefficient of z^{-(m+1)} scales as λ^{-m}; the residue T_1 is invariant.",
        section="5",
        pages=[8, 9],
        anchor="§5 式 (5.1) 及其后关于 T_1 与奇点阶数 n 为规范不变量的讨论",
        lean_name="Witten2008.coefficient_scaling",
        lean_stmt="theorem coefficient_scaling (lam c : ℂ) (hlam : lam ≠ 0) (m : ℕ) :\n"
                  "    lam * (c / lam ^ (m + 1)) = c / lam ^ m",
        imports=IMPORTS08,
        deps=[],
        hypotheses=["λ ≠ 0"],
        scope="algebraic-core",
        bt="对任意非零复数 λ、复数 c 与自然数 m，λ 乘以 c 除以 λ 的 m+1 次幂，等于 c 除以 λ 的 m 次幂。",
        notes="把「重标度下第 (m+1) 个系数变成 λ^{1-(m+1)}T_{m+1}」这个算术内容固定下来；"
              "留数不变（m=0）是同文件 `residue_invariant`。真正的模空间不变量陈述见 G08。",
    ),
    dict(
        key="s05",
        title="规范变换群的 currying",
        zh="M = Σ×C 上的规范变换群是 Maps(Σ, Maps(C,G))，按定义即 Maps(Σ×C, G)；"
           "类型层面这只是 currying。原文用这一步把四维规范理论看成以 Σ 为底、取值于 Bun_G(C) 的二维 sigma 模型。",
        en="Gauge transformations on M = Σ×C are Maps(Σ, Maps(C,G)) = Maps(Σ×C, G): a currying of function spaces.",
        section="6.1",
        pages=[12, 13],
        anchor="§6.1（Atiyah–Bott 1982 的无限维对 (Y, W_C)，W = Maps(C,G)）",
        lean_name="Witten2008.gauge_maps_curry",
        lean_stmt="theorem gauge_maps_curry (Sig C G : Type*) :\n"
                  "    Nonempty (((Sig → C → G) ≃ (Sig × C → G)))",
        imports=IMPORTS08,
        deps=[
            dict(name="Equiv.curry", module="Mathlib.Logic.Equiv.Prod", kind="mathlib"),
        ],
        hypotheses=["无"],
        scope="discrete-core",
        bt="对任意类型 Σ、C、G，两变量的函数空间 Σ → (C → G) 与乘积定义域上的函数空间 (Σ×C) → G 之间存在等价。",
        notes="只形式化类型等价（`Equiv.curry`），群结构由逐点乘法给出、此处不重复构造。"
              "原文 §6 的四维/二维物理陈述见 G09。",
    ),
    dict(
        key="g01",
        title="缺口：Y(G,C) 复辛、维数 2(g−1)dim G、典范丛平凡",
        zh="Y(G,C) 是平坦 G_ℂ-丛的模空间（= Hom(π₁(C),G_ℂ)/G_ℂ），复辛、典范丛平凡，复维数 2(g−1)dim G。",
        en="Y(G,C) = Hom(π₁(C),G_ℂ)/G_ℂ is complex symplectic with trivial canonical bundle, of complex dimension 2(g−1)dim G.",
        section="1",
        pages=[1, 1],
        anchor="§1 开头（Y(G,C) 的定义与复辛结构）",
        lean_name="Witten2008.Gaps.moduli_dim",
        lean_stmt="theorem moduli_dim (g d : ℤ) (hg : 2 ≤ g) :\n"
                  "    moduliDim g d = 2 * (g - 1) * d",
        imports=IMPORTS08_GAP,
        deps=[],
        hypotheses=["g ≥ 2；`moduliDim` 为占位定义（值为 0）"],
        scope="gap",
        bt="（缺口占位）亏格 g 曲面上平坦丛模空间的复维数是 2(g−1)dim G。",
        notes="缺口：mathlib 无 Hom(π₁(C),G_ℂ)/G_ℂ 模空间、无曲面基本群与表示簇；`moduliDim` 为占位 def。",
    ),
    dict(
        key="g02",
        title="缺口：A-模型与 B-模型的数据",
        zh="同一复辛流形 Y 上：B-模型 = (Y, 复结构, 平凡典范丛)；A-模型 = (Y, ω = Im Ω)。"
           "镜像对称把 (^LG 的) B-模型与 (G 的) A-模型配对。",
        en="B-model: (Y, complex structure, trivial canonical bundle); A-model: (Y, ω = Im Ω).",
        section="1",
        pages=[1, 2],
        anchor="§1（A-模型与 B-模型的定义）",
        lean_name="Witten2008.Gaps.a_b_model",
        lean_stmt="theorem a_b_model (G C : Type*) :\n"
                  "    Nonempty (aModelData (flatConnModuli G C) ≃ bModelData (flatConnModuli G C))",
        imports=IMPORTS08_GAP,
        deps=[],
        hypotheses=["`aModelData`/`bModelData`/`flatConnModuli` 均为占位定义"],
        scope="gap",
        bt="（缺口占位）同一个底流形上的 A-模型数据与 B-模型数据之间存在等价。",
        notes="缺口：mathlib 无超凯勒/复辛流形、无二维拓扑场论（A/B 模型）与镜像对称本身。",
    ),
    dict(
        key="g03",
        title="缺口：Hitchin 方程 (2.1)",
        zh="Hitchin 方程：F − φ∧φ = 0、Dφ = D⋆φ = 0，其中 φ 是 C 上取值于 ad(E) 的 1-形式，⋆ 由 C 的复结构决定。",
        en="Hitchin's equations: F − φ∧φ = 0 and Dφ = D⋆φ = 0.",
        section="2",
        pages=[2, 2],
        anchor="§2 式 (2.1)",
        lean_name="Witten2008.Gaps.hitchin_equations",
        lean_stmt="theorem hitchin_equations (F phi : Type*) :\n"
                  "    isHitchinSolution F phi",
        imports=IMPORTS08_GAP,
        deps=[],
        hypotheses=["`isHitchinSolution` 为占位定义（恒真）"],
        scope="gap",
        bt="（缺口占位）给定联络曲率与希格斯场，(F, φ) 满足 Hitchin 方程。",
        notes="缺口：mathlib 无黎曼面联络、Hodge 星、ad(E) 值 1-形式；连「方程」这一层的对象都不存在。",
    ),
    dict(
        key="g04",
        title="缺口：Hitchin 解 ↔ 复平坦联络 ↔ 半稳定希格斯丛",
        zh="Hitchin 方程的解有两种解释：A + iφ 是复平坦联络（给出 Y 的点）；(E,φ) 是半稳定希格斯丛，"
           "φ ∈ H⁰(C, K⊗ad E)（给出 M_H 在复结构 I 下的点）；M_H 超凯勒，Ω_I = ω_J + iω_K。",
        en="Solutions of Hitchin's equations correspond both to flat G_ℂ-connections and to semistable Higgs bundles (E,φ).",
        section="2",
        pages=[3, 3],
        anchor="§2（A+iφ 平坦 ↔ 希格斯丛；M_H 的超凯勒结构 Ω_I = ω_J + iω_K）",
        lean_name="Witten2008.Gaps.flat_iff_higgs",
        lean_stmt="theorem flat_iff_higgs (G C : Type*) :\n"
                  "    Nonempty (flatConnModuli G C ≃ higgsBundleModuli G C)",
        imports=IMPORTS08_GAP,
        deps=[],
        hypotheses=["`flatConnModuli`/`higgsBundleModuli` 为占位定义"],
        scope="gap",
        bt="（缺口占位）平坦丛模空间与希格斯丛模空间之间存在等价。",
        notes="缺口：同 G03；另缺希格斯丛、稳定性（GIT）与超凯勒商 Ω_I = ω_J + iω_K。",
    ),
    dict(
        key="g05",
        title="缺口：Hitchin 纤维化的底与一般纤维",
        zh="Hitchin 纤维化 π: M_H → B 把 (E,φ) 映到 φ 的特征多项式；dim_ℂ B = (g−1)dim G，"
           "一般纤维是复阿贝尔簇（或挠子）、对 Ω_I 拉格朗日，故 M_H 是完全可积系统。",
        en="The Hitchin fibration π: M_H → B has dim_ℂ B = (g−1)dim G; a generic fiber is a complex abelian variety (or torsor), Lagrangian for Ω_I.",
        section="3",
        pages=[3, 4],
        anchor="§3（Hitchin 纤维化与一般纤维是 special Lagrangian）",
        lean_name="Witten2008.Gaps.hitchin_base_dim",
        lean_stmt="theorem hitchin_base_dim (g d : ℤ) (hg : 2 ≤ g) :\n"
                  "    hitchinBaseDim g d = (g - 1) * d",
        imports=IMPORTS08_GAP,
        deps=[],
        hypotheses=["g ≥ 2；`hitchinBaseDim` 为占位定义"],
        scope="gap",
        bt="（缺口占位）Hitchin 底的复维数为 (g−1)dim G。",
        notes="缺口：无模空间、特征多项式映射、阿贝尔簇与 Lagrange 子流形。",
    ),
    dict(
        key="g06",
        title="缺口（本文主定理）：Hitchin 纤维化上的镜像对称",
        zh="M_H(^LG, C) 在复结构 J 下的 B-模型，镜像于 M_H(G, C) 配 ω = ω_K 的 A-模型；"
           "经 SYZ，对偶纤维化就是对偶群的 Hitchin 纤维化（纤维上作 T-对偶）。",
        en="The B-model of M_H(^LG,C) in complex structure J is mirror to the A-model of M_H(G,C) with ω_K.",
        section="3",
        pages=[4, 5],
        anchor="§3（主定理：mirror symmetry between Hitchin fibrations）",
        lean_name="Witten2008.Gaps.mirror_symmetry",
        lean_stmt="theorem mirror_symmetry (G C : Type*) :\n"
                  "    Nonempty (bModelData (higgsBundleModuli (langlandsDual G) C) ≃\n"
                  "      aModelData (higgsBundleModuli G C))",
        imports=IMPORTS08_GAP,
        deps=[],
        hypotheses=["`bModelData`/`aModelData`/`higgsBundleModuli`/`langlandsDual` 均为占位定义"],
        scope="gap",
        bt="（缺口占位）对偶群 Higgs 模空间的 B-模型与群 G 的 Higgs 模空间的 A-模型等价。",
        notes="缺口：同 G05；另缺 SYZ/T-对偶与镜像对称本身。这是全文主定理，恰好是 mathlib 缺口最深的一条。",
    ),
    dict(
        key="g07",
        title="缺口：tame ramification 的单值 exp(−2π(α−iγ))",
        zh="正则奇点（tame ramification）的留数 (α,γ) 决定绕 punctures 的单值 U = exp(−2π(α−iγ))；"
           "镜像侧参数按 (α,η) = (^Lη, −^Lα) 对应（Gukov–Witten）。",
        en="Around a regular singularity the monodromy is U = exp(−2π(α−iγ)); the mirror parameter map is (α,η) = (^Lη, −^Lα).",
        section="4",
        pages=[7, 7],
        anchor="§4 式 (4.3) 与 Remark 4.1",
        lean_name="Witten2008.Gaps.tame_monodromy",
        lean_stmt="theorem tame_monodromy (α γ : ℝ) :\n"
                  "    monodromyExp α γ = Complex.exp (-(2 * Real.pi) * (α - γ * Complex.I))",
        imports=IMPORTS08_GAP,
        deps=[],
        hypotheses=["α, γ 为实数；`monodromyExp` 为占位定义"],
        scope="gap",
        bt="（缺口占位）留数 (α,γ) 给出的单值等于 exp(−2π(α − iγ))。",
        notes="缺口：缺 𝔤 值留数、ad-作用下的矩阵指数与单值理论（mathlib 只有 `NormedSpace.exp` 的标量/赋范情形），"
              "缺 Gukov–Witten 的参数对偶。",
    ),
    dict(
        key="g08",
        title="缺口：wild ramification 与辫群 B(G) ≅ B(^LG)",
        zh="非正则奇点的扩展单值 = 普通单值 ⊕ Stokes 矩阵；Y(G,C;T_1,…,T_n) 复辛且与 T_2,…,T_n 无关；"
           "辫群 B(G) = π₁(𝔱^reg) 与 B(^LG) 自然同构，镜像对称与辫群作用交换。",
        en="Extended monodromy = monodromy + Stokes matrices; the braid groups B(G) and B(^LG) are naturally isomorphic.",
        section="5",
        pages=[8, 10],
        anchor="§5（Stokes 矩阵、等单值变形、辫群 B(G) ≅ B(^LG)）",
        lean_name="Witten2008.Gaps.braid_dual",
        lean_stmt="theorem braid_dual (G : Type*) :\n"
                  "    Nonempty (braidGroup G ≃ braidGroup (langlandsDual G))",
        imports=IMPORTS08_GAP,
        deps=[],
        hypotheses=["`braidGroup`/`langlandsDual` 为占位定义"],
        scope="gap",
        bt="（缺口占位）G 与对偶群的辫群之间存在等价。",
        notes="缺口：缺 Stokes 现象、等单值变形（Jimbo–Miwa–Ueno 1981）、辫群 π₁(𝔱^reg) 与其对偶同构。",
    ),
    dict(
        key="g09",
        title="缺口：四维提升与 Bun_G 无有限维整体商",
        zh="M = Σ×C 上四维扭转 N=4 规范理论低能给出二维 sigma 模型 Φ: Σ → M_H(G,C)；"
           "规范变换群为 Maps(Σ×C, G)。Bun_G(C) 不能写成有限维整体商 (Y, W_C)，故奇点处必须回到四维。",
        en="The 4d twisted theory reduces to a 2d sigma model on M_H; Bun_G(C) admits no finite-dimensional global quotient.",
        section="6",
        pages=[12, 13],
        anchor="§6（四维提升）与 §6.1（Bun_G 无有限维整体商）",
        lean_name="Witten2008.Gaps.four_dimensional_lift",
        lean_stmt="theorem four_dimensional_lift (Sig C G : Type*) :\n"
                  "    Nonempty (sigmaModelOn Sig C G ≃ fourDimGaugeTheory Sig C G)",
        imports=IMPORTS08_GAP,
        deps=[],
        hypotheses=["`sigmaModelOn`/`fourDimGaugeTheory` 为占位定义"],
        scope="gap",
        bt="（缺口占位）Σ×C 上的四维规范理论与 Σ 上取值的二维 sigma 模型给出同一物理。",
        notes="缺口：无四维规范理论/二维 sigma 模型的物理层形式化；Atiyah–Bott 1982 的「Bun_G 无整体商」亦缺。",
    ),
]


def batch15_entries():
    out = []
    for d in DATA15:
        e = dict(d)
        e["batch"] = "witten2015"
        gap = d["key"] in GAP_KEYS15
        e["lean_file"] = "Gaps.lean" if gap else "Statements.lean"
        e["status"] = "gap" if gap else "certified"
        e["sorry"] = 1 if gap else 0
        if gap:
            e["gaps"] = [dict(reason=d["notes"].split("缺口：", 1)[-1], blocked_by="mathlib 基础设施缺失")]
        else:
            e["gaps"] = []
        out.append(e)
    return out


def batch08_entries():
    out = []
    for d in DATA08:
        e = dict(d)
        e["batch"] = "witten2008"
        e["status"] = "gap" if d["scope"] == "gap" else "certified"
        e["lean_file"] = "Gaps.lean" if e["status"] == "gap" else "Statements.lean"
        e["sorry"] = 1 if e["status"] == "gap" else 0
        e["gaps"] = ([dict(reason=d["notes"].split("缺口：", 1)[-1], blocked_by="mathlib 基础设施缺失")]
                     if e["status"] == "gap" else [])
        out.append(e)
    return out


def batch77_entries():
    out = []
    for d in DATA77:
        e = dict(d)
        e["batch"] = "gno1977"
        e["status"] = "gap" if d["scope"] == "gap" else "certified"
        e["lean_file"] = "Gaps.lean" if e["status"] == "gap" else "Statements.lean"
        e["sorry"] = 1 if e["status"] == "gap" else 0
        e["gaps"] = ([dict(reason=d.get("gap_reason", d["notes"]), blocked_by="mathlib 基础设施缺失")]
                     if e["status"] == "gap" else [])
        out.append(e)
    return out


def entries():
    return batch15_entries() + batch08_entries() + batch77_entries()


def card_json(e):
    m = META[e["batch"]]
    return {
        "id": m["id_prefix"] + e["key"],
        "type": "statement",
        "title": e["title"],
        "track": m["track"],
        "source": {
            "paper": m["paper"],
            "arxiv": m["arxiv"],
            "section": e["section"],
            "pages": e["pages"],
            "anchor": e["anchor"],
        },
        "natural_language": {"zh": e["zh"], "en": e["en"]},
        "lean": {
            "file": m["lean_dir"] + "/" + e["lean_file"],
            "name": e["lean_name"],
            "statement": e["lean_stmt"],
            "imports": e["imports"],
        },
        "dependencies": e["deps"],
        "hypotheses": e["hypotheses"],
        "scope": e["scope"],
        "backtranslation": {
            "zh": e["bt"],
            "method": "blind-backtranslation",
            "reviewer": REVIEWER,
        },
        "verification": {
            "status": e["status"],
            "toolchain": LEAN_TOOLCHAIN,
            "lean_version": LEAN_VERSION,
            "mathlib_rev": MATHLIB_REV,
            "checked_at": CHECKED_AT,
            "checker": "lake env lean（逐文件）",
            "sorry_count": e["sorry"],
        },
        "gaps": e["gaps"],
        "notes": e["notes"],
        "rights": "rewritten",
        "status": "dev",
    }


def render_md(card, e):
    m = META[e["batch"]]
    lines = [
        "# " + card["title"],
        "",
        "- 卡号：`" + card["id"] + "`　轨道：" + m["track"] + "（" + m["paper"].split(",")[0] + "）"
        "　scope：`" + card["scope"] + "`　验证：**" + card["verification"]["status"] + "**",
        "- 来源：" + m["paper"] + "（" + m["arxiv"] + "）" + card["source"]["section"]
        + "，印刷页 " + str(card["source"]["pages"][0]) + "–" + str(card["source"]["pages"][1])
        + "（" + m["pages_note"] + "）",
        "",
        "## 原文陈述",
        "",
        "> " + e["zh"],
        "",
        "英文：" + e["en"],
        "",
        "## Lean 陈述",
        "",
        "```lean",
        card["lean"]["statement"],
        "```",
        "",
        "文件 `" + card["lean"]["file"] + "`，声明名 `" + card["lean"]["name"] + "`；imports："
        + "、".join("`" + i + "`" for i in card["lean"]["imports"]),
        "",
        "## 依赖",
        "",
    ]
    if card["dependencies"]:
        for dep in card["dependencies"]:
            lines.append("- `" + dep["name"] + "`（" + dep["kind"] + "，`" + dep["module"] + "`）")
    else:
        lines.append("- 仅用核心库/基础算术，无额外依赖（gap 卡另见「备注与缺口」）")
    lines += ["", "## 假设", ""]
    lines += ["- " + h for h in card["hypotheses"]]
    lines += [
        "",
        "## 盲验回译",
        "",
        "> " + card["backtranslation"]["zh"],
        "",
        "方法：" + card["backtranslation"]["method"] + "；验卡人：" + card["backtranslation"]["reviewer"] + "。",
        "",
        "## 备注与缺口",
        "",
        card["notes"],
        "",
        "验证环境：" + card["verification"]["toolchain"] + "，mathlib `" + card["verification"]["mathlib_rev"]
        + "`，检查日期 " + card["verification"]["checked_at"] + "，`sorry` 数 "
        + str(card["verification"]["sorry_count"]) + "。",
        "",
    ]
    return "\n".join(lines)


def build_readme():
    es = entries()
    n = len(es)
    n15 = sum(1 for e in es if e["batch"] == "witten2015")
    n08 = sum(1 for e in es if e["batch"] == "witten2008")
    c15 = sum(1 for e in es if e["batch"] == "witten2015" and e["status"] == "certified")
    c08 = sum(1 for e in es if e["batch"] == "witten2008" and e["status"] == "certified")
    n77 = sum(1 for e in es if e["batch"] == "gno1977")
    c77 = sum(1 for e in es if e["batch"] == "gno1977" and e["status"] == "certified")
    g15 = n15 - c15
    g08 = n08 - c08
    g77 = n77 - c77
    return """# leanstmt —— 自然语言陈述 ↔ Lean 陈述对照语料

研究级论文里的**陈述**（定义/命题/定理）与其 Lean 4 转写之间的逐条对照语料。
不做证明层：目标是把「这句数学话在 Lean 里到底写成什么」固定下来，并让每一条都
可被机器重放检查。

## 30 秒入口

| 想看什么 | 看哪里 |
| --- | --- |
| {n} 张卡的总览 | `MAP.md` |
| 字段规范 | `SCHEMA.md` |
| 一条卡长什么样 | `cards/statements/witten2008-s01.json`（及其 `md/` 渲染） |
| Lean 源码 | `lean/ShuyiFormal/Witten2015/{{Statements,Gaps}}.lean`、`lean/ShuyiFormal/Witten2008/{{Statements,Gaps}}.lean` |
| 验证怎么做 | `tools/check_lean.py`、`tools/lint_cards.py` |
| 这批是怎么做出来的 | `workflow/PRODUCTION.md` |
| 下一步找哪些文献、做哪些陈述 | `ROADMAP.md` |

## 两批范围（{n} 卡 = {cert} certified + {gap} gap）

**A 批：Witten 2015**（{n15} 卡，{c15} certified + {g15} gap）
底本 *More On Gauge Theory And Geometric Langlands*，arXiv:1506.04293v3（79 页；印刷页 = PDF 页 − 1）。
只取能落在现有 mathlib 上的离散/代数陈述。

**B 批：Witten 2008**（{n08} 卡，{c08} certified + {g08} gap）
底本 *Mirror Symmetry, Hitchin's Equations, and Langlands Duality*，arXiv:0802.0999v1（15 页；印刷页 = PDF 页）。
本文的主定理（Hitchin 纤维化上的镜像对称）恰好落在 mathlib 缺口最深的一层，
因此 B 批的 certified 卡只是若干离散/代数影子（中心 μ_N、有限 Pontryagin 对偶、
非正则奇点系数的伸缩律、函数空间 currying）。

**C 批：Goddard–Nuyts–Olive 1977**（{n77} 卡，{c77} certified + {g77} gap）
底本 *Gauge Theories and Magnetic Charge*，Nucl. Phys. B125 (1977) 1–28（CERN-TH-2255 影印本；无文字层，经 OCR）。
certified 卡是量子化条件与对偶群的离散影子（整数权、狄拉克量子化、中心元 N 次幂、对偶群同阶、
双对偶、Weyl 反射不变性）；磁权的根格/权格构造、GNO 主定理与附录 D 的具体表见 G01–G07。

- 轨道：`W15`（Witten 2015）、`W08`（Witten 2008）、`GNO77`（Goddard–Nuyts–Olive 1977）。
- scope 四值：`discrete-core`（有限群/单位根）、`algebraic-core`（对偶空间/维数/群中心）、
  `arithmetic-core`（维数账与 RH 推论）、`gap`（mathlib 缺口，`sorry` 占位）。
- certified 判据：`lake env lean` 对该文件 **0 error**、`sorry` 计数为 0、声明的 mathlib
  依赖用 `#check`/`lake env lean` 实证存在。
- gap 卡同样发布：缺口清单本身是交付物（`verification.jsonl` 与卡片 `gaps` 字段）。

## 验证环境（钉死）

| 项 | 值 |
| --- | --- |
| Lean | `leanprover/lean4:v4.36.0`（4.36.0, commit 611c117b） |
| mathlib | `d33c49ca43873d3746194325da62640cc893c9d9`（`master`） |
| 工作工程 | `C:\\\\Users\\\\admin\\\\Desktop\\\\数译发布\\\\shuyi\\\\formal`（`lakefile.lean` 里 `require mathlib ... @ "master"`） |
| 检查方式 | 逐文件 `lake env lean <file>`（**不在 LSP 里 import 全量 Mathlib**，见 `workflow/PRODUCTION.md` 事故记录） |

## 已知限制

1. {n} 条仍是试点，不是全量。A 批原文 §2.4–§5 的主体（Hitchin 模空间、谱曲线、本征膜）
   几乎全部落在 gap 卡里；B 批的主定理见 G06。
2. `arithmetic-core`/`algebraic-core` 的卡只固化代数恒等式或群论骨架，几何前提没有形式化，
   引用时须连带 gap 卡一起看，不能当成「Hitchin 系统已形式化」。
3. 盲验回译目前是单一 reviewer（subagent），不是双盲；`verification.status` 只到
   `certified`，还没有 `reviewed`/`expert-checked` 档。
4. 本语料**不进 mathlib**，只发布原文已有陈述的重述（`rights: rewritten`）。

## 质检

```bash
python tools/lint_cards.py cards --strict      # 字段/枚举/lean 名存在性/sorry 一致性
python tools/build_index.py                     # 生成 index.jsonl
python tools/render_md.py                       # 生成 md/
python tools/check_lean.py --project <formal 工程路径> --run   # 真跑 Lean（需要 elan）
```

## 版本

- v0.1（2026-11-19）：试点 12 卡（10 certified + 2 gap）、Lean 快照入库、工具与规范落地。
- v0.2（2026-11-19）：加入 Witten 2008 批 14 卡（5 certified + 9 gap）；轨道改为 `W15`/`W08`。
- v0.3（2026-11-19）：加入 GNO 1977 批 13 卡（6 certified + 7 gap），新增轨道 `GNO77`；
  原文为 CERN 扫描件（无文字层），经 OCR 重排后按节/式号抽取；合计 {n} 卡（{cert} certified + {gap} gap）。
""".format(n=n, cert=c15 + c08 + c77, gap=g15 + g08 + g77, n15=n15, n08=n08, n77=n77,
           c15=c15, c08=c08, c77=c77, g15=g15, g08=g08, g77=g77)


def build_schema():
    return """# leanstmt 卡 schema（v0.3）

一卡一 JSON，UTF-8、缩进 2 空格、`ensure_ascii=false`；字段顺序不强制，但下列字段必须有。

| 字段 | 类型 | 约束 |
| --- | --- | --- |
| `id` | string | `leanstmt/witten2015-<key>` / `leanstmt/witten2008-<key>` / `leanstmt/gno1977-<key>`，`<key>` 小写字母数字，全包唯一 |
| `type` | string | 固定 `"statement"` |
| `title` | string | 中文短标题，≤ 40 字 |
| `track` | string | `W15`（Witten 2015）/ `W08`（Witten 2008）/ `GNO77`（GNO 1977）；后续论文加新标签 |
| `source.paper` | string | 原题名 |
| `source.arxiv` | string | `arXiv:<id>v<版>`，版次必须写明 |
| `source.section` | string | 原文节号，如 `2.6.6`、`5`、`C`（附录） |
| `source.pages` | [int,int] | 原文页区间（闭区间）。Witten 2015：印刷页 = PDF 页 − 1；Witten 2008：印刷页 = PDF 页；GNO 1977：CERN 影印 PDF 页（页脚数字 OCR 不可靠，以节/式号为准） |
| `source.anchor` | string | 更细的锚（式号/定理名/段落），不许写「见正文」 |
| `natural_language.zh` | string | 译文的陈述句（一至两句，量词与假设写全） |
| `natural_language.en` | string | 英文原文的紧缩版（≤ 200 字符，只作对照） |
| `lean.file` | string | 相对本包根的 Lean 文件路径 |
| `lean.name` | string | 全限定声明名（`Namespace.name`），必须能在 `lean.file` 里 grep 到 |
| `lean.statement` | string | Lean 语句源码（可含换行），必须与文件中声明一致 |
| `lean.imports` | [string] | 该文件实际 import 的模块名（`Mathlib.X.Y`） |
| `dependencies[]` | [{name,module,kind}] | 用到的 mathlib/自有引理；`kind ∈ {mathlib,local}`；gap 卡可为空 |
| `hypotheses` | [string] | Lean 语句里显式/隐式假设的中文说明（空数组表示无） |
| `scope` | string | `discrete-core` / `algebraic-core` / `arithmetic-core` / `gap` |
| `backtranslation.zh` | string | 只读 Lean 语句写出的回译（不看中文陈述） |
| `backtranslation.method` | string | 固定 `"blind-backtranslation"` |
| `backtranslation.reviewer` | string | 回译者标识（`subagent`/人名）；写卡人不得同时是回译者 |
| `verification.status` | string | `certified`（0 error、`sorry_count=0`）或 `gap`（有 `sorry`） |
| `verification.toolchain` | string | `lean-toolchain` 内容 |
| `verification.mathlib_rev` | string | `lake-manifest.json` 里 mathlib 的 `rev`（40 位） |
| `verification.checked_at` | string | `YYYY-MM-DD` |
| `verification.checker` | string | 检查方式（如 `lake env lean（逐文件）`） |
| `verification.sorry_count` | int | 该声明所在文件里**本声明**引入的 `sorry` 数 |
| `gaps[]` | [{reason,blocked_by}] | `scope="gap"` 时至少 1 条；否则空数组 |
| `notes` | string | 写卡人备注：这一步形式化了什么、没形式化什么 |
| `rights` | string | 固定 `"rewritten"` |
| `status` | string | `draft` / `dev`（禁 `prod`/`train`） |

## 硬性纪律

1. **不虚标**：`verification.status` 只能由 `tools/check_lean.py --run` 的实测结果决定。
2. **不掺沙**：`lean.statement` 与源文件必须逐字一致（lint 会做归一化比对）。
3. **不越界**：只转写原文已有的陈述；不替作者补新命题、不改假设强弱；改写假设必须在
   `hypotheses` 与 `notes` 里写明「与原文的差异」。
4. **不留假名**：`dependencies` 里出现的一切名字，必须能用 `#check` 或 `lake env lean` 复现；
   查不到就删，不许写「大概在 mathlib 里」。
5. **缺口照登**：做不到的陈述不删，写 `gap` 卡并把缺什么写清楚；缺口卡数量按论文统计。
"""


def build_map():
    es = entries()
    rows = []
    for e in es:
        m = META[e["batch"]]
        label = m["track"] + "-" + e["key"].upper()
        rows.append("| " + label + " | " + e["title"].replace("|", "/") + " | " + e["scope"]
                    + " | " + e["status"] + " |")
    return """# leanstmt 地图（{n} 卡）

三条读法，按目的选一条。

## 路线 1：从原文到 Lean（想学「怎么转写」）

Witten 2015 §2.6.6 't Hooft 磁通 → W15-S01 → S02 → S03（有限群三步：有界、循环、挠）
→ §4.1/§7.1 本征值 → W15-S04 → S05（单位根两步：定义、计数）
→ §3.2 GNO 对偶 → W15-S06 → S07（双对偶、同秩）
→ Witten 2008 §2 对偶群 → W08-S01（中心 μ_N）→ §3 纤维 T-对偶 → W08-S02 → S03
→ §5 非正则奇点 → W08-S04（系数伸缩律）→ §6.1 四维提升 → W08-S05（currying）

## 路线 2：从 Lean 到原文（想核「这句 Lean 对不对」）

W15-S01–S05（`discrete-core`，只依赖 ZMod 与 RootsOfUnity 两个模块）
W15-S06–S07（`algebraic-core`，只依赖 Dual 与 Finrank）
W15-S08–S10（`arithmetic-core`，`ring` 级恒等式，几何前提在 G01/G02）
W08-S01（`algebraic-core`，SL(N,ℂ) 的中心，依赖 SpecialLinearGroup）
W08-S02–S03、S05（`discrete-core`，依赖 PontryaginDuality 与 Equiv.curry）
W08-S04（`algebraic-core`，复数幂的基础算术）
GNO77-S01–S06（`discrete-core`/`algebraic-core`，exp 周期 + 有限 Pontryagin 对偶）

## 路线 3：缺口清单（想知道「为什么这么多做不了」）

W15-G01 谱曲线亏格 → 缺曲线亏格/分歧除子/黎曼–胡尔维茨
W15-G02 Hitchin 纤维维数 → 缺 `Bun_G`/稳定性/辛结构
W08-G01 Y 的模空间 → 缺平坦丛模空间/表示簇/复辛流形
W08-G02 A/B 模型 → 缺超凯勒流形与二维拓扑场论
W08-G03 Hitchin 方程 → 缺黎曼面联络/Hodge 星/ad(E) 值 1-形式
W08-G04 解 ↔ 平坦联络 ↔ 希格斯丛 → 缺希格斯丛与稳定性（GIT）
W08-G05 Hitchin 纤维化 → 缺特征多项式映射/阿贝尔簇/Lagrange 子流形
W08-G06 主定理：镜像对称 → 缺 SYZ/T-对偶与镜像对称本身
W08-G07 tame ramification → 缺 𝔤 值留数与单值理论
W08-G08 wild ramification/辫群 → 缺 Stokes 现象、等单值变形、辫群
W08-G09 四维提升与栈 → 缺四维规范理论与 `Bun_G` 无整体商定理
GNO77-G01 对偶群构造 → 缺根数据的对偶层
GNO77-G02 磁权 = H^∨ 的权（主定理）→ 缺对偶表示论
GNO77-G03 Cartan 共轭（式 1.5）→ 缺紧 Lie 群的最大环面
GNO77-G04 π₂(G/H) ≅ π₁(H)（式 2.3）→ 缺同伦长正合列
GNO77-G05 单极解渐近行为 → 缺变分解的存在性/渐近分析
GNO77-G06 非半单 H（§6）→ 缺 U(1) 因子的对偶推广
GNO77-G07 附录 D 磁权表 → 缺 Dynkin 图/根数据表

## 卡片索引

| 卡 | 内容 | scope | 状态 |
| --- | --- | --- | --- |
{rows}
""".format(n=len(es), rows="\n".join(rows))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    cards_dir = os.path.join(ROOT, "cards", "statements")
    if not os.path.isdir(cards_dir):
        os.makedirs(cards_dir)

    es = entries()
    cards = [card_json(e) for e in es]
    files = []
    for card, e in zip(cards, es):
        p = os.path.join(cards_dir, card["id"].split("/", 1)[1] + ".json")
        files.append((p, json.dumps(card, ensure_ascii=False, indent=2) + "\n"))
        if e["batch"] == "witten2015":
            continue
        # 2008 批同时写一份 md 模板？不：md 由 render_md.py 统一生成
    files.append((os.path.join(ROOT, "README.md"), build_readme()))
    files.append((os.path.join(ROOT, "SCHEMA.md"), build_schema()))
    files.append((os.path.join(ROOT, "MAP.md"), build_map()))

    if args.check:
        bad = 0
        for p, content in files:
            if not os.path.isfile(p):
                print("MISSING " + p)
                bad += 1
            elif io.open(p, encoding="utf-8").read() != content:
                print("STALE " + p)
                bad += 1
        print("checked {0} files, {1} problem(s)".format(len(files), bad))
        return 1 if bad else 0

    for p, content in files:
        with io.open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
    print("wrote {0} files ({1} cards)".format(len(files), len(cards)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
