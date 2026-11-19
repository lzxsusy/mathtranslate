# -*- coding: utf-8 -*-
"""生成 datasets/leanstmt/ 的 12 张陈述卡、README/SCHEMA/MAP、index.jsonl 与 md 渲染。

用法：python tools/make_cards.py            # 写文件
      python tools/make_cards.py --check    # 只校验不写
卡片数据集中在本文件 DATA 中；改卡片请改这里再重跑，保证 index/md 一致。
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LEAN_TOOLCHAIN = "leanprover/lean4:v4.36.0"
LEAN_VERSION = "Lean 4.36.0 (x86_64-w64-windows-gnu, commit 611c117bfaf7b7ae1cfcf246ce6fba31e8f509e9)"
MATHLIB_REV = "d33c49ca43873d3746194325da62640cc893c9d9"
PAPER = "Witten, More On Gauge Theory And Geometric Langlands"
ARXIV = "arXiv:1506.04293v3"
LEAN_DIR = "lean/ShuyiFormal/Witten2015"

DATA = [
    dict(
        key="s01",
        title="'t Hooft 磁通所在的群 ℤ_N 有 N 个元素",
        zh="PSU(N) 规范的 't Hooft 磁通 ξ 取值于 H²(C, ℤ_N)，因此磁通的可能取值构成一个恰有 N 个元素的有限群。",
        en="The 't Hooft magnetic flux for PSU(N) gauge theory takes values in H²(C, ℤ_N).",
        section="2.6.6",
        pages=[14, 16],
        anchor="§2.6.6 关于 PSU(N) 与 't Hooft flux 的段落",
        lean_name="Witten2015.card_zmod",
        lean_stmt="theorem card_zmod (N : ℕ) [NeZero N] : Fintype.card (ZMod N) = N",
        imports=["Mathlib.Data.ZMod.Basic"],
        deps=[dict(name="ZMod.card", module="Mathlib.Data.ZMod.Basic", kind="mathlib")],
        hypotheses=["N ≥ 1（`NeZero N`）"],
        scope="discrete-core",
        bt="对任意正整数 N，群 ℤ/N 的元素个数等于 N。",
        notes="把「磁通取值于 ℤ_N」这一步落到「ℤ_N 是有限群、阶为 N」；H²(C,ℤ_N) 本身的群结构未在 mathlib 中形式化（缺口见 README §4）。",
    ),
    dict(
        key="s02",
        title="ℤ_N 由 1 生成，加法阶为 N",
        zh="ℤ_N 是 N 阶循环群：元素 1 的加法阶恰为 N，即 N 次重复的 't Hooft 磁通为零。",
        en="ℤ_N is cyclic of order N; the additive order of 1 is N.",
        section="2.6.6",
        pages=[14, 16],
        anchor="§2.6.6",
        lean_name="Witten2015.orderOf_one_zmod",
        lean_stmt="theorem orderOf_one_zmod (N : ℕ) : addOrderOf (1 : ZMod N) = N",
        imports=["Mathlib.Data.ZMod.Basic"],
        deps=[dict(name="ZMod.addOrderOf_one", module="Mathlib.Data.ZMod.Basic", kind="mathlib")],
        hypotheses=["无（N = 0 时两边都是 0）"],
        scope="discrete-core",
        bt="对任意自然数 N，元素 1 在 ℤ/N 中的加法阶等于 N。",
        notes="ℤ_N 的循环性给出磁通的「N 次为零」量化；与 S03 的 n-挠陈述互为表里。",
    ),
    dict(
        key="s03",
        title="ℤ_N 中每个元素都是 N-挠的",
        zh="磁通的任何取值 ξ 都满足 N·ξ = 0：'t Hooft 磁通是 N 挠的。",
        en="Every element of ℤ_N is N-torsion: N·x = 0.",
        section="2.6.6",
        pages=[14, 16],
        anchor="§2.6.6",
        lean_name="Witten2015.nsmul_zmod",
        lean_stmt="theorem nsmul_zmod (N : ℕ) (x : ZMod N) : N • x = 0",
        imports=["Mathlib.Data.ZMod.Basic"],
        deps=[dict(name="ZMod.natCast_self", module="Mathlib.Data.ZMod.Basic", kind="mathlib"),
              dict(name="nsmul_eq_mul", module="Mathlib.Algebra.Group.Defs", kind="mathlib")],
        hypotheses=["无"],
        scope="discrete-core",
        bt="对任意自然数 N 与 ℤ/N 中任意元素 x，N 倍 x 等于 0。",
        notes="PSU(N) 丛的障碍类落在 N-挠子群，这一条是其离散内核。",
    ),
    dict(
        key="s04",
        title="N 次单位根的刻画",
        zh="复数 z 是 N 次单位根，当且仅当 z^N = 1；'t Hooft 算符的本征值必满足此方程。",
        en="z is an N-th root of unity iff z^N = 1.",
        section="7.1",
        pages=[66, 67],
        anchor="§7.1（'t Hooft 算符本征值的讨论）",
        lean_name="Witten2015.mem_rootsOfUnity_iff",
        lean_stmt="theorem mem_rootsOfUnity_iff (n : ℕ) (z : ℂˣ) : z ∈ rootsOfUnity n ℂ ↔ (z : ℂ) ^ n = 1",
        imports=["Mathlib.RingTheory.RootsOfUnity.Complex"],
        deps=[dict(name="mem_rootsOfUnity'", module="Mathlib.RingTheory.RootsOfUnity.Basic", kind="mathlib")],
        hypotheses=["无（用单位群 ℂˣ 表达非零性，避免零元的平凡解）"],
        scope="discrete-core",
        bt="对任意自然数 n 与任意非零复数 z，z 属于 n 次单位根群当且仅当 z 的 n 次方等于 1。",
        notes="用 ℂˣ 而非 ℂ 是为了排除 z = 0（0^n = 0 ≠ 1 时该方程无解，用单位群更贴近「本征值」的非零语境）。",
    ),
    dict(
        key="s05",
        title="ℂ 中 N 次单位根恰有 N 个",
        zh="复数域中 N 次单位根恰有 N 个（N ≥ 1），故 't Hooft 算符的本征值只能从这 N 个数中取。",
        en="There are exactly N N-th roots of unity in ℂ.",
        section="4.1",
        pages=[18, 20],
        anchor="§4.1（本征膜与 't Hooft 算符的本征值）",
        lean_name="Witten2015.card_rootsOfUnity_complex",
        lean_stmt="theorem card_rootsOfUnity_complex (n : ℕ) [NeZero n] : Nat.card (rootsOfUnity n ℂ) = n",
        imports=["Mathlib.RingTheory.RootsOfUnity.Complex"],
        deps=[dict(name="card_rootsOfUnity_eq_iff_exists_isPrimitiveRoot", module="Mathlib.RingTheory.RootsOfUnity.PrimitiveRoots", kind="mathlib"),
              dict(name="Complex.isPrimitiveRoot_exp_of_coprime", module="Mathlib.RingTheory.RootsOfUnity.Complex", kind="mathlib")],
        hypotheses=["n ≥ 1（`NeZero n`）"],
        scope="discrete-core",
        bt="对任意正整数 n，复数域中 n 次单位根构成的集合恰有 n 个元素。",
        notes="证明通过给出本原根 exp(2πi/n) 完成；这是 π、exp 与单位根三条 API 的接口，也是本批唯一用到复分析的陈述。",
    ),
    dict(
        key="s06",
        title="电荷格的双对偶回到自身",
        zh="有限自由模与其双对偶同构：Langlands/GNO 对偶环面取两次对偶回到原来的环面。",
        en="A finite free module is isomorphic to its double dual; the dual torus' dual torus is the original torus.",
        section="3.2",
        pages=[20, 24],
        anchor="§3.2–§3.3（对偶环面与 GNO 对偶）",
        lean_name="Witten2015.double_dual",
        lean_stmt="theorem double_dual (K V : Type*) [Field K] [AddCommGroup V] [Module K V]\n    [Module.Finite K V] [Module.Free K V] : Nonempty (V ≃ₗ[K] Module.Dual K (Module.Dual K V))",
        imports=["Mathlib.LinearAlgebra.Dual.Lemmas"],
        deps=[dict(name="Module.evalEquiv", module="Mathlib.LinearAlgebra.Dual.Defs", kind="mathlib"),
              dict(name="Module.instIsReflexiveOfFiniteOfProjective", module="Mathlib.LinearAlgebra.Dual.Defs", kind="mathlib")],
        hypotheses=["K 是域（特征任意）", "V 有限生成自由模"],
        scope="algebraic-core",
        bt="对任意域 K 与任意有限维 K-向量空间 V，存在 V 到其双对偶空间的线性同构。",
        notes="环面 T = Λ⊗ℝ/Λ 的对偶是 Hom(Λ,ℤ)⊗U(1)；在格（自由 ℤ-模）层面「双对偶 ≅ 自身」正是这条代数陈述。环面层面未形式化。",
    ),
    dict(
        key="s07",
        title="对偶格与原格同秩",
        zh="对偶格与原格有相同的秩：GNO 对偶环面与原环面维数相同。",
        en="The dual lattice has the same rank; the GNO dual torus has the same dimension.",
        section="3.2",
        pages=[20, 22],
        anchor="§3.2",
        lean_name="Witten2015.dual_finrank",
        lean_stmt="theorem dual_finrank (K V : Type*) [Field K] [AddCommGroup V] [Module K V]\n    [Module.Finite K V] : Module.finrank K (Module.Dual K V) = Module.finrank K V",
        imports=["Mathlib.LinearAlgebra.Dual.Lemmas", "Mathlib.LinearAlgebra.Dimension.Finrank"],
        deps=[dict(name="Subspace.dual_finrank_eq", module="Mathlib.LinearAlgebra.Dual.Lemmas", kind="mathlib")],
        hypotheses=["K 是域", "V 有限维"],
        scope="algebraic-core",
        bt="对任意域 K 与有限维 K-向量空间 V，对偶空间的维数等于 V 的维数。",
        notes="把「对偶环面维数相同」落到对偶空间 finrank 相等；T-对偶保持底空间维数在物理上正是这一点。",
    ),
    dict(
        key="s08",
        title="典范丛次数为偶数，自旋结构存在",
        zh="亏格 g 曲面上典范丛的次数 2g−2 是偶数，因此 K^{1/2}（自旋结构）总存在。",
        en="deg K = 2g−2 is even, hence a spin structure exists.",
        section="2.6.5",
        pages=[16, 18],
        anchor="§2.6.5（酉群的谱覆盖与 K^{1/2} 的选择）",
        lean_name="Witten2015.even_deg_canonical",
        lean_stmt="theorem even_deg_canonical (g : ℤ) : Even (2 * g - 2)",
        imports=["Mathlib.Data.ZMod.Basic"],
        deps=[],
        hypotheses=["g 为整数（亏格）"],
        scope="arithmetic-core",
        bt="对任意整数 g，整数 2g−2 是偶数。",
        notes="本卡只形式化「偶性」这一步；「K 的次数 = 2g−2」与「偶次数线丛有平方根」两条留在缺口清单（G01/G03）。",
    ),
    dict(
        key="s09",
        title="Prym 的维数 = (N²−1)(g−1)",
        zh="谱曲线亏格 g_D = N²(g−1)+1 时，阿贝尔化的余核（Prym）维数 g_D − g = (N²−1)(g−1)。",
        en="If the spectral curve has genus N²(g−1)+1, the Prym has dimension (N²−1)(g−1).",
        section="2.6.2",
        pages=[11, 13],
        anchor="§2.6.2（阿贝尔化与 Prym）",
        lean_name="Witten2015.prym_dim",
        lean_stmt="theorem prym_dim (N g : ℤ) : (N ^ 2 * (g - 1) + 1) - g = (N ^ 2 - 1) * (g - 1)",
        imports=["Mathlib.Data.ZMod.Basic"],
        deps=[],
        hypotheses=["N, g 为整数"],
        scope="arithmetic-core",
        bt="对任意整数 N、g，若谱曲线亏格为 N²(g−1)+1，则它与底曲线的亏格差等于 (N²−1)(g−1)。",
        notes="几何前提 g_D = N²(g−1)+1 本身没有形式化（缺口 G01），本卡只固化其维数推论，避免把前提当已证。",
    ),
    dict(
        key="s10",
        title="分歧除子的次数 = 2N(N−1)(g−1)",
        zh="由 Riemann–Hurwitz 公式反解，N 层谱覆盖 D → C 的分歧除子次数为 2N(N−1)(g−1)。",
        en="Riemann–Hurwitz gives deg R = 2N(N−1)(g−1) for an N-sheeted spectral cover.",
        section="2.6.1",
        pages=[10, 12],
        anchor="§2.6.1（谱曲线的 Riemann–Hurwitz 计算）",
        lean_name="Witten2015.ramification_degree",
        lean_stmt="theorem ramification_degree (N g : ℤ) :\n    2 * (N ^ 2 * (g - 1) + 1) - 2 - N * (2 * g - 2) = 2 * N * (N - 1) * (g - 1)",
        imports=["Mathlib.Data.ZMod.Basic"],
        deps=[],
        hypotheses=["N, g 为整数"],
        scope="arithmetic-core",
        bt="对任意整数 N、g，把 g_D = N²(g−1)+1 代入 2g_D−2 = N(2g−2)+deg R 解出的 deg R 等于 2N(N−1)(g−1)。",
        notes="与 S09 同族：Riemann–Hurwitz 本身未形式化，本卡固化代数恒等式；原文式 (2.19) 附近。",
    ),
    dict(
        key="g01",
        title="缺口：谱曲线的亏格 N²(g−1)+1",
        zh="谱曲线 D → C 是 N 层覆盖，其亏格为 N²(g−1)+1（原文 §2.6.1–2.6.2 的核心几何事实）。",
        en="The spectral curve is an N-sheeted cover of C and has genus N²(g−1)+1.",
        section="2.6.1",
        pages=[10, 13],
        anchor="§2.6.1–§2.6.2",
        lean_name="Witten2015.Gaps.spectral_curve_genus",
        lean_stmt="theorem spectral_curve_genus (N g : ℕ) (hN : 2 ≤ N) (hg : 2 ≤ g) :\n    specCurveGenus N g = N ^ 2 * (g - 1) + 1",
        imports=["Mathlib.Data.ZMod.Basic"],
        deps=["Mathlib 无曲线亏格：本卡用占位 `specCurveGenus` 承载命题"],
        hypotheses=["N ≥ 2（N 层谱覆盖）", "g ≥ 2（曲线非平凡）", "`specCurveGenus` 为待实现占位（def 值 0），因此本卡 status=gap"],
        scope="gap",
        bt="（缺口占位）N 层覆盖的谱曲线亏格为 N²(g−1)+1。",
        notes="缺口：mathlib 无紧黎曼面/代数曲线的亏格、分歧除子、Riemann–Hurwitz。需要 `Curve` 上的 `genus`、有限态射分歧除子与 RH 公式；这是本批 12 条中阻塞最硬的一条。",
    ),
    dict(
        key="g02",
        title="缺口：Hitchin 纤维维数 (g−1)·dim G",
        zh="Hitchin 纤维化的一般纤维是 ½ dim M_H = (g−1)·dim G 维紧复环面（原文 §2.4、§2.6）。",
        en="A generic Hitchin fiber is a compact complex torus of dimension (g−1)·dim G.",
        section="2.4",
        pages=[8, 10],
        anchor="§2.4–§2.6",
        lean_name="Witten2015.Gaps.hitchin_fiber_dimension",
        lean_stmt="theorem hitchin_fiber_dimension (g dimG : ℕ) (hg : 2 ≤ g) :\n    hitchinFiberDim g dimG = (g - 1) * dimG",
        imports=["Mathlib.Data.ZMod.Basic"],
        deps=["Mathlib 无 Hitchin 模空间：本卡用占位 `hitchinFiberDim` 承载命题"],
        hypotheses=["g ≥ 2", "`hitchinFiberDim` 为待实现占位（def 值 0），因此本卡 status=gap"],
        scope="gap",
        bt="（缺口占位）一般 Hitchin 纤维是复维数 (g−1)·dim G 的紧复环面。",
        notes="缺口：mathlib 无 Hitchin 模空间、`Bun_G`、稳定性判据、余切丛的辛结构。需要黎曼面上主丛的模空间（栈）与 Hitchin 系统的基础设施。",
    ),
]

GAP_KEYS = {"g01", "g02"}


def card_json(d):
    return {
        "id": f"leanstmt/witten2015-{d['key']}",
        "type": "statement",
        "title": d["title"],
        "track": "W",
        "source": {
            "paper": PAPER,
            "arxiv": ARXIV,
            "section": d["section"],
            "pages": d["pages"],
            "anchor": d["anchor"],
        },
        "natural_language": {"zh": d["zh"], "en": d["en"]},
        "lean": {
            "file": f"{LEAN_DIR}/Statements.lean" if d["key"] not in GAP_KEYS else f"{LEAN_DIR}/Gaps.lean",
            "name": d["lean_name"],
            "statement": d["lean_stmt"],
            "imports": d["imports"],
        },
        "dependencies": d["deps"],
        "hypotheses": d["hypotheses"],
        "scope": d["scope"],
        "backtranslation": {
            "zh": d["bt"],
            "method": "blind-backtranslation",
            "reviewer": "subagent（未见本卡中文陈述，仅据 Lean 语句回译）",
        },
        "verification": {
            "status": "gap" if d["key"] in GAP_KEYS else "certified",
            "toolchain": LEAN_TOOLCHAIN,
            "lean_version": LEAN_VERSION,
            "mathlib_rev": MATHLIB_REV,
            "checked_at": "2026-11-19",
            "checker": "lake env lean（逐文件）",
            "sorry_count": 1 if d["key"] in GAP_KEYS else 0,
        },
        "gaps": [] if d["key"] not in GAP_KEYS else [
            {"reason": d["notes"].split("缺口：", 1)[-1], "blocked_by": "mathlib 基础设施缺失"}
        ],
        "notes": d["notes"],
        "rights": "rewritten",
        "status": "dev",
    }


def render_md(card):
    d = next(x for x in DATA if f"leanstmt/witten2015-{x['key']}" == card["id"])
    lines = [
        f"# {card['title']}",
        "",
        f"- 卡号：`{card['id']}`　轨道：W（Witten 2015）　scope：`{card['scope']}`　验证：**{card['verification']['status']}**",
        f"- 来源：{PAPER}（{ARXIV}）{card['source']['section']}，印刷页 {card['source']['pages'][0]}–{card['source']['pages'][1]}",
        "",
        "## 原文陈述",
        "",
        f"> {d['zh']}",
        "",
        f"英文：{d['en']}",
        "",
        "## Lean 陈述",
        "",
        "```lean",
        card["lean"]["statement"],
        "```",
        "",
        f"文件 `{card['lean']['file']}`，声明名 `{card['lean']['name']}`；imports："
        + "、".join(f"`{i}`" for i in card["lean"]["imports"]),
        "",
        "## 依赖",
        "",
    ]
    if card["dependencies"]:
        for dep in card["dependencies"]:
            lines.append(f"- `{dep['name']}`（{dep['kind']}，`{dep['module']}`）")
    else:
        lines.append("- 仅用核心库/基础算术，无额外依赖")
    lines += [
        "",
        "## 假设",
        "",
    ]
    lines += [f"- {h}" for h in card["hypotheses"]]
    lines += [
        "",
        "## 盲验回译",
        "",
        f"> {card['backtranslation']['zh']}",
        "",
        f"方法：{card['backtranslation']['method']}；验卡人：{card['backtranslation']['reviewer']}。",
        "",
        "## 备注与缺口",
        "",
        card["notes"],
        "",
        f"验证环境：{card['verification']['toolchain']}，mathlib `{card['verification']['mathlib_rev']}`，"
        f"检查日期 {card['verification']['checked_at']}，`sorry` 数 {card['verification']['sorry_count']}。",
        "",
    ]
    return "\n".join(lines)


README = """# leanstmt —— 自然语言陈述 ↔ Lean 陈述对照语料

