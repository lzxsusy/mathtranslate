# 资料卡每日外部核验工作手册（v1.0）

> 适用对象：`datasets/*/cards/**/*.json` 全部资料卡。
> 定位：这些卡是后续**形式化**（Lean/Isabelle 命题）的起点，所以核验的目标不是「译文好不好」，而是**这张卡作为数学陈述能不能站住、能不能被机器检查**。
> 关系：`11_card_audit/WORKFLOW.md` 是「一次性审计」的规范；本手册是「每天 20 张」的巡检规范。两者证据标准一致，但巡检**只记录、不改卡**。

---

## 0. 一句话流程

**抽样 → 找源 → 逐句对读 → 判 pass/issue/unverifiable → 写 JSONL → 校验 → 写 SUMMARY → 记 ledger → commit + push。**

每天产出三样东西：`records.jsonl`（机器可读）、`SUMMARY.md`（人读）、`ledger.jsonl` 追加（防重复抽样）。

---

## 1. 为什么核验（判断标准的总纲）

一张卡只有同时满足下面四条，才算「可用的形式化起点」：

1. **陈述是真的**：定义/定理与一手来源一致，条件、方向、量词、层级没有改变。
2. **出处是真的**：页码、节号、编号、逐字引文能在一手来源里定位到。
3. **内部是一致的**：summary、definition、key_points、theorems、formulas、pitfalls 不互相打架。
4. **是可形式化的**：变量有类型、假设显式、记号已定义、没有「适当」「显然」这类无法翻译的词。

任何一条不满足，就要写 issue；**找不到一手来源**，写 unverifiable，不许猜。

---

## 2. 每日流程（按顺序执行）

1. **抽样**：`python 11_card_audit/daily_verify/tools/sample_daily.py --n 20`
   - 生成 `11_card_audit/daily_verify/<YYYY-MM-DD>/sample.json`。
   - 抽样是确定性的（seed = 日期），同一天重跑得到同一批；不会重复抽 365 天内已核过的卡（不足 20 时按最久未核补足）。
2. **建工作目录**：`11_card_audit/daily_verify/<date>/`，笔记放 `notes/`（一卡一 md，可选）。
3. **逐卡核验**：按 §4 找源，按 §5 清单逐条检查，按 §6 判定，按 §7 写记录。
4. **自检**：`python 11_card_audit/daily_verify/tools/check_daily.py --file records.jsonl --sample sample.json`
   - 必须 0 error；warning 要逐条看。
5. **追加 ledger**：`... --append-ledger`（只在校验通过后跑；重复跑不会重复追加同一 id+date）。
6. **写 SUMMARY.md**：按 §10 模板，数字必须与 `records.jsonl` 一致。
7. **提交**：
   ```bash
   git add 11_card_audit/daily_verify/<date> 11_card_audit/daily_verify/ledger.jsonl
   git commit -m "daily-verify: <date>（20 张，X issue）"
   ```
8. **推送**（钥匙路径必须是 Windows 形式）：
   ```bash
   GIT_SSH_COMMAND='ssh -i C:/Users/admin/.ssh/id_ed25519_shuyi -o IdentitiesOnly=yes' \
     git push atomgit master:main
   GIT_SSH_COMMAND='ssh -i C:/Users/admin/.ssh/id_ed25519_shuyi -o IdentitiesOnly=yes' \
     git push origin master
   ```
   推送失败不要 force；在 SUMMARY 里记下失败原因，保留本地 commit。
9. **返还消息**：采样数、pass/issue/unverifiable、最高 severity、需立即处理的卡、产物路径。

时间预算：20 张 ≈ 2–4 小时。允许开 4 个 subagent 各核 5 张，但 **lead 必须亲自复核每一条 issue 的 `card_says` 与 `evidence.quote`**，不能把子代理结论直接拼进 `records.jsonl`。

---

## 3. 抽样规则

