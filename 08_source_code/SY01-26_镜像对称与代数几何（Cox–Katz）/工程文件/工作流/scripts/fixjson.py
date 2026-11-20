import json, sys, io

VALID = set('"\\/bfnrtu')


def repair(text):
    out = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c != "\\":
            out.append(c)
            i += 1
            continue
        if i + 1 >= n:
            out.append("\\\\")
            i += 1
            continue
        nxt = text[i + 1]
        if nxt in VALID:
            out.append(c)
            out.append(nxt)
            i += 2
        else:
            out.append("\\\\")
            out.append(nxt)
            i += 2
    return "".join(out)


for path in sys.argv[1:]:
    raw = io.open(path, encoding="utf-8").read()
    try:
        data = json.loads(raw)
        print(path, "ok", len(data.get("issues", [])))
        continue
    except Exception as exc:
        print(path, "repairing:", exc)
    data = json.loads(repair(raw))
    io.open(path, "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, indent=2))
    print(path, "repaired", len(data.get("issues", [])))
