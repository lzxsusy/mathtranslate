#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Apply lead-reviewed minimal fixes to GLC cards (field level, with old assertion).

fix_plan.json shape:
{
  "fixes": [
    {"id": "glc/concept/x", "path": "datasets/glc/cards/concepts/x.json",
     "confirmed_by": "both_issue" | "arbiter",
     "severity": "minor|major|critical",
     "evidence": ["..."],
     "edits": [{"field": "definition.text", "old": "...", "new": "...", "why": "..."}]
    }
  ]
}

Behaviour:
  --check   validate every edit against the current file, write nothing
  --apply   apply, rewrite file as json.dumps(ensure_ascii=False, indent=2)+"\n",
            append one record per card to fix_log.json (before/after per edit,
            sha256 before/after, unified diff hunks count)
Never touches git.
"""
import argparse
import difflib
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
REPO = os.path.abspath(os.path.join(ROOT, "..", "..", ".."))

TOKEN = re.compile(r"^([A-Za-z0-9_]+)((?:\[\d+\]|\.[A-Za-z0-9_]+)*)$")
PART = re.compile(r"\[(\d+)\]|\.([A-Za-z0-9_]+)")


def split_field(field):
    """'theorems[0].proof.status' -> ['theorems', 0, 'proof', 'status']"""
    m = TOKEN.match(field)
    if not m:
        raise ValueError("bad field path: %r" % field)
    parts = [m.group(1)]
    for idx, name in PART.findall(m.group(2)):
        parts.append(int(idx) if idx != "" else name)
    return parts


def resolve(doc, parts):
    cur = doc
    for p in parts[:-1]:
        cur = cur[p]
    return cur, parts[-1]


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def page_span(pages):
    return "-".join(str(p) for p in pages)


def md_targets(e):
    """(old, new) text pairs to replace in the md mirror for one edit.

    The md is a hand-maintained rendering whose `sources` line prints pages as
    `p.6（PDF p.6）` / `p.76-77（PDF p.76-77）`, not as the JSON list.  Callers may
    pass explicit `md_edits`; list-valued pages are derived automatically.
    """
    if e.get("md_edits"):
        return [(m["old"], m["new"]) for m in e["md_edits"]]
    if isinstance(e["before"], list):
        a, b = page_span(e["before"]), page_span(e["after"])
        return [("p.%s（PDF p.%s）" % (a, a), "p.%s（PDF p.%s）" % (b, b))]
    return [(e["before"], e["after"])]


def sync_md(rel, after_doc, edits_log):
    """Keep the hand-maintained md mirror in step with the card.

    datasets/glc/md/concepts/<slug>.md renders the card fields verbatim (same
    characters, no re-escaping), so a literal old->new replacement is the
    minimal sync.  Refuse to write when a target string is absent (mirror is
    not the rendering we assume) or occurs more than once (replacement would
    then be ambiguous); both are reported for the lead to fix by hand.
    """
    md_rel = rel.replace("/cards/", "/md/").replace(".json", ".md")
    md_abs = os.path.join(REPO, md_rel)
    rec = {"md_path": md_rel, "status": "ok", "edits": [], "not_found": [],
           "ambiguous": []}
    if not os.path.isfile(md_abs):
        rec["status"] = "absent"
        return rec, None
    with open(md_abs, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    def strings(o):
        if isinstance(o, dict):
            for v in o.values():
                for x in strings(v):
                    yield x
        elif isinstance(o, list):
            for v in o:
                for x in strings(v):
                    yield x
        elif isinstance(o, str):
            yield o

    vals = list(strings(after_doc))
    for e in edits_log:
        if isinstance(e["before"], str) and any(v == e["before"] for v in vals):
            rec["ambiguous"].append(e["field"] + " (same text in another field)")
    if rec["ambiguous"]:
        rec["status"] = "ambiguous"
        return rec, None
    new_text = text
    applied = set()
    for e in edits_log:
        for old, new in md_targets(e):
            if old in applied:  # pages and pdf_pages render to the same md text
                continue
            c = new_text.count(old)
            if c > 1:
                rec["ambiguous"].append("%s (md holds it %d times)" % (e["field"], c))
                continue
            if c == 0:
                rec["not_found"].append(e["field"])
                continue
            new_text = new_text.replace(old, new)
            applied.add(old)
            rec["edits"].append({"field": e["field"], "md_old": old, "md_new": new})
    if rec["ambiguous"]:
        rec["status"] = "ambiguous"
        return rec, None
    rec["sha256_before"] = sha256_bytes(raw)
    rec["sha256_after"] = sha256_bytes(new_text.encode("utf-8"))
    return rec, new_text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", default=os.path.join(ROOT, "fix_plan.json"))
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    if args.check == args.apply:
        sys.exit("pass exactly one of --check / --apply")

    with open(args.plan, "r", encoding="utf-8") as f:
        plan = json.load(f)
    fixes = plan.get("fixes", [])
    errors = []
    log = []
    n_edits = 0

    for fx in fixes:
        rel = fx["path"]
        abspath = os.path.join(REPO, rel)
        if not os.path.isfile(abspath):
            errors.append("%s: missing file %s" % (fx["id"], rel))
            continue
        with open(abspath, "rb") as f:
            raw0 = f.read()
        doc = json.loads(raw0.decode("utf-8"))
        if doc.get("id") != fx["id"]:
            errors.append("%s: file id is %r" % (fx["id"], doc.get("id")))
            continue
        before_doc = json.loads(raw0.decode("utf-8"))
        edits_log = []
        for ed in fx["edits"]:
            field = ed["field"]
            try:
                parts = split_field(field)
                holder, key = resolve(doc, parts)
                cur = holder[key]
            except Exception as e:  # noqa: BLE001
                errors.append("%s %s: unresolved path (%s)" % (fx["id"], field, e))
                continue
            if not isinstance(cur, (str, list)):
                errors.append("%s %s: current value is neither string nor list" % (fx["id"], field))
                continue
            mode = ed.get("mode", "field")
            if mode == "substring":
                if not isinstance(cur, str):
                    errors.append("%s %s: substring edit on non-string" % (fx["id"], field))
                    continue
                cnt = cur.count(ed["old"])
                if cnt != 1:
                    errors.append("%s %s: substring occurs %d times (need exactly 1)"
                                  % (fx["id"], field, cnt))
                    continue
                newval = cur.replace(ed["old"], ed["new"])
                item = {"field": field, "mode": "substring", "before": cur,
                        "after": newval, "old_sub": ed["old"], "new_sub": ed["new"],
                        "why": ed.get("why", "")}
            else:
                if cur != ed["old"]:
                    errors.append("%s %s: old assertion mismatch\n  file: %r\n  plan: %r"
                                  % (fx["id"], field, cur[:400], ed["old"][:400]))
                    continue
                if ed["new"] == ed["old"]:
                    errors.append("%s %s: new == old (no-op edit)" % (fx["id"], field))
                    continue
                newval = ed["new"]
                item = {"field": field, "mode": "field", "before": ed["old"],
                        "after": ed["new"], "why": ed.get("why", "")}
            holder[key] = newval
            if ed.get("md_edits"):
                item["md_edits"] = ed["md_edits"]
            edits_log.append(item)
            n_edits += 1
        if not edits_log:
            continue

        new_text = json.dumps(doc, ensure_ascii=False, indent=2) + "\n"
        md_rec, md_new = sync_md(rel, doc, edits_log)
        if md_rec["status"] == "ambiguous":
            errors.append("%s: md mirror ambiguous for %s (old text survives in "
                          "an untouched field); resolve by hand"
                          % (fx["id"], ", ".join(md_rec["ambiguous"])))
            continue
        if args.apply:
            with open(abspath, "w", encoding="utf-8", newline="\n") as f:
                f.write(new_text)
            if md_new is not None:
                with open(os.path.join(REPO, md_rec["md_path"]), "w",
                          encoding="utf-8", newline="\n") as f:
                    f.write(md_new)

        # per-file minimal-diff sanity: count changed lines of the JSON text
        old_text = json.dumps(before_doc, ensure_ascii=False, indent=2) + "\n"
        diff = list(difflib.unified_diff(old_text.splitlines(), new_text.splitlines(),
                                        lineterm="", n=0))
        changed = sum(1 for l in diff if l.startswith(("+", "-"))
                      and not l.startswith(("+++", "---")))
        log.append({
            "id": fx["id"],
            "path": rel,
            "confirmed_by": fx.get("confirmed_by"),
            "severity": fx.get("severity"),
            "evidence": fx.get("evidence", []),
            "sha256_before": sha256_bytes(raw0),
            "sha256_after": sha256_bytes(new_text.encode("utf-8")),
            "json_text_changed_lines": changed,
            "edits": edits_log,
            "md_sync": md_rec,
        })

    if errors:
        print("VALIDATION ERRORS (%d):" % len(errors))
        for e in errors:
            print(" -", e)
        sys.exit(1)

    if args.check:
        print("OK: %d cards, %d edits would apply cleanly (nothing written)"
              % (len(log), n_edits))
        for r in log:
            md = r["md_sync"]
            print("  %-52s %d edit(s), %d changed json lines | md %s, %d md edit(s)%s"
                  % (r["path"], len(r["edits"]), r["json_text_changed_lines"],
                     md["status"], len(md["edits"]),
                     "" if not md["not_found"] else
                     " NOT_FOUND=" + ",".join(md["not_found"])))
        return

    logpath = os.path.join(ROOT, "fix_log.json")
    with open(logpath, "w", encoding="utf-8") as f:
        json.dump({
            "campaign": "glc_full_2026-11-26",
            "repo_head": os.popen("git -C \"%s\" rev-parse HEAD" % REPO).read().strip(),
            "policy": "minimal field-level edits, old value asserted before write; "
                      "files rewritten as json.dumps(ensure_ascii=False, indent=2)+LF",
            "n_cards": len(log),
            "n_edits": n_edits,
            "fixes": log,
        }, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("APPLIED: %d cards, %d edits -> %s" % (len(log), n_edits, logpath))


if __name__ == "__main__":
    main()