- 范围：`datasets/*/cards/**/*.json`；只收「有 `id` 且有 `type`」的卡；排除 `work.json`、`index.jsonl` 与不是卡的 JSON。
- 去重：`11_card_audit/daily_verify/ledger.jsonl` 里 365 天内出现过的 `id` 优先排除；候选不足 20 时按「最久未核」补足，并在 SUMMARY 注明补样。
- 确定性：`sort(key=sha256(f"{date}|{id}").hexdigest())` 取前 20。
- 可用 `--set glc` 只抽某集；可用 `--include-recent` 强制重抽。
- 抽样脚本会把 `n_sources`、`status`、`set` 一并写入 `sample.json`，便于安排顺序：**先核有 sources 的卡**，无 sources 的卡直接按 §6 判 unverifiable（缺来源本身也是一个要报告的事实）。

---

## 4. 怎么找源（按优先级）

### 4.1 先看卡里有什么

`sources[]` 常见两种 schema：

- 讲义型：`{book, section, pages, pdf_pages, anchor}`，`anchor` 常指向本地译注源码，如 `源码/chapters/ch02.tex:84-86（定理 2.4.1）`。
- 论文型：`{text, section, pages, anchor, quote}`，`anchor` 如 `A p.30 §2.2.2 (2.45) 的适用范围`。

先读 `sources[]`、`theorems[].source`、`verification.checks[]`（**只作线索，不作证据**），确定「要去哪本书/哪篇论文的哪一页」。

### 4.2 再找源文件（本地优先）

1. `datasets/<set>/META.json`：常有 `pdf`、`arxiv`、`pages`。
2. `datasets/<set>/README.md`、`MAP.md`、`SCHEMA.md`：集的口径、页码偏移、权利说明。
3. `datasets/<set>/pdf/`、`datasets/<set>/external/`。
4. 审计用的一手源仓库：`datasets/_audit/third_party_2026-11-26/tmp/sources/`（40 个 PDF，含 `glc.pdf`、`ggl08/10/12/13.pdf`、`benzvi.pdf`、`dmod.pdf`、`fln.pdf` 等）。
5. 中译源码：`08_source_code/<项目>/源码/chapters/chNN.tex`（anchor 的行号可精确切；`\srcpage{N}` 是原书页标记，但会漂移，见 §4.5）。

### 4.3 本地没有就取一手

- arXiv：摘要页 `https://arxiv.org/abs/<id>`；PDF `https://arxiv.org/pdf/<id>`；**TeX 源码** `https://arxiv.org/e-print/<id>`（tar 解包后 grep 最可靠）。
- 出版社/项目页：numdam、PMIHES、Springer、JAMS 等官方 PDF。
- 只用一手或权威二手（nLab、Stacks Project 仅用于术语/定义/标准构造的佐证，**不能**拿来证一条具体定理的条件）。

### 4.4 禁止

Wikipedia、博客、知乎/CSDN/内容农场、二手讲义转述、模型记忆、其他轮审计的结论、卡自带的 `verification`（只能当线索）。**禁止编造 URL、页码、引文；找不到就 unverifiable。**

### 4.5 页码口径（最容易出错的地方）

1. 先确定「PDF 页」与「印刷页」的偏移：看页眉/页脚数字、目录、正文首页。
2. 记录口径：`PDF p.N = 印刷 p.M（偏移 ±k）`，写进 `notes` 与 SUMMARY。
3. `\srcpage{N}` 的语义是「**其后**内容属于原书第 N 页」，标记行本身算 N；但它可能插在段末、标题后、或整页缺失，机械映射会差一页。
   - 已知坑：`ch11.tex` 无 `\srcpage{60}`；`ch12.tex` 无 `\srcpage{64}`；`ch15.tex` §15.4 标题在 :65 而 `\srcpage{74}` 在 :77；`ch16.tex:2` 注释「原PDF第75页」是错的（实际 76）；`ch14.tex` 章首无 `\srcpage`。
4. PDF 自带目录对后几章可能不准（§15.4 之后、第 16 章），**以正文页眉/正文内容为准**。
5. 判「页码错」的门槛：卡自己的定义/记号/定理正文出现在 `pages` 之外的页才算错；只是背景句/续证句在别页不算。

