# -*- coding: utf-8 -*-
"""Emit 11_card_audit/glc_full/casebook/ from the settled fix_log.json.

One case per repaired card: 错误版 / 正确版 / 为什么错 / 证据 / 审计轨迹 /
形式化提示 / 防再犯, plus the directory README.md and index.json.

Run after `apply_fixes.py --apply` (needs fix_log.json) and after compare.json
exists (used only for the confirmation chain).  Never touches the frozen
11_card_audit/casebook/ archive of the previous 100-card campaign.
"""
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
AUDIT = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(AUDIT, "..", "..", ".."))
OUT = os.path.join(REPO, "11_card_audit", "glc_full", "casebook")

MODE = "页码/出处定位漂移"
MODE_RANGE = "页码范围遗漏"
MODE_TERM = "术语拼写"
MODE_INTERNAL = "内部不一致"
MODE_MATH = "数学断言过强"

META = {
    "gl1-trace-character": dict(
        mode=MODE,
        why="引理 1.1.4 排在 PDF p.7 页眉后第一行，而源码 `ch01.tex:109-110` 把 `\\srcpage{7}` "
            "放在 `\\end{lemma}` 之后，卡照抄了「原书 p.6」。",
        hint="校验 `theorems[].source` 的 `原书 p.N` 时，以 PDF 该页正文是否出现该陈述为准，"
             "`\\srcpage` 只作旁证；本卡 pitfalls 里另有指向 p.6 的 Frobenius 约定，不在修复范围。",
        guard="引理/定理编号在页脚出现时，页码取「陈述起始页」，不能取 `\\srcpage` 标记所在行。"),
    "affine-grassmannian": dict(
        mode=MODE_RANGE,
        why="卡引用的 anchor 自述「定义与扭曲积见 76-98 行」，其中 `L^+G_X/LG_X`、"
            "`Gr≃LG/L^+G`、`Bun^∞`、Hecke 扭曲积都落在 p.14，而 `sources.pages` 只写 [13]。",
        hint="`sources.pages` 必须覆盖 anchor 自述行范围所涉的全部印刷页；"
             "§2.4 的定理陈述确在 p.13，故正确值是 [13,14] 而非 [14]。",
        guard="anchor 里出现「…见 NN-MM 行」时，必须反查这些行的 `\\srcpage` 页并纳入 pages。"),
    "deligne-gl1-existence": dict(
        mode="符号/约定漂移（系数域）",
        why="卡把底域 `k=F_q` 当成了系数域来写 `Shv(Spec k)`；讲义 p.7 明写系数域是代数闭的 `e`，"
            "ℓ-进情形即 `Q̄_ℓ`（同页 Theorem 1.1.1 用 `Q_ℓ^×`）。",
        hint="形式化时把 base field 与 coefficient field 分成两个参数；`Shv(Spec k)` 的系数域"
             "由 sheaf theory 的 `e` 决定，不由 `Spec k` 决定。",
        guard="出现 `Shv(Spec k)`／`k-向量空间` 时，先确认 k 是底域还是系数域。"),
    "local-whittaker-eigenfunction": dict(
        mode="边界情形（不等式取等）",
        why="优势权含边界点：`λ=(c,0,…,0)` 时 `Σ_i(i-1)λ_i = 0`，Casselman–Shalika 指数是 0 不是负。",
        hint="`n(λ)=Σ(i-1)λ_i ≥ 0` 只在 `λ` 不是 `(c,0,…,0)` 型时才严格为正；"
             "形式化时把「有效优势权」细分为 `n(λ)>0` 与非零两项两种情形。",
        guard="「指数为负」类断言必须检查 Σ 型泛函为 0 的边界。"),
    "b-lambda-ic": dict(
        mode=MODE_TERM,
        why="人名拼写错误：讲义与中译全篇都写 `Casselman–Shalika`（如 `glc.txt:488`、"
            "`ch03.tex:68`），卡写成 `Casselman–Shalala`。",
        hint="人名类术语在形式化时不参与语义，但会污染检索与交叉引用；应作为词表项统一。",
        guard="术语表锁定 `Casselman–Shalika`；全文检索 `Shalala` 必须为 0。"),
    "local-laumon-formula": dict(
        mode=MODE_TERM,
        why="同 b-lambda-ic：`Casselman–Shalala` 应为 `Casselman–Shalika`，本卡 4 处"
            "（definition、key_points、proof.steps、gap_note）。",
        hint="同一错误在多个段落重复时，逐处修但只记一个失效模式；修完 grep 全卡计数应为 0。",
        guard="术语表统一；提交前对易错人名（Shalika、Drinfeld、Beilinson）做一次词表比对。"),
    "fourier-deligne-transform": dict(
        mode=MODE_INTERNAL,
        why="`proof.steps[2].why` 仍保留「（至多差平移）」这一旧措辞，与本步 text「单靠 t-正合不足」"
            "及 key_points[2]「等价加 t-正合才保持单对象，且不产生平移」矛盾；README 的 2026-11-18 "
            "修订也明令「删去平移」。",
        hint="`t`-正合只给「单对象至多差平移」；要「保持单对象」必须再加范畴等价。"
             "形式化时把这两条作为两个独立引理。",
        guard="修订记录写「删去 X」时，必须全局 grep X；proof 的 why 是最容易漏的字段。"),
    "vanishing-theorem": dict(
        mode="逻辑条件反转（放宽方向）",
        why="卡称一般形式「不再要求 k<n 且 E 几何不可约」，但讲义 p.36 的一般形式前提是 "
            "`rank(E)>k`——这正是 `k<n`（`n=rank(E)`），而且没有去掉 `E` 几何不可约。",
        hint="形式化：`rank(E)>k ↔ k<n`。所谓「放宽」只放宽了下界估计的常数形式"
             "（`nk(2g-2)` → `(2g-2)k·rank(E)`），不是放宽前提集合。",
        guard="凡写「更一般/放宽」，逐条对照前提列表，确认没有把原前提偷偷保留或删除。"),
    "base-whittaker-sheaf": dict(
        mode="适用范围（限制 vs 茎）",
        why="summary 说 `q_!j_{k,!}F_k` 是 `Av_E^d(W_k)` 的茎，但同卡 definition/定理/key_points[2]"
            "与 `ch06.tex:69` 都写成限制到 `C_k^{tor=0}` 的层；茎（stalk）是逐点取纤维，限制是"
            "取子叠上的截面，二者不同。",
        hint="形式化时 `Av^d_E(W_k)|_{C_k^{tor=0}}` 与 `(Av^d_E(W_k))_x` 类型不同；"
             "summary 必须复用 definition 的表达式。",
        guard="summary 中出现的对象必须是 definition 中已定义的同一个表达式，不能换一种说法。"),
    "torsion-stack-local-model": dict(
        mode=MODE,
        why="`Tor^d ≃ gl_d/GL_d` 的矩阵模型在 p.42 末三行；p.43 首段已转入 `d=d1+d2` 的抛物对应。",
        hint="该卡定理陈述与证明同页跨段，`sources.pages` 应取 [42,43] 以覆盖 p.42 的模型与 p.43 的证明。",
        guard="`§7.4 证明` 的页码以证明起始页为准，并检查是否跨页。"),
    "euler-characteristic-trace-test": dict(
        mode=MODE_RANGE,
        why="`χ_K(y):=Σ(-1)^i dim H^i(K_ȳ)` 的定义在 p.44 末尾，p.45 首行才接"
            "「for the Euler characteristic of the stalk」与判据；卡只写 [45]。",
        hint="兄弟卡 descent-projective-bundle 对同一段已写 [44,45]；同章卡之间应保持一致。",
        guard="定义句与判据句跨页时，pages 取并集；与兄弟卡比对同一段落的页码。"),
    "hecke-laumon-eigensheaf": dict(
        mode=MODE_RANGE,
        why="定义式 `α_d: HL^d_k(K) → L^d_E ⊠ K` 在 p.45 末尾，p.46 首行才接归一化与相容性；"
            "卡只写 [46]。",
        hint="`α_d` 的 d≥0 家族与 d=0 归一化分居两页，pages 应为 [45,46]。",
        guard="公式与其归一化条件分居两页时，pages 取并集。"),
    "hecke-laumon-stack": dict(
        mode=MODE_MATH,
        why="短正合列 `0→M'→M→T→0` 中，`(M',T)` 一般不能决定 `M`：扩充由 "
            "`Ext^1(T,M')≅⊕_x((T_x)^∨⊗M'_x)` 参数化；同卡 pitfalls[1] 已自述"
            "「忘记 M' 会丢掉子层信息，无法还原 M」，key_points[0] 却说「三者互相决定其中之二」，自相矛盾。",
        hint="形式化时把「短正合列」建成 `Ext^1(T,M')`-torsor，而不是三元组的一一对应；"
             "只有 `(M',M)` 与 `(M,T)` 能直接互相读出。",
        guard="出现「互相决定」字样时，检查是否隐含 `Ext^1=0` 或分裂性假设。"),
    "perverse-quotient-lemma": dict(
        mode="summary 漏前提",
        why="summary 只写 `π_*K` 反常，漏掉 `π_!K` 反常；同卡 definition/theorem/pitfalls[1] "
            "都要求两者同时成立（p.47：`π! K, π∗ K ∈ Perv(B)`）。",
        hint="形式化时引理前提是合取 `π_!K ∈ Perv(B) ∧ π_*K ∈ Perv(B)`；summary 必须写成合取。",
        guard="summary 与 theorem.statement 的前提集合必须逐项对齐。"),
    "restricted-local-systems": dict(
        mode=MODE_INTERNAL + "（verification 陈旧残留）",
        why="卡正文已于 2026-11-18 按 AGK20a §0.5.4 改成「IndLisse 的左完备化」，但 "
            "`verification.checks[1]` 仍写「卡中 definition.notation 与此冲突 → P1，alignment=error」；"
            "核验块与正文自相矛盾。",
        hint="verification 是历史核验记录，也必须随正文修订同步，否则会误导下一次审计。",
        guard="修改 definition/theorem 后，检查 verification 中是否还有「与此冲突」「error」等旧判词。"),
    "scheme-of-singularities": dict(
        mode=MODE,
        why="`Coh_0(Y)≃Perf(Y), IndCoh_0(Y)≃QCoh(Y)` 的等价陈述在 p.53 末段；`ch10.tex:42` 才"
            "`\\srcpage{54}`，卡把 theorem.source 写成 p.54。",
        hint="pages [53,54] 本身没错（k-线性支撑横跨两页），只需把定理出处改成陈述所在 p.53。",
        guard="`theorems[].source` 的页码取陈述句所在页，不取 `\\srcpage` 下一行。"),
    "shv-nilpotent-support": dict(
        mode=MODE_RANGE,
        why="§11.6 末段（分层控制）在 p.60 页眉后首段；p.59 以「Third, it is not too large…」结束，"
            "而 `ch11.tex` 全文没有 `\\srcpage{60}`，卡只写到 [58,59]。",
        hint="中译 ch11 缺 p.60 标记属源码缺陷；页码应以 PDF p.60 正文为准补上。",
        guard="`\\srcpage` 缺页时以 PDF 页眉为准；末段/首段跨页要读下一页首行。"),
    "frobenius-twisted-trace": dict(
        mode=MODE_RANGE,
        why="命题后半句（取全局截面恢复自守迹空间）在 p.64 首段；`ch12.tex` 无 `\\srcpage{64}`，"
            "卡只写 [63]。",
        hint="该卡是 git 基线里已有的未提交改动（游走→巡游），修 pages 不碰那处措辞。",
        guard="修卡前先 `git diff` 看该卡是否已有他人未提交改动，避免覆盖。"),
    "restricted-categorical-langlands": dict(
        mode="页码范围过宽",
        why="§12.6 整节在 p.63；p.62 末仍是 §12.5 末句，卡却把 pages 写成 [62,63] 并把定理出处"
            "写成 p.62–63（`ch12.tex` 的 `\\srcpage{63}` 落在 :117 的 note 句中，造成误判）。",
        hint="只有陈述完全落在 p.63 时才能把 pages 收窄为 [63]；先读 p.62 末行确认。",
        guard="收窄页码前确认上一页末行不属于本节；`\\srcpage` 在段落中间时不可信。"),
    "whittaker-coefficient": dict(
        mode=MODE,
        why="`coeff(F):=C_{dR,c}(Bun^Ω_N, p^!(F)⊗ψ^!(exp))` 的定义在 p.64，卡 pages [64] 正确；"
            "但「经由到温和商的投影分解」这一基本事实在 p.65，theorem.source 误写 p.64。",
        hint="定义与基本事实分居两页时，pages 覆盖定义页即可，但 theorem.source 必须指向陈述页。",
        guard="`theorems[].source` 指向的是定理/事实的陈述页，不是定义页。"),
    "aut-sigma-module": dict(
        mode=MODE,
        why="§14.5 与 Theorem 14.5.1 都在 p.71（p.70 只有 §14.4 与对 14.5.1 的引用）；卡只写 [70]。",
        hint="章内小节跨页时，`sources.pages` 取本节标题与定理所在页。",
        guard="小节标题页与定理页不一致时，pages 取定理页。"),
    "drinfeld-sokolov-gauge": dict(
        mode=MODE,
        why="§14.2「局部正规形」在 p.69；p.68 只有 §14.1 与 Hitchin 底。",
        hint="定理出处与 sources.pages 同步；本卡 gap_note 只写「§14.2」不含页码，无需改。",
        guard="小节号与页码必须自洽：小节首次出现页 = pages 起点。"),
    "hitchin-base": dict(
        mode=MODE_RANGE,
        why="`c_{Ĝ,Ω}≃⊕_i Ω_X^{d_i+1}` 与 `Hitch_Ĝ(X):=Γ(X,c_{Ĝ,Ω})` 在 p.68；卡写 [67]。",
        hint="章首（p.67）给出背景，Hitchin 底的定义在 p.68，pages 应为 [67,68]。",
        guard="章首卡：pages 至少覆盖定义/陈述页，不能只写章首页。"),
    "quantum-local-langlands": dict(
        mode=MODE,
        why="§15.4 标题在 `ch15.tex:65`，但 `\\srcpage{74}` 在 :77；PDF p.74 L11 才是 "
            "`15.4. Relation with quantum local Langlands.`，卡却写 p.73。",
        hint="`\\srcpage` 与标题行分离时，以 PDF 标题页为准；本卡其余内容（水平 κ）与 2026-11-18 修订一致。",
        guard="§ 标题所在页用 PDF 页眉核对，不用 `\\srcpage` 行号推算。"),
    "unramified-oper": dict(
        mode=MODE_RANGE,
        why="anchor `ch15.tex:28-33` 跨 p.72-73：`η∈ĝ[[t]]dt`、缺陷度量 `λ̌`、`Op^unr=⊔Op^{reg,λ̌}` "
            "与形式片包含都在 p.73，卡只写 [72]。",
        hint="参数化定义跨页时 pages 取并集；本卡 summary 同时用到 p.72 的朴素定义与 p.73 的缺陷分层。",
        guard="anchor 行范围跨 `\\srcpage` 时，pages 必须包含两端。"),
    "eisenstein-compatibility": dict(
        mode=MODE,
        why="图表 (16.1) 整幅在 p.77；p.76 §16.2 只有文字，卡把 theorem.source 写成 p.76。",
        hint="图表类对象的页码取整幅所在页；sources.pages 已含 76,77，只需改 theorem.source。",
        guard="theorem.source 指向图表时，页码取图表所在页而非小节起页。"),
    "global-langlands-functor": dict(
        mode=MODE,
        why="第 16 章起于 p.76（PDF p.76 页眉），`ch16.tex:12` 的 `\\srcpage{76}` 正确；"
            "但 `ch16.tex:2` 注释「原PDF第75页」错，卡照抄成 p.75。",
        hint="源码注释与 `\\srcpage` 冲突时以 PDF 正文为准；本卡数学内容（`L_G^0=Ψ∘L_G` 的"
             "提升方向、QCoh^! 重整化）正确，只改页码。",
        guard="章起页以 PDF 页眉为准，源码开头的「原PDF第 N 页」注释只作线索。"),
}