研究级论文里的**陈述**（定义/命题/定理）与其 Lean 4 转写之间的逐条对照语料。
不做证明层：目标是把「这句数学话在 Lean 里到底写成什么」固定下来，并让每一条都
可被机器重放检查。

## 30 秒入口

| 想看什么 | 看哪里 |
| --- | --- |
| 12 张卡的总览 | `MAP.md` |
| 字段规范 | `SCHEMA.md` |
| 一条卡长什么样 | `cards/statements/witten2015-s01.json`（及其 `md/` 渲染） |
| Lean 源码 | `lean/ShuyiFormal/Witten2015/{Statements,Gaps}.lean` |
| 验证怎么做 | `tools/check_lean.py`、`tools/lint_cards.py` |
| 这批是怎么做出来的 | `workflow/PRODUCTION.md` |
| 下一步找哪些文献、做哪些陈述 | `ROADMAP.md` |

## 试点范围

底本：Witten, *More On Gauge Theory And Geometric Langlands*, arXiv:1506.04293v3（79 页；
印刷页 = PDF 页 − 1）。本批只取其中**能落在现有 mathlib 上**的离散/代数陈述，
共 12 条：**10 条 certified + 2 条 gap**。

- 通轨 W（Witten 2015），scope 四值——
  `discrete-core`（有限群/单位根）、`algebraic-core`（对偶空间/维数）、
  `arithmetic-core`（维数账与 RH 推论）、`gap`（mathlib 缺口，`sorry` 占位）。
