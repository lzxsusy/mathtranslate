# 2026-11-27 修卡施工说明

> **施工日期**：2026-11-27（Asia/Shanghai）
> **触发**：当日 `11_card_audit/daily_verify/2026-11-27/records.jsonl` 的 12 条 issue（11 张卡）
> **依据**：`11_card_audit/WORKFLOW.md` §7–§9；`11_card_audit/README.md`「卡片已在原位置修改，本区只做追溯」

## 1. 做了什么

把当日核验判出的 12 条 issue 真正修进 `datasets/` 的卡片，而不是只留在审计记录里。
11 张卡共 **23 处字段级改动**（12 条 issue 中 functoriality 一卡两条，另有 3 处「同一错误的其它副本」一并清掉）：

| # | 卡片 | 严重度 | issue | 改动处 |
|---|---|---|---|---|
| 1 | `siebert/correction/prop-3-12-lci` | minor | (3.58) 定义在 p.50，卡写 p.51 起 | 1 |
| 2 | `gtgl15/concept/eigenbranes` | minor | 把定义登记成 theorem + gap | 1（删整段） |
| 3 | `kw/concept/n4-sym-theory` | minor | (2.14) 在印刷 p.10，卡写 p.11 | 1（第二次修改） |
| 4 | `functoriality/concept/strip-shrinking` | minor | 定理在 p.27/p.28，卡写 p.25/p.26 | 3（含 provenance_note） |
| 5 | `ggl09/deriv/descent-to-xi` | **major** | 边界之差方向取反 | 1 |
| 6 | `siebert/concept/gromov-witten-invariant` | **major** | 把 lci 换成「连通」 | 1 |
| 7 | `lbook04/concept/ch9-langlands-spectral` | minor | 带扭极点位置写成 s=1 | 1 |
| 8 | `lbook04/concept/ch3-three-motives` | minor | pages [39,40] 覆盖不到 §2.3 | 2 |
| 9 | `bzg/concept/categorical-fourier` | **major** | 核公式不在所引 §2.1 | 4（section/pages/anchor/page_note + verification 2 处） |
| 10 | `gw06/concept/two-dimensional-defect` | minor | 离散 α,η 互换在印刷 31 | 3（pages/pdf_pages/page_note） |
| 11 | `glc/concept/fundamental-local-equivalence` | minor | 相对构造在 p.72 | 2 |

逐处 before/after 见 `fix_log.json`（23 条，每条带 `why`）；逐卡七节案例见 `casebook/`。

## 2. 怎么改的（可回滚）

- 脚本：`apply_fixes.py` 做前 20 处（每条带 before 断言，先全量校验再写盘，`--dry-run` 可用）；
  其余 3 处（functoriality `provenance_note`、benzvi `verification.checks[0].entry/asserts`）用同样带断言的字段级替换补上。
- 写盘保持原文件的换行（CRLF/LF）与缩进（gw06 为 1 空格），改后立即 `json.load` 并回读 after 写入 `fix_log.json`。
- 回滚：`git revert <本次 commit>`；或按 `fix_log.json` 的 `after → before` 反向替换（每条均有断言值）。

## 3. 派生文件同步（避免「错误版与正确版并存」）

卡片 JSON 是源，md / index 是产物，必须同步：

- **md（9 个）**：siebert×2、gtgl15、kw06、functoriality、glc、lbook04×2、gw06。
  前 8 个用各集自带 `tools/render_md.py`（lbook04 用 `tools/build.py`）在临时副本重生成后逐字比对，只回拷本卡文件；
  gw06 的 `tools/make_cards.py` 依赖仓库相对路径的 `08_source_code` 锚点（仓库本身有 2 条既有缺失），临时副本跑不通，
  其 md 的 pages / page_note 两行按生成器同样格式手工同步。
- **索引**：`datasets/gw06/index.jsonl` 的 `pdf_pages` 由 [30,31] 同步为 [30,32]（该文件由 `make_cards.py` 派生，
  手动改后与生成规则一致）。其余集 index 不含受影响页码。
- **生成器**（否则下次重建会退回错误值）：
  - `datasets/lbook04/tools/cards_1.py:416`：`src(3, "§2", [39, 40], …)` → `[39, 43]`；
  - `datasets/lbook04/tools/cards_3.py:171`：ch9 的 key_points 旧句 → 新句；
  - `datasets/benzvi_glc/tools/build_cards.py`：categorical-fourier 的 `"§2.1", [8]` → `"§1.3", [6]`，新增 `note=`/`asserts=`
    关键字与 `C()` 的可选参数 `note`/`asserts`（写成 `sources[0].page_note` 与 verification 文案）。
  - 验证：三个生成器在临时副本重建后与已改 JSON **逐字段相等**（lbook04 两卡、benzvi 一卡）。

## 4. 验证结果

| 检查 | 结果 |
|---|---|
| `verify_final.py`（全量 1859 张） | `cards parsed: 1859, errors: 0` |
| `git diff --check` | 干净（rc=0） |
| 目标卡 `json.load` | 11/11 通过 |
| `check_casebook.py` | 仍 32 条（本批不往 `casebook/index.json` 追加） |
| md 与卡片一致性 | 9 个 md 均由卡片重生成后回拷；gw06 手工两行与生成格式一致 |

**需要说明的 5 条 STALE**：`verify_final.py` 拿 11-26 批次的 `fix_log.json` 当期望值，会报
`kw06/n4-sym-theory ('theorems',0,'source')` 的 got≠want——这正是本批**故意**修正 11-26 的 off-by-one（p.11 → p.10，
按 PDF 页脚）。历史档案不改，故该条永久显示为 STALE，属预期。另外 4 条（`kw06/concept/hecke-eigensheaf`、
`kw/deriv/gno-to-langlands` ×3）是工作树里 11-26 之后他人未提交的既有改动，与本批无关。

## 5. 与既有案例库的关系

- `11_card_audit/casebook/` 的 32 例与 `index.json` **未动**：`tools/check_casebook.py` 硬编码 32 条，追加会导致校验失败
  （先例：`11_card_audit/glc_full/` 独立归档 25 例）。
- 本批 11 例放在本目录 `casebook/`，编号 `D27-01…D27-11`，frontmatter 按 `templates/CASE_TEMPLATE.md` 七节撰写。
- `kw06/n4-sym-theory` 是同一卡的第二次修改，按 WORKFLOW §9 在案例与 `casebook/README.md` 里注明，不改 11-26 的 fix_log。

## 6. 遗留

- `gw06` 的 `make_cards.py` 在仓库根跑也会因 2 条既有缺失锚点（`s04b-lines.tex`、`sA-duality.tex`）rc=1；
  本次未修锚点（超出当日核验范围），只用其派生规则手工同步了 1 个 index 字段与 1 个 md 的两行。
- 工作树仍有他人未提交的 46 个 `datasets/` 文件，本批 commit 只暂存下面列出的自有文件。
