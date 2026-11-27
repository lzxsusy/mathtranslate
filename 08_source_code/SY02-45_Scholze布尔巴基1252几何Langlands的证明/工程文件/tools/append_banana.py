# -*- coding: utf-8 -*-
"""向 SY02-41 的香蕉空间核对文件追加 SY02-45 的增量（只追加，不改前文）。"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code")
SRC = ROOT / "SY02-41_局部Langlands几何化Berkeley讲义" / "工程文件" / "work" / "术语外部核对_香蕉空间.md"

ADD = r"""
---

# 继承自 SY02-41，只记增量（SY02-45《Scholze 布尔巴基 1252 号：几何 Langlands 的证明》）

> 本节由 SY02-45 追加。**上文（一至五节）一字未改**；本节只记本工程新遇到、SY02-41 未收的词。
> 按 SY02-45 任务书要求，**未重新联网核**香蕉空间，仅沿用上文的判据与本库结论；
> 凡未实际读到香蕉空间页面的，一律标「无专条/未重核」，不臆测社区用法。

## 六、SY02-45 增量词表

| 英文 | 本工程采用 | 依据 | 香蕉空间情况 |
| --- | --- | --- | --- |
| oper | oper（不译） | 本库 SY02-26/29 一致不译 | 有专条「oper」，中文条目名仍作 oper |
| shtuka | shtuka（不译） | 本库冻结（香蕉空间作「块」） | 分歧，见上文第五节第 2 条 |
| leg（shtuka 的腿） | leg（不译） | 本库冻结（香蕉空间作「爪」） | 分歧，同上 |
| Hecke eigensheaf | Hecke 特征层 | 本库 SY02-41 | 无专条 |
| geometric Satake | 几何 Satake | 上文一致 | 一致 |
| Whittaker sheaf | Whittaker 层 | 本库 SY02-41 | 无专条 |
| Kac–Moody localization | Kac–Moody 局部化 | 本库 SY02-41 | 无专条 |
| critical level | 临界水平 | 本库 | 无专条（「临界水平」为通行译法） |
| nilpotent singular support | 幂零奇异支撑 | 本库 SY02-41（「奇异支撑」） | 无专条 |
| microsupport | 微支撑 | 与「奇异支撑」配套 | 无专条 |
| Hecke-lisse | Hecke-lisse（不译） | 本工程裁定：与「lisse 层」联动，不译 | 无专条 |
| suave / prim | suave / prim（不译） | 本工程裁定：Heyer–Mann 专用词，不译 | 无专条 |
| Gestalt | Gestalt（不译） | 本工程裁定：Scholze 专用词，不译 | 无专条 |
| transmutation | transmutation（不译） | 同上 | 无专条 |
| ind-coherent sheaves | 归纳凝聚层（记号 IndCoh 保留） | 本库 | 无专条 |
| second adjunction | 第二伴随 | 本库 | 无专条 |
| monodromy-free opers | 无单值 opers | 本工程 | 无专条 |
| coarse Langlands functor | 粗 Langlands 函子 | 本工程 | 无专条 |
| geometric Casselman–Shalika | 几何 Casselman–Shalika | 本库 | 无专条 |

## 七、结论（增量）

1. 本工程**没有**与香蕉空间冲突的新词：新遇到的全是「无专条」，按本库与通行中文处理即可。
2. 与上文第五节第 2 条相同的 6 条分歧在本工程**全部沿用本库**（shtuka/leg 不译、perverse 反常层等），
   正文不出现「块/爪/错致层」等异名。
3. 建议：`Hecke-lisse`、`suave`、`prim`、`Gestalt`、`transmutation` 五个「不译」裁定会被后续几何 Langlands 工程复用，
   **建议并入 termbase**（由 Lead 统一处理，本工程不改 `01_corpus_zh/数语规范/TERMS.tsv`）。
"""

text = SRC.read_text(encoding="utf-8")
if "SY02-45" in text:
    print("已追加过，跳过")
else:
    SRC.write_text(text.rstrip() + "\n" + ADD, encoding="utf-8")
    print("已追加 SY02-45 增量节")
