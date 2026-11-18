---
id: dmod/concept/characteristic-ideal
type: concept
track: B
---

# 特征理想

> 特征理想 $J(M)$ 是分次模零化子的根，与好滤过无关；它的零点集就是特征簇，因此是特征簇的代数替身。

**问题**：分次模的零化子随好滤过而变，为什么它的根不变，这个根与特征簇是什么关系？

## 定义

设 $D$ 是配置满足 §3 开头公理 (i)–(vii) 的滤过 $F D$ 的滤过环，$M$ 是有限生成 $D$-模，$F M$ 是 $M$ 的好滤过。则 $\operatorname{Gr}M$ 是分次 $\operatorname{Gr}D$-模；设 $I$ 是 $\operatorname{Gr}M$ 在 $\operatorname{Gr}D$ 中的零化子。$I$ 按定义即为分次理想，其根 $r(I)$ 也是分次理想。引理 7.2 断言 $r(I)$ 不依赖好滤过的选择，称之为 $M$ 的\emph{特征理想}，记为 $J(M)$。

*记号*：$r(I)$ 表示理想 $I$ 的根；$\operatorname{Gr}$ 总是指 $F D$ 诱导的分次；对 $D=D(n)$ 配次数滤过时 $\operatorname{Gr}D(n)=k[X_1,\dots,X_n,\xi_1,\dots,\xi_n]$，$V(J(M))=\operatorname{Ch}(M)$。

## 要点

- $J(M)=r(\operatorname{Ann}_{\operatorname{Gr}D}(\operatorname{Gr}M))$ 是 $\operatorname{Gr}D$ 中的根式分次理想，而不是 $D$ 中的理想。
- 与好滤过无关：若 $F M$、$F'M$ 是两条好滤过，$I$、$I'$ 为相应零化子，则 $r(I)=r(I')$（引理 7.2）。
- 特征簇就是它的零点集：$\operatorname{Ch}(M)=V(J(M))$；因此特征理想只记到根为止。
- 对 $M=D(n)/L$（$L$ 为左理想）有 $J(M)=r(\operatorname{Gr}L)$，$\operatorname{Gr}$ 取次数滤过及其诱导滤过。
- 对短正合列 $0\to M'\to M\to M''\to 0$ 有 $V(J(M))=V(J(M'))\cup V(J(M''))$（命题 7.4 的等价说法）。

## 关键公式

- $J(M)=r\bigl(\operatorname{Ann}_{\operatorname{Gr}D}(\operatorname{Gr}M)\bigr)$
- $\operatorname{Ch}(M)=V(J(M))$
- $r(I)=r(I')$
- $J(D(n)/L)=r(\operatorname{Gr}L)$

## 定理与证明

### 引理 7.2（零化子的根与好滤过无关）（完整）

设 $M$ 是有限生成 $D$-模，$F M$ 和 $F'M$ 是 $M$ 上的两条好滤过，$I$、$I'$ 分别是分次 $\operatorname{Gr}D$-模 $\operatorname{Gr}M$、$\operatorname{Gr}'M$ 的零化子。则 $$r(I)=r(I').$$

1. 取 $T\in r(I)\cap\operatorname{Gr}_pD$，并取 $Y\in F_pD$ 使 $Y+F_{p-1}D=T$。由 $T^s\in I$ 得 $Y^sF_qM\subset F_{q+sp-1}M$，归纳得 $Y^{ms}F_qM\subset F_{q+msp-m}M$ 对一切 $m\in\mathbb N$、$q\in\mathbb Z$ 成立。  
   *为什么*：每一步把 $Y^s$ 的作用叠上去，指标按 $sp-1$ 累加，再减去累积的 $m$。
2. 由引理 3.7，两条好滤过等价：存在 $l\in\mathbb Z_+$ 使得 $F_qM\subset F'_{q+l}M\subset F_{q+2l}M$ 对一切 $q$ 成立。  
   *为什么*：好滤过互相被有限平移控制，这是 §3 中好滤过等价性的定义内容。
3. 于是 $Y^{ms}F'_qM\subset F'_{q+2l+msp-m}M$；取 $m>2l$ 得 $Y^{ms}F'_qM\subset F'_{q+msp-1}M$，即 $T^{ms}\in I'$，故 $T\in r(I')$，$r(I)\subset r(I')$。  
   *为什么*：$m>2l$ 时 $2l-m<0$，指数被 $msp-1$ 吸收；这正是需要 $m$ 足够大的原因。
4. 交换 $I$ 与 $I'$ 的角色，同样得 $r(I')\subset r(I)$，故 $r(I)=r(I')$。  
   *为什么*：上一步的论证对两条滤过完全对称，不需要额外假设。

*出处*：引理 7.2 / 原书 p.26


## 易错点

- 只有「根」不依赖好滤过；零化子 $I$ 本身依赖滤过，写 $J(M)=\operatorname{Ann}(\operatorname{Gr}M)$ 是错的。
- $J(M)$ 是 $\operatorname{Gr}D$（对 $D(n)$ 即 $k[X,\xi]$）里的理想，不是 $D(n)$ 里零化 $M$ 的左理想；两者维数含义完全不同。
- $J(M)$ 记不住 $M$：不同模可以有同一个特征簇，§8 的例子说明特征簇不能决定相应的 $D$-模。
- 取根会丢掉重数信息；重数由 Bernstein 重数 $e(M)$ 记录，不在 $J(M)$ 中。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译校订批注本，150 页），§7 特征簇，p.26-27（PDF p.32-33），`源码/chapters/chap1.tex:950-976（引理 7.2、特征理想的定义）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/characteristic-variety`
- `dmod/concept/bernstein-dimension`
- `dmod/concept/holonomic-module`
- `dmod/concept/weyl-algebra`
