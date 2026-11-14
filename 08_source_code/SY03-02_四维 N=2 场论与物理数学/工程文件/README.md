# 四维 N=2 场论与物理数学 —— 中文译注本

**底本**：Gregory W. Moore, *Four-dimensional N=2 Field Theory and Physical
Mathematics*, arXiv:1211.2331v1 [hep-th], 10 Nov 2012, 19 pp（印刷页 1–18）。
原文为 2012 年 8 月丹麦奥尔堡（Aalborg）国际数学物理大会（ICMP）的综述报告。

**成品规模**：编译后 21 页；中文正文约 1.47 万汉字（源码 5.67 万字符，1229 行）；
编号公式 39 个，编号与原文逐一对应；`% [Tutor Note: ...]` 审校批注 57 条；
脚注 6 条（对应原文脚注 1–6）；参考文献 53 条（编号 [1]–[53] 与原文一致）；
原文插图 **0 幅**（见 §7）。

## 1. 文件清单

```
1211.2331v1(1)_中文译注.tex   ← 单一自足源码（主文件，无外部依赖）
1211.2331v1(1)_中文译注.pdf   ← 编译产物（XeLaTeX 两遍，21 页，含 PDF 书签/目录）
README.md                     ← 本文件
审校批注汇总.md                ← 57 条 [Tutor Note] 的分类索引（不读源码也能查阅）
静态校验报告.txt               ← 交付前静态审计 + 实际编译记录的逐项存档
```

## 2. 编译方法

```bash
xelatex 1211.2331v1(1)_中文译注.tex
xelatex 1211.2331v1(1)_中文译注.tex     # 第二遍生成目录与 PDF 书签
```

或 `latexmk -xelatex "1211.2331v1(1)_中文译注.tex"`。

- 文档类：`ctexart`，**必须用 XeLaTeX**（中文排版；pdfLaTeX 不支持）。
- 依赖宏包（TeX Live / MiKTeX 常规安装均自带）：`geometry, fancyhdr, amsmath,
  amssymb, amsthm, mathtools, bm, graphicx, xcolor, booktabs, array, enumitem,
  caption, hyperref`。精简发行版可运行
  `tlmgr install ctex xecjk fandol enumitem caption mathtools bm fancyhdr`。
- 中文字体：本稿用 `\documentclass[...,fontset=fandol]{ctexart}`，Fandol 字体随
  TeX Live 提供，因此在没有中文字体的最小 TeX 环境中也能编译；若想改用系统字体，
  把 `fontset=fandol` 换成 `fontset=windows`（Windows）或 `fontset=macnew`（macOS）。
- **实测**：TeX Live 2026 + XeLaTeX 两遍编译通过 → 21 页，0 error，0 Overfull，
  0 缺字，2 处 Underfull（均在参考文献的英文折行，纯视觉、可忽略）；目录与 PDF
  书签正常。
- 源码中 `% [Tutor Note: ...]` 是 LaTeX 注释，编译后不显示；删除不影响编译。
- `keypoints` 环境与全部自定义宏都定义在导言区，无需外部文件。

## 3. 排版与翻译约定

1. **公式编号沿用原文**（式 (2.1)、(5.9)、(7.9) 等），用 `\tag{}` 手工标注；
   正文一律写“式 (2.1)”，不做自动交叉引用，便于与英文本逐条对读。
2. **页码对应**：印刷页 = PDF 页 − 1。每节文件头与本文 §6 的对照表均按此标注。
3. **记号统一**：原文 `N=2` 与 `\mathcal N=2` 混用，译本统一写
   $\mathcal N=2$（在 §9 批注中说明）。原文 Hodge 星号 `*` 统一写作 `\ast`
   （如 $F^{I}\ast F^{J}$），以免与普通乘法混淆。
