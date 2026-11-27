# 「holonomic 模形式」应为「holomorphic 模形式」

- id：`raskin_glc/correction/holonomic-vs-holomorphic`
- 类型：correction　轨道：B　状态：dev
- 一句话：原文写「a (holonomic) modular form」，括号里的 holonomic 应为 holomorphic（全纯）。holonomic 是 D-模的有限性条件，与模形式的全纯性无关；上下文正在定义权 k、级 1 的模形式，只能是全纯。

**问题**：holonomic 与 holomorphic 只差一个字母，为什么不能算拼写瑕疵？

## 位置

§2.2，模形式动机，原文 p.7（译文 p.8）

## 原文

> Recall a (holonomic) modular form (of weight $k$ and level 1) is a sum ...

## 应为

> Recall a holomorphic modular form (of weight $k$ and level 1) is a sum ...

## 理由

模形式按全纯性分为全纯模形式与非全纯（Maass）情形；这里要的是 $q$-展开 $f=\sum a_nq^n$、$f(g\tau)=(c\tau+d)^kf(\tau)$ 的全纯模形式。holonomic 是 $D$-模的术语（holonomic $D$-module），指解的有限维性，与「模形式是否全纯」不是同一层面的性质。

## 说明

译文正文照录 holonomic 并加注；这是「术语误植」而非普通拼写错误，因为两个词各自都有确定含义。

## 出处

- Sam Raskin (lecturer), Lin Chen (notes), Notes for ``Geometric Langlands for Projective Curves'', July 07--11, 2025, 18 pp.，§2.2，模形式动机，pp. 7；`源码/sections/s02-cusp.tex:L147（正文与译注）`
  > Recall a (holonomic) modular form (of weight k and level 1) is a sum f =

## 相关卡

- `raskin_glc/concept/coefficient-functor`

## 核验（partial，2026-11-27）

- nLab, modular form / Definition：`supports` — 模形式是上半平面上的全纯函数，并满足 SL_2(Z) 的变换规则；支持 holomorphic。
- Diamond–Shurman, A First Course in Modular Forms, GTM 228 / Ch. 1：`supports` — 全纯模形式的定义与 q-展开；holonomic 不在模形式的标准术语中。

holonomic 作为 D-模术语本身另有含义，故本条不是纯拼写表能覆盖的。
