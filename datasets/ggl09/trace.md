# 09 判断轨迹

| # | 判断点 | 依据 | 结论与理由 | 事后确认 |
|---|---|---|---|---|
| 1 | (2.3) 第三式的符号：txt 作 $d_A^*\varphi+i[\sigma^\vee,\sigma^\vee]=0$，按此算 $i[\sigma^\vee,\sigma^\vee]=0$，与 (2.6) 的 $+[X_1,X_2]$ 冲突（**弯路**） | txt/09/p011.txt 与式号 | 先怀疑自己算错，重算两遍仍差一个 $[X_1,X_2]$；改看 PDF 渲染 external/pages/p-11.png，发现原文是 $[\sigma^\vee,\bar\sigma^\vee]$，txt 丢了横线 | 重算 $i[\sigma^\vee,\bar\sigma^\vee]=[X_1,X_2]$，与 (2.6) 完全一致；D1 第 3 步按此写 |
| 2 | (2.15) 左端缺 $\vee$：初判为 pdftotext 提取错误（**弯路**） | txt 与 PDF 文本层都缺 | 渲染 p-19.png 逐字核对，印刷体确实作 $P_i^{(2)}$ 与 $\partial P_i/\partial\sigma^\vee$；再查 v1.txt:1040，v1 同样缺 | 立 errata E1（low，open），卡片保留原文并在定义里注明校正读法 |
| 3 | 外部 C 源页码：本想引 KW06 p.127 作卡片 C 源 | lint 的 `--max-pages 37` | KW06 的相关页远超 37，塞进卡片必被 lint 拒；改为在 notes 外部来源表记录 KW06，卡片 C 源改用 ggl12 p.46–47、ggl21 p.34/42（≤37） | 重跑 lint 通过；notes 表 6 行覆盖 KW06 |
| 4 | 卡标题撞名：初稿用『Bogomolny 方程』『正则 Nahm 极点』 | term_index 对 title+aliases 做归一化精确匹配；kw06、ggl12 已有同名卡 | 改成带限定词的标题（带奇点的…、Nahm 极点作为…），别名的英文写法也换掉 | term_index check 无撞名 |
| 5 | $d_A^*$ 的约定：先按 $-\star d\star$ 算，得 $X_3'$ 前负号（**弯路**） | 常见场论约定 | 与 (2.6) 的 $+[X_1,X_2]$ 冲突；查 p.11 紧邻正文『$d_A^*=\star d_A\star$』无负号 | 采用无负号，符号自洽；D1 的 gap 里记下约定依赖 |
| 6 | (2.9) 的系数：试从 (2.8) 解 2-形式部分 | 只有结果，无中间步骤 | 形状能对上，$\psi\wedge\psi$ 项的 $1/2$ 与符号依赖 $\psi$ 归一，无法唯一确定 | 不硬写推导，D2 的 gap 与 notes『不懂』都记 |
| 7 | v1 与 v2 的差异：原以为只差参考文献 | pdftotext 后 diff | v1 p.32 (3.14) 作 $+$，v2 作 $-$；v1 同页上一行已写 $-$，自相矛盾 | 记入 notes『版本差异』；因是版本修正而非本篇笔误，不入 errata |
| 8 | $N(\rho)$ 与 $\overline N(\rho)$：初以为紧化只是拓扑完备化 | p.3 原文 | 紧化允许 type 变小（monopole bubbling），因此不是单纯加边界 | 改写 C2 的定义与 key_point |
| 9 | $bB$ 态空间：初以为也是某个上同调 | p.13–14 | Nahm 解唯一、模空间一点，故 $\mathcal H=R^\vee$；无标记点时 $\mathbb C$ | 改写 C6；与 T6 一致 |
| 10 | pole 是否可用任意 $\mathfrak{sl}_2$：初稿写『$\mathfrak{sl}_2$ 嵌入』 | p.12 | 必须 principal（不可约）；不可约嵌入必共轭于 principal | C5 的 key_point 与 pitfalls 补上 |
| 11 | $x_i(S)$ 是态还是算符：初稿写成态 | p.16 Remark 2.1 | $S$ 定在固定时刻，$x_i(S)$ 是作用在 $\mathcal H$ 上的算符 | 改写 C7 与 D2 |
| 12 | (2.18) 的指数：初算 $\gamma^\vee$ 为 $d_i$、$n_g$ 为 $d_i$（**弯路**） | 只看 (2.16) | 代入 (2.17) 的 $(\gamma^\vee)^{-1}$ 后才得 $d_i-1$ 与 $d_i/2$；漏代入会整体差一次幂 | D3 第 2 步改正并写进 pitfalls |
| 13 | quadric 上的点是否给新理论：初稿把 $Q$ 上点当新理论（**弯路**） | p.30 | $Q$ 上是来自 4d 紧化的 $\mathbb{CP}^1$ 族；补集才是单个轨道、$Z_2$-分级的新理论 | 改写 C10 的 key_points 与 pitfalls |
| 14 | 融合态空间：初以为多标记点会改变 $N(\rho)$ | p.21 (2.19)(2.20) | $\mathcal H=\otimes_\alpha H^*(N(\rho_\alpha))$，$x_i$ 作用为各因子之和 | 与 T1 的 OPE 一致，未单独立卡 |
