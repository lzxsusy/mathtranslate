# 每日外部核验（daily_verify）

每天从全库资料卡中抽 **20 张**，按 [`../DAILY_VERIFICATION_PLAYBOOK.md`](../DAILY_VERIFICATION_PLAYBOOK.md) 做外部核验；只记录问题，不改卡。

## 一条命令开始

```bash
python 11_card_audit/daily_verify/tools/sample_daily.py --n 20
```

生成 `daily_verify/<YYYY-MM-DD>/sample.json`（确定性抽样，seed = 日期；365 天内核过的不重抽）。

核完后把 20 条记录写成 `records.jsonl`，跑：

```bash
python 11_card_audit/daily_verify/tools/check_daily.py \
  --file 11_card_audit/daily_verify/<date>/records.jsonl \
  --sample 11_card_audit/daily_verify/<date>/sample.json \
  --append-ledger
```

0 error 后写 `SUMMARY.md`（模板见 playbook §10），然后 commit + push。

## 目录

```text
daily_verify/
├── README.md              # 本文件
├── ledger.jsonl           # 已核台账：date,id,path,verdict,confidence,severity_max,n_issues
├── tools/sample_daily.py  # 抽样（确定性、去重、可 --set/--date/--n）
├── tools/check_daily.py   # 校验 records 并追加台账
└── <date>/                # 每天的 sample.json / records.jsonl / SUMMARY.md / notes/
```

## 约定

- 记录 schema 与判定口径见 playbook §6–§7；每卡 ≥3 条 checks，覆盖数学 / 出处 / 内部一致三类。
- `card_says` 必须是卡 JSON 的逐字子串；`evidence.quote` 必须是来源逐字句。
- 巡检**不修改** `datasets/**`；确认的问题留给确认修复流程。
- 台账只追加，不删行；需要重核时用 `--include-recent` 或新日期。
