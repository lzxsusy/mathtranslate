---
id: glc/concept/averaging-functor
type: concept
track: D
---

# 平均函子 Av_E^d

> 沿 Hecke 叠 Mod_k^d 先拉回、再乘 π^*L_E^d、再紧支撑推前定义的函子，带 [dk](dk/2) 归一化。

**问题**：平均函子 Av_E^d 的核与归一化分别是什么？

## 定义

令 $\operatorname{Mod}_k^d$ 为 Hecke 叠
\[
\operatorname{Mod}_k^d=\{M\subset M',\ \operatorname{length}(M'/M)=d\},
\]
带有映射 $h^{\leftarrow},h^{\rightarrow}:\operatorname{Mod}_k^d\to\operatorname{Bun}_k$ 与 $\pi:\operatorname{Mod}_k^d\to\operatorname{Tor}$，其中 $\pi(M\subset M')=M'/M$。平均函子定义为
\[
\operatorname{Av}^d_E(-):=\overrightarrow{h}_!\bigl(\overleftarrow{h}^*(-)\otimes\pi^*\mathcal{L}_E^d\bigr)[dk](dk/2).
\]

*记号*：$\overleftarrow{h}$ 记录子层 $M$，$\overrightarrow{h}$ 记录扩层 $M'$；$[dk](dk/2)$ 是与 §5.2 同型的相对移位与 Tate 扭转。

## 要点

- $\operatorname{Mod}_k^d$ 记录 $\operatorname{Bun}_k$ 中长度为 $d$ 的修改。
- 平均函子的核是 $\pi^*\mathcal{L}_E^d$。
- 归一化 $[dk](dk/2)$ 中的 $dk$ 是相对维数 $d\cdot k$。
- 满射情形把所需的 $!$-推前化为 $\operatorname{Av}^d_E$ 的一个茎；基础情形则化为 $\operatorname{Av}^d_E(W_k)$，其中 $W_k$ 是基础 Whittaker 层（见 §6.3）。两者不是同一个对象。

## 关键公式

- $\operatorname{Av}^d_E(-)=\overrightarrow{h}_!(\overleftarrow{h}^*(-)\otimes\pi^*\mathcal{L}_E^d)[dk](dk/2)$
- $\operatorname{Mod}_k^d=\{M\subset M'\mid\operatorname{length}(M'/M)=d\}$

## 易错点

- 不要把 $d$ 与层的次数混为一谈：这里 $d=\operatorname{length}(M'/M)$ 是修改的长度。
- 注意两个方向的箭头：$\overleftarrow{h}$ 是拉回用的子层投影，$\overrightarrow{h}$ 是紧支撑推前用的扩层投影。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§5.7 洁净性与平均消失，p.35（PDF p.35），`源码/chapters/ch05.tex:107-112（§5.7 Mod_k^d 与平均函子）`

## 核验

状态：`source-only`（2026-11-18）
- Gaitsgory 2002 (arXiv:math/0204081)：https://arxiv.org/abs/math/0204081 — §1.2 defines Av_E^d(F)=h←_!(h→^*(F)⊗s^*(L_E^d))[nd] (paper's convention: pull back along h→, push forward along h←). The book's formula has the opposite h←/h→ assignment and an extra (dk/2) twist; same shape, not verbatim. The paper says nothing about the ch6 base/surjective cases.

## 关联

- `glc/concept/vanishing-theorem`
- `glc/concept/normalized-degree`
- `glc/concept/base-whittaker-sheaf`
