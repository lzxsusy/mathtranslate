---
id: glc/concept/derham-ran-construction
type: concept
track: G
---

# de Rham Ran 构造与 Betti 的比较

> de Rham 侧把局部 Hecke 范畴沿对角映射粘成 Ran 范畴；其到谱侧 QCoh 的幺半函子核很大，正是消失猜想来源。

**问题**：为什么 Betti 情形不能照搬 Ran 余极限来构造单个幺半范畴？

## 定义

在 de Rham 情形，将 $Y=X(\mathbb C)$ 与 $\operatorname{LocSys}(Y^I)$ 替换为 de Rham 层理论 $\operatorname{DMod}(X^I)$。局部 Hecke 范畴组织成 Ran 范畴表达式
$$\operatorname{Rep}(\check G)_{\mathrm{Ran}}\simeq\operatorname{colim}_I\bigl(\operatorname{Rep}(\check G)^{\otimes I}\otimes\operatorname{DMod}(X^I)\bigr),$$
其中过渡映射由对角映射构造。有一个自然的幺半函子
$$\operatorname{Rep}(\check G)_{\mathrm{Ran}}\longrightarrow\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{dR}}_{\check G}),$$
它的核很大，而且难以描述；这就是前面各章消失猜想的来源。

*记号*：$\operatorname{DMod}(X^I)$ 为 $X^I$ 上的 $D$ 模范畴；下标 $\mathrm{Ran}$ 表示沿有限子集配置空间（Ran 空间）取的余极限；$\operatorname{LocSys}^{\mathrm{dR}}_{\check G}$ 见 §11.2。

## 要点

- de Rham 侧把 $\operatorname{LocSys}(Y^I)$ 换成 $\operatorname{DMod}(X^I)$，过渡映射由对角映射构造。
- 所得 Ran 范畴 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}$ 接收一个自然幺半函子到 $\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{dR}}_{\check G})$，其核很大且难以描述，这是消失猜想的来源。
- Betti 情形不能朴素照搬：对对角映射 $\Delta:Y^J\to Y^I$，构造 Ran 型余极限所需的左 Kan 延拓 $\Delta_!:\operatorname{LocSys}(Y^J)\to\operatorname{LocSys}(Y^I)$ 一般并非幺半函子。
- 甚至像 $\mathrm{pt}\to S^1$ 这样的映射，也会产生具有无限 Jordan 块的局部系统；因此正确的幺半对象仍是 $\operatorname{Perf}(\operatorname{Maps}(Y,B\check G))$ 或其 $\operatorname{QCoh}$-完备化（定理 9.3.1，局部到整体定理）。

## 关键公式

- $$\operatorname{Rep}(\check G)_{\mathrm{Ran}}\simeq\operatorname{colim}_I\bigl(\operatorname{Rep}(\check G)^{\otimes I}\otimes\operatorname{DMod}(X^I)\bigr)$$
- $$\operatorname{Rep}(\check G)_{\mathrm{Ran}}\longrightarrow\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{dR}}_{\check G})$$
- $$\Delta_!:\operatorname{LocSys}(Y^J)\longrightarrow\operatorname{LocSys}(Y^I)$$

## 定理与证明

### Betti 侧 Ran 构造的障碍（要点（有缺口））

对 $\Delta:Y^J\to Y^I$，左 Kan 延拓 $\Delta_!:\operatorname{LocSys}(Y^J)\to\operatorname{LocSys}(Y^I)$ 一般并非幺半函子，因此不能朴素地对取值于 $\operatorname{LocSys}(Y^I)$ 的 Hecke 数据取余极限形成单个幺半范畴；正确的幺半对象是 $\operatorname{Perf}(\operatorname{Maps}(Y,B\check G))$ 或其 $\operatorname{QCoh}$-完备化。

1. 写出 Betti 侧 Ran 型余极限所需的左 Kan 延拓 $\Delta_!$。  
   *为什么*：沿对角映射的推前是粘接 Hecke 数据的自然候选。
2. 用 $\mathrm{pt}\to S^1$ 的例子说明 $\Delta_!$ 会产生无限 Jordan 块，故一般不幺半。  
   *为什么*：幺半性要求保持张量积，而无限 Jordan 块破坏有限性。
3. 改取定理 9.3.1 给出的 $\operatorname{Perf}(\operatorname{Maps}(Y,B\check G))$ 作为正确的幺半对象。  
   *为什么*：局部到整体定理保证该谱范畴编码同一份作用数据。

> 缺口：讲义只陈述该比较（p.61），$\Delta_!$ 非幺半与无限 Jordan 块的断言均未证明；关键引用为定理 9.3.1。

*出处*：注（§12.3，讲义无编号） / 原书 p.61


## 易错点

- 不要把 Ran 余极限当成纯形式构造：de Rham 侧它的核很大且难以描述（消失猜想由此而来），Betti 侧则因 $\Delta_!$ 非幺半而根本不能这样取。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§12.3 与 de Rham Ran 构造的比较，p.61（PDF p.61），`源码/chapters/ch12.tex:46-59（Ran 构造与 Betti 比较，§12.3）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/Ran+space — Ran_X := colim_I X^I，I 取非空有限集、态射为满射，过渡映射为对角映射。

## 关联

- `glc/concept/betti-local-to-global`
- `glc/concept/locsys-on-homotopy-type`
- `glc/concept/hecke-lisse-sheaves`
