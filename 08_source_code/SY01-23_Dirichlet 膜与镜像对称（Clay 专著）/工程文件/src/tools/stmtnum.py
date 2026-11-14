# -*- coding: utf-8 -*-
"""Compare numbered statements per type per chapter with the original book."""
import re, os, collections

ROOT = r"C:\Users\admin\Downloads\DBMS_work"
pages = open(os.path.join(ROOT, "original", "full.txt"), encoding="utf-8").read().split("\f")

CH_PAGES = {"1": (11, 36), "2": (37, 118), "3": (119, 225), "4": (227, 302),
            "5": (303, 429), "6": (431, 518), "7": (519, 583), "8": (585, 663)}

MAP = {
    "theorem": "thm", "definition": "def", "proposition": "prop", "lemma": "lem",
    "corollary": "cor", "conjecture": "conj", "example": "ex", "exercise": "exer",
    "construction": "constr", "property": "property", "axiom": "axiom",
    "claim": "claim", "problem": "prob", "principle": "principle",
}

orig = collections.defaultdict(lambda: collections.defaultdict(set))
for ch, (a, b) in CH_PAGES.items():
    for p in range(a, b + 1):
        for line in pages[p - 1].splitlines():
            m = re.match(r"\s*(Theorem|Definition|Proposition|Lemma|Corollary|Conjecture|Example|Exercise|Construction|Property|Axiom|Claim|Problem|Principle)s?\s+(\d+)\.(\d+)", line)
            if m and m.group(2) == ch:
                orig[ch][MAP[m.group(1).lower()]].add(int(m.group(3)))

texdir = os.path.join(ROOT, "Dirichlet-Mirror-Symmetry-zh", "chapters")
ours = collections.defaultdict(lambda: collections.defaultdict(set))
for f in os.listdir(texdir):
    if not f.endswith(".tex"):
        continue
    txt = open(os.path.join(texdir, f), encoding="utf-8").read()
    for m in re.finditer(r"\\label\{([a-z]+):(\d+)\.(\d+)\}", txt):
        ours[m.group(2)][m.group(1)].add(int(m.group(3)))
    # Property labels may be stored as property:N.M and duplicated as pty:N.M
    for m in re.finditer(r"\\label\{pty:(\d+)\.(\d+)\}", txt):
        ours[m.group(1)]["property"].add(int(m.group(2)))

types = sorted(set(sum([list(v.keys()) for v in orig.values()], [])))
print("type | ch | orig | ours | missing from ours | extra in ours")
tot_missing = []
for t in types:
    for ch in sorted(CH_PAGES):
        o = orig[ch].get(t, set())
        u = ours.get(ch, {}).get(t, set())
        if not o and not u:
            continue
        miss = sorted(o - u)
        extra = sorted(u - o)
        if miss or extra:
            print("%s | %s | %d | %d | %s | %s" % (t, ch, len(o), len(u), miss, extra))
            if miss:
                tot_missing.append((t, ch, miss))
print("\nper-type totals (orig / ours):")
for t in types:
    to = sum(len(orig[c].get(t, ())) for c in CH_PAGES)
    tu = sum(len(ours.get(c, {}).get(t, ())) for c in CH_PAGES)
    print("  %-12s %3d / %3d %s" % (t, to, tu, "" if to == tu else "  <-- DIFF"))
