"""Sequential page segmentation for slide-based lecture videos.

Frames are already deduplicated by the extractor; here we walk them in time
order and cut a new page whenever the ink layout (Jaccard on a binarised
crop of the page area) drops below TH against the current page's richest frame.

usage: python segment_pages.py <frames_dir> [TH] [MERGE]
Writes <frames_dir>/slides.json  [{page,t0,t1,rep,n,ink}]
"""
import json, os, sys
import numpy as np
from PIL import Image

D = sys.argv[1] if len(sys.argv) > 1 else 'frames_p04'
TH = float(sys.argv[2]) if len(sys.argv) > 2 else 0.55
MERGE = float(sys.argv[3]) if len(sys.argv) > 3 else 0.88

items = json.load(open(os.path.join(D, 'index.json'), encoding='utf-8'))


def detect_page_box(path, margin=2):
    """Bounding box of the bright (page) area, found from a representative frame."""
    g = np.asarray(Image.open(path).convert('L'), dtype=np.uint8)
    bright = g > 200
    rows = np.where(bright.mean(axis=1) > 0.5)[0]
    cols = np.where(bright.mean(axis=0) > 0.5)[0]
    if len(rows) < 10 or len(cols) < 10:
        h, w = g.shape
        return int(w * .12), int(h * .05), int(w * .88), int(h * .96)
    return (int(cols[0]) + margin, int(rows[0]) + margin,
            int(cols[-1]) - margin, int(rows[-1]) - margin)


L, T, R, B = detect_page_box(os.path.join(D, items[len(items) // 2]['file']))
print(f'page box: L={L} T={T} R={R} B={B}')


def load(p):
    im = Image.open(os.path.join(D, p)).convert('L').crop((L, T, R, B))
    g = np.asarray(im.resize((384, 288), Image.BILINEAR), dtype=np.uint8)
    return g < 150


M = {it['file']: load(it['file']) for it in items}


def jac(a, b):
    return float(np.logical_and(a, b).sum()) / max(np.logical_or(a, b).sum(), 1)


pages, cur = [], None
for it in items:
    f = it['file']
    if cur is not None:
        j = jac(M[f], M[cur['rep']])
        if j >= TH:
            cur['files'].append(f)
            cur['t1'] = it['t']
            if M[f].sum() > M[cur['rep']].sum():
                cur['rep'] = f
            continue
    cur = {'rep': f, 'files': [f], 't0': it['t'], 't1': it['t']}
    pages.append(cur)

# merge pages that come back to a previous layout (very similar reps)
merged = []
for p in pages:
    hit = None
    for q in merged:
        if jac(M[p['rep']], M[q['rep']]) >= MERGE:
            hit = q
            break
    if hit is not None and abs(hit['t0'] - p['t0']) < 600:
        hit['files'] += p['files']
        hit['t1'] = max(hit['t1'], p['t1'])
        continue
    merged.append(p)

out = []
for i, p in enumerate(merged):
    out.append(dict(page=i, t0=round(p['t0'], 1), t1=round(p['t1'], 1),
                    rep=p['rep'], n=len(p['files']),
                    ink=round(float(M[p['rep']].mean()), 4)))
json.dump(out, open(os.path.join(D, 'slides.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=0)
print(f'{len(items)} frames -> {len(pages)} runs -> {len(out)} pages  '
      f'({os.path.join(D, "slides.json")})')