---

## 5. 逐卡检查清单（每卡至少 3 条，A/B/C 各至少 1）

### A. 数学陈述（definition / theorem / formula / example）

- **A1 定义**：量词（∀/∃/唯一）、参数范围（$k$ 什么域、$n$ 是否 ≥1、$g$ 是否 ≥2）、隐含假设（连通、光滑、proper、既约、代数闭、$\ell\neq \operatorname{char} k$）、对象层级（范畴/层/复形/函子/叠）。
- **A2 定理**：方向（$\Rightarrow$ / $\Leftarrow$ / $\Leftrightarrow$）、条件是否齐全、结论是强了还是弱了、有限/无限、紧/非紧、局部/整体。
- **A3 公式**：符号、系数、归一化（$2\pi i$、$q$、$(-1)^i$、$[\,\text{shift}\,]$、twist）、指标范围、上下标、对偶群记号（$\check G$ 与 $G^\vee$ 不要混）。
- **A4 例子/边界**：能否真的算出、退化情形（$n=0$、$k=0$、空集、rank 0、$g=0,1$）。
- **A5 层级**：定义 / 构造 / 命题 / 定理 / 猜想 / 猜想性定理；`proof.status` 与 `gap_note` 是否诚实（sketch 不要求补全，但**定理不能降级成猜想**，反之也不行）。
- **A6 术语**：首次出现是否定义；与一手来源的术语是否一致（人名拼写、复合词）；中译是否偷换（如「茎」vs「限制」、「等价」vs「同构」）。
- **A7 归因**：谁提出/证明、年份、文献编号；不要把 A 的定理记到 B 名下。
- **A8 形式化就绪**：能否直接写成 Lean 命题；变量是否都有类型；是否有未定义记号；是否有「适当」「自然」「显然」这类无法翻译的词；结论是否依赖未形式化的背景。

### B. 出处（sources）

- **B1 页覆盖**：`pages`/`pdf_pages` 是否覆盖 anchor 自述的行范围所涉页（不只是「背景页」）。
- **B2 节/编号**：`section`、定理编号是否真实存在（`{N.M.K}` 是否能在源码/PDF 里找到）。
- **B3 逐字引文**：有 `quote` 的，逐字核对；允许省略号断句，不允许改词、改符号、改上下标。
- **B4 anchor 行号**：`源码/chapters/chNN.tex:start-end` 是否真的覆盖该陈述（切出来读一遍）。
- **B5 多来源**：两条 `sources` 是否各自成立；不要把 A 条的页码借给 B 条用。
- **B6 页码偏移**：按 §4.5 复核；PDF 页 ≠ 印刷页时写清。

### C. 内部一致性

- **C1 字段互斥**：`summary`、`definition`、`key_points`、`theorems[].statement`、`formulas`、`pitfalls` 之间是否矛盾（尤其 summary 与正文）。
- **C2 记号统一**：同一对象在卡内是否始终同一记号（$\mathcal T$ vs $T$、$q$ vs $q_x$、$\check G$ vs $\hat G$）。
- **C3 related**：指向的 id 是否存在、标题是否对得上、方向是否说反。
- **C4 verification 陈旧**：卡改了之后，`verification.checks[].asserts/verdict` 是否还在断言旧文本。
- **C5 formulas ↔ definition**：公式里的符号是否都在 `definition.notation` 里定义过。
- **C6 pitfalls ↔ 正文**：坑是否其实与正文的说法冲突（如正文说「互相决定」，坑说「会丢信息」）。

---

## 6. 判定与严重度

行级 `verdict`：

- `pass`：三类都没有实质问题。**风格、记号选择、解释性补充、等价改写不算错。**
- `issue`：至少一条 check 有不一致，且你有可定位的证据。
- `unverifiable`：找不到可访问的一手来源，或来源本身缺失/矛盾到无法判定；必须写清「缺什么、试过什么」。

