# 23 系数域写成底域 $k$

- 卡片：`glc/concept/deligne-gl1-existence`
- 失效模式：术语/系数域混淆
- 严重度：minor
- 确认链：lead+E1/E2（用户 m01466 授权后补核；原 A1 issue / B1 pass / arbiter-t1b pass，属单方发现）
- 修复字段：`definition.notation`

## 错误版

- `definition.notation`：`$\operatorname{Shv}(\operatorname{Spec} k)$：$k$-向量空间（分次）构成的层范畴，其对象张量到 $\operatorname{Pic}_{X/k}$ 上的层不改变特征值。`

## 正确版

- `definition.notation`：`$\operatorname{Shv}(\operatorname{Spec} k)$：系数域 $e$ 上的（分次）向量空间构成的层范畴（$\ell$-进情形 $e=\overline{\mathbb{Q}}_{\ell}$；底域 $k=\mathbb{F}_q$ 不充当系数域），其对象张量到 $\operatorname{Pic}_{X/k}$ 上的层不改变特征值。`

## 为什么错

`definition.text` 已声明 $X$ 是 $k=\mathbb{F}_q$ 上的曲线，因此同一个 $k$ 是**底域**；而 $\operatorname{Shv}(\operatorname{Spec} k)$ 的对象是带系数域作用的（分次）向量空间。原书在 p.7 先把系数域固定为代数闭域 $e$，$\ell$-进情形即 $e=\overline{\mathbb{Q}}_\ell$。把系数域写成 $k=\mathbb{F}_q$ 会让读者以为可以拿任意 $\mathbb{F}_q$-向量空间去张量，从而破坏「保持特征值」这一唯一性陈述的前提。

## 证据

- E1 glc.pdf p.7 L22–24：`Fix a reasonable sheaf theory with algebraically closed coefficient field e.`
- E2 nLab `l-adic cohomology`：$H^j_{\mathrm{et}}(X_{\bar k},\mathbb{Q}_\ell):=\varprojlim H^j_{\mathrm{et}}(X_{\bar k},\mathbb{Z}/\ell^n\mathbb{Z})\otimes\mathbb{Q}_\ell$，且「Fix $\ell$ a prime number different from the characteristic of $k$」——系数是 $\mathbb{Q}_\ell$，底域是 $k$。
- E2 nLab `geometric class field theory`：理论对任意常值完全域 $k$ 表述，可为特征 0（如 $\mathbb{C}$），底域不兼作系数域。
- 卡内：`definition.text` 固定 $k=\mathbb{F}_q$；`definition.notation` 的「$k$-向量空间」与之冲突。

## 审计轨迹

- Pass A（A1）判 issue，字段 `definition.notation`；Pass B（B1）pass；arbiter T1b pass → 按协议记为 `single_sided`，第一轮未修。
- 用户 m01385 要求对英文原本再核；lead 重读 glc.pdf p.7 后确认底本用 $e$ 作系数域，m01466 授权按 E1+E2 修复。
- 修复记录：`fix_log.json#followup`（1 处，JSON 变更 2 行）；md 镜像同步 1 处。

## 形式化提示

审计定义记号时把「底域 / 系数域」当两个独立变量：`Shv(Spec k)` 的形状是「系数域 $e$ 上的分次对象」，$k$ 只决定几何（Frobenius、$\operatorname{Pic}_{X/k}$ 的 $k$-结构）。

## 防再犯

凡是记号里出现「$k$-向量空间」，先查本卡是否已把 $k$ 用作底域；$\ell$-进系数一律写成 $e$（或 $\overline{\mathbb{Q}}_\ell$），不写 $k$。
