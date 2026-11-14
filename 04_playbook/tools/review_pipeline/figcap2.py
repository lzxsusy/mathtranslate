# -*- coding: utf-8 -*-
"""Audit figure captions: compare original caption text with our tex captions.

v2: truncate tex tail at \\end{figure}; parse original caption line from the
layout text (a caption line starts with "Figure N."); handle unnumbered
diagram crops named ChNN_Diagram_PDFpXXX_II_BookpYYY.pdf.
"""
import os, re, io

ROOT = r"<本地路径>"
PROJ = os.path.join(ROOT, "Dirichlet-Mirror-Symmetry-zh")
FIGS = os.path.join(PROJ, "figures")
FULL = os.path.join(ROOT, "original", "full.txt")

pages = open(FULL, encoding="utf-8").read().split("\f")

tex_chunks = {}
for f in os.listdir(os.path.join(PROJ, "chapters")):
    if f.endswith(".tex"):
        tex_chunks[f] = open(os.path.join(PROJ, "chapters", f), encoding="utf-8").read()

img_index = {}
for name, text in tex_chunks.items():
    for m in re.finditer(r"\\BookImage\{([^}]*)\}", text):
        base = os.path.basename(m.group(1).strip())
        img_index[base] = (name, m.start())

def orig_caption(page, fignum):
    """Return caption text of Figure fignum on the page ('' if none)."""
    lines = page.splitlines()
    pat = re.compile(r"^\s*Figure\s+" + str(fignum) + r"\s*(\.|$)")
    for i, line in enumerate(lines):
        m = pat.match(line)
        if not m:
            continue
        parts = [m.string[m.end():].strip()]
        j = i + 1
        # continuation lines: stop at blank line or next "Figure N"
        while j < len(lines):
            nxt = lines[j]
            if not nxt.strip():
                break
            if re.match(r"^\s*Figure\s+\d+", nxt):
                break
            parts.append(nxt.strip())
            j += 1
        text = " ".join(p for p in parts if p)
        return text
    return None  # caption line not found

rows = []
for dirpath, dirs, files in os.walk(FIGS):
    for f in files:
        if not f.endswith(".pdf"):
            continue
        m = re.match(r"Ch(\d+)_(?:Fig(\d+)_|Diagram_)?PDFp(\d+)(?:_(\d+))?_Bookp(\d+)", f)
        if not m:
            rows.append((f, None, None, "NAME?", "", "NOT-IN-TEX", ""))
            continue
        ch, fignum, pdfp = m.group(1), m.group(2), int(m.group(3))
        page = pages[pdfp - 1] if pdfp - 1 < len(pages) else ""
        if fignum:
            cap = orig_caption(page, int(fignum))
            numshow = "F" + fignum if cap is not None else "F%s-NOTFOUND" % fignum
        else:
            cap = ""
            numshow = "unnum"
        info = img_index.get(f)
        if not info:
            rows.append((f, ch, pdfp, numshow, cap or "", "NOT-IN-TEX", ""))
            continue
        texname, pos = info
        pre = tex_chunks[texname][max(0, pos - 300):pos]
        in_fig = pre.rfind("\\begin{figure}") > pre.rfind("\\end{figure}")
        end = tex_chunks[texname].find("\\end{figure}", pos) if in_fig else pos
        tail = tex_chunks[texname][pos:end if (in_fig and end > 0) else pos + 5]
        if "\\BookNumberOnlyCaption" in tail:
            texcap = "NUMBERONLY"
        else:
            cm = re.search(r"\\caption\{", tail)
            if not cm:
                texcap = "NOCAPTION"
            else:
                i = cm.end() - 1
                depth, j = 0, i
                while j < len(tail):
                    if tail[j] == "{":
                        depth += 1
                    elif tail[j] == "}":
                        depth -= 1
                        if depth == 0:
                            break
                    j += 1
                texcap = tail[i + 1:j].replace("\n", " ")
        rows.append((f, ch, pdfp, numshow, cap or "", texname, texcap))

rows.sort(key=lambda r: (str(r[1]).zfill(3), str(r[0])))

out = io.StringIO()
by_ch = {}
for r in rows:
    by_ch.setdefault(r[1], []).append(r)

def mismatch(r):
    f, ch, pdfp, numshow, cap, texname, texcap = r
    if texname in ("NOT-IN-TEX",) or numshow == "NAME?":
        return True
    if numshow != "unnum":
        has_orig_text = bool(cap.strip())
        our_text = texcap not in ("NUMBERONLY", "NOCAPTION", "")
        if has_orig_text and not our_text:
            return True
        if (not has_orig_text) and our_text:
            return True
    else:
        # unnumbered diagram: our text should also be absent
        if texcap not in ("NUMBERONLY", "NOCAPTION", ""):
            return True
    return False

counts = {}
for ch in sorted(by_ch, key=lambda c: str(c)):
    rs = by_ch[ch]
    bad = [r for r in rs if mismatch(r)]
    counts[ch] = (len(rs), len(bad))
    out.write("\n#### chapter %s : %d figures, %d suspicious\n" % (ch, len(rs), len(bad)))
    for r in bad:
        out.write("  %s | orig:%s | %s\n" % (r[0], r[3], r[4][:100]))
        out.write("      tex: %s | %s\n" % (r[5], (r[6] or "")[:100]))

out.write("\n#### summary\n")
for ch in sorted(counts, key=lambda c: str(c)):
    out.write("ch%s figures=%d suspicious=%d\n" % (ch, counts[ch][0], counts[ch][1]))
out.write("\n#### all rows\n")
for r in rows:
    out.write("%s | %s | %s | %s\n" % (r[0], r[3], (r[4] or "")[:60].replace("\n", " "), (r[6] or "")[:60].replace("\n", " ")))

txt = out.getvalue()
open(os.path.join(ROOT, "review", "figcap_report.txt"), "w", encoding="utf-8").write(txt)
print(txt[:5000])


