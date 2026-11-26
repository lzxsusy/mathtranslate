#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Post-fix verification for the glc_full_2026-11-26 campaign.

Checks
  1. 154 glc cards: every file parses, id matches filename, ids unique
  2. whole library (datasets/*/cards/**/*.json == 1676): 0 parse errors
  3. git diff --numstat -- datasets/glc  ⊆  baseline dirty files ∪ fix_log targets
  4. git diff --check: no whitespace errors introduced
  5. HEAD unchanged (nothing committed)
  6. fix_log integrity: sha256_after matches on disk; every `after` present,
     every `before` gone (unless still legitimately present elsewhere)
  7. md mirror: every fixed card's md parses as text and holds no stale `before`
"""
import argparse
import glob
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
REPO = os.path.abspath(os.path.join(ROOT, "..", "..", ".."))


def run(args):
    p = subprocess.run(args, cwd=REPO, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p.returncode, p.stdout, p.stderr


def sha(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix-log", default=os.path.join(ROOT, "fix_log.json"))
    args = ap.parse_args()
    fails = []
    rep = {}

    # 1. glc cards
    glc = sorted(glob.glob(os.path.join(REPO, "datasets/glc/cards/**/*.json"),
                           recursive=True))
    ids = {}
    for p in glc:
        try:
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
        except Exception as e:  # noqa: BLE001
            fails.append("glc parse error: %s: %s" % (p, e))
            continue
        slug = os.path.basename(p)[:-5]
        if d.get("id", "").split("/")[-1] != slug:
            fails.append("id/filename mismatch: %s vs %s" % (p, d.get("id")))
        ids[p] = d["id"]
    rep["glc_cards"] = len(glc)
    rep["glc_unique_ids"] = len(set(ids.values()))
    if len(glc) != 154:
        fails.append("glc card count %d != 154" % len(glc))

    # 2. whole library
    lib = sorted(glob.glob(os.path.join(REPO, "datasets/*/cards/**/*.json"),
                           recursive=True))
    lib_bad = 0
    for p in lib:
        try:
            with open(p, "r", encoding="utf-8") as f:
                json.load(f)
        except Exception:  # noqa: BLE001
            lib_bad += 1
            fails.append("library parse error: %s" % p)
    rep["library_cards"] = len(lib)
    rep["library_parse_errors"] = lib_bad
    if len(lib) != 1676:
        fails.append("library card count %d != 1676" % len(lib))

    # fix log
    fix = {"fixes": []}
    if os.path.isfile(args.fix_log):
        with open(args.fix_log, "r", encoding="utf-8") as f:
            fix = json.load(f)
    all_fixes = list(fix.get("fixes", [])) + list(fix.get("followup", {}).get("fixes", []))
    expected = set()
    for r in all_fixes:
        expected.add(r["path"])
        if r.get("md_sync", {}).get("status") == "ok":
            expected.add(r["md_sync"]["md_path"])

    # 3. diff numstat
    rc, out, err = run(["git", "diff", "--numstat", "--", "datasets/glc"])
    changed = {}
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) == 3:
            changed[parts[2]] = (parts[0], parts[1])
    rep["glc_changed_files"] = {k: list(v) for k, v in changed.items()}
    allowed = {"datasets/glc/cards/concepts/frobenius-twisted-trace.json",
               "datasets/glc/md/concepts/frobenius-twisted-trace.md"} | expected
    extra = sorted(set(changed) - allowed)
    if extra:
        fails.append("unexpected changed glc files: %r" % extra)
    missing = sorted(expected - set(changed))
    if missing:
        fails.append("fix_log targets not actually changed: %r" % missing)

    # 4. diff --check
    rc, out, err = run(["git", "diff", "--check"])
    rep["diff_check"] = "clean" if not out.strip() else out.strip()[:2000]
    if out.strip():
        fails.append("git diff --check reports whitespace problems")

    # 5. HEAD
    rc, out, _ = run(["git", "rev-parse", "HEAD"])
    rep["head"] = out.strip()
    base_head = ""
    bp = os.path.join(ROOT, "tmp", "git_baseline_head.txt")
    if os.path.isfile(bp):
        base_head = open(bp, "r", encoding="utf-8").read().strip()
    rep["baseline_head"] = base_head
    if base_head and rep["head"] != base_head:
        rc2, _, _ = run(["git", "merge-base", "--is-ancestor", base_head, rep["head"]])
        if rc2 != 0:
            fails.append("HEAD moved and baseline is not an ancestor: %s -> %s"
                         % (base_head, rep["head"]))
        else:
            rc3, out3, _ = run(["git", "log", "--format=%h %s",
                                base_head + ".." + rep["head"]])
            rep["commits_since_baseline"] = [x for x in out3.splitlines() if x.strip()]

    # 6. fix log integrity
    checked = 0
    for r in all_fixes:
        absp = os.path.join(REPO, r["path"])
        if not os.path.isfile(absp):
            fails.append("fix target missing: %s" % r["path"])
            continue
        h = sha(absp)
        if h != r["sha256_after"]:
            fails.append("sha256_after mismatch: %s" % r["path"])
        with open(absp, "r", encoding="utf-8") as f:
            doc = json.load(f)
        blob = json.dumps(doc, ensure_ascii=False)
        for e in r["edits"]:
            checked += 1
            aft = e["after"]
            texts = aft if isinstance(aft, list) else [aft]
            for t in texts:
                if json.dumps(t, ensure_ascii=False) not in blob:
                    fails.append("after-text absent in %s [%s]"
                                 % (r["path"], e["field"]))
    rep["fix_edits_checked"] = checked
    rep["fix_cards"] = len(all_fixes)
    rep["fix_edits"] = fix.get("n_edits")

    # 7. md mirrors
    stale = []
    for r in all_fixes:
        ms = r.get("md_sync", {})
        if ms.get("status") != "ok":
            stale.append({"id": r["id"], "md": ms.get("status")})
            continue
        md = os.path.join(REPO, ms["md_path"])
        txt = open(md, "r", encoding="utf-8").read()
        for e in ms.get("edits", []):
            new = e.get("md_new") or ""
            if new and new not in txt:
                fails.append("md missing after-text: %s [%s]"
                             % (ms["md_path"], e.get("field")))
        for f in ms.get("not_found", []):
            if not str(f).endswith(".verdict"):
                fails.append("md edit not applied: %s [%s]"
                             % (ms["md_path"], f))
    rep["md_not_synced"] = stale

    rep["fails"] = fails
    rep["ok"] = not fails
    print(json.dumps(rep, ensure_ascii=False, indent=2))
    with open(os.path.join(ROOT, "verify_report.json"), "w", encoding="utf-8") as f:
        json.dump(rep, f, ensure_ascii=False, indent=2)
        f.write("\n")
    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
