# $\Theta$ 图的自同构群

> `pi/example/theta-automorphisms` · 轨道 E · 微扰与代数结构 · 状态 draft

> **这张卡练什么**：两个顶点、三条平行边的图上，究竟能有多少种保持全部结构的对称？

## 一句话

$\Theta$ 图的自同构共 $12$ 个：交换两顶点或轮换三条边，两者独立，合起来是 $\mathbb{Z}_2\times S_3$。

## 设定

取例 2.8.7 的 $\Theta$ 图（两个顶点、三条平行边）：顶点 $V=\{1,2\}$，半边 $HE=\{a,b,c,a',b',c'\}$，边 $E=\{(a,a'),(b,b'),(c,c')\}$，关联映射 $i(a)=i(b)=i(c)=1$、$i(a')=i(b')=i(c')=2$，两顶点度数都是 $3$。自同构是一对双射 $(\sigma_V,\sigma_{HE})$，满足：每条边映成边，且与关联映射相容 $i\circ\sigma_{HE}=\sigma_V\circ i$、$\iota\circ\sigma_{HE}=\sigma_{HE}\circ\iota$（$\iota$ 把半边换成同一条边的另一半边（非自环时落在另一顶点））。书上给出两个例子① ②，并断言 $\operatorname{Aut}(\Gamma)=\mathbb{Z}_2\times S_3$；本例要把这 $12$ 个元素数清楚。

## 计算

**第 1 步**：先把边条件翻译成「配对」条件：三条边 $\{a,a'\},\{b,b'\},\{c,c'\}$ 互不相交地划分六个半边，故 $\sigma_{HE}$ 诱导三条边的置换 $\pi\in S_3$；顶点条件则规定 $\sigma_{HE}$ 把 $\{a,b,c\}$ 送到 $\{a,b,c\}$ 或送到 $\{a',b',c'\}$。

> 为什么：边条件是「集合层面」的置换，顶点条件决定这个置换落在两个分支里的哪一个；分开数才不会重复。

**第 2 步**：分支 A（$\sigma_V=\mathrm{id}$）：$\{a,b,c\}\mapsto\{a,b,c\}$，$\{a',b',c'\}\mapsto\{a',b',c'\}$。此时 $\sigma_{HE}$ 完全由 $\pi\in S_3$ 决定：$a_j\mapsto\pi(a_j)$，$a'_j\mapsto(\pi(a_j))'$，共 $6$ 个。

> 为什么：边 $\{a_j,a'_j\}$ 必须映到边 $\{\pi(a_j),(\pi(a_j))'\}$，这迫使 $a'_j$ 按同一个 $\pi$ 走；反过来任意 $\pi$ 都保结构，故不多不少。

**第 3 步**：分支 B（$\sigma_V=(1\,2)$）：$\{a,b,c\}\mapsto\{a',b',c'\}$，于是 $a_j\mapsto(\pi(a_j))'$、$a'_j\mapsto\pi(a_j)$，同样由 $\pi\in S_3$ 决定，共 $6$ 个。

> 为什么：分支 B 只是把每个半边的落点换成它的伙伴，边的像仍是边；条件与分支 A 逐字对称，所以计数相同。

**第 4 步**：两个分支合起来 $6+6=12$ 个。分支 A 的 $\pi=\mathrm{id}$ 给出恒等，$\pi=(a\,b\,c)$ 正是书上②；分支 B 取 $\pi=\mathrm{id}$ 即书上①（把每个半边送到伙伴）。

> 为什么：把元素与书上的两个显式例子对上，才知道数的确实是同一个群，而不是一个更大的群。

**第 5 步**：结构上，分支 A 是 $S_3$，分支 B 是 $s\cdot S_3$（$s$ 为换顶点、$a_j\mapsto a'_j$）；逐半边可验 $s\pi s=\pi$，故 $s$ 与整个 $S_3$ 交换，$\operatorname{Aut}(\Gamma)\cong\mathbb{Z}_2\times S_3$。

> 为什么：直积要求两个因子互不影响；$s$ 只交换伙伴名称，不改变三条边的轮换方式，所以才能写成直积。

## 结果

$|\operatorname{Aut}(\Gamma)|=2\cdot 6=12$，且 $\operatorname{Aut}(\Gamma)\cong\mathbb{Z}_2\times S_3$：$\mathbb{Z}_2$ 因子来自两个顶点的交换，$S_3$ 因子来自三条边的轮换；$|\operatorname{Aut}|$ 与书上一致。

## 复核

逐条核对书上①：$\sigma_V=(1,2)$、$\sigma_{HE}:(a,b,c,a',b',c')\mapsto(a',b',c',a,b,c)$，则 $\{a,a'\}\mapsto\{a',a\}$、$\{b,b'\}\mapsto\{b',b\}$ 等，三条边都映成边 ✓。再核②：$\sigma_V=\mathrm{id}$、$\sigma_{HE}:(a,b,c,a',b',c')\mapsto(b,c,a,b',c',a')$，边 $\{a,a'\}\mapsto\{b,b'\}$、$\{b,b'\}\mapsto\{c,c'\}$、$\{c,c'\}\mapsto\{a,a'\}$ ✓，且半边的伙伴关系不被破坏 ✓。最后核阶：$12=2\cdot6$ 与 $\mathbb{Z}_2\times S_3$ 相符，且与「$2$ 种顶点安排 $\times$ 三条边的 $6$ 种轮换」的直积解释一致。

## 易错点

- 自同构是半边置换与顶点置换的一对，必须满足 $i\circ\sigma_{HE}=\sigma_V\circ i$；只写出一个半边置换、不再确认顶点条件，很容易数进不保关联的映射。
- 书上①的箭头顺序是 $(a,b,c,a',b',c')\mapsto(a',b',c',a,b,c)$，不要读成 $(a,a',b,b',c,c')$：后者不保边 $\{a,a'\}\mapsto\{a,b\}$。
- 「$\mathbb{Z}_2$ 换顶点」不只是交换两个顶点：它同时把 $a,b,c$ 送到 $a',b',c'$，把三个半边整体搬到另一侧。

## 用到哪些概念

- [费曼图的组合定义与展开公式](../concepts/feynman-diagrams.md)

## 相关卡

- [Θ 图的顶点、半边与边](../examples/theta-graph.md)
- [两个自环加一条连边图的自同构群](../examples/vacuum-graph-automorphisms.md)

## 出处

- §2.8.3 例 2.8.7（图与自同构），p.143–144（PDF p.144–145），源码 `ch02c.tex:371-395`