issue 的 `severity`（只按数学/形式化影响判，不按打字错误判）：

- `critical`：结论反了；定义恒真/恒假；核心公式符号或归一化错；定理被写成猜想或猜想被写成定理；量词错到命题不再是同一个。
- `major`：条件缺失或加强；方向错；关键因子错；定理编号/出处无法定位；例子算错；定义适用范围明显缩小/扩大。
- `minor`：页码、节号、术语拼写、related 断链、陈旧 verification、非关键记号漂移。

`confidence`：`high`（一手来源逐字确认）/ `medium`（一手来源间接或需一步推理）/ `low`（旁证或仅内部矛盾）。

**一次 issue 只写一个字段。** 同一卡多字段问题写多条 issue。

---

## 7. 记录格式（JSONL，一行一卡）

```json
{"n":1,"date":"2026-11-27","set":"glc","id":"glc/concept/xxx","path":"datasets/glc/cards/concepts/xxx.json","verdict":"issue","confidence":"high",
 "checks":[{"aspect":"definition","verdict":"ok","detail":"..."},
           {"aspect":"sources","verdict":"issue","detail":"p.36 记成 p.37"},
           {"aspect":"internal","verdict":"ok","detail":"..."}],
 "issues":[{"severity":"minor","aspect":"sources","field":"sources[0].pages",
            "card_says":"\"pages\": [37]","problem":"定理在 p.36","should_be":"\"pages\": [36]",
            "evidence":[{"kind":"pdf","ref":"glc.pdf p.36 L4-8","quote":"If E is geometrically irreducible …"}]}],
 "unverifiable_aspects":[],
 "notes":"页码口径：PDF=印刷页",
 "formalization_notes":["定理陈述可直接写；注意 E 需 geometrically irreducible"]}
```

硬约束：

- 每卡 `checks` ≥ 3，且 `aspect` 覆盖 A/B/C 三类（`definition`/`theorem`/`formula` 都算 A，`sources` 算 B，`internal` 算 C）。
- `issues` 非空 ⇔ `verdict == "issue"`；`verdict == "issue"` 时 `confidence` 不能为空。
- 每条 issue 必须有 `severity`、`field`、`card_says`、`problem`、`should_be`、`evidence`。
- `card_says` 去空白后必须是卡 JSON 文本的**逐字子串**（校验器会查）。
- `evidence[].quote` 必须是来源里的逐字句（可截断，不可改写）；`ref` 写「文件 + 页/行」。
- 不写「疑似」「可能」当结论；不确定就降 confidence 或判 unverifiable。

---

## 8. 修复边界（本任务不改卡）

- 每日巡检**只记录，不修改** `datasets/**` 下的卡与 md。
- 确认的 issue 进 `records.jsonl`，由人工/下一轮确认后按 `WORKFLOW.md` 的「最小修复 + before/after + fix_log」流程处理。
- 例外只有一个：如果 issue 是 `critical` 且会污染当天的形式化工作，立即在 SUMMARY 顶部标「⛔ 立即处理」，并单独发给用户；**仍然不要直接改卡**。

---

## 9. 常见误判与反模式

参考 `11_card_audit/casebook/` 的 32 例 + `11_card_audit/glc_full/casebook/` 的 25 例，最高频的 12 种：

