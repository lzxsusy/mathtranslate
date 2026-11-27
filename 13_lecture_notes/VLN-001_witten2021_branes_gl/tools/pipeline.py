"""Video (PPT-style online lecture) -> trainable text corpus.

Two phases, because the middle step needs a vision model:

  prep   download + audio + frames + slide segmentation + ASR + transcription batches
  merge  (after the batches have been transcribed into slides_tx/*.json)
         collapse PowerPoint builds, attach narration, emit .md + .jsonl

Examples
  python pipeline.py prep --url BV1b34y1Q7Ah --part 4 --slug witten --pages-per-batch 20
  python pipeline.py merge --slug witten --tx slides_tx --out corpus/witten \
         --title "..." --speaker "..." --date "..." --url "..."

Everything runs on local tools only: yt-dlp (download), PyAV (decode), Pillow/numpy
(frame analysis), faster-whisper (ASR). No system ffmpeg is required.
"""
import argparse, json, os, subprocess, sys, glob

PY = sys.executable
HERE = os.path.dirname(os.path.abspath(__file__))


def run(cmd, **kw):
    print('+', ' '.join(str(c) for c in cmd), flush=True)
    subprocess.run(cmd, check=True, **kw)


def prep(a):
    slug = a.slug
    os.makedirs(slug, exist_ok=True)
    url = a.url if a.url.startswith('http') else f'https://www.bilibili.com/video/{a.url}'
    if a.part:
        url += f'?p={a.part}'

    video = os.path.join(slug, 'video.mp4')
    audio = os.path.join(slug, 'audio.m4a')
    if not os.path.exists(video) or not os.path.exists(audio):
        run([PY, '-m', 'yt_dlp', '-f', a.video_format, '-o', video, url])
        run([PY, '-m', 'yt_dlp', '-f', a.audio_format, '-o', audio, url])

    frames = os.path.join(slug, 'frames')
    if not os.path.exists(os.path.join(frames, 'index.json')):
        run([PY, os.path.join(HERE, 'extract_frames.py'), video, frames])
    run([PY, os.path.join(HERE, 'segment_pages.py'), frames])

    asr = os.path.join(slug, 'asr.json')
    if not os.path.exists(asr):
        run([PY, os.path.join(HERE, 'chunk_transcribe.py'), audio,
             os.path.join(slug, 'asr_raw'), a.model, str(a.chunks)])
        # chunk_transcribe may lose a chunk; merge whatever exists
        rows = []
        for f in sorted(glob.glob(os.path.join(slug, 'asr_raw_chunk*.json'))):
            rows += json.load(open(f, encoding='utf-8'))
        rows.sort(key=lambda r: r['start'])
        json.dump(rows, open(asr, 'w', encoding='utf-8'), ensure_ascii=False)
    run([PY, os.path.join(HERE, 'clean_asr.py'), asr, os.path.join(slug, 'asr_clean.json')])

    # batches for the vision transcription step
    slides = json.load(open(os.path.join(frames, 'slides.json'), encoding='utf-8'))
    bdir = os.path.join(HERE, 'batches')
    os.makedirs(bdir, exist_ok=True)
    for f in glob.glob(os.path.join(bdir, 'b*.json')):
        os.remove(f)
    recs = [dict(page=s['page'], t=s['t0'], file=os.path.abspath(os.path.join(frames, s['rep'])))
            for s in slides]
    n = a.pages_per_batch
    for i in range(0, len(recs), n):
        p = os.path.join(bdir, f'b{i//n:02d}.json')
        json.dump(recs[i:i + n], open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        print('batch ->', p)
    print(f'\n{len(slides)} slides. Transcribe batches/*.json with the vision model into '
          f'slides_tx/bNN.json, then run the merge phase.')


def merge(a):
    args = [PY, os.path.join(HERE, 'merge_corpus.py'), '--out', a.out,
            '--tx', a.tx, '--asr', a.asr,
            '--frames', os.path.join(a.slug, 'frames')]
    run(args)
    md = a.out + '.md'
    if os.path.exists(md):
        print('wrote', md)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('prep')
    p.add_argument('--url', required=True, help='BV id or full url')
    p.add_argument('--part', type=int, default=None)
    p.add_argument('--slug', required=True)
    p.add_argument('--video-format', default='30080')
    p.add_argument('--audio-format', default='30280')
    p.add_argument('--model', default='small.en')
    p.add_argument('--chunks', type=int, default=6)
    p.add_argument('--pages-per-batch', type=int, default=20)
    p.set_defaults(func=prep)

    m = sub.add_parser('merge')
    m.add_argument('--slug', required=True)
    m.add_argument('--tx', default='slides_tx')
    m.add_argument('--asr', default='asr_p04_clean.json')
    m.add_argument('--out', required=True)
    m.set_defaults(func=merge)

    a = ap.parse_args()
    a.func(a)


if __name__ == '__main__':
    main()
