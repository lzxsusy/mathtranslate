# 费曼图的组合定义与展开公式

> `pi/concept/feynman-diagrams` · 轨道 E · 微扰与代数结构 · 状态 draft

> **先自测**：为什么费曼图展开中每个图要除以 $|\operatorname{Aut}(\Gamma)|$，而写成指数后只剩连通图？

## 一句话

把含三次相互作用的积分按 $\lambda$ 展开，每阶写成三价图的求和：顶点给 $I_{ijk}$、边给 $(Q^{-1})^{ij}$，按自同构群大小除重；取指数后只剩连通图。

## 定义

这里的「图」不是画出来的线条，而是一组组合数据：顶点集 $V(\Gamma)$；半边集 $HE(\Gamma)$；关联映射 $i_{\Gamma}:HE(\Gamma)\to V(\Gamma)$，说明每条半边附着在哪个顶点；$HE(\Gamma)$ 上的一个完美匹配 $E(\Gamma)$，匹配中的每一对叫作一条边；以及顶点 $v$ 的度数 $\#i_{\Gamma}^{-1}(v)$，即附在 $v$ 上的半边个数。两条边可以连接同一对顶点（平行边），图的拓扑完全由匹配与关联映射决定，与画法无关。

**记号约定**：$V(\Gamma)$ 顶点集；$HE(\Gamma)$ 半边集；$E(\Gamma)$ 半边上的完美匹配（边集）；$i_{\Gamma}$ 关联映射；$\operatorname{Aut}(\Gamma)$ 为自同构群；$|E(\Gamma)|$、$|V(\Gamma)|$ 分别为边数与顶点数，$l(\Gamma)$ 为圈数。

## 要点

- 定义 2.8.4 把图拆成顶点、半边、关联映射与半边上的配对四件数据，度数由关联映射的原像个数读出。
- 定义 2.8.6 的同构要求一对双射同时保持关联映射与配对；$\operatorname{Aut}(\Gamma)$ 就是 $\Gamma$ 到自身的这种双射对之群。
- 三次相互作用使每个顶点度数都是 3：$m$ 个顶点有 $3m$ 条半边、$\frac{3m}{2}$ 条边，故圈数 $l(\Gamma)=\frac{m}{2}+1$。
- 第 $m$ 阶系数 $\frac{1}{m!(3!)^{m}}\langle I^{m}\rangle_{x}$ 按 $G=S_{m}\times(S_{3})^{m}$ 的轨道重组，商掉 $|G|$ 后每个同构类贡献 $\omega_{\Gamma}/|\operatorname{Aut}(\Gamma)|$。
- 命题 2.8.10 的指数形式说明：取对数消掉不连通图，连通图的圈数决定 $\hbar$ 的幂次 $l(\Gamma)-1$。

## 关键公式

$$
\left\langle e^{\frac{\lambda}{3!\hbar}I(x)}\right\rangle_{x}=\sum_{\Gamma:\ \text{三价}}\hbar^{|E(\Gamma)|-|V(\Gamma)|}\,\lambda^{|V(\Gamma)|}\,\frac{\omega_{\Gamma}}{|\operatorname{Aut}(\Gamma)|}
$$

$$
\frac{1}{m!\,(3!)^{m}}\langle I(x)^{m}\rangle_{x}=\sum_{\Gamma:\ |V(\Gamma)|=m}\frac{\omega_{\Gamma}}{|\operatorname{Aut}(\Gamma)|}\,\hbar^{|E(\Gamma)|}
$$

$$
\omega_{\Gamma}=\sum_{i_{1},j_{1},k_{1},i_{2},j_{2},k_{2}}I_{i_{1}j_{1}k_{1}}I_{i_{2}j_{2}k_{2}}(Q^{-1})^{i_{1}i_{2}}(Q^{-1})^{j_{1}j_{2}}(Q^{-1})^{k_{1}k_{2}}
$$

$$
l(\Gamma)=|E(\Gamma)|-|V(\Gamma)|+1=1-\chi(\Gamma)
$$

$$
\left\langle e^{\frac{\lambda}{3!\hbar}I(x)}\right\rangle_{x}=\exp\left(\sum_{\Gamma:\ \text{连通三价}}\lambda^{|V(\Gamma)|}\,\hbar^{l(\Gamma)-1}\,\frac{\omega_{\Gamma}}{|\operatorname{Aut}(\Gamma)|}\right)
$$

## 定理与证明

