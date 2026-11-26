# Lafforgue Tata 讲义资料卡（lafforgue02）

**一句话定位**：这是 Laurent Lafforgue《Cours à l'Institut Tata sur les chtoucas de Drinfeld et la correspondance de Langlands》（IHES/M/02/45，Juin 2002，56 页法文讲义）的中文资料卡。讲义用六章把函数域上 Langlands 对应证明的骨架讲完：Harder–Narasimhan 截断 → 紧化（fourre-tout 与完整同态）→ 边界上同调可忽略 → 本质上同调上的迹公式。本包把它拆成 **18 张卡（14 概念 + 4 推导）**，与同目录配套的中译本（`08_source_code/SY02-39_...`）逐页对齐。

## 一张卡只回答一个问题

- **概念卡**三问：这是什么？为什么需要它？哪里容易讲错？
- **推导卡**两问：这条推导怎么走通？每一步凭什么（原文写了什么，哪里是我们补的）？

## 底本与规模

- **A** = Lafforgue, *Cours à l'Institut Tata…*，IHES 预印本 IHES/M/02/45，**印刷页 1–56**。引用一律写印刷页。原书印刷页 = 底本 PDF 页 − 1（底本第 1 页是封面）。
- **B** = 白名单二次文献（nLab、Stacks Project）与本库译注；**C** = 原始文献（Drinfeld 1974/1987/1988/1989、Lafforgue 1997/1998/2002、Laumon 1987/2000，即讲义文献表里的九条）。
- 规模：**18 张 = 14 概念卡 + 4 推导卡**，全部 `status: "dev"`、`rights: "rewritten"`。
- 底本没有 LaTeX 源码，PDF 文本层是 2002 年 Ghostscript 用 Type3 位图字体写的（抽取即乱码），所有引用文字均由页面图像逐页录入。

## 30 秒入口

| 想看什么 | 打开 |
| --- | --- |
| 全包骨架与三条阅读路径 | `MAP.md` |
| 按轨道浏览全部卡 | `md/index.md` |
| 机器可读轻量索引 | `index.jsonl` |
| 概念卡样例 | `cards/concepts/drinfeld-chtouca.json`、`harder-narasimhan-truncation.json`、`r-negligible-representation.json` |
| 推导卡样例 | `cards/derivations/truncation-to-compactification.json`、`essential-part-in-middle-degree.json` |

## 三条阅读路径

1. **想懂证明在干什么**：`drinfeld-chtouca` → `truncation-to-compactification` → `r-negligible-representation` → `essential-part-in-middle-degree` → `trace-from-truncation`。五张卡就是第 I–II 章的主线。
2. **想懂紧化怎么造**：`fourre-tout` → `complete-homomorphism` → `chtouca-moduli-stack`。
3. **想懂紧合性怎么证**：`valuative-criterion-properness` → `iterated-phi-lattice` → `degenerator` → `properness-by-valuative-criterion`。

## 术语

与 `08_source_code/SY02-39_.../工程文件/reports/03_术语表.md` 同一份冻结表。两条硬约定：

- `chtouca`、`fourre-tout` 保留原文不译（前者是 Drinfeld 自造词，另有拼法 `shtuka`；后者是 Lafforgue 对「把所有截断紧化都收作开子叠的不分离叠」的自造称呼）。本库 SY02-18 对 `shtuka` 亦保留原文。
- `cohomologie essentielle` 一律译「本质上同调」，`cohomologie négligeable` 一律译「可忽略上同调」；「可忽略」是相对于固定的秩 $r$ 而言，不是通常意义上的「零」。

## 生产与校验

```bash
python tools/lint_cards.py      # 字段、id、related、anchor、页码范围
python tools/build_index.py     # 重建 index.jsonl
python tools/render_md.py       # 重建 md/
```

当前状态：18 张卡，`lint_cards.py` **0 error**，`related` 全部可解析，`A` 级页码全部落在 1–56。

## 权利

底本为 IHES 公开预印本，版权归作者与 IHES。本包是中文重写（`rights: rewritten`），只照录公式，不收录原文段落；英文/法文短引均 ≤120 字符。如原作者或 IHES 有异议，将立即撤下。
