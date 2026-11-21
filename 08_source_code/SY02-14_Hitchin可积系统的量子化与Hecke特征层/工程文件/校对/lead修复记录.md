# Lead 直接修订记录

只记 lead（主译）亲手做的、跨单元的全局修订，供第二轮校订与交付报告引用。
格式：日期 | 文件 | 位置 | 原 | 改 | 理由。

## 2026-11-21

1. `源码/main.tex` | `\bdsec` 宏 | `\addcontentsline{toc}{section}{#1}` | `\addtocontents{toc}{\protect\contentsline{section}{#1}{\thepage}{}}` | 节标题带 `$...$` 数学时 hyperref 写书签触发 `! Improper alphabetic constant`（ch07_u01 的 `7.2. $\mathcal{D}$- 与 $\Omega$-模` 复现 100 个错误）。改后全书 0 error，目录正常显示数学标题。

2. `源码/units/ch04_u04.tex`（6 处）| 半直积 | `\rtimes` | `\ltimes` | 原书 p.163 放大 600 dpi 核对，字形为 ⋉（`Aut₂O ⋉ SO_n(K)`）；同章 u03/u05 均用 `\ltimes`，统一。

3. `源码/units/ch04_u06.tex`、`ch04_u07.tex`、`ch05_u04.tex`（共 25 处）| 上标 loc/glob | `^{loc}`、`^{glob}` | `^{\mathrm{loc}}`、`^{\mathrm{glob}}` | 原书印正体；与 `ch04_u05` 已有写法统一。

## 待办（第二轮校订时处理）

- 跨单元断句接缝：ch04_u01→u02（p.132）、ch05_u01→u02（p.200「故按」+「Deligne 定理」已核）、ch06→ch07（p.236）、ch07 各单元之间。
- `\rtimes`/`\ltimes` 之外，检查 `\ltimes` 与 `\rtimes` 是否仍有混用（全局 grep）。
- `h` 与 `\hbar`：p.68 与 p.91 原书印刷不同，保留分歧并在术语表加注。
