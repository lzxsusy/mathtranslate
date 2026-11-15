# -*- coding: utf-8 -*-
"""统一语料 schema：flags 恒为数组、seg 恒存在（空串=旧口径），不改 text 因而 para_id 不变。"""
import io, json, shutil, os, datetime
P = "zh_paragraphs.jsonl"
stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
bak = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath("."))), "_corpus_backups", "schema_%s" % stamp)
os.makedirs(bak, exist_ok=True)
shutil.copy2(P, os.path.join(bak, os.path.basename(P)))
print("backup ->", bak)
n = added_flags = added_seg = 0
tmp = P + ".tmp"
with io.open(P, encoding="utf-8") as f, io.open(tmp, "w", encoding="utf-8", newline="\n") as g:
    for line in f:
        line = line.strip()
        if not line:
            continue
        d = json.loads(line)
        n += 1
        if "flags" not in d:
            d["flags"] = []
            added_flags += 1
        if "seg" not in d:
            d["seg"] = ""
            added_seg += 1
        g.write(json.dumps(d, ensure_ascii=False) + "\n")
os.replace(tmp, P)
print("rows", n, "| +flags", added_flags, "| +seg", added_seg)
