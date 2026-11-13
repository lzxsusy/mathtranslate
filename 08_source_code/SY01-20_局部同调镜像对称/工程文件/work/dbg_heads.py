import io, re
t = io.open(r"<本地路径>", encoding="utf-8").read()
parts = re.split(r"===== PDF PAGE (\d+) =====", t)
pages = {}
for k in range(1, len(parts), 2):
    pages[int(parts[k])] = parts[k+1]

heads = ["Introduction", "Proof of the Theorems", "Algebraic Preparations",
         "Fukaya Categories of Discrete Quotients", "G-equivariant sheaves",
         "Twisted K", "Eilenberg", "Question 1.1", "Theorem 1.1", "Corollary 1.2",
         "Theorem 2.1", "Theorem 3.", "Definition 3.", "Lemma 3."]
buf = []
for h in heads:
    hits = [p for p in sorted(pages) if h in pages[p]]
    buf.append("%-45s -> pages %s" % (h, hits[:12]))
io.open(r"<本地路径>", "w", encoding="utf-8").write("\n".join(buf))
