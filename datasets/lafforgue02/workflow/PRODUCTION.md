# hausel22 生产说明（五步）

本包从底本 Hausel, *Enhanced mirror symmetry for Langlands dual Hitchin systems*（Proc. ICM 2022 Vol. 3, pp. 2228–2249；arXiv:2112.09455v2）生产 29 张资料卡（20 概念 + 9 推导）。全部工作只用仓库内工具与原文源码，不复制既有译文。

## 第 1 步：定位原文页

- 底本有 LaTeX 源码（arXiv:2112.09455 的 `HauselICM-arxiv.tex`，存放在 `08_source_code/SY05-29_*/源码/original/`），逐节与译本 `源码/ch1_intro.tex`、`ch2_background.tex`、`ch3_enhanced.tex` 对应。
- 印刷页与 PDF 页的对应：**印刷页 = 2227 + PDF 页**（印本 22 页，2228–2249）。22 行对照表在译本 `ch0_front.tex` 的 longtable 与 `工程文件/reports/01_通读笔记.md`。
- 关键公式回原页面图像核对：

```python
import fitz
doc = fitz.open("original/Hausel_ICM2022.pdf")
pix = doc[11].get_pixmap(dpi=150)   # 第 12 页
pix.save("_p12.png")
```

- `anchor` 写成可查形式：`A p.2237`、`A p.2243 eq (3.12)`；区间页用 `pages: [2237, 2238]`。

## 第 2 步：抽取概念与推导

- 通读 §1–§3.4，按六条轨道（A 镜像对称与几何 Langlands / B 拓扑镜像对称与 Hodge 数 / C 增强镜像对称与膜 / D 幂零锥上的等变重数 / E 仿射 Grassmannian 与重数代数 / O 总览）列清单。
- **先定 id 清单、再写卡**：`related` 只能引用清单内的 id，否则 lint 报"related 指向不存在"。
- 切片原则：一张卡只回答一个问题；概念卡拆到"定义 + 为什么需要 + 易错"，推导卡拆到"3–6 步、每步有 locator"。

## 第 3 步：写卡

- 用 Python dict 组织字段，`json.dumps(card, ensure_ascii=False, indent=2)` 写文件（UTF-8、2 空格缩进、文件名 = id 最后一段），避免手写 JSON 转义错误；LaTeX 反斜杠用 Python 原始字符串。
- 字段与规则见 `SCHEMA.md`。写卡时同步核对：
  - `summary` ≤120 汉字（去掉 `$...$` 与空白）；
  - `question` 以问号结尾；
  - 概念卡 `key_points` ≥3、`formulas` ≥1、`pitfalls` ≥2；
  - 推导卡 `steps` ≥3，每步 `text/why/locator/provenance` 齐全；
  - 任意一步非 `A` 时，`gaps` 至少一条；
  - `provenance_note` 点名 A/B/C 构成与**最没把握处**；
  - 中文自己写，术语与全文中译本一致（超 Kähler、非常稳定、重数代数、上行流、仿射 Grassmannian、jet 概形……）。
- 卡里不写本机路径、不写页码估计值以外的编号。

## 第 4 步：lint

```bash
cd datasets/hausel22
python tools/lint_cards.py cards --strict   # 必须 0 error，退出码 0
```

- 草稿阶段可用 `--allow-missing` 暂时悬空 `related`；定稿前必须去掉并跑 `--strict`。
- 输出末行形如：`cards=29 ids=29 dup=0 tracks={...} errors=0`，随后 `OK: 0 error`。

## 第 5 步：build_index 与 render

```bash
python tools/build_index.py   # 生成 index.jsonl（id/track/title/summary/path 等）
python tools/render_md.py     # 生成 md/concepts/*.md、md/derivations/*.md、md/index.md
```

- 检查 `md/index.md` 的轨道统计与卡数；`md/` 下渲染文件不得手写。
- 最后把三步命令与实际输出贴回 `README.md` 的「质检」一节，并把本次最没把握的页码写进各卡 `provenance_note`。

## 修订记录

### 2026-11-22 · 首版（29 卡）

- 依据：底本 LaTeX 源码逐节核对；印刷页靠 22 行对照表；公式编号 (1.1)(2.1)–(2.5)(3.1)–(3.14) 与定理编号 3.1–3.20 均与印本一致。
- 已知取舍：式 (3.9)(3.10)(3.11) 的角标按疑点清单 t1-08 订正为 $d=2,3$ 对应值，卡内注明；定理 3.10 的乘积分解、猜想 3.12 与 3.19 的断言均按原文标 `gap` 或"猜想"，未当成已证结论。
- 复检：`lint_cards.py cards --strict` = 29 卡 0 error；`build_index.py` 29 行；`render_md.py` 29 篇，全部通过。
