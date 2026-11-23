# -*- coding: utf-8 -*-
"""A3 Nam2026: 版面感知抽取 + 页面渲染
用法:
  python extract.py text      -> full_marked.txt (上标 ^ {...} / 下标 _ {...})
  python extract.py pages 10 16  -> work/pages/p010.png ... 200dpi
"""
import sys, os, statistics
import fitz

PDF = r"C:\Users\admin\Desktop\待翻译\A3_Nam2026_走向驯顺分歧的几何朗兰兹对应.pdf"
HERE = os.path.dirname(os.path.abspath(__file__))


def marked_text():
    doc = fitz.open(PDF)
    out = []
    for pno in range(doc.page_count):
        page = doc[pno]
        out.append("===== PDF PAGE %d =====" % (pno + 1))
        d = page.get_text("rawdict")
        for blk in d["blocks"]:
            if blk.get("type") != 0:
                continue
            for line in blk["lines"]:
                spans = [s for s in line["spans"] if s.get("chars")]
                if not spans:
                    continue
                sizes = [s["size"] for s in spans]
                med = statistics.median(sizes)
                base = max(s["origin"][1] for s in spans)
                runs = []  # [kind, text]，kind ∈ {None,'^','_'}
                prev_x1, prev_size = None, None
                for s in spans:
                    t = "".join(c["c"] for c in s["chars"])
                    small = s["size"] < 0.78 * med
                    kind = None
                    if small:
                        kind = "^" if s["origin"][1] <= base - 0.15 * med else "_"
                    gap = (prev_x1 is not None
                           and s["bbox"][0] - prev_x1 > 0.22 * (prev_size or med))
                    if runs and runs[-1][0] == kind:
                        runs[-1][1] += (" " if gap else "") + t
                    else:
                        runs.append([kind, (" " if (gap and runs) else "") + t])
                    prev_x1, prev_size = s["bbox"][2], s["size"]
                parts = runs
                buf = []
                for k, txt in parts:
                    txt = txt.rstrip("\n")
                    if k == "^":
                        buf.append("^{%s}" % txt)
                    elif k == "_":
                        buf.append("_{%s}" % txt)
                    else:
                        buf.append(txt)
                out.append("".join(buf).rstrip())
    open(os.path.join(HERE, "full_marked.txt"), "w", encoding="utf-8").write("\n".join(out))
    print("wrote full_marked.txt", len(out), "lines")


def render(nums, dpi=200):
    doc = fitz.open(PDF)
    os.makedirs(os.path.join(HERE, "pages"), exist_ok=True)
    for n in nums:
        page = doc[n - 1]
        pix = page.get_pixmap(dpi=dpi)
        p = os.path.join(HERE, "pages", "p%03d.png" % n)
        pix.save(p)
        print(p, pix.width, "x", pix.height)


if __name__ == "__main__":
    if sys.argv[1] == "text":
        marked_text()
    else:
        render([int(a) for a in sys.argv[2:]])
