# Hecke 对应与 Hecke 算子

> `goresky04/concept/hecke-operator` · 轨道 B · 自守侧 · 状态 dev

> **先自测**：Hecke 算子是怎么从「一个矩阵」变成一个「作用在模形式上的算子」的？

## 一句话

每个 $g\in\GL(2,\bbQ)$ 给出一个双陪集 $\Gamma g\Gamma$，它定义模曲线之间的对应，作用在函数上就是 Hecke 算子 $T_g=s_*t^*$。

## 定义

记 $\Gamma=\SL(2,\bbZ)$，$g\in\GL(2,\bbQ)$，$\Gamma'=\Gamma\cap g\Gamma g^{-1}$。有两个自然映射 $s\colon\Gamma'\backslash\he\to(g\Gamma g^{-1})\backslash\he$ 与 $t\colon\Gamma'\backslash\he\to\Gamma\backslash\he$，它们都是有限覆叠和谐同态，于是 $X'\to X\times X$ 给出一个对应。这个对应只依赖双陪集 $\Gamma g\Gamma$。它作用在函数上为 $T_g(f)=s_*t^*f$；在模曲线上则是「把 $X'$ 的像推回去」，是多值映射的像。

**记号**：$T_g$ 记 Hecke 算子；对 $g=\mathrm{diag}(p,1)$ 记 $T_p$；$s_*$ 为沿 $s$ 的推前（对覆叠取迹）。

## 要点（为什么需要它）

1. Hecke 算子不是「函数的线性变换」这么简单：它由对应给出，$s_*$ 里带着「有限覆叠的迹」，这一步是它成为自伴算子的原因。
2. 对应只依赖双陪集：同一个双陪集里的不同 $g$ 给出同一个算子，这就是为什么 Hecke 代数以双陪集为基。
3. $T_p$ 的几何含义是「$p$ 阶子群」：在模曲线分类椭圆曲线的意味下，$T_p$ 是把 $E$ 送到它的 $p$ 个 $p$ 阶子商的对应。

## 核心公式

$$
$T_g(f)=s_*t^*f$  (5.4.1)$\Gamma'=\Gamma\cap g\Gamma g^{-1}$，$[\Gamma:\Gamma']<\infty$
$$

$$
$\Gamma'=\Gamma\cap g\Gamma g^{-1}$，$[\Gamma:\Gamma']<\infty$
$$

## 定理与证明（或缺口）

### $T_g$ 的函子性

$T_g$ 只依赖双陪集 $\Gamma g\Gamma$；当 $g,h$ 的阶互素时 $T_gT_h=T_{gh}$。

> 证明状态：**sketch**。原文给出定义与「只依赖双陪集」一句，乘法表没有展开；本卡步 2–3 是译者按通行证明补的。

出处：`A p.8`

## 常见误解

- 推前 $s_*$ 在覆叠次数不为 1 时不是「直接前推」，要按纤维求和；漏掉这一点会把 $T_p$ 算错。
- $T_g$ 与 $T_{g^{-1}}$ 一般不相等，尽管它们是伴随；「自伴」只在配上 Petersson 内积之后成立。

## 相关卡

[经典模形式](../concepts/modular-form-classical.md) · [Hecke 特征形式与 Fourier 系数](../concepts/hecke-eigenform.md) · [Satake 参数：非分歧局部表示的指纹](../concepts/satake-parameter.md)

## 出处（印刷页）

- A p.8–9（A p.8）

> 说明：对应原文 §5.4 的 (5.4.1) 与对应图；乘法表一条原文未证，按通行说法补齐。
