# Hitchin 1987：黎曼面上的自对偶方程

| 项 | 内容 |
|---|---|
| 文献 | N. J. Hitchin, *The self-duality equations on a Riemann surface* |
| 出处 | Proc. London Math. Soc. (3) **55** (1987) 59–126 |
| arXiv | 无（1987 年，已用标题检索核对，故只登记书目） |
| 页数 | 68（期刊页码区间） |
| 本地 | 未下载（`00_原文/基础文献/06_Hitchin与WKB谱网络/` 下只留有书目说明） |

> 摘要依据：本文无公开全文，以下按该文的标准内容 + GMN2 §4「Hitchin systems」与 GMN1 §2 的转述整理；未逐页核对公式编号，故不给具体式号。

## 1. 它解决什么

从一个**方程**造出**超凯勒流形**，再把这个流形做成**完全可积系统**。方程是黎曼面 C 上秩 2 复丛 (E, A, Φ) 的自对偶方程

  F_A + [Φ, Φ*] = 0

（Φ 是 (1,0)-形式取值的 Higgs 场，Φ* 是其关于 Hermite 度量的共轭）。Hitchin 证明：解模空间 M 是**超凯勒流形**，且含 Teichmüller 空间作为其一个连通分支（取 Φ 为全纯二次微分的那一支）。这就是「Hitchin 系统」的出生地，也是「谱曲线」进入 4d N=2 的入口。

## 2. 核心构造 / 定理

- 方程与模空间：解模空间 M 带三个复结构 I, J, K 与一个超凯勒度量；M 的一半（复结构 I）就是 Higgs 丛模空间。
- **谱曲线与纤维化**：特征方程 det(Φ − λ) = 0 定义 C 的总空间里的分支覆盖 Σ → C（rank 2 时为二次覆盖）；每个点给出 Σ 上的一个线丛 L，于是 M → B（B = 二次微分空间）是阿贝尔簇纤维化，纤维 = Prym(L)。这是**可积系统**的 Lax 形式：运动积分 = B 的坐标。
- 上述纤维化的极化与 Abel–Jacobi 映射使 M 成为代数完全可积系统（Hitchin fibration）。
- 解的存在性依赖 Higgs 对的稳定性（与 Donaldson–Uhlenbeck–Yau / Corlette 的调和映射理论同一套分析）。

## 3. GMN1–3 里哪一步用到它

- **GMN1 §2.1–§2.3**：4d N=2 在 R³×S¹ 上的低能模空间 = 一个复可积系统；其库仑分支 B 与纤维正是 Hitchin 纤维化的原型（GMN1 说「M 是复环面丛 M → B」）。
- **GMN2 §4（p.59）「Hitchin systems」整节**：把 GMN2 的全部几何建立在「C 上的 Hitchin 系统」上——谱曲线 Σ → C 给出电荷格 Γ，Z_γ = ∮_γ λ 是 Seiberg–Witten 微分沿 Σ 上闭链的积分，BPS 态 = Σ 上的测地线（WKB 曲线）。没有这篇就没有 GMN2 的第 4 章。
- **GMN2 §6「WKB triangulation」** 的「WKB 曲线」= 谱曲线上 Im(e^{−iϑ}λ) = 0 的轨迹，其局部规则直接继承 Hitchin 的谱覆盖。
- GMN3 里 Hitchin 系统以「class S 理论的 UV 曲线」出现（GMN3 §1 提到的 class S 构造）。

## 4. 读它的前置知识

主丛上的联络与曲率、Hermite–Einstein 度量与稳定性（Donaldson–Uhlenbeck–Yau）、黎曼面的 Teichmüller 理论、以及一点可积系统语言（Lax 对、代数完全可积）。GMN 读者可只读「方程 → 超凯勒 → 谱曲线纤维化」这条主线，分析细节可跳。
