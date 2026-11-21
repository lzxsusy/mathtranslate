# Hausel ICM 2022 资料卡（hausel22）

**一句话定位**：这是 Hausel《Enhanced mirror symmetry for Langlands dual Hitchin systems》（Proc. Int. Cong. Math. 2022, Vol. 3, pp. 2228–2249，DOI 10.4171/ICM2022/164）的中文资料卡。前半是 Langlands 对偶群 Hitchin 系统之间镜像对称的综述，后半引入拉格朗日子上 Hitchin 系统的重数代数，并猜想它们在镜像上的结构。本包把这条主线拆成可检索、可自测、可打印的 29 张卡（20 概念 + 9 推导），与同目录下的全文中译本配套。

## 一张卡只回答一个问题

- **概念卡**三问：这是什么？为什么需要它？哪里容易讲错？
- **推导卡**两问：这条推导怎么走通？每一步凭什么（原文写了什么，哪里是我们补的）？

## 底本与规模

- **A** = Hausel, *Enhanced mirror symmetry for Langlands dual Hitchin systems*，Proc. ICM 2022 Vol. 3，印刷页 2228–2249（22 页）。引用一律写**印刷页**。arXiv:2112.09455v2（23 页）为同一稿的预印本，公式编号一致，可用作对照。
- **B** = nLab（`07_refs_nlab/` 白名单缓存：Hitchin fibration、geometric Langlands correspondence、geometric Satake equivalence）；**C** = 原始文献（Hitchin 1987、Hausel–Thaddeus 2003、Kapustin–Witten 2007、Donagi–Pantev 2013、Hausel–Hitchin 2021、Groechenig–Wyss–Ziegler 2018 等，即原文文献表里的条目）；**D** = 其他白名单与本库译注。B/C/D 在本包用得少，`sources[].text` 用对应字母标注。
- 规模：**29 张 = 20 概念卡 + 9 推导卡**，全部 `status: "dev"`。
- 权利：全部 `rights: "rewritten"`——中文重写；公式可照录；英文短引 ≤120 字符；不收录原文段落。
- 底本授权：CC BY 4.0（EMS Press 2022 年出版）。

## 30 秒入口

| 想看什么 | 打开 |
| --- | --- |
| 全包骨架与三条阅读路径 | `MAP.md` |
| 按轨道浏览全部卡 | `md/index.md` |
| 机器可读轻量索引 | `index.jsonl` |
| 概念卡样例 | `cards/concepts/very-stable-higgs-bundle.json`、`local-multiplicity-algebra.json`、`affine-grassmannian.json` |
| 推导卡样例 | `cards/derivations/very-stable-chain.json`、`q-delta-grassmann.json` |
| 字段规范 | `SCHEMA.md` |
| 生产流程 | `workflow/PRODUCTION.md` |

## 六条轨道

| 轨道 | 主题 | 概念卡 | 推导卡 |
| --- | --- | --- | --- |
| A | 镜像对称与几何 Langlands | 6 | 1 |
| B | 拓扑镜像对称与 Hodge 数 | 2 | 1 |
| C | 增强镜像对称与膜 | 4 | 1 |
| D | 幂零锥上的等变重数 | 4 | 4 |
| E | 仿射 Grassmannian 与重数代数 | 3 | 2 |
| O | 总览 | 1 | 0 |

## 这张卡是怎么做出来的（四步）

1. **定位原文页**：用论文的 LaTeX 源码（arXiv:2112.09455 的 `HauselICM-arxiv.tex`）逐节核对；印刷页 = 2227 + PDF 页（印本 22 页），先制 22 行页码对照表写进译本，再按表定 `sources[].pages`。关键公式回原页面图像核对（`pymupdf` 渲染 150 dpi）。
2. **定 id 清单**：按六轨列出 20 概念 + 9 推导的 id，先保证 `related` 只引用包内 id，再写卡（本包 `related` 全部可解析）。
3. **写卡**：一卡一 JSON，用 Python dict + `json.dumps(..., ensure_ascii=False, indent=2)` 生成（避免手写转义错误）；术语与全文中译本（`08_source_code/SY05-29_*/源码/`）一致，句子自己重写。
4. **质检**：lint → build_index → render_md；`--strict` 必须 0 error。

## 质检

```bash
cd datasets/hausel22
python tools/lint_cards.py cards --strict      # 必须 0 error
python tools/build_index.py                    # 生成 index.jsonl
python tools/render_md.py                      # 生成 md/
```

本包实际输出：

```text
cards=29 ids=29 dup=0 tracks={'A': 7, 'B': 3, 'C': 5, 'D': 8, 'E': 5, 'O': 1} errors=0
OK: 0 error
wrote .../datasets/hausel22/index.jsonl (29 cards: concept=20 derivation=9)
rendered 29 cards -> .../datasets/hausel22/md
```

## 已知限制

- 全部 `status: "dev"`：未经人类逐张认证；每张卡的 `provenance_note` 标了 A/B/C 的构成与**最没把握处**。
- 抽样非全量：29 张覆盖 §1–§3.4 主线，不是每节每式一卡；§2.4 的 $p$ 进证明与 §3.3 的仿射 Springer 纤维细节只作背景提及。
- 原文的自造术语 `wobbly`、`multiplicity algebra` 按语用定译（"wobbly"保留原文，重数代数按 §3.2 定义），已在术语表注明。
- 原文式 (3.9)(3.10)(3.11) 的角标有笔误（见译本译注与疑点清单 t1-08），本包 `jet-scheme-n2` 卡按应有值 $d=2,3$ 表述并写明这一处。
- 定理 3.10 的证明归给 [HH]，本文只有结论；本包相应推导卡把"乘积分解无额外分量"标为 `B` 级并写进 `gaps`。
- 猜想 3.12、3.19 都是原文的猜想（"我们预期"），卡里一律写"猜想"，不说"已证"。
