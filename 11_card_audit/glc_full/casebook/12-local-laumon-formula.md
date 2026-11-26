# 12 Laumon 层的局部公式（命题 4.9.1）

- 卡片：`glc/concept/local-laumon-formula`
- 失效模式：术语拼写
- 严重度：minor
- 确认链：A(A2)+arbiter-t1a
- 修复字段：`definition.text`、`key_points[3]`、`theorems[0].proof.steps[7].why`、`theorems[0].proof.gap_note`

## 错误版

- `definition.text`：令 $V=E_x$ 为 $E$ 在 $x$ 处的纤维。对满足 $s\le n$ 的分拆 $\lambda=(\lambda_1\ge\cdots\ge\lambda_s>0)$，添零将其扩展为 $\operatorname{GL}(V)\simeq\operatorname{GL}_n$ 的优势权 $(\lambda_1,\ldots,\lambda_s,0,\ldots,0)$；令 $V^\lambda$ 为 $\operatorname{GL}(V)$ 中最高权为 $\lambda$ 的不可约最高权表示。等价地，若 $\chi^\lambda\in\operatorname{Irr}(S_d)$ 是与 $\lambda$ 对应的 Specht 表示，则 Schur–Weyl 对偶给出 $V^\lambda\simeq(V^{\otimes d}\otimes\chi^\lambda)^{S_d}$；若 $s>n$ 这个向量空间为零。置 $n(\lambda):=\sum_{i\ge1}(i-1)\lambda_i$，按通常的 Casselman–Shalala 归一化看作 $n(\lambda)=\langle\lambda,(0,1,\ldots,n-1)\rangle$。则对每个几何点 $x\in X$ 与整数 $d\ge0$，$\mathcal{L}_{E,x}^d[-d]\simeq\bigoplus_{\lambda\vdash d,\ \ell(\lambda)\le n}B_{\lambda,x}\otimes E_x^\lambda(-n(\lambda))$。
- `key_points[3]`：$n(\lambda)$ 是 Casselman–Shalala 归一化下的 Tate 指数：它不来自 IC 层本身（§4.10 的比较里只有 $dn$），而来自 Whittaker 归一化，正如 §3.4 局部 Whittaker 函数公式中的 $q_x^{-\sum_i(i-1)\lambda_i}$。
- `theorems[0].proof.steps[7].why`：$B_{\lambda,x}$ 的定义即 $\operatorname{IC}_{\overline{\operatorname{Tor}_x^\lambda}}$；Tate 扭转按 Casselman–Shalala 归一化补回。
- `theorems[0].proof.gap_note`：讲义在 §4.11 原位给出完整证明（引用经典 Springer 对应 [GPR20,AHJR14] 作为外部工具），无证明缺口；Tate 扭转的指数由 Casselman–Shalala 归一化给出。

## 正确版

- `definition.text`：令 $V=E_x$ 为 $E$ 在 $x$ 处的纤维。对满足 $s\le n$ 的分拆 $\lambda=(\lambda_1\ge\cdots\ge\lambda_s>0)$，添零将其扩展为 $\operatorname{GL}(V)\simeq\operatorname{GL}_n$ 的优势权 $(\lambda_1,\ldots,\lambda_s,0,\ldots,0)$；令 $V^\lambda$ 为 $\operatorname{GL}(V)$ 中最高权为 $\lambda$ 的不可约最高权表示。等价地，若 $\chi^\lambda\in\operatorname{Irr}(S_d)$ 是与 $\lambda$ 对应的 Specht 表示，则 Schur–Weyl 对偶给出 $V^\lambda\simeq(V^{\otimes d}\otimes\chi^\lambda)^{S_d}$；若 $s>n$ 这个向量空间为零。置 $n(\lambda):=\sum_{i\ge1}(i-1)\lambda_i$，按通常的 Casselman–Shalika 归一化看作 $n(\lambda)=\langle\lambda,(0,1,\ldots,n-1)\rangle$。则对每个几何点 $x\in X$ 与整数 $d\ge0$，$\mathcal{L}_{E,x}^d[-d]\simeq\bigoplus_{\lambda\vdash d,\ \ell(\lambda)\le n}B_{\lambda,x}\otimes E_x^\lambda(-n(\lambda))$。
- `key_points[3]`：$n(\lambda)$ 是 Casselman–Shalika 归一化下的 Tate 指数：它不来自 IC 层本身（§4.10 的比较里只有 $dn$），而来自 Whittaker 归一化，正如 §3.4 局部 Whittaker 函数公式中的 $q_x^{-\sum_i(i-1)\lambda_i}$。
- `theorems[0].proof.steps[7].why`：$B_{\lambda,x}$ 的定义即 $\operatorname{IC}_{\overline{\operatorname{Tor}_x^\lambda}}$；Tate 扭转按 Casselman–Shalika 归一化补回。
- `theorems[0].proof.gap_note`：讲义在 §4.11 原位给出完整证明（引用经典 Springer 对应 [GPR20,AHJR14] 作为外部工具），无证明缺口；Tate 扭转的指数由 Casselman–Shalika 归一化给出。

## 为什么错

同 b-lambda-ic：`Casselman–Shalala` 应为 `Casselman–Shalika`，本卡 4 处（definition、key_points、proof.steps、gap_note）。

## 证据

- 同 b-lambda-ic：讲义与中译全篇写 `Casselman–Shalika`

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 4 处，JSON 变更 8 行；md 镜像同步 4 处

## 形式化提示

同一错误在多个段落重复时，逐处修但只记一个失效模式；修完 grep 全卡计数应为 0。

## 防再犯

术语表统一；提交前对易错人名（Shalika、Drinfeld、Beilinson）做一次词表比对。
