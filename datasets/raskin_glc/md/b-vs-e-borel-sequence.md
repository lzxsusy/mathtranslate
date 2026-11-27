# Borel 正合列中的 $B$ 应为 $\cE$

- id：`raskin_glc/correction/b-vs-e-borel-sequence`
- 类型：correction　轨道：B　状态：dev
- 一句话：命题 2.1.5 的证明写 $0\to L\to B\to\cO\to0$ 分裂，其中 $B$ 应为秩 2 向量丛 $\cE$。$B$ 在同页是 Borel 子群，不能充当正合列的中项；同页定义 2.1.1 与脚注都用 $\cE$。

**问题**：为什么把 $\cE$ 写成 $B$ 不是无害的排版问题？

## 位置

§2.1，命题 2.1.5 的证明，原文 p.6（译文 p.8）

## 原文

> the corresponding sequence $0\to L\to B\to\cO\to0$ splits.

## 应为

> the corresponding sequence $0\to L\to\cE\to\cO\to0$ splits.

## 理由

此处 $B$ 已在同页被定义为 $\mathrm{PGL}_2$ 的标准 Borel 子群 $B\subset\mathrm{PGL}_2$，是群而非向量丛；正合列的中项是 $B$-约化所对应的秩 2 向量丛 $\cE$（定义 2.1.1 记作 $\cE$）。若把 $B$ 读成 Borel 子群，正合列 $0\to L\to B\to\cO\to0$ 在类型上就不成立。

## 说明

译文正文照录 $B$，脚注说明应为 $\cE$；这是同一符号在一页内承担两个对象的典型冲突。

## 出处

- Sam Raskin (lecturer), Lin Chen (notes), Notes for ``Geometric Langlands for Projective Curves'', July 07--11, 2025, 18 pp.，§2.1，命题 2.1.5 的证明，pp. 6；`源码/sections/s02-cusp.tex:L62-L64（正文与译注）`
  > the corresponding sequence 0 →L →B →O →0 splits.

## 相关卡

- `raskin_glc/concept/cuspidal-sheaf`

## 核验（partial，2026-11-27）

- 底本 §2.1（A） / 定义 2.1.1 与命题 2.1.5 同页：`supports` — 定义 2.1.1 用 E 记 Bun_B 上的秩 2 向量丛；B 在同页被定义为 Borel 子群。

符号冲突由同页上下文即可判定，不需要外部文献。
