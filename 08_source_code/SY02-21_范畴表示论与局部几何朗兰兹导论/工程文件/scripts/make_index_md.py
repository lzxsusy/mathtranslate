import io, re, os
root = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论"
raw = io.open(os.path.join(root, "工程文件", "work", "条款索引_raw.md"), encoding="utf-8").read()
items = len(re.findall(r"^- (?:段|定理|引理|推论|命题|猜想|注|例|定义) ", raw, re.M))
eqs = len(re.findall(r"^- 公式 ", raw, re.M))
groups = len(re.findall(r"^### ", raw, re.M))
head = """# 资料卡 03 · 条款索引

本索引由译本 PDF 逐页抽取（`工程文件/scripts/index_md.py`），不是手工录入，因此可与原文逐项对账。

**怎么读**

- 每行格式为「类型 编号（页码）正文首句」；「类型」取 `定理／引理／推论／命题／猜想／注／例／定义／段` 之一，其中「段」指原文的 `\\subsubsection` 段落（无标题的 run-in 编号段）。
- 页码是**译本 PDF 的绝对页码**（1 = 扉页，2 = 摘要，3 = 译者说明，4 = 目录，正文自 5 起），与页脚印刷页码相差 1。
- `公式 (x.y)` 单独列一行，表示该小节内有编号公式 (x.y)。
- 分组标题 `### §x.y` 对应原文的小节。

**编号体制提醒**：原文用 amsart 的 `[subsubsection]` 共享计数器，所以同一个小节内「定理 3.2.10」之后直接就是「例 3.2.14」——定理类环境与编号段落**共用**编号。本书完全沿用了这一体制（`\\newtheorem{...}[subsubsection]`），因此编号与原文逐项相同。公式按节编号，附录为 (A.1)–(A.7)。

**规模**：@ITEMS@ 个编号条目、@EQS@ 条编号公式、@GROUPS@ 个小节分组。与原文对账：`\\label` 集合 132=132（缺 0、多 0、悬空引用 0），编号条目序列逐小节无缺号，编号公式 72=72。

""".replace("@ITEMS@",str(items)).replace("@EQS@",str(eqs)).replace("@GROUPS@",str(groups))
out = head + raw.lstrip("\n")
io.open(os.path.join(root, "资料卡", "03-条款索引.md"), "w", encoding="utf-8").write(out)
print("items", items, "eqs", eqs, "groups", groups, "bytes", len(out))
