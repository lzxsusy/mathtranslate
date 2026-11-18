# 定理 B：从 PL 数据构造 $\B$

> `seidel/deriv/theorem-b-construction` ｜ track A ｜ draft

**目标**：构造定理 B 中的有限 A∞ 范畴 $\B$，并说明 $\Tw\B$ 含与 $\F(X)$ 拟等价的全子范畴。

**自测**：定理 B 里的 $\B$ 具体怎么造？为什么它自动 directed？

## 前提

- $\pi:X\to\C$ 是 Lefschetz 纤维化，临界点 $p_1,\ldots,p_m$，消失圈 $V_i\subset X_{t_0}$。
- 取 $X$ 的 PL 数据：匹配路径与辫 monodromy。

## 步骤

1. **对象取 $V_1,\ldots,V_m$；态射取 $\hom_\B(V_i,V_j)=CF^*(V_i,V_j)$。**  
   为什么：消失圈是 $X$ 中的 Lagrangian 球面，故 Floer 复形有定义。  
   锚点：原书 p.5（证据 B）

2. **高阶运算 $\mu^d_\B$ 由 $X$ 中的全纯圆盘计数给出，圆盘边界落在 $V_i$ 上。**  
   为什么：$\B$ 是 $\F(X)$ 的全子范畴，故运算由同一个圆盘计数诱导。  
   锚点：原书 p.5（证据 B）

3. **$\B$ 是 directed 的：存在对象排序使 $i>j$ 时 $\hom(V_i,V_j)=0$（或同调为零）。**  
   为什么：按临界值在 $\C$ 中的位置排序；匹配路径只从低到高，故反向态射消失。  
   锚点：原书 p.5（证据 B）

4. **$\Tw\B$ 是 $\F(X)$ 的全子范畴，且由生成性它与 $\F(X)$ 拟等价。**  
   为什么：消失圈生成 $\F(X)$；$\Tw$ 补齐锥与直和。  
   锚点：原书 p.5（证据 B）

## 结果

$\B$ 有限、directed；$\Tw\B\subset\F(X)$ 是拟等价的全子范畴，故 $\F(X)$ 与有限 directed A∞ 范畴的扭曲复形同调等价。

## 缺口

- 第 3 步的 directed 性是「匹配路径不反向」的几何事实，需 §17 的伪全纯截面论证。

## 易错点

- $\B$ 的对象不是 $X$ 的所有 Lagrangian，而是消失圈；这是定理 B 与 A 的共同点。
- directed 不等于「没有态射」；低到高的态射仍非零。
- $\Tw\B$ 与 $\F(X)$ 的等价是全子范畴的拟等价，不是范畴同构。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，引言、§19，p.5–5（原书 p.5）

关联：`seidel/concept/fukaya-category`、`seidel/concept/twisted-complex`、`seidel/deriv/directed-dg`

来源说明：据原书引言 p.5 与 §19 转述；构造细节分散在 §17–19。
