# leanstmt 制作流程与事故记录

本文件记录 `datasets/leanstmt/` 这一批（Witten 2015 试点 12 条）是怎么做出来的、验证到什么程度、踩过什么坑，
以及续做下一批时必须遵守的流程。

## 一、本批（v0.1，2026-11-19）做了什么

1. **选源**：Witten, *More On Gauge Theory And Geometric Langlands*, arXiv:1506.04293v3（本库另有完整中文校订译注本 SY03-20）。
2. **筛条目**：不是从全文抽，而是**只抽能落在现有 mathlib 上的陈述**。先按原文逐节打勾：§2.6.6（'t Hooft 磁通 / ℤ_N）、§4.1+§7.1（单位根与电荷）、§3.2（GNO 对偶）、§2.6.5（自旋结构）、§2.6.1–2.6.2（谱曲线亏格、分歧除子次数、Prym 维数）、§2.4（Hitchin 纤维维数）。
   - 凡是需要「曲线亏格 / 分歧除子 / Riemann–Hurwitz / Hitchin 模空间 / 稳定丛 / 辛结构」的，先写成 **gap 卡**（K01/K02），不硬凑成 `True`。
3. **写 Lean**：在用户本机 lake 工程 `C:\Users\admin\Desktop\数译发布\shuyi\formal` 里写 `ShuyiFormal/Witten2015/Statements.lean`（10 条定理）与 `Gaps.lean`（2 条缺口）。
   - 只 `import` 需要的基础模块（`Mathlib.Data.ZMod.Basic`、`Mathlib.RingTheory.RootsOfUnity.Complex`、`Mathlib.LinearAlgebra.Dual.Lemmas`、`Mathlib.LinearAlgebra.Dimension.Finrank`），**绝不在 LSP 里 `import Mathlib`**（见事故记录）。
4. **编译**：`lake env lean ShuyiFormal/Witten2015/Statements.lean` → exit 0、无输出；`Gaps.lean` → exit 0、2 条 `declaration uses 'sorry'` 警告。
5. **写卡**：`tools/make_cards.py` 里 `DATA` 表集中维护 12 卡（原文锚、中英陈述、Lean 语句、依赖、假设、盲验回译、缺口），再生成 `cards/`、`README.md`、`SCHEMA.md`、`MAP.md`；`build_index.py` → `index.jsonl`；`render_md.py` → `md/`。
6. **静态检查**：`python tools/lint_cards.py cards --strict` → `cards=12 ids=12 errors=0 warnings=0`。
7. **真跑 Lean**：`python tools/check_lean.py --project C:\Users\admin\Desktop\数译发布\shuyi\formal --run --write-verification` → 两个文件 exit 0（Statements 0 个 sorry，Gaps 2 个 sorry，注释里的 "sorry" 已剥除后再计数），写 `verification.jsonl`。

## 二、硬性纪律（与 `SCHEMA.md` 的 5 条对应）

1. **不虚标**：`verification.status` 只有 `certified`（真编译通过、0 sorry）与 `gap`（真编译通过、命题里显式 sorry）。没有 "应该对"「大概对」「专家说对」这一档。
2. **不掺沙**：`natural_language.en` 必须能在原文找到原句（`source.section` + `source.pages` + `source.anchor`）；`lean.statement` 必须是原文陈述的**忠实重述**（弱化/强化假设都要在 `hypotheses` 里写出来），不得把"证明"塞进陈述、不得把定理换成例子。
3. **不越界**：只形式化原文**已有**的陈述；我们补的定义（`specCurveGenus` 等）只作占位并标 `def`，不冒充 mathlib 内容；不向 mathlib 提交本批内容；`rights: "rewritten"`。
4. **盲验回译**：`backtranslation.zh` 必须由没看 Lean 的人从 Lean 语句独立回译（本批为 lead 起草、独立核查；下一批起要求 `reviewer` 与 `checker` 不同人）。
5. **缺口照登**：做不动的原文陈述 → gap 卡，写 `gaps[].reason` 与 `blocked_by`（缺什么基础设施），同样入库、同样进 index。**失败条目也是语料**。

