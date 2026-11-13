# afterword 施工报告

## 负责页段
PDF 185–196 = 原书 p.176–187（「あとがき」后记，12 页），由 Lead 本人翻译。

## 文件
- `src/chunks/afterword.tex`：34,657 bytes（约 33.8 KB），308 行，UTF-8 无 BOM。
- 体例：`\chapter*{后记}` + `\addcontentsline{toc}{chapter}{后记}` + `\markboth{后记}{后记}`；末尾不写 `\chapterreview`（后记非正文章）。

## 结构
- 先列各章参考书（16 条日文文献，用 `quote` 夹排，如「[森田 05] 森田茂之，《微分形式的几何学》，岩波书店，2005 年」）；
- 再讲正文未展开的发展话题：三体问题（Šuvakov–Dmitrašinović [123]、Albers–Frauenfelder–van Koert–Paternain [4]）、邻近 Lagrange 猜想、Liouville 区域／Stein 区域／wrapped Fukaya 范畴、GIT 与动量映射、conifold 的三种解消（奇点解消／复结构形变／链环）、AdS/CFT 与 Sasaki–Einstein（(1)–(10) 的 conifold 形变计算）、锥流形转迁与 Gopakumar–Vafa、矩阵模型与拓扑引力／Witten 猜想／Kontsevich、Hermite Yang–Mills 与 Kobayashi–Hitchin 对应（(11)–(18)）、Verlinde 与 Witten 公式、Goldman 系／弯曲系、抛物向量丛与 Mehta–Seshadri、Chern–Simons 与 2+1=3（(19)）、反自对偶与 Donaldson 理论、瞬子 Floer 与 Atiyah–Floer 猜想（(21)(22)）、超 Kähler／ALE／引力瞬子／Klein 奇点／箭图簇、Higgs 丛与 Hitchin 系（(23)(24)）、单值保持形变与 Frobenius 流形／镜像对称。
- 24 个编号公式全部用 `\begin{equation*}…\tag{N}\end{equation*}` 照录原书号（**注意：`\tag` 只写数字**，曾误写 `\tag{(1)}` 导致显示成 ((1))，已用正则 `<本地路径>)\)\}` → `\tag{$1}` 全文修正）。

## 编译判据
`powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk afterword`：

```
LOG  file:line=0  fatal=0  undefined=0  missingchar=0  overfull=0  undefref=0
```

- 草稿 PDF：`tmp_afterword.pdf`，共 10 页；渲染第 1、4 页：公式右对齐编号、quote 缩进正常。
- 全量编译（16:26）中本章无告警（preamble 新增 `\Ext`、`\MCG`，并已把 `\xeCJKDeclareCharClass{CJK}{"0400->"04FF}` 加在 `\parindent` 之前以渲染西里尔字母）。
- 已把批注中的裸 unicode 数学（`∫_M dω`、`(dω,η)=(ω,δη)`、`L²`、`∂`）改为 LaTeX：`$\int_M \rd\omega = \int_{\partial M}\omega$` 等；`・` 改 `·`（「季刊·数学」）。

## 批注（共 13 条：背景 5 / 难点 3 / 校勘 5）

| 原书页 | 类型 | 内容 |
|---|---|---|
| p.176 | 背景 | 原书在此只提「邦訳」（日译本）；中译本读者更常用的是中译本：Landau–Lifshitz《力学》、Arnold《经典力学的数学方法》，读者若找不到日译本可径用中译本对照，公式编号一致。 |
| p.176 | 难点 | Stokes 定理「伴随」说法指 $(d\omega, \eta) = (\omega, \delta\eta)$ 这一形式伴随关系：外微分 d 与余微分 $\delta$ 在 $L^2$ 内积下互为伴随，而 $\delta$ 正是边缘算子 $\partial$ 在链复形层面的对偶。 |
| p.176 | 背景 | 森田茂之《微分形式の幾何学》与松本幸夫《多様体の基礎》都是日本流形论的标准入门书，前者以 de Rham 理论见长，后者以定义细致、图多著称。 |
| p.176 | 校勘 | 原书正文作「複素幾何」；中译名「复素几何」中的「素」为日文「複素＝complex」的直译，中文习惯作「复几何」。此处照录原书名，正文行文一律用「复几何」。 |
| p.177 | 校勘 | 原书作「第 5 章を書く際には」；但所列 [110]、[13]、[高崎 01] 均为完全可积系统（第 6 章）的文献，且上下文正讨论第 6 章，故疑为「第 6 章」之误。 |
| p.179 | 校勘 | 原书此句为「[三松 01] が日本数学会のホームページからダウンロードできる」，指该文可从学会网页下载 PDF，而非指书。 |
| p.180 | 校勘 | 原书「同次直線束」的「同次」二字，扫描件字迹与 OCR 均不清晰（OCR 读作「同音」）；按上下文应为「同次直线丛」（homogeneous line bundle）。中译本取「同次」。 |
| p.180 | 背景 | (1)–(7) 是 conifold 的「形变」描述：$Y_\varepsilon$ 是以 $S^3$ 为底的 $\R^3$ 丛，即 $TS^3$，与 $T^*S^3$ 辛同胚；$\varepsilon\to0$ 时退化到奇点 $w_1^2+\cdots+w_4^2=0$。 |
| p.181 | 背景 | 佐佐木流形的 Riemann 锥为 Kähler 这一等价，是 Sasaki–Einstein 几何的出发点；$S^5$ 的锥就是 $\C^3\setminus\{0\}$，故 $S^5$ 与 $S^2\times S^3$ 的圆锥都对应 Kähler 锥，这正是 AdS/CFT 里把 $S^5$ 换成 Sasaki–Einstein 流形的几何依据。 |
| p.181 | 校勘 | 原书「超対称殻ゲージ理論」的「殻」字义不可通（OCR 亦不确定），按上下文（Klebanov–Witten 模型、quiver gauge theory）应读作「超对称规范理论」。中译本按「超对称规范理论」处理。 |
| p.183 | 难点 | (11) 中的 $\Lambda$ 是关于 Kähler 形式的内乘；$\Lambda F_A=\mu\,\id$ 是「常中心曲率」条件的矩阵形式：$F_A$ 的 $\omega$-迹（中心部分）为常数 $\mu$ 乘恒等。$X$ 为曲线时 $F_A$ 是 $(1,1)$ 形式，$\Lambda F_A$ 就是标量曲率。 |
| p.186 | 术语 | 原书「箙多様体」即 quiver variety，中译通作「箭图簇」。此处与第 10 章译名统一（10.7 节名 OCR 作「臨」，实为「箙」）。 |
| p.186 | 难点 | (24) 中 $\Ext^1(\mathcal{E},\mathcal{E})^*$ 与 $T^*_{[\mathcal{E}]}\mathcal{M}$ 的等同来自形变理论：$\Ext^1$ 分类 $\mathcal{E}$ 的一阶形变，故是切空间；Higgs 场 $\Phi\in H^0(\omega_X\otimes\End\mathcal{E})$ 由 Serre 对偶正是余切向量，故 Higgs 丛模空间＝余切丛，自动带超 Kähler 结构。 |

## 校勘与遗留
- 「第 5 章」→「第 6 章」、「殻→对称」两处为原书疑误，译文按上下文处理并在批注说明，正文不加脚注、不改原意。
- 后记中 `\tag` 24 个全部照录原书 (1)–(24)，与正文章号无关（后记为独立编号）。
- 无遗留问题。
