# Seidel《Fukaya 范畴与 Picard–Lefschetz 理论》资料卡

Paul Seidel, *Fukaya Categories and Picard–Lefschetz Theory*（EMS，2008）中文译注本的**可检索、可自测**资料卡。

一张卡只回答一个问题：**概念卡**回答「这是什么、为什么需要、哪里会错」，**推导卡**回答「这条论证怎么一步步走通、每步凭什么」，**勘误卡**回答「初版哪里译错、为什么必须改」。

- 底本：原书 334 页 PDF，印刷页 1–326；**PDF 页 = 印刷页 + 8**。卡中的 `原书 p.N` 一律指印刷页。
- 材料：301 页中文译注本（187 条译者注、40 条修订、12 份分章报告）——译稿本身**不入库**，只把其中的数学与校订结论裁成卡。
- 规模：**54 张** —— 16 张概念卡 + 8 张推导卡 + 30 张勘误卡。
- 权利：全部 `rights: "rewritten"`。定义、证明、要点用自己的话重写；公式照录；勘误卡的初版/改后引文**每处不超过 60 字**，只用于指出错误；不收录原书段落，也不收录译本正文。

## 30 秒入口

| 想做什么 | 打开 |
|---|---|
| 看全书骨架与卡的位置 | [MAP.md](MAP.md) |
| 按类型、轨道浏览 | [md/index.md](md/index.md) |
| 按 id / 页码检索 | [index.jsonl](index.jsonl) |
| 看一张概念卡 | [md/concepts/twisted-complex.md](md/concepts/twisted-complex.md) |
| 看一条推导链 | [md/derivations/lefschetz-induction.md](md/derivations/lefschetz-induction.md) |
| 看一条勘误 | [md/corrections/a03-section-4-19.md](md/corrections/a03-section-4-19.md) |
| 字段规范 | [SCHEMA.md](SCHEMA.md) |

## 三条轨道

| 轨道 | 主题 | 概念 | 推导 | 勘误 |
|---|---|---|---|---|
| A | A∞ 代数与三角范畴：μ^d、Tw、Karoubi、分裂生成、正合三角 | 6 | 6 | 5 |
| B | Floer 与 Fukaya：正合 Lagrangian、CF、Maslov、行列式线、膜结构、Fukaya 范畴 | 6 | 0 | 12 |
| C | Picard–Lefschetz：纤维化、消失圈、匹配圈、顶针、归纳与变异 | 4 | 2 | 13 |

## 这套卡是怎么来的

1. **校订先行**：82 个章节文件按原书页分成 12 段，逐段对照英文原文通读；公式与交换图回到原书页面图像逐式核对；共写 187 条译者注、31 处译文修订，另登记原书笔误。
2. **结论沉淀**：译者注汇总成 `译者注总表.tsv`（187 行），修订汇总成 `修订总表.tsv`（40 行），页码由 `page_map.csv`（81 个文件）与各条注文中的 `原书 p.N` 互校。
3. **裁成卡片**：概念与推导卡按「定义—要点—公式—定理与证明—易错点」重写；勘误卡按「初版—改后—为什么改」逐条落卡，合并了 operad（2 处）与 thimble（9 处）两组术语改动。
4. **机器质检**：`lint_cards.py` 校验字段、长度、id 与文件名、related 可解析、页码 1–326、anchor 以「原书 p.」开头、禁本机路径；`build_index.py` 与 `render_md.py` 生成索引与渲染版。

## 质检

```bash
python tools/lint_cards.py cards --strict     # 0 error 才算过
python tools/build_index.py                   # 重建 index.jsonl
python tools/render_md.py                     # 重建 md/
```

## 已知限制

- 全部卡 `status: "draft"`：机器质检通过，**未经人类逐卡认证**；若要用于训练，按仓库规则只能标 `dev`，不能直接当 `train`。
- 证明卡里 `sketch` 是诚实的缺口标记，不是完整证明；`gap_note` 说明缺在哪。
- 勘误卡只覆盖本次校订实际改动的 40 条，不是全书的全部误译；未改的可疑处留在分章报告的「存疑」节，没有强行落卡。
- 页码锚点取自译稿的 `\SourcePage` 与注文，个别跨页段落可能有一页误差；`page_map.csv` 只作交叉核对，不是独立证据。
