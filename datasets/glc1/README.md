# glc1 —— GLC I（Gaitsgory–Raskin, arXiv:2405.03599v3）资料卡集

本集是工程 **SY02-35（几何 Langlands 猜想 I：函子的构造）** 的结构化资料卡，
服务于译者、读者与下游检索。卡的规范见同目录 `SCHEMA.md`，校验工具见
`tools/lint_glc1.py`。

## 1. 底本

- 作者：Dennis Gaitsgory、Sam Raskin
- 原题：*Proof of the Geometric Langlands Conjecture I: Construction of the Functor*
- 版本：arXiv:2405.03599v3 [math.AG]，2025-09-30 提交（正文印 Oct 2, 2025）
- 规模：43 页，§0–§6 + References，无图，参考文献 21 条
- 译本：`08_source_code/SY02-35_几何Langlands猜想I_函子的构造/`
- PDF 不入库（`COMPLIANCE.md` §4）；`sources[].anchor` 指向仓内译文分块文件，
  便于从卡直接跳到译文对应段落。

## 2. 覆盖范围

本篇是几何 Langlands 猜想（GLC）证明五篇系列的第一篇。它**不证明** GLC，
只做三件事：

1. 无条件地造出 Langlands 函子 $L_G$（主定理 1.6.2），并给出唯一性刻画（推论 1.6.5）；
2. 证明猜想各版本等价（定理 3.5.6：de Rham / Betti / restricted / full / tempered）；
3. 在 GLC 成立的假设下，给出 Hecke 特征层的结构定理（定理 6.1.3），其中第 (5) 条
   （特征闭链等于幂零锥）是本文的新结果。

卡集只覆盖本篇内容，不代替对 [AG]、[AGKRRV]、[FR] 等前置文献的阅读。

## 3. 轨道（track）

| 轨道 | 主题 | 对应原文 |
| --- | --- | --- |
| A | 自守侧：$\operatorname{Bun}_G$ 与半步扭曲 D 模 | §1.1、§3.1 |
| B | 谱侧：$\operatorname{LS}_{{}^LG}$、归纳凝聚层、幂零支撑 | §1.2、§3.1 |
| C | Langlands 函子：真空 Poincaré 层、粗化版本、$L_G$ | §1.3–§1.6、§3.3–§3.4 |
| D | 有界性、$t$-结构与余连通性 | §1.7–§1.8、§2 |
| E | 版本比较与缓增（tempered）子范畴 | §0.3、§3.5、§5 |
| F | Hecke 特征层：结构定理与特征闭链 | §0.4、§6 |

## 4. 文件

```
glc1/
├── SCHEMA.md                 字段规范（本集的唯一权威）
├── README.md                 本文件
├── index.jsonl               索引（由 lint 工具重建，勿手改）
├── verification.jsonl        核验记录汇总（由 lint 工具重建）
├── cards/concepts/*.json     资料卡正本
└── tools/lint_glc1.py        校验 + 重建
```

## 5. 校验与重建

```bash
PYTHONIOENCODING=utf-8 python tools/lint_glc1.py            # 只校验
PYTHONIOENCODING=utf-8 python tools/lint_glc1.py --build    # 校验并重建 index/verification
```

要求 `error == 0` 才能合入。`related` 指向尚未写的卡只会报 warn，等补卡后自动消失。

## 6. 约定

- **数学只用 MathJax 标准宏**：卡里的公式要能被渲染器直接吃下，故禁用译本宏
  （`\Bun`、`\LG`、`\Dmodh` 等）；$\operatorname{Bun}_G$ 一律写全。
- 原文的 $\check G$（Langlands 对偶群）在本集统一写作 ${}^LG$。
- 印刷页 = PDF 页（原文页码与 PDF 页一致）。
- `status: published` 必须配 `verification.status: external-confirmed`；
  仅比对过原文、未做外部文献核对的卡保持 `source-only`。
- 原文标注为「新结果」的条目，必须在 `key_points` 中保留该标注，不得含混成
  「已知结论」。
- `rights` 恒为 `rewritten`：卡内文字为改写，不复制原文段落。

## 7. 相关工程

- `08_source_code/SY02-35_几何Langlands猜想I_函子的构造/` —— 译本本体与施工记录
- `datasets/glc/` —— 陈麟《几何 Langlands 纲领导论》（SY02-33）的 154 张卡，
  属讲义层，与本集的证明层互补
- `04_playbook/02_文献引进标准.md` —— 本工程入库时的三层闸门与评分卡

## 8. 现状（v1.0，2026-11-25）

共 **11 张**卡：A 轨 4 张、B 轨 4 张、C 轨 2 张、E 轨 1 张；D 轨（有界性与 t-结构）与 F 轨（Hecke 特征层）尚未建卡，留待 v1.1。

| 轨 | slug | 类型 | 题名 |
|---|---|---|---|
| `A` | automorphic-category | concept | 自守范畴 $\operatorname{D\!-\!mod}^{1/2}(\operatorname{Bun}_G)$ |
| `A` | betti-automorphic-category | concept | Betti 自守范畴 $\operatorname{Shv}^{\mathrm{Betti}}_{1/2,\operatorname{Nilp}}(\operatorname{Bun}_G)$ |
| `A` | half-twist | concept | 半步扭曲（half-twist）与 $\det$ 归一化 |
| `A` | hecke-action | concept | Hecke 作用与 Hecke 函子 |
| `B` | indcoherent-nilpotent-support | concept | 幂零奇异支撑与 $\operatorname{IndCoh}_{\operatorname{Nilp}}$ |
| `B` | nilpotent-cone | concept | 幂零锥 $\operatorname{Nilp}\subset\operatorname{Sing}(\operatorname{LS}_{{}^LG})$ |
| `B` | spectral-action | concept | 谱作用（spectral action）与局部化 $\operatorname{Loc}^{\operatorname{spec}}$ |
| `B` | spectral-stack | concept | 谱栈 $\operatorname{LS}_{{}^LG}$ 与受限变形版本 |
| `C` | coarse-langlands-functor | concept | 粗化 Langlands 函子 $L_{G,\mathrm{coarse}}$ |
| `C` | langlands-functor | concept | Langlands 函子 $L_G$ 与主定理 1.6.2 |
| `E` | glc-conjecture | conjecture | 几何 Langlands 猜想（de Rham 与 Betti 两种陈述） |