def fmt_value(v):
    if isinstance(v, list):
        return "[" + ", ".join(str(x) for x in v) + "]"
    return str(v)


def main():
    with io.open(os.path.join(AUDIT, "fix_log.json"), encoding="utf-8") as fh:
        log = json.load(fh)
    with io.open(os.path.join(AUDIT, "sample_inventory.json"), encoding="utf-8") as fh:
        inv = json.load(fh)
    title = {c["id"]: c["title"] for c in inv["cards"]}

    os.makedirs(OUT, exist_ok=True)
    entries = []
    for n, fx in enumerate(log["fixes"], 1):
        slug = fx["id"].split("/")[-1]
        meta = META[slug]
        lines = []
        lines.append("# %02d %s" % (n, title.get(fx["id"], slug)))
        lines.append("")
        lines.append("- 卡片：`%s`" % fx["id"])
        lines.append("- 失效模式：%s" % meta["mode"])
        lines.append("- 严重度：%s" % fx["severity"])
        lines.append("- 确认链：%s" % fx["confirmed_by"])
        lines.append("- 修复字段：%s" % "、".join("`%s`" % e["field"] for e in fx["edits"]))
        lines.append("")
        lines.append("## 错误版")
        lines.append("")
        for e in fx["edits"]:
            lines.append("- `%s`：%s" % (e["field"], fmt_value(e["before"])))
        lines.append("")
        lines.append("## 正确版")
        lines.append("")
        for e in fx["edits"]:
            lines.append("- `%s`：%s" % (e["field"], fmt_value(e["after"])))
        lines.append("")
        lines.append("## 为什么错")
        lines.append("")
        lines.append(meta["why"])
        lines.append("")
        lines.append("## 证据")
        lines.append("")
        for ev in fx.get("evidence", []):
            lines.append("- " + ev)
        lines.append("")
        lines.append("## 审计轨迹")
        lines.append("")
        lines.append("- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）")
        lines.append("- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）")
        lines.append("- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`")
        lines.append("- 本卡修复 %d 处，JSON 变更 %d 行；md 镜像同步 %d 处"
                     % (len(fx["edits"]), fx["json_text_changed_lines"],
                        len(fx["md_sync"]["edits"])))
        lines.append("")
        lines.append("## 形式化提示")
        lines.append("")
        lines.append(meta["hint"])
        lines.append("")
        lines.append("## 防再犯")
        lines.append("")
        lines.append(meta["guard"])
        lines.append("")

        fname = "%02d-%s.md" % (n, slug)
        with io.open(os.path.join(OUT, fname), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(lines))
        entries.append({
            "n": n,
            "slug": slug,
            "id": fx["id"],
            "title": title.get(fx["id"], ""),
            "mode": meta["mode"],
            "severity": fx["severity"],
            "fields": [e["field"] for e in fx["edits"]],
            "confirmed_by": fx["confirmed_by"],
            "file": "casebook/" + fname,
        })

    with io.open(os.path.join(OUT, "..", "index.json"), "w",
                 encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps({
            "campaign": "glc_full_2026-11-26",
            "note": "本批 154 张 glc 卡全量审计的案例集；与 11_card_audit/casebook/ 的 32 例（上一批 100 卡）相互独立",
            "n_cases": len(entries),
            "cases": entries,
        }, ensure_ascii=False, indent=2) + "\n")

    readme = [
        "# GLC 全量审计案例集（2026-11-26）",
        "",
        "本目录是 `datasets/glc/cards` 154 张 concept 卡**全量双盲审计**中确认修复的案例归档。",
        "与 `11_card_audit/casebook/`（上一批 100 卡审计的 32 例，已冻结）相互独立，不修改它。",
        "",
        "## 目录",
        "",
        "每张修过的卡一例，文件名 `<序号>-<slug>.md`，含七节：",
        "错误版 / 正确版 / 为什么错 / 证据 / 审计轨迹 / 形式化提示 / 防再犯。",
        "`../index.json` 是索引；`../README.md` 与 `../TRACE.md` 记录方法与时间线。",
        "",
        "## 收录口径",
        "",
        "只有同时满足以下条件的卡才有一例：",
        "",
        "1. Pass A 与 Pass B 两名互盲审计员都判 issue（`both_issue`）；或单方判 issue 后",
        "   第三名 arbiter 盲审也判 issue；",
        "2. lead 逐条复核证据成立（E1 一手来源或卡内自相矛盾）；",
        "3. 已按 `fix_log.json` 做字段级最小修复，且 md 镜像同步。",
        "",
        "单方发现但未获第二判断认可的，不进本目录，只记入审计目录的 `report.md` 残余风险。",
    ]
    with io.open(os.path.join(OUT, "README.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(readme) + "\n")
    print("wrote %d cases + index.json + README.md to %s" % (len(entries), OUT))


if __name__ == "__main__":
    main()
