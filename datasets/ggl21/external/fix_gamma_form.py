import glob, json, io, sys

sys.stdout.reconfigure(encoding="utf-8")

OLD = r"\epsilon_{\mu\nu\rho}F^{3\rho}+\gamma F_{\mu\nu}=0"
NEW = r"\epsilon^{\lambda\mu\nu}F_{3\lambda}+\gamma F_{\mu\nu}=0"

changed = []


def walk(x, path, hits):
    if isinstance(x, str):
        if OLD in x:
            hits.append(path)
            return x.replace(OLD, NEW)
        return x
    if isinstance(x, list):
        return [walk(v, path + "[%d]" % i, hits) for i, v in enumerate(x)]
    if isinstance(x, dict):
        return {k: walk(v, path + "." + k, hits) for k, v in x.items()}
    return x


for p in sorted(glob.glob("out/21_ggl21/cards/*/*.json")):
    c = json.load(open(p, encoding="utf-8"))
    hits = []
    c2 = walk(c, "", hits)
    if hits:
        with open(p, "w", encoding="utf-8") as f:
            json.dump(c2, f, ensure_ascii=False, indent=2)
            f.write("\n")
        changed.append((p, len(hits)))

for p, n in changed:
    print("fixed", p, n)
print("total files changed:", len(changed))
