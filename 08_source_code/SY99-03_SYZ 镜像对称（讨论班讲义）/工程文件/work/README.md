# 《学习讨论班：SYZ 镜像对称》中文译注本 —— 交付说明（README）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：全库统一 CC BY 4.0，明确欢迎用于训练、蒸馏与商用（署名即可）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 本目录是交付包：成品 PDF、可独立重编译的 LaTeX 源码、编译日志、全部译者批注汇总，以及本说明。
> 工程规范见 `work/STYLE_GUIDE.md`；分工与边界见 `work/BRIEF.md`；单点修复记录见 `work/PATCH_LOG.md`。

## 1. 底本信息与「页码映射」

| 项 | 值 |
|---|---|
| 标题 | Learning Seminar: SYZ Mirror Symmetry |
| 形态 | **网页**（HTML + MathJax；非 PDF，故**没有页码**） |
| URL | <https://diewildkatze.com/SYZ.html> |
| 快照 | 2026-11-04 抓取，106,386 字节；本译本锁定该快照（`raw/SYZ.html` 随工程保留） |
| 作者 | 底本**未署名**；仅在日程表中列出报告人：Si-Yang Liu、Yunpeng Niu、Kyoungmo Kim、Maximilian Schimpf |
| 结构 | 6 章正文（卷首 Overview 无章号；Introduction…Toric Varieties, Continued = 底本第 1–5 章）+ References |
| 公式真值 | 网页 HTML 里 MathJax 的 **LaTeX 源码**（不是 OCR、不是扫描图） |

**页码映射（本译本用「源块」代替页码）**：底本无页码，无法给出 PDF 页 ↔ 印刷页偏移。
工程把 HTML 解析成 **246 个源块**（`work/source/blockmap.tsv`，每块 `B001`–`B246`），
每个源块翻译时在源码里留一行 `% [源 Bxxx]`。因此：

| 底本位置 | 源块区间 | 译本文件 | 译本 PDF 大致页 |
|---|---|---|---|
| 概论（Overview） | B001–B011 | `chunks/c01.tex` | p4–5 |
| 第 1 章 引言 | B012–B037 | `chunks/tr01a.tex`、`tr01b.tex` | p5–8 |
| 第 2 章 拉格朗日环面纤维化 | B038–B104 | `chunks/tr02a.tex`、`tr02b.tex` | p8–12 |
| 第 3 章 环簇 Fano 集的 SYZ 镜像对称 | B105–B154 | `chunks/tr03a.tex`、`tr03b.tex`、`tr04a.tex`、`tr04b.tex` | p13–17 |
| 第 4 章 焦点-焦点奇点与近环面纤维化 | B155–B188 | `chunks/tr05a.tex`、`tr05b.tex` | p18–20 |
| 第 5 章 环簇的 SYZ 镜像对称（续） | B189–B214 | `chunks/tr06a.tex` | p21–23 |
| 参考文献（英文原貌） | B215–B246 | `chunks/c-refs.tex`（脚本生成） | p23–25 |

## 2. 结构清单

- 封面 + 译者说明 + 目录（`chunks/c00.tex`）+ 概论（`c01.tex`）；
- 5 个编号章（`\section`）+ 14 个小节（`\subsection`）；
- **独立公式 38 处**（与底本源文 38 处一一对应；底本没有任何编号公式，本译本一律不编号——`\[…\]` / `align*` / `gather*` / `multline*`，无 `\tag`）；
- **定理类环境 59 个**（定义 18、定理 14、引理 7、命题 8、推论 4、例 3、习题 2、注 2、陈述 1）+ **证明 12 个**；
- **表 3 张**：表 1 学习讨论班日程（概论）、表 2 Williamson 型（第 4 章）、表 3 底流形与节点数（第 4 章）；
- **交换图 3 个**（都在第 2 章）：B082、B089、B093，用 `tikz-cd` 重画；
- **图 2 张**（底本为 canvas 绘制，无位图）：图 1 $\mathbb{P}^2$ 的矩多面体、图 2 $H_1$ 的轨道，用 tikz 重画；
- **参考文献 32 条**（英文原貌，自动转录，未逐条校对）；
- **译者批注 125 条**（`% [Tutor Note: …]`，不进入排版；全文见本目录 `译注汇总.md`）。

## 3. 编译方法

环境：TeX Live 2026（LuaLaTeX 1.24 / LuaHBTeX）+ Python 3.12（仅工具脚本需要）。中文字体由 `ctex` 自动取系统字体，**不需要** fontconfig 或手写 `\setCJKmainfont`。

```powershell
# 在 src\ 目录（或把 build.ps1 与 src\ 一起拷到任意 ASCII 路径）：
powershell -ExecutionPolicy Bypass -File build.ps1
```

