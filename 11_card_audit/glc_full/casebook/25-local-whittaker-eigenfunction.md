# 25 指数符号：负 vs 非正

- 卡片：`glc/concept/local-whittaker-eigenfunction`
- 失效模式：符号/约定漂移
- 严重度：minor
- 确认链：lead+E1/E2（用户 m01466 授权后补核；原 A2 issue / B1 pass / arbiter-t1b issue 但只认 `verification.checks[2]`）
- 修复字段：`key_points[4]`、`verification.checks[2].asserts`、`verification.checks[2].verdict`

## 错误版

- `key_points[4]`：`……仅当 $\lambda$ 为有效优势权（$\lambda_n\ge 0$，如 $\lambda=(2,1,0)$）时各项非负、指数为负；……`
- `verification.checks[2].asserts`：`卡3 KP4：「λ 为优势权时各项非负，指数为负」`，verdict 为 `contradicts`。

## 正确版

- `key_points[4]`：`……仅当 $\lambda$ 为有效优势权（$\lambda_n\ge 0$，如 $\lambda=(2,1,0)$）时各项非负、指数非正（$\lambda=(c,0,\ldots,0)$、$c\ge 0$ 时恰为 $0$）；一般优势权指数可正可负（$n=2$、$\lambda=(0,-1)$ 时指数为 $+1$），这与 Casselman–Shalika 公式的指数约定一致。`
- `verification.checks[2]` 的 `asserts` 改写为修订后的 KP4，`verdict` 改为 `supports`（并保留旧判词针对旧表述的说明）。

## 为什么错

指数是 $-\sum_i(i-1)\lambda_i$。有效优势权只要求 $\lambda_1\ge\cdots\ge\lambda_n\ge0$；取 $\lambda=(c,0,\ldots,0)$（$c\ge0$）时 $\sum_i(i-1)\lambda_i=0$，指数恰为 $0$，并不严格为负。只有 $\lambda_2,\ldots,\lambda_n$ 中有非零分量时指数才严格为负。卡自己的 `verification.checks[2]` 已经记下 $P_n^+$ 没有 $\lambda_n\ge0$，且给出 $\lambda=(0,-1)$ 指数 $+1$ 的反例，说明「为负」的措辞在该卡内部也已站不住。

## 证据

- E1 glc.pdf p.21 L24：`W_{\gamma,x}(t_x^\lambda)=q_x^{-\sum_i(i-1)\lambda_i}\operatorname{Tr}(\gamma,V^\lambda)`，$\lambda$ 优势；$\lambda=(c,0,\ldots,0)$ 时指数为 $0$。
- E1 中译 ch03.tex:79：`q_x^{-\sum_i(i-1)\lambda_i}\Tr(\gamma,V^\lambda)`。
- E2 Casselman–Shalika, Compositio Math. 41 (1980) 207（numdam `CM_1980__41_2_207_0.pdf`）；BIRS 13w5154 幻灯片、Chhaibi ART 幻灯片用同一指数形状 $-\sum(i-1)\lambda_i$（相差归一化）。
- 卡内：`verification.checks[2]` 原文给出 $n=2$、$\lambda=(0,-1)$ 指数 $+1$ 的反例。

## 审计轨迹

- Pass A（A2）判 issue，字段 `key_points[4]`；Pass B（B1）pass；arbiter T1b 判 issue 但落在 `verification.checks[2]`，与 A 的字段不同 → 原记录为 `single_sided`。
- 用户 m01466 授权补核；lead 用 E1 p.21 公式与 CS 文献复核后修复 KP4，并同步 `verification.checks[2]`（与 `restricted-local-systems` 的陈旧 verification 同型）。
- 修复记录：`fix_log.json#followup`（3 处，JSON 变更 6 行）；md 镜像同步 2 处（verdict 不渲染，属预期 not_found）。

## 形式化提示

$n(\lambda)=\sum_i(i-1)\lambda_i$ 的零点恰在 $\lambda$ 只支撑于第一个坐标时（如 $(c,0,\ldots,0)$）；断言「指数为负」前先排除这个零元，改为「非正」或分情形。

## 防再犯

凡是「负 / 正 / 非零」这类符号断言，先找零元与边界例；正文改动后同步检查 `verification` 里是否还引用旧措辞（否则卡内自相矛盾）。
