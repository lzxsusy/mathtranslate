# 分章报告：§2.2–2.3（chapters/sec02b.tex）

## 一、翻译要点
- 覆盖原书 p.5–9：§2.2 例 1–3 与图 1–5；§2.3 未正规化／正规化的 Morse 收缩，式 (9)–(22)、脚注 6。
- 编号公式 15 条（(8)–(22)）全部 `\tag` 保留原号；未编号行间公式 7 处（例 1、例 2、链修改版的复合映射，例 2 维数公式，$\delta^\epsilon_Z$ 定义，$\mathrm{d}h+h\mathrm{d}$，$[\mathrm{d}_X,K]$ 恒等式）用 `\[ \]`。
- 图 1–5 用 `figure`，标签 `fig:1`–`fig:5`，caption 中译并标“（原书 p.N）”；宽度按原书版面比例（0.35／0.76／0.76／0.20／0.30 `\linewidth`）。
- 公式逐行对 p07–p09 页面图核对；式 (8) 的 `\underbrace`、δ 的复合下标（$\delta_{\mathrm{Unstab}P}$、$\delta^\epsilon_{\mathrm{Unstab}P}$）、式 (22) 的映射图另做 350 dpi 裁剪复核。
- 批注 10 条：图 1 标号读法、图 2 的 $\epsilon\to0$ 与伪全纯、例 2 维数公式逐项、例 3 的 (7)$\to$(8) 展开、$i$／$p$ 的稳定-不稳定流形、式 (9) 的 $\iota_v$ 与交换性、式 (14) 的指数简写、(16) 笔误与 $\widetilde Y$ 边界、式 (18) 的链同伦、正规化动机。

## 二、术语裁定请求
- 新增两条，请 Lead 决定是否入表：broken trajectory → 断裂轨道（首次括注英文）；interior product $\iota_v$ → 内乘。
- Lefschetz thimble 按裁定在式 (10) 处首次括注“莱夫希茨顶针”，此后用英文。

## 三、疑似笔误（保留原样＋同处批注）
- 原书 p.8：the gradient trajectory **of** starting at y（多一 of）。译文按无 of 理解，其余照录。

## 四、存疑
- 式 (9) 下方 writing $U=e^{-(\mathrm{d}_t+[\mathrm{d}_X,-])(t\iota_v)}$ 是指数记号滥用（原文如此），照录并批注。
- 式 (22) 原书用长双箭头（上 $i^\epsilon$、下 $p$），排版以 `\rightleftharpoons` 加 `\overset`／`\underset` 近似；若要视觉一致请 Lead 统一（如 `tikz-cd`）。
- `\cite{witten,frenkel}` 在 natbib `sort&compress` 下排为 [4,17]，与原文 [17],[4] 顺序不同（内容一致）。

## 五、自检
- `work/lint.py chapters/sec02b.tex`：**PASS，0 FAIL，4 warn**（均为跨文件 `\ref`：`sec:2.1`、`eq:4`、`eq:7`、`sec:4.1`）。
- 规模：汉字约 2100，编号式 15，未编号行间式 7，图 5，批注 10；文件以 `\endinput` 结尾。
