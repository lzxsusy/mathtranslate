# -*- coding: utf-8 -*-
"""Validate units / inferences / chain / concepts JSONL+JSON.

Usage: python validate_annotations.py <dir>
Exit 0 = pass (warnings allowed), 1 = errors.
"""
import json, os, re, sys

E = []
W = []
UNIT_ID = re.compile(r"^[A-Za-z0-9_.-]+:[a-z]+-[A-Za-z0-9_.:-]+$")
KN_ID = re.compile(r"^kn_[0-9a-f]{12}$")
SLUG = re.compile(r"^[a-z0-9][a-z0-9-]{1,63}$")
KINDS = {"definition", "theorem", "lemma", "proposition", "corollary", "construction",
         "example", "remark", "proof", "step", "claim", "question", "method"}
ROLES = {"spine", "key", "routine", "gap", "background"}
DIMS = {"D1_conceptual", "D2_gap", "D3_technical", "D4_notation",
        "D5_transfer", "D6_verification", "D7_loadbearing", "D8_expository"}
RELS = {"uses", "proves", "generalizes", "specializes", "analogous", "contradicts", "equivalent", "defines"}
RULES = {"SUB", "APPLY", "EXPAND", "COLLECT", "COMPONENT", "CONSTRUCT", "COMPAT", "COMBINE", "OPAQUE"}
REVIEW = {"proposed", "accepted", "rejected", "needs_review", "unresolved"}
CONCEPT_TYPES = {"object", "property", "construction", "theorem", "method", "problem"}
CONCEPT_STATUS = {"draft", "reviewed", "canonical", "merged", "deprecated"}


def load(path):
    if path.endswith(".jsonl"):
        out = []
        for i, line in enumerate(open(path, encoding="utf-8"), 1):
            line = line.strip()
            if line:
                try:
                    out.append((i, json.loads(line)))
                except Exception as e:
                    E.append(f"{os.path.basename(path)}:{i} invalid JSON: {e}")
        return out
    try:
        d = json.load(open(path, encoding="utf-8"))
        return [(1, d)]
    except Exception as e:
        E.append(f"{os.path.basename(path)} invalid JSON: {e}")
        return []


def req(o, keys, tag):
    for k in keys:
        if k not in o:
            E.append(f"{tag} missing {k}")


def check_locator(loc, tag):
    if not isinstance(loc, dict):
        E.append(f"{tag} locator not object"); return
    ok = any(k in loc for k in ("page_orig", "para_id")) or ("page_pdf" in loc and "bbox" in loc) or ("tex_file" in loc and "tex_lines" in loc)
    if not ok:
        E.append(f"{tag} locator has no usable anchor")


