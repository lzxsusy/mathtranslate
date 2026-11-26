# 14 量子局部 Langlands 与 FLE 的边界值

- 卡片：`glc/concept/quantum-local-langlands`
- 失效模式：页码/出处定位漂移
- 严重度：minor
- 确认链：A(A8)+B(B1)
- 修复字段：`sources[0].pages`、`sources[0].pdf_pages`、`theorems[0].source`

## 错误版

- `sources[0].pages`：[73, 74]
- `sources[0].pdf_pages`：[73, 74]
- `theorems[0].source`：无编号陈述 / 原书 p.73

## 正确版

- `sources[0].pages`：[74]
- `sources[0].pdf_pages`：[74]
- `theorems[0].source`：无编号陈述 / 原书 p.74

## 为什么错

§15.4 标题在 `ch15.tex:65`，但 `\srcpage{74}` 在 :77；PDF p.74 L11 才是 `15.4. Relation with quantum local Langlands.`，卡却写 p.73。

## 证据

- E1 glc.pdf p.74 L11: `15.4. Relation with quantum local Langlands.`；L17-18: `κ = κG,crit + c κKil,G`
- ch15.tex:65 是 §15.4 标题、\srcpage{74} 在 :77

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 3 处，JSON 变更 4 行；md 镜像同步 2 处

## 形式化提示

`\srcpage` 与标题行分离时，以 PDF 标题页为准；本卡其余内容（水平 κ）与 2026-11-18 修订一致。

## 防再犯

§ 标题所在页用 PDF 页眉核对，不用 `\srcpage` 行号推算。