`build.ps1` 做三件事：① 找 TeX bin；② 把 `main.tex`/`preamble.tex`/`chunks/`/`figures/` 镜像到 ASCII 可写目录
（默认 `%USERPROFILE%\Documents\deepseek-harness\default-workspace\syzbuild`，脚本里可改），并设 `TMP`/`TEMP`；
③ `lualatex` 跑 3 遍，把 `main.pdf` 拷回 `src\`，并解析 `main.log` 报告错误数。

**本机踩过的坑（换机器时注意）**：
- LuaLaTeX 在**非 ASCII 路径**下写 `.log` 会失败（报 `I can't write on file main.log`，具有误导性）→ 必须镜像到 ASCII 路径编译；
- 子进程**不能写 Desktop**（同样报错）→ 编译目录不要设在桌面；
- `TMP`/`TEMP` 必须显式指向可写目录，否则字体缓存/`xdvipdfmx` 可能崩；
- 日志不要重定向到 `<jobname>.out`（TeX 会把它当输入文件读，导致满屏 invalid character）。

也可手工编译：`cd` 到 `src\`，`lualatex -interaction=nonstopmode -file-line-error main.tex` ×3。
`src\` 可独立重编译（不依赖 `work\` 下的中间素材）。

## 4. 译校体例

1. **底本形态与公式**：底本是网页，公式真值 = HTML 中的 LaTeX 源码，故数学内容逐字转写，不经图像辨认。
2. **章节**：底本 5 个编号章对应译本 `\section` 自动编号 1–5；卷首 Overview 不编号（`\section*`，但进目录）。
   章内 `<h3>` 小节 → `\subsection`。
3. **公式编号**：底本 0 条编号公式 → 译本不编号、不 `\tag`、不 `\label/\ref/\eqref`；正文引用一律纯文本。
4. **定理类环境**：底本无编号 → 一律无编号环境；作者名/文献放在可选参数里（如 `定理 (Bondal–Orlov)`）。
   底本中少数 `<div class="env">` 实际只是**粗体小标题句**（如 "Topological monodromy on torus bundle."），
   按语义用 `\para{…}` 排成行内粗体标题，不套定理环境。
5. **引用**：`[Kon94]`、`[CO06]`、`[Eva23，第 6 章]` 等一律纯文本，不用 `\cite`；参考文献保留英文原貌。
6. **图表**：表格用 `booktabs` + 手工编号表题；交换图用 `tikz-cd`；canvas 图用 tikz 重画（见 §7）。
7. **术语**：以 `work/glossary.tsv`（冻结表，186 行）为准；人名、模型名、缩写（SYZ/HMS/Floer/Fukaya/Maslov…）保留拉丁字母。
8. **批注**：`% [Tutor Note: …]` 写在源码里，编译不显示；内容限于：可验证易错点、补出的省略论证、
   原文笔误及正确形式、术语首现、译文取舍。批注可含 `$…$`，但 `$` 必须成对。

## 5. 原文笔误登记表（均已按原文排印，只在批注/本表指出正确形式；**未擅改正文数学**）

| # | 源块 | 原文（摘录） | 说明 / 正确形式 |
|---|---|---|---|
| 1 | B005 | `$b\in H^1(L,\lambda_0)$`（正文称 $\Lambda_0$ 为诺维科夫环） | 小写 $\lambda_0$ 应为 $\Lambda_0$；译本按语义排作 $\Lambda_0$ |
| 2 | 表 1 | "Landau-Ginburg superpotential…" | 应为 Landau–Ginzburg |
| 3 | B004 | "the phenomena seems mysterious" | 应为 the phenomenon seems（单复数） |
| 4 | B022 | "resconstruction theorem" | 应为 reconstruction |
| 5 | B027 | "Assuming on of the following condition is true" | one of the following conditions |
| 6 | B036 | "moduli spaces of paris" | 应为 pairs |
| 7 | B056 | "$H_i$s are Poisson-commute" | 应为 are Poisson-commuting（语法） |
| 8 | B065 | `\espan\left\{…\right\}` | **不是笔误**：底本 HTML 的 MathJax 配置 `tex.macros` 里定义了 `espan:"{\operatorname{span}}"`（因为 `\span` 是 TeX 原语）。本译本按 `\operatorname{span}` 排印，页内还自定义了 `Hom/ev/hol` 三个宏，均等价于本工程 preamble 的 `\Hom/\ev/\hol` |
| 9 | B081 | `$\psi\colon\mathbb{R}^n$ a diffeomorphism` | 缺靶空间，据 B082 交换图应为 $\psi\colon\mathbb{R}^n\to\mathbb{R}^n$ |
| 10 | B097 | "does not admit any compatible complex structures (so that it becomes a Kähler manifold)" | 括注与前半句矛盾，应为「故不能成为 Kähler 流形」 |
| 11 | B112 | 矩多面体三角形界 $\{t_i\le\sqrt{\lambda}\}$ | 与同段显式矩映射 $\mu=(|x|^2/2,\dots)$ 及约化层 $\lambda$ 不自洽；疑应为 $\lambda$（**存疑，未改**） |
| 12 | B114 | "Fanoness" | 非标准拼写（Fano-ness），译作「Fano 性」 |
| 13 | B120 | "decompostion" | 应为 decomposition |
| 14 | B126 | 求和条件 $2-k+\mu(\beta)$，全段无 $k$ | 按 $\mathfrak{m}^d$ 次数应为 $2-d+\mu(\beta)$（**存疑，未改**） |
| 15 | B126 | $H^1(L_0;\mathbb{R})\cong\mathbb{R}^2$、$\pi_1\cong\mathbb{Z}^2$ | 对一般 $n$ 应为 $\mathbb{R}^n$、$\mathbb{Z}^n$（疑沿用 $n=2$） |
| 16 | B127 | "falt connection" | 应为 flat connection |
| 17 | B138 | $T(\Sigma)$ 只称 "a constant element"，未定义 | 照译，批注说明其作用 |
| 18 | B146 | `$\{w_i\}_{i=1}^w$` | 上限与指标撞名，据 B147 疑应为 $\{w_i\}_{i=1}^N$（**存疑**） |
| 19 | B147 | $\sum_{i=1}^N w_i^{v_i}$ 与「$w_i$ 是 $(\mathbb{C}^\ast)^n$ 的基」 | 记号混用（标准写法 $W_\Sigma=\sum w^{v_i}$）；照译 |
| 20 | B152 | "associate product" | 应为 associative product |
| 21 | B156 | `$H\colon (M^{2n},\omega)$ be a completely integrable hamiltonian system` | 缺靶空间，应为 $H\colon(M^{2n},\omega)\to\mathbb{R}^n$ |
| 22 | B163 | "We call this singularity has Williamson type" | 语法：应为 is of / has |
| 23 | B167 | `$\pi_{H_2}^t` | 与上一条 $\phi_{H_1}^t$ 对照应为 $\phi_{H_2}^t$ |
| 24 | B174 | "thta"；且 $X_{S_0}\to X_{S_1}$ 中 $S_0$ 未定义 | thta→that；$S_0$ 疑为 $S_1$、$S_1$ 疑为 $S_2$（**存疑**） |
| 25 | B187 | "affineimmersion"、"aneigenvalue"、"The inclusions … is" | 应为 affine immersion、an eigenvalue；主谓不一致 |
| 26 | B189 | "recollment of toric manifolds" | 应为 recollection（回顾） |
| 27 | B203 | `$\mathbb{K}=\langle e_1+\dotsb+e_n\rangle$`；作用式坐标 $z_1,\dotsb,z_n$ | 由 $\pi\colon\mathbb{Z}^{n+1}\to\mathbb{Z}^n$ 应对应 $\langle e_1+\dotsb+e_{n+1}\rangle$、坐标 $z_1,\dots,z_{n+1}$ |
| 28 | B207 | `$x_1^{\sigma}=z_1^{\langle v,u_{i_1}\rangle}\dotsb$` | 漏下标，据第三行应为 $\langle v_1,u_{i_1}\rangle$；对偶基 $\{u_{i_1},\dots\}$ 疑为 $\{u_1,\dots,u_n\}$ |
| 29 | B208 | "Sympletic aspects" | 应为 Symplectic（译本按「辛几何方面」） |
| 30 | B211 | "smoothmanifold" | 应为 smooth manifold |
| 31 | B206 | `(2) $U(\sigma)\supseteq U(\sigma')$ if $\sigma$ is a face of $\sigma'$` | 方向疑误：按 B204 定义，$\sigma$ 是 $\sigma'$ 的面时条件更少，应为 $U(\sigma)\subseteq U(\sigma')$（以 $\mathbb{P}^1$ 的扇可验证）；照译+批注（**存疑**） |

## 6. 统计

| 指标 | 数值 |
|---|---|
| 底本源块 | 246（译本覆盖 214 个正文/表格/图/小节块；其余 32 个为参考文献条目） |
| 译本 PDF | **25 页**（A4，11pt；封面/译者说明/目录 3 页 + 正文 + 参考文献） |
| 独立公式 | 38（与底本源文 38 处一一对应） |
| 编号公式 | 0（底本即无编号；译本 0 个 `\tag`） |
| 定理类环境 / 证明 | 59 / 12 |
| 表 / 交换图 / 图 | 3 / 3 / 2（图与交换图均为 tikz 重画） |
| 参考文献 | 32 条（英文原貌自动转录，key 无重复；正文引用 26 个 key 全部命中） |
| 译者批注 | 125 条（`译注汇总.md`） |
| 编译 | LuaLaTeX ×3：**0 file:line error / 0 undefined / 0 missing character / 0 overfull** |
| 成品回读 | 8 个章级标题齐全、表 1–3 齐全、32 条文献全在、字体全部子集嵌入、无 `??`/`**`/`Undefined` 残留 |
| 原文笔误登记 | 31 项（其中 5 项标「存疑」） |
| 交叉校对 | 6 轮（每人校一块），6 份报告，全部「必须改」已落改（见 `work/PATCH_LOG.md` 第三轮） |

## 7. 已知偏差与限制（不做静默降级）

1. **底本无页码**：无法给出 PDF 页 ↔ 印刷页偏移；本译本以「源块号」`B001`–`B246` 作为定位与验收锚点
   （源码中每块前有 `% [源 Bxxx]`），并在 §1 给出「章 → 源块 → 译本页」映射。
2. **图**：底本没有位图/ SVG（`<img>`=0、`<svg>`=0），但有 **2 张由页面内联 JS 绘制的 `<canvas>` 图**：
   图 1「Moment polytope for $\mathbb{P}^2$」（B112）与图 2「Orbits of $H_1$」（B167 附近）。
   本译本按 canvas 的**绘制指令**（三点三角形、原点+两轴+一条双曲轨道）用 tikz 重画为图 1、图 2；
   这是重画而非原始像素，比例可能有细微差异，特此声明。
3. **交换图**：B082 在底本中正常显示；**B089、B093 两张 `q.uiver.app` 内嵌图在底本 HTML 中被注释掉**
   （网页上不显示）。因正文有「fitting into the commutative diagram」「commutes.」等句子，本译本按源码中的
   q.uiver.app 数据用 `tikz-cd` 重画并补入正文，以保证句子可读；三张图均不改变任何数学含义。
4. **表 1 后两行日程**（26.01.26 / 02.02.26 的补充报告）在底本 HTML 中处于注释状态、网页不显示，故未收录。
5. **公式类型**：底本的独立公式与译本一一对应（38/38）。B065 有一处行内公式曾因超过版心 27.7pt 暂改为独立公式，交叉校对指出这违反「行内公式原样保留」后已回退为行内，改用局部 `{\sloppy … \par}` 解决溢出（数学内容与排版位置均与底本一致）。另：表 1、参考文献、B126 长公式做过纯排版调整（`\footnotesize`/`\sloppy`/`\resizebox`），均记录在 `work/PATCH_LOG.md`。
6. **参考文献**：`gen_refs.py` 从 HTML 逐条转录（32 条，0 缺 0 重），仅做 LaTeX 转义与重排，**未逐条与原出版核对**；
   含 URL/DOI 的条目可能随出版信息更新而变化。
7. **底本未署名**：封面「报告人」据日程表列出，不代表论文作者；引用本译本时请引底本 URL。
8. **快照**：底本可能被作者继续更新；本译本只对 2026-11-04 的 HTML 快照负责。
9. **定理/环境数量口径**：底本 62 个 `<div class="env">` 中有若干实为粗体小标题句（按 STYLE_GUIDE 用 `\para`），
   故译本定理类环境为 59 个，另有 12 个 `proof` 环境；不是漏译（`check.py` 的块覆盖为 214/214）。
10. **列表类型**：底本 6 处 `<ol>` 已按 `enumerate` 排印（三处 `type="i"` → i./ii./iii.，第 3 章 B150–B152 → 1./2./3.，
    第 5 章 bracketed-list → 1) 2)）；第 4 章 `circled-list` 的圈码 ①② 因正文字体缺 U+2460/2461，改用（i）（ii）
    （措辞与指代关系不变，源码批注已说明）。

## 8. 版权声明

- 底本《Learning Seminar: SYZ Mirror Symmetry》版权归原作者/学习讨论班所有，见底本 URL；
- 本译本为**学习交流用**的非正式中文译注，不含商业用途；译者的补充说明仅写在批注中，不对原文内容主张著作权；
- 参考文献保留英文原貌；图片/交换图为按底本绘制指令的 tikz 重画，非原图像素；
- 如原作者对译本有异议，请联系删除。

---

**复现路径**（从源码重建成品）：

```powershell
$py = "<本地路径>"
powershell -ExecutionPolicy Bypass -File .\build.ps1        # Gate 2：真编译（×3）
& $py ..\tools\check.py                                      # Gate 0/1：块覆盖 + 静态检查
& $py ..\tools\verify_pdf.py .\main.pdf                      # Gate 3：成品回读
& $py ..\tools\gen_notes.py                                  # 译注汇总.md
& $py ..\tools\pack.py                                       # 打包 deliverable/
```
