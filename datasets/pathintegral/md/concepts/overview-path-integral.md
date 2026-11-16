# 路径积分总览：从费曼核到量子 HKR

> `pi/concept/overview-path-integral` · 轨道 总览 · 状态 draft

> **先自测**：路径积分这条主线如何从费曼核一路走到半经典近似与量子 HKR？

## 一句话

第 2 章的主线：把传播子写成路径和，用时间切片与高斯积分算出精确核，再用驻定相位得到半经典核、格林函数与 WKB，最后进入威克定理、费曼图与量子 HKR。

## 定义

路径积分把量子传播子写成对路径的相位加权和。第 2 章先定义费曼核与路径积分，再用时间切片把它化为多重积分；高斯情形可精确计算，一般情形则用驻定相位得到半经典展开。由此得到半经典费曼核、固定能量格林函数、WKB 波函数与隧穿系数。最后把路径积分看成生成函数，用威克定理与费曼图组织微扰展开，并在 $S^1$ 上把关联函数与霍赫希尔德同调、量子 HKR 联系起来。

**记号约定**：$K$ 为费曼核；$S$ 为作用量；$G(E)$ 为固定能量格林函数；$\hbar$ 为约化普朗克常数；$\beta$ 为逆温度。

## 要点

- 第一层是定义：$K=\int[Dx]e^{iS/\hbar}$，它把时间演化算子写成积分核。
- 第二层是计算：时间切片把路径积分化为 $N\to\infty$ 的多重积分；高斯路径积分可精确求出自由粒子与谐振子的核。
- 第三层是半经典：$\hbar\to0$ 时驻定相位把主要贡献压到经典轨道，二阶涨落给出行列式与 Maslov 相位。
- 格林函数是传播子对时间的傅里叶变换；它的鞍点方程同时给出经典轨道与旅行时间。
- WKB 与隧穿是半经典格林函数在转折点两侧的匹配，连接公式本质上是斯托克斯跳跃。
- 威克定理把高斯矩化为配对求和，费曼图把展开按图的同构类组织。
- $S^1$ 上的关联函数给出量子化乘法；量子 HKR 把 Hochschild 同调与微分形式对应起来。

## 关键公式

$$
K(x'',t'';x',t')=\int_{x(t')=x'}^{x(t'')=x''}[Dx]\,e^{\frac{i}{\hbar}S[x]}
$$

$$
K=\lim_{N\to\infty}\left(\frac{m}{2\pi i\hbar\varepsilon}\right)^{N/2}\int\prod_{j=1}^{N-1}dx_j\,e^{\frac{i}{\hbar}\sum_j\varepsilon L}
$$

$$
K_{sc}(x'',x')=\left(\frac{1}{2\pi i\hbar}\right)^{n/2}\sqrt{\left|\det\left(-\frac{\partial^2S_{cl}}{\partial x'\partial x''}\right)\right|}\,e^{\frac{i}{\hbar}S_{cl}-\frac{i\pi}{2}\nu}
$$

$$
G(x'',x';E)=\frac{1}{i\hbar}\int_0^\infty dT\,e^{\frac{iET}{\hbar}}K(x'',T;x',0)
$$

$$
\langle x^{i_1}\cdots x^{i_{2n}}\rangle=\sum_{\text{pairings}}\hbar^n\prod (Q^{-1})^{i_aj_b}
$$

$$
f\star g=f\exp\left(\frac{i\hbar}{2}(\overleftarrow{\partial_x}\overrightarrow{\partial_p}-\overleftarrow{\partial_p}\overrightarrow{\partial_x})\right)g
$$

## 定理与证明

### 半经典费曼核（Van Vleck–Pauli–Morette）

当经典轨道唯一且非退化时，$K(x'',t'';x',t')\simeq(2\pi i\hbar)^{-n/2}|\det(-\partial^2S_{cl}/\partial x'\partial x'')|^{1/2}e^{iS_{cl}/\hbar-i\pi\nu/2}$，$\nu$ 为 Maslov 指标。

**完整证明**

1. 把路径写成经典轨道加涨落 $x=x_{cl}+\delta x$，作用量展开到二阶。
   - *为什么*：驻定相位只保留二次涨落；一阶项由经典轨道方程为零。
2. 二阶变分写成 $\delta^2S=\frac12\int \delta x\,(-\partial_t^2-\partial_x^2V)\delta x$，即雅可比算子。
   - *为什么*：二次型由雅可比场方程决定，边界条件为两端固定。
3. 对涨落作高斯积分，得到 $\det(\text{Jacobi})^{-1/2}$，并用经典作用量的混合偏导表示该行列式。
   - *为什么*：高斯积分公式给出行列式倒数平方根；Van Vleck 行列式是它的经典极限。
4. 统计焦散点处行列式的负号/绕数，乘以 $e^{-i\pi\nu/2}$。
   - *为什么*：每次穿过焦散，驻定相位的相位跳变由 Maslov 指标记录。

来源：ch02b.tex:31-88、ch02b.tex:89-465（原书 p.108–115）

### 霍赫希尔德–科斯坦特–罗森伯格（HKR）定理

设 $A=k[y^i]$ 为多项式环，$\Omega^\bullet_A=k[y^i,dy^i]$ 为代数微分形式，则 $HH_p(A)\simeq\Omega^p_A$。

**证明提纲**

1. 把 Hochschild 链复形按多项式次数分解，并用 Koszul 型消去处理正次数部分。
   - *为什么*：这是 HKR 证明的代数骨架；书中只引用结论。
2. 剩下的同调由 $A$ 的微分形式代表，次数 $p$ 对应 $HH_p$。
   - *为什么*：消去后同调集中在对角部分，正好与 Kähler 微分形式同构。

> **缺口**：书中只陈述定理 2.8.16，未给完整证明；这里只补了 Koszul 消去的思路，具体谱序列与自然性未展开。


来源：ch02c.tex:1103-1151（原书 p.156–157）

## 易错点

- 路径积分测度一般没有严格定义，形式操作不能替代测度论证明；欧氏情形才有维纳测度。
- 驻定相位在焦散点失效，必须加 Maslov 相位或改用半密度。
- 格林函数的 $+i\epsilon$  prescription 决定围道与出射波边界条件，漏掉会得到错误的渐近行为。
- 威克定理只对高斯测度成立；相互作用项要按幂级数逐项赋值，级数通常发散。
- 实时路径积分与虚时间路径积分不能直接互换，欧氏核对应的是密度矩阵而非酉演化。

## 相关卡

- [费曼核与传播子](../concepts/feynman-kernel.md)
- [半经典费曼核](../concepts/semiclassical-kernel.md)
- [固定能量格林函数](../concepts/fixed-energy-green-function.md)
- [威克定理与高斯矩的配对](../concepts/wick-theorem.md)
- [量子 HKR 映射](../concepts/quantum-hkr.md)

## 出处

- §2.1–§2.5 路径积分与渐近方法，p.80–107（PDF p.81–108），源码 `ch02a.tex:8-1466`
- §2.6–§2.7 半经典近似与格林函数，p.108–137（PDF p.109–138），源码 `ch02b.tex:6-1538`
- §2.8 微扰展开与量子 HKR，p.138–160（PDF p.139–161），源码 `ch02c.tex:51-1374`
