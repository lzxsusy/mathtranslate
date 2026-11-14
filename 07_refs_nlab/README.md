# nLab 参考资料库（07_refs_nlab）

本目录是翻译《Langlands 纲领导论》（SY02-09）时建的 **nLab 条目摘要缓存 + 替代来源卡**，随仓发布，
供后续几何 Langlands 相关文献的翻译、校订与讲注直接复用——不必每次重新抓取、重新判断某个词条是否可用。
2026-11-15 又为《几何朗兰兹对偶是什么？》（SY02-10，Ben-Zvi 2026 综述）补抓 16 条，清单见
`tools/list_BenZvi2026.tsv`。

## 一、`pages/`：nLab 条目摘要（136 条）

- 每条对应 `https://ncatlab.org/nlab/show/<slug>`，抓的是该页的 **Instiki 源码**（`/nlab/source/<slug>`），
  比渲染后的 HTML 干净约 5 倍；保留标题、URL、`last_revised` 与正文前 6000 字符。
- 文件头四行固定格式：
  ```
  # <标题>
  url: https://ncatlab.org/nlab/show/<slug>
  last_revised: YYYY-MM-DD
  ---
  ```
  `last_revised` 取自页面底部 `Last revised on <月> <日>, <年> at …`，可直接写进译注来源行
  （`[来源：nLab "entry"，<url>（Last revised YYYY-MM-DD；YYYY-MM-DD 访问）。]`）。
- 索引：[`INDEX.tsv`](INDEX.tsv)，列 `file / slug / url / last_revised / title`。

## 二、`alt/`：nLab 没有（或只有存根/重定向）时的替代来源卡（37 份）

经典数论与表示论概念在 nLab 上覆盖很薄——`ramification index`、`idele group`、`newform`、
`local langlands correspondence` 等 31 个词条实测 404 或只剩存根。这些词条的来源改走
**本讲参考文献（A 级教材，带版次与章节）或 MathWorld / Stacks Project（B 级）**，每张卡片六字段：

```
concept / level / citation_zh / citation_en / verified / note
```

- [`alt/INDEX.tsv`](alt/INDEX.tsv)：全部替代来源卡索引
- [`alt/_BIB.tsv`](alt/_BIB.tsv)：从 23 讲 `references` 环境里抽出的书目（作者/年份/题名/出处），
  是判断"某词条能不能引本讲文献"的底账
- [`alt/AUDIT_SOURCES.md`](alt/AUDIT_SOURCES.md)：两批共 **110 条**译注的来源真实性抽查记录
  （PASS 98 / WARN 11 / FAIL 1，FAIL 已整改），每条含文件:行号与核对依据

## 三、怎么用（下次翻译几何 Langlands 时）

1. **先查本目录**：`grep -ril "<英文术语>" pages/ alt/`，命中就直接拿来源行，不用再抓。
2. 没命中 → 用 `tools/nlab_fetch.py` 补抓（同目录 `tools/` 下有完整脚本与 `list_*.tsv` 示例）。
   ⚠️ 必须走 `/nlab/source/<slug>`；**不要**用 nLab 的 `/nlab/search?query=`（实测解析不出结果），
   找 slug 用 `tools/nlab_index.py`（先抓 `all_pages` 建 2 万条 slug 索引）。
3. 仍然没有 → 按 `04_playbook/01_数学文献翻译纪律.md` §2.5 的顺序降级：
   本讲参考文献 A 级教材（带版次、章节）→ MathWorld / Stacks（B 级，Stacks 写 Tag 号）
   → 本库既往译注（I 级，标 `本库:SYxx-yy`）→ 实在没有外部依据才写
   `[译者按（上下文推断，无外部依据）：…]`。
4. **红线**：不编 URL / 日期 / 定理号；不用"众所周知"顶替来源；不引知乎、百度百科、CSDN、
   简书、公众号、B 站笔记、个人博客、AI 摘要与搜索摘要卡。

## 四、与术语表的关系

同一批术语的定案表在 [`../01_corpus_zh/terms_frozen_SY02-09.tsv`](../01_corpus_zh/terms_frozen_SY02-09.tsv)
（223 条：英文 / 中文 / 等级 A·B·I / 依据 / 首次出现讲次 / 本轮校订备注），
机器可读版本是 [`../01_corpus_zh/termbase.jsonl`](../01_corpus_zh/termbase.jsonl) 中 `pkg=SY02-09` 的 215 行
（`status=confirmed`）。术语与来源一一对应：定案表里 `等级=B` 且写 nLab 的条目，都能在本目录 `pages/` 里找到对应页。

## 五、同名不同义的坑（引用前必看）

nLab 的条目名常常比我们要的义项更宽或另有所指，直接引会闹错。本轮踩到并已处理的四个：

| 条目 | 坑 | 处理 |
|---|---|---|
| `polarization` | 该页讲**辛流形**的极化，与阿贝尔簇的极化（polarization of an abelian variety）无关 | 改引 MathWorld "Abelian Variety Polarization"（B 级），这是本轮唯一一条 FAIL 的来源，已整改 |
| `symmetric power` | 重定向到 `symmetric algebra`（对称代数），不是曲线/流形的对称幂 | 改引 MathWorld "SymmetricPower"（B 级） |
| `artin map` | 只有 `Artin reciprocity law`（互反律本身），没有"Artin 映射"这个词条的独立条目 | 引 `Artin reciprocity law` 页并在译注里点明，或用本讲参考文献 |
| `root system` | 重定向到 `root (in representation theory)`，是表示论意义的根系 | 根系与根数据改引 Springer《Reductive groups》（本讲 [S]，A 级） |

2026-11-15 为 SY02-10 核词条时又踩到四个，都是**重定向**（`/nlab/show/` 返回 200，`/nlab/source/` 却没有 textarea，抓取脚本报 NOTFOUND）：

| 条目 | 重定向到 | 处理 |
|---|---|---|
| `singular support` | `support of a distribution`（分布的支集），义项完全不同 | 不作链接，改引 `characteristic variety`（2017-08-29），并在译注里写明原因 |
| `moduli stack of G-principal bundles` | `moduli space of bundles` | 统一引 `moduli stack`（合并为一行的「$G$-主丛／向量丛模栈」） |
| `moduli stack of vector bundles` | 同上 | 同上 |
| `geometric Langlands program` | `geometric Langlands correspondence` | 只保留 `geometric Langlands correspondence` 一行，不重复列 |

**不要引存根页**：只有一两行文字、正文 200 字符以内的 nLab 页（本库 `pages/` 里 `chars` 很小的那些）不构成"定义展开"的依据，按 A 级教材处理。

## 六、抓取日期与维护

- 全部条目抓取/核对于 **2026-11-14**（SY02-10 补充的 16 条于 **2026-11-15** 抓取）；`last_revised` 是各条目在 nLab 上的最后修订日期，随条目一同记录。
- nLab 条目会继续修订：若某条 `last_revised` 已明显早于当前日期而结论又被新文献推翻，重抓该条并更新
  `INDEX.tsv` 与引用它的译注。
