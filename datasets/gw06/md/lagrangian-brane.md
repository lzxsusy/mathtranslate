# A-模型中的拉格朗日膜

- **id**：`gw06/concept/lagrangian-brane`
- **类型**：concept
- **位置**：§5.3
- **问题**：线算符插在中间时，它究竟对边界条件做了什么，为什么可以写成一个核卷积？

> A-模型的膜是拉格朗日膜；线算符通过 MH×MH 中的一个对应（核）作用在膜上，写成拉回—张量—前推三步，本质上是作用于 Fukaya 范畴的函子。

## 定义

$A$-模型的膜是 $\mathcal M_H$ 中关于辛结构 $\omega_K$ 拉格朗日的子流形，附以一个 Chan–Paton 丛（层）；两个膜的态射空间由 Floer 上同调给出。线算符 $L_y$ 通过 $\mathcal M_H\times\mathcal M_H$ 中的一个对应 $\mathcal Q$ 作用在膜上：$\mathcal Q$ 参数化对 $(\tilde E_u,E_u)$，其中 $\tilde E_u$ 由 $E_u$ 跳过 $L_y$ 得到；作用是 $\mathcal B_1\mapsto\pi_{2*}(p_1^*\mathcal B_1\otimes\mathcal Q)$，即先拉回、再与 $\mathcal Q$ 张量、最后前推。物理上这就是算符作用在边界条件上：$\mathcal Q$ 由保持 $(B,A,A)$ 超对称的解构造，故本身是 $(B,A,A)$ 型膜，但主要当作 $K$ 型的 $A$-膜使用。由于 $\mathcal Q$ 是紧化空间里的对应，映射 $\mathcal B_1\mapsto L_y\cdot\mathcal B_1$ 保持 Floer 上同调的次数，这正是「算符作用在膜上」在数学上应有的样子，也是拉格朗日膜必须配 Chan–Paton 层的原因。

**记号**：$\mathcal B_1,\mathcal B_2$：$\mathcal M_H$ 上的膜（边界条件）、$\mathcal Q\subset\mathcal M_H\times\mathcal M_H$：线算符给出的对应、$\pi_i:\mathcal M_H\times\mathcal M_H\to\mathcal M_H$：两个投影、$\bar{\mathcal N}$：超对称位形的紧化模空间、$\Xi(E_u)$：使 $(\tilde E_u,E_u)$ 落在 $\mathcal Q$ 中的 $\tilde E_u$ 构成的空间

## 关键点

- $\mathcal Q\subset\mathcal M_H\times\mathcal M_H$ 参数化 $(\tilde E_u,E_u)$，$\tilde E_u$ 由 $E_u$ 跳过线算符 $L_y$ 得到；它由保持 $(B,A,A)$ 的解构造，因此是 $(B,A,A)$ 型膜。
- 作用公式 $\mathcal B_1\mapsto\pi_{2*}(p_1^*\mathcal B_1\otimes\mathcal Q)$：拉回、与 $\mathcal Q$ 张量、前推，两个投影为 $\pi_i:\mathcal M_H\times\mathcal M_H\to\mathcal M_H$。
- 若 $\mathcal B_1$ 是 $(B,A,A)$ 型膜，这些运算可用复结构 $I$ 的复几何实施；若 $\mathcal B_1$ 只是一般的 $K$ 型 $A$-膜，必须改用 $A$-模型的类比，即在 Floer 上同调中的类比。
- 物理希尔伯特空间是紧化模空间 $\bar{\mathcal N}$ 的上同调；$L_y\cdot\mathcal B_1$ 的 Chan–Paton 层在 $E_u$ 处的纤维，是 $\Xi(E_u)$ 的上同调。
- 用来定义 $\mathcal Q$ 的抛物丛大多不稳定，需用 $(\tilde E_u,E_u)$ 空间的紧化，即把 $|m|$ 更小的类 Hecke 修改也纳入。

## 公式

```latex
\EUQ\subset \MH\times \MH
```
```latex
L_y\cdot {\mathcal B}_1=\pi_{2\,*}(p_1^*({\mathcal B}_1)\otimes \EUQ)
```
```latex
\pi_i:\MH\times\MH\to \MH
```

## 常见错误

- 把作用写成 $\pi_{1*}(p_2^*\mathcal B_1\otimes\mathcal Q)$（拉回与前推的投影对调）：这样得到的膜不依赖 $L_y$ 的插入位置，等于把线算符的作用写成恒等。
- 对任意 $A$-膜都用复几何实现：只有 $(B,A,A)$ 型膜可以只用 $I$ 的复几何；一般 $K$ 型 $A$-膜必须用 Floer，硬把 $A$-膜当成复流形上的层会丢掉 Floer 修正。
- 忽略 $\mathcal Q$ 的紧化：直接用不稳定抛物丛定义对应，会把不稳定点当成膜上的点，得到不闭（$Q^2\ne 0$）的上同调。

## 批注

### 易错预警：公式里的两个投影其实是同一对

原文刚把两个投影定义为 $\pi_1,\pi_2$，紧接着却在同一公式里写 $p_1^*$ 与 $\pi_{2*}$：$p_1,p_2$ 指的就是 $\pi_1,\pi_2$，译文照原文保留这一记号笔误。照字面把它当成四个不同投影，就写不出自洽的作用公式，也会误以为 $\mathcal Q$ 被拉回到错误的因子上。核对方法是看原文下一段的 $\mathcal B_2=\pi_{2*}(\cdots)$：那里用的仍是同一对投影。

### 含糊点拨：为什么可以只看 K 型 A-膜

$\mathcal Q$ 同时是 $I$ 上 $B$-模型、$J$ 与 $K$ 上 $A$-模型的膜，即 $(B,A,A)$ 型。作用在膜上时按 $K$ 型 $A$-膜理解最方便，因为要用的等式全在 $A$-模型一侧。原文说「我们主要把它看作 $K$ 型的 $A$-膜」，正是为了把复几何运算与 Floer 运算分开处理：前者只对特殊膜有效，后者才是一般情形。

### 背景直觉：拉格朗日膜就是边界条件

四维理论紧化到二维后，膜的选取就是边界条件；线算符插在中间，等价于在 $\mathcal M_H$ 上作一次核卷积。这与无分歧情形中 't Hooft 算符给出 Hecke 对应完全平行：几何朗兰兹的「算符即对应」在这里被具体化为 $\mathcal M_H\times\mathcal M_H$ 中的一个子流形，而膜的角色就是被这个对应搬运的对象。

## 出处

- Gukov–Witten 2006（hep-th/0612073v2）中译校订本 §5.3；印刷页 [122, 125] / PDF 页 [123, 126]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s05b-amodel.tex:191-220`
- 「在膜上的作用」一节见 PDF 第 123–126 页（印刷 122–125）。页码为原文印刷页，原文 PDF 页 = 印刷页 + 1；区间按原文页脚定位，定位只依赖节号与中译源码行号。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
