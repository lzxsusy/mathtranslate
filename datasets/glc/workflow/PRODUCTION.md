# glc 资料卡生产流程（PRODUCTION v1）

本文件回答三件事：**这批卡怎么来的**、**每张卡怎么过闸**、**怎么复现与纠错**。

## 1. 分工

| 角色 | 负责 | 不做什么 | 产物 |
| --- | --- | --- | --- |
| Lead | 切章、定 track、集成、入库、push | 不替人写卡；不自己给自己的卡打勾 | `taxonomy.md`、`README.md`、`verification.jsonl` 合并 |
| drafter（8 人，每人 2 章） | 从译本逐条抽出定义/定理/命题/引理/猜想，写成卡 | 不联网找外部文献、不改译本、不补数学 | `cards/concepts/*.json`、`_index_<name>.tsv` |
| verifier（8 人，交叉分配） | 核对每张卡：①与讲义原句是否一致；②外部权威页面是否真的有同一陈述 | 不改卡片的数学内容（只写核验记录） | `verification.jsonl` 分片、`review/verify_<name>.md` |
| archivist | 抽检 anchors：`source` 的 tex 行号与页码能否对上 | 不改卡 | 抽检表 |
| integrator（Lead 兼） | lint、index、md、docs、commit | 不批量重写卡片正文 | 站点文件与提交 |

drafter 与 verifier 必须**不是同一个 agent**，且 verifier 只读卡与原文，不读起草过程。

## 2. 每张卡怎么过闸

```
起草（只依据译本 + 英文原文）
   ↓  tools/lint_glc.py（结构闸）
闸 1  字段齐全、id/track 合法、related 可解析、sources 五要素齐全    0 error
   ↓
闸 2  原文对齐：抽 100% 的 source.anchor，回译本该行确认「卡里的陈述 = 该条原文」
   ↓
闸 3  外部核验：每条数学断言找一条 B 级白名单（nLab / Stacks Project / ProofWiki）
      或 A 级文献的公开页面，逐字读那段并记「哪句支持哪条断言」；找不到就标 source-only
   ↓
闸 4  一票否决：任一条 fabricated（引用不存在、页码错、把猜想写成定理、把 source-only
      写成 external-confirmed）→ 整批退回重写
   ↓
入库：status draft → reviewed；index/md/taxonomy/MAP 重建；commit
```

## 3. 核验的硬规矩

1. **只确认、不推广**：外部页面只要有一句与该卡陈述对应即可记 `match`；页面上没有的细节不补，
   也不许因为「nLab 说得更强」而改卡。
2. **记录到句**：`verification.checks[].asserts` 写清「卡里哪条断言」被哪句支持；只写 URL 不算核过。
3. **日期与版本**：nLab 记 `Last revised`（页面没有就不写）；Stacks 记 Tag 号；访问日期统一写当日。
4. **B 级不唯一**：nLab/Stacks 只作框架确认，涉及具体定理编号与归因时以 A 级（原书、原始论文、
   经典教材）为准；本讲义自身的陈述以讲义为 A 级。
5. **黑名单**：知乎、百度百科、CSDN、简书、公众号、B 站、个人博客、AI 摘要一律不看、不引。
6. **讲义自创的构造**（受限变体、$\Shv_{\mathrm{Nilp}}$ 的某些表述、FLE 的具体形式）通常没有外部页面，
   标 `source-only` 是诚实的结果，不丢分；把它标成 `external-confirmed` 才是事故。

## 4. 复现

```bash
cd datasets/glc
python tools/lint_glc.py      # 0 error 才继续
python tools/build_index.py   # cards → index.jsonl
python tools/render_md.py     # cards → md/
python tools/gen_docs.py      # taxonomy.md + MAP.md
```

## 5. 纠错

发现错误：记「卡 id + 错在哪 + 证据（tex 行号 / 外部页面原句）+ 正确说法」，交 Lead 复核；
确认后改 `cards/**/<slug>.json`，重跑 §4 四步，并在 `verification.jsonl` 追加一条更正记录
（`note` 写改了什么），提交信息写 `fix(glc): <id> ...`。历史错误不删除，只追加记录，保留可追溯性。

## 6. 本批执行记录（2026-11-18）

| 项 | 数字 |
| --- | --- |
| 底本 | Lin Chen《Introduction to Geometric Langlands Theory》，85 页，16 章 119 节 |
| 卡片 | 154 张（concept），16 章，每章 8–10 张 |
| drafter | 8 人，每人 2 章（c0102 / c0304 / c0506 / c0708 / c0910 / c1112 / c1314 / c1516） |
| verifier | 16 人，一章一人（v01–v16），与 drafter 完全不相交 |
| 闸 1（lint） | 154 卡 0 error；summary 超长的 47 条压到 ≤120 字后 0 warning |
| 闸 2（对齐） | 154 卡全部对齐；`alignment=error` 9 条，已全部改正并复验 |
| 闸 3（外部核验） | external-confirmed 66、source-only 88、rejected 0 |
| 闸 4（一票否决） | 未触发；无捏造 URL / 日期 / 页码 |

核验抓到的 9 处实质错误（改法见 `README.md` 修订表）：量子局部 GL 的水平与临界水平混用、
Whittaker 特征函数指数符号、$\operatorname{QLisse}$ 的定义、范畴迹的单位/余单位、
Fourier–Deligne 变换的 $t$-正合性、平均函子的基础情形、消失定理的秩条件、
$P=G$ 的归属、整体函子的提升方向。

流程偏差：verifier 原计划 8 人交叉分配，实做改为 16 人一章一人——因为「逐句对齐 + 逐字找依据」
在两章合并时精度不够；单章单人可以读完该章全部原句。