## 三、续做流程（下一批 50–100 条按这个走）

```
选源 → 抽取 statements.tsv（id/kind/zh/lean/deps/status）→ 逐条查 mathlib 现有声明（rg，不用 LSP 全量 import）
     → 写 Statements.lean / Gaps.lean → lake env lean 批跑 → make_cards + build_index + render_md
     → lint_cards --strict（0 error/0 warn）→ check_lean --run --write-verification → 更新 MAP/README 计数
```
- 每条卡的 `verified` 必须能由 `verification.jsonl` 复算：`exit == 0` 且（`certified` ⟺ `file_sorry == 0`）。
- 一批做完后跑一次 `tools/make_cards.py --check`，确认 README/SCHEMA/MAP 与卡片数据一致。

## 四、事故记录（2026-11-19 18:31）

- **现象**：桌面卡死，DSH 应用被杀；机器未重启。
- **取证**：Windows `Resource-Exhaustion-Detector` Event ID 2004（18:31:11）——`lean.exe` 7.84 GB + DSH 2.83 GB + `lean.exe` 2.16 GB，物理内存 15.6 GB。
- **原因**：lead 在 lean-lsp MCP 的服务进程里对一份首行 `import Mathlib` 的探针文件（`Probe.lean`）请求诊断，LSP 把整个 mathlib4 展开进内存。**不是**项目源码的问题，也不是编辑器问题。
- **修复**：删除探针文件；所有 Lean 验证改为「窄 import + `lake env lean 文件` 批处理」；重活一次只开一个；不建议在 LSP 里对 `import Mathlib` 的文件做诊断。
- **可复现的教训**：本数据集所有 Lean 文件 import 总量 ≤ 4 个 mathlib 模块，`lake env lean` 单文件峰值远低于 2 GB。

## 五、已知限制

- mathlib 缺口导致 2 条原文核心陈述只能 `sorry`（曲线亏格、Hitchin 纤维维数）；这两条是"等待 mathlib 成长"的长期缺口。
- 本批 12 条全部是 **statement-level**（陈述层），没有证明层价值；`certified` 的含义是"陈述类型正确且假设写清"，不是"陈述已被证明"。
- `certified` 的语义验证目前是单人自查 + 回译，尚未做外部专家盲审（`verification.checker` 如实写 `lead`/`kaduika`，不虚构头衔）。
- 原文锚用 arXiv v3 印刷页（79 页版），与 SY03-20 中文译注本的页（来自同一 PDF）一致；引用时以 `source.anchor` 的节号为准，页码只作定位提示。

## 六、B 批：Witten 2008（2026-11-19 增补）

- 底本：Witten, *Mirror Symmetry, Hitchin's Equations, and Langlands Duality*，arXiv:0802.0999v1（15 页；**印刷页 = PDF 页**，与 A 批差 1）。
- Lean：`formal/ShuyiFormal/Witten2008/{Statements,Gaps}.lean`。Statements 共 6 个声明（5 张卡 + 1 个同节特例 `residue_invariant`）；Gaps 9 条，均带中文 docstring 说明缺什么。
- 选卡原则同 A 批：只把「能落在现有 mathlib 上」的离散/代数骨架写成 certified；本文主定理（Hitchin 纤维化上的镜像对称）落在模空间/复辛/镜像对称层，mathlib 完全缺失，如实记为 G06 gap，不写「近似」。
- 复核命令与结果：`python tools/check_lean.py --project "C:/Users/admin/Desktop/数译发布/shuyi/formal" --run --write-verification` → 4 个文件全部 exit 0（Witten2015/Statements 0 sorry、Witten2015/Gaps 2、Witten2008/Statements 0 sorry、Witten2008/Gaps 9），`verification.jsonl` 26 行。
- 工程备注：S02/S03 是有限 Pontryagin 对偶的两面（基数 vs 典范同构）；S04 刻意用 `(m+1)` 指标（避免 `k−1` 的指数算术，`1+(k−1)-1` 难证）；`lint_cards.py` 的 sorry 计数改为先剥注释（A 批文件注释里提到 "sorry" 会误判为 certified 卡所在文件含 sorry）。