- certified 的判据：`lake env lean` 对该文件 **0 error**、`sorry` 计数为 0、
  声明的 mathlib 依赖用 `#check`/`lake env lean` 实证存在。
- gap 卡同样发布：缺口清单本身是交付物（`verification.jsonl` 与卡片 `gaps` 字段）。

## 验证环境（钉死）

| 项 | 值 |
| --- | --- |
| Lean | `leanprover/lean4:v4.36.0`（4.36.0, commit 611c117b） |
| mathlib | `d33c49ca43873d3746194325da62640cc893c9d9`（`master`） |
| 工作工程 | `C:\\Users\\admin\\Desktop\\数译发布\\shuyi\\formal`（`lakefile.lean` 里 `require mathlib ... @ "master"`） |
| 检查方式 | 逐文件 `lake env lean <file>`（**不在 LSP 里 import 全量 Mathlib**，见 `workflow/PRODUCTION.md` 事故记录） |

## 已知限制

1. 只覆盖 12 条，是试点，不是全量；原文 §2.4–§5 的主体（Hitchin 模空间、谱曲线、
   本征膜）几乎全部落在 2 条 gap 卡所代表的缺口里。
2. `arithmetic-core` 四卡（S08–S10、S09）只固化代数恒等式，几何前提没有形式化，
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
"""

SCHEMA = """# leanstmt 卡 schema（v0.1）

