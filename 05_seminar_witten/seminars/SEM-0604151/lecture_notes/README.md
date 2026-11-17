# Kapustin–Witten 理论：几何朗兰兹的物理入门 —— 十讲导读讲义

一份**讲义体**的导读（不是解经本、不是综述），目标是让读者能自己翻开
Kapustin–Witten 2006（arXiv:hep-th/0604151，231 页）从第一页读到 §12。

- 成品：`deliverables/KW_lecture_notes.pdf`（46 页，2026-11）
- 编译：`powershell -NoProfile -ExecutionPolicy Bypass -File build\compile_ln.ps1`
  （两遍 xelatex，输出 `build/out/main.pdf`，并自动拷到 `deliverables/`）
- 质量检查：`python tools/check_lectures.py --strict`
  （每讲四盒齐全、汉字数在区间内、有图或表、无绝对路径 / 无 `\usepackage` / 无 Markdown 粗体）

## 结构

| 部分 | 内容 |
|---|---|
| 写在前面 | 一句话总述、三条读法（3 小时 / 3 天 / 2 周）、前置、记号约定、十讲地图、三条诚实提醒 |
| 第 1 讲 | 舞台：曲线 $C$、群 $G$、Hitchin 模空间 $M_H$（三复结构、维数、Hitchin 纤维化） |
| 第 2 讲 | 四维主角：$\mathcal N=4$ SYM、复耦合 $\tau$、S-对偶、$\Ldual$、Table 1 |
| 第 3 讲 | 扭化：为什么扭、扭出什么、$\mathbb{CP}^1$ 参数族与典范参数 $\Psi$ |
| 第 4 讲 | 紧化：$\Sigma\times C$ → $M_H$ 上的 2d sigma 模型；S-对偶 = 镜像对称 |
| 第 5 讲 | 膜与线算子：A/B 膜、Wilson/'t Hooft、特征膜、局部系统 $\rho:\pi_1(C)\to\LdualC$ |
| 第 6 讲 | 核心等式：'t Hooft 算子 = Hecke 算子（Hecke 修改、仿射 Grassmannian、Bogomolny） |
| 第 7 讲 | 翻译器：A-膜 → D-模（c.c. 膜、开弦 BRST 代数、$f(\Psi)$） |
| 第 8 讲 | 收获与边界：§12 检查表、证明了什么没证明什么、2024 年数学路线、后续读物 |
| 附录 A–C | 术语与符号表（90 条，7 组）、习题（30 题，均带提示）、参考文献与阅读路线 |

## 每讲统一的五个部件

`goals`（本讲目标 3 条）→ 正文（2–4 小节，2,200–3,200 汉字）→
`keybox`（本讲核心，一句话）→ `follow`（跟读提示：原文页段）→ `checkbox`（自检问题 4–6 条）。
所有断言尽量带 `\src{B p.N}` 页锚，回到原文可逐条核对。

## 和另外两份材料的关系

- 219 页**解经本**（`../deliverables/电磁对偶与几何朗兰兹_..._v1.3.pdf`）：逐节深读、四层结构、nLab 注释、60 条原文问答；
- 讨论班第二期（仓库 `05_seminar_witten/seminars/SEM-GL2/`）：八轮报告、112 条语料、独立复算。

这份讲义把两者里「最该先知道的」压成十讲，所以比解经本浅，但更适合第一次读原文。

## 已知薄弱处

1. 第 1 讲 §1.4「为什么可解」依赖 T-对偶与镜像的直觉——原文 §4 本来就没有对偶论证。
2. 第 2 讲 §2.3 GNO ↔ $\Ldual$ 的格论解释只有一行。
3. 第 8 讲 §8.1 三类膜的四维边界条件只列标志性条件，四步推导未展开。
4. 公式编号全书连号（非按讲编号）；TOC 里讲号显示为 1–8（正文标题为「第 N 讲」）。
