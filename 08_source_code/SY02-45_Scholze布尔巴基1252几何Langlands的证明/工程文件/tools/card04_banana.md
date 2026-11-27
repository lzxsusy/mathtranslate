## 四、与香蕉空间（bananaspace.org）通行译名的增量与分歧

**方法**：按 SY02-45 任务书要求，本轮**不重新联网核**，直接继承 `SY02-41_局部Langlands几何化Berkeley讲义/工程文件/work/术语外部核对_香蕉空间.md` 的 15 词对照表与「无专条」清单（该文件第一节记录了可复核的取证方式：MediaWiki API + 过 Cloudflare 验证后读 wikitext），增量 19 条在该文件第六节「六、SY02-45 增量词表」。本卡不复述取证过程，只列裁定结果。

### 4.1 已知 6 条实质分歧（本文一律从本库）

| 词 | 本库冻结（本文采用） | 香蕉空间 | 本文出现处 |
| --- | --- | --- | --- |
| shtuka / leg | 保留英文 | 块 / 爪 | §5 定义 5.5（p29）、注 5.4（p29） |
| perfectoid | 完满 | 完全胚 | 未出现 |
| diamond | 菱形 | 钻石 | 未出现（**全文无「钻石」**） |
| tilt / untilt | 倾斜 / 保留 untilt | 斜置 / 正置 | 未出现 |
| perverse sheaf | 反常层（T1131） | 错致层 | §2 几何 Satake（p13）、§3（p21）（**全文无「错致层」**） |
| isocrystal | 等晶体 | 有理晶体 | 未出现 |

其余 4 条（prism 棱镜、condensed/solid 凝聚态/固体、adic/affinoid 保留英文）本文未涉及或与香蕉空间一致。

### 4.2 本工程新增的 19 条裁定（香蕉空间均无专条）

来源：`SY02-41/工程文件/work/术语外部核对_香蕉空间.md` §六。其中 5 条是**「不译」裁定**，建议由 Lead 统一并入 termbase（本工程不改全局 `TERMS.tsv`）：

| 英文 | 本工程采用 | 依据 | 香蕉空间 |
| --- | --- | --- | --- |
| oper | oper（不译） | 本库 SY02-26/29 一致不译 | 有专条，条目名仍作 oper |
| shtuka | shtuka（不译） | 本库冻结 | 分歧（作「块」） |
| leg（shtuka 的腿） | leg（不译） | 本库冻结 | 分歧（作「爪」） |
| Hecke eigensheaf | Hecke 特征层 | 本库 SY02-41 | 无专条 |
| geometric Satake | 几何 Satake | 与本库一致 | 一致 |
| Whittaker sheaf | Whittaker 层 | 本库 SY02-41 | 无专条 |
| Kac–Moody localization | Kac–Moody 局部化 | 本库 SY02-41 | 无专条 |
| critical level | 临界水平 | 本库 | 无专条（通行译法） |
| nilpotent singular support | 幂零奇异支撑 | 本库 SY02-41 | 无专条 |
| microsupport | 微支撑 | 与「奇异支撑」配套 | 无专条 |
| Hecke-lisse | Hecke-lisse（**不译**） | 与「lisse 层」联动 | 无专条 |
| suave / prim | suave / prim（**不译**） | Heyer–Mann 专用词 | 无专条 |
| Gestalt | Gestalt（**不译**） | Scholze 专用词 | 无专条 |
| transmutation | transmutation（**不译**） | 同上 | 无专条 |
| ind-coherent sheaves | 归纳凝聚层（IndCoh 记号保留） | 本库 | 无专条 |
| second adjunction | 第二伴随 | 本库 | 无专条 |
| monodromy-free opers | 无单值 opers | 本工程 | 无专条 |
| coarse Langlands functor | 粗 Langlands 函子 | 本工程 | 无专条 |
| geometric Casselman–Shalika | 几何 Casselman–Shalika | 本库 | 无专条 |

### 4.3 取词顺序的口径冲突（需 Lead 裁定，本工程按任务书执行）

本工程任务书规定的取词顺序是「**本库冻结值最高优先** → 香蕉空间次之 → 都没有则保留英文」。但仓内 `CHANGELOG.md` 2026-11-27 条（术语对齐声明 v1.0）写的是「**新工程优先取香蕉空间写法，本库冻结值次之**」。两者在 6 条已知分歧上结论相反（perfectoid、diamond、tilt、perverse sheaf、shtuka/leg、isocrystal）。

**本工程一律按任务书执行**（即本库冻结值优先），理由：任务书是对本工程的直接指令，且同期在建的其余工程也彼此引用本库既有译名，中途改口径会造成同仓前后不一致。若 Lead 决定改按 CHANGELOG 的新口径，需要改的只有 6 行术语与本表，正文按词表全局替换一次即可（`check_terms.py` 会立刻报出漏改处）。

### 4.4 一处需 Lead 注意的符号口径

原文 §3 注 3.1（p20）明确说作者**读不懂** $(-^!,-_*)$-形式化，本报告统一用 $(-^*,-_!)$。这两套形式化的名字在中文里没有既定译法，本文一律保留符号原文（不译成「上叹号／下星号」之类），仅在正文首现处加一句括注，不另立名词。

