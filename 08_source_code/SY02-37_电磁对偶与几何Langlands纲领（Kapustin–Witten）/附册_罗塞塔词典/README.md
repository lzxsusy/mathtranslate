# 附册｜数学 ↔ 物理 罗塞塔词典（v1.1）

> SY02-37《电磁对偶与几何 Langlands 纲领》附册之二。底本：Kapustin–Witten, *Electric–Magnetic Duality and the Geometric Langlands Program*, arXiv:hep-th/0604151v3。
> 本册把 KW06 的数学侧与物理侧做成一部**可查阅的对照词典**，并配一张论证逻辑流程图。

## 这一版做了什么

- **108 条词条**（103 主干 + 4 深水区 + 5 读后修补），7 条轨道：对偶与群论 / 超对称与扭化 / Hitchin 与可积 / 膜与算子 / 几何 Langlands / 深水区 / 读后修补。
- **三个附录**：
  - A. 石碑总表（词条 × 一句话对应）
  - B. 背景术语 8 条（Nahm 方程、Nahm 定理、相干层、导出范畴、环路群、opers、Dolbeault、Kac–Moody）
  - C. 速查三表：左右约定（$G/{}^LG$ × A/B × 膜/层）、符号索引（58 行）、断言状态表（16 行，定理 / 原文推导 argued / 纲要）
- **论证逻辑流程图**（横版一页）：4d $\mathcal N=4$ → GL 扭化 → 紧化 → Hitchin $\mathcal M_H$ → 镜像（A/B）→ 膜↔层 → Hecke → 几何 Langlands；实线为正文明确蕴含，虚线为纲要。

## 盲测（诚实记录）

三轮盲测，由只读词典纯文本、不联网的智能体作答：

| 版本 | 页数 | 词条 | 懂 | 半懂 | 不懂 | 反向错误 |
|---|---|---|---|---|---|---|
| v1.0 | 80 | 103+4+8bg | 2 | 8 | 0 | 0 |
| v1.0.1 | 80 | 107+8bg | 5 | 5 | 0 | 0 |
| **v1.1** | **87** | **108+8bg** | **12** | 3 | 0 | 0 |

v1.1 已能支撑读者独立复述 KW06 的完整主线；剩余 3 个半懂点是「推导细节」而非「术语定义」，逐条列在 `盲测/评分报告.md`，作为 v1.2 的方向。

## 目录

```
附册_罗塞塔词典/
├── KW06_罗塞塔词典_v1.1.pdf          ← 成品（87 页）
├── KW06_论证逻辑流程图_v1.1.pdf      ← 成品（横版一页）
├── 源码/                             ← LaTeX 源（main/preamble/front/附录/entries/flow）
├── 工程文件/                         ← SCHEMA、REF-TERMS、TEST-QUESTIONS、构建脚本
├── 盲测/                             ← 三轮题面、答卷、词典纯文本、评分报告
└── 成品/                             ← 源码 zip
```

## 构建

```bash
export PATH="/c/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64:$PATH"
xelatex -interaction=nonstopmode main.tex    # 2–3 遍
grep -c '^!' main.log                        # 应为 0
```

## 版权

译文、词条、图表与盲测记录均为本工程原创；引用的原文公式、编号、图号标注出处（arXiv:hep-th/0604151v3）。不收录原文连续段落。引用请注明：数译发布 · SY02-37 附册。
