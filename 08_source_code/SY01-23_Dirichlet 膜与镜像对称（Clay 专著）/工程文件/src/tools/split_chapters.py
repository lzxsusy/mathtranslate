# -*- coding: utf-8 -*-
"""Split ch03.tex / ch05.tex into two part files for parallel proofreading.
Keeps line endings byte-identical; splits only at a \\SourceParagraph boundary line start.
Writes review/_split_map.txt documenting the mapping.
"""
import os, io

ROOT = r"C:\Users\admin\Downloads\DBMS_work\Dirichlet-Mirror-Symmetry-zh"
CH = os.path.join(ROOT, "chapters")
os.makedirs(os.path.join(ROOT, "review"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "review", "orig_backup"), exist_ok=True)

# split_line is 1-based: first line of part2
targets = {
    "ch03.tex": 2279,
    "ch05.tex": 2221,
}

map_lines = []
for fn, split_line in targets.items():
    src = os.path.join(CH, fn)
    with io.open(src, "r", encoding="utf-8", newline="") as f:
        data = f.read()
    # split into lines preserving endings
    lines = data.splitlines(keepends=True)
    assert len(lines) >= split_line, (fn, len(lines))
    # sanity: part2 must start with \SourceParagraph
    assert lines[split_line - 1].startswith("\\SourceParagraph"), (fn, lines[split_line - 1][:80])
    base = fn[:-4]
    p1, p2 = base + "a.tex", base + "b.tex"
    with io.open(os.path.join(CH, p1), "w", encoding="utf-8", newline="") as f:
        f.write("".join(lines[:split_line - 1]))
    with io.open(os.path.join(CH, p2), "w", encoding="utf-8", newline="") as f:
        f.write("".join(lines[split_line - 1:]))
    # back up the original, remove from build path
    os.replace(src, os.path.join(ROOT, "review", "orig_backup", fn))
    map_lines.append("%s: %d lines; split at line %d; %s = L1..L%d, %s = orig L%d..L%d"
                     % (fn, len(lines), split_line, p1, split_line - 1, p2, split_line, len(lines)))
    print(map_lines[-1])

# record global offsets for align-file line numbers
with io.open(os.path.join(ROOT, "review", "_split_map.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(map_lines) + "\n")
    f.write("\nch03b.tex line = ch03.tex line - 2278\n")
    f.write("ch05b.tex line = ch05.tex line - 2220\n")
print("done")
