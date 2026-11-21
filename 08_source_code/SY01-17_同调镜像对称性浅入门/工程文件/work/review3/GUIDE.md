# 第三轮校订工作指南（对照英文原书）

本轮与第二轮的根本区别：**手上有英文原书全文**（PDF 文本层提取），因此逐段对照英文，找真正的误译、漏译、加译与数学错误；不再只做中文内部一致性。

## 文件

- 中文定稿：`chapters/chNN.tex`（你只改自己这一章，别的章一概不碰）。
- 英文原文：`work/review3/en/chNN.txt`。格式：
  `===== BOOK PAGE 216 =====` 后面是该页文本；页码为书页码（= PDF 页码 − 12）。
- 你的产出：
  1. 直接改 `chapters/chNN.tex`；
  2. 写 `work/review3/chNN.json`（逐条改动清单，见下）；
  3. 写 `work/review3/chNN.digest.md`（200–400 字：改了几处、主要问题类型、存疑项）。

## 英文文本的可信度

PDF 文本层对**数学公式是坏的**（上下标、符号、希腊字母常丢失或错位），对**普通句子是好的**。因此：

- 判断句意、定义、定理陈述、条件、量词、因果，用英文；
- 判断公式，以中文 LaTeX 为准，除非英文句子明确说明公式结构而中文明显不符；
- 英文里读不通的片段，不要据此改中文，记入 uncertain。

## 允许改的（按优先级）

1. **误译**：句意与英文相反、主体/对象搞错、条件丢失或加强。
2. **漏译**：英文整句/整段的信息在中文缺失（尤其是定义中的条件、定理的假设）。
3. **加译**：中文出现了英文没有的断言、例子、因果（导读/评注除外，见下）。
4. **数学错误**：公式、符号、上下标、量词、方向、维数、编号与英文或上下文矛盾。
5. **术语不一致**：与冻结术语表冲突，或同一概念前后两名。
6. **中文不可读**：硬译到读不懂、指代不明、句子成分残缺。只改到读得通，不追求文采。

## 禁止

- 不许改 `\label`、`\ref`、`\eqref`、`\cite`/`\bookcite` 的 key、`\index` 的排序 key（`拼音@` 的前半段）；可以改 `\index` 的显示文字。
- 不许改章节结构、环境名、图文件路径、`\begin{...}`/`\end{...}` 配对。
- 不许整段重写、不许润色式改写（改动行数应远小于全章行数）。
- 不许动 `\takeaway{...}` 的**存在**（它是译者导读，英文原书没有）；但其中若有与正文/英文矛盾的事实错误，可以改。
- `% [Tutor Note: ...]` 批注是译者所加，英文没有；只在批注事实错误时改，不新增超过 2 条。
- 不许把英文术语硬造中文新词；拿不准就保留英文并记入 uncertain。

## 冻结术语（不要改）

箭图 quiver；层/预层 sheaf/presheaf；凝聚层 coherent sheaf；消解 resolution；crepant 消解；通有 generic；gentle 代数 / gentle $A_\infty$ 代数；阿米巴 amoeba；二聚体 dimer；商栈 quotient stack；胖点 fat point；环簇 toric variety；带对象 band object；弦对象 string object；完美匹配 perfect matching；矩阵分解 matrix factorisation；扭曲复形 twisted complex；导出范畴 derived category；Fukaya 范畴；wrapped / stop / thimble 保留英文。

## 改法（必须可复核）

用 Python 精确替换，每次断言命中数为 1：

```python
import io
p='chapters/ch08.tex'; s=io.open(p,encoding='utf-8').read()
old='……'; new='……'
assert s.count(old)==1, s.count(old)
io.open(p,'w',encoding='utf-8').write(s.replace(old,new))
```

一次脚本可批量做多条，但每条都要 `assert count==1`；若某条 old 在文中出现多次而你只想改一处，就把 old 扩到足够长的唯一片段。

改完后自检：

```
python tools/check_chapter.py chapters/chNN.tex
```

（检查花括号/环境配对、`\index` 花括号、行数变化。）

## chNN.json 格式

```json
[
 {"line": 447, "cat": "误译", "old": "……", "new": "……",
  "why": "EN p.224: '...' 意为……；原译把主语弄反。"}
]
```

`line` 用改动前的行号（从 1 开始）。`old`/`new` 必须与文件中的实际片段一致（含标点）。`cat` ∈ {误译, 漏译, 加译, 数学, 术语, 中文}。

## 存疑

拿不准的（英文公式乱码、疑似原书笔误、两种读法都通）不要改，写进 `work/review3/chNN.uncertain.md`，每条注明页码、中文行号、英文原句、你的两种理解。这部分同样有价值，主校会逐条裁决。

## 语气

这是给读者读的译本，不是审稿意见。改动要让句子更像中文数学书，而不是更像英文。
