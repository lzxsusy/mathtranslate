# -*- coding: utf-8 -*-
"""Collapse doubled LaTeX backslashes in generated cards."""
import glob
import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAT = re.compile(r"\\{2,}")


def norm(x):
    if isinstance(x, str):
        return PAT.sub(lambda m: "\\" * (len(m.group(0)) // 2), x)
    if isinstance(x, list):
        return [norm(v) for v in x]
    if isinstance(x, dict):
        return {k: norm(v) for k, v in x.items()}
    return x


for path in sorted(glob.glob(os.path.join(ROOT, "cards", "concepts", "*.json"))):
    with io.open(path, encoding="utf-8") as f:
        data = json.load(f)
    with io.open(path, "w", encoding="utf-8") as f:
        json.dump(norm(data), f, ensure_ascii=False, indent=2)
        f.write("\n")
print("normalized", len(glob.glob(os.path.join(ROOT, "cards", "concepts", "*.json"))), "cards")
