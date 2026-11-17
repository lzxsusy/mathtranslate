# K–W 2006 资料卡

Kapustin–Witten《Electric–Magnetic Duality and the Geometric Langlands Program》(hep-th/0604151, 231 页) 的**可检索、可自测、可打印**资料卡。

一张卡只回答一个问题：**概念卡**回答「这是什么、为什么需要、哪里会错」，**推导卡**回答「这条论证是怎么一步步走通的、每步凭什么」。

- 底本：`B` = Kapustin–Witten 2006（印刷页 2–222）；参考 `A` = Frenkel 2009（arXiv:0906.2747）、`C` = Witten 2008（arXiv:0802.0999）、`D` = Ben-Zvi 的电磁对偶与 Langlands 课程笔记。
- 规模：**67 张** —— 40 张概念卡 + 27 张推导卡。
- 权利：全部 `rights: "rewritten"`。文字是改写；公式照录；出处逐条标印刷页；**不收录原文段落**。

## 30 秒入口

| 想做什么 | 打开 |
|---|---|
| 看整篇的骨架 | [MAP.md](MAP.md) |
| 按轨道浏览 | [md/index.md](md/index.md) |
| 按 id / 页码检索 | [index.jsonl](index.jsonl) |
| 看一张概念卡长什么样 | [md/concepts/hitchin-moduli.md](md/concepts/hitchin-moduli.md) |
| 看一条推导链长什么样 | [md/derivations/sdual-mirror.md](md/derivations/sdual-mirror.md) |
| 字段规范 | [SCHEMA.md](SCHEMA.md) |

## 五条轨道

| 轨道 | 主题 | 概念卡 | 推导卡 |
|---|---|---|---|
| A | 四维物理与对偶：$N=4$ SYM、$\tau$、S-对偶、GNO、$^LG$ | 8 | 3 |
| B | 扭化与拓扑：twist、BRST、上同调、CP¹ 参数族、$\Psi$ | 6 | 5 |
| C | 舞台：曲线、Higgs 丛、$\mathcal M_H$、超凯勒商、Hitchin 纤维化 | 10 | 4 |
| D | 二维、膜与算子：A/B-模型、镜像、A/B-膜、Wilson、't Hooft、特征膜 | 8 | 6 |
| E | Langlands 与翻译器：Hecke、特征层、仿射 Grassmannian、Bogomolny、D-模 | 8 | 9 |

## 这张卡是怎么做出来的

1. **底本先行**：231 页原文 → 逐页文本（印刷页 N ↔ `p(N+1).txt`）→ 解经本 219 页（四层结构 + 1,330 处锚点）。
2. **讨论班检验**：八轮轮值报告（每轮报告 → 三席质询 → 修订 diff → 证据官核验 → 复算），共 112 条结构化语料；正是这一轮抓出了已发布解经本里的三处实质错误（(3.52) 共轭位置、(4.11)(4.20) 与 §10.5/§12.3 的下标横线、§12.3 type F 型别）。
3. **讲义压缩**：46 页十讲导读讲义把骨架讲成课堂语言。
4. **资料卡**：从上面三份材料里抽出 67 张卡，补公式、补证明或缺口、补常见误解、逐条回原文核页锚。

所以每张卡的 `sources` 都能回到原文的具体印刷页；`provenance_note` 说明哪些是原文说了（A）、哪些是原文暗示我们补的（B）、哪些是我们的判断（C）。

## 质检

```bash
python tools/lint_cards.py cards --strict      # 字段/长度/anchor/交叉引用，0 error 才算过
python tools/audit_pages.py --src <本机 source/text>   # anchor 与页文本对照（本机复核用）
python tools/build_index.py                    # 重建 index.jsonl
python tools/render_md.py                      # 重建 md/
```

已知限制：

- 全部卡 `status: dev`：**机器自检 + 抽样核对，未经人类逐卡认证**，训练语料只能标 `dev`，不能直接当 `train`。
- 抽样而非全量：页锚抽核 ≠ 全量重核；`theorems` 里 `sketch`/`gap` 是诚实的缺口标记，不是证明。
- 只覆盖非分歧情形（K–W 原文自己的边界），分歧与野分歧只在 §12 与文献里出现。
