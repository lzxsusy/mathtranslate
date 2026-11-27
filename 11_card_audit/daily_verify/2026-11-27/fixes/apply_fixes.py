#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-27 修卡：按 11_card_audit/WORKFLOW.md §7.2 做字段级替换。

每条改动都带 before 断言；任何一个 before 不匹配就整体中止（不写盘）。
写盘时保持原文件的缩进与换行（CRLF/LF 由原文件决定），保证 diff 只落在目标字段。
改完自动回读 after，并写 fix_log.json。
"""
from __future__ import annotations

import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
LOG = HERE / "fix_log.json"

DELETED = object()


def load(path: Path):
    raw = io.open(path, encoding="utf-8", newline="").read()
    return raw, json.loads(raw)


def fmt(raw: str, data) -> str:
    nl = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.split(nl)
    indent = 2
    for line in lines[1:]:
        if line.strip():
            indent = len(line) - len(line.lstrip(" "))
            break
    return json.dumps(data, ensure_ascii=False, indent=indent).replace("\n", nl) + nl


def get(obj, field):
    cur = obj
    for k in field:
        cur = cur[k]
    return cur


def put(obj, field, value):
    cur = obj
    for k in field[:-1]:
        cur = cur[k]
    if value is DELETED:
        del cur[field[-1]]
    else:
        cur[field[-1]] = value


# ---------------------------------------------------------------- 编辑清单
EDITS = [
    # n1 siebert/correction/prop-3-12-lci —— (3.58) 在 p.50
    dict(
        path="datasets/siebert/cards/corrections/prop-3-12-lci.json",
        field=["pitfalls", 1],
        before="别把 lci 与光滑互换着用：讲义 p.51 起只为 lci 嵌入定义 Gysin 拉回 (3.58)(3.64)，而 Prop 3.12 的 $j_s^!$ 正需要这个工具；光滑只是充分条件。",
        after="别把 lci 与光滑互换着用：讲义 p.50–51 只为 lci 嵌入定义 Gysin 拉回（(3.58) 在 p.50，(3.64) 在 p.51），而 Prop 3.12 的 $j_s^!$ 正需要这个工具；光滑只是充分条件。",
        why="sources 页码错误：(3.58) 是 Definition 3.4，在讲义 p.50；p.51 只有 (3.64)。",
    ),
    # n3 gtgl15/concept/eigenbranes —— 定义被登记成 theorem
    dict(
        path="datasets/gtgl15/cards/concepts/eigenbranes.json",
        field=["theorems", 0],
        before={
            "name": "本征值空间的来源",
            "statement": "对线算符本征的膜，其“本征值”取值为有限维向量空间（Chan–Paton 空间）。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文 $\\S4.1$ 直接以定义形式给出 eq (4.3)，并说明“术语不好但物理上合理”；未从第一原理证明本征值必为向量空间。",
            },
            "source": "A p.37",
        },
        after=DELETED,
        why="层级错误：eq (4.3) 是定义（原文 §4.1），卡却把它放进 theorems 并标 proof.status=gap；内容与卡内 definition.text 重复。",
    ),
    # n4 kw06 —— eq (2.14) 在印刷 p.10
    dict(
        path="datasets/kw06/cards/concepts/n4-sym-theory.json",
        field=["theorems", 0, "source"],
        before="B p.7–11（eq (2.14) 在 p.11）",
        after="B p.7–10（eq (2.14) 在 p.10）",
        why="eq (2.14) 在 PDF 11（页脚「10」），即印刷 p.10；p.11 是 (2.15)。",
    ),
    # n5 functoriality —— (62) 在 p.27、(63) 在 p.28
    dict(
        path="datasets/functoriality/cards/concepts/strip-shrinking.json",
        field=["theorems", 0, "source"],
        before="原书 p.25 §3.5.2",
        after="原书 p.27 §3.5.2",
        why="§3.5.2 与 eq (62) 在印刷/PDF p.27（页脚 27），p.25 是 §3.5 的开头（(58) 附近）。",
    ),
    dict(
        path="datasets/functoriality/cards/concepts/strip-shrinking.json",
        field=["theorems", 1, "source"],
        before="原书 p.26 §3.5.2",
        after="原书 p.28 §3.5.2",
        why="[WW15, Theorem 5.1] 的推广段落在 p.28（页脚 28）。",
    ),
    # n6 ggl09 —— 左右边界 vs 小 S^2
    dict(
        path="datasets/ggl09/cards/derivations/descent-to-xi.json",
        field=["steps", 4, "text"],
        before="取 $S$ 为固定时刻的曲面，则 $x_i(S)$ 是作用在 $\\mathcal H$ 上的算符；在右边界 Dirichlet 处 $A,\\psi,\\sigma$ 全为零，$x_i=0$，非零贡献在 Neumann 边界与环绕 $w$ 的小 $S^2$ 之差；该差给出 $H^{2d_i-2}(N(\\rho))$ 中的 $x_i$，即杯积算符。",
        after="取 $S$ 为固定时刻的曲面，则 $x_i(S)$ 是作用在 $\\mathcal H$ 上的算符；右边界（Dirichlet）上 $A,\\psi,\\sigma$ 全为零，故该处 $x_i=0$；左边界（Neumann）与右边界之差同调于环绕 $w$ 的小 $S^2$，所以非零贡献来自左边界，且等于 $x_i$ 在小 $S^2$ 上的值，它给出 $H^{2d_i-2}(N(\\rho))$ 中的 $x_i$，即杯积算符。",
        why="原文 p.16–17 说差分的是「左(Neumann)与右(Dirichlet)边界」，该差同调于小 S²；卡写成「Neumann 与小 S² 之差」，而这个差正是 x_i=0 的右边界，方向反了。",
    ),
    # n12 siebert GW —— lci 而非连通
    dict(
        path="datasets/siebert/cards/concepts/gromov-witten-invariant.json",
        field=["pitfalls", 4],
        before="GW 不变量的形变不变性只在『连通基底 + 代数等价』的意义下成立（Prop 3.12），不是任意同调类扰动下不变。",
        after="GW 不变量的形变不变性只在『lci 基底 + 代数等价』的意义下成立（Prop 3.12），不是任意同调类扰动下不变；原文并不要求基底连通。",
        why="Prop 3.12 的假设是「If S is lci」；卡删掉 lci、换成「连通」，与卡 1 勘误「讲义原文也没有『同一连通分支』这一条」直接冲突。",
    ),
    # n13 lbook04 ch9 —— 极点位置
    dict(
        path="datasets/lbook04/cards/concepts/ch9-langlands-spectral.json",
        field=["key_points", 2],
        before="留数非零 $\\Rightarrow$ 存在 $\\mathrm{GL}_n(\\mathbb{A})$-不变配对 $\\Rightarrow$ $\\pi\\cong\\widetilde{\\pi}'\\otimes|\\det|^{i\\sigma}$；反过来该条件也保证 $s=1$ 处有极点（定理 4.2 后的两条观察）。",
        after="留数非零 $\\Rightarrow$ 存在 $\\mathrm{GL}_n(\\mathbb{A})$-不变配对 $\\Rightarrow$ $\\pi\\cong\\widetilde{\\pi}'\\otimes|\\det|^{i\\sigma}$；反过来该条件保证在 $s=-i\\sigma$ 与 $s=1-i\\sigma$ 处有单极点（$\\sigma=0$ 时即 $s=1$；定理 4.2 后的两条观察是未扭情形）。",
        why="Thm 4.2 给的是 s=−iσ 与 s=1−iσ 处的极点，只有 σ=0 才化为 s=1；后续两条 observation 是未扭（π×π̃）情形。",
    ),
    # n14 lbook04 ch3 —— §2.3 到 p.43
    dict(
        path="datasets/lbook04/cards/concepts/ch3-three-motives.json",
        field=["sources", 0, "pages"],
        before=[39, 40],
        after=[39, 43],
        why="definition 含 §2.3（从印刷 41 起、Example 2.1 在 42、G_k 在 43），pages 只到 40。",
    ),
    dict(
        path="datasets/lbook04/cards/concepts/ch3-three-motives.json",
        field=["sources", 0, "pdf_pages"],
        before=[46, 47],
        after=[46, 50],
        why="印刷 39–43 ↔ PDF 46–50（本章偏移 7）。",
    ),
    # n17 benzvi —— §2.1 无此内容
    dict(
        path="datasets/benzvi_glc/cards/concepts/categorical-fourier.json",
        field=["sources", 0, "section"],
        before="§2.1",
        after="§1.3",
        why="§2.1（p.8）是「范畴 ≈ Hilbert 空间」的类比，没有 FM 核公式；categorical Fourier 只在 §1.3（p.6）作 general theme 出现。",
    ),
    dict(
        path="datasets/benzvi_glc/cards/concepts/categorical-fourier.json",
        field=["sources", 0, "pages"],
        before=[8],
        after=[6],
        why="同上，locator 改到 p.6。",
    ),
    dict(
        path="datasets/benzvi_glc/cards/concepts/categorical-fourier.json",
        field=["sources", 0, "pdf_pages"],
        before=[8],
        after=[6],
        why="p.6 为 PDF 第 6 页（偏移 0）。",
    ),
    dict(
        path="datasets/benzvi_glc/cards/concepts/categorical-fourier.json",
        field=["sources", 0, "anchor"],
        before="arXiv:2605.23167 §2.1, p.8",
        after="arXiv:2605.23167 §1.3, p.6",
        why="同上。",
    ),
    dict(
        path="datasets/benzvi_glc/cards/concepts/categorical-fourier.json",
        field=["sources", 0, "page_note"],
        before=None,  # 新增字段：不存在
        after="原文只在 §1.3（p.6）以「general theme of categorical Fourier transforms」提到此类等价，未写出核公式 $FM_{\\mathcal K}(F)=p_{Y!}(p_X^*F\\otimes\\mathcal K)$；该公式按标准 Fourier–Mukai 变换给出。",
        why="让读者知道核公式不是原文逐字给的，避免把「出处」当成「逐字定义」。",
    ),
    # n19 gw06 —— 互换句在印刷 31
    dict(
        path="datasets/gw06/cards/concepts/two-dimensional-defect.json",
        field=["sources", 0, "pages"],
        before=[29, 30],
        after=[29, 31],
        why="α 与 η 在对偶下互换的句子在印刷 p.31（PDF 32），pages 少一页。",
    ),
    dict(
        path="datasets/gw06/cards/concepts/two-dimensional-defect.json",
        field=["sources", 0, "pdf_pages"],
        before=[30, 31],
        after=[30, 32],
        why="同上（本集 PDF = 印刷 + 1）。",
    ),
    dict(
        path="datasets/gw06/cards/concepts/two-dimensional-defect.json",
        field=["sources", 0, "page_note"],
        before="抛物子群、博雷尔子群与幂幺根（式 (2.57)–(2.63)），以及极大列维情形的离散 $\\alpha,\\eta$；印刷页 29–30，原文 PDF 第 30–31 页。",
        after="抛物子群、博雷尔子群与幂幺根（式 (2.57)–(2.63)），以及极大列维情形的离散 $\\alpha,\\eta$；印刷页 29–31，原文 PDF 第 30–32 页。",
        why="互换句在印刷 p.31，页码区间要覆盖到它。",
    ),
    # n20 glc —— 相对构造在印刷 72
    dict(
        path="datasets/glc/cards/concepts/fundamental-local-equivalence.json",
        field=["sources", 0, "pages"],
        before=[71],
        after=[71, 72],
        why="definition 末句的相对构造与 Op(X\\{x})^unr 定义在印刷 p.72，pages 只有 [71]。",
    ),
    dict(
        path="datasets/glc/cards/concepts/fundamental-local-equivalence.json",
        field=["sources", 0, "pdf_pages"],
        before=[71],
        after=[71, 72],
        why="本集 PDF = 印刷（偏移 0）。",
    ),
]


def main() -> int:
    by_file: dict[str, list[dict]] = {}
    for e in EDITS:
        by_file.setdefault(e["path"], []).append(e)

    log = []
    pending = []
    for rel, items in by_file.items():
        path = ROOT / rel
        raw, data = load(path)
        assert fmt(raw, data) == raw, f"格式无法无损往返：{rel}"
        changes = []
        for e in items:
            try:
                cur = get(data, e["field"])
                exists = True
            except (KeyError, IndexError):
                cur, exists = None, False
            e["_parent_len"] = len(get(data, e["field"][:-1])) if e["after"] is DELETED else None
            if e["before"] is None:
                assert not exists, f"字段已存在：{rel} {e['field']}"
            else:
                assert exists, f"字段不存在：{rel} {e['field']}"
                assert cur == e["before"], f"before 不匹配：{rel} {e['field']}\n  got={cur!r}"
            put(data, e["field"], e["after"])
            changes.append(
                {
                    "field": e["field"],
                    "before": e["before"],
                    "after": (None if e["after"] is DELETED else e["after"]),
                    "why": e["why"],
                }
            )
        out = fmt(raw, data)
        pending.append((rel, path, out, items, changes, data["id"]))
        log.append({"id": data["id"], "path": rel, "changes": changes})

    # 全部断言通过后才写盘
    if "--dry-run" in sys.argv:
        print(f"DRY-RUN OK: {len(pending)} files, {len(EDITS)} changes (未写盘)")
        return 0
    for rel, path, out, items, changes, _id in pending:
        io.open(path, "w", encoding="utf-8", newline="").write(out)
        _, again = load(path)
        for e in items:
            if e["after"] is DELETED:
                parent = get(again, e["field"][:-1])
                assert len(parent) == e["_parent_len"] - 1, f"删除后长度不对：{rel} {e['field']}"
            else:
                assert get(again, e["field"]) == e["after"], f"after 回读失败：{rel} {e['field']}"

    io.open(LOG, "w", encoding="utf-8", newline="\n").write(
        json.dumps(log, ensure_ascii=False, indent=2) + "\n"
    )
    print(f"OK: {len(by_file)} files, {len(EDITS)} changes -> {LOG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
