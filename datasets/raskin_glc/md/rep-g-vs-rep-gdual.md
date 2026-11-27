# $\Gd$-局部系统的函子定义误写 $\Rep(G)$

- id：`raskin_glc/correction/rep-g-vs-rep-gdual`
- 类型：correction　轨道：B　状态：dev
- 一句话：原文把 $\Gd$-局部系统定义为右 t-正合对称幺半函子 $\Rep(G)\to\Shv(X)$；按上下文（$\Gd$-局部系统、$V_\sigma$、下一句 $V\in\Rep(\Gd)$）应为 $\Rep(\Gd)\to\Shv(X)$。$\Rep(G)$ 是 $G$-丛的表示，方向正好相反。

**问题**：为什么 $\Rep(G)$ 与 $\Rep(\Gd)$ 不能互换？

## 位置

§4.1，$\Gd$-局部系统的定义，原文 p.12（译文 p.14）

## 原文

> $\Rep(G)\to\Shv(X),\quad V\mapsto V_\sigma$.

## 应为

> $\Rep(\Gd)\to\Shv(X),\quad V\mapsto V_\sigma$.

## 理由

$G$-丛 $P_G$ 给出函子 $\Rep(G)\to\QCoh(S)$，$V\mapsto V_{P_G}$；对偶地，$\Gd$-局部系统给出函子 $\Rep(\Gd)\to\Shv(X)$，$V\mapsto V_\sigma$。原文上一段刚用 $\Rep(G)\to\QCoh(S)$ 定义 $G$-丛，紧接着的 $\Gd$-局部系统若仍写 $\Rep(G)$，就把两个方向混同了；下一句「若 $V\in\Rep(\Gd)$ 有限维，则 $V_\sigma$ 是 lisse 的」也证明这里应是 $\Rep(\Gd)$。

## 说明

译文正文照录 $\Rep(G)$，脚注给出 $\Rep(\Gd)$；这是「对偶群写漏 check」的典型，不是排版。

## 出处

- Sam Raskin (lecturer), Lin Chen (notes), Notes for ``Geometric Langlands for Projective Curves'', July 07--11, 2025, 18 pp.，§4.1，$\Gd$-局部系统的定义，pp. 12；`源码/sections/s04-hecke.tex:L35-L38（正文与译注）`
  > Rep(G) →Shv(X), V ↦Vσ.

## 相关卡

- `raskin_glc/concept/geometric-satake`
- `raskin_glc/concept/hecke-eigensheaf`

## 核验（partial，2026-11-27）

- 底本 §4.1 上下文（A） / 紧邻的上一段与下一句：`supports` — 上一段用 Rep(G)→QCoh(S) 定义 G-丛；下一句写 V∈Rep(Ĝ)，V_σ lisse。
- Gaitsgory–Raskin, GLC I, arXiv:2405.03599 / §1.2：`supports` — Ĝ-局部系统是 Rep(Ĝ)→Shv(X) 的对称幺半函子；确认方向。

修正不涉及任何定理内容，只恢复对偶群记号。
