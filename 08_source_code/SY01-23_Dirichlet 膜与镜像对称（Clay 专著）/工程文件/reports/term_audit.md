# 术语与记号一致性审计（只读）

- 审计人：rv-preface-ch01
- 任务：team task-13（只读审计，未修改任何 .tex）
- 审计时点：2026-11-14 12:3x（**审计期间有其他同事在改 ch05b 等文件，行号会随编辑漂移**）
- 范围：`chapters/preface.tex`、`chapters/ch01–ch08`（含 `ch08-sec82/83/84head/84tail/85`）、`references.bib`（figures/ 未读）
- **重要结构事实**：`main.tex:16,18` 编译的是 `chapters/ch03.tex` 与 `chapters/ch05.tex`，而这两个文件是 `ch03a.tex+ch03b.tex`、`ch05a.tex+ch05b.tex` 的**逐字节拼接副本**（166657+149578=316235；177899+167855=345754）。同一段文字在两个文件里各存一份，**任何修改都要改两处**，行号不同（合并文件行号 = 拆分文件行号 + 前一部分行数）。下表同时给出两种行号。

---

## A. 术语多译

### A1. quintic：三种译法并存（本轮最重要的一条）

| 问题类型 | 文件:行号 | 当前写法 | 建议统一写法 | 出现次数 |
|---|---|---|---|---|
| 术语多译（quintic threefold） | `chapters/ch05.tex:2850`、`ch05b.tex:631` | 五次三维流形（§5.5.6 标题） | 五次三维流形 | 18（ch05 9 + ch05b 9） |
| 同上 | `chapters/ch05.tex:2853`、`ch05b.tex:634` | 五次三维流形 | 五次三维流形 | |
| 同上 | `chapters/ch05.tex:2885`、`ch05b.tex:666` | 五次三维流形（§5.5.6.1 标题） | 五次三维流形 | |
| 同上 | `chapters/ch05.tex:2893`、`ch05b.tex:674` | 五次三维流形 | 五次三维流形 | |
| 同上 | `chapters/ch05.tex:2928`、`ch05b.tex:709` | 镜像五次三维流形 | 五次三维流形 | |
| 同上 | `chapters/ch05.tex:3374`、`ch05b.tex:1155` | 五次三维流形 | 五次三维流形 | |
| 同上 | `chapters/ch05.tex:3379`、`ch05b.tex:1160` | 五次三维流形 | 五次三维流形 | |
| 同上 | `chapters/ch05.tex:3493`、`ch05b.tex:1274` | 五次三维流形 | 五次三维流形 | |
| 同上 | `chapters/ch05.tex:4097`、`ch05b.tex:1878` | 五次三维流形 | 五次三维流形 | |
| **误译/术语（quintic threefold 译成"五次三维超曲面"）** | `chapters/ch03.tex:2694`、`ch03b.tex:416` | 取 $Y$ 为"五次三维超曲面" | 五次三维流形（原文 p179-188:422 "We take Y to be the 'quintic threefold'"） | 5 |
| 同上 | `chapters/ch04.tex:37` | 在五次三维超曲面上固定一组 Chern 类 | 五次三维流形（原文 p227-236:167 "take a quintic threefold"） | |
| 同上 | `chapters/ch06.tex:3629`（同句 2 处） | 同胚于镜像五次三维超曲面…同胚于五次三维超曲面 | 五次三维流形（原文 p501-510:667-668 "homeomorphic to the mirror quintic … to the quintic"） | |
| 术语多译（quintic / quintic hypersurface） | `chapters/ch01.tex:532`（2 处）、`ch01.tex:541` | 五次超曲面 | 五次三维流形（原文 p031-036:331,336,385 只说 "the quintic"） | 18 |
| 同上 | `chapters/ch03.tex:2459`、`ch03b.tex:181` | Fermat 五次超曲面 | 保留（原文 p169-178:806 "the Fermat quintic"） | |
| 同上 | `chapters/ch03.tex:2465`、`ch03b.tex:187` | Fermat 五次超曲面 | 保留 | |
| 同上 | `chapters/ch03.tex:2694`、`ch03b.tex:416` | 在五次超曲面这一语境中 | 保留（同页，指 P⁴ 中的超曲面） | |
| 同上 | `chapters/ch03.tex:2714`、`ch03b.tex:436` | 镜像五次超曲面 | 建议 镜像五次三维流形 | |
| 同上 | `chapters/ch03.tex:3935`、`ch03b.tex:1657` | 五次超曲面的语境中 | 保留 | |
| 同上 | `chapters/ch05.tex:160`、`ch05a.tex:160` | Fermat 五次超曲面 | 保留（原文即 "Fermat quintic" 的超曲面描述） | |
| 同上 | `chapters/ch05.tex:2856`、`ch05b.tex:637` | $\mathbb{P}^4$ 中的五次超曲面 | 保留（原文 p383-392:290 "X be a quintic hypersurface in P⁴"） | |
| 同上 | `chapters/ch07.tex:466` | 包括五次超曲面中 | 建议 五次三维流形 | |

