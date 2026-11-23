# 块 B · 译手决策记录（trace-chI-b）

四栏：判断点 / 依据 / 结论与理由 / 事后确认。记号：`A:` 有原文或工程依据，`B:` 有外部文献依据，`I:` 译者推理，`J:` 译者判断。范围 §I.5–§I.9（p.23–36），产出 `源码/sections/s02-chI-2.tex`。

## 一、结构与编译

| 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- |
| 节边界收到 p.36 还是 p.38 | 原页 p.34 是 §I.9 开头、p.36 末段收在定理 I.9.6 的说明句；p.37 起是 §I.10 | 收到 **p.36**。§I.10 按节归块 C，若我译到 p.38 会造成两文件争同一个 `\section` 与计数器 | A: `01_pages/p036.txt` 末行 “semisimple L-parameter”，p.37 首行 “I.10. The spectral action” |
| 本文件是否写 `\chapter` | SPEC「sections 只写 `\section`」 | 不写。单文件 `_check_b` 的节号为 0.1–0.5，成书由 main 的 `\chapter` 统一为 1.5–1.9 | A: `_check_b.pdf` 14 页，页眉 “0.5 L-参数的构造” |
| 定理类环境编号怎么显示原文号 | preamble 把可选参数作括注追加在自动编号后 | 照 TASK 用 `\begin{theorem}[I.6.3]`，显示「定理 0.5.6 (I.9.6)」；成书为「1.9.6 (I.9.6)」。若 Lead 要只显示原文号需改 preamble，我未动 | A: 渲染页 `_chk13/_chk14`；报告 §6 第 3 条 |
| 作者脚注（p.36 第 5 号）用 `\footnote` | TASK「作者脚注用 `\footnote` 保留原序号」 | 用 `\footnote`；但译注共用计数器，实际序号≠5，无法自动保留原文号 | A: `_chk13` 脚注 10；报告 §7 第 4 条给 `\footnotetext[5]` 备选 |

## 二、**真实弯路**（走过又退回）

| 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- |
| ① 编译命令用反斜杠还是正斜杠 | TASK 与 SPEC 都写 `build.bat check sections\s02-chI-2.tex b` | 先按文档用反斜杠 → `! Missing endcsname inserted.`＋`! Undefined control sequence.<argument> "sectionss 02-chI-2.tex"`。查 `build.bat` 发现它写 `\input{"%~2"}`，引号内的 `\s` 被当控制序列。**改用正斜杠** `sections/s02-chI-2.tex` 即 `[OK]`；未改 build.bat，缺陷写进报告 §7 第 3 条 | A: 反斜杠日志 l.4 报错原文；正斜杠连跑 12 轮全 `[OK]` |
| ② `i_b^*` 还是 `i^{b*}` | 原页 p.24、p.25 各一处 | 动笔时按习惯“纠正”成 `i_b^*`；核对 p.24 渲染图发现书上是 `i^{b*}A`。**改回** `i^{b*}` 并全书统一（含定理 I.5.1(iii)(v)） | A: p.24、p.25 两页目视；编译后 `_chk2` 显示 $i^{b*}A$ |
| ③ 局部 Hecke 叠用 `\Hck` 还是 `\mathcal{H}\mathrm{ck}` | symbols.tsv 只给 `\Hck`；原页 p.26 排作 script H + roman ck，p.30 图表左端却是 roman Hck | 先按 symbols 全用 `\Hck`；对 p.26 做 400dpi 裁图后发现局部叠是 $\mathcal{H}\mathrm{ck}$、p.30 图里两者并置（左 roman=全局、右 script=局部）。**新增 `\fsHck` 表局部并把 §I.6 全部替换**，`\Hck` 只留给全局 | A: `_c26.png`、`_c30a.png` 两张裁图对比；`_chk7` 中原图五处 $\mathcal{H}\mathrm{ck}^I_G$ |
| ④ tikzcd 三点图用 `\arrow[ddl]` | 首版按 3 行 3 列设想写 `ddl/ddr` | 编译报 `! Package pgf Error: No shape named `tikz@f@5-3-0' is known.`——矩阵未声明到 3 行，`ddl` 指向不存在的格。**改成 2 行 3 列**（(1,2)=\Hck、(1,3)=$\mathcal{H}$ck、(2,1)=Bun、(2,3)=Bun×(Div¹)）并显式写 `&` 占位 | A: 错误原文；`_chk1` 第 1 页图正确 |
| ⑤ 用 `python -c` 批量改公式 | 想省事 | 多重转义把 `$\ell$` 变成 `\ellhBcpower`、把 `”` 变成 `$`，报 `! Undefined control sequence.<recently read> \ellhBcpower`。**改为先 `write` 脚本到 /tmp/fixN.py 再执行**，并把替换写成 `assert old in s` 防静默失败 | A: 两次坏结果与修复后 diff；后续 5 次批量修全部一次通过 |