### 费曼图展开公式（命题 2.8.10）

作为形式幂级数，$\left\langle e^{\frac{\lambda}{3!\hbar}I(x)}\right\rangle_{x}=\sum_{\Gamma:\ \text{三价}}\hbar^{|E(\Gamma)|-|V(\Gamma)|}\lambda^{|V(\Gamma)|}\frac{\omega_{\Gamma}}{|\operatorname{Aut}(\Gamma)|}=\exp\left(\sum_{\Gamma:\ \text{连通三价}}\lambda^{|V(\Gamma)|}\hbar^{l(\Gamma)-1}\frac{\omega_{\Gamma}}{|\operatorname{Aut}(\Gamma)|}\right)$。

**证明提纲**

1. 把 $\langle I^{m}\rangle_{x}$ 用威克定理写成对完美匹配的求和，再让 $G=S_{m}\times(S_{3})^{m}$ 作用在匹配集上，按轨道归并。
   - *为什么*：匹配与图的标号方式一一对应，按轨道归并正好消掉标号带来的重复计数。
2. 每条轨道贡献 $\frac{|G|}{|\operatorname{Aut}(\Gamma)|}\omega_{\Gamma}\hbar^{|E(\Gamma)|}$，除以 $|G|$ 后得按同构类求和的式子。
   - *为什么*：同构类的大小是 $|G|/|\operatorname{Aut}(\Gamma)|$，而同类每个标号图的 $\omega$ 相同，故乘以类大小即可。
3. 把 $\sum_{m}\lambda^{m}$ 拼起来并补上 $1/\hbar^{|V|}$ 的幂次，再把不连通图按连通分量分解，用 $\sum_{\text{所有图}}=\exp\left(\sum_{\text{连通图}}\right)$ 得到第二式。
   - *为什么*：一个图是若干连通分量的无序集合，指数函数正是按分量个数做无序求和的生成函数。

> **缺口**：书中把这一步明说「细节留给读者」：只写到 $\frac{1}{|G|}\sum$ 的重组，没有逐项验证轨道计数、也没有讨论连通分量分解后各项的渐近展开与截断；这里给出思路，指数化那步按形式幂级数补出，未做严格收敛分析。


来源：ch02c.tex:476-488（原书 p.145–146）

### 同构的图有相同的权

若 $\Gamma$ 与 $\Gamma'$ 同构，则 $\omega_{\Gamma}=\omega_{\Gamma'}$。

**完整证明**

1. 取同构 $(\sigma_{V},\sigma_{HE})$，它把每个顶点送到顶点、每条边送到边。
   - *为什么*：定义 2.8.6 要求这对双射与关联映射、匹配都相容，因此图的结构逐项对应。
2. 在 $\omega_{\Gamma'}$ 的求和里作哑标替换：顶点的 $I$ 指标按 $\sigma_{V}$ 重命名，边的 $(Q^{-1})$ 指标按 $\sigma_{HE}$ 重命名。
   - *为什么*：求和指标是哑标，整体重命名不改变总和。
3. 重命名后 $\omega_{\Gamma'}$ 逐项等于 $\omega_{\Gamma}$ 的对应项，故两者相等。
   - *为什么*：每个顶点的 $I_{ijk}$ 与每条边的 $(Q^{-1})^{ij}$ 都被同构一一对应，因子集合相同。

来源：ch02c.tex:429-451（原书 p.145）

## 易错点

- 自同构群大小在分母：对称性越高的图贡献越小，漏掉它就是把同一标号方式重复相加。
- 只有连通图进指数；把不连通图也塞进指数会重复计算，因为它们已经由连通图的乘积给出。
- 三价公式只属于三次相互作用；若加入 $I_{4}$，顶点度数变成 4，$|E|$ 与 $\hbar$ 幂次要按新度数重算。
- 求和的对象是同构类而非标号图：同一类里每个标号图同权，逐个相加会多出 $|G|/|\operatorname{Aut}(\Gamma)|$ 倍。

## 相关卡

- [威克定理与高斯矩的配对](../concepts/wick-theorem.md)
- [Θ 图的顶点、半边与边](../examples/theta-graph.md)
- [$\Theta$ 图的权重 $\omega_\Gamma$](../examples/theta-weight.md)
- [外尔量子化与 Moyal 乘积](../concepts/weyl-quantization-moyal.md)

## 出处

- §2.8.2 费曼图展开，p.142–146（PDF p.143–147），源码 `ch02c.tex:274-520`
