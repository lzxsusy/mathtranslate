# -*- coding: utf-8 -*-
"""Split full.txt into one source file per lecture (chunk), and emit a page map.

Chunk boundaries = lines matching  ^<n>. Day <d> Lecture <k> ...
Outputs:
  工程文件/work/原文/chNN.txt          (UTF-8, starts with the heading line)
  工程文件/work/原文/chunk_map.tsv     (no|heading|start_line|end_line|start_page|end_page)
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = r"C:\Users\admin\Downloads\BenZvi_LD_work\full.txt"
OUT = os.path.normpath(os.path.join(HERE, "..", "work", "原文"))

HEAD = re.compile(r"^(\d{1,2})\.\s+Day\s+(\d)\s+Lecture\s+(\d)(.*)$")
PAGE = re.compile(r"^===== PDF PAGE (\d+) =====$")


def main() -> None:
    with open(SRC, encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    page_of_line = []
    page = 0
    for ln in lines:
        m = PAGE.match(ln)
        if m:
            page = int(m.group(1))
        page_of_line.append(page)

    heads = []
    for i, ln in enumerate(lines):
        m = HEAD.match(ln)
        if m:
            heads.append((i, int(m.group(1)), ln.strip()))

    os.makedirs(OUT, exist_ok=True)
    rows = []
    for k, (i, num, text) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        name = "ch%02d.txt" % (k + 1)
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines[i:end]) + "\n")
        p0, p1 = page_of_line[i], page_of_line[end - 1]
        rows.append((k + 1, num, name, i + 1, end, p0, p1, text))

    with open(os.path.join(OUT, "chunk_map.tsv"), "w", encoding="utf-8") as fh:
        fh.write("chunk\tsection\tfile\tline0\tline1\tpage0\tpage1\theading\n")
        for r in rows:
            fh.write("\t".join(str(x) for x in r) + "\n")

    for r in rows:
        print("ch%02d sec%-2s %s L%-5d-%-5d p%s-%s | %s" % (r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7][:70]))
    print("chunks:", len(rows))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