## 三、术语与记号

| 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- |
| `dim.\ trg` 译不译 | 原书 p.23/p.25/p.29/p.31 同用；glossary 无 | **不译**，按原样排 `dim.\ trg`（点号保留），加 `\yizhu` 说明是 [Sch17a] 的维数概念 | A: 400dpi 裁图确认是 “dim. trg” 而非 “dim.trg”；报告 §6 第 1 条 |
| 「solid」取「固体」 | glossary 第 148 行附近、裁定第 25 行 | 取**固体**（固体模、固体层），加一次译注引 Clausen–Scholze；不写「固态」 | A: 裁定即冻结；全文 6 处「固体」，无「固态」 |
| $\Lambda$-平坦的说法 | 原文 “flat over $\Lambda$ (i.e., for all $\Lambda$-modules $M$, also $A\otimes^L_\Lambda M$ is perverse)” | 定义 I.6.2 照译，另加译注把「逐 $M$ 张量仍反常」写成显式条件（原文用 i.e. 已给，注只理顺语序） | A: p.27 原文；`_chk7` 定义块 |
| `\mathbb{D}_{\mathrm{BZ}}` 的下标 | p.24 印 `D_BZ`（黑体 D，下标 BZ） | 用 `\fsBZ=D_{\mathrm{BZ}}`，与 $\fsblk$（黑方块，用于 $D_\blacksquare$）区分：后者是固体复形范畴，前者是 BZ 对偶函子 | A: p.24 两处目视；`_chk2` 显示 $D_{\mathrm{BZ}}$ |
| 「congredients」（定理 I.9.6(iv)） | glossary、疑点清单均无；疑为 [AV16] 术语 | **保留英文**并用 `\yizhuw`（无外部依据）标注，不臆造译名 | A: p.36 原文；报告 §6 第 2 条 |

| 页锚点 `\srcpage` 放哪 | Lead 新规：必须段首，否则 `\marginpar` 静默不印；preamble 已改 marginnote 并新增 `\srcpageinl` | 首版 14 个全按「页界处」内联，用 check_pagemarks 查出一半没印出。处理：页界正好在段首且能印的用 `\srcpage`（5 处），**页界落在句中**或**段首被吞**的用 `\srcpageinl`（9 处）；p.23/26/28/34 先试着挪到段首仍不印（23 在文首、26/34 紧贴 `\section`、28 在显示式后），最终改用行内锚点 | A: `[ok] 14 个锚点全部在 PDF 中可见`、`[ok] p.23–p.36 锚点齐全`；`--end 38` 报缺 37/38（属 C 块） |

## 四、跳步补注的取舍

| 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- |
| 「当 $\Lambda$ 是 $\ell$-幂挠时容易」要不要补证 | p.25 原文 “Parts (i) and (ii) are easy when Λ is ℓ-power torsion” | 补。注文给两条：切除三角形把 $D(\Bun_G,\Lambda)$ 拼起来；[Sch17a] 六函子在挠系数下已够用 | A: p.25 原句；`_chk2` 注 3 |
| 「本质上是形式推论」补到多细 | p.25 原文 “Finally, part (v) is essentially a formal consequence” | 补到「左伴随保紧 + 容许性定义 + Verdier 对偶保持 ULA」三步为止，不展开 Ch V 的证明 | A: p.25 原句；报告 §4 第 5 条 |
| 「证明出奇地形式化」只补归约不补归纳 | p.31 原文 “The proof is surprisingly formal: One reduces to I={*} by an inductive argument” | 只补「$\Div^1=\Spd\dot E/\varphi^\ZZ$ 仍只是一个点，故 $D(\Bun_G)\to D(\Bun_G\times\Spd\dot E)$ 是等价」这一步；归纳细节原文未写，疑点清单已标待核，注里明说「原文未写出」 | A: p.31 原句；报告 §6 第 4 条 |
| 「etc. .」算不算笔误 | p.29 末行 “commutes with any base change, etc. .” | 判**笔误**（多一个句点），译「等等」并加注说明原写法，不静默吞掉 | A: p.29 目视；报告 §4 第 9 条 |
| p.32 显示式括号错位 | p.32 首式 `D([*/G_b(E)])\times\prod…,\Lambda)` 右括号在 `\Lambda` 前 | 判**疑似排版错位**，按文意订正为 $D([*/G_b(E)]\times\prod_i\Spd\dot E_i,\Lambda)$ 并加注（不改原文其他符号） | A: p.32 第 3–4 行 400dpi 裁图 |
