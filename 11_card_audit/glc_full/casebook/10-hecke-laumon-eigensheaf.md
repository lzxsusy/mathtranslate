# 10 Hecke–Laumon 特征层

- 卡片：`glc/concept/hecke-laumon-eigensheaf`
- 失效模式：页码范围遗漏
- 严重度：minor
- 确认链：A(A4)+B(B2)
- 修复字段：`sources[0].pages`、`sources[0].pdf_pages`

## 错误版

- `sources[0].pages`：[46]
- `sources[0].pdf_pages`：[46]

## 正确版

- `sources[0].pages`：[45, 46]
- `sources[0].pdf_pages`：[45, 46]

## 为什么错

定义式 `α_d: HL^d_k(K) → L^d_E ⊠ K` 在 p.45 末尾，p.46 首行才接归一化与相容性；卡只写 [46]。

## 证据

- E1 glc.pdf p.45 末: `αd : HL^d_k(K) −→ L^d_E ⊠ K (d ≥ 0)`
- E1 glc.pdf p.46 首行: `with the evident normalization for d = 0 …`

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 2 处，JSON 变更 2 行；md 镜像同步 1 处

## 形式化提示

`α_d` 的 d≥0 家族与 d=0 归一化分居两页，pages 应为 [45,46]。

## 防再犯

公式与其归一化条件分居两页时，pages 取并集。
