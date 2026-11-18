# 虚拟基本类

> `siebert/concept/virtual-fundamental-class` ｜ track C ｜ draft

**一句话**：由完美障碍理论造出的类：把障碍锥用 Gysin 拉回，得到维数正确的『虚拟』基本类，用来定义 GW 不变量。

**自测**：为什么模空间的普通基本类不能定义 GW 不变量，虚拟类又补上了什么？

## 定义

设 $\pi:M\to S$ 是模问题。完美障碍理论是一项局部自由复形 $F^\bullet=[F^{-1}\to F^0]$ 连同 $\varphi^\bullet:F^\bullet\to L^\bullet_{M/S}$，使 $h^0$ 同构、$h^{-1}$ 满射（Def 3.5）。取 $\varphi^\bullet$ 的锥 $C_{\varphi^\bullet}\subset F_1$（3.91），虚拟基本类定义为\n$$[M]^{virt,\varphi^\bullet}:=s_0^![C_{\varphi^\bullet}]\in A_*(M).$$

记号：$L^\bullet_{M/S}$ 余切复形；$C_{\varphi^\bullet}$ 障碍锥；$M_{M/S}=[N_{M/Z}/T_{Z/S}|_M]$ 内蕴法层；$s_0$ 零截面；$A_*$ Chow 群。

## 要点

- 为什么普通基本类不行：模空间的实际维数 $\ge$ 虚拟维数，而且往往不在一般位置；$[M]$ 落在 $A_{\dim M}$，而 GW 不变量要在 $A_d$（$d=$ 预期维数）上积分。
- 障碍理论记录『形变—障碍』的线性化：$T^1-T^2$ 的差就是实际维数与虚拟维数之差，$F^\bullet$ 的两项分别对应形变与障碍。
- 内蕴法锥与嵌入无关（Lemma 3.8）：$0\to T_{Z/S}|_M\to F_0\oplus C_{M/Z}\to C_{\varphi^\bullet}\to0$ 使 $C_{\varphi^\bullet}$ 不依赖辅助的 $Z$，故虚拟类是 $M$ 上的类。
- Thm 3.10：$M_{M/S}$ 是泛的、最小的障碍理论；任何完美障碍理论都通过它分解，故『最小障碍理论』给出典范的虚拟类。
- GW 情形：$\varphi^\bullet:R\pi_*(f^*\Omega_X\otimes\omega_\pi)\to L^\bullet_{M/m}$ 由迹映射给出（3.106），Lemma 3.11 用相对丰线丛 $L=\omega(x)\otimes f^*\mathcal O(1)^{\otimes3}$ 证明它可以换成两项局部自由复形。

## 公式

$$[M]^{virt,\varphi^\bullet}=s_0^![C_{\varphi^\bullet}]\in A_*(M)$$
$$0\to T_{Z/S}|_M\to F_0\oplus C_{M/Z}\to C_{\varphi^\bullet}\to0$$
$$\varphi^\bullet:R\pi_*(f^*\Omega_X\otimes\omega_\pi)\longrightarrow L^\bullet_{M/m}$$
$$M_{M/S}=[N_{M/Z}/T_{Z/S}|_M],\qquad M_{M/S}\hookrightarrow h^0(F^\bullet)/h^1(F^\bullet)$$

## 定理与证明

### Thm 3.10：内蕴法层是泛障碍理论

内蕴法层 $M_{M/S}$ 是泛的、最小的障碍理论：对任何完美障碍理论 $\varphi^\bullet:F^\bullet\to L^\bullet_{M/S}$，都存在态射 $F^\bullet\to M_{M/S}$ 使之分解；且 $M_{M/S}$ 在同构意义下唯一。

（sketch；来源：原书 p.54–56（Lemma 3.8、3.91–3.102、Thm 3.10））

