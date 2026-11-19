# gtgl15 生产说明（五步）

本包从底本 arXiv:1506.04293v3 生产 40 张资料卡（30 概念 + 10 推导）。全部工作只用仓库内工具与原文抽取，不联网检索、不复制译文。

## 第 1 步：定位原文页

- 原文文字抽取在 `原文/EN_part1.txt`–`EN_part4.txt`，每页开头有页锚 `[[PDF p.N | printed p.M]]`，**印刷页 = PDF 页 − 1**。引用、`sources[].pages`、`anchor` 一律用印刷页。
- 先用脚本统计「公式号 → 首次出现印刷页」（本包用 `pdftotext` 抽取文本按页锚分页后正则匹配 `\(2\.15\)` 这类公式号）。
- 关键公式再用页图核对：

```bash
pdftoppm -f <PDF页号> -l <PDF页号> -r 110 -png 原文/Witten_1506.04293v3_EN.pdf /tmp/pg
```

- `anchor` 写成可查形式：`A p.38 eq (4.4)`、`A p.71 eq (7.6)`；区间页用 `pages: [68, 71]`。

## 第 2 步：抽取概念与推导

- 通读 §1–§7，按六条轨道（A 几何 / B 对偶环面 / C 膜 / D 't Hooft–Hecke / E 行列式线丛 / O 总览）列清单。
- **先定 id 清单、再写卡**：`related` 只能引用清单内的 id，否则 lint 报“related 指向不存在”。
- 切片原则：一张卡只回答一个问题；概念卡拆到“定义 + 为什么需要 + 易错”，推导卡拆到“3–5 步、每步有 locator”。

## 第 3 步：写卡

- 用 Python dict 组织字段，`json.dumps(card, ensure_ascii=False, indent=2)` 写文件（UTF-8、2 空格缩进、文件名 = id 最后一段），避免手写 JSON 转义错误；LaTeX 反斜杠用 Python 原始字符串。
- 字段与规则见 `SCHEMA.md`。写卡时同步核对：
  - `summary` ≤120 汉字（去掉 `$...$` 与空白）；
  - `question` 以问号结尾；
  - 概念卡 `key_points` ≥3、`formulas` ≥1、`pitfalls` ≥2；
  - 推导卡 `steps` ≥3，每步 `text/why/locator/provenance` 齐全；
  - 任意一步非 `A` 时，`gaps` 至少一条；
  - `provenance_note` 点名 A/B/C 构成与**最没把握处**；
  - 中文自己写，术语与中文初译本一致（希格斯丛、希钦纤维化、谱曲线、本征膜、赫克修正……）。
- 卡里不写本机路径、不写页码估计值以外的编号。

## 第 4 步：lint

```bash
cd datasets/gtgl15
python tools/lint_cards.py cards --strict   # 必须 0 error，退出码 0
```

- 草稿阶段可用 `--allow-missing` 暂时悬空 `related`；定稿前必须去掉并跑 `--strict`。
- 输出末行形如：`cards=40 ids=40 dup=0 tracks={...} errors=0`，随后 `OK: 0 error`。

## 第 5 步：build_index 与 render

```bash
python tools/build_index.py   # 生成 index.jsonl（id/track/title/summary/path 等）
python tools/render_md.py     # 生成 md/concepts/*.md、md/derivations/*.md、md/index.md
```

- 检查 `md/index.md` 的轨道统计与卡数；`md/` 下渲染文件不得手写。
- 最后把三步命令与实际输出贴回 `README.md` 的「质检」一节，并把本次最没把握的页码写进各卡 `provenance_note`。

## 修订记录

### 2026-11-19 · 维数类断言纠错

依据：Witten 2015 §2.4 eq (2.6)（印刷 p.8；`原文/EN_part1.txt` 第 389–394 行）：
$\dim F=\dim\mathcal V=\frac12\dim\MH=(g-1)\dim G$，其中维数均指复维数；故 $\dim_\mathbb{C}\MH=2(g-1)\dim G$、$\dim_\mathbb{R}\MH=4(g-1)\dim G$。

- **错误 1：`cards/concepts/hitchin-moduli.json`** —— 曾把 $\dim_\mathbb{C}\MH$ 写成 $(g-1)\dim G$（漏因子 2），涉及 `summary`、`definition.text`、`formulas[0]`、`theorems[0].statement` 与 `theorems[0].proof.steps`、`pitfalls[1]`；已全部改为 $2(g-1)\dim G$，证明改写为「底空间维数 $\to$ 纤维 Lagrangian $\to$ 一半维数」三步。顺带更正 $U(N)$ 情形：$\dim_\mathbb{C}\MH=2N^2(g-1)+2$（§2.6.5 明写 $\frac12\dim\MH=N^2(g_c-1)+1$）。
- **错误 2：`cards/concepts/stable-locus.json`** —— 曾称 $\mathcal M$「与 $\MH$ 复维数相同、是『中维』而非一半维数」；已改为 $\dim_\mathbb{C}\mathcal M=(g-1)\dim G=\frac12\dim_\mathbb{C}\MH$，$\mathcal M$ 是复 Lagrangian（实余维 = 实维数一半），并在 `formulas` 补上维数式、`pitfalls` 改写。
- **自查**：其余含维数断言的卡（`abelianization-prym`、`hitchin-fibration`、`hyperkahler-quotient`、`integrable-system`、`skyscraper-zero-brane`、`spectral-cover`、`spectral-curve`、`deriv/dimension-count`、`deriv/prym-abelianization`、`deriv/spectral-genus`）逐条对照 eq (2.5)(2.6) 与 §2.6.1/§2.6.3/§2.6.5，数值无误；仅把 $\MH$ 的维数统一标明为复维 $\dim_\mathbb{C}\MH$，避免「一半」歧义。
- **复检**：`lint_cards.py cards --strict` = 40 卡 0 error；`build_index.py` 40 行；`render_md.py` 40 篇，全部通过。