**建议统一为**：`quintic threefold`／"the quintic"（指整族 CY 三维流形）→ **五次三维流形**；只有原文明确说 quintic hypersurface、或在描述"P⁴ 中由五次多项式定义的超曲面"时，才用 **五次超曲面**。当前 5 处"五次三维超曲面"属混合造词，应全改为"五次三维流形"。

> 附注：`五次曲面` 在审计开始时出现 6 处（`ch05b.tex:631,666,674,709,1160,1274`），**审计过程中已被其他同事改为"五次三维流形"**（现在全书 0 处）——说明这条正是本轮校对的实际战场，请 Lead 核对该批修改是否已同步到 `ch05.tex`（已同步，见上表）。

### A2. unimodular → 幺模（一致，无需改）

| 文件:行号 | 当前写法 | 出现次数 |
|---|---|---|
| `chapters/ch02.tex:814` | 幺模格 $\mathcal{L}_B$ | 11（ch02 1 + ch05 5 + ch05a 1 + ch05b 4） |
| `chapters/ch05.tex:176`、`ch05a.tex:176` | 模去挠子群后的相交格幺模 | |
| `chapters/ch05.tex:3787`、`ch05b.tex:1568`（3 处） | 偶幺模格…代数子格一般不幺模 | |
| `chapters/ch05.tex:3819` | Mukai 配对为幺模的 | |

`非退化` 38 处（ch01:1、ch02:20、ch03+ch03b 各 4、ch05 3、ch05a 1、ch05b 2、ch06:1、ch08-sec83:2）经抽查全部对应 non-degenerate，**未发现把 unimodular 误译为"非退化"**。建议统一写法：**幺模**。无需改动。

### A3. equivariant / gauged → 等变 / 规范化理论（一致，无需改）

| 文件:行号 | 当前写法 | 英文 | 出现次数 |
|---|---|---|---|
| `chapters/ch02.tex:45` | 从规范化理论得到的"轨形"理论 | gauged theory | 规范化理论 3（ch02:45,1099,1226） |
| `chapters/ch02.tex:1099` | 必须区分等变理论与…"规范化理论"…通过对这些规范场"求和"得到 | 'G-equivariant' or 'G-gauged' TFTs（ch02 chunk p037-046:102） | 等变 124（含"等变凝聚层/等变导出范畴"） |
| `chapters/ch02.tex:1226` | 规范化理论通过对规范场求和，从等变理论得到 | gauged theory（ch02 chunk p078-088:112-114） | 规范场 = gauge field |

**建议统一为**：equivariant→**等变**、gauged theory→**规范化理论**、gauge field→**规范场**（现状即如此）。

### A4. divide (out) by the group action → 除去 / 取商 / 模去

| 问题类型 | 文件:行号 | 当前写法 | 建议统一写法 | 出现次数 |
|---|---|---|---|---|
| 同义多译 | `chapters/ch01.tex:66` | 对一个全纯等距变换取商 | 取商 | 取商 16 |
| 同上 | `chapters/ch03.tex:880`、`ch03a.tex` | 先不再对零范数后裔取商 | 取商 | |
| 同上 | `chapters/ch03.tex:1081`、`ch03a.tex` | 并对上述关系取商 | 取商 | |
| 同上 | `chapters/ch03.tex:1462`、`ch03a.tex` | 对 $O(d)\times O(d)$ 取商 | 取商 | |
| 同上 | `chapters/ch02.tex:423` | 模去在边界圆周上为恒等映射的…微分同胚 | 模去 | 模去 43（ch06 17、ch05 8、ch05a 7 等） |
| 同上 | `chapters/ch02.tex:469` | 共形结构模去…微分同胚所得的模空间 | 模去 | |
| 同上 | `chapters/ch05.tex:1639`、`ch05b.tex:1639` | $\operatorname{Hom}_{\mathbb Z}$…（配额） | — | 除去 30 |

