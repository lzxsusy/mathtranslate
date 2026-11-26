# 03 基础 Whittaker 层 W_k

- 卡片：`glc/concept/base-whittaker-sheaf`
- 失效模式：适用范围（限制 vs 茎）
- 严重度：minor
- 确认链：A(A3)+B(B2)
- 修复字段：`summary`

## 错误版

- `summary`：把 exp_ψ 从 Bun_{N_k} 直像到 Bun_k 得到的层；基础情形中 q_!j_{k,!}F_k 是 Av_E^d(W_k) 的茎。

## 正确版

- `summary`：把 exp_ψ 从 Bun_{N_k} 直像到 Bun_k 得到的层；基础情形中 q_!j_{k,!}F_k 是 Av_E^d(W_k) 限制到 C_k^{tor=0} 上的层。

## 为什么错

summary 说 `q_!j_{k,!}F_k` 是 `Av_E^d(W_k)` 的茎，但同卡 definition/定理/key_points[2]与 `ch06.tex:69` 都写成限制到 `C_k^{tor=0}` 的层；茎（stalk）是逐点取纤维，限制是取子叠上的截面，二者不同。

## 证据

- 同卡 definition/定理/key_points[2] 与 ch06.tex:69 均为 Av^d_E(W_k)|_{C_k^{tor=0}}（限制，不是茎）
- datasets/glc/README.md 2026-11-18 对 averaging-functor 同款修订「基础情形非茎」

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 1 处，JSON 变更 2 行；md 镜像同步 1 处

## 形式化提示

形式化时 `Av^d_E(W_k)|_{C_k^{tor=0}}` 与 `(Av^d_E(W_k))_x` 类型不同；summary 必须复用 definition 的表达式。

## 防再犯

summary 中出现的对象必须是 definition 中已定义的同一个表达式，不能换一种说法。
