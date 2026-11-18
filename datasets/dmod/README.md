# dmod · D-模资料卡

Dragan Miličić《Lectures on Algebraic Theory of D-Modules》（Utah，1999 修订版，150 页，5 章 35 节，283 条编号条目）的**结构化资料卡**：
一卡一个可独立回答的问题，共 **61 张**（59 张概念卡 + 2 张例子卡），按 O–H 九条轨道组织。
每张卡都对齐**校订批注本**的源码行号，并尝试在 nLab 与 Stacks Project 中逐字找依据。

- 底本：英文讲义 PDF，150 页（印刷页 = PDF 页 − 6）
- 工作底稿：同仓库 [`08_source_code/SY07-10_D-模的代数理论讲义（Miličić）`](../../08_source_code/SY07-10_D-模的代数理论讲义（Miličić）/) 的校订批注本（153 页，含 17 条校注）
- 卡片规范：[`SCHEMA.md`](SCHEMA.md)　生产流程：[`workflow/PRODUCTION.md`](workflow/PRODUCTION.md)　外部来源白名单：[`SOURCES.md`](SOURCES.md)
- 总表：[`taxonomy.md`](taxonomy.md)　索引：[`index.jsonl`](index.jsonl)　核验：[`verification.jsonl`](verification.jsonl)

## 核验状态

| 状态 | 张数 | 含义 |
| --- | --- | --- |
| `external-confirmed` | 17 | 至少一条 nLab / Stacks Project 页面逐字支持卡内断言，`checks[]` 记录了「哪句支持哪条」 |
| `source-only` | 44 | 与讲义逐句一致，但外部白名单里没有对应陈述（讲义自创构造或未成文定理）；**不声称外部已核** |
| `rejected` | 0 | 与权威陈述冲突 |

> `source-only` 不等于「有错」：它表示在公开的权威渠道找不到逐字对应，卡片仍严格对齐讲义原句。
> 引用这些卡时请按讲义页码引，不要写成「已由 nLab 确认」。

## 原文对齐（本库的硬闸）

`sources[].anchor` 形如 `源码/chapters/chap4.tex:991-1014（定理 4.7.1）`，指校订批注本的 LaTeX 源码。
`tools/build_verification.py` 会逐卡回查每个 anchor 的文件与行区间：

```
alignment: match 61 | broken 0 | no-anchor 0
```

坏 anchor 不允许入库；`broken > 0` 时脚本会逐条列出卡 id 与越界区间。

## 目录

```
cards/concepts/*.json   59 张概念卡（一卡一文件）
cards/examples/*.json   2 张例子卡
index.jsonl             轻量索引：id / type / track / title / summary / path
verification.jsonl      核验台账（一行一卡：status / alignment / checks / anchors）
taxonomy.md             分类体系（手写 §1–§5）+ 按 track 的卡片总表（脚本生成 §6）
MAP.md                  卡片关系图（related 图，含跨轨全图）
md/                     渲染后的 Markdown（一卡一文件）
tools/                  lint_dmod / build_index / build_verification / render_md / gen_docs
workflow/PRODUCTION.md  五角色四闸流程与本批记录
```

## 轨道

| track | 主题 | 张数 |
| --- | --- | --- |
| O | 预备：交换代数与维数 | 6 |
| A | 算子环与 $D(n)$-模 | 6 |
| B | 特征簇与完整模 | 9 |
| C | $\mathcal{D}_X$-模层 | 12 |
| D | 直像与逆像（六种运算） | 10 |
| E | Bernstein 不等式与 Kashiwara | 5 |
| F | 局部上同调与基变换 | 5 |
| G | 分类与联络 | 5 |
| H | 例子与计算 | 3 |

## 生产流程（本批实做）

1. **Lead** 读校订规范与校订批注本 → 写 `taxonomy.md`（轨道、粒度、slug 规则）与 `SOURCES.md`（可用外部来源白名单，含 nLab 的 Last revised 与 Stacks 的 Tag 断言原文）。
2. **drafter** 六人分轨起草（O+A、B、C、D、E+F、G+H），只依据校订批注本与 `SOURCES.md`，产卡到 `cards/**`。
3. **结构闸**：`tools/lint_dmod.py` 必须 `errors=0 warnings=0`（字段齐全、`related` 闭合、`summary ≤120` 字、`proof.sketch` 带 `gap_note`）。
4. **原文对齐闸**：`tools/build_verification.py` 回查全部 anchor → `alignment: match 61 | broken 0`。
5. **Lead 汇总**：去重（合并三张重复的「直像保持完整」卡、拆分两处 Kashiwara 定理、给两处「特征簇」与两处「Kashiwara 基变换」加消歧标题）、补跨轨 `related`、重跑四步。

## 本批修订记录（2026-11-19）

| 问题 | 处理 |
| --- | --- |
| `holonomicity-under-direct-image` 与 `holonomicity-preserved-by-direct-image` 覆盖同一条定理（5.3.1 / 5.3.4） | 删除前者，全部引用改指后者，并从后者连回 `preservation-of-holonomicity`（第 I 章 §13 的对应定理） |
| `kashiwara-theorem` 与 `kashiwara-theorem-statement` 同名不同定理（IV §8 的拟逆 vs I §12 的陈述） | 保留两卡，标题标明章号，互相连接 |
| 两处「特征簇」（$D(n)$-模 vs $\mathcal D_X$-模层）与两处「基变换」（4.10.2 vs 4.10.3）容易混 | 标题加限定语并互连 |
| `artin-rees-lemma` 的 JSON 有一处非法转义 `\le`（`$\le m_0$`） | 补成 `\\le`，`json.loads` 通过 |
| 19 张卡的 `summary` 超过 120 字 | 逐张改写到 ≤120 字（数学细节移到 `definition` / `formulas`） |
| 5 张卡的 `related` 指向未创建的 id | 补齐被引用的 5 张卡（投影公式、标准滤过、导出逆像、$i^+$ 同调维数、局部上同调） |

## 纠错

发现错误请开 issue 或在卡上标注：给出 **卡 id / 原句（`sources.anchor`）/ 错在哪 / 权威依据（URL + Tag 或页码）**。
修订时同时改三处：卡片字段、`verification.jsonl`（重跑 `tools/build_verification.py`）、`md/`（重跑 `tools/render_md.py`）。

## 复现

```bash
cd datasets/dmod
python tools/lint_dmod.py                # 0 error 才入库
python tools/build_verification.py       # 原文对齐闸 + verification.jsonl
python tools/build_index.py              # index.jsonl
python tools/render_md.py                # md/
python tools/gen_docs.py                 # taxonomy.md §6 / MAP.md
```

## 版权与引用

卡片是对讲义内容的**改写**（`rights: "rewritten"`），不逐字复制原文；数学记号与编号照讲义。
引用请注明底本：Dragan Miličić, *Lectures on Algebraic Theory of D-Modules*, University of Utah, 1999（中文校订批注本，2026），并给出本库卡 id。
