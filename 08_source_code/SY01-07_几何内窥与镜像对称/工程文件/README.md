# 几何内窥与镜像对称（中文译注本）

**原文**：Edward Frenkel & Edward Witten, *Geometric Endoscopy and Mirror Symmetry*,
arXiv:0710.5939v3 [math.AG]，2008 年 4 月 5 日，130 页（正文 3--127，参考文献 127--130）。

**成品**：`Frenkel-Witten_几何内窥与镜像对称_0710.5939.pdf` + 可编辑 LaTeX 源码（单文件版与分片版）。

---

## 一、目录结构

```
Frenkel-Witten_几何内窥与镜像对称_0710.5939/
├── Frenkel-Witten_几何内窥与镜像对称_0710.5939.pdf   成品（已编译）
├── Frenkel-Witten_几何内窥与镜像对称_0710.5939.tex   单文件全文源码（自包含）
├── main.tex                分片版主文件（标题、摘要、目录、\input 各分片）
├── preamble.tex            导言区：宏包、版式、定理/重点环境、记号宏
├── sections/
│   ├── s01-intro.tex       §1 引言（Lead 样板）
│   ├── s02-duality.tex     §2 对偶、膜与内窥
│   ├── s03a-genus1.tex     §3 亏格一显例（3.1--3.5）
│   ├── s03b-genus1.tex     3.6--3.11
│   ├── s04a-branes.tex     §4 A-膜与 D-模（4.1--4.6）
│   ├── s04b-branes.tex     4.7--4.9
│   ├── s05a-spectral.tex   §5 谱覆盖、Hecke 算子与高亏格（5.1--5.2）
│   ├── s05b-hecke.tex      5.3 't Hooft/Hecke 算子
│   ├── s06-categories.tex  §6 本征层范畴
│   ├── s07-classical.tex   §7 经典故事
│   ├── s08-functions.tex   §8 从 Hecke 本征层到 Hecke 本征函数
│   ├── s09-other.tex       §9 其他群
│   ├── s10-gerbes.tex      §10 gerbe
│   ├── s11-appendix.tex    §11 附录：SL2 的 L-包
│   └── references.tex      参考文献（保留英文原貌）
├── figures/
│   └── fig-p18-hitchin-fibers.png   原书 p.18 唯一插图（600 dpi 裁剪）
├── GLOSSARY.md             术语冻结表（译名依据）
├── SPEC.md                 译校规范（分工、公式、批注、文风）
├── README.md               本文件
├── 审校报告.md             学术审校说明与统计
└── 编译工具/
    ├── tectonic.exe        自包含 TeX 引擎（无需安装 TeX Live）
    └── build.bat           一键编译
```

## 二、如何编译

**方式 A（推荐，本机已装 TeX Live/MiKTeX）**

```bat
xelatex main.tex
xelatex main.tex
```

必须用 **XeLaTeX**（中文依赖 `ctex`；`fontset=fandol` 使用 TeX Live 自带的 Fandol 字库，无需系统字体）。
单文件版同样：`xelatex Frenkel-Witten_几何内窥与镜像对称_0710.5939.tex` 两遍。

**方式 B（不装 TeX）**：双击 `编译工具\build.bat`，用附带的 tectonic 编译 `main.tex`。
首次使用需联网下载宏包（约 100 MB，仅一次）；也可直接用本目录已编译好的 PDF。

## 三、翻译与审校说明

1. **底本**：arXiv:0710.5939v3 的 PDF。PDF 页码 = 印刷页码（正文从第 3 页起）。
   正文逐句对译，公式逐式对照 160 dpi 页面图像（`pages/`，工程内）重建；文字层只作措辞参考。
2. **术语**：统一采用 `GLOSSARY.md` 的冻结译名（如 geometric endoscopy = 几何内窥、
   Hitchin fibration = Hitchin 纤维化、Hecke eigensheaf = Hecke 本征层、perverse sheaf = 反常层）。
   无通行译名者保留英文（gerbe、oper 等），首次出现给括注。
3. **批注**：正文源码中插入 `% [Tutor Note: ...]` 等 LaTeX 注释（不影响排版，源码中可直接阅读），
   分「推导补足 / 易错预警 / 物理图像」三类；原书疑似笔误另以 `% [原文疑误: ...]` 标注并保留原样。
4. **本节重点**：每个 `\section` 开头设 `keytakeaway` 环境，提炼物理图像、数学工具与主要结论。
5. **图表**：原书无编号 Figure、无带框表格；唯一插图位于 p.18（奇异 Hitchin 纤维，
   A-模型 $G=SL_2$ / B-模型 ${}^{L}G=SO_3$），已按 600 dpi 裁剪并在 §2 对应位置以 `figure` 环境插入，
   图注为中文并标注原文页码。
6. **参考文献**：保留英文原貌，编号标签 `[KW]`、`[N1]` 等与原书一致。
7. **脚注**：原文脚注保留为脚注，编号由 LaTeX 重新生成，与原文编号可能整体偏移（正常现象）。

## 四、统计

- 成品页数：**97 页**（原书 130 页；中文本增页来自中文排印与批注区）
- 带编号公式：**225 个**（照原文编号 (1.1)–(11.6)，缺号 0、重号 0，已用脚本比对）
- 审校批注：**182 条**（Tutor Note 134、原文疑误 29、存疑 13、背景补充 6；按页索引见 `审校批注索引.md`）
- 插图：**1 幅**（原书 p.18，600 dpi 裁剪，图注译中文）
- 编译自检：xelatex 两遍 → 97 页，0 error、0 overfull、0 missing character、0 undefined、
  0 hyperref 书签警告；另有 3 处 underfull（排版松散提示，不影响正确性）
- 源码规模：约 8.9 万汉字（不含公式与英文文献）