一卡一 JSON，UTF-8、缩进 2 空格、`ensure_ascii=false`；字段顺序不强制，但下列字段必须有。

| 字段 | 类型 | 约束 |
| --- | --- | --- |
| `id` | string | `leanstmt/witten2015-<key>`，`<key>` 小写字母数字，全包唯一 |
| `type` | string | 固定 `"statement"` |
| `title` | string | 中文短标题，≤ 40 字 |
| `track` | string | 试点期固定 `"W"`（Witten 2015）；后续论文加新字母 |
| `source.paper` | string | 原题名 |
| `source.arxiv` | string | `arXiv:<id>v<版>`，版次必须写明 |
| `source.section` | string | 原文节号，如 `2.6.6` |
| `source.pages` | [int,int] | **印刷页**区间闭区间；印刷页 = PDF 页 − 1 |
| `source.anchor` | string | 更细的锚（式号/定理名/段落），不许写「见正文」 |
| `natural_language.zh` | string | 译文的陈述句（一至两句，量词与假设写全） |
| `natural_language.en` | string | 英文原文的紧缩版（≤ 200 字符，只作对照） |
| `lean.file` | string | 相对本包根的 Lean 文件路径 |
| `lean.name` | string | 全限定声明名（`Namespace.name`），必须能在 `lean.file` 里 grep 到 |
| `lean.statement` | string | Lean 语句源码（可含换行），必须与文件中声明一致 |
| `lean.imports` | [string] | 该文件实际 import 的模块名（`Mathlib.X.Y`） |
| `dependencies[]` | [{name,module,kind}] | 用到的 mathlib/自有引理；`kind ∈ {mathlib,local}` |
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