`除去` 的 30 处经逐条看：绝大多数是 "remove / up to / except"（ch01:440 除去真空能量平移、ch03:640 除去碰撞对角线、ch05:711 除去整体归一化因子、ch05:4091 未除去 $\mathbb{C}$ 的整体作用、ch07:498 除去 Hausdorff 余维二集合），**属正当译法，不要动**。
**建议统一为**：对群作用/等价关系取商 → **模去**（ch02 的 "mod out by the diffeomorphisms" 即此义）；"取商"只用于名词化场合（"取商所得的空间"）。建议把 `ch01.tex:66`、`ch03.tex:880/1081/1462`（及 ch03a 对应行）的"取商"统一为"模去/模"。

### A5. stack → 模堆（一致）

`模堆` 8 处：`chapters/ch05.tex:3759,4161,4203,4288`、`ch05b.tex:1540,1942` 等；全书 **0 处"栈"**。建议统一为**模堆**（现状）。

### A6. gerbe → 保留英文（一致）

6 处（ch03/ch03b 各 3）：`chapters/ch03.tex:3055,3079,3779` / `ch03b.tex:777,801,1501`，均作"gerbe"。建议统一：**保留 gerbe 不译**（现状；若译者愿意可加"（格贝）"首现注，但 GUIDE 不允许加注，故维持）。

### A7. coherent sheaf → 凝聚层（一致）

`凝聚层` 175 处；`相干层`/`连贯层`/`一致层` 均 0 处。建议统一为**凝聚层**（现状）。

### A8. stability condition → 稳定性条件（一致）

`稳定性条件` 141 处（ch05 64、ch05b 52、ch05a 12、ch01 7、ch03/ch03b 各 2、ch04 1、ch07 1）；`稳定条件` 0 处。建议统一为**稳定性条件**（现状）。

### A9. brane → 膜（一致）

`brane` 仅在术语首现处保留：`chapters/ch01.tex:111`（"这些解称为 brane，是 membrane 的简称，中文称为'膜'"）、`ch03.tex:2860`/`ch03b.tex:582`（`\label{def:3.dirichlet-p-brane}`）。其余全书作"膜 / D 膜 / B 膜 / A 膜"。一致。

### A10. family → 族（一致）

`家族` 0 处；"族" 用于 family（如"4 膜族"）。一致。

### A11. 迹：tr / Tr 混用（建议统一）

| 问题类型 | 文件:行号 | 当前写法 | 建议统一写法 | 出现次数 |
|---|---|---|---|---|
| 大小写不一致 | `chapters/ch02.tex:529`（3 处）、`ch05.tex:…`、`ch05a.tex:…` | `\operatorname{tr}` | 视原文：矩阵迹用 tr，算子迹用 Tr（**需逐处对原文**） | tr 19 |
| 同上 | `chapters/ch02.tex:563,566,592,598,900,903` 等 | `\operatorname{Tr}` | 同上 | Tr 61 |
| 误判排除 | `chapters/ch08-sec83.tex:193,195,196,221,223` | `\mathrm{tr}` | **不是迹**，是对象下标 $\mathrm{Ob}_{\mathrm{tr}}$，**不要改** | 5 |

**建议**：先确认原书 ch02 用 "tr" 还是 "Tr"（英文原书两章不同），再按章统一；不建议盲目全局替换。

---

## B. 记号 / 字体

### B1. P¹ 的三种写法（同一对象）

| 文件:行号 | 当前写法 | 出现次数 |
|---|---|---|
| `chapters/ch07.tex` 48 处、`ch02.tex` 2、`ch03.tex`+`ch03b.tex` 各 2、`ch05.tex`+`ch05a.tex` 各 2 | `\mathbb{CP}^1` | 58 |
| `chapters/ch04.tex:…` 2、`ch05.tex`/`ch05b.tex` 各 11 | `\mathbb{P}^1` | 24 |
| `chapters/ch07.tex:106`（唯一一处！同章其余 48 处都写 `\mathbb{CP}^1`）、`ch08-sec82.tex:323,326,352` 等 36 处、`ch08-sec84head.tex:53,85,129` | `\mathbb P^1` | 40 |

