# 《谱网络：连接高阶泰希米勒理论与 BPS 态》中文译注本

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；本项目语料默认不用于训练，要用须先整库审计并经 Lead 书面批准。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 底本：Clarence Kineider, Georgios Kydonakis, Eugen Rogozinnikov, Valdo Tatitscheff,
> Alexander Thomas, *Spectral Networks: Bridging higher-rank Teichmüller theory and BPS states*,
> Springer Lecture Notes in Mathematics **2386**（arXiv:2412.03588v3 [math-ph]）。
> 原书 514 页（印刷页 474 页）：5 个 Part、26 章 + 附录 A、Glossary、Bibliography、Index。

本目录是**全书中文译注本**的完整交付：成品 PDF + 可重编译的 xelatex 源码工程 + 译注索引。

---

## 一、交付清单

```
deliverable/
├── Spectral_Networks_中文译注本.pdf   成品（352 页）
├── src/                               全部 LaTeX 源码（可直接重编译）
│   ├── main.tex                       装配文件
│   ├── preamble.tex                   导言区（字体/宏/定理环境/图注宏）
│   ├── front/titlepage.tex            标题页
│   ├── part/*.tex                     各块正文（front.tex, ch01_02.tex, …, appA.tex, glossary.tex, bibliography.tex）
│   └── figures/*.png                  插图（从底本矢量图裁切，146 张）
├── build_xelatex.bat                  一键编译脚本（Windows）
├── compile.log                        真实编译日志（0 error）
├── 译注汇总.md                        全部 Tutor Note 索引（217 条）
└── README.md                          本文件
```

## 二、页码映射与结构

- **底本印刷页码 = PDF 页号 − 40**（例：PDF p43 = 印刷 p.3）。
- 译注本正文中的 `% [原文 p.xx]` 一律指**底本印刷页码**，供逐段对照。
- 结构：前言（印刷 v–viii）→ 动机与历史回顾（xxi–xl）→ 符号表（xvii–xx）→
  Part I 数学基础（Ch.1–5）→ Part II 高阶泰希米勒理论（Ch.6–12）→
  Part III 几何中的谱网络（Ch.13–16）→ Part IV BPS 态的计数（Ch.17–22）→
  Part V 推广（Ch.23–26）→ 附录 A 李论基础 → 术语表 → 参考文献。

## 三、编译方法（重要：三条环境约束，均为本机实测）

1. 引擎：**xelatex ×2**（TeX Live 2026）。本机路径：
   `<本地路径>`
2. **项目路径必须是纯 ASCII**：中文/非 ASCII 路径下 xelatex 无法写文件（`I can't write on file *.log`）。
3. **必须把 `TMP`/`TEMP` 指到可写目录**（脚本已内置 `src/../tmp`），否则 `xdvipdfmx` 可能崩溃、PDF 为 0 字节。
4. 字体用 `fontset=none` + 显式文件路径（`simsun.ttc`/`simhei.ttf`/`simkai.ttf`/`simfang.ttf`），不依赖 fontconfig。

```powershell
cd src
$env:TMP = "..\tmp"; $env:TEMP = $env:TMP
xelatex -interaction=nonstopmode -file-line-error main.tex
xelatex -interaction=nonstopmode -file-line-error main.tex
```

## 四、译校体例

- **正文照译，一字不删不加**；底本笔误照原样排，只在 `% [Tutor Note: ...]` 批注中指出正确形式与判断依据（见第五节登记表）。
- **公式编号**：手工 `\tag{1.1}`，与底本一一对应（全书 197 条编号公式）；正文引用写纯文本「式 (1.1)」。
- **定理类环境**：编号手工给定（`\begin{theorem}[6.3]` → 「定理 6.3」），与底本一致。
- **插图**：底本插图全部为矢量绘图，按图注分带从 200 dpi 页面图像裁切（146 张），图注译为中文；图内标号（如 "Pole of order 2"）保留原英文并在批注说明。
- **批注**（Tutor Note）：217 条，只写在 LaTeX 注释中、不进入排版；内容包括可验证的易错点、补出的省略论证、原文笔误。
- **术语**：全书统一，见 `src/part/glossary.tex` 与术语冻结表口径（泰希米勒、Hitchin 表示、谱网络、BPS 态、S 类理论等）。
- **参考文献**：条目保持英文原貌（编号与底本一致），由底本文字层转录并做间距清理。

