# 16 受限局部系统叠

- 卡片：`glc/concept/restricted-local-systems`
- 失效模式：内部不一致（verification 陈旧残留）
- 严重度：minor
- 确认链：A(A5)+B(B2)
- 修复字段：`verification.checks[1].asserts`、`verification.checks[1].verdict`

## 错误版

- `verification.checks[1].asserts`：同一段把 QLisse(X) 定义为有限秩局部系统范畴 Lisse(X) 的 ind-完备化 IndLisse(X) 在自然 t-结构下的左完备化（quasi-lisse），并非「拟凝聚的局部系统」；卡中 definition.notation 的说法与此冲突 → P1，alignment=error。
- `verification.checks[1].verdict`：contradicted

## 正确版

- `verification.checks[1].asserts`：同一段把 QLisse(X) 定义为有限秩局部系统范畴 Lisse(X) 的 ind-完备化 IndLisse(X) 在自然 t-结构下的左完备化（quasi-lisse），并非「拟凝聚的局部系统」；卡中 definition.notation 已按此写成「IndLisse 的左完备化」，与之一致。
- `verification.checks[1].verdict`：confirmed

## 为什么错

卡正文已于 2026-11-18 按 AGK20a §0.5.4 改成「IndLisse 的左完备化」，但 `verification.checks[1]` 仍写「卡中 definition.notation 与此冲突 → P1，alignment=error」；核验块与正文自相矛盾。

## 证据

- 同卡 definition.notation 已改为「IndLisse 的左完备化」（2026-11-18，按 AGK20a §0.5.4）
- verification.checks[1] 仍写「卡中 definition.notation 的说法与此冲突 → P1，alignment=error」

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 2 处，JSON 变更 4 行；md 镜像同步 1 处

## 形式化提示

verification 是历史核验记录，也必须随正文修订同步，否则会误导下一次审计。

## 防再犯

修改 definition/theorem 后，检查 verification 中是否还有「与此冲突」「error」等旧判词。
