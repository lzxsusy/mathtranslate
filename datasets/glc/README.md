# glc · 几何 Langlands 资料卡

陈麟《Introduction to Geometric Langlands Theory》（清华 2023 秋讲义，2025-08-08 修订版，85 页）的**结构化资料卡**：
一卡一个定义、定理或关键构造，共 **154 张**，按 O–H 九条轨道组织。每张卡都经独立核验员逐句对齐讲义原文，
并尝试在 nLab、Stacks Project 与讲义参考文献中逐字找依据。

- 底本：`LinChenGLC2023.pdf`（16 章 119 节，正文 p.5–p.83）
- 工作底稿：同目录中文译注本（`LinChenGLC2023_中文译注_校订版`，110 页，59 条译注）
- 卡片规范：[`SCHEMA.md`](SCHEMA.md)　生产流程：[`workflow/PRODUCTION.md`](workflow/PRODUCTION.md)
- 总表：[`taxonomy.md`](taxonomy.md)（按 track）　索引：[`index.jsonl`](index.jsonl)　核验：[`verification.jsonl`](verification.jsonl)

## 核验状态

| 状态 | 张数 | 含义 |
| --- | --- | --- |
| `external-confirmed`（published） | 66 | 至少一条 nLab / Stacks / 讲义参考文献页面逐字支持卡内全部数学断言，核验员记录了「哪句支持哪条」 |
| `source-only`（reviewed） | 88 | 与讲义逐句一致，但外部无对应陈述（讲义自创构造、未成文定理）；**不声称外部已核** |
| `rejected` | 0 | 与权威陈述冲突 |

逐卡明细见 [`verification.jsonl`](verification.jsonl)：每行给出 `alignment`（与原句对齐）、`checks[]`
（核验的页面、URL、nLab `last_revised`、页面原句支持的断言、判定）。渲染后的卡在 `md/`。

> `source-only` 不等于「有错」：它表示核验员在公开权威渠道找不到逐字对应，卡片仍严格对齐讲义原句。
> 引用这些卡时请按讲义页码引，不要写成「已由 nLab 确认」。

## 目录

```
cards/concepts/*.json   154 张概念卡（一卡一文件）
cards/examples/         例子卡（本批未产出）
index.jsonl             轻量索引：id / track / title / summary / path
verification.jsonl      核验台账（一行一卡）
taxonomy.md             按 track 的总表，含核验标记 E/S
MAP.md                  卡片关系图（related 图）
md/                     渲染后的 Markdown（一卡一文件）
tools/                  lint_glc / build_index / render_md / gen_docs
workflow/PRODUCTION.md  五角色四闸流程
```

## 轨道

| track | 主题 | 张数 |
| --- | --- | --- |
| O | 总览：几何 Langlands 的纲领 | 4 |
| A | 整体类域论与 Abel 侧 | 4 |
| B | Hecke 特征层、几何 Satake、$\operatorname{Bun}_G$ | 9 |
| C | Whittaker 模型与 Laumon 层 | 20 |
| D | Fourier 变换与洁净性 | 19 |
| E | 因子化、Ran 空间与 Laumon 因子化 | 18 |
| F | 消失猜想与范畴猜想 | 30 |
| G | 谱侧、Hitchin 系统与受限变体 | 20 |
| H | 局部等价与整体证明架构 | 30 |

## 生产流程（本批实做）

1. **Lead** 读规范与底本 → 切章、写 `BRIEF.md`（只依讲义，宏全部展开，编号照抄）。
2. **drafter** 每人两章起草 6–10 张，产出 `_index_<name>.tsv`；自检 JSON、字段、`related` 闭合。
3. **verifier** 一章一人、独立于 drafter：①与 `chNN.tex` 锚点逐句对齐（记 `alignment`）②去 nLab / Stacks /
   原始文献逐字核验并写「哪句支持哪条断言」③判 `external-confirmed` / `source-only` / `rejected`。
4. **Lead 汇总**：修 `alignment=error`（本批 9 条，全部已改并复验）、合并台账、设置 `status`、lint 清零、
   生成索引与渲染、写 README。
5. 入库前 `tools/lint_glc.py` 必须 `errors=0`；`published` 不得是 `source-only`。

本批共 8 名 drafter、16 名 verifier；每章 8–10 张，全书 154 张。

## 本批修订记录（2026-11-18）

核验发现的 9 处对齐错误已全部改正（明细见 `verification.jsonl` 的 `alignment` 与 `report_*.md`）：

| 卡 | 问题 | 改法 |
| --- | --- | --- |
| `quantum-local-gl` | 把 §1.5 的 $\mathrm{KM}_{\mathfrak g,\kappa}$ 写成「临界水平」 | 改为「水平 $\kappa$」（临界水平只用于 §1.4） |
| `local-whittaker-eigenfunction` | KP 称优势权指数恒为负 | 限定为有效优势权；一般优势权（如 $\lambda=(0,-1)$）指数可为正 |
| `restricted-local-systems` | $\operatorname{QLisse}$ 说成「拟凝聚局部系统」 | 改为 $\operatorname{IndLisse}$ 的左完备化（quasi-lisse） |
| `categorical-trace` | 把 coev/ev 写成「余单位与单位」 | coev = 单位 $\eta$，ev = 余单位 $\varepsilon$ |
| `fourier-deligne-transform` | 把「$t$-正合⇒单」写进定理，且说可能带平移 | 改为「等价 + $t$-正合」，删去平移；补 KL85 归一化差异 |
| `averaging-functor` | 基础情形也说成「茎」 | 基础情形是 $\operatorname{Av}^d_E(W_k)$，不是茎 |
| `vanishing-theorem` | 写成 $k=\operatorname{rank}(E)$ | 改为 $\operatorname{rank}(E)>k$ |
| `whittaker-equivalence` | 把 $P=G$ 错挂到 Whittaker→球面的延拓条件 | 删去 $P=G$，指明那是第 16 章导出 Satake 的边界 |
| `global-langlands-functor` | summary 把提升方向写反 | $\mathbb L_G$ 是 $\mathbb L_G^0$ 经 $\Psi$ 的提升（$\mathbb L_G^0=\Psi\circ\mathbb L_G$） |

## 纠错

发现错误请开 issue 或在卡上标注：给出 **卡 id / 原句（sources.anchor）/ 错在哪 / 权威依据（URL + 页码或 Tag）**。
修订时同时改三处：卡片字段、`verification.jsonl` 的对应行、`md/` 渲染文件（重跑 `tools/render_md.py`）。

## 复现

```bash
cd datasets/glc
python tools/lint_glc.py        # 0 error 才入库
python tools/build_index.py     # index.jsonl
python tools/render_md.py       # md/
python tools/gen_docs.py        # taxonomy.md / MAP.md
```

## 版权与引用

卡片是对讲义内容的**改写**（`rights: "rewritten"`），不逐字复制原文；数学记号与编号照讲义。
引用请注明底本：Lin Chen, *Introduction to Geometric Langlands Theory*, lecture notes (Fall 2023,
revised 2025-08-08, notes by Wenhan Dai)，并给出本库卡 id。

`sources[].anchor` 形如 `源码/chapters/ch05.tex:114-123`，指中译校订本
《LinChenGLC2023_中文译注_校订版》的 LaTeX 源码目录（版权原因不随数据集发布）。
只读卡片时用 `sources[].pages`（印刷页，与 `pdf_pages` 相同，底本正文自 p.5 起）即可定位；
有该源码时可 grep 锚点行号复核。