**建议统一为**：`\mathbb{P}^1`（全书射影空间统一用 P 记号）；至少 `chapters/ch07.tex:106` 与同章 48 处必须一致。注意 `\mathbb{CP}^1` 还散在 ch02/ch03/ch05，属全章级选择，需 Lead 拍板是否统一。

### B2. 数学字体：带括号 / 不带括号两种风格按章分裂

| 写法 | 计数 | 分布 |
|---|---|---|
| `\mathbb{Z}`（带括号） | 240 | ch01 11、ch02 28、ch03 50、ch03a 39、ch03b 11、ch04 25、ch05 38、ch05a 26、ch05b 12 |
| `\mathbb Z`（不带括号） | 392 | **ch05 5**、**ch05b 5**、ch06 228、ch07 35、ch08-sec83 18、ch08-sec84head 61、ch08-sec84tail 37、ch08 3 |
| `\mathrm{i}` | 381 | ch02–ch05b（ch03 105、ch05 83、ch05b 59…） |
| `\mathrm i` | 313 | **ch06 176、ch07 126**、ch08-sec83 8、ch08-sec84head 3 |
| `\mathrm{d}` | 494 | ch02–ch05b |
| `\mathrm d` | 199 | **ch06 148、ch07 51** |
| `\mathcal{O}` | 826 | ch01–ch05b |
| `\mathcal O` | 59 | ch06 1、ch07 4、ch08-sec82 43、ch08-sec84head 10、ch08-sec84tail 1 |

**结论**：不是随机混乱，而是 **ch02–ch05b 用带括号、ch06–ch08 不带括号** 的两套风格；违反者是 `chapters/ch05.tex:3666,3721,3723,3797,3858` 与 `ch05b.tex:1447,1502,1504,1578,1639` 这 10 处 `\mathbb Z`（其余同章都带括号）。
**建议统一为**：`\mathbb{Z}`、`\mathrm{i}`、`\mathrm{d}`、`\mathcal{O}`（带括号，全书多数派且与 ch02–ch05 一致）；若决定反向统一，则需改 240+381+494+826 ≈ 1900 处，工作量大，建议只修 ch05/ch05b 的 10 处 `\mathbb Z` 泄漏，其余留待通稿时统一。

### B3. 算子名：`\operatorname` vs `\mathrm` vs 裸写

| 问题类型 | 文件:行号 | 当前写法 | 建议统一写法 | 出现次数 |
|---|---|---|---|---|
| 字体不一致 | `chapters/ch01.tex:175` | `\mathrm{id}_N` | `\operatorname{id}` | 1（用 `\operatorname{id}` 31 处） |
| 潜在误判（勿改） | `chapters/ch07.tex:1174,1178,1202,1248,1251,1259,1261,1265,1277` | `\mathcal M_{\mathrm{SL}}` | **保留**（特殊 Lagrange 模空间的下标，不是群 SL） | 9 |
| 层版 Hom 与函子版 Hom 混用 | `chapters/ch08-sec82.tex:11,13,14,19,21,29,34,73,76,337,338,340,342,344,346` | `\mathcal Hom`（无括号） | `\mathcal{H}om`（层版）/ `\operatorname{Hom}`（函子版） | 15（`\operatorname{Hom}` 449 处） |
| 行内裸写群名 | `chapters/ch03.tex:2574,2662,3422` / `ch03b.tex:296,384,1144` | `$SU(3)$` | `\operatorname{SU}(3)` | 13（含合并副本） |
| 同上 | `chapters/ch03.tex:1549` / `ch03a.tex:1549` | `$SO(2)$` | `\operatorname{SO}(2)` | |
| 同上 | `chapters/ch04.tex:2448` | `$SU(2)\to SO(3)$` | `\operatorname{SU}(2)\to\operatorname{SO}(3)` | |
| 同上 | `chapters/ch05.tex:203,2053` / `ch05a.tex:203,2053` | `$SU(3)$`、`$SU(n)$` | `\operatorname{SU}(3)`、`\operatorname{SU}(n)` | |

