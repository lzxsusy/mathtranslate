# STYLE_GUIDE —— SY05-26 语言与体例规范

## 一、总体原则

1. **准确优先于流畅**。原文是研究论文，语气谨慎（大量 “should”“it is natural to expect”“we believe”），中译不得把这些弱化语气改成断言。
2. **不增删论证**。原文的“我们假设”“粗略地说”“在某种意义上”必须保留；不能为了通顺补出原文没有的因果。
3. **公式不动**。所有公式、编号、符号沿用作者源码；译者不改写公式，只改公式前后的文字。
4. **术语一致**。以 `work/glossary.tsv` 为准；同一英文词在全书中只用一个中文译名（除首次出现可加括注）。

## 二、体例

| 项 | 规定 |
|---|---|
| 章节标题 | 沿用原文层级；`\section` 译为“章”级标题，不编号改动 |
| 术语首现 | `\term{中文}{English}`，只在本节首次出现时用 |
| 强调 | 原文无衬线强调 → 粗体（`\emph` 已重定义为 `\bfseries`） |
| 公式编号 | 沿用原文（按节编号），不重排、不补号 |
| 图 | 图题译为中文；图内英文标签保留原样（作者图不可改） |
| 参考文献 | 原样保留作者条目与编号，不译、不删、不增 |
| 脚注 | 全部译出；原文脚注中的公式照抄 |
| 引号 | 中文引号「」用于术语与引语；英文引号保留于直接引用的英文短语 |
| 数字与单位 | 数字用阿拉伯数字；“二维”“$n$ 维”按中文习惯 |

## 三、术语规范（节选，全表见 deliverable/术语对照表.tsv）

- brane 膜；A-brane / B-brane A-膜 / B-膜；coisotropic brane 余各向同性膜；canonical coisotropic brane 典范余各向同性膜
- polarization 极化；real / complex / Kähler / holomorphic polarization 实 / 复 / Kähler / 全纯极化
- prequantum line bundle 预量子线丛；metaplectic correction 亚辛校正；Spin$^c$ structure 旋量$^c$ 结构
- geometric quantization 几何量子化；deformation quantization 形变量子化；quantization via branes 膜量子化
- half-density 半密度；leaf 叶；B-field B-场；complexified symplectic form 复化辛形式
- hyper-Kähler 超 Kähler；affine linear structure 仿射线性结构；exact symplectomorphism 恰当辛同构
- Lagrangian correspondence 拉格朗日对应；topological interface 拓扑界面；domain wall 畴壁；corner 角
- Chan–Paton bundle Chan–Paton 丛；tame symplectomorphism 驯顺辛同胚；central extension 中心扩张
- conformal blocks 共形块；Ricci potential Ricci 势；mapping class group 映射类群

## 四、批注规范

- **译注**（`yizhu`）：解释背景、补足跳步、说明译法取舍。必须带 `[来源：A 级]` / `[来源：B 级]` / `[来源：I 级]`；无外部依据时写 `[译者按（无外部依据）]`。
- **校勘**（`kanwu`）：只标“原文写法 → 建议改法”与依据；明显笔误直接改正文并在汇总中记录，有歧义者保留原文加框。
- **概念卡片**（`conceptbox`）：每章至多一张，放该章核心概念的“一句话定义 + 三个要点”，标明“（译者所加）”。
- **本节重点**（`keytakeaways`）：仅用于长节（§3、§4），列 3–5 条，不重复正文原句。

## 五、LaTeX 约定

- 源码的 51–214 行单字母宏（`\B`、`\cc`、`\j`、`\S`、`\U` 等）整体照搬，正文公式直接复制；不要在译文中新造宏。
- 方框环境必须成对：`\begin{yizhu}[标题] … \end{yizhu}`，不可写成 `\yizhu{…}`。
- 图路径写 `figures/xxx.pdf`（preamble 无 `\graphicspath`）；文件名全小写。
- 新标签用英文小写短语，避免与原文标签冲突（原文标签如 `scbq`、`branerp` 已占用）。

## 六、常见错误清单

1. 把 “should” 译成“必须”。
2. 把 “we believe / it is natural to expect” 译成“可以证明”。
3. 术语前后不一（如“预量子”与“前量子”混用）。
4. 公式里擅自增删 `\hbar` 或交换上下标。
5. 译注无来源标注。
6. 方框未闭合导致后续 figure 报 “Not in outer par mode”。
