# 由多胞体经法扇构造投影环面簇与丰除子

> `siebert/deriv/polytope-to-fan` ｜ track D ｜ draft

**目标**：由满维凸有理多胞体 $\Xi\subset M_\RR$ 造出环面簇 $X(\Xi)=X(\Sigma_\Xi)$，证明 $\Sigma_\Xi$ 完备当且仅当 $\Xi$ 有界，并把 $\Xi$ 的顶点写成分段线性函数 $\varphi$ 使 $\OO_X(D)=\OO_X(1)$ 丰，从而得到射影嵌入。

**自测**：一个多胞体怎样变成扇，又怎样保证造出的环面簇是投影的、并带一个丰除子？

## 前提

- $\Xi\subset M_\RR$ 是满维凸有理多胞体，$N=M^*$；$\Xi$ 的面指各维面，$\Xi^\circ$ 是极多胞体 $\{v\in N_\RR:\langle u,v\rangle\le1\ \forall u\in\Xi\}$（定义 4.13–4.14）。
- 对每个面 $\Xi'\subseteq\Xi$ 定义法锥 $\sigma_{\Xi'}=\{v:\langle u-u',v\rangle\ge0\ \forall u\in\Xi,u'\in\Xi'\}$，即 $\overline{\RR_{\ge0}\{u-u'\}}^\vee$（(4.96)）。
- 回收锥 $C(\Xi)=\overline{\{(m,h):h>0,\ m\in h\Xi\}}\subset M_\RR\times\RR$，以及 $\Xi$ 的顶点与极大锥的对应（(4.92)、§19–§20）。

## 步骤

1. **对每个面 $\Xi'$ 算出 $\sigma_{\Xi'} $，它是 $N_\RR$ 中的有理多面尖锥；把全体取负得 $\Sigma_\Xi=\{-\sigma_{\Xi'}:\Xi'\subseteq\Xi\ \text{面}\}$（(4.98)），称为 $\Xi$ 的法扇。**  
   为什么：取负是为了让锥指向「$\Xi'$ 的外法向」，这样锥与面反序对应（面越大锥越小），才符合扇的包含结构；$\sigma_{\Xi'}$ 由 $\Xi$ 的整点差生成，故有理。  
   锚点：原书 p.75 (4.96)、(4.98)（证据 A）

