# 01 oper 对应的临界扭转 D 模 $\operatorname{Aut}_\sigma$

- 卡片：`glc/concept/aut-sigma-module`
- 失效模式：页码/出处定位漂移
- 严重度：minor
- 确认链：A(A7)+B(B1)
- 修复字段：`sources[0].pages`、`sources[0].pdf_pages`

## 错误版

- `sources[0].pages`：[70]
- `sources[0].pdf_pages`：[70]

## 正确版

- `sources[0].pages`：[71]
- `sources[0].pdf_pages`：[71]

## 为什么错

§14.5 与 Theorem 14.5.1 都在 p.71（p.70 只有 §14.4 与对 14.5.1 的引用）；卡只写 [70]。

## 证据

- E1 glc.pdf p.71 L4: `14.5. The automorphic module attached to an oper.`
- E1 glc.pdf p.71 L8: `Theorem 14.5.1 (Beilinson–Drinfeld [BD91]) …`

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 2 处，JSON 变更 4 行；md 镜像同步 1 处

## 形式化提示

章内小节跨页时，`sources.pages` 取本节标题与定理所在页。

## 防再犯

小节标题页与定理页不一致时，pages 取定理页。
