# 「$K$ 值点的集合」漏译「（即概形论意义下的点）」

> `siebert/correction/k-valued-points` ｜ 原书 p.62 ｜ draft

**一句话**：初版把「$K$ 值点的集合」直接译出，漏掉原文括注「the scheme theoretic points」；补回后才不会被读成 $X$ 的普通点集。

**自测**：为什么「$K$ 值点的集合」后面必须保留「（即概形论意义下的点）」这个括注？

## 初版

```
可以考虑 $K$ 值点的集合。
```

## 改后

```
可以考虑 $K$ 值点的集合（即概形论意义下的点）。
```

## 为什么改

讲义原文为「we can form the set of $K$-valued points (the scheme theoretic points)」，括注是有意的限定。按 (4.15)，$X(K)=\Hom_k(\Spec K,X)=\{(x,\iota):\iota:\kappa(x)\hookrightarrow K\}$，一个 $K$ 值点是「一个点连同它的剩余域到 $K$ 的嵌入」，不是 $X$ 的拓扑点本身；漏掉括注，「$K$ 值点」容易与「$X$ 的点」混同，进而误读 Note 4.4（$k$ 代数闭且有限型时 $X(k)$ 才是闭点集）。nLab 与 Stacks 对 $K$-points 的处理同样是「$\Spec K\to X$ 的态射」，与 $X$ 的点集区分。

## 补注

只补括注，不改 (4.15) 的公式与 Note 4.4 的陈述。这句话出现在 §6「$k$ 有理点」开头，是为下一段的 $X(K)=\Hom_k(\Spec K,X)$ 做铺垫，括注承担的就是「不要把它当成普通点」的提示功能。

## 易错点

- 不要把括注改写成「即 $X$ 的点」或「即闭点」：前者混淆两个概念，后者只在 $k$ 代数闭且有限型时才成立。
- 也不要把「$K$ 值点」统一译成「有理点」：$K=k$ 时才是 $k$ 有理点，一般 $K$ 是扩张时不是。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，校订，p.62–62（原书 p.62）

关联：`siebert/concept/affine-toric-variety`、`siebert/concept/monoid`

来源说明：原书 p.62 §6 开头与 (4.15)；据讲义原文括注（orig_full.txt 第 2956 行）核过，概念上核 nLab「rational point」与 Stacks 对 $K$-points 的用法。
