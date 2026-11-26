# 函子 II：经 Tannakian 重构把 $F_1$ 扩到 $\mathrm{Coh}_{\mathrm{free}}(\widehat{\mathcal N}_X)$

> `sandvik25/concept/functor-f2` · 轨道 B · Springer 侧与三造函子 · 状态 dev

> **先自测**：为什么要绕道 Tannakian 重构，$\mathcal O(\widehat{\mathcal N}_X)\to A$ 这个映射又从哪里来？

## 一句话

把 $\mathcal P_I^{\mathrm{Wak}}$ 换成一个对称幺半的非全子范畴 $\mathcal C$，用 Tannakian 形式得 $H\colon\mathcal C\xrightarrow{\sim}A\text{-}\mathrm{mod}^{G^\vee\times T^\vee}_{\mathrm{free}}$，于是扩张 $F_1$ 等价于造一个等变代数映射 $\mathcal O(\widehat{\mathcal N}_X)\to A$。

## 定义

取对称幺半的非全子范畴 $\mathcal C\subset\mathcal P_I^{\mathrm{Wak}}$ 使 $F_1$ 穿过它（脚注 10 指出：$\mathrm{Coh}^{G^\vee\times T^\vee}_{\mathrm{free}}(\widehat{\mathcal N}_X)$ 对称幺半而 $\mathcal P_I^{\mathrm{Wak}}$ 不是）。由 Tannakian 形式得等价 $H\colon\mathcal C\to A\text{-}\mathrm{mod}^{G^\vee\times T^\vee}_{\mathrm{free}}$，其中 $A$ 带 $G^\vee\times T^\vee$ 作用；$F'_1$ 在 $H$ 下成为 $V\mapsto V\otimes A$。扩张 $F'_1$ 到 $\mathrm{Coh}^{G^\vee\times T^\vee}_{\mathrm{free}}(\widehat{\mathcal N}_X)$ 等价于给一个 $G^\vee\times T^\vee$-等变代数映射 $\mathcal O(\widehat{\mathcal N}_X)\to A$。

**记号**：$A\text{-}\mathrm{mod}^{G^\vee\times T^\vee}_{\mathrm{free}}$ 为自由 $A$-模构成的等变范畴。

## 要点（为什么需要它）

1. 这一步的动机是「对称幺半」：要借用交换代数的语言（$\mathcal O(\widehat{\mathcal N}_X)$ 是交换环），必须先把非对称的目标范畴换成对称的 $\mathcal C$。
2. Tannakian 重构在此是黑箱：$A$ 是 $\mathcal C$ 的「函数环」，$V\otimes A$ 是 $\mathcal C$ 中自由对象的统一写法；原文不给构造。
3. 两个分量映射各有出处：$\mathcal O(\mathfrak g^\vee)\to A$ 是附近循环单值自同构的对数，$\mathcal O(X)\to A$ 由定理 2.5.3 的 Wakimoto 滤链决定。
4. 合成 $\mathcal O(\mathfrak g^\vee)\otimes\mathcal O(X)\to A$ 唯一分解出 $\mathcal O(\widehat{\mathcal N}_X)\to A$：因为 $\mathcal O(\widehat{\mathcal N}_X)$ 是 $\mathcal O(\mathfrak g^\vee)\otimes\mathcal O(X)$ 的商。
5. 得到 $F_2$ 的公式 $M\mapsto M\otimes_{\mathcal O(\widehat{\mathcal N}_X)}A$：这是标准的「沿环映射换基」，说明 $F_2$ 本质是一个张量积函子。

## 核心公式

$$
$H\colon\mathcal C\xrightarrow{\sim}A\text{-}\mathrm{mod}^{G^\vee\times T^\vee}_{\mathrm{free}},\quad V\otimes k_{T^\vee}(\lambda)\mapsto V\otimes k_{T^\vee}(\lambda)\otimes A$$F_2\colon\mathrm{Coh}^{G^\vee\times T^\vee}_{\mathrm{free}}(\widehat{\mathcal N}_X)\to A\text{-}\mathrm{mod}^{G^\vee\times T^\vee}_{\mathrm{free}}\cong\mathcal C\hookrightarrow\mathcal P_I^{\mathrm{Wak}},\quad M\mapsto M\otimes_{\mathcal O(\widehat{\mathcal N}_X)}A$
$$

$$
$F_2\colon\mathrm{Coh}^{G^\vee\times T^\vee}_{\mathrm{free}}(\widehat{\mathcal N}_X)\to A\text{-}\mathrm{mod}^{G^\vee\times T^\vee}_{\mathrm{free}}\cong\mathcal C\hookrightarrow\mathcal P_I^{\mathrm{Wak}},\quad M\mapsto M\otimes_{\mathcal O(\widehat{\mathcal N}_X)}A$
$$

## 常见误解

- Tannakian 重构要求 $\mathcal C$ 对称幺半且「足够小」；若直接对 $\mathcal P_I^{\mathrm{Wak}}$ 做，会因它非对称幺半而失败。
- $A$ 不是 $\mathcal O(\widehat{\mathcal N}_X)$：前者是 $\mathcal C$ 的端环，后者是几何环；两者的映射 $\mathcal O(\widehat{\mathcal N}_X)\to A$ 才是全部内容，方向不能反。

## 相关卡

[函子 I：$F_1\colon\mathrm{Rep}(G^\vee\times T^\vee)\to\mathcal P_I^{\mathrm{Wak}}$](../concepts/functor-f1.md) · [无穷小稳定化子 $\widehat{\mathcal N}$ 与 $\widehat{\mathcal N}_X$](../concepts/hat-n-x.md) · [Tannakian 重构里的代数 $A$ 与 $\mathcal O(\widehat{\mathcal N}_X)\to A$](../derivations/tannakian-algebra.md)

## 出处（印刷页）

- A p.7–8（A p.7）

> 说明：构造在 p.7，两个分量映射的说明与 $F_2$ 的公式在 p.8。
