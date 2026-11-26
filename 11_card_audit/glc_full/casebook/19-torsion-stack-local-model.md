# 19 $\operatorname{Tor}^d$ 的局部模型与抛物对应

- 卡片：`glc/concept/torsion-stack-local-model`
- 失效模式：页码/出处定位漂移
- 严重度：minor
- 确认链：A(A4)+B(B1)
- 修复字段：`sources[0].pages`、`sources[0].pdf_pages`、`theorems[0].source`

## 错误版

- `sources[0].pages`：[43]
- `sources[0].pdf_pages`：[43]
- `theorems[0].source`：§7.4 证明 / 原书 p.43

## 正确版

- `sources[0].pages`：[42, 43]
- `sources[0].pdf_pages`：[42, 43]
- `theorems[0].source`：§7.4 证明 / 原书 p.42

## 为什么错

`Tor^d ≃ gl_d/GL_d` 的矩阵模型在 p.42 末三行；p.43 首段已转入 `d=d1+d2` 的抛物对应。

## 证据

- E1 glc.pdf p.42 末三行: `Tor^d ≃ gl_d/GL_d`；p.43 首段已是 `For d=d1+d2 … parabolic correspondence`

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 3 处，JSON 变更 4 行；md 镜像同步 2 处

## 形式化提示

该卡定理陈述与证明同页跨段，`sources.pages` 应取 [42,43] 以覆盖 p.42 的模型与 p.43 的证明。

## 防再犯

`§7.4 证明` 的页码以证明起始页为准，并检查是否跨页。
