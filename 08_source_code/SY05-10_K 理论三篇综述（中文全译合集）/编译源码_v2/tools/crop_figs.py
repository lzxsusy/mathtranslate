# -*- coding: utf-8 -*-
import pymupdf, re, os
src = pymupdf.open(r'C:\Users\admin\Downloads\hep-th_0304018.pdf')
outdir = r'C:\Users\admin\Desktop\数译发布\shuyi\translations\SY05-10\工程文件\v2\moore\src'
os.makedirs(outdir, exist_ok=True)
caps = []
for pno, page in enumerate(src):
    for b in page.get_text('blocks'):
        txt = b[4].strip().replace('\n', ' ')
        if re.match(r'^(Fig\.|Figure)\s*\d+\.', txt):
            m = re.match(r'^(Fig\.|Figure)\s*(\d+)\.', txt)
            caps.append((int(m.group(2)), pno, b))
print('captions', len(caps), [c[0] for c in caps])
for num, pno, b in caps:
    page = src[pno]
    cap = pymupdf.Rect(b[:4])
    drs = [d['rect'] for d in page.get_drawings() if d['rect'].y1 <= cap.y0 + 2 and d['rect'].y0 > cap.y0 - 380]
    if not drs:
        print('NO DRAWINGS', num); continue
    # cluster: start from drawings closest above caption, expand upward while gaps < 25pt
    drs.sort(key=lambda r: r.y1, reverse=True)
    u = pymupdf.Rect(drs[0])
    for r in drs[1:]:
        if u.y0 - r.y1 < 25:
            u |= r
        else:
            break
    # include text blocks (labels) intersecting expanded union
    u.x0 -= 6; u.x1 += 6; u.y0 -= 6; u.y1 = cap.y0 - 2
    for tb in page.get_text('blocks'):
        r = pymupdf.Rect(tb[:4])
        if r.intersects(u) and r.y0 < cap.y0 and not re.match(r'^(Fig\.|Figure)', tb[4].strip()):
            u |= r
    u = pymupdf.Rect(u.x0 - 2, u.y0 - 2, u.x1 + 2, u.y1 + 2)
    # crop as vector pdf
    doc = pymupdf.open()
    w, h = u.width, u.height
    pg = doc.new_page(width=w, height=h)
    pg.show_pdf_page(pg.rect, src, pno, clip=u)
    out = os.path.join(outdir, 'fig%02d.pdf' % num)
    doc.save(out)
    doc.close()
    print(num, 'p', pno + 1, [round(x, 1) for x in u], os.path.getsize(out))
