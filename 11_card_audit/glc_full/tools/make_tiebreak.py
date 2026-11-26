#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build blind tie-break (arbiter) lists from compare.json.

Only cards classified a_issue_only or b_issue_only need an arbiter.
The arbiter sees ONE path list and nothing else: no A verdict, no B verdict,
no field names -- otherwise it is not blind.
"""
import json
import math
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))


def main():
    with open(os.path.join(ROOT, "compare.json"), "r", encoding="utf-8") as f:
        cmp = json.load(f)
    need = [c for c in cmp["cards"] if c["class"] in ("a_issue_only", "b_issue_only")]
    rng = random.Random(777)
    rng.shuffle(need)
    per = 12
    ng = max(1, int(math.ceil(len(need) / float(per)))) if need else 0
    out_dir = os.path.join(ROOT, "tiebreak")
    grp = os.path.join(out_dir, "groups")
    os.makedirs(grp, exist_ok=True)
    manifest = {}
    for i in range(ng):
        gname = "T%d" % (i + 1)
        sub = need[i::ng]
        with open(os.path.join(grp, gname + ".txt"), "w", encoding="utf-8") as f:
            for c in sub:
                f.write(c["path"] + "\n")
        manifest[gname] = [{"n": j + 1, "id": c["id"], "path": c["path"]}
                           for j, c in enumerate(sub)]
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump({"summary": {"n_cards": len(need), "groups": len(manifest)},
                   "groups": manifest}, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps({"n_cards": len(need), "groups": len(manifest),
                      "ids": [c["id"] for c in need]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
