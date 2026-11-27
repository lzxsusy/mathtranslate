"""Rebuild a clean slide deck PDF from the corpus blocks.

Every block in the .jsonl carries the frame it came from; we crop the viewer
chrome away, upscale a touch, and write one PDF page per block. Duplicate
PowerPoint builds were already collapsed by merge_corpus.py, so the result is
the deck as the speaker actually stepped through it.

usage: python make_pdf.py <corpus.jsonl> <frames_dir> <out.pdf>
"""
import json, os, sys
from PIL import Image


BOX = (161, 33, 1277, 866)          # white page inside the 1440x900 capture
CHROME = [(484, 776, 672, 833),      # PDF viewer "Page N of M" pill
          (705, 800, 1120, 833)]     # viewer toolbar icons (bottom right)


def page_box(img, margin=0):
    """The capture is a fixed 1440x900 window; the page sits at a constant place."""
    return BOX


def strip_chrome(img):
    """Paint over the viewer overlay so the deck looks like a real slide."""
    from PIL import ImageDraw
    d = ImageDraw.Draw(img)
    for x0, y0, x1, y1 in CHROME:
        d.rectangle([x0, y0, x1, y1], fill=(255, 255, 255))
    return img


def longest_run(vals, step):
    """Longest contiguous run of sampled indices (ignores stray 1-2 row strips)."""
    if not vals:
        return None
    best = cur = (vals[0], vals[0])
    for v in vals[1:]:
        if v - cur[1] <= step:
            cur = (cur[0], v)
        else:
            best = cur if cur[1] - cur[0] > best[1] - best[0] else best
            cur = (v, v)
    best = cur if cur[1] - cur[0] > best[1] - best[0] else best
    return best


def main():
    src, frames, out = sys.argv[1], sys.argv[2], sys.argv[3]
    recs = [json.loads(l) for l in open(src, encoding='utf-8')]
    pages, box = [], None
    for r in recs:
        f = r.get('frame') or ''
        p = os.path.join(frames, f) if f else ''
        if not p or not os.path.exists(p):
            continue
        im = Image.open(p).convert('RGB')
        if box is None:
            box = page_box(im)
        c = strip_chrome(im.crop(box))
        if c.width < 1100:
            s = 1400 / c.width
            c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
        pages.append(c)
    if not pages:
        print('no frames found'); return
    pages[0].save(out, save_all=True, append_images=pages[1:], resolution=150.0)
    print(f'{len(pages)} pages -> {out}  (crop box {box}, size {pages[0].size})')


if __name__ == '__main__':
    main()
