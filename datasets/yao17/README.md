# 一般线性群的局部 Langlands 对应 · 资料卡（yao17）

**一句话定位**：这是 Zijian Yao《Notes on Local Langlands for GLn》（哈佛学习讨论班，2017 秋，**36 页**）的中文资料卡。讲义用六节、36 页把 $\GL_n$ 的局部 Langlands 对应讲成一条可操作的链：Weil–Deligne 表示 → $\GL_n$ 的容许/超尖点表示 → LLC 的陈述与 Henniart 路线 → Bernstein–Zelevinsky 分类与不变量（平方可积、缓增、generic、导子、深度）→ 惯性 Langlands → 收尾三节只剩标题。本包把它拆成 **29 张卡（23 概念 + 6 推导）**，与同目录配套的中译注本（`08_source_code/SY02-43_一般线性群局部Langlands对应讲义`）逐页对齐。

## 一张卡只回答一个问题

- **概念卡**三问：这是什么？为什么需要它？哪里容易讲错？
- **推导卡**两问：这条推导怎么走通？每一步凭什么（原文写了什么，哪里是我们补的）？

## 底本与规模

- **A** = Zijian Yao, *Notes on Local Langlands for GLn*, 哈佛大学 2017 秋学习讨论班讲义，**印刷页 1–36**（底本 PDF 页 = 印刷页，偏移 0）。引用一律写印刷页。
- **B** = 白名单二次文献（nLab、Stacks Project、ProofWiki）与本库译注；**C** = 原始文献（Bernstein–Zelevinsky、Zelevinsky、Bushnell–Kutzko、Henniart、Paskunas 等，书目见译本 §参考文献）。
- 规模：**29 张 = 23 概念卡 + 6 推导卡**，全部 `status: "dev"`、`rights: "rewritten"`。
- 轨道分布：O（总览与主陈述）3、A（Weil–Deligne 侧）7、B（自守侧）7、C（分类与不变量）8、D（惯性 Langlands 与类型）4。
- 底本没有 LaTeX 源码，PDF 文本层可抽取（36 页、75,579 字符）；全部引文均已对回原 PDF 页核对。底本有 11 条编号脚注，译本 §原注 逐条译出。

## 30 秒入口

| 想看什么 | 打开 |
| --- | --- |
| 全包骨架与四条阅读路径 | `MAP.md` |
| 按轨道浏览全部卡 | `md/index.md` |
| 机器可读轻量索引 | `index.jsonl` |
| 概念卡样例 | `cards/concepts/llc-statement.json`、`wd-representation.json`、`bz-classification.json` |
| 推导卡样例 | `cards/derivations/wd-from-galois.json`、`inertia-from-bernstein.json` |

## 四条阅读路径

1. **只想懂 LLC 在说什么**（约 12 分钟）：`llc-statement` → `llc-finer-properties` → `bz-classification` → `gl2-llc-cases`。
2. **想通「$\rho\mapsto(\rho,N)$ 怎么来、$L$/$c$ 怎么算」**：`weil-group` → `wd-representation` → `wd-from-galois` → `frobenius-semisimple` → `wd-functor` → `tate-epsilon` → `wd-invariants`。
3. **想懂「为什么只需在超尖点上验证 LLC」**：`smooth-admissible` → `hecke-modules` → `parabolic-induction` → `jacquet-supercuspidal` → `supercuspidal-criterion` → `bz-classification` → `zelevinsky-segment` → `induction-to-supercuspidal` → `gl2-llc-cases`。
4. **只关心惯性侧**：`bernstein-decomposition` → `inertia-from-bernstein` → `inertial-correspondence` → `type-and-k-type`。

## 术语

与 `08_source_code/SY02-43_一般线性群局部Langlands对应讲义/工程文件/work/glossary.tsv` 同一份冻结表；外部核对记录见该工程的 `术语外部核对_香蕉空间.md`。五条硬约定：

- `supercuspidal` 一律译「超尖点」、`cuspidal` 译「尖点的/尖点表示」：香蕉空间有「尖点表示」的实际用例，但无「超尖点」专条，故沿本库既有冻结译名。
- `Weil–Deligne representation` 译「Weil–Deligne 表示」，`Weil group` 译「Weil 群」，保留连字符与拉丁拼写；`$\mathrm{Sp}_m$`/`$\mathrm{St}_m$` 分别写「$\Sp_m$」与「Steinberg 表示 $\St_m$」。
- `generic` 译「一般的」（不译「泛型的」「通用的」），`Whittaker model` 译「Whittaker 模型」。
- `component`（Bernstein）译「分量」，`block` 在 Bernstein–Zelevinsky 语境译「块」；`segment` 译「段」。
- `type` 译「类型」，`$K$-type` 写「$K$-型」（底本 p.35 明说与 Bushnell–Kutzko 的 type 不同，卡里已注明）。

## 生产与校验

```bash
python workflow/gen_cards.py                # 由 workflow/cards_*.py 生成 cards/
python tools/lint_cards.py cards --strict   # 字段、id、related、anchor、页码范围
python tools/build_index.py                 # 重建 index.jsonl
python tools/render_md.py                   # 渲染 md/（人读版）
python tools/card_spec_check.py --set yao17 --strict   # 仓级规范（在仓库根目录跑）
```

最近一次校验：`cards=29 hard=0 warn=0`。

## 许可与出处

底本版权归原作者 Zijian Yao。卡内文字为中文重写（`rights: "rewritten"`），每张卡都在 `provenance_note` 里写明「哪些是原文的、哪些是我们整理的」。底本 PDF 不入仓（`原文级别: L4 禁入`）。