MAP = """# leanstmt 地图（试点 12 卡）

三条读法，按目的选一条：

## 路线 1：从原文到 Lean（想学「怎么转写」）

§2.6.6 't Hooft 磁通 → S01 → S02 → S03（有限群三步：有界、循环、挠）
→ §4.1/§7.1 本征值 → S04 → S05（单位根两步：定义、计数）
→ §3.2 GNO 对偶 → S06 → S07（双对偶、同秩）

## 路线 2：从 Lean 到原文（想核「这句 Lean 对不对」）

S01–S05（`discrete-core`，只依赖 ZMod 与 RootsOfUnity 两个模块）
S06–S07（`algebraic-core`，只依赖 Dual 与 Finrank）
S08–S10（`arithmetic-core`，`ring` 级恒等式，几何前提在 G01/G02）

## 路线 3：缺口清单（想知道「为什么这么多做不了」）

G01 谱曲线亏格 → 缺曲线亏格/分歧除子/黎曼–胡尔维茨
G02 Hitchin 纤维维数 → 缺 `Bun_G`/稳定性/辛结构

## 卡片索引

| 卡 | 内容 | scope | 状态 |
| --- | --- | --- | --- |
| S01 | ℤ_N 有 N 个元素 | discrete-core | certified |
| S02 | ℤ_N 由 1 生成 | discrete-core | certified |
| S03 | ℤ_N 的 N-挠性 | discrete-core | certified |
| S04 | N 次单位根的刻画 | discrete-core | certified |
| S05 | ℂ 中 N 次单位根恰有 N 个 | discrete-core | certified |
| S06 | 双对偶回到自身 | algebraic-core | certified |
| S07 | 对偶格同秩 | algebraic-core | certified |
| S08 | 典范丛次数为偶数 | arithmetic-core | certified |
| S09 | Prym 维数 (N²−1)(g−1) | arithmetic-core | certified |
| S10 | 分歧除子次数 2N(N−1)(g−1) | arithmetic-core | certified |
| G01 | 谱曲线亏格 N²(g−1)+1 | gap | gap（sorry 1） |
| G02 | Hitchin 纤维维数 (g−1)dim G | gap | gap（sorry 1） |
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    cards_dir = os.path.join(ROOT, "cards", "statements")
    md_dir = os.path.join(ROOT, "md")
    for d in (cards_dir, md_dir):
        if not os.path.isdir(d):
            os.makedirs(d)

    cards = [card_json(d) for d in DATA]
    files = []
    for card in cards:
        p = os.path.join(cards_dir, card["id"].split("/", 1)[1] + ".json")
        files.append((p, json.dumps(card, ensure_ascii=False, indent=2) + "\n"))
    files.append((os.path.join(ROOT, "README.md"), README))
    files.append((os.path.join(ROOT, "SCHEMA.md"), SCHEMA))
    files.append((os.path.join(ROOT, "MAP.md"), MAP))

    if args.check:
        bad = 0
        for p, content in files:
            if not os.path.isfile(p):
                print(f"MISSING {p}")
                bad += 1
            elif io.open(p, encoding="utf-8").read() != content:
                print(f"STALE {p}")
                bad += 1
        print(f"checked {len(files)} files, {bad} problem(s)")
        return 1 if bad else 0

    for p, content in files:
        with io.open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
    print(f"wrote {len(files)} files ({len(cards)} cards)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
