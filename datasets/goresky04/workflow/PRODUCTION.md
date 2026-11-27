# PRODUCTION —— goresky04 资料卡生产流程

> 五步。每一步都可以停，停在哪一步，卡就停在哪个状态。

## 第 1 步：抽页并对齐

```bash
python -c "import pymupdf,sys; d=pymupdf.open('06_Goresky_Langlands_Conjectures_for_Physicists.pdf"); \
  open('work/原文/fulltext.txt','w',encoding='utf-8').write(''.join(f'===== PDF p.{i+1} =====\n'+p.get_text() for i,p in enumerate(d)))"
```

- 底本是 dvips 生成，文本层干净，可以直接抽；**PDF 页 = 印本页**，偏移 0。
- 抽完立刻检查：页数是否 20、每页是否有 `===== PDF p.n =====` 标记、$\\zeta$、$\\Fr_p$ 这类符号是否变成乱码（dvips 常见 `ﬁ` 连字）。

## 第 2 步：定 id 清单

先写一张「原文节 → 卡 id」的对照表（本包见 `MAP.md` 末尾），再动手写卡。**顺序很重要**：先定 id，后写内容，避免写到一半改名。

id 命名规则：用**概念名**而不是节号（`satake-parameter` 而不是 `section-6-4`）。

## 第 3 步：用生成器写卡

```bash
cd workflow
python cards_oa.py    # O 轨 2 + A 轨 5
python cards_b.py     # B 轨 6
python cards_cd.py    # C 轨 6 + D 轨 3
```

卡写在 `cards_*.py` 里（Python dict），由 `gen_cards.py` 统一序列化成 JSON。好处：

- 不用手写 JSON 转义（LaTeX 里全是反斜杠）；
- 同一张卡的 `summary`/`question`/`sources` 只写一次；
- 改一个字段重跑一次即可。

**写卡时刻意区分三档来源**：
`A` 原文明确写了 / `B` 原文暗示、我们补的中间步 / `C` 我们的判断。这个区分体现在 `sources[].anchor` 首字母与推导卡每步的 `provenance` 上。

## 第 4 步：三道校验

```bash
python tools/lint_cards.py cards --strict   # 字段、id、related 可解析、页码范围
python tools/build_index.py                 # index.jsonl（22 行）
python tools/render_md.py                   # md/（22 个 md + index.md）
```

`--strict` 与 `--allow-missing` 的区别：前者要求所有 `related` 指向的卡都已存在。**发布前必须跑 `--strict` 且 0 error。**

## 第 5 步：登记与对账

1. `08_source_code/SY02-42_.../资料卡/` 五件套（00 速览 / 01 结果清单 / 02 论证地图 / 03 条款索引 / 04 术语文献勘误）；
2. `03_translations_meta/SY02-42/投稿信息.md`；
3. `RELEASE_REGISTER.csv` 加一行（16 列）；
4. `datasets/README.md` §1 包表加 `goresky04/` 行、版本日志加一条；
5. 仓库根跑 `python make_stats.py --write`。

## 已知空白

- **§7.3、§8.2–8.7 正文为空**：本包为这几节各写了一张卡，明确标注「原文空缺 + 译者按」，**没有**代拟正文。
- **§8.7「重大结果抽样」**：原文只留标题、指向参考文献 [F]，本包没有为它单独建卡（因为没有内容可锚）。
- **注 6（自守因子）与注 25（Satake 同构）**：内容很长，已在译本的「注释」中全文译出，本包只把它们的结论吸收进 `satake-parameter` 与 `automorphic-representation` 两张卡，没有单独建卡。
