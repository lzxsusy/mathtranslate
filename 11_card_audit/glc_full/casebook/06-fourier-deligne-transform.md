# 06 向量丛的 Fourier–Deligne 变换

- 卡片：`glc/concept/fourier-deligne-transform`
- 失效模式：内部不一致
- 严重度：minor
- 确认链：A(A3)+arbiter-t1b
- 修复字段：`theorems[0].proof.steps[2].why`

## 错误版

- `theorems[0].proof.steps[2].why`：$t$-正合函子把单对象送到单对象（至多差平移）。

## 正确版

- `theorems[0].proof.steps[2].why`：等价加 $t$-正合才保持单对象，且不产生平移。

## 为什么错

`proof.steps[2].why` 仍保留「（至多差平移）」这一旧措辞，与本步 text「单靠 t-正合不足」及 key_points[2]「等价加 t-正合才保持单对象，且不产生平移」矛盾；README 的 2026-11-18 修订也明令「删去平移」。

## 证据

- 同卡 steps[2].text: 「单靠 $t$-正合不足：一般 $t$-正合函子可以不保单对象」
- 同卡 key_points[2]: 「等价加 $t$-正合才保持单对象，且不产生平移」
- datasets/glc/README.md 2026-11-18 修订: 「删去平移」

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 1 处，JSON 变更 2 行；md 镜像同步 1 处

## 形式化提示

`t`-正合只给「单对象至多差平移」；要「保持单对象」必须再加范畴等价。形式化时把这两条作为两个独立引理。

## 防再犯

修订记录写「删去 X」时，必须全局 grep X；proof 的 why 是最容易漏的字段。
