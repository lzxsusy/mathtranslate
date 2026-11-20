# 《镜像对称与代数几何》全书中文译排

## 完成范围

译稿从原书前言起，覆盖原扫描 PDF 物理页 14–492：前言、符号说明、十二章正文、附录 A、B、完整英文参考文献及全部原书索引。物理页 23、37、53、239、353、419、459、475 为原书空白页；135、189、297 均有正文。前面的出版资料不译。原书 493 为留白，494 为丛书广告，495 为封底宣传。全书译排 PDF 共 403 页。

最后一批接续物理页 476–492，共 17 页原书索引；原书剩余内容不足 50 页。索引 1458 个条目全部人工译入并保留从属层级，427 个主条目按中文排序规则编排，英文人名和数学符号保留。原书的页码换算为译本页码；338 处跨页的索引引用使用正文实际词条的独立标签定位。其余引用按对应原页的正文起点映射。同页去重，相邻页合并为范围；页码和全部“参见／另见”目标均可点击。索引在译本中占 24 页。

## 排版与文件

- 用户提供的 ElegantBook 4.7 类文件；正文 11pt。
- 中英文字体采用 ElegantBook 的 Windows 原生配置；数学字体为 New Computer Modern Math。
- 交付 PDF 的全部字体已经嵌入，可在其他设备显示，不依赖阅读设备安装这些字体。
- 原生 ElegantBook 封面；生成的替换图片为 1536×1024、3:2 横幅。
- 原书为整页扫描，没有可拆出的矢量插图。十九幅插图直接从原扫描像素裁切，图中文字不翻译、不重绘，并依原书相对宽度缩放。
- 定理、引理、推论、命题、定义、例题、笔记和证明等使用 ElegantBook 环境；例题、练习、问题按原书所在节编号。
- 目录与书签保留原书目录的章、节层级；正文仍保留小节及其编号。
- 主文件包含 hyperref 与 titlesec 的加载次序兼容处理，使分页后的节标题目标随标题定位；原生类文件与标题样式保留。两处跨页例题的引用目标设在例题起始文字处。
- 公式、定理和章、节及附录等内部交叉引用可点击；文献引用链接到英文书目条目，中文索引页码链接到正文，索引参见链接到对应条目。前言及符号说明的续页页眉分别显示其本身的标题。
- `chapters/references.tex` 收录全部 325 条原书文献及原书说明，保留英文和原书顺序；原书提供的 arXiv 标识符和网址已添加链接。原书有两组重复书目标签，显示仍保留 BD、KS；Bjorken/Drell 与 Katz/Strømme 条目分别使用独立内部键 BjoD、KaS，正文链接对应各自条目。

压缩包包含 `main.tex`、`elegantbook.cls`、`chapters/`、`figure/` 以及本说明，不含原扫描 PDF、OCR、预览图或编译缓存。

## 编译

在本目录使用 XeLaTeX。Windows 源码编译需要 ElegantBook 默认使用的宋体、黑体、楷体和仿宋字体，以及 TeX Live 中的 New Computer Modern Math 等依赖。阅读交付 PDF 无需安装字体。

