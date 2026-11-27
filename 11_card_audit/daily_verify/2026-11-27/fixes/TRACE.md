# TRACE · 2026-11-27 核验与修卡

时间均为 Asia/Shanghai。命令在仓库根 `C:/Users/admin/Desktop/数译发布/gitee_shuyi` 执行，
Python 统一用 `C:/Users/admin/.dsh/dsh-runtimes/dsh-primary-runtime/dependencies/python/python.exe`（`PYTHONIOENCODING=utf-8`）。

## 一、抽样与核验（12:30–12:50）

1. `python 11_card_audit/daily_verify/tools/sample_daily.py --n 20`
   → `daily_verify/2026-11-27/sample.json`（20 张，library_total 1858）。
2. 读 `DAILY_VERIFICATION_PLAYBOOK.md`；按 set 找一手源：本地 PDF 在
   `datasets/_audit/third_party_2026-11-26/tmp/sources/`，抽文本到 `C:/Users/admin/AppData/Local/Temp/cardverify/<set>.txt`
   （按 `\f` 分页）。ggl09 本地无 PDF，从 arXiv:0905.4795 取（E1）。
3. 20 张分 4 组交子代理核验；lead 对每条 issue 的 `card_says` 与 `evidence.quote` 做机械复核
   （`notes/verify_quotes.py`：去空白后分别为卡 JSON / 源文本的子串），全部 BAD=0。
4. `notes/assemble.py` 合并、按 sample 顺序排序、归一化 aspect；`check_daily.py --append-ledger`
   首次 31 error（aspect 自由文本），归一化后 **0 error / 0 warning**，ledger 追加 20 行。
5. 结果：pass 8 / issue 11 卡 12 条（major 3、minor 9）/ unverifiable 1。
   commit `57c08a5d`，推送 atomgit（`master:main`）与 origin（`master`）。

## 二、决定修卡（12:59）

用户要求：把 12 条 issue 真正修掉；要有正误对照、为什么错、说明文件与施工日期；
旧内容只能作为「正误对照」存在，不能让错误版与正确版并存。

读 `11_card_audit/README.md` 与 `WORKFLOW.md` §7–§9：
- 卡片在 `datasets/` 原位置修改，本区只做追溯；
- 三条铁律（不伪造证据、不强行找问题、可回滚）；
- `casebook/index.json` 被 `check_casebook.py` 硬编码为 32 条，**不追加**，独立归档（先例 `glc_full/`）。

## 三、核实证据（13:00–13:10）

- lbook04 ch3 原书 PDF：`C:/Users/admin/Desktop/文献库/04_朗兰兹与表示论/bernstein_gelbart_introduction.pdf`；
  实测印刷 39=PDF 46（偏移 7），Example 2.1 在印刷 42=PDF 49。
- benzvi：§1.3（p.6）是 categorical Fourier 的 general theme；§2.1（p.8）是范畴/Hilbert 类比，无核公式。
- kw06：PDF 11 页脚 10 且 (2.14) 在该页；PDF 12 页脚 11 且 (2.15) 在该页 → 11-26 批次的 p.11 是 off-by-one。
- 各 set 生成链：lbook04 `tools/build.py`←`cards_1.py`/`cards_3.py`；benzvi `build_cards.py`→`normalize_cards.py`；
  gw06 `make_cards.py`（写 index/md/MAP/taxonomy，校验 `08_source_code` 锚点）；其余 `render_md.py`。
- 格式：11 张卡中 5 张 CRLF、6 张 LF；gw06 1 空格缩进，其余 2 空格。

## 四、施工（13:10–13:20）

1. 写 `fixes/apply_fixes.py`（20 处，每条 before 断言 + why，先校验后写盘，保持原换行/缩进）。
   - `--dry-run` → `DRY-RUN OK: 11 files, 20 changes`
   - 正式 → `OK: 11 files, 20 changes`，回读 after 写 `fixes/fix_log.json`
   - `git diff --stat`：11 文件 28 insertions / 36 deletions（gtgl15 的 theorem 整段删除占 13 行）
2. 追加 3 处同源副本：functoriality `provenance_note`（p.25–26 → p.27–28）、
   benzvi `verification.checks[0].entry`（§2.1 → §1.3）与 `asserts`（「逐句对齐」→「依据 general theme 整理」）。
   `fix_log.json` 共 11 卡 23 处。
3. 生成器同步：lbook04 `cards_1.py:416`、`cards_3.py:171`；benzvi `build_cards.py`（section/pages + `note`/`asserts` 参数）。
   临时副本重建后与已改 JSON 逐字段相等（lbook04 两卡、benzvi 一卡）。
4. md 同步：8 个用各集渲染器在临时副本重生成（siebert×2、gtgl15、kw06、functoriality、glc、lbook04×2），
   逐字比对后只回拷本卡文件；gw06 改两行（pages / page_note），并同步 `gw06/index.jsonl` 的 `pdf_pages`。
   ggl09、benzvi 无 md 目录。
5. 生成案例集与说明：`fixes/build_docs.py` → `fixes/casebook/`（11 例 + index.json + README）、`fixes/README.md`、本 TRACE。

## 五、验证

- `python datasets/_audit/third_party_2026-11-26/tools/verify_final.py` →
  `cards parsed: 1859, errors: 0`；`field errors: 5`，其中 1 条是本批有意修正 11-26 的 off-by-one（expected），
  4 条是他批既有未提交改动（与本批无关）。
- `git diff --check` rc=0；11 张卡 `json.load` 全通过。
- `python 11_card_audit/tools/check_casebook.py`：既有 32 例未动，校验通过。

## 六、提交

- `git add` 仅本批自有文件：11 张卡 JSON、9 个 md、`gw06/index.jsonl`、3 个生成器、
  `11_card_audit/daily_verify/2026-11-27/fixes/` 全目录（含 `fix_log.json`、案例集、说明）。
- commit 信息：`fix: 2026-11-27 核验 12 issue 修入卡片（11 卡 23 处）`
- 推送 atomgit `master:main`，再 origin `master`。
