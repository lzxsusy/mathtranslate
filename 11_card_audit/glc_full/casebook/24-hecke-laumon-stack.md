# 24 短正合列「任两者决定第三」

- 卡片：`glc/concept/hecke-laumon-stack`
- 失效模式：内部不一致（数学断言）
- 严重度：minor
- 确认链：lead+E1/E2（用户 m01466 授权后补核；原 A4 issue / B3 pass / arbiter-t1a pass，属单方发现）
- 修复字段：`key_points[0]`

## 错误版

- `key_points[0]`：`一个点就是一条短正合列：$M'$ 是子层、$M$ 是大层、$\mathcal T$ 是长度 $d$ 的挠商；三者互相决定其中之二。`

## 正确版

- `key_points[0]`：`一个点就是一条短正合列：$M'$ 是子层、$M$ 是大层、$\mathcal T$ 是长度 $d$ 的挠商；已知 $M$ 与 $\mathcal T$（或 $M$ 与 $M'$）时第三个由正合列确定，但只知 $(\mathcal T,M')$ 时 $M$ 还要额外选取 $\operatorname{Ext}^1(\mathcal T,M')$ 中的一个类，通常并不唯一（如 $\mathcal T=\mathcal O_x$ 时 $\operatorname{Ext}^1(\mathcal O_x,M')\cong M'|_x$，可以多于一个）。`

## 为什么错

短正合列 $0\to M'\to M\to\mathcal T\to0$ 中，$(M',M)$ 决定 $\mathcal T=M/M'$，$(M,\mathcal T)$ 决定 $M'=\ker(M\to\mathcal T)$；但 $(\mathcal T,M')$ 只决定一个 $\operatorname{Ext}^1(\mathcal T,M')$-torsor，$M$ 还要选一个扩张类。$\mathcal T=\mathcal O_x$ 时 $\operatorname{Ext}^1(\mathcal O_x,M')\cong M'|_x$，只要 $M'$ 在 $x$ 的纤维非零就有多个选择。这个非唯一性正是 Hecke–Laumon 叠作为对应非平凡的原因；若 $(\mathcal T,M')$ 真能决定 $M$，叠会退化成 $\operatorname{Tor}^d\times\operatorname{Coh}_k$。同卡 `pitfalls[1]` 已经写过「忘记 $M'$ 会丢掉子层信息，无法还原 $M$」，与本句直接矛盾。

## 证据

- E1 glc.pdf p.45–46：`HL_k^d := {0 → M′ → M → T → 0 | M, M′ ∈ Coh_k, T ∈ Tor^d}` 以及两条腿；原文把 $M$ 列为叠对象的组成部分，从未说任两者决定第三。
- E2 CAG 2001（`CAG-2001-0009-0004-a003.pdf`）：`s = dim Ext^1(O_x, L) > 1. They will be parametrized by a projective space P^{s-1}.` —— 固定 $(\mathcal T=\mathcal O_x, M'=L)$ 后中间项成一族 $\mathbb{P}^{s-1}$。
- E2 nLab `extension`：`Q` 被 `K` 的扩张就是短正合列 $K\to X\to Q$，扩张由 Ext 分类。
- 卡内：`pitfalls[1]`（忘记 $M'$ 无法还原 $M$）与错误版自相矛盾。

## 审计轨迹

- Pass A（A4）判 issue，字段 `key_points[0]`；Pass B（B3）pass；arbiter T1a pass → 记为 `single_sided`，第一轮未修。
- 用户 m01466 授权补核；lead 取 E1 p.45–46 与 CAG 2001 的 Ext¹ 参数化证据后修复。
- 修复记录：`fix_log.json#followup`（1 处，JSON 变更 2 行）；md 镜像同步 1 处。

## 形式化提示

Hecke–Laumon 叠的对象应写成三元组 $(M',M,\mathcal T)$ 连同正合列，而不是「由两元决定」；判断「任两者决定第三」时，先问第三项是不是一个 Ext 类。

## 防再犯

遇到「三者互相决定其中之二」这类对称断言，逐对检查：两端的映射是否单值、中间项是否只在 Ext 的 torsor 意义下确定。卡内已有相反提示（pitfalls）时，要点必须与之一致。