```powershell
xelatex -interaction=nonstopmode -halt-on-error main.tex
biber main
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

书目正文使用保留原书标签的 LaTeX `thebibliography` 环境；这里的 biber 仅完成 ElegantBook 原生加载的空 biblatex 后端，消除其重编译提示，不改动英文书目。完整索引已保存在 `chapters/index.tex`，使用原生索引环境排版，无须运行 makeindex 或任何翻译脚本。多次 XeLaTeX 编译用于稳定目录、索引页码映射及交叉引用。

## 统一术语

| English | 中文 |
| --- | --- |
| mirror symmetry / mirror map | 镜像对称 / 镜像映射 |
| Calabi–Yau manifold / quintic threefold | Calabi–Yau 流形 / 五次三维簇 |
| quantum cohomology / Gromov–Witten invariant | 量子上同调 / Gromov–Witten 不变量 |
| toric variety / fan / cone | 环面簇 / 扇 / 锥 |
| polytope / facet / normal fan | 多胞形 / 刻面 / 法扇 |
| polar / reflexive polytope | 极多胞形 / 自反多胞形 |
| homogeneous coordinate ring / Chow group | 齐次坐标环 / Chow 群 |
| primitive collection / primitive cohomology | 本原集合 / 本原上同调 |
| ample / very ample / semiample | 丰沛 / 十分丰沛 / 半丰沛 |
| Kähler cone / Mori cone | Kähler 锥 / Mori 锥 |
| symplectic reduction / moment map | 辛约化 / 矩映射 |
| maximal projective subdivision | 极大射影细分 |
| monodromy / maximally unipotent | 单值性 / 最大幺幂 |
| cycle / vanishing cycle | 圈 / 消失圈 |
| nilpotent / quasi-unipotent | 幂零 / 拟幺幂 |
| variation of Hodge structure / Hodge filtration | Hodge 结构变分 / Hodge 滤过 |
| exact form / residue | 恰当形式 / 留数 |
| orbifold / involution / isogeny | 轨形 / 对合 / 同源映射 |
| nef partition / monomial-divisor mirror map | nef 分拆 / 单项式–除子镜像映射 |
| linear circuit / flip / flop | 线性回路 / 翻转 / 翻越 |
| movable cone / primitive contraction | 可动锥 / 本原收缩 |
| normalization (variety) / normal crossing | 正规化 / 正规交叉 |
| normalization (function) / integrality conjecture | 归一化 / 整性猜想 |
| blow-up / blow-down / phase | 爆破 / 爆缩 / 相 |
| extremal transition / conifold transition | 极端跃迁 / 锥形奇点跃迁 |
| node / ruled surface / pencil | 结点 / 直纹曲面 / 线性系 |
| stack / stable map / prestable curve | 代数叠 / 稳定映射 / 预稳定曲线 |
| virtual fundamental class / evaluation map | 虚拟基本类 / 赋值映射 |
| normal cone / intrinsic normal cone | 法锥 / 内蕴法锥 |
| excess normal bundle / obstruction / perfect | 超额法丛 / 障碍 / 完美 |
| tamed / almost complex / semi-positive | 受驯服 / 几乎复 / 半正 |
| cobordism / pseudomanifold / proper | 协边 / 伪流形 / 固有 |
| small / big quantum cohomology | 小量子上同调 / 大量子上同调 |
| instanton number / tree-level | 瞬子数 / 树级 |
| supermanifold / supercommutative | 超流形 / 超交换 |
| potential / fermion | 势 / 费米子 |
| Dubrovin connection / Frobenius manifold | Dubrovin 联络 / Frobenius 流形 |
| localization / equivariant cohomology | 局部化 / 等变上同调 |
| flag / valence / smoothing | 旗 / 价数 / 光滑化 |
| gravitational correlator / descendant | 引力关联数 / 引力后裔 |
| dilaton axiom / topological recursion relation | 伸缩公理 / 拓扑递推关系 |
| partition function / Euler data | 配分函数 / Euler 数据 |
| linked / convex / concave / concavex | 相关联 / 凸 / 凹 / 凸凹 |
| quantum hyperplane section principle | 量子超平面截面原理 |
| critical bundle / double construction | 临界丛 / 双重构造 |
| canonical / terminal singularity | 典范奇点 / 终端奇点 |
| Q-factorial / gauged linear sigma model | Q 析因 / 规范线性 σ 模型 |
| action / Lagrangian / Hamiltonian | 作用量 / Lagrange 量 / Hamilton 量 |
| conformal field theory / primary field | 共形场论 / 初级场 |
| chiral ring / twisted sector | 手征环 / 扭曲部分 |
| topological quantum field theory | 拓扑量子场论 |
| Frobenius algebra / cobordism | Frobenius 代数 / 协边 |
| expected dimension / integral lattice | 预期维数 / 整数格 |
| flag manifold / tangent–obstruction complex | 旗流形 / 切—障碍复形 |
| A-system / GKZ system | A 方程组 / GKZ 方程组 |
| étale / universal | 平展 / 万有 |
| deformation / signature | 形变 / 号型 |
| bipyramid / Berglund–Hübsch transpose rule | 双棱锥 / Berglund–Hübsch 转置法则 |
| energy–momentum tensor | 能动量张量 |
| note / example / exercise / problem | 笔记 / 例题 / 练习 / 问题 |

英文人名、参考文献条目及图内文字保留原文。
