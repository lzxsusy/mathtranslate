# references.bib 校对日志（rv-ch03b / task-11）

校对对象：`<本地路径>`（476 条，`@misc{refNNN,` + `sortkey` + `note`）
对照源：`<本地路径>`（Clay 原书 PDF 665–685 抽取，476 条，`=== [N] ===`）
日期：2025-11-14

## 一、方法

1. 用临时 python 脚本逐条解析 476 个 `note` 与 476 段 `[N]` 原文，做归一化比对：剥掉 `$...$` 包装、LaTeX 宏（`\sigma`→sigma 等）、NFC/组合重音差异、连字符与空格、大小写与标点，仅比较字母数字序列 → 首轮 174 条"差异"经人工判读后，真差异只剩个位数。
2. 另做数值与结构检查：页码区间是否倒置（末页 < 首页）、期号区间是否被并成两位数（如 `(3-4)`→`(34)`）、花括号/引号配对、`sortkey` 与编号一致性、编号连续性、每条 note 是否完整结尾。
3. 疑点逐条人工复核，必要时用 Crossref API 核实（[375]、[449]）。
4. 只改 `note` 文本内容；**未**改键名、字段结构、`sortkey`，**未**回退 Lead 已做的排版字符（ASCII `'`、`--`/`---`、prime、NFC、`$...$`）。

## 二、已核对范围（476/476 全部逐条比对，按 50 条一段）

| 段 | 编号范围 | 结果 |
|---|---|---|
| 1 | [1]–[50] | 已核对，改动 6 处：[7][11][13][21][25][44] |
| 2 | [51]–[100] | 已核对，改动 1 处：[70] |
| 3 | [101]–[150] | 已核对，改动 1 处：[142] |
| 4 | [151]–[200] | 已核对，改动 5 处：[159][161][169][171][197] |
| 5 | [201]–[250] | 已核对，改动 3 处：[209][213][249] |
| 6 | [251]–[300] | 已核对，无改动 |
| 7 | [301]–[350] | 已核对，无改动 |
| 8 | [351]–[400] | 已核对，改动 1 处：[375] |
| 9 | [401]–[450] | 已核对，改动 1 处：[449] |
| 10 | [451]–[476] | 已核对，无改动 |

合计 18 条改动（19 个字符级修正，[13] 两处）。

## 三、改动表

| 编号 | 字段 | bib 原文（或原值） | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|
| [7] | note | `Selecta Math. (N.S.), 12(34):307--377` | `12(3--4):307--377` | 期号错 | 原文跨行作 `12(3- 4)`，转换时连字符丢失被并成 `34` |
| [11] | note | `higher genus riemann surfaces` | `higher genus Riemann surfaces` | 专名大小写 | 论文标题专名 Riemann 应大写（原抽取文本亦作小写） |
| [13] | note | `The L2 structure ... on 4manifolds.` | `The $L^2$ structure ... on 4-manifolds.` | 字符损坏/数学 | 原文 `L2`、`4- manifolds`（连字符在行末被吞）；按 Lead 要求统一为 `$L^2$`，并补连字符 |
| [21] | note | `Massless D-branes on CalabiYau threefolds` | `Calabi-Yau threefolds` | 字符损坏 | 原文 `Calabi- Yau`，连字符丢失 |
| [25] | note | `AddisonWesley Publishing Co.` | `Addison-Wesley Publishing Co.` | 字符损坏 | 原文 `Addison- Wesley`，连字符丢失 |
| [44] | note | `]. SpringerVerlag, Berlin, 1987` | `Springer-Verlag, Berlin, 1987` | 字符损坏 | 原文 `Springer- Verlag`，连字符丢失 |
| [70] | note | `LandauGinzburg realization of open string TFT` | `Landau-Ginzburg realization ...` | 字符损坏 | 原文 `Landau- Ginzburg`，连字符丢失 |
| [142] | note | `Finite-dimensional algebras. SpringerVerlag, Berlin, 1994` | `Springer-Verlag, Berlin, 1994` | 字符损坏 | 原文 `Springer- Verlag`，连字符丢失 |
| [159] | note | `North-holland ( 1984)` | `North-Holland (1984)` | 专名/标点 | 出版者 North-Holland 大小写错误，且 `( 1984)` 多出空格 |
| [161] | note | `KramersWannier duality` | `Kramers-Wannier duality` | 字符损坏 | 原文 `Kramers- Wannier`，连字符丢失 |
| [169] | note | `Phys. Lett. B, 410(24):151--159` | `410(2--4):151--159` | 期号错 | 原文跨行作 `410(2- 4)`，连字符丢失被并成 `24` |
| [171] | note | `HyperKähler manifolds and multiply intersecting branes` | `Hyper-Kähler manifolds ...` | 字符损坏 | 原文 `Hyper- Kähler`，连字符丢失 |
| [197] | note | `WileyInterscience [John Wiley & Sons]` | `Wiley-Interscience [...]` | 字符损坏 | 原文 `Wiley- Interscience`，连字符丢失 |
| [209] | note | `for a class of CalabiYau threefolds` | `Calabi-Yau threefolds` | 字符损坏 | 原文 `Calabi- Yau`，连字符丢失 |
| [213] | note | `homogeneous MongeAmpère equation` | `homogeneous Monge-Ampère equation` | 字符损坏 | 原文 `Monge- Ampère`，连字符丢失 |
| [249] | note | `Universitext. SpringerVerlag, Berlin, 2005` | `Springer-Verlag, Berlin, 2005` | 字符损坏 | 原文 `Springer- Verlag`，连字符丢失 |
| [375] | note | `Cihan Sacliog̃lu` | `Cihan Saçlıoğlu` | 专名/字符损坏 | `g` 上误挂组合波浪号；Crossref（10.1103/PhysRevD.53.2240）作者姓名为 Saçlıoğlu |
| [449] | note | `Commun. Math. Phys., 126:325--246, 1989` | `126:325--346, 1989` | 页码错（倒置/截断） | 末页 246 < 首页 325；Crossref（10.1007/BF02125128）为 126:325-346 |

## 四、已核查但未改动的疑点（说明而非待办）

1. **数学记号未统一改排**：`N = 1`、`G2`、`S 1 -actions`、`A∞`（未被 Lead 转写的部分）等仍按抽取文本原样保留——属排版级改写，按要求不动。如需全书统一，可另行批量处理。
2. **[17]**：原抽取文本末尾多出 `655`（页眉/页脚残留），bib 中无此串，正确，无需改。
3. **[160]/[165]/[230]/[279]/[396]**：归一化比对显示的差异全部是 `$...$` 与 Unicode 希腊字母（`ε` vs `\varepsilon`、`∞` vs `\infty`）的等价写法，非错误。
4. **[472]** `pages Vol 2; pp. 1119--1424` 等奇怪写法来自原书抽取，未动。
5. 多数 `Springer-Verlag`/`North-Holland` 以外的出版社名（如 `Birkhäuser Boston`）已正确，未改。

## 五、结论

- 476 条全部逐条核对；共修正 **18 条**（**19 处**字符级改动）：页码错 1（[449]）、期号错 2（[7][169]）、连字符丢失 12（[13][21][25][44][70][142][161][171][197][209][213][249]）、专名/标点 3（[11][159][375]）、数学记号 1（[13] 的 `L2`→`$L^2$`，与上条同一条目）。
- 结构校验：476 条、键唯一、编号连续、`sortkey` 与编号一一对应、花括号净差 0、每条 note 完整结尾、无残留损坏串。
- 未完成项：无。
