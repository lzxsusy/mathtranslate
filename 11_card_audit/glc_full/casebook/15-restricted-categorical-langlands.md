# 15 受限范畴 Langlands 猜想

- 卡片：`glc/concept/restricted-categorical-langlands`
- 失效模式：页码范围过宽
- 严重度：minor
- 确认链：A(A6)+arbiter-t1b
- 修复字段：`sources[0].pages`、`sources[0].pdf_pages`、`theorems[0].source`、`theorems[0].proof.gap_note`

## 错误版

- `sources[0].pages`：[62, 63]
- `sources[0].pdf_pages`：[62, 63]
- `theorems[0].source`：猜想（§12.6，讲义无编号） / 原书 p.62–63
- `theorems[0].proof.gap_note`：这是猜想，讲义未证明；且讲义自己声明朴素形式可能过大或需限制到直和因子（p.62–63）。

## 正确版

- `sources[0].pages`：[63]
- `sources[0].pdf_pages`：[63]
- `theorems[0].source`：猜想（§12.6，讲义无编号） / 原书 p.63
- `theorems[0].proof.gap_note`：这是猜想，讲义未证明；且讲义自己声明朴素形式可能过大或需限制到直和因子（p.63）。

## 为什么错

§12.6 整节在 p.63；p.62 末仍是 §12.5 末句，卡却把 pages 写成 [62,63] 并把定理出处写成 p.62–63（`ch12.tex` 的 `\srcpage{63}` 落在 :117 的 note 句中，造成误判）。

## 证据

- E1 glc.pdf p.62 末仍是 §12.5 末句；p.63 页眉后第 4 行 `12.6. Restricted categorical Langlands.`
- ch12.tex:110 是 §12.6 标题，\srcpage{63} 却落在 :117 的 note 句中

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 4 处，JSON 变更 6 行；md 镜像同步 3 处

## 形式化提示

只有陈述完全落在 p.63 时才能把 pages 收窄为 [63]；先读 p.62 末行确认。

## 防再犯

收窄页码前确认上一页末行不属于本节；`\srcpage` 在段落中间时不可信。