## 五、原文笔误登记表（译注本正文照印，批注给出正确形式）

| # | 位置（印刷页） | 底本原文 | 应读作 / 依据 |
|---|---|---|---|
| 1 | p.17 | $G(\tilde X)\curvearrowright X$ | $G(\tilde X)\curvearrowright\tilde X$（同句 "on the connected space"） |
| 2 | p.22 | $(x,\lambda)\in V\times\C^k$ | $(x,\lambda)\in(U\cap V)\times\C^k$（取 $x\in V\setminus U$ 即知 $g_{UV}$ 无定义） |
| 3 | p.26 | $\sum_{i,j}$（左端 $i$ 自由） | $\sum_j$（$n\ge2$ 取定 $i$ 可验） |
| 4 | p.30 | "commutes" | 按上下文应为 "permutes" |
| 5 | p.40 | $\partial_\infty X\subseteq H$ | $\subseteq\partial_\infty H$（下句语义、§4.3/4.4 同类写法） |
| 6 | p.43 | "resulting ciliated surface" | "marked surface"（$\bar S$ 与 $S$ 的记号分野） |
| 7 | p.50 | Euler 示性数 $2-2g-p_0-k$ | $2-2g-k$（代回验算；$\Delta$ 剖分的是 $\bar S_{g,\mathbf p}$） |
| 8 | p.62 | 定义 5.12「种子 $S$ 的格」 | $S'$（记号一致性） |
| 9 | p.62 | 例 5.14「模去 $\SL_n(\C)$」 | $\SL_2(\C)$（向量在 $\C^2$、$\omega\in\Omega^2(\C^2)$） |
| 10 | p.74 | 「除 $k$ 条边界环路外」 | 按语境应为 $h$ |
| 11 | p.99 | $N\in\R$ | $N\in\N$（$R^N$ 的 $N$ 是维数） |
| 12 | p.106 | 三重比链式等式 $b_1\to v_2$ 一步 | 漏一负号；正确符号使末行恰为 $1/\lambda$ |
| 13 | p.107 | 定理 10.28 证明第二点 | 应为 $v_i'=(-1)^{i-1}v_{n+1-i}$（$n=2$ 可核） |
| 14 | p.128 | $(g\cdot\rho)=g\rho(\gamma)g^{-1}$ | $(g\cdot\rho)(\gamma)=g\rho(\gamma)g^{-1}$（左端漏自变量） |
| 15 | p.131 | 例 12.11 末句不完整（"…if the triple ratio is."） | 按上下文应读作「三比值为正时」；疑底本脱字 |
| 16 | p.147 | 命题 13.10 证明末项重复 $t'$ | 应为 $\pi(p_{h'}(-t'))$ |
| 17 | p.150 | $\theta:=\psi_T\circ(z\mapsto z^2)\circ\varphi_T^{-1}$ | 复合次序应为 $\theta_T=\varphi_T^{-1}\circ(z\mapsto z^2)\circ\psi_T$（交换图） |
| 18 | p.153 | $1<i<k$ | $1<i<r$ |
| 19 | p.156 | 注 13.23「$n=2$」 | $k=2$（本章一律用 $k$ 表秩） |
| 20 | p.158 | 例 13.25 判别式 $4z^2-27$ | $4-27z^2$（零点个数结论无误） |
| 21 | p.170 | $T_\gamma:=\sum_{r\in I}T_{\gamma_k}$ | 求和指标应为 $T_{\gamma_r}$ |
| 22 | p.243 | 「$3F<N$ 时 SQCD 渐近自由」 | $F<3N$（$b_1=3N-F>0$） |
| 23 | p.326 | 命题 21.3「$2\le\alpha\le n-1$」 | 本节无 $n$，按语境应为 $k$ |
| 24 | p.341 | 「二次微分 $\varphi_2(s)$ 的 Hitchin 场」 | 按语境应为 $\varphi_2(z)$ |
| 25 | p.355 | 电荷列向量第 4 行 $n_r^1$、分块矩阵 $\mathrm{Id}_{k\times f}$ | 应为 $n_e^r$、$\mathrm{Id}_f$ |
| 26 | p.358 | 「秩 1 $4d$ $\mathcal N=1$ SCFT」 | 本节为 $\mathcal N=2$（节标题即 Remarkable 4d $\mathcal N=2$ SCFTs） |
| 27 | p.360 | 例 21.43「$p_3=2$」 | 按 $p_i=i-h(i)$ 应为 $p_4=2$ |
| 28 | p.405–406 | $M_{\ge 3a}$（两处） | 疑为 $M_{\ge -3a}$（层按负余维标号；同一定义 24.5 第三条即写 $M_{\ge-3a}$） |
| 29 | p.413 | 定义 25.6 的 $b(x)=\sum_{i=1}^{\infty}a_ix^i\,dx$ | 与随后用到的 $a_{-1}$ 矛盾，应为 $\sum_{i=-1}^{\infty}$ |
| 30 | p.418 | 一点函数 $\frac14\langle\tilde J(z^{(1)})-\tilde J(z^{(2)})^2E_{\mathrm{ren}}\rangle$ | 平方号应作用于整个差：$\frac14\langle(\tilde J(z^{(1)})-\tilde J(z^{(2)}))^2E_{\mathrm{ren}}\rangle$ |
| 31 | p.448 | 子覆盖 $X_\lambda$ | $\tilde X_\lambda$（同段前文均带波浪号） |
| 32 | p.xxxii | 花体 $\mathcal Z$ 与正体 $Z$ 混用（同一中心荷） | 译文统一作 $\mathcal Z$，见批注 |
| 33 | p.xxvi / p.xxxvi | "Nyuts" / "Scherck" | 人名应为 Nuyts / Scherk |


## 六、统计

- 成品：**352 页**，正文汉字约 **180,891** 字
- 编号公式：**197** 条（与底本 197 条一一对应）
- 插图：**145** 张（全部由底本矢量图裁切，未自造）
- 定理类环境：底本 Definition 179 条、Proposition 122 条、Theorem 43 条、Example 68 条、Remark 132 条等，编号全部照原文
- 批注（Tutor Note）：**217** 条，索引见 `译注汇总.md`
- 编译：xelatex ×2，**0 error / 0 undefined control sequence / 0 missing character**

## 七、已知偏差与限制

1. **索引（Index）未重排**：底本 Index 的页码是英文本页码，中译本页码不同，逐条重排意义有限，故未收录；需要时请对照底本 pp.465–474。
2. **参考文献**保持英文原貌（Springer 体例即如此），由底本文字层机器转录，DOI/arXiv 间距已清理，个别符号可能与印刷本略有差异。
3. **图内英文标注**（如 "Pole of order 2"、"type I/type II"）属于图形内容，未替换为中文，已在相应批注说明。
4. **排版**：中译本重新排版，页数与原书不同；所有编号（式、定理、图、节）与底本对齐，但**页码不对齐**——请用 `% [原文 p.xx]` 锚点对照。
5. 批注中的数值/文献判断均由译者核对给出；若与读者理解不同，以底本为准。
6. **附录 A 的 9 个 Dynkin 图**：原书以排版图给出，译文以「链/三叉结构 + 边重数 + 顶点权」的文字形式等价给出（信息完整，见定理 A.16 处批注）；Fig A.1 已按原图裁切收录。

## 八、版权声明

底本版权归原作者与 Springer Nature 所有。本译注本仅供个人学习、研究与教学使用，不得用于商业用途；引用请注明原文出处（LNM 2386 / arXiv:2412.03588）。
