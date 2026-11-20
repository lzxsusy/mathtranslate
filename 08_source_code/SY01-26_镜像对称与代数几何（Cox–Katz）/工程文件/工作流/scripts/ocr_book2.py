import os, sys, time
os.environ["OMP_NUM_THREADS"] = "2"
os.environ["ORT_NUM_THREADS"] = "2"
from concurrent.futures import ProcessPoolExecutor

PDF = r"C:\Users\admin\Desktop\归档\08_教材与参考书\Mirrorsymmetryandalgebraicgeometry(DavidA.Cox)(Z-Library).pdf"
OUT = r"C:\Users\admin\Downloads\_mirror_review\ocr2"
os.makedirs(OUT, exist_ok=True)

_engine = None
_doc = None

def init():
    global _engine, _doc
    import pymupdf
    from rapidocr_onnxruntime import RapidOCR
    _engine = RapidOCR()
    _doc = pymupdf.open(PDF)

def work(p):
    import numpy as np
    out = os.path.join(OUT, f"p{p:03d}.txt")
    if os.path.exists(out) and os.path.getsize(out) > 50:
        return p, 0
    page = _doc[p-1]
    pix = page.get_pixmap(dpi=300)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    if pix.n == 1:
        img = np.repeat(img, 3, axis=2)
    elif pix.n == 4:
        img = img[:, :, :3]
    t0 = time.time()
    res, _ = _engine(img, det_limit_side_len=1600)
    lines = []
    if res:
        for box, text, score in res:
            if score is None or score < 0.3 or not text.strip():
                continue
            lines.append((box[0][1], box[0][0], text))
    lines.sort()
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(t for _, _, t in lines))
    return p, time.time()-t0

if __name__ == "__main__":
    pages = list(range(13, 496))
    t0 = time.time()
    done = 0
    with ProcessPoolExecutor(max_workers=8, initializer=init) as ex:
        for p, dt in ex.map(work, pages, chunksize=1):
            done += 1
            if done % 20 == 0:
                print(f"{done}/{len(pages)} page {p} {dt:.1f}s elapsed {time.time()-t0:.0f}s", flush=True)
    print("ALL DONE", time.time()-t0, flush=True)
