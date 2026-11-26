# Gaitsgory 中心函子 $Z$

> `sandvik25/concept/gaitsgory-central-functor` · 轨道 A · 中心层与 Wakimoto 层 · 状态 dev

> **先自测**：中心函子怎么定义，「像落在中心」这条性质为什么是整篇文章的枢纽？

## 一句话

$Z(\mathcal F)=\Psi_f(\mathcal F\boxtimes k_{\mathbb C^\times}[1])$ 把 $L^+G$-等变层送到 $I$-等变层；定理 2.4.1 说它幺半、$t$-正合、像落在中心，且 $\pi_*Z(\mathcal F)\cong\mathcal F$。

## 定义

由中心仿射 Grassmann 簇上的附近循环定义 $Z\colon\mathcal D^b_c(\mathrm{Gr}_G)\to\mathcal D^b_c(\mathrm{Fl}_G)$，$\mathcal F\mapsto\Psi_f(\mathcal F\boxtimes k_{\mathbb C^\times}[1])$；再升级为等变版本 $Z\colon\mathcal D^b_c(L^+G\backslash\mathrm{Gr}_G)\to\mathcal D^b_c(I\backslash\mathrm{Fl}_G)$。$\mathcal F\in\mathrm{Perv}(L^+G\backslash\mathrm{Gr}_G)$ 的像 $Z(\mathcal F)$ 称为中心层。

**记号**：$\star_{L^+G}$、$\star_I$ 为两边的卷积分；$\pi\colon\mathrm{Fl}_G\to\mathrm{Gr}_G$ 为投影。

## 要点（为什么需要它）

1. 「像落在中心」= $Z(\mathcal F)\star_I\mathcal G\cong\mathcal G\star_I Z(\mathcal F)$ 对一切 $\mathcal G\in\mathcal D^b_c(I\backslash\mathrm{Fl}_G)$ 成立；这是定理 2.4.1(3)，也是函子 I 幺半性的来源（引理 3.2.1）。
2. 定理 2.4.1(5) 的 $\pi_*Z(\mathcal F)\cong\mathcal F$ 说明 $Z$ 在球侧是「单的」：它不丢信息，只是加进了 Iwahori 侧的位置变量。
3. 证明 (5) 的手法值得记住：造 $\varpi\colon\mathrm{Gr}^{\mathrm{cen}}_G\to\mathrm{Gr}_G\times\mathbb C$，用紧合基变换 (4) 与常层特殊化 (5) 把 $\Psi_f$ 化成 $\pi_*\Psi_{\mathrm{pr}_2}$。
4. 旁注 2.4.2 提醒：$Z$ **不是**到中心的等价——仿射 Hecke 范畴的中心比 $\mathrm{Rep}(G^\vee)$ 大得多（见 [BNP] 的谱描述）。
5. 注 2.4.3 把 $Z$ 与几何 Satake 复合，得 $\mathrm{Rep}(G^\vee)\to\mathrm{Perv}(I\backslash\mathrm{Fl}_G)$；原文此后常不加区分地写 $Z$。

## 核心公式

$$
$Z(\mathcal F)=\Psi_f(\mathcal F\boxtimes k_{\mathbb C^\times}[1])$$Z(\mathcal F)\star_I\mathcal G\cong\mathcal G\star_I Z(\mathcal F)$$\pi_*Z(\mathcal F)\cong\mathcal F$
$$

$$
$Z(\mathcal F)\star_I\mathcal G\cong\mathcal G\star_I Z(\mathcal F)$
$$

$$
$\pi_*Z(\mathcal F)\cong\mathcal F$
$$

## 定理与证明（或缺口）

### 定理 2.4.1（Gaitsgory）

中心函子 $Z$：(1) 幺半；(2) perverse $t$-正合；(3) 像落在 $\mathcal D^b_c(I\backslash\mathrm{Fl}_G)$ 的中心；(4) 两个反常层卷积后仍反常；(5) $\pi_*Z(\mathcal F)\cong\mathcal F$。

> 证明状态：**sketch**。(1)(3)(4) 原文不证；等变性需要 $\mathbb A^1$ 上的群 ind-概形（脚注 6，引 [AcRi] §2.2、§10.3）。

出处：`A p.4`

## 常见误解

- 「幺半」不是「张量等价」：$Z$ 只保证 $Z(\mathcal F\star\mathcal G)\cong Z(\mathcal F)\star Z(\mathcal G)$，不保证反映同构。
- 把 $Z$ 与几何 Satake $\mathrm{Sat}$ 复合之后，$Z$ 的定义域变成 $\mathrm{Rep}(G^\vee)$，但这不改变它仍是同一个函子这一事实——原文的记号滥用容易让人以为是两个不同构造。

## 相关卡

[中心仿射 Grassmann 簇 $\mathrm{Gr}^{\mathrm{cen}}_G$](../concepts/central-affine-grassmannian.md) · [中心层的 Wakimoto 滤链（定理 2.5.3）](../concepts/wakimoto-filtration.md) · [函子 I：$F_1\colon\mathrm{Rep}(G^\vee\times T^\vee)\to\mathcal P_I^{\mathrm{Wak}}$](../concepts/functor-f1.md)

## 出处（印刷页）

- A p.3–4（A p.4）

> 说明：定义在 p.3，定理 2.4.1 与证明在 p.4；旁注 2.4.2、注 2.4.3 同在 p.4。
