import pymupdf

P = r"<本地路径> and Knots.pdf"
d = pymupdf.open(P)
jobs = [
    (20, (60, 150, 560, 265), "p21_eq326.png"),
    (11, (60, 425, 560, 565), "p12_eq230.png"),
    (19, (60, 60, 560, 200), "p20_etag.png"),
]
for pg, rect, fn in jobs:
    pix = d[pg].get_pixmap(clip=pymupdf.Rect(*rect), dpi=230)
    pix.save("work/" + fn)
    print(fn, pix.width, pix.height)
