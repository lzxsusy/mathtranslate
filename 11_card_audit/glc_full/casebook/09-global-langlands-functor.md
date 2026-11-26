# 09 整体 Langlands 函子与重整化目标

- 卡片：`glc/concept/global-langlands-functor`
- 失效模式：页码/出处定位漂移
- 严重度：minor
- 确认链：A(A8)+B(B3)
- 修复字段：`sources[0].pages`、`sources[0].pdf_pages`、`theorems[0].source`

## 错误版

- `sources[0].pages`：[75]
- `sources[0].pdf_pages`：[75]
- `theorems[0].source`：章首定理（无编号）/ 原书 p.75

## 正确版

- `sources[0].pages`：[76]
- `sources[0].pdf_pages`：[76]
- `theorems[0].source`：章首定理（无编号）/ 原书 p.76

## 为什么错

第 16 章起于 p.76（PDF p.76 页眉），`ch16.tex:12` 的 `\srcpage{76}` 正确；但 `ch16.tex:2` 注释「原PDF第75页」错，卡照抄成 p.75。

## 证据

- E1 glc.pdf p.76 L4: `16. Proof of the global conjecture`；L10-14 给出 L_G
- ch16.tex:2 注释「原PDF第75页」错、ch16.tex:12 \srcpage{76} 对

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 3 处，JSON 变更 6 行；md 镜像同步 2 处

## 形式化提示

源码注释与 `\srcpage` 冲突时以 PDF 正文为准；本卡数学内容（`L_G^0=Ψ∘L_G` 的提升方向、QCoh^! 重整化）正确，只改页码。

## 防再犯

章起页以 PDF 页眉为准，源码开头的「原PDF第 N 页」注释只作线索。
