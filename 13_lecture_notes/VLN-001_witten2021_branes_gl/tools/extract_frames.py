"""Extract stable 'slide' frames from a lecture video.

Single decode pass. Samples ~1 frame/sec, computes a 64x36 gray fingerprint,
and saves a full-res JPEG whenever the screen content changes enough.
Also writes index.json (times, hashes, diff scores).
"""
import sys, os, json, time
import numpy as np
import av
from PIL import Image

def fingerprint(img_rgb: Image.Image) -> np.ndarray:
    return np.asarray(img_rgb.convert('L').resize((64, 36), Image.BILINEAR), dtype=np.int16)

def changed(prev, cur, thr=0.004, lvl=16):
    if prev is None:
        return 1.0
    d = np.abs(cur - prev) > lvl
    return float(d.mean())

def main():
    src = sys.argv[1]
    outdir = sys.argv[2]
    sample_fps = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
    thr = float(sys.argv[4]) if len(sys.argv) > 4 else 0.004
    os.makedirs(outdir, exist_ok=True)
    container = av.open(src, options={'threads': 'auto'})
    vs = container.streams.video[0]
    vs.thread_type = 'AUTO'
    tb = float(vs.time_base)
    step = max(1, int(round(float(vs.average_rate) / sample_fps)))
    print(f"stream: {vs.codec_context.name} {vs.codec_context.width}x{vs.codec_context.height} "
          f"fps={float(vs.average_rate):.2f} frames={vs.frames} step={step}", flush=True)

    prev_fp = None
    kept = []
    idx = 0
    t0 = time.time()
    for frame in container.decode(vs):
        if idx % step == 0:
            img = frame.to_image()          # RGB PIL image, full res
            fp = fingerprint(img)
            sc = changed(prev_fp, fp, thr)
            if prev_fp is None or sc > thr:
                ts = float(frame.pts * tb) if frame.pts is not None else idx / float(vs.average_rate)
                name = f"f{len(kept):04d}_t{int(ts):05d}.jpg"
                img.save(os.path.join(outdir, name), quality=88)
                kept.append({'file': name, 't': round(ts, 2), 'score': round(sc, 5),
                             'w': img.width, 'h': img.height})
                prev_fp = fp
                print(f"[{ts:8.1f}s] saved {name} score={sc:.4f}  ({len(kept)} kept)", flush=True)
            else:
                prev_fp = (prev_fp * 0.5 + fp * 0.5).astype(np.int16)  # slow drift tracking
        idx += 1
        if idx % 2500 == 0:
            el = time.time() - t0
            print(f"... {idx} frames, {el:.0f}s elapsed, {idx/el:.0f} fps decode", flush=True)
    json.dump(kept, open(os.path.join(outdir, 'index.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f"DONE: {len(kept)} frames from {idx} decoded in {time.time()-t0:.0f}s")

if __name__ == '__main__':
    main()
