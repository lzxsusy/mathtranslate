# 02 局部 IC 层 $B_{\lambda,x}$（定义 4.8.1）与仿射 Grassmann 簇的比较

- 卡片：`glc/concept/b-lambda-ic`
- 失效模式：术语拼写
- 严重度：minor
- 确认链：A(A2)+arbiter-t1a
- 修复字段：`key_points[3]`、`pitfalls[0]`

## 错误版

- `key_points[3]`：局部 Laumon 公式里的 Tate 因子 $-n(\lambda)$ 不属于这个比较，它属于 Whittaker／Casselman–Shalala 归一化；因此 $B_{\lambda,x}$ 与 $A_\lambda$ 的对应里没有 $n(\lambda)$，只有 $dn$。
- `pitfalls[0]`：移位是 $dn$，不是 $n(\lambda)$：$n(\lambda)=\sum_i(i-1)\lambda_i$ 属 Whittaker／Casselman–Shalala 归一化，不在这个光滑拉回比较里出现。

## 正确版

- `key_points[3]`：局部 Laumon 公式里的 Tate 因子 $-n(\lambda)$ 不属于这个比较，它属于 Whittaker／Casselman–Shalika 归一化；因此 $B_{\lambda,x}$ 与 $A_\lambda$ 的对应里没有 $n(\lambda)$，只有 $dn$。
- `pitfalls[0]`：移位是 $dn$，不是 $n(\lambda)$：$n(\lambda)=\sum_i(i-1)\lambda_i$ 属 Whittaker／Casselman–Shalika 归一化，不在这个光滑拉回比较里出现。

## 为什么错

人名拼写错误：讲义与中译全篇都写 `Casselman–Shalika`（如 `glc.txt:488`、`ch03.tex:68`），卡写成 `Casselman–Shalala`。

## 证据

- glc.txt:488 与 ch03.tex:68/78/105/121、ch04.tex:157/169 均写 `Casselman–Shalika`

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 2 处，JSON 变更 4 行；md 镜像同步 2 处

## 形式化提示

人名类术语在形式化时不参与语义，但会污染检索与交叉引用；应作为词表项统一。

## 防再犯

术语表锁定 `Casselman–Shalika`；全文检索 `Shalala` 必须为 0。