1. **出处定位漂移**：`\srcpage`/目录/页眉不一致，按机械映射报错页。→ 先定页码偏移，再看正文。
2. **适用范围遗漏**：把「$\operatorname{rank}(E)>k$」读成「不再要求 $k<n$」。→ 条件改写 ≠ 取消条件。
3. **术语替换**：茎/限制、等价/同构、局部系统/可构造层。→ 回原文术语表。
4. **归一化/系数**：$q^{-1}$、$(-1)^i$、$[\,\text{shift}\,]$、twist。→ 对公式逐符号。
5. **内部不一致**：summary 与正文、pitfall 与 key_points。→ 用 C1/C6 扫。
6. **逻辑方向反转**：$\Rightarrow$ 写成 $\Leftarrow$、必要写成充分。→ 画箭头。
7. **证据强度夸大**：把 nLab 的术语页当定理证明。→ E2 只证术语。
8. **定理/猜想混淆**：把 conjecture 写成 theorem（或反之）。→ 看 `proof.status` 与原文标题。
9. **定义弱化/量词错误**：∀ 变 ∃、去掉唯一性、去掉非空。→ 逐字读量词。
10. **符号/约定漂移**：$\check G$ vs $\hat G$、$q$ vs $q_x$、$A$ vs $A_0$。→ 卡内统一 + 原文对照。
11. **归因错误**：作者/年份/编号错。→ 查文献首页。
12. **JSON 转义损坏**：改卡时 `\\`、`$`、引号写坏。→ 这次不改卡，但记录时也要保证 JSON 合法。

---

## 10. 质量闸门与交付物

**闸门**（全过才算完成）：

- `check_daily.py` 0 error；warning 逐条解释。
- 20 张全部有记录；每卡 ≥3 checks 且 A/B/C 覆盖。
- 所有 issue 的 `card_says` 能在卡 JSON 里搜到；所有 `quote` 能在源文件里 grep 到（在 notes 里留命令）。
- SUMMARY 的统计与 records 一致。
- `git status` 只多出 `daily_verify/<date>/` 与 `ledger.jsonl`。

**目录**：

```text
11_card_audit/daily_verify/
├── README.md
├── ledger.jsonl                  # 已核 id 台账（date,id,path,verdict,...）
├── tools/sample_daily.py
├── tools/check_daily.py
└── 2026-11-27/
    ├── sample.json
    ├── records.jsonl
    ├── SUMMARY.md
    └── notes/                    # 可选：一卡一 md
```

**SUMMARY.md 模板**：

```markdown
# 每日核验 <date>

- 采样：20 张（首次 18 + 补样 2）；集分布：glc 6、ggz 4 …
- 结果：pass 15 / issue 4（critical 0、major 1、minor 3）/ unverifiable 1
- ⛔ 立即处理：<卡 id>：<一句话>
- 页码口径：<本批涉及的偏移>

## issue 清单

| # | 卡 | 字段 | severity | 一句话 | 证据 |
|---|---|---|---|---|---|
| 1 | … | sources[0].pages | minor | p.37 → p.36 | glc.pdf p.36 L4 |

## unverifiable

- <卡 id>：缺 <来源>，试过 <arXiv/本地路径>。

## 本批可形式化提示

- <卡 id>：陈述可直接形式化；需补 <假设>。
```

---

## 11. 升级与停止条件

- 某卡 `critical` → 当天 SUMMARY 顶部 + 直接告知用户。
- 同一集连续 3 天 ≥3 条 issue → 建议该集做一次全量专项审计。
- 连续 3 天 `unverifiable` 占比 > 50% → 说明源缺失是系统问题，先补源再巡检，并在 SUMMARY 里列缺源清单。
- 任何一步无法完成（网络、SSH、磁盘）→ 保留已完成部分，SUMMARY 写清断点，不要伪造完成。

---

## 附：常用命令

```bash
# 抽样
python 11_card_audit/daily_verify/tools/sample_daily.py --n 20

# 自检 + 追加台账
python 11_card_audit/daily_verify/tools/check_daily.py \
  --file 11_card_audit/daily_verify/<date>/records.jsonl \
  --sample 11_card_audit/daily_verify/<date>/sample.json \
  --append-ledger

# 看某卡的源
python -c "import json;d=json.load(open('datasets/<set>/cards/concepts/<id>.json',encoding='utf-8'));print(json.dumps(d['sources'],ensure_ascii=False,indent=1))"

# PDF 取页
pdftotext -f 36 -l 36 -layout <pdf> - | head -60

# arXiv TeX
curl -L https://arxiv.org/e-print/<id> -o /tmp/src.tar && tar -xf /tmp/src.tar -C /tmp/src
```
