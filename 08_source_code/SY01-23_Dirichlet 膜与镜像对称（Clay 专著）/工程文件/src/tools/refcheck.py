# -*- coding: utf-8 -*-
"""Verify that every printed number equals the number hardcoded in its label.

The translation keeps the original book's numbering by letting counters count
normally and writing display text by hand (\\BookEqRef{...}{2.83}).  If one
numbered object is missing or extra, every later number in that chapter shifts
silently.  main.aux records what was actually printed, so compare.
"""
import re, os, collections, io

AUX = r"<本地路径>"
text = open(AUX, encoding="utf-8", errors="replace").read()

# \newlabel{key}{{printed}{page}...}
pat = re.compile(r"\\newlabel\{([^{}]*)\}\{\{([^{}]*)\}\{([^{}]*)\}")
entries = pat.findall(text)
print("labels in aux:", len(entries))

# label key forms: eq:2.83 thm:2.19 fig:2.32 sec:2.1 ex:2.42 def:3.5 exer:2.1 ...
keypat = re.compile(r"^([a-zA-Z]+):(\d+)\.([^.}]+)$")

bad = []
ok = 0
skipped = []
bytype = collections.Counter()
for key, printed, page in entries:
    m = keypat.match(key)
    if not m:
        skipped.append(key)
        continue
    typ, ch, num = m.group(1), m.group(2), m.group(3)
    bytype[typ] += 1
    # printed may contain formatting; expected: CH.num   (num may itself contain dots, e.g. 3.3.4 for sections)
    if not num.isdigit():
        skipped.append(key)
        continue
    expected = num if typ in ("fig", "tab") else ch + "." + num
    got = printed.strip()
    # hyperref may append extra tokens; keep first token
    got1 = got.split()[0] if got.split() else got
    if got1 == expected or got.endswith(expected) or got.startswith(expected):
        ok += 1
    else:
        bad.append((key, expected, got))

print("checked:", ok + len(bad), "ok:", ok, "mismatch:", len(bad), "skipped:", len(skipped))
print("by type:", dict(bytype))

out = io.StringIO()
out.write("key | expected | printed\n")
for key, expected, got in bad:
    out.write("%s | %s | %s\n" % (key, expected, got))
open(r"<本地路径>", "w", encoding="utf-8").write(out.getvalue())
print(out.getvalue()[:3000])
if skipped[:10]:
    print("skipped sample:", skipped[:10])

