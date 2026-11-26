# 20 非分歧 oper 空间

- 卡片：`glc/concept/unramified-oper`
- 失效模式：页码范围遗漏
- 严重度：minor
- 确认链：A(A8)+B(B1)
- 修复字段：`sources[0].pages`、`sources[0].pdf_pages`

## 错误版

- `sources[0].pages`：[72]
- `sources[0].pdf_pages`：[72]

## 正确版

- `sources[0].pages`：[72, 73]
- `sources[0].pdf_pages`：[72, 73]

## 为什么错

anchor `ch15.tex:28-33` 跨 p.72-73：`η∈ĝ[[t]]dt`、缺陷度量 `λ̌`、`Op^unr=⊔Op^{reg,λ̌}` 与形式片包含都在 p.73，卡只写 [72]。

## 证据

- E1 glc.pdf p.73 L4 起: `d+η, η∈ĝ[[t]]dt`、缺陷 λ̌、Op^{reg,λ̌} 分层
- anchor ch15.tex:28-33 跨 p.72-73

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 2 处，JSON 变更 6 行；md 镜像同步 1 处

## 形式化提示

参数化定义跨页时 pages 取并集；本卡 summary 同时用到 p.72 的朴素定义与 p.73 的缺陷分层。

## 防再犯

anchor 行范围跨 `\srcpage` 时，pages 必须包含两端。
