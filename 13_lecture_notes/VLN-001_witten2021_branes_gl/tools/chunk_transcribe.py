"""Chunked parallel transcription: split audio, run N whisper processes, merge.

usage: python chunk_transcribe.py <audio> <outprefix> <model> <nchunks> [threads]
"""
import os, sys, json, subprocess, math, time
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
os.environ.setdefault('HF_ENDPOINT', 'https://hf-mirror.com')
from faster_whisper import WhisperModel
from clip_wav import load_audio

def fmt(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},000"

HOT = ("Geometric Langlands, Hecke functors, Hecke eigensheaves, branes, boundary conditions, "
       "Wilson line operators, 't Hooft operators, Hitchin moduli space, opers, A-model, B-model, "
       "D-modules, quantization, mirror symmetry, holomorphic Chern-Simons, gauge theory, "
       "coisotropic, Lagrangian, spectral decomposition, automorphic forms, geometric Satake, "
       "G-vee, dual group, line operators, functors")

def run_chunk(args):
    wav, size, out, threads, offset, idx = args
    import numpy as np
    audio = load_audio(wav).astype('float32') / 32768.0
    model = WhisperModel(size, device='cpu', compute_type='int8',
                         cpu_threads=threads, download_root='models')
    segs, info = model.transcribe(audio, language='en', beam_size=5, vad_filter=True,
                                  initial_prompt=HOT,
                                  vad_parameters=dict(min_silence_duration_ms=400),
                                  condition_on_previous_text=False)
    rows = []
    for s in segs:
        rows.append({'start': round(s.start + offset, 2), 'end': round(s.end + offset, 2),
                     'text': s.text.strip()})
        if idx == 0:
            print(f"[c0 {s.start:6.1f}] {s.text.strip()}", flush=True)
    json.dump(rows, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
    print(f"chunk{idx} done: {len(rows)} segs, {offset/60:.0f}-{offset/60+info.duration/60:.0f} min", flush=True)
    return rows

def main():
    src, outpre = sys.argv[1], sys.argv[2]
    size = sys.argv[3] if len(sys.argv) > 3 else 'small.en'
    n = int(sys.argv[4]) if len(sys.argv) > 4 else 6
    if len(sys.argv) > 5:                      # chunk mode: args = wav out idx offset threads
        run_chunk((sys.argv[1], size, outpre, int(sys.argv[5]), float(sys.argv[6]), 0))
        return
    t0 = time.time()
    a = load_audio(src)
    total = len(a) / 16000
    print(f"audio {total/60:.1f} min", flush=True)
    import numpy as np, wave
    bounds = [round(total * i / n, 1) for i in range(n + 1)]
    procs = []
    for i in range(n):
        seg = a[int(bounds[i]*16000):int(bounds[i+1]*16000)]
        wav = f"{outpre}_chunk{i}.wav"
        with wave.open(wav, 'wb') as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(16000)
            w.writeframes(seg.tobytes())
        out = f"{outpre}_chunk{i}.json"
        procs.append(subprocess.Popen([sys.executable, __file__, wav, out, size, '0',
                                       '3', str(bounds[i])]))
    for p in procs:
        p.wait()
    rows = []
    for i in range(n):
        rows += json.load(open(f"{outpre}_chunk{i}.json", encoding='utf-8'))
    rows.sort(key=lambda r: r['start'])
    json.dump(rows, open(f"{outpre}.json", 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    open(f"{outpre}.srt", 'w', encoding='utf-8').write('\n'.join(
        f"{i+1}\n{fmt(r['start'])} --> {fmt(r['end'])}\n{r['text']}\n" for i, r in enumerate(rows)))
    open(f"{outpre}.txt", 'w', encoding='utf-8').write('\n'.join(r['text'] for r in rows))
    print(f"MERGED {len(rows)} segs in {time.time()-t0:.0f}s -> {outpre}.json/.srt/.txt")

if __name__ == '__main__':
    main()
