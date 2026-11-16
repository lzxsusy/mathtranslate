# 经由路径积分的 WKB

> `pi/concept/wkb-path-integral` · 轨道 D · 格林函数与 WKB · 状态 draft

> **先自测**：半经典格林函数怎样给出 WKB 波函数的振幅 $p^{-1/2}$ 与相位 $\frac{1}{\hbar}\int p\,\mathrm{d}x$？

## 一句话

把半经典格林函数的端点速度换成 $\sqrt{2(E-V)/m}$，$G$ 就呈 WKB 形状：振幅 $\propto p^{-1/2}$、相位由 $\int p\,\mathrm{d}x$ 给出，与定态 WKB 波函数同构。

## 定义

WKB 近似假设波函数是“慢变振幅乘快变相位”：$\psi(x)\approx A(x)e^{\frac{i}{\hbar}S_0(x)}$，其中 $S_0$ 是经典作用量，$\mathrm{d}S_0/\mathrm{d}x=p=\sqrt{2m(E-V)}$，振幅 $A$ 由概率流守恒定出。路径积分给出同一结构的另一条来路：半经典格林函数的振幅只依赖两端点的经典速率 $\dot x=\sqrt{2(E-V)/m}$，相位是约化作用量 $\int p\,\mathrm{d}x$。当轨道在两端同向通过（无折返）时，把 $-\dot x(0)\dot x(T_s)$ 用端点动量改写，就有 $$G\simeq\frac{1}{\hbar}\sum_{(x_{cl},T_s)}\left(-\frac{1}{\sqrt{2(E-V(x'))/m}\,\sqrt{2(E-V(x''))/m}}\right)^{1/2}e^{\frac{i}{\hbar}\int_{x'}^{x''}p\,\mathrm{d}x},$$ 它正是两个 WKB 因子的拼接。

**记号约定**：$p(x)=\sqrt{2m(E-V(x))}$；$\dot x=\sqrt{2(E-V)/m}$ 为经典速率；$p^{-1/2}=(2m(E-V))^{-1/4}$ 为 WKB 振幅；求和遍历围道上的鞍点。

## 要点

- WKB 波函数的两件套：相位 $\frac{1}{\hbar}\int p\,\mathrm{d}x$ 与振幅 $p^{-1/2}$，缺一不可。
- 路径积分版：$G$ 的振幅只含端点速率 $\dot x=\sqrt{2(E-V)/m}$，中间轨道的细节已被积分掉。
- $p^{-1/2}=(2m(E-V))^{-1/4}$；在转折点 $p=0$ 处振幅发散，WKB 失效。
- 相位 $\int_{x'}^{x''}p\,\mathrm{d}x$ 等于 $W_{cl}=ET_s+S_{cl}$，是能量固定时的约化作用量。
- $-\dot x(0)\dot x(T_s)$ 的符号由两端速度方向决定：同向通过给 $-i$，折返一次给 $+1$；每经一个焦散乘 $e^{-i\pi/2}$，这就是马斯洛夫因子的来源。

## 关键公式

$$
p(x)=\sqrt{2m(E-V(x))}
$$

$$
\psi_{\mathrm{WKB}}(x)\approx\dfrac{1}{\sqrt{p(x)}}\exp\left(\pm\dfrac{i}{\hbar}\displaystyle\int^x p\,\mathrm{d}x'\right)
$$

$$
G(x'',x';E)\simeq\dfrac{1}{\hbar}\sum_{(x_{cl},T_s)}\left(-\dfrac{1}{\dot x(0)\dot x(T_s)}\right)^{\frac12}e^{\frac{i}{\hbar}\int_{x'}^{x''}p\,\mathrm{d}x}
$$

$$
\dot x=\sqrt{\dfrac{2(E-V)}{m}},\qquad p^{-1/2}=(2m(E-V))^{-1/4}
$$

$$
W_{cl}=ET_s+S_{cl}=\displaystyle\int_{x'}^{x''}p\,\mathrm{d}x
$$

## 定理与证明

### 半经典格林函数的 WKB 形状

在 $\hbar\to0$ 首阶，$G(x'',x';E)=\frac{1}{\hbar}\sum_s(-\dot x_{cl}(0)\dot x_{cl}(T_s))^{-1/2}e^{iW_s/\hbar}$，相位 $W_s=\int_{x'}^{x''}p\,\mathrm{d}x$。平方根的分支由两端速度方向决定：同向通过给 $e^{-i\pi/2}=-i$，折返一次给 $+1$；等价地，每经过一个焦散乘 $e^{-i\pi/2}$（马斯洛夫因子）。

**完整证明**

1. 由能量守恒 $E=\frac{m}{2}\dot x^2+V(x)$ 得两端速率 $|\dot x(0)|=\sqrt{2(E-V(x'))/m}$、$|\dot x(T_s)|=\sqrt{2(E-V(x''))/m}$。
   - *为什么*：端点处势能只由位置决定，速率的绝对值因此只由端点位置决定。
2. 振幅中的 $-\dot x(0)\dot x(T_s)$ 带符号：两端速度同向时乘积为负，$(-\dot x\dot x)^{-1/2}=(v'v'')^{-1/2}e^{-i\pi/2}$；折返一次（经过一个焦散）时乘积为正，分支为 $+1$。一般地每经一个焦散乘 $e^{-i\pi/2}$。
   - *为什么*：平方根是双值的，物理分支由轨道是否穿过焦散决定，不能无条件取 $-i$。
3. 把 $W_s$ 写成 $\int p\,\mathrm{d}x$，与 $\psi_{\mathrm{WKB}}\propto p^{-1/2}e^{\pm\frac{i}{\hbar}\int p\,\mathrm{d}x}$ 对比：$G$ 与两端 WKB 波函数的乘积 $\psi(x'')\psi^*(x')$ 只差一个常数因子；在常见一维归一约定下该因子为 $(m/\hbar)(-i)$，不能只写 $1/\hbar$。
   - *为什么*：$p^{-1/2}$ 因子分别来自两个端点，相位是同一积分的差；常数因子取决于 $\psi$ 的归一约定，量纲上必须保留 $m/\hbar$。

来源：ch02b.tex:1264-1293（原书 p.131–132）

### 约化作用量的梯度给出动量

固定 $E$，$W_{cl}(x'',x')=\int_{x'}^{x''}p\,\mathrm{d}x$ 满足 $\partial W_{cl}/\partial x''=p(x'')$、$\partial W_{cl}/\partial x'=-p(x')$；这正是 WKB 相位梯度等于 $\pm ik$ 的来源。

**完整证明**

1. 由 $W_{cl}=ET_s+S_{cl}$ 对 $x''$ 求导：$\partial_{x''}W=E\,\partial_{x''}T_s+\left.\partial_{x''}S_{cl}\right|_{T}+\partial_TS_{cl}\,\partial_{x''}T_s$。
   - *为什么*：$T_s$ 也依赖 $x''$，所以两处都要用链式法则。
2. 用鞍点条件 $E+\partial_TS_{cl}=0$ 消去含 $\partial_{x''}T_s$ 的两项，得 $\partial_{x''}W=\left.\partial_{x''}S_{cl}\right|_{T}$。
   - *为什么*：这正说明从 $S_{cl}$ 到 $W_{cl}$ 是固定能量的勒让德变换，多余的时间依赖被消掉。
3. 固定 $T$ 时 $\partial_{x''}S_{cl}=p(T_s)=p(x'')$（作用量对末点的偏导是末动量），故结论成立；对 $x'$ 同理得 $-p(x')$。
   - *为什么*：作用量作为端点函数的这一性质是哈密顿–雅可比理论的基本结论。

来源：ch02b.tex:1270-1292（原书 p.132）

## 易错点

- 把 WKB 振幅写成 $p^{-1}$（漏掉平方根）；正确是 $p^{-1/2}=(2m(E-V))^{-1/4}$。
- 在转折点 $E=V$ 处照用 WKB：振幅发散，必须换成艾里函数（见连接公式）。
- 忽略 $(-\dot x\dot x)^{-1/2}$ 的负号分支，结果会与正确的 WKB 相位差 $\pi/2$。
- 把 $\int p\,\mathrm{d}x$ 与 $\int L\,\mathrm{d}t$ 混为一谈：二者相差 $ET_s$，能量固定时必须用前者。
- 以为 $G$ 的 WKB 形式对每条轨道都成立：焦散点附近振幅发散，需要一致渐近处理。

## 相关卡

- [半经典格林函数](../concepts/semiclassical-green-function.md)
- [连接公式再探](../concepts/connection-formula.md)
- [量子隧穿](../concepts/quantum-tunneling.md)
- [散射态的渐近行为](../examples/scattering-asymptotics.md)

## 出处

- §2.7.3 经由路径积分的 WKB，p.131–132（PDF p.132–133），源码 `ch02b.tex:1250-1293`
