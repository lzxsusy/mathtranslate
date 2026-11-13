# -*- coding: utf-8 -*-
"""JP11 pre-delivery self-check: tag counts / per-section continuity / env balance / encoding.
Usage:
    python check.py          # whole book
    python check.py c05      # one chunk only
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CHUNKS = os.path.join(ROOT, "src", "chunks")

EXPECT = {
    "c00": (1, "1.1", "1.1"),
    "c01": (5, "1.2", "3.2"),
    "c02": (15, "3.3", "4.14"),
    "c03": (15, "4.15", "4.29"),
    "c04": (14, "5.1", "6.1"),
    "c05": (13, "6.2", "7.5"),
    "c06": (14, "7.6", "8.10"),
    "c07": (13, "8.11", "8.23"),
    "c08": (9, "8.24", "8.32"),
    "c09": (0, "-", "-"),
}

tag_re = re.compile(r"<本地路径>)\.(\d+)\}")


def check_chunk(name):
    path = os.path.join(CHUNKS, name + ".tex")
    if not os.path.exists(path):
        print("[MISSING] %s.tex" % name)
        return None
    raw = open(path, "rb").read()
    problems = []
    if raw.startswith(b"\xef\xbb\xbf"):
        problems.append("has BOM")
    if b"\r" in raw:
        problems.append("has CR")
    text = raw.decode("utf-8")
    tags = tag_re.findall(text)
    n_exp = EXPECT[name][0]
    if len(tags) != n_exp:
        problems.append("tag count %d != %d" % (len(tags), n_exp))
    begins = re.findall(r"<本地路径>*?)\}", text)
    ends = re.findall(r"<本地路径>*?)\}", text)
    for env in set(begins) | set(ends):
        if begins.count(env) != ends.count(env):
            problems.append("env %s: %d begin / %d end" % (env, begins.count(env), ends.count(env)))
    body = "\n".join(l for l in text.splitlines() if not l.strip().startswith("%"))
    body = body.replace("\\$", "")
    if body.count("$") % 2:
        problems.append("unbalanced $")
    if "**" in body:
        problems.append("markdown bold left in")
    for m in re.finditer(r"\$([^$]*)\$", body):
        if "\uff08" in m.group(1) or "\uff09" in m.group(1):
            problems.append("full-width paren inside math")
            break
    secs = re.findall(r"<本地路径>]*)\}", text)
    subs = re.findall(r"<本地路径>]*)\}", text)
    return {
        "name": name,
        "tags": len(tags),
        "problems": problems,
        "first": "%s.%s" % tags[0] if tags else "-",
        "last": "%s.%s" % tags[-1] if tags else "-",
        "tags_list": tags,
        "sections": secs,
        "subsections": subs,
        "figures": re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", text),
    }


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    names = [only] if only else sorted(EXPECT)
    total = 0
    alltags = []
    secs, subs, figs = [], [], []
    ok = True
    for name in names:
        r = check_chunk(name)
        if r is None:
            ok = False
            continue
        total += r["tags"]
        alltags.extend(r["tags_list"])
        secs.extend(r["sections"])
        subs.extend(r["subsections"])
        figs.extend(r["figures"])
        if r["problems"]:
            ok = False
        flag = "OK " if not r["problems"] else "ERR"
        print("%s %s: tags=%d (%s..%s) %s" % (
            flag, name, r["tags"], r["first"], r["last"],
            "; ".join(r["problems"])))
    if only:
        # per-section continuity within this chunk only
        bysec = {}
        for a, b in alltags:
            bysec.setdefault(int(a), []).append(int(b))
        for s in sorted(bysec):
            got = sorted(bysec[s])
            print("  section %d tags: %s" % (s, got))
    else:
        print("\nTOTAL tags = %d (expect 99)" % total)
        bysec = {}
        for a, b in alltags:
            bysec.setdefault(int(a), []).append(int(b))
        for s in sorted(bysec):
            got = sorted(bysec[s])
            if got != list(range(1, len(got) + 1)):
                print("  [WARN] section %d numbering gap: %s" % (s, got))
                ok = False
        print("sections:", secs)
        print("subsections:", subs)
        print("figures:", figs)
        if len(secs) != 8:
            print("  [WARN] expect 8 \\section, got %d" % len(secs))
            ok = False
        if len(subs) != 4:
            print("  [WARN] expect 4 \\subsection, got %d" % len(subs))
            ok = False
    print("\n" + ("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