def main(d):
    units = {}
    for ln, u in load(os.path.join(d, "units.jsonl")):
        tag = f"units:{ln}"
        req(u, ["unit_id", "paper_id", "kind", "statement", "locator", "role", "difficulty", "review", "provenance"], tag)
        if not UNIT_ID.match(u.get("unit_id", "")): E.append(f"{tag} bad unit_id {u.get('unit_id')}")
        if u.get("unit_id") in units: E.append(f"{tag} duplicate unit_id")
        if u.get("kind") not in KINDS: E.append(f"{tag} bad kind")
        if u.get("role") not in ROLES: E.append(f"{tag} bad role")
        check_locator(u.get("locator"), tag)
        dif = u.get("difficulty", {})
        if not isinstance(dif.get("score"), int) or not 1 <= dif.get("score", 0) <= 5: E.append(f"{tag} bad score")
        if not dif.get("dims") or any(x not in DIMS for x in dif.get("dims", [])): E.append(f"{tag} bad dims")
        for k in ("why_hard", "check"):
            if not dif.get(k): E.append(f"{tag} missing difficulty.{k}")
        if u.get("role") in {"spine", "key", "gap"}:
            if dif.get("score", 0) < 3: E.append(f"{tag} role {u.get('role')} needs score>=3")
            if not dif.get("why_hard") or not dif.get("check"): E.append(f"{tag} key step needs why_hard+check")
        if u.get("role") == "gap" and not dif.get("jump", {}).get("missing"):
            E.append(f"{tag} gap needs difficulty.jump.missing")
        sev = dif.get("jump", {}).get("severity")
        if sev is not None and sev not in {"small", "medium", "large"}:
            E.append(f"{tag} bad jump.severity {sev}")
        if u.get("review", {}).get("status") not in REVIEW: E.append(f"{tag} bad review.status")
        if not u.get("provenance", {}).get("annotator"): E.append(f"{tag} missing provenance.annotator")
        units[u.get("unit_id")] = u

    infs = []
    for ln, x in load(os.path.join(d, "inferences.jsonl")):
        tag = f"inferences:{ln}"
        req(x, ["inference_id", "paper_id", "premises", "conclusion", "relation", "and_or", "warrant", "rule", "evidence", "review"], tag)
        if not x.get("premises"): E.append(f"{tag} empty premises")
        if x.get("relation") not in RELS: E.append(f"{tag} bad relation")
        if x.get("and_or") not in {"and", "or", "single"}: E.append(f"{tag} bad and_or")
        if x.get("rule") not in RULES: E.append(f"{tag} bad rule")
        if len(x.get("warrant", "")) < 8: E.append(f"{tag} warrant too short")
        ev = x.get("evidence", {})
        if not ev.get("quote") or len(ev.get("quote", "")) > 400: E.append(f"{tag} bad evidence.quote")
        if "locator" not in ev: E.append(f"{tag} missing evidence.locator")
        if x.get("review", {}).get("status") not in REVIEW: E.append(f"{tag} bad review.status")
        infs.append(x)

    chains = []
    for ln, c in load(os.path.join(d, "chain.json")):
        tag = "chain"
        req(c, ["paper_id", "chain_id", "thread", "problem_state", "move", "chain", "closure", "boundaries"], tag)
        seqs = [s.get("seq") for s in c.get("chain", [])]
        if seqs != list(range(1, len(seqs) + 1)): E.append(f"{tag} seq not contiguous: {seqs}")
        for s in c.get("chain", []):
            if not s.get("because") or not isinstance(s.get("enables"), list): E.append(f"{tag} step {s.get('seq')} bad because/enables")
        chains.append(c)

    concepts = []
    for ln, k in load(os.path.join(d, "concepts.jsonl")):
        tag = f"concepts:{ln}"
        req(k, ["concept_id", "slug", "type", "name_zh", "one_line", "status", "entry_unit", "related"], tag)
        if not KN_ID.match(k.get("concept_id", "")): E.append(f"{tag} bad concept_id")
        if not SLUG.match(k.get("slug", "")): E.append(f"{tag} bad slug")
        if k.get("type") not in CONCEPT_TYPES: E.append(f"{tag} bad type")
        if k.get("status") not in CONCEPT_STATUS: E.append(f"{tag} bad status")
        for r in k.get("related", []):
            if not r.get("evidence"): E.append(f"{tag} relation {r.get('to')} without evidence")
        concepts.append(k)

    # cross references
    ids = set(units)
    cids = {k["concept_id"] for k in concepts}
    for u in units.values():
        for f in ("uses", "used_by", "proves"):
            for r in u.get(f, []) or []:
                if r not in ids and r not in cids:
                    W.append(f"{u['unit_id']} {f} dangling {r}")
        for r in u.get("concepts", []) or []:
            if r not in cids: E.append(f"{u['unit_id']} unknown concept {r}")
    for x in infs:
        for p in x["premises"]:
            if p not in ids: E.append(f"{x['inference_id']} premise not found {p}")
        if x["conclusion"] not in ids and x["conclusion"] not in cids:
            E.append(f"{x['inference_id']} conclusion not found {x['conclusion']}")
    for c in chains:
        for s in c["chain"]:
            if s["unit_id"] not in ids: E.append(f"{c['chain_id']} step unit not found {s['unit_id']}")
        for key in (c["move"]["unit_id"], c["closure"]["unit_id"]):
            if key not in ids: E.append(f"{c['chain_id']} ref not found {key}")
        for cf in c.get("counterfactual", []):
            if cf["remove"] not in ids: E.append(f"{c['chain_id']} counterfactual not found {cf['remove']}")
    for k in concepts:
        if k["entry_unit"] not in ids: E.append(f"{k['concept_id']} entry_unit not found")
        for r in k.get("related", []):
            if r["to"] not in cids: E.append(f"{k['concept_id']} related target not found {r['to']}")
            for ev in r.get("evidence", []):
                if ev not in ids: E.append(f"{k['concept_id']} relation evidence not found {ev}")

    # cycle detection over inference premises->conclusion
    graph = {}
    for x in infs:
        for p in x["premises"]:
            graph.setdefault(p, set()).add(x["conclusion"])
    color = {}

    def dfs(n):
        color[n] = 1
        for m in graph.get(n, ()):
            if color.get(m) == 1:
                E.append(f"cycle in inference graph at {m}"); return True
            if color.get(m, 0) == 0 and dfs(m): return True
        color[n] = 2; return False

    for n in list(graph):
        if color.get(n, 0) == 0: dfs(n)

    # orphans (warnings only)
    referenced = set()
    for x in infs:
        referenced.update(x["premises"]); referenced.add(x["conclusion"])
    for c in chains:
        referenced.update(s["unit_id"] for s in c["chain"]); referenced.add(c["move"]["unit_id"]); referenced.add(c["closure"]["unit_id"])
    for k in concepts:
        referenced.add(k["entry_unit"]); referenced.update(k.get("key_units", []))
    for u in units:
        if u not in referenced: W.append(f"orphan unit (not in any inference/chain/concept): {u}")

    print(f"units={len(units)} inferences={len(infs)} chains={len(chains)} concepts={len(concepts)}")
    for w in W[:20]: print("WARN", w)
    for e in E[:50]: print("ERROR", e)
    print("RESULT", "PASS" if not E else f"FAIL ({len(E)} errors)")
    return 1 if E else 0


if __name__ == "__main__":
    default = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "examples")
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else default))
