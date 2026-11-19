# 原文 p.9：$dq$ 的右端应落在 $p$ 上

> `functoriality/correction/d18-floer-differential-index` ｜ 原书 p.9 ｜ draft

**一句话**：$S^2$ 大圆例子里 $dq=T^aq+T^aq=0$ 的右端应为 $T^ap+T^ap$，否则微分不改变生成元类型。

**自测**：$dp$ 落在 $q$ 上，$dq$ 为什么也写成落在 $q$ 上？

## 初版

```
$dq = T^a q + T^a q = 0$
```

## 改后

```
$dq = T^a p + T^a p = 0$
```

## 为什么改

$d$ 把生成元 $p$ 送到 $q$、把 $q$ 送到 $p$：绿色带贡献 $dp$、橙色带贡献 $dq$（图 4）；若 $dq$ 也落在 $q$ 上，$d$ 就不改变生成元类型。

## 补注

中译本照录原文，并在式 (17) 后加译者按。

## 易错点

- $d$ 在 $p$ 与 $q$ 之间来回切换，两条带分别贡献 $dp$ 与 $dq$。
- 不要因为两行形式对称就照抄同一右端。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§2.1，p.9–9（原书 p.9）

关联：`functoriality/concept/floer-cohomology`、`functoriality/deriv/floer-d-squared`

来源说明：英文底本 prelim.tex 式 (17)（A 级）；对照图 4 的绿/橙带与「$dq$ 由橙色带贡献」的说明。
