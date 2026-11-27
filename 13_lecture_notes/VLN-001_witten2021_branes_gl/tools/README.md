# tools/ · VLN-001 的提取脚本

七个脚本，纯 Python，不依赖系统 ffmpeg（本机没有，也能跑）：解码用 **PyAV**（自带 ffmpeg 库），
转写用 **faster-whisper**，出图用 **PyMuPDF**。依赖：

```bash
pip install av faster-whisper ctranslate2 pymupdf numpy pillow
```

| 脚本 | 作用 | 关键参数 |
| --- | --- | --- |
| `pipeline.py` | 总调度：`prep`（下载 + 抽帧 + 分页）与 `merge`（合并语料） | `--url BV… --part 4 --slug p04` |
| `extract_frames.py` | 单遍解码，每秒取 1 帧，仅在画面变化时存全分辨率 JPEG | `--thr 0.004`（差异像素占比） |
| `segment_pages.py` | 把关键帧按「页面相同」聚成页：裁白底页框 → 二值墨迹掩码 → 顺序比较 | `TH=0.55 MERGE=0.88` |
| `chunk_transcribe.py` | 音频切 N 块并行转写，合并时按 start 排序 | `audio out small.en 6` |
| `clean_asr.py` | 术语表替换清洗（不改原转写） | `--asr x.json --out y.json` |
| `merge_corpus.py` | 按时间对齐「逐页转写」与「ASR」，折叠 build 链 | `--tx slides_tx --asr asr.json --frames frames_p04` |
| `make_pdf.py` | 从 `blocks.jsonl` 的 `frame` 字段重建 deck PDF（本机回看用，**不入仓**） | `--jsonl x.jsonl --out _local/deck.pdf` |

## 两个踩过的坑（改脚本别踩回去）

1. **`av.open(..., metadata_errors=…)` 在 PyAV 19 会抛 `TypeError`**。faster-whisper 内部就是这么调 `decode_audio` 的，
   所以 `model.transcribe("x.wav")` 会直接崩。本目录的 `chunk_transcribe.py` 先把音频读成 float32 数组再喂给模型。
2. **Windows 控制台默认 GBK**，打印含 `ö` 的转写文本会 `UnicodeEncodeError` 并**杀死整个进程**（分块转写时静默丢两块）。
   每个脚本开头都做了 `sys.stdout.reconfigure(encoding='utf-8', errors='replace')`。

## 分页参数怎么来的

幻灯片是「深色底 + 白页 + 播放器浮层」的屏幕录制，直接用整帧去比会被恒定背景淹没（Jaccard 全部 ≥0.9）。
必须先裁到白页区域，再只比墨迹：本报告白页框约 `(161, 33, 1277, 866)`（1440×900 下），
`TH=0.55` 判「换页」、`MERGE=0.88` 把相邻同页合并。换一段录像（分辨率/播放器不同）要重测这两个框与阈值。
