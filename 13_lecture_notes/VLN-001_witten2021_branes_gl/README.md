# VLN-001 · Quantization by Branes and Geometric Langlands

Edward Witten 2021 年 2 月在 IAS「几何 Langlands 小型会议」上的报告，从 A/B 模型与边界条件出发，
把 Etingof–Frenkel–Kazhdan 关于 Higgs 丛上 Hecke 特征函数的猜想重新解释为一次「brane 量子化」。
本目录把这场 2 小时的报告拆成 **109 个内容块**：每块一页幻灯片正文（含 LaTeX 公式）+ 该页期间讲者的原话 +
在录像里的时间区间。

## 元数据卡

| 字段 | 值 |
| --- | --- |
| `id` | `VLN-001` |
| `题名` | Quantization by Branes and Geometric Langlands |
| `讲者/机构` | Edward Witten / IAS |
| `场合` | Mini-Conference on the Geometric Langlands Correspondence |
| `日期` | 2021-02-03 |
| `来源` | Bilibili `BV1b34y1Q7Ah` p=4（短链 `b23.tv/qbdqoHe` 落在 p=4） |
| `时长` | 02:04:53 |
| `讲义规模` | 228 / 201 / 109（原 deck 页数 / 实际转录页数 / 折叠后内容块数） |
| `语言` | en + en（Q&A 有提问者口音） |
| `提取日期` | 2026-11-27 |
| `工具链` | PyAV 19.0.2 / faster-whisper small.en / 逐页视觉转写 + xelatex |
| `质量等级` | B（完整转写；公式抽核 18 处；时间轴未逐条回放） |
| `权利` | 笔记与语料为本库自产（CC BY 4.0）；原 deck 页面图、录像、关键帧**不入仓**（COMPLIANCE §4 L4） |
| `复核` | 2026-11-27 抽核 18 处公式（Kapustin–Witten τ、几何 Satake、Θ_τ 内积、corners 等式），均回帧核对 |

## 本报告讲了什么（三句话）

1. **A 模型侧**：4d N=4 SYM 的电磁对偶给出 `G ↔ G^∨` 的几何 Langlands；边界条件成范畴，线算子是其上的函子，
   对偶把 `'t Hooft 线算子（几何 Hecke）` 换成 `Wilson 线算子`——这就是几何 Satake 对应的物理读法。
2. **中间那座桥**：把 `M_H(G)` 看成实辛流形（`ω = Im Ω`），量子化它得到 EFK 的 Hilbert 空间；
   而 `Hom(B, B_cc)` 正是 brane 量子化给出的同一个空间，于是「EFK 的 L² 猜想」=「一次量子化的谱对应」。
3. **可检验的预言**：`B_cc` 的对偶是 opers 的结构层（Beilinson–Drinfeld，数学上已知、物理上"initially unclear"），
   `A ⊗ Ā` 上 Hecke 算子的联合谱是实 opers，`SL_2` 情形特征值为 `±(ȷ̄(v), ȷ(w))`——由此可写出双倍分叉的算子对角化。

笔记按这三点组织（§3–§8），`[t=…]` 标注原话出处，`整理者按` 标出整理者补的衔接（非讲者原话）。

## 产物

| 路径 | 内容 | 规模 |
| --- | --- | --- |
| `notes/main.tex` | 笔记源码（ctexart / xelatex） | 13 页 |
| `notes/VLN-001_讲义笔记_v1.pdf` | 成稿 PDF | 13 页 |
| `source/VLN-001_corpus.md` | 逐块人读版：时间、页正文、图注、该页原话 | 198 KB |
| `source/VLN-001_blocks.jsonl` | 机器读版，109 行，字段见下 | 215 KB |
| `source/VLN-001_asr.json` | 清洗后 ASR，2,338 段（含时间戳），2:04:53 全覆盖 | 213 KB |
| `source/VLN-001_asr.srt` | 同上的字幕格式，便于对轴 | — |
| `tools/` | 本条用的提取脚本（抽帧 / 分页 / 转写 / 清洗 / 合并 / 出 PDF） | 7 个 |

`blocks.jsonl` 每行字段：`idx`, `t_start`, `t_end`, `t_start_str`, `t_end_str`, `kind`, `heading`,
`slide_markdown`, `figures`, `narration`, `frame`, `pages`。`frame` 是关键帧文件名（本机 `_local/` 内，
仓外不复现）；`pages` 是该块对应的原 deck 页码（来自录像里的页码浮层，供回看定位）。

内容块类型分布：`text` 84 / `figure` 16 / `formula` 7 / `title` 1 / `blank` 1。
幻灯片正文 9,918 词 + 讲者原话 20,141 词 ≈ **30,059 词**。32 块带图注（图注为整理者描述，非原文）。

## 复现

```bash
PY=python   # 需 av / faster-whisper / ctranslate2 / pymupdf / numpy / pillow
python tools/pipeline.py prep --url BV1b34y1Q7Ah --part 4 --slug p04   # 下载 + 1fps 抽帧 + 分页
python tools/chunk_transcribe.py p04_audio.m4a p04 small.en 6          # 6 块并行 ASR（约 25 min / 20 线程）
python tools/clean_asr.py --asr p04.json --out asr_p04_clean.json      # 术语表清洗（不改原转写）
python tools/merge_corpus.py --out VLN-001 --tx slides_tx --asr asr_p04_clean.json --frames frames_p04
python tools/make_pdf.py --jsonl VLN-001.jsonl --out _local/deck.pdf   # 仅供本机回看，不入仓
cd notes && xelatex -interaction=nonstopmode -jobname=VLN-001_讲义笔记_v1 main.tex   # 两遍
```

成稿 PDF 的 jobname 不能是 `main`：`tools/check_compliance.py` 把任何名为 `main.pdf` 的 PDF 判为编译产物、禁止入库。

逐页视觉转写这一步是「人来定规则、模型来读图」：每 20 页一个批次，按
`04_playbook/24_…md` §7 的格式产出（直录原文、公式转 LaTeX、忽略播放器 UI）。

## 已知问题

- **27 页没单独成页**：deck 共 228 页，逐帧分割出 201 页。讲者快速翻过或一页停留 <2 s 的页会并进相邻块，
  这些页的正文只在相邻块的 `narration` 里留下痕迹。回看录像时可补。
- **ASR 术语**：`small.en` 未做领域微调，已用术语表（branes / opers / Hitchin / Gaiotto / Beilinson…）清洗 212 段，
  但专名仍可能有误；引用讲者原话时以 `source/VLN-001_asr.srt` + 回放为准。
- **图注**是整理者对示意图的描述（如"裤衩形（pair of pants）带状示意图"），**不是**幻灯片原文，
  已在 `figures` 字段与笔记里标明。
- 讲者有几处**翻回**前面的页，合并后留下近重复块（如 `t≈33:47` 与 `t≈41:22` 的同页），保留未删——
  那是报告的真实节奏。

## 引用

```
Witten, Edward. Quantization by Branes and Geometric Langlands.
Mini-Conference on the Geometric Langlands Correspondence, IAS, 2021-02-03.
视频：https://www.bilibili.com/video/BV1b34y1Q7Ah?p=4
本笔记：数译 13_lecture_notes/VLN-001（2026-11-27，B 级）
```
