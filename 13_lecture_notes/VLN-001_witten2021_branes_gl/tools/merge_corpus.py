"""Merge slide transcriptions + ASR into a corpus, keyed by TIME (not page ids).

Inputs
  slides_tx/b*.json  [{page,t,kind,heading,body,figures,notes}]  t = seconds in the video
  asr_p04.json       [{start,end,text}]
  frames_p04/index.json  (optional, for the frame file behind each slide)

The PDF deck exports PowerPoint builds as separate pages, so consecutive records
often repeat the same text with more content appended. We collapse such chains
into one block (keeping the fullest version) and pair it with the narration that
was spoken while it was on screen.

usage: python merge_corpus.py [--out NAME] [--tx slides_tx] [--asr asr_p04.json]
                              [--frames frames_p04] [--no-dedupe]
"""
import os, sys, json, glob, argparse, re

META = {
    'title': 'Quantization by Branes and Geometric Langlands',
    'speaker': 'Edward Witten (IAS)',
    'date': 'February 3, 2021',
    'event': 'Mini-Conference on the Geometric Langlands Correspondence',
    'url': 'https://www.bilibili.com/video/BV1b34y1Q7Ah?p=4',
    'duration': 7493,
}


def hms(t):
    t = max(0, int(t))
    return f"{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}"


def norm(s):
    return re.sub(r'\s+', ' ', (s or '')).strip()


def load_tx(dirpath):
    out = []
    for f in sorted(glob.glob(os.path.join(dirpath, 'b*.json'))):
        try:
            arr = json.load(open(f, encoding='utf-8'))
        except Exception as e:
            print(f'!! {f}: {e}')
            continue
        for r in arr:
            r['t'] = float(r['t'])
            r['body'] = norm(r.get('body', ''))
            out.append(r)
    out.sort(key=lambda r: r['t'])
    return out


def load_asr(path):
    return json.load(open(path, encoding='utf-8')) if os.path.exists(path) else []


def narrate(segs, t0, t1):
    keep = [s for s in segs if s['start'] < t1 and s['end'] > t0]
    if not keep:
        return ''
    return re.sub(r'\s+', ' ', ' '.join(s['text'].strip() for s in keep)).strip()


def collapse(recs):
    """Chain of records where each body extends the previous one -> one block."""
    blocks, cur = [], None
    for r in recs:
        if cur is None:
            cur = dict(recs=[r], t0=r['t'], body=r['body'], best=r)
            continue
        prev = cur['body']
        same = r['body'] and prev and (r['body'].startswith(prev) or prev.startswith(r['body']))
        if same:
            cur['recs'].append(r)
            if len(r['body']) > len(prev):
                cur['body'] = r['body']
                cur['best'] = r
        else:
            blocks.append(cur)
            cur = dict(recs=[r], t0=r['t'], body=r['body'], best=r)
    if cur:
        blocks.append(cur)
    return blocks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='Witten2021_Quantization_by_Branes_and_GL')
    ap.add_argument('--tx', default='slides_tx')
    ap.add_argument('--asr', default='asr_p04.json')
    ap.add_argument('--frames', default='frames_p04')
    ap.add_argument('--no-dedupe', action='store_true')
    a = ap.parse_args()

    recs = load_tx(a.tx)
    segs = load_asr(a.asr)
    print(f'slide records={len(recs)} asr_segs={len(segs)}')

    blocks = ([dict(recs=[r], t0=r['t'], body=r['body'], best=r) for r in recs]
              if a.no_dedupe else collapse(recs))
    print(f'blocks after collapsing builds: {len(blocks)}')

    # optional: attach the frame file behind each block
    by_time = {}
    idx = os.path.join(a.frames, 'index.json')
    if os.path.exists(idx):
        for it in json.load(open(idx, encoding='utf-8')):
            by_time[round(it['t'], 1)] = it['file']

    out = []
    for i, b in enumerate(blocks):
        t0 = b['t0']
        t1 = blocks[i + 1]['t0'] if i + 1 < len(blocks) else META['duration']
        best = b['best']
        out.append(dict(
            idx=i, t_start=round(t0, 1), t_end=round(t1, 1),
            t_start_str=hms(t0), t_end_str=hms(t1),
            kind=best.get('kind', ''), heading=best.get('heading', ''),
            slide_markdown=best.get('body', ''),
            figures=best.get('figures', []),
            narration=narrate(segs, t0, t1),
            frame=by_time.get(round(t0, 1), ''),
            pages=[r['page'] for r in b['recs']],
        ))

    md = [f"# {META['title']}", '',
          f"**{META['speaker']}** · {META['date']}", '',
          f"{META['event']} · {hms(META['duration'])}", '',
          f"Source: <{META['url']}>  ·  {len(out)} content blocks "
          f"(from {len(recs)} captured PDF pages)", '', '---', '']
    for r in out:
        md += [f"## {r['t_start_str']}  ·  block {r['idx']+1}", '']
        if r['heading']:
            md += [f"**{r['heading']}**", '']
        md += [r['slide_markdown'] or '_(no text on this slide)_', '']
        for f in r['figures']:
            fs = f.strip()
            md.append("> " + (fs if fs.startswith('[Figure') else '[Figure] ' + fs))
        if r['figures']:
            md.append('')
        if r['narration']:
            md += [f"**Narration** `{r['t_start_str']}–{r['t_end_str']}`", '',
                   '> ' + r['narration'], '']
        md += ['---', '']
    open(a.out + '.md', 'w', encoding='utf-8').write('\n'.join(md))

    with open(a.out + '.jsonl', 'w', encoding='utf-8') as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    n_narr = sum(1 for r in out if r['narration'])
    n_words = sum(len(r['slide_markdown'].split()) for r in out)
    print(f"wrote {a.out}.md / .jsonl : {len(out)} blocks, {n_words} slide words, "
          f"{n_narr} blocks with narration")


if __name__ == '__main__':
    main()
