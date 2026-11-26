# 08 Hecke 特征层的迹函数是特征标

- 卡片：`glc/concept/gl1-trace-character`
- 失效模式：页码/出处定位漂移
- 严重度：minor
- 确认链：A(A1)+B(B1)
- 修复字段：`sources[0].pages`、`sources[0].pdf_pages`、`theorems[0].source`

## 错误版

- `sources[0].pages`：[6]
- `sources[0].pdf_pages`：[6]
- `theorems[0].source`：引理 1.1.4 / 原书 p.6

## 正确版

- `sources[0].pages`：[7]
- `sources[0].pdf_pages`：[7]
- `theorems[0].source`：引理 1.1.4 / 原书 p.7

## 为什么错

引理 1.1.4 排在 PDF p.7 页眉后第一行，而源码 `ch01.tex:109-110` 把 `\srcpage{7}` 放在 `\end{lemma}` 之后，卡照抄了「原书 p.6」。

## 证据

- E1 glc.pdf p.7: `Lemma 1.1.4.` 是 p.7 页眉后第一行；p.6 以 Definition 1.1.3 结束
- 中译 ch01.tex:109-110 的 \srcpage{7} 落在 \end{lemma} 之后（标记漂移）

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 3 处，JSON 变更 6 行；md 镜像同步 2 处

## 形式化提示

校验 `theorems[].source` 的 `原书 p.N` 时，以 PDF 该页正文是否出现该陈述为准，`\srcpage` 只作旁证；本卡 pitfalls 里另有指向 p.6 的 Frobenius 约定，不在修复范围。

## 防再犯

引理/定理编号在页脚出现时，页码取「陈述起始页」，不能取 `\srcpage` 标记所在行。
