#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""draft_cards.py —— 从解经本语料生成 kw06 资料卡的初稿（之后再人工/agent 补写）。

输入（只读，不入仓）：
  ../../../../witten-exegesis/papers/WIT-0604151-EMDGL/derivation/*.jsonl
输出：
  cards/concepts/*.json    概念卡初稿（definition/key_points/related 已填，formulas/theorems/pitfalls 留空）
  cards/derivations/*.json 推导卡初稿（goal/setup/steps 已填，gaps/pitfalls 留空）

用法：python tools/draft_cards.py --src <derivation 目录>
注意：初稿 status 一律 draft，且 summary 里带「（初稿）」标记，便于 lint 区分。
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"

# ---- 概念卡选目：40 个核心概念，按 track 分组 ----
CONCEPTS = [
    # A 四维物理与对偶
    ("A", "C-N4", "n4-sym-theory"),
    ("A", "C-SDUAL", "s-duality"),
    ("A", "C-EMDUAL", "electromagnetic-duality"),
    ("A", "C-GNO", "gno-dual-group"),
    ("A", "C-LG", "langlands-dual-group"),
    ("A", "C-THETA", "theta-angle"),
    ("A", "C-SC", "supercharge"),
    ("A", "C-BPS", "bps-state"),
    # B 扭化与拓扑
    ("B", "C-TWIST", "topological-twist"),
    ("B", "C-TQFT", "topological-qft"),
    ("B", "C-BRST", "brst-operator"),
    ("B", "C-COHOM", "cohomology"),
    ("B", "C-INST", "instanton"),
    ("B", "C-RSYM", "r-symmetry"),
    # C 舞台
    ("C", "C-RS", "riemann-surface"),
    ("C", "C-HIGGSB", "higgs-bundle"),
    ("C", "C-HIGGSF", "higgs-field"),
    ("C", "C-MH", "hitchin-moduli"),
    ("C", "C-HK", "hyperkahler-manifold"),
    ("C", "C-HKQ", "hyperkahler-quotient"),
    ("C", "C-MMAP", "moment-map"),
    ("C", "C-CPLX", "complex-structure"),
    ("C", "C-HFIB", "hitchin-fibration"),
    ("C", "C-INTEG", "integrable-system"),
    # D 二维、膜与算子
    ("D", "C-AMODEL", "a-model"),
    ("D", "C-BMODEL", "b-model"),
    ("D", "C-MIRROR", "mirror-symmetry"),
    ("D", "C-ABRANE", "a-brane"),
    ("D", "C-BBRANE", "b-brane"),
    ("D", "C-WILSON", "wilson-operator"),
    ("D", "C-THOOFT", "thooft-operator"),
    ("D", "C-EIGEN", "eigenbrane"),
    # E Langlands 与翻译器
    ("E", "C-GL", "geometric-langlands"),
    ("E", "C-HECKEO", "hecke-operator"),
    ("E", "C-HECKEE", "hecke-eigensheaf"),
    ("E", "C-GR", "affine-grassmannian"),
    ("E", "C-BOG", "bogomolny-equation"),
    ("E", "C-DMOD", "d-module"),
    ("E", "C-CC", "canonical-coisotropic-brane"),
    ("E", "C-LOCAL", "local-system"),
]

# ---- 推导卡选目：24 条链（每条 = skeleton.jsonl 的一组 step id）----
DERIVATIONS = [
    ("A", "gno-to-langlands", "从 GNO 对偶群到 Langlands 对偶群", ["S1-02", "S1-03", "S1-10"]),
    ("A", "sdual-sl2z", "S-对偶生成元、SL(2,Z) 与超荷的双覆盖", ["S1-04", "S1-05", "S1-06", "S1-07"]),
    ("A", "table1-and-ng", "非单连通群的 n_g 修正与 Table 1", ["S1-08", "S1-09", "S1-11"]),
    ("B", "twist-construction", "GL 扭化的构造：选哪个 Spin(4)", ["S2-01", "S2-02", "S2-03", "S2-04"]),
    ("B", "one-parameter-family", "一族拓扑场论：t ∈ CP¹ 与 Q² = 0", ["S2-05", "S2-06", "S2-07", "S2-08"]),
    ("B", "vanishing-theorem", "Q-不变方程与消失定理", ["S2-09", "S2-10"]),
    ("B", "canonical-parameter", "典范参数 Ψ：定义、S 作用与消去 t", ["S2-11", "S2-12", "S2-13", "S2-14"]),
    ("B", "psi-special-points", "Ψ 的特殊点与为什么必须是 GL 扭化", ["S2-15", "S2-16", "S2-17", "S2-18"]),
    ("C", "compactify-to-hitchin", "紧化到 Hitchin 方程：M = Σ×C", ["S3-01", "S3-02", "S3-03", "S3-04"]),
    ("C", "hyperkahler-quotient", "超凯勒商与三个复结构 I, J, K", ["S3-05", "S3-06", "S3-07", "S3-08"]),
    ("C", "mh-sigma-data", "M_H 上的 sigma 模型数据与维数公式", ["S3-09", "S3-10", "S3-11"]),
    ("C", "hitchin-integrability", "Hitchin 系统的完全可积性与 Lagrange 纤维", ["S3-12", "S3-13", "S3-14"]),
    ("D", "two-d-theories", "二维理论：B-模型、A-模型与不变量 q", ["S4-01", "S4-02", "S4-03", "S4-04", "S4-05"]),
    ("D", "generalized-complex", "广义复几何：A/B 与 B-场的统一语言", ["S4-06", "S4-07", "S4-08", "S4-09"]),
    ("D", "sdual-mirror", "S-对偶 = 镜像对称（全文心脏）", ["S4-10", "S4-11", "S4-12", "S4-13", "S4-14", "S4-15"]),
    ("D", "line-operators", "Wilson 与 't Hooft 线算子及其分类", ["S5-01", "S5-02", "S5-04", "S5-05", "S5-06", "S5-07"]),
    ("D", "folding", "折叠：线算子变成边界条件", ["S5-08", "S5-09", "S5-10"]),
    ("D", "eigenbranes", "特征膜：XB ≅ B ⊗ V 与同时对角化", ["S5-11", "S5-12", "S5-13", "S5-14", "S5-15"]),
    ("E", "center-and-flux", "中心 Z、离散 flux 与 S-对偶的作用", ["S6-01", "S6-02", "S6-03"]),
    ("E", "twisted-bundles", "universal bundle 的障碍与 twisted 丛", ["S6-04", "S6-05", "S6-06", "S6-07", "S6-08"]),
    ("E", "electric-eigenbranes", "电特征膜 = 平坦 ^LG_C 联络", ["S6-09", "S6-10", "S6-11", "S6-12", "S6-13"]),
    ("E", "toofty-hecke", "'t Hooft 算子的 Hecke 修改：U(1) 到 U(N)", ["S7-01", "S7-02", "S7-03", "S7-04", "S7-05"]),
    ("E", "grassmann-schubert", "Hecke 修改空间、仿射 Grassmannian 与 Schubert 胞腔", ["S7-06", "S7-07", "S7-08", "S7-09", "S7-10"]),
    ("E", "bubbling-ope", "单极子冒泡、辛商与 OPE 代数", ["S7-11", "S7-12", "S7-13", "S7-14", "S7-15"]),
    ("E", "a-to-dmod", "c.c. A-膜、开弦代数与 A-膜→D-模", ["S8-01", "S8-02", "S8-03", "S8-04", "S8-05", "S8-06"]),
    ("E", "psi-lambda", "Ψ ≠ 0：λ-连接与扭化 D-模", ["S8-07", "S8-08", "S8-09", "S8-10", "S8-11", "S8-12"]),
    ("E", "back-to-4d", "三类膜回到四维：§12 检查表", ["S8-13", "S8-14", "S8-15"]),
]

NODE_SECTION = {"S1": "§2", "S2": "§3", "S3": "§4", "S4": "§5",
                "S5": "§6–§8", "S6": "§7–§8", "S7": "§9–§10", "S8": "§11–§12"}


def load_jsonl(p: Path):
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="derivation 目录（含 concepts.jsonl / skeleton.jsonl）")
    args = ap.parse_args()
    src = Path(args.src)
    concepts = {c["id"]: c for c in load_jsonl(src / "concepts.jsonl")}
    skel = {s["id"]: s for s in load_jsonl(src / "skeleton.jsonl")}

    (CARDS / "concepts").mkdir(parents=True, exist_ok=True)
    (CARDS / "derivations").mkdir(parents=True, exist_ok=True)

    n_c = 0
    for track, cid, slug in CONCEPTS:
        c = concepts.get(cid)
        if not c:
            print(f"[warn] concept {cid} not found, skipped")
            continue
        edges = []
        for e in c.get("edges", []):
            tgt = e.get("to") or e.get("target") or e.get("id")
            edges.append(tgt)
        card = {
            "id": f"kw/concept/{slug}",
            "type": "concept",
            "title": c["name_zh"],
            "aliases": [c["name_en"]] if c.get("name_en") else [],
            "track": track,
            "summary": c.get("definition_our", "")[:120],
            "question": f"{c['name_zh']}是什么，它在整条论证链里起什么作用？",
            "definition": {"text": c.get("definition_our", ""), "notation": ""},
            "key_points": [x for x in [c.get("why_needed", ""), c.get("physical_reading", ""),
                                       c.get("math_reading", "")] if x][:3],
            "formulas": [],
            "theorems": [],
            "pitfalls": [],
            "related": [f"kw/concept/{s}" for s in edges if s][:4],
            "sources": [{"text": "B", "section": "待补", "pages": [2, 2], "anchor": "B p.2"}],
            "rights": "rewritten",
            "status": "draft",
            "provenance_note": f"初稿自动生成自 concepts.jsonl 的 {cid}；nLab={c.get('nlab')}, stacks={c.get('stacks')}",
        }
        (CARDS / "concepts" / f"{slug}.json").write_text(
            json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        n_c += 1

    n_d = 0
    for track, slug, title, ids in DERIVATIONS:
        steps = []
        for i, sid in enumerate(ids, 1):
            s = skel.get(sid)
            if not s:
                print(f"[warn] step {sid} missing in {slug}")
                continue
            text = "；".join(x for x in [s.get("idea", ""), s.get("technique", ""), s.get("claim", "")] if x)
            steps.append({
                "no": i,
                "text": text,
                "why": s.get("why_it_matters", ""),
                "locator": s.get("anchor", "B p.2"),
                "provenance": s.get("provenance", "B"),
            })
        if len(steps) < 3:
            print(f"[warn] {slug} has only {len(steps)} steps")
        node = ids[0].split("-")[0]
        pages = []
        for sid in ids:
            s = skel.get(sid, {})
            m = re.search(r"p\.(\d+)", s.get("anchor", ""))
            if m:
                pages.append(int(m.group(1)))
        lo, hi = (min(pages), max(pages)) if pages else (2, 2)
        card = {
            "id": f"kw/deriv/{slug}",
            "type": "derivation",
            "title": title,
            "aliases": [],
            "track": track,
            "summary": f"（初稿）{title}：{len(steps)} 步。",
            "question": f"{title}——这条推导是怎么走通的？",
            "goal": title,
            "setup": ["待补：这条推导的输入前提。"],
            "steps": steps,
            "result": "待补：推导的结论。",
            "gaps": [],
            "pitfalls": [],
            "related": [],
            "sources": [{"text": "B", "section": NODE_SECTION.get(node, "§"), "pages": [lo, hi],
                         "anchor": f"B p.{lo}"}],
            "rights": "rewritten",
            "status": "draft",
            "provenance_note": "初稿自动生成自 skeleton.jsonl；steps 的 provenance 取自原始记录。",
        }
        (CARDS / "derivations" / f"{slug}.json").write_text(
            json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        n_d += 1

    print(f"[ok] concepts={n_c} derivations={n_d}")


if __name__ == "__main__":
    main()