1. 先证 $M_{M/S}$ 与局部嵌入 $M\subset Z$ 无关：换一个嵌入时 $N_{M/Z}$ 与 $T_{Z/S}|_M$ 同时变化，其商不变（Lemma 3.8）。  
   为什么：只有与嵌入无关的量才能定义在 $M$ 上，这是虚拟类良定义的前提。
2. 把任意 $\varphi^\bullet$ 与内蕴法层比较：$h^0$ 同构 + $h^{-1}$ 满射给出 $M_{M/S}\hookrightarrow h^0/h^1(F^\bullet)$ 的单态射（3.96）。  
   为什么：这个单态射就是『$\varphi^\bullet$ 通过最小障碍理论分解』的精确形式。
3. 最后用 $s_0^!$ 把锥的类拉回到 $M$，得 $[M]^{virt}\in A_*(M)$，并在 $M$ 光滑时化为 $c_{top}(F^0)/c_{top}(F^{-1})$ 型表达式。  
   为什么：Gysin 拉回 $s_0^!$ 把 $C_{\varphi^\bullet}$ 的类降到 $M$ 上，次数正好是虚拟维数。

缺口：讲义把 3.96 的单态射判据与 Thm 3.10 的泛性作为结论给出，未写出与 $Z$ 无关性的完整验证。

### Prop 3.9：完美障碍理论的等价刻画

$F^\bullet\to L^\bullet_{M/S}$ 是完美障碍理论 $\iff$ $M_{M/S}\hookrightarrow h^0(F^\bullet)/h^1(F^\bullet)$ 是单态射（且 $F^\bullet$ 为两项局部自由）。

（sketch；来源：原书 p.56（Prop 3.9））

1. 必要性：由 $h^0$ 同构、$h^{-1}$ 满射，把 $M_{M/S}$ 的每个截面提升到 $F^\bullet$ 上，得到单态射。  
   为什么：单态射正是『障碍理论不比内蕴法层多出多余信息』的表述。
2. 充分性：反向用五引理/长正合列把 $h^0,h^{-1}$ 的条件从单态射读回来。  
   为什么：两项复形的上同调只有 $h^0,h^{-1}$ 两个，单态射恰好控制这两项。

缺口：讲义只给判据，验证留给读者；本卡把它列为 sketch。

## 易错点

- 虚拟类依赖所选的障碍理论 $\varphi^\bullet$，不是只依赖 $M$；不同的障碍理论可以给出不同的类（虽然『最小障碍理论』给出典范选择）。
- 『完美』指复形只有两项且局部自由；一般模问题的障碍是无穷维的，必须先截断或用相对丰线丛把它化成两项。
- 积分在 $A_d$（虚拟维数）而不是 $A_{\dim M}$；混用会得到 0 或无意义的数。
- $C_{\varphi^\bullet}$ 与 $Z$ 无关（Lemma 3.8），但构造时仍要先选一个局部嵌入 $M\subset Z$，别把『无关』当成『不用选』。
- 虚拟类不是基本类的推前：一般情况下没有从 $C_{\varphi^\bullet}$ 到 $M$ 的自然『基本类』映射，必须用 $s_0^!$。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 3 章 §2 超曲面的亏格零 Gromov–Witten 不变量，p.46–46（原书 p.46）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 3 章 §4 障碍理论与虚拟基本类，p.52–56（原书 p.52–56）

关联：`siebert/concept/gromov-witten-invariant`、`siebert/concept/stack`、`siebert/concept/deligne-mumford-stack`

来源说明：原书 p.46（Kontsevich 的 Chern 类版本，作为虚拟类的第一个显式例子）、p.51–56（相交论回顾、Def 3.5、Lemma 3.8、Prop 3.9、Thm 3.10、3.102）。nLab「virtual fundamental class」（last revised 2015-08-15）核过定义与 Behrend–Fantechi 的障碍理论表述；Stacks Project Ch. 93「Deformation Problems」(tag 0DVK) 已核对章节标题（未逐节比对）。
