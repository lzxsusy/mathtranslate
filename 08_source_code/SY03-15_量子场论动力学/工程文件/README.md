# 《量子场论动力学》中文译注本 — 交付说明

原著：Edward Witten, *Dynamics of Quantum Field Theory*,
载于 *Quantum Fields and Strings: A Course for Mathematicians*, Vol. 2（AMS, 1999），
第 4 部分，pp. 1119–1424。

本目录是**可直接编辑、可编译**的 XeLaTeX 工程：19 讲正文（含导言）、习题、部分习题解答，
全部按扫描原稿逐页译出；公式按页面图像逐条重排，编号与原书一致；插图从 400 dpi 扫描页
裁切后插入；关键推导处附 `% [Tutor Note: ...]` 审校批注；每讲开头有「本节重点」。

## 1. 目录结构

```
Witten，量子场论讲义/
├── main.tex                 # 主文件（导言区、封面、译者说明、目录、\input 汇总）
├── sections/
│   ├── intro.tex            # 导言（原书 pp.1119–1120）
│   ├── lec01_p1.tex ...     # 第 1–19 讲，按扫描页分段（每段约 7–9 页）
│   ├── lec09.tex            # 第 9 讲（未分段）
│   ├── exo_p1.tex           # 习题（原书 pp.1403–1409）
│   ├── sol_p1.tex, sol_p2.tex  # 部分习题解答（pp.1411–1424）
│   └── glossary.tex         # 附录 A：术语表
├── figs/                    # 正文插图（fig_pNNN_k.png：扫描页 N 上第 k 张图）
├── TRANSLATION_SPEC.md      # 翻译与排版规范（体例说明）
├── tools/                   # 辅助脚本（裁图、静态检查、覆盖度审计）
└── README.md
```

## 2. 编译

需要 TeX Live / MiKTeX（含 `ctex` 宏包），**用 XeLaTeX**：

```
xelatex main.tex
xelatex main.tex
```

两遍是为了生成目录与交叉引用。若用 TeXstudio / VS Code（LaTeX Workshop），
把默认编译器设为 `xelatex` 即可；`main.tex` 首行已写 `% !TeX program = xelatex`。

- 不建议 pdfLaTeX：中文需 `ctex` 的 pdftex 选项并另行配置字体。
- 图片路径为相对路径 `figs/...`，请在 `main.tex` 所在目录编译。
- 文件均为 UTF-8 编码。

> 编译验证：本工程已用 TeX Live 2026 + XeLaTeX 实际编译通过，产出
> `Witten，量子场论讲义.pdf`，共 **280 页**；无未定义引用、无重复标签、无编译错误
> （仅有少量 overfull hbox 的排版微警告，不影响阅读）。

## 3. 体例

1. **公式编号**：原书编号 (n.m) 用 `\tag{n.m}` 原样复现，并用 `\label{eq:n-m}` 建立引用；
   无编号公式用 `\[...\]`。多行公式用 `align`。
2. **小节编号**：小节由 LaTeX 自动编号，与原书 §n.m 不一定一致；每个小节首行注释
   `% 原文 §n.m` 给出原编号。
3. **页标记**：每个扫描页前有 `% ===== 原文 p.N =====`（N 为 PDF 扫描页序），
   便于逐页对勘；原书印刷页码 = N + 1118。
4. **审校批注**：`% [Tutor Note: ...]`，分「易错预警」「含糊点拨」「原文勘误」三类，
   只作注释、不影响排版；在编辑器中搜索 `Tutor Note` 即可逐条阅读。
5. **图表**：`figs/fig_pNNN_k.png` 为扫描页 N 上第 k 张图的原图裁切；图注为中文，
   并注明「原文 Figure k，p.N」。
6. **术语**：见附录 A 与 `TRANSLATION_SPEC.md` §5；首次出现括注英文。
7. **号差（signature）**：原书**并不统一**；**本版按统一要求把四维闵氏号差一律取为
   $(-,+,+,+)$**（约定包：$\eta=\mathrm{diag}(-1,1,1,1)$、$(\gamma^0)^2=-1$、
   $\epsilon^{0123}=+1$、$L_{\rm gauge}=-\frac{1}{4e^2}F^2$、$L_{\rm scalar}=-\frac12(\partial\phi)^2$）。
   第 1 讲原本就是 $(-,+,+,+)$（p.1138）；第 17 讲原印 $(+,-,-,-)$（p.1351），
   本版改为 $(-,+,+,+)$ 并在批注中保留原式；第 18--19 讲沿用第 17 讲。第 8、16 讲明言欧氏
   （p.1226、p.1341），欧氏部分不涉及号差之别，保持原样。第 4 讲为**二维**光锥 $(+,-)$
   （p.1175，$ds^2=dx_+dx_-$），属二维光锥坐标的另一约定，本版保留原式。
   详见 PDF 内「译者说明·关于号差与符号约定」。

## 4. 已知问题与处理原则

- 原书由课堂记录整理排印，个别公式存在笔误或记号不一致（如矩阵基序、系数与符号归一化）。
  译注本**忠实照录原文**，可疑处以批注标出，不擅自改动公式。
- 扫描件的 OCR 文本层公式错误极多（λ→fi、φ→¢、L→£ 等），译文全部以页面图像为准重排。
- 极少数页面因扫描模糊、符号难以辨认，已在对应位置以批注说明；如教授手边有清晰原书，
  可据批注定位复核。

## 5. 校验脚本

```
python tools/qc.py sections/lec01_p1.tex     # 单文件 LaTeX 静态检查
python tools/audit.py                         # 全书页覆盖度、图片、宏定义审计
python tools/crop_fig.py --page 185 --box 0.10,0.40,0.90,0.72 --out figs/fig_p185_1.png
```