4. **号差**：全篇沿用原文的 $d=4$ 闵可夫斯基号差 $(-,+,+,+)$；在 §2 关于式 (2.1)
   的批注中说明 $\sigma^m$、$P_m$ 的约定及换号差时的改号规则。
5. **术语**：以国内理论物理界通行译法为准（规范场、中心荷、超凯勒、穿墙、谱网络、
   和乐、丛代数等）；无稳定中译的术语保留英文并在首次出现处加括注
   （`framed BPS 态`、`Lefschetz` 类人名等）。人名一律保留拉丁字母。
6. **批注只写三类**：易错预警（指标、符号、归一化、约定）、含糊点拨（作者用
   “显然/结果表明/可以证明”跳过的论证，补出定理与文献）、背景直觉（一两句物理图像）。
   每条批注给出具体信息，避免“很重要”“值得注意”之类的空话。
7. **每节开头「本节重点」**：9 节均有 `keypoints` 环境，含物理图像／数学工具／
   关键结论（多数另有“与前后文的联系”）。

## 4. 章节与原文页码对照

| 章节 | 原文印刷页 | PDF 页 | 编号公式 |
|---|---|---|---|
| 标题页／摘要 | — | 1 | — |
| 目录、§1 引言 | 1–2 | 2–3 | — |
| §2 $d=4$、$\mathcal N=2$ 场论 | 2–4 | 3–5 | (2.1)–(2.6) |
| §3 穿墙现象 101 | 4–5 | 5–6 | (3.1)–(3.3) |
| §4 插曲：局域量子场论中的缺陷 | 6 | 7 | — |
| §5 穿墙现象 102 | 6–8 | 7–9 | (5.1)–(5.12) |
| §6 约化到三维与超凯勒几何 | 8–10 | 9–11 | (6.1)–(6.7) |
| §7 S 类理论 | 10–13 | 11–14 | (7.1)–(7.9) |
| §8 谱网络 | 13–14 | 14–15 | (8.1)–(8.2) |
| §9 结论 | 14–15 | 15–16 | — |
| 致谢 | 15 | 16 | — |
| 参考文献 | 16–18 | 17–19 | — |

## 5. 核心内容速览

- **背景**：$d=4$、$\mathcal N=2$ 超对称场论的低能有效作用量（LEEA）可精确求出
  （Seiberg–Witten 曲线与微分的周期），但 **BPS 谱**长期只能逐例计算。
- **穿墙**：BPS 简并度 $\Omega(\gamma;u)$ 在真空模空间的腔室内分段常值，跨过
  临界稳定性墙时跳变；完整的跳变规律是 **Kontsevich–Soibelman 穿墙公式 (KSWCF)**。
- **推导**：用超对称线缺陷 $L_\zeta$ 与 framed BPS 指标，把穿墙写成扭曲函数代数上
  差分算子 $K_\gamma$ 的乘积；绕临界稳定性墙的单值性直接给出 KSWCF。
- **超凯勒几何**：把 $\mathcal N=2$ 理论紧化到圆上，三维超对称 sigma 模型的靶空间
  $\mathcal M$ 承载超凯勒度量；其扭量空间上的达布函数 $Y_\gamma$ 满足一个与热力学
  Bethe 拟设同型的积分方程 (6.6)，由 BPS 谱数据精确确定。
- **S 类理论与谱网络**：六维 (2,0) 理论紧化在紫外曲线 $C$ 上得到 S 类理论；
  Hitchin 系统给出 Seiberg–Witten 曲线，谱网络 $\mathcal W_\vartheta$ 的跳变
  编码 BPS 谱，并把 Fock–Goncharov 丛坐标推广到高阶。

## 6. 术语对照表（核心条目；完整表见项目工作稿）