### B4. C\* 的两种写法

| 文件:行号 | 当前写法 | 出现次数 |
|---|---|---|
| `chapters/ch03.tex:+`、`ch04.tex`、`ch05.tex`、`ch05a.tex`、`ch05b.tex` | `\mathbb{C}^\times` | 26 |
| `chapters/ch02.tex`（1 处） | `\mathbb C^\times` | 1 |
| `chapters/ch06.tex:2104,2113,…`（41 处） | `\mathbb C^\times` | 41 |

**建议统一为**：`\mathbb{C}^\times`（不用 `\mathbb{C}^*`；若与原书 `C^*` 对齐则反向统一，需 Lead 拍板）。附带 B2 的括号问题。

### B5. `\BookRef` 显示格式

| 问题类型 | 文件:行号 | 当前写法 | 建议统一写法 | 出现次数 |
|---|---|---|---|---|
| 图号空格不一致 | `chapters/ch08-sec82.tex:141,195,214`（2 处）、`301,392`；`ch08-sec83.tex:100,273,318,376,431,507`（2 处）、`510,514,523,537` | `图 10`、`图 11`…（图号前有空格） | `图10`（与全书 187 处一致） | 17 |
| 定理类编号前空格 | `chapters/ch03.tex:3145`/`ch03b.tex:867`（例题 5.21）、`ch08-sec83.tex:507`（例题 2.3）、`ch07.tex:279,283,565,603,624,627,636,655,690,862,905,913,921,974,1004,1015,1024,1027,1042,1202,1220,1275,1297,1389,1397,1400,1415,1418,1424,1453,1504,1691,1765,1772,1810,1876,1900,2026,2063` | `例题 7.8`、`定理 7.12`、`定义 7.13`、`命题 7.6`、`引理 7.26`、`构造 6.86`、`猜想 7.32`、`笔记 7.23`、`问题 7.25` | `例题7.8`、`定理7.12`…（无空格，与全书 254 处一致） | 47（例题 21、定理 7、构造 5、命题 5、定义 4、引理 2、问题 1、笔记 1、猜想 1） |

说明：`\BookRef` 的显示串是该宏的第二个参数，格式不影响编译，但会直接印在 PDF 上；ch07 与 ch08-sec82/83 是唯一两处"带空格"的区段，建议按多数派改。

---

## C. 中英混排

| 检查项 | 结果 | 说明 |
|---|---|---|
| 中文后接半角 `,` `;` `?` `!` | **0 处** | 全部使用全角，合格 |
| 中文句内半角双引号 `"` | **0 处**（163 个 `"` 全是 `K\"ahler` 之类变音符） | 引号统一 `“”`（812 个左引号） |
| 中文之间用 `--` 当破折号 | **0 处** | 合格 |
| `---` | **0 处** | 合格 |
| `——`（正确破折号） | 26 处：ch05 10、ch05a 8、ch05b 2、ch08-sec83 6 | 合格 |
| `--`（连字符/英文人名） | 806 处，均用于 Calabi--Yau、Mukherji--… 等 | 合格 |
| 数字与量词空格 | 少数不一致：`ch07.tex:473,477,1446,2000`、`ch08-sec85.tex:44`（2 处）、`47`（3 处）作"27 个/16 个/64 个/955 页"；`ch03.tex:…`、`ch03b.tex:…`、`ch05.tex:…`、`ch05a.tex:…`、`ch06.tex:…` 共 9 处作"N个"（无空格） | 建议统一"数字 空格 量词"（与 ch07 一致），或反向统一下沉；属 P3 风格问题 |
| `??`/未解析引用 | 未发现 | — |

---

## D. 附：本次审计的方法与可复现性

- 对 `chapters/*.tex` 与 `review/chunks/**/*.txt` 做正则统计（计数 + 行号），脚本在临时目录，未写入项目；**未修改任何 .tex，未编译，未读 figures/**。
- 行号以审计时点的文件内容为准；`ch03.tex`/`ch05.tex` 与拆分文件重复，修一处必须修两处。
- 审计期间 `ch05b.tex` 被他人修改（五次曲面→五次三维流形），说明并发编辑存在，**正式改稿前需重新 grep 一遍行号**。
