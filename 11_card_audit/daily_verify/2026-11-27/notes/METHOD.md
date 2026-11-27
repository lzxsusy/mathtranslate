# 2026-11-27 核验方法记录

## 环境

- Python：`C:/Users/admin/.dsh/dsh-runtimes/dsh-primary-runtime/dependencies/python/python.exe`（必须 `PYTHONIOENCODING=utf-8`）
- pdftotext：`C:/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdftotext.exe`
- 一手 PDF 目录：`datasets/_audit/third_party_2026-11-26/tmp/sources/`；ggl09 本轮从 arXiv 下载（0905.4795v1，E1），文本存 `%TEMP%/cardverify/ggl09.txt`，不入库。
- 抽文本缓存（仓库外）：`C:/Users/admin/AppData/Local/Temp/cardverify/<set>.txt`，按 `\f` 分页，`pages[i]` = PDF 第 i+1 页。
- lbook04 原书 PDF：`C:/Users/admin/Desktop/文献库/04_朗兰兹与表示论/bernstein_gelbart_introduction.pdf`。

## 页码口径（本轮实测）

| 集 | PDF 页 ↔ 印刷页 | 依据 |
|---|---|---|
| siebert / ggl08 / benzvi_glc / glc / ggl09 | 相同 | 页眉页脚 |
| kw06 / gw06 | PDF = 印刷 + 1 | kw06 PDF 10 页脚 9；gw06 PDF 32 = 印刷 31 |
| gtgl15 | PDF = 印刷 + 2 | PDF 39 页脚 37（README 写 +1，未改数据集） |
| lbook04 | ch9 +3、ch3 +7 | 与 PAGE_MAP 一致 |

## 逐字校验

- `notes/verify_quotes.py records.jsonl`：issue 的 `card_says` 去空白后必须是卡 JSON 子串；`evidence.quote` 去空白后必须是源文本子串（kind=internal 改查卡自身）。
- 本轮结果：20 行、12 条 issue，`BAD = 0`。
- 复跑命令：

```bash
python 11_card_audit/daily_verify/tools/check_daily.py \
  --file 11_card_audit/daily_verify/2026-11-27/records.jsonl \
  --sample 11_card_audit/daily_verify/2026-11-27/sample.json
```

## 分工

- lead：抽卡、卡 1–3、口径裁定、全部 issue 的 card_says/quote 机械复核、SUMMARY。
- vfy-a：卡 4–7；vfy-b：卡 8–11；vfy-c：卡 12–15；vfy-d：卡 16–20。
- 子代理只提供候选证据；每条 issue 的引文均由 `verify_quotes.py` 复核后才进入 records。