| English | 中文 | 备注 |
|---|---|---|
| supersymmetry, $\mathcal N=2$ | 超对称，$\mathcal N=2$ | 记号统一 |
| super-Poincaré algebra | 超庞加莱代数 | $\mathfrak S=\mathfrak S^0\oplus\mathfrak S^1$ |
| central charge | 中心荷 | $Z_\gamma$ |
| R-symmetry | $R$ 对称性 | $su(2)_R$ |
| BPS bound | BPS 界 | 原文 Bogomolnyi |
| BPS spectrum / degeneracy | BPS 谱／BPS 简并度 | $\Omega(\gamma;u)$ |
| wall-crossing | 穿墙 | 穿墙公式 |
| marginal stability wall | 临界稳定性墙 | |
| primitive / semi-primitive formula | 原始／半原始穿墙公式 | |
| halo particle | 晕粒子 | |
| framed BPS state | framed BPS 态 | 首次括注“带框 BPS 态” |
| hyperkähler (HK) | 超凯勒 | |
| hyperholomorphic connection | 超全纯联络 | |
| twistor space | 扭量空间 | |
| Darboux functions / coordinates | 达布函数／达布坐标 | |
| semiflat metric | 半平坦度量 | 原文 §6 |
| Riemann–Hilbert problem | 黎曼–希尔伯特问题 | |
| thermodynamic Bethe ansatz | 热力学贝特拟设 | |
| theory of class S | S 类理论 | |
| ultraviolet curve | 紫外曲线 | $C$ |
| Hitchin system / equations | Hitchin 系统／方程 | |
| spectral network | 谱网络 | $\mathcal W_\vartheta$ |
| WKB path | WKB 路径 | |
| string web / string junction | 弦网／弦交汇 | |
| nonabelianization map | 非阿贝尔化映射 | $\Psi_{\mathcal W}$ |
| cluster algebra / transformation | 丛代数／丛变换 | |
| Teichmüller theory | 泰希米勒理论 | |
| moduli space of flat connections | 平坦联络模空间 | |
| holonomy | 和乐 | |
| defect (line / surface) | 缺陷（线／面） | |
| 't Hooft loop | 't Hooft 圈 | 保留英文 |
| torsor | 扭子 | |
| quiver | 箭图 | |
| vev | 真空期望值 | 保留缩写 |

## 7. 图表核查（原文确无插图）

原文 PDF 共 19 页，逐页核查结果：**嵌入位图 0 幅，矢量绘图对象 0 个，正文与图注
中无 Figure/Diagram 环境**。核查方法（PyMuPDF）：

```python
import pymupdf
doc = pymupdf.open("1211.2331v1(1).pdf")
for page in doc:
    print(len(page.get_images(full=True)), len(page.get_drawings()))
# 全部 19 页输出均为 0 0
```

并逐页渲染（170 dpi）目视复核，未发现任何图形、示意图或照片。因此本译本不含
`figure` 环境，也不存在“漏剥图”的问题。原文中的数学结构（穿墙、扭量空间、
谱网络等）全部以文字与公式呈现。

## 8. 原文疑似笔误与可疑处

