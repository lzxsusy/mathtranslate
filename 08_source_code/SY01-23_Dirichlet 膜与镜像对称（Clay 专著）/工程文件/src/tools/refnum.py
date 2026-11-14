# -*- coding: utf-8 -*-
"""Check hard-coded display numbers in \\BookRef / \\BookEqRef / \\BookSectionRef
against the label's own number."""
import re, io, glob, os, collections

root = r"C:\Users\admin\Downloads\DBMS_work\Dirichlet-Mirror-Symmetry-zh\chapters"
files = sorted(glob.glob(os.path.join(root, "*.tex")))

pat_ref = re.compile(r"\\BookRef\{([^{}]+)\}\{([^{}]*)\}")
pat_eq = re.compile(r"\\BookEqRef\{([^{}]+)\}\{([^{}]*)\}")
pat_sec = re.compile(r"\\BookSectionRef\{([^{}]+)\}\{([^{}]*)\}")

def norm_num(s):
    s = s.replace("\u3000", " ")
    return re.sub(r"[^0-9.]", "", s)

bad = []
count = collections.Counter()
for f in files:
    s = io.open(f, encoding="utf-8").read()
    for m in pat_ref.finditer(s):
        label, disp = m.group(1), m.group(2)
        count[label.split(":")[0]] += 1
        kind, num = label.split(":", 1)
        ln = norm_num(num)          # e.g. 2.31
        dn = norm_num(disp)         # e.g. 31 (figures/tables print only 2nd part) or 2.13
        if not dn:
            continue
        parts = ln.split(".")
        ok = dn in (ln, parts[-1], ".".join(parts[-2:]))
        if not ok:
            bad.append((os.path.basename(f), label, disp))
    for m in pat_eq.finditer(s):
        label, disp = m.group(1), m.group(2)
        count["eq"] += 1
        num = label.split(":", 1)[1]
        if norm_num(disp) != norm_num(num) and norm_num(num) not in norm_num(disp):
            bad.append((os.path.basename(f), label, disp))
    for m in pat_sec.finditer(s):
        label, disp = m.group(1), m.group(2)
        count["sec"] += 1
        num = label.split(":", 1)[1]
        if norm_num(num) not in norm_num(disp):
            bad.append((os.path.basename(f), label, disp))

print("reference kinds:", dict(count))
print("total BookRef:", sum(v for k, v in count.items()))
print("suspect mismatches:", len(bad))
for b in bad[:40]:
    print("  ", b)
