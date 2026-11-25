# 卡片手流程（PRODUCTION）

你在 Phase 3 被指派一组卡片。**只写 `cards\concepts\`、`cards\examples\` 下的 json**，别碰工程里的其它文件。

## 0. 开工前读三样

1. `SCHEMA.md`（本目录上一层）——字段与硬规则，含一个完整示例。
2. `taxonomy.md` 的「轨道」表——确认你负责的 track 和配额。
3. 你那张卡对应的章：`..\Grassmannians-精读\产出\导读\chNN-导读.md`（别人写的，先看省事）
   和 `..\Grassmannians-精读\source\chapters\chNN.tex`（正文，数学以此为准）。

> 页面渲染：`python ..\Grassmannians-精读\tools\pdf_pages.py png zh 12 --dpi 140`
> 取文本：`python ..\Grassmannians-精读\tools\pdf_pages.py text zh 7-9 -o tmp\x.txt`
> PDF 文字层的公式是碎的，只能用来定位；定义与公式一律从 `.tex` 抄并核对。

## 1. 选题

- 一个概念一张卡。先 `grep` 一遍 `cards\`，已有就别重复建，改进旧卡或加 `aliases`。
- 选的标准：**读懂它需要超过三句话**。太初等的（如「向量丛」）不建卡；本书特有的、反复引用的才建。
- 例子卡只选真能算完的：能写出显式取值、能画出区间/表格、结论能用一两行验算。算不完就别建。

## 2. 写卡（按这个顺序，不要跳）

1. `definition.text`：先照着 `.tex` 抄准，再改写成自己的话。公式里的每个符号都在 `notation` 里交代。
2. `key_points`：3–5 条，写「为什么这样定义」「什么时候退化」「和相邻概念什么关系」，不写复述。
3. `theorems`：只放**本章真用到**的定理，`proof.status` 老实填：
   - `complete` 的前提是你自己把步骤写全了（steps ≥2，每步 `text` 说做了什么、`why` 说为什么合法）；
   - 只抄了结论没抄证明 → `reference`；
   - 知道证明思路但有一步过不去 → `sketch` + `gap_note` 写清哪一步。
   **不许把 reference 写成 complete。**
4. `pitfalls`：写你（或译文）真会踩的坑。最好的来源是：你第一次读时误解的地方、errata 里的错误、符号冲突。
5. `related`：≥2 张，优先跨章（这是资料卡的价值所在）。
6. `sources.anchor`：`chapters/chNN.tex:行号`，行号必须是**定义或定理真正开始的那一行**。

## 3. 自检

```
python tools\validate_cards.py            # 你写的卡 0 error
python tools\build_index.py               # 能出索引
```

常见报错与修法：

| 报错 | 修法 |
|---|---|
| `anchor … line N is blank` | 行号偏了，往上找定义起始行 |
| `anchor … exceeds file length` | 章号或行号错，重新 grep `\section` 定位 |
| `related … not found` | 你引用的卡还没建：换一张已存在的，或把 id 报给 Lead 让他补 |
| `summary: N 汉字` | 太长就砍定语，太短就补「它解决什么问题」 |
| `formula: odd number of $` | 公式里少一个 `$`；多行公式用 `\\` 分行但 `$` 要成对 |
| `contains absolute path` | 删掉本机路径 |

## 4. 交付

- 卡片 `status` 保持 `draft`，Lead 抽查后才改 `reviewed`。
- 在做章 report 里登记一行：`id | track | 一句话 | anchor`。
- 不确定的数学**不要装懂**：写进卡的 `gap_note` 或报给 Lead，宁可少一张卡，不可错一张卡。