| # | 位置 | 原文 | 判断与处理 |
|---|---|---|---|
| 1 | 印刷 p.2（PDF p.3） | “solutions to Einsteins equations” | 缺所有格撇号，应为 Einstein's equations；纯拼写 |
| 2 | 印刷 p.4（PDF p.5） | “Bogomolnyi” | 通行拼法 Bogomol'nyi；正文从通行拼法，§2 批注说明 |
| 3 | 印刷 p.4 / p.6 节标题 | “Wall-crossing 101” vs “Wall Crossing 102” | 大小写不一致；译文统一为“穿墙现象 101/102” |
| 4 | 印刷 p.7 式 (5.2) | 左端 $\mathcal H_\gamma$ 与右端求和指标 $\gamma$ 同名 | 记号冲突；照排并批注（左端指缺陷的整个希尔伯特空间） |
| 5 | 印刷 p.7 式 (5.5) | 分母印作 $2\Im Z_\gamma(u)/\zeta$，缺括号 | 应为 $2\Im\bigl(Z_\gamma(u)/\zeta\bigr)$；正文补括号并批注 |
| 6 | 印刷 p.7 式 (5.7) | $(-1)$ 的指数印作 $\langle\gamma_1,\gamma_2\rangle$ | 应为 $\langle\gamma,\gamma_c\rangle$（由 (5.8) 的 $K_\gamma$ 立得）；正文改正并批注 |
| 7 | 印刷 p.7（PDF p.8） | “the generating function $F(L)$ is is well-defined” | 重复 is |
| 8 | 印刷 p.8 式 (5.10) | 左端 $K_{\gamma_1}K_{\gamma_1}$ | 应为 $K_{\gamma_2}K_{\gamma_1}$（五边形恒等式，与 (5.11) 一致）；正文改正并批注 |
| 9 | 印刷 p.9（PDF p.10） | “there is a holomorphic 2-form form $\varpi$” | 重复 form |
| 10 | 印刷 p.9 式 (6.3) 后 | 公式用 $C^{ij}$，行文称“$C_{ij}$ 是 $\Gamma$ 的辛形式” | 上下标不一致；按“$C_{ij}$ 为辛形式、$C^{ij}$ 为其逆矩阵元素”的通行约定理解，未改，见 §6 批注 |
| 11 | 印刷 p.13（PDF p.14） | “together with the the full sum” | 重复 the |
| 12 | 文献 [18] | 作者 “K. A. Intriligator” | 通行作 K. Intriligator；照原文保留 |
| 13 | 文献 [22]、[28] | 条目末尾无句点 | 照原文保留 |
| 14 | 全文 | `N=2` 与 `\mathcal N=2` 混用 | 原文记号不统一；译本统一为 $\mathcal N=2$，§9 批注说明 |

> 第 4–8、10 条影响数学内容，均已在正文相应位置加 `% [Tutor Note: ...]` 批注，
> 并在 `审校批注汇总.md` 中单独列出；其余为拼写/排印问题，未改动译文内容。

## 9. 已知限制

1. **编译环境**：已在 TeX Live 2026 + XeLaTeX 下实测编译通过（21 页：0 error、
   0 Overfull、0 缺字，2 处参考文献折行 Underfull）。若在更旧的 TeX Live
   （< 2023）或精简发行版上编译，可能需补装 `ctex`、`fandol`、`enumitem`、
   `caption`、`mathtools`、`bm`、`fancyhdr`；报错时把日志发回即可快速定位。
   `% [Tutor Note: ...]` 批注与 `keypoints` 环境不影响编译，可按需删除或保留。
2. **未做逐句回译**：译文以“读懂后重述”为主，长句按中文学术文风拆分；数学内容
   与公式逐符号对照页面图像核对，但个别语序调整未保留英文句法。
3. **批注取舍**：批注聚焦于数学与物理，不解释基础概念；纯拼写/重复字问题汇总在
   §8 表中。
4. **原文无图**：不涉及图表裁切文件；如后续发现其他版本含图，需另行处理。
5. **三处原文笔误按上下文改正**：式 (5.5)(5.7)(5.10) 已在正文采用自洽形式并加批注；
   若需严格照排原文，只需还原这三处、保留批注即可（见 §8 表第 5、6、8 条）。

## 10. 生成方式与可复现性

- 页面图像：PyMuPDF 2.0，170 dpi 渲染（`pages/pNN.png`），公式逐一对图核对。
- 组装：`main.tex`（导言区）+ `work/*.tex` 各节，以脚本展开 `\input` 合并为单一源码。
- 批注索引：脚本从源码自动抽取，批注改动后需重新生成（禁止手改生成物）。
- 静态审计：`tools/final_audit.py` 生成 `静态校验报告.txt`；结果：全部通过。
- 参考文献：53 条与原文逐条比对（连字 ﬁ/ﬀ 已还原，`~` 写作 `$\sim$`）。
