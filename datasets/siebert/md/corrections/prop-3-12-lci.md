# 命题 3.12：假设从「局部完全交」被收窄成「光滑」

> `siebert/correction/prop-3-12-lci` ｜ 原书 p.58 ｜ draft

**一句话**：讲义原文假设是局部完全交，初版译成「光滑从而为局部完全交」，把命题的适用范围改小了。

**自测**：命题 3.12 的假设被译成「光滑」而不是「局部完全交」，会让命题少覆盖哪些情形？

## 初版

```
「若 $S$ 光滑，从而为局部完全交」
```

## 改后

```
「若 $S$ 是局部完全交（例如光滑）」
```

## 为什么改

讲义 p.58 的假设只有一句：Proposition 3.12. If $S$ is lci, then for all $s,s'$ ...（orig_full.txt 行 2762）。lci 即局部完全交，是一个比光滑更弱的条件：光滑态射自动是 lci（Stacks §42.59 里 $f^!=i^!\circ g^*$ 的分解对光滑 $g$ 成立），反之不然——结点曲线、$\PP^2$ 中两条相交直线之并、$\Spec k[\epsilon]/(\epsilon^2)$ 上的族都是 lci 而非光滑。因此把假设写成「$S$ 光滑」是\emph{加强}假设：命题在更强假设下仍然成立，但覆盖的情形变少了，而形变不变性的典型用途恰恰是 $S$ 取（可能带结点的）曲线、比较两根纤维 $X_s,X_{s'}$ 的 GW 不变量。讲义另一个前提「$s,s'$ 同属一个连通分支」则是对「代数等价要靠 $S$ 内连接两点的曲线」的补充说明，属译本增补，不构成错误。

## 补注

校订层级：译文修订（初版译法 → 改后译法），非讲义笔误。三校汇总 §3 主控改判：按原文口径重写，「lci 是原文假设，应保留原文的普适性，把光滑降为例」，现译见 ch03.tex:406「若 $S$ 是局部完全交（例如光滑）」。校对记录 ch03.jsonl 该条原为 applied=false、severity mid，理由「原文仅 If S is lci……略窄于原文但结论正确，建议主控复核」；本轮按改判落地。相邻的「同一连通分支」为补充条件，另见 expected-dimension 卡，此处不单独立卡。

## 易错点

- 这不是「结论错」的勘误：加强假设后命题仍真，错的是适用范围——读者会以为只有光滑族才有形变不变性。
- 别把 lci 与光滑互换着用：讲义 p.50–51 只为 lci 嵌入定义 Gysin 拉回（(3.58) 在 p.50，(3.64) 在 p.51），而 Prop 3.12 的 $j_s^!$ 正需要这个工具；光滑只是充分条件。
- 讲义原文也没有「同一连通分支」这一条：若把补充条件当原文条件引用，会误判原文的强度。
- 「光滑 ⇒ lci」不能反推：结点曲线是 lci 而非光滑的典型例子，也正是形变不变性最想用的场景。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 3 章 校订，p.58–58（原书 p.58）

关联：`siebert/concept/expected-dimension`、`siebert/correction/local-isomorphic`、`siebert/concept/gysin-map`

来源说明：原书 p.58（Prop 3.12 原文「If $S$ is lci」）；对照片 p.50–52 的 Gysin 拉回 (3.58)(3.64) 与 lci 适用边界。Stacks tag 0FEZ（§42.59 Gysin maps for local complete intersection morphisms）核过「光滑是 lci 的特例」这一方向；lci 与光滑的分离例子（结点曲线、相交直线之并、$\Spec k[\epsilon]/(\epsilon^2)$）属标准交换代数事实，未指定外部条目。
