# 04 Drinfeld–Sokolov 规范形式与 Kostant 切片

- 卡片：`glc/concept/drinfeld-sokolov-gauge`
- 失效模式：页码/出处定位漂移
- 严重度：minor
- 确认链：A(A7)+B(B2)
- 修复字段：`sources[0].pages`、`sources[0].pdf_pages`、`theorems[0].source`

## 错误版

- `sources[0].pages`：[68]
- `sources[0].pdf_pages`：[68]
- `theorems[0].source`：§14.2 局部正规形 / 原书 p.68

## 正确版

- `sources[0].pages`：[69]
- `sources[0].pdf_pages`：[69]
- `theorems[0].source`：§14.2 局部正规形 / 原书 p.69

## 为什么错

§14.2「局部正规形」在 p.69；p.68 只有 §14.1 与 Hitchin 底。

## 证据

- E1 glc.pdf p.69 L4: `14.2. The local normal form.`

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 3 处，JSON 变更 6 行；md 镜像同步 2 处

## 形式化提示

定理出处与 sources.pages 同步；本卡 gap_note 只写「§14.2」不含页码，无需改。

## 防再犯

小节号与页码必须自洽：小节首次出现页 = pages 起点。