2. **验证 $\Sigma_\Xi$ 是扇：任取两面 $\Xi',\Xi''$，$\sigma_{\Xi'}\cap\sigma_{\Xi''}=\sigma_{\operatorname{conv}(\Xi'\cup\Xi'')}$ 型的关系成立，故交仍是某个面给出的锥，且取面封闭。**  
   为什么：扇的两条公理（定义 4.7）要求取面封闭、交为共同面；法锥的构造正好把「面的交」翻译成「锥的并/交」，这一步保证后面能粘合。  
   锚点：原书 p.75 §20（证据 B）

3. **完备性判别：$\Sigma_\Xi$ 完备 $\iff$ $\Xi$ 有界（命题 4.12(a)）；若 $0\in\operatorname{int}\Xi$，则 $\Sigma_\Xi=\{\{0\}\}\cup\{\RR_{\ge0}F:F\subsetneq\Xi^\circ\ \text{面}\}$（(4.99)），法扇就是极多胞体的面锥。**  
   为什么：有界意味着每个方向都有支撑面，故每个方向都落在某个法锥里；反之无界方向没有支撑面，对应锥缺失，扇不完备。  
   锚点：原书 p.75–76 命题 4.12（证据 A）

4. **定义 $X(\Xi)=X(\Sigma_\Xi)$（定义 4.15）。例：$\Xi=\conv\{0,e_1,\ldots,e_d\}$ 时 $X(\Sigma_\Xi)\simeq\PP^d$（(4.101)），$d=2$ 给 $\PP^2$，$d=3$ 给四面体对应的 $\PP^3$。**  
   为什么：这是检验定义是否合理的最小例子：单纯形应当给出射影空间，因为它的法扇正是 $\PP^d$ 的扇 $\RR_{\ge0}e_i,\RR_{\ge0}(-\sum e_i)$。  
   锚点：原书 p.76–77 定义 4.15、例 4.25（证据 A）

5. **给出射影实现：$\Proj k[C(\Xi)\cap(M\oplus\ZZ)]\simeq X(\Sigma_\Xi)$（命题 4.13）。证明是在 $\chi^{(v,1)}$ 处去齐次化，得到 $\Spec k[\sigma^\vee\cap M]$，即某个仿射图。**  
   为什么：$C(\Xi)$ 的整点环按 $\ZZ$ 分次后，齐次局部化恰好恢复每个法锥对应的仿射环面簇，于是 $\Proj$ 就是把它们粘起来的整体对象。  
   锚点：原书 p.77 命题 4.13（证据 A）

6. **读除子：$\Xi$ 的每个顶点 $v_i$ 对应一个极大锥 $\sigma_i$，令 $\varphi|_{\sigma_i}=v_i$ 线性延拓，得到 $\varphi\in\mathrm{PL}(\Sigma_\Xi)$；则 $D=\sum\varphi(v_i)D_i$ 满足 $\OO_X(D)=\OO_X(1)$，且 $\varphi$ 凸（顶点在边界，法锥在其上交叠），故 $\OO_X(D)$ 丰。**  
   为什么：这正是 (4.103) 的字典：满维有理多胞体 $\leftrightarrow$ (支撑凸的扇，有理严格凸分段线性函数)，顶点对应极大锥；命题 4.20 把「$\varphi$ 严格凸」翻译成「$\OO_X(D)$ 丰」。  
   锚点：原书 p.77 注 4.13、p.80 命题 4.20（证据 B）

7. **合起来：$\Xi$ 有界 $\Rightarrow$ $\Sigma_\Xi$ 完备 $\Rightarrow$ $X(\Xi)$ 固有；$\varphi$ 严格凸 $\Rightarrow$ $\OO_X(1)$ 丰 $\Rightarrow$ $X(\Xi)\hookrightarrow\PP^N$ 是闭嵌入，$X(\Xi)$ 投影。**  
   为什么：丰层给出到射影空间的闭嵌入（Stacks 01PR 的等价刻画），完备性给出固有性，两者合起来就是「投影环面簇」的完整含义。  
   锚点：原书 p.80 命题 4.20（证据 B）

## 结果

满维凸有理多胞体 $\Xi$ 给出法扇 $\Sigma_\Xi$、环面簇 $X(\Xi)=X(\Sigma_\Xi)$ 与同构 $X(\Xi)\simeq\Proj k[C(\Xi)\cap(M\oplus\ZZ)]$；$\Xi$ 有界时 $\Sigma_\Xi$ 完备，$X(\Xi)$ 是投影环面簇，顶点给出的分段线性函数 $\varphi$ 使 $\OO_X(D)=\OO_X(1)$ 丰。反向地，$\varphi\in\mathrm{PL}(\Sigma)$ 严格凸时以 Newton 多胞体 $\Xi(\Sigma,\varphi)$ 为原像，$\Xi\mapsto\Xi+m$ 对应 $\varphi\mapsto\varphi+m$。

## 缺口

- 命题 4.13 的证明讲义只写了「在 $\chi^{(v,1)}$ 处去齐次化」一句，未逐图验证 $\Proj$ 的粘合与 $X(\Sigma_\Xi)$ 的粘合一致。
- 并非每个扇都来自多胞体（注 4.14）：二维总是可以，三维及以上不然，反例是图 4.7 上方锥的三角剖分非正则；本卡不重建该反例。
- 严格凸性 $\leftrightarrow$ 丰性依赖命题 4.20 的事实 7、事实 8（折角与限制次数相等），讲义未证。

## 易错点

- 法扇必须取负号（(4.98)）：若直接用 $\sigma_{\Xi'}$ 而不取 $-\sigma_{\Xi'}$，得到的锥方向相反，与 $\PP^d$ 的标准扇对不上。
- 「多胞体有界」不是多余假设：无界多面体的法扇不完备（命题 4.12(a)），对应环面簇不固有，不能得到射影簇。
- 顶点对应极大锥、而非射线：把顶点错配到射线上会得到错误的分段线性函数，进而把丰除子算成分段线性但不凸的函数。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §20 由多面体构造环面簇，p.75–77（原书 p.75–77）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §25 丰环面除子，p.80–80（原书 p.80）

关联：`siebert/concept/fan`、`siebert/concept/divisor-class-group`、`siebert/deriv/toric-p2`、`siebert/concept/reflexive-polytope`、`siebert/concept/batyrev-mirror-construction`

来源说明：原书 p.75–77（(4.92)、(4.96)、(4.98)、(4.99)、(4.101)、(4.103)，命题 4.12–4.13，例 4.25–4.27）与 p.80（命题 4.20）。核过 nLab「polytope」（2024-06-30：凸 $k$ 多胞体、面与极多胞体的用法）与「toric variety」；丰给出闭嵌入的等价刻画用 Stacks tag/01PR。
