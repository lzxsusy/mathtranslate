# trace · 15 ggl15

判断记录按实际发生顺序排列；「事后确认」列写的是回查动作与结果，不是猜测。

| # | 判断点 | 依据 | 结论与理由 | 事后确认 |
|---|---|---|---|---|
| 1 | PDF 页与印刷页的对应关系 | `txt/15/p002.txt` 末行为页脚「1」，`p003.txt` 末行为「2」；`p056` 无正文 | 本篇 PDF 页 = 印刷页 + 1（封面占 p001）。所有卡片、notes、excerpts 的页码统一用 PDF 页序，避免把 p035 写成印刷页 34 | 用 `p001`（标题+摘要）与 `p002`（§1 开头）逐页核对页脚，确认 56 页中含 1 页封面 |
| 2 | p028/p029 的公式能否直接引用 | `grep` 把 `p028.txt` 判为 binary；`sed` 读出的行里夹着控制字符，公式被截断 | 不能照抄 txt。改用 PyMuPDF 的 `get_text("text")` 逐页取文本，并把两页渲染成 PNG 放到 `external/` 目视核对 | `out/15_ggl15/external/page028.png`、`page029.png` 为 200 dpi；get_text 给出的 (5)(11)(16)(17)(22) 与图一致，确认乱码是 extract.py 写文件时的编码问题，不是 PDF 内容 |
| 3 | 推导卡的 `type` 该写什么 | 照概念卡习惯写了 `"type": "deriv"`；lint 报「type 与目录不符」 | 目录是 `cards/derivations/`，lint 要求 `type == "derivation"`、id 段才是 `deriv`。改为 `derivation` | 重跑 lint，三张推导卡该错误消失；对照 `out/14_ggl14/cards/derivations/cs-to-kw.json` 确认同为 `derivation` |
| 4 | minuscule 卡的 p36 引文 | 选了 "…has a unique asymptotically flat hyperkähler metric"，verify_pages 报 p36 搜不到 | 原因是归一化只保留 [a-z0-9]：卡片里的 `ä` 被整字丢弃，txt 里的 `hyperk¨ahler` 则留下 `a`，两边对不上。改引不含变音符的 "metric: the Eguchi-Hanson metric. Therefore, one can produce" | 重跑 verify_pages，39 条 quote 全部命中；教训是含 ä/ö/ü 的句子必须换掉或写成 ASCII |
| 5 | errata.tsv 的行与表头 | 先写数据行时把表头覆盖了 | lint 报「errata.tsv 缺表头」。恢复表头并保留 1 条数据行，9 个 tab 字段逐一数过 | 重跑 lint：`[ok] 包级检查：核对节 + errata 1 条`；`awk -F'\t'` 数出每行 9 列 |
| 6 | term_index 撞名 | 首轮 check 报 4 处：affine Grassmannian、GL twist、geometric Satake correspondence、Hecke functor | 按「译名以旧卡为准、不重复造卡」处理：保留中文标题，把英文别名改成本篇特有的限定形式（如 affine Grassmannian Gr_G、GL-twisted N=4 SYM） | 第二轮又冒出 Gr_G 与 Kapustin-Witten twist 两处，再改为 `Gr_G = G((z))/G[[z]]` 与 `KW twist`；第三轮 0 处 |
| 7 | p053 的 "eq. (42)" 是不是笔误 | 该段说「乘积的左右两边」，而 (42) 在 p035 是 D̄ρ=0、D̄†ρ=0 两个 PDE | 判为交叉引用滑脱，应为 (43)。但只有本篇一处内部证据、期刊版拿不到，按三源定则记 low、状态 open，不改卡片原文 | 回查 p036–p037：k=0 的乘积预言确为 (43)，m=0 另给 (44)；errata.tsv 第 1 行与 notes 4.2 一致 |
| 8 | (43) 在 m=0 是否与 (44) 矛盾 | 把 m=0 代入 (43) 会多出 WT_{0,0} 与 WT_{0,−2} 两项，看似与 (44) 冲突 | 回读原文：p037 明写 (43) 要求 m≠0，m=0 单独由 (44) 给出。不是笔误，不记 errata，只写进 notes「不是笔误但易误判」 | 重读 p037 原句 "for m ≠ 0"（txt 中为 `m 6= 0` 的渲染），确认无误 |
| 9 | (41) 的不等是否说明 (40) 错了 | (41) 两侧秩都是 n+1，容易误以为只是写法不同 | 两侧分层不同（O(−n)⊕…⊕O(n) vs 平凡丛），作为线算符确实不等；本文的论点是「只在 K-理论里相等」，故 (40) 应读作 K0 恒等式，不是笔误 | 用 p034 的滤过论证复算：F_k/F_{k−1} 权 2k−n，逐项给出 O(2k−n)，与 (41) 右侧对上 |
| 10 | t=v/u 还是 t=u/v | 本文 p006 写 Q=uQ_l+vQ_r、t=v/u；库内 ggl20/concept/gl-twist-family 写 t=u/v | 判为文献间约定差，不记 errata；卡片引用本文时按 v/u，并在 notes 4.1 第 5 项写明两种参数化的差别 | 对照两处原文措辞与 ggl20 卡的 t=i↔t=1 说法，确认只是取倒数后的重命名 |
| 11 | audit_locators 会不会误报 | 脚本只查 `(x.y)` 形式的式号，本篇是 (1)–(81) 单调编号 | locator 统一写 `A p.33 eq (40)`（式号无小数点），审计按设计跳过；既满足「式号真在标注页」的人工要求，也不触发误报 | 跑 `python audit_locators.py out/15_ggl15 15 56`（审计脚本在库外工具目录）得 OK；另用 grep 核对 (40) 确在 p033、eq (43) 确在 p037 |
| 12 | 页数 55 还是 56 | arXiv 评论写 "55 pages"；META 与本库 PDF 都是 56 页 | 本库 PDF 多一页封面（p001 为标题+摘要），正文仍 55 页；--max-pages 用 56，卡片页码上限也用 56 | `pdfinfo` 与 META.json 均为 56；p056 只剩参考文献尾部，无第 56 页正文 |

弯路说明（写错—发现—改正，均真实发生）：

- 第 3 条：三张推导卡先写成 `type: "deriv"`，lint 直接报错；改 `derivation` 后通过。
- 第 4 条：minuscule 卡的引文含 `hyperkähler`，verify_pages 报搜不到；换成不含变音符的句子后通过。
- 第 5 条：errata.tsv 先写数据行、覆盖了表头；lint 报缺表头后补回。
- 第 6 条：别名撞名改了一轮后仍剩两处，第二轮才清零。
