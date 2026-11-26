# 11 Hitchin 底空间

- 卡片：`glc/concept/hitchin-base`
- 失效模式：页码范围遗漏
- 严重度：minor
- 确认链：A(A7)+B(B2)
- 修复字段：`sources[0].pages`、`sources[0].pdf_pages`

## 错误版

- `sources[0].pages`：[67]
- `sources[0].pdf_pages`：[67]

## 正确版

- `sources[0].pages`：[67, 68]
- `sources[0].pdf_pages`：[67, 68]

## 为什么错

`c_{Ĝ,Ω}≃⊕_i Ω_X^{d_i+1}` 与 `Hitch_Ĝ(X):=Γ(X,c_{Ĝ,Ω})` 在 p.68；卡写 [67]。

## 证据

- E1 glc.pdf p.68 L4-6: `c_{Ĝ,Ω} ≃ ⊕_i Ω_X^{d_i+1}, and the Hitchin base is Hitch_Ĝ(X) := Γ(X, c_{Ĝ,Ω}).`

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 2 处，JSON 变更 6 行；md 镜像同步 1 处

## 形式化提示

章首（p.67）给出背景，Hitchin 底的定义在 p.68，pages 应为 [67,68]。

## 防再犯

章首卡：pages 至少覆盖定义/陈述页，不能只写章首页。
