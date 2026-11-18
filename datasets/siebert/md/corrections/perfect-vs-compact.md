# 「完美复形 ↔ 紧对象」方向写反

> `siebert/correction/perfect-vs-compact` ｜ 原书 p.98 ｜ draft

**一句话**：原文说「完美复形就是紧对象」（perfect $\Rightarrow$ compact），初版译文写成「紧对象是完美复形」，把蕴含方向颠倒；拟凝聚层导出范畴里紧性还需 qcqs 条件。

**自测**：「完美复形就是紧对象」与「紧对象是完美复形」，为什么在本章的语境里只有前者是对的？

## 初版

```
拟凝聚层导出范畴中的紧对象是完美复形。
```

## 改后

```
（一般而言，）拟凝聚层导出范畴中的完美复形就是紧对象；不过若从一开始就假定射影，所涉及的对象本来就都是紧的。
```

## 为什么改

这是数学事实，也是原文的蕴含方向。英文原文（原书 p.98）为 “In general, the perfect complexes are the compact objects. But if we are projective from the beginning, the objects are compact anyway.”，主语是 perfect complexes、谓语是 compact objects，即完美 $\Rightarrow$ 紧。nLab「perfect complex」条目（last revised 2016-01-02）的「Relation to compact objects」节写明：perfect modules 与 dualizable objects 一致，但一般并不等于 compact objects，「后者在拟紧拟分离概形上成立，是 Thomason、Neeman、Bondal–Van den Bergh 的工作」；同条并写「$A$ 上复形 $M_\bullet$ 完美当且仅当它是 $D(A)$ 的紧对象」。Stacks tag 08G4（完美复形）给出同样的刻画。译文把方向反过来后，「紧对象是完美复形」在一句话里就要用到 qcqs 与 Thomason–Neeman 定理，而这句话在原文中只是为下一句「射影情形下对象本来就都是紧的」作铺垫，方向必须与原文一致。

## 补注

位置在 §2.1 导出范畴的 Čech 模型，p.98 末（英文原文第 4549–4550 行），紧接 $D^b(X)=D^b(\operatorname{Coh}X)=\operatorname{Perf}(X)$（6.19）之后。它用来说明：一般情形下完美复形（局部可由有限自由复形表示）就是紧对象；但在射影情形下，$D^b(X)$ 的对象本来就是完美复形，于是本来就都是紧的——这正是 6.19 让 Čech 模型能只用局部自由复形作对象的原因。据本轮校对记录（校对/ch06.jsonl 第 1 条，applied=true），改动依据为 Stacks tag 08G4 与 nLab「perfect complex」。附带一点：原文 “In general” 本身也略宽——紧 = 完美在任意（非 qcqs）叠上并不成立，严格说应在 qcqs 概形上陈述；译文保留「一般而言」时宜理解为 qcqs 情形。

## 易错点

- 完美复形 $\Rightarrow$ 紧对象，反之在非 qcqs 的概形/叠上不成立；别把「iff」写进去。
- 「紧」是范畴性质（$\Hom$ 保持余积），「完美」是表示性质（局部同构于有限自由复形），两者不是定义上的同义词。
- 不要与 6.19 的 $\operatorname{Perf}(X)=D^b(X)$ 混为一谈：6.19 用的是 $X$ 光滑射影，而这句是一般性陈述。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，校订，p.98–98（原书 p.98）

关联：`siebert/concept/cech-model`、`siebert/concept/dg-category`

来源说明：原书 p.98（英文原文 4549–4550 行：the perfect complexes are the compact objects）；校对/ch06.jsonl 第 1 条（p.98 line105，applied）。nLab「perfect complex」（last revised 2016-01-02）核对 perfect 与 compact 的关系及 qcqs 条件；Stacks tag 08G4 核对完美复形的定义。
