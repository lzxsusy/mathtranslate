# cdm14 生产说明（五步）

本包从底本 arXiv:1111.2087v4 生产 35 张资料卡（27 概念 + 8 推导）。全部工作只用仓库内工具与原文抽取，不联网检索、不复制译文。

## 第 1 步：定位原文页

- 原文文字抽取在 `08_source_code/SY02-12_晶体与D-模（Gaitsgory–Rozenblyum）/工程文件/work/en_full.txt`，每页开头有页锚 `===== BOOK PAGE n (PDF n) =====`，**印刷页 = PDF 页**（第 1 页即标题页）。
- 用脚本统计「公式号/定理号 → 首次出现印刷页」；关键公式再用页图核对：

```bash
pdftoppm -f <PDF页号> -l <PDF页号> -r 110 -png 原文/1111.2087v4.pdf /tmp/pg
```

- `anchor` 写成可查形式：`A p.12`、`A p.26–27`、`A p.47 eq (5.2)`；区间页用 `pages: [26, 27]`。

## 第 2 步：抽取概念与推导

- 通读 §0–§7，按八条轨道（A de Rham / B 左右晶体 / C 下降 / D t-结构 / E D-模 / F 扭化 / G 扭晶体 / O 总览）列清单。
- **先定 id 清单、再写卡**：`related` 只能引用清单内的 id，否则 lint 报「related 指向不存在」。
- 切片原则：一张卡只回答一个问题；概念卡拆到「定义 + 为什么需要 + 易错」，推导卡拆到「3–5 步、每步有 locator」。

## 第 3 步：写卡

- 用 Python dict 组织字段，`json.dumps(card, ensure_ascii=False, indent=2)` 写文件（UTF-8、2 空格缩进、文件名 = id 最后一段），避免手写 JSON 转义错误；LaTeX 反斜杠用 Python 原始字符串。
- 字段与规则见 `SCHEMA.md`。写卡时同步核对：
  - `summary` ≤120 字（去掉 `$...$` 与空白）；
  - `question` 以问号结尾；
  - 概念卡 `key_points` ≥3、`formulas` ≥1、`pitfalls` ≥2；
  - 推导卡 `steps` ≥3，每步 `text/why/locator/provenance` 齐全；
  - 任意一步非 `A` 时，`gaps` 至少一条；
  - `provenance_note` 点名 A/B/C 构成与**最没把握处**；
  - 中文自己写，术语与译注本一致（晶体、预栈、归纳凝聚、最终余连接、扭化、扭晶体……）。
- 卡里不写本机路径、不写页码估计值以外的编号。

## 第 4 步：lint

```bash
cd datasets/cdm14
python tools/lint_cards.py cards --strict   # 必须 0 error，退出码 0
```

本包实际输出：

```text
cards=35 ids=35 dup=0 tracks={'D': 8, 'A': 4, 'E': 4, 'F': 4, 'C': 6, 'B': 6, 'O': 1, 'G': 2} errors=0
OK: 0 error
```

## 第 5 步：索引与渲染

```bash
python tools/build_index.py     # 生成 index.jsonl（每行一张卡）
python tools/render_md.py       # 生成 md/{concepts,derivations,index.md}
```

二者都由 JSON 直接生成，可随时重跑；提交前确认 `git status` 里 `index.jsonl` 与 `md/` 已同步更新。
