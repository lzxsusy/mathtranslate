# SCHEMA —— goresky04 资料卡字段规范

> 本文件只管 `goresky04` 这一包。通用规范见 `datasets/README.md` §2–§4。

## 1. id 与文件名

- 概念卡：`goresky04/concept/<slug>`，文件 `cards/concepts/<slug>.json`
- 推导卡：`goresky04/deriv/<slug>`，文件 `cards/derivations/<slug>.json`
- `<slug>` 只允许小写字母、数字与连字符（正则 `[a-z0-9]+(-[a-z0-9]+)*`）。
- **注意**：id 里是 `concept` / `deriv`（单数），**不是** `concepts` / `derivation`；目录名才是复数。

## 2. 轨道

| 轨道 | 主题 | 本包卡数 |
| --- | --- | --- |
| `O` | 总览：猜想陈述、两侧地图 | 2 |
| `A` | 域与 Galois 侧：域、平展上同调、$\zeta$ 函数、Frobenius | 5（4 概念 + 1 推导） |
| `B` | 自守侧：模形式、Hecke 算子、特征形式、平代环、自守表示 | 6（5 概念 + 1 推导） |
| `C` | 对应与障碍：Satake 参数、Eichler–Shimura、Shimura 簇、$n\ge3$ | 6（4 概念 + 2 推导） |
| `D` | 几何侧与展望：几何朗兰兹、函子性、对偶群 | 3 |

## 3. 来源与锚点

- `sources[].pages` 是**印本页**，范围 $1\le a\le b\le 20$（PDF 页 = 印本页）。
- `sources[].anchor` 正则：`^(A|B|C|D) (p\.\d+|nLab: .+)$`。
  - `A p.7`：原文第 7 页明确写了。
  - `B p.15`：原文只暗示/只有标题，我们补的中间步。
  - `C p.15`：我们的判断（原文没有）。
- `sources[].text` ∈ `A|B|C|D`，与 anchor 的首字母必须一致（lint 会查格式，不查一致性，作者自觉）。
- **§8.2–8.7 与 §7.3 的正文是空的**：这几页的卡一律用 `B p.15` 级锚点，并在 `provenance_note` 里写明「原文正文空缺，本卡按标题补，属译者按」。这是本包最重要的一条纪律——不把补的内容冒充原文。

## 4. 概念卡字段

| 字段 | 要求 |
| --- | --- |
| `title` | 中文题名，可含 LaTeX 行内公式 |
| `aliases` | ≥1 条，英文名/别名，便于检索 |
| `track` | `O/A/B/C/D` |
| `summary` | ≤120 汉字，无公式与空白，一条说完「是什么 + 为什么重要」 |
| `question` | 以「？」结尾，一句话，是这张卡要回答的问题 |
| `definition.text` | 定义，3–6 句，必须先给「设 …」再给「称 …」 |
| `definition.notation` | 记号说明，至少列 2 个符号 |
| `key_points` | ≥3 条，每条回答「为什么需要它」，不是复述定义 |
| `formulas` | ≥1 条，LaTeX 源码 |
| `theorems` | 每条含 `name`/`statement`/`proof{status,steps,gap_note}`/`source` |
| `pitfalls` | ≥2 条，写「最容易错在哪」 |
| `related` | ≥1 条，必须是已存在的 id（`--strict` 会查） |
| `sources` | ≥1 条，见 §3 |
| `provenance_note` | 一句话说明这张卡对应原文哪几页、哪些是我们补的 |

### proof.status

- `complete`：原文给了完整证明（本包几乎没有）。
- `sketch`：原文给了证明思路，我们补了步骤——**必须写 `gap_note`** 说明哪几步是我们补的。
- `gap`：原文只有结论，没有证明——**必须写 `gap_note`** 说明该去哪找（文献标签）。

## 5. 推导卡字段

在概念卡公共字段外，另有：

| 字段 | 要求 |
| --- | --- |
| `goal` | 一句话：这张卡要证什么 |
| `setup` | ≥1 条前提（每条一句，带公式） |
| `steps` | ≥3 步，每步 `{no,text,why,locator,provenance}` |
| `result` | 一句话：算完得到什么，它在整篇文章里起什么作用 |
| `gaps` | 列表，写清哪一步原文没给 |

每步的 `why` 写**为什么这一步成立**，不是复述 `text`。`locator` 是 `A p.N`，`provenance` ∈ `A|B|C`。

## 6. 写作纪律

1. **`why` 写机制**：不是「由定理 3.1 可得」，而是「因为 $\Fr_p$ 在非分歧处共轭类良定义，所以特征多项式不依赖选取」。
2. **空节不代拟**：§7.3、§8.2–8.7 的卡只写「原文此处空缺 + 本该讲什么」，不写成正文章节。
3. **数字与页码必须可核**：任何「原文说 X」都要能用 `A p.N` 在 20 页内找到。
4. **不引入库外文献**：需要引用时只用原文的 22 条参考文献标签（[Ar][F][G1][G2][Gr][Kn][K][R1][T] 等）。
