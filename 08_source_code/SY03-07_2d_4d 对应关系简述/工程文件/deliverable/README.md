# 2d/4d 对应关系简述 —— 中文译注本

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 为准：语料 / 轨迹 / 会话 CC BY 4.0，明确欢迎用于训练与蒸馏（译文与工程文档 CC BY-NC-SA 4.0）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

**底本**：Yuji Tachikawa（立川裕二），*A brief review of the 2d/4d correspondences*，
arXiv:1608.02964v5（2016-10-15），IPMU-16-0048，46 页。原为综述文集
《Localization techniques in quantum field theories》（eds. V. Pestun & M. Zabzine，共 17 章）之一章。

**成品**：`2d4d对应关系简述_中文译注本.pdf`，39 页；LuaLaTeX 编译 3 遍，
**0 个 `file:line` 错误 / 0 个 `!` 致命错误 / 0 个未定义命令 / 0 个缺字 / 0 处 Overfull**。

---

## 1. 底本信息与页码映射

| 项 | 底本（原文） | 本译本 |
|---|---|---|
| 页数 | 46 页（正文 pp.1–41，参考文献 pp.41–46） | 39 页 |
| 版面 | US Letter（612 × 792 pt） | A4，左右边距 2.4 cm |
| 页码偏移 | **0**（PDF 页号 = 印刷页码） | 本译本自身页码（见目录） |
| 章节编号 | §1–§6（含 2.1/2.1.1 等层级） | **完全一致**（由 `\section` 自动生成，逐节核对过） |
| 公式编号 | 137 条：1.1 / 2.1–2.72 / 3.1–3.11 / 4.1–4.27 / 5.1–5.26 | **一一对应，不缺不重不跳**（`\tag{}` 手工复刻） |
| 图 | 13 幅（图 1–13，全为矢量图，0 位图） | 13 幅，500 dpi 从原文矢量图裁取 |
| 表 | **0 张** | 0 张（没有造表） |
| 参考文献 | 77 条（`[1]`–`[77]`，0 缺号 0 重号） | 77 条，脚本转录（见 §7 限制） |
| 附录 / 习题 / 要点框 | **都没有** | 都没有（对应宏只保留备用） |

**怎么回查原文**：译文中的批注一律写「原文 p.$N$」，公式号 `(x.y)`、图号「图 $N$」、
文献号 `[n]` 全部照抄原文，所以按 (x.y) / 图号 / 「原文 p.N」都能直接翻到底本对应的页。
**注意**：本译本 39 页 ≠ 底本 46 页，不要用译本页码去对底本页码。

## 2. 结构清单

```
标题页 / 摘要 / 译者说明
目录
§1 Introduction ................................................ 1 条编号公式 (1.1)
§2 Two two-dimensional theories
   §2.1 Two-dimensional Yang-Mills theories .................... 2.1–2.30（图 1–5）
      2.1.1 Action / 2.1.2 On the cylinder / 2.1.3 On a general surface / 2.1.4 q-deformation
   §2.2 The Liouville theory ................................... 2.31–2.72（图 6）
      2.2.1 Free boson theory / 2.2.2 Interacting theory
      2.2.3 Four-point function: general structure / 2.2.4 …: explicit expressions
§3 A class of four-dimensional theories ........................ 3.1–3.11（图 7–10）
   §3.1 N=2 supersymmetric gauge theories
   §3.2 Class S theories of type SU(2)
      3.2.1 Construction from three-punctured spheres and cylinders / 3.2.2 One-punctured torus
      3.2.3 Four-punctured sphere / 3.2.4 General consideration
§4 Two supersymmetric backgrounds .............................. 4.1–4.27（图 11）
   §4.1 General yoga of supersymmetric localization
   §4.2 S^1×S^3
   §4.3 S^4   4.3.1 General structure / 4.3.2 Classical and one-loop factors / 4.3.3 Instanton contributions
§5 Two correspondences and an interpretation ................... 5.1–5.26（图 12–13）
   §5.1 S^1×S^3 and the two-dimensional Yang-Mills / §5.2 S^4 and the Liouville theory
   §5.3 Six-dimensional interpretation   5.3.1 / 5.3.2
§6 Future directions ........................................... 无编号公式
   6.1 Two unsolved problems in the SU(2) case / 6.2 More objects in the SU(2) case
   6.3 Using 6d N=(2,0) theories of other types / 6.4 Other spacetimes, other theories
致谢
参考文献（77 条）
```

**章节号自检**：§2 起于原文 p.4、§3 p.16、§4 p.21、§5 p.28、§6 p.36，与底本目录页给出的起点完全一致；
§6 之后只有「致谢」与「参考文献」两个 `\section*`（不编号），故不会出现「第 7 节」。

## 3. 编译方法（本机实测；含字体与路径坑）

### 3.1 一键编译

```powershell
powershell -ExecutionPolicy Bypass -File .\build.ps1
```

`build.ps1` 做四件事：① 找 TeX bin；② 把 `src/`、`src/chunks/`、`src/figures/` 镜像到
**ASCII 且可写**的目录（默认 `<本地路径>`）；
③ 在那里跑 `lualatex ×3`（并把 `TMP`/`TEMP` 指到该目录下的 `tmp`）；④ 解析 `main.log` 统计
`file:line / fatal / undefined / missing char / overfull`，成功后把 `main.pdf` 拷回 `src/`。

### 3.2 直接手动编译（会踩坑，故不推荐）

```powershell
$bin = "<本地路径>"
$env:PATH = "$bin;$env:PATH"
cd <一个 ASCII 且可写的目录>          # 关键：不要在中文字符目录里编
lualatex -interaction=nonstopmode -file-line-error main.tex   # ×3（目录/页码/交叉引用）
```

**本机三个必须知道的坑（都实测过）**：

1. **`lualatex` 不能在非 ASCII 路径下写 `.log`**（报 `I can't write on file main.log`，
   看起来像权限问题，其实是路径编码问题）→ 必须镜像到 ASCII 目录再编译。
2. **子进程不能写 Desktop**（同样的报错）→ 编译目录固定放 `default-workspace` 下。
3. **`TMP`/`TEMP` 必须显式指向可写目录**，否则 xdvipdfmx / 字体缓存可能崩。
4. 不要把日志重定向到 `<jobname>.out`——TeX 会把它当输入文件读，满屏 `Text line contains an invalid character`。

### 3.3 字体

`LuaLaTeX + ctex`，**自动取系统字体**，不需要 fontconfig，也不需要手写 `\setCJKmainfont`。
换到没有中文字体的机器上，可改用：

```latex
\usepackage[UTF8,fontset=fandol]{ctex}   % 本机已装 fandol
```

## 4. 译校体例

1. **正文一字不改**：原文的措辞、笔误、排版怪癖一律照原样译出；任何订正只出现在批注里。
2. **批注不进入排版**：全部写成 LaTeX 注释 `% [Tutor Note: ...]`，共 **128 条**，
   全文汇总见随交付的 `译注汇总.md`。每 2–3 页 ≥ 1 条、每节 ≥ 3 条。
3. **批注只允许四类内容**：① 易错点的精确提醒（哪个上下标/哪个因子 2）；② 作者跳过的推导**补出来**；
   ③ 原文笔误的指认 + 正确形式（必须先 500 dpi 以上裁图复核）；④ 与其它章节/文献的对照。
   **不写**空泛评语，不编造原文没有的物理内容。
4. **术语冻结**：`work/glossary.tsv`（236 行）为全书唯一术语表；首次出现写「中文（English）」，
   之后只用中文；人名、模型名与缩写（SU(2)、CFT、OPE、DOZZ、$T_N$、BPS）保留英文。
   易混淆词严格分开：**three-holed sphere→三孔球面 / three-punctured sphere→三穿刺球面**；
   **reflection amplitude→反射振幅 / reflection coefficient→反射系数**；
   **双基表示 / 三基表示**。
5. **公式**：`\begin{equation} … \tag{x.y}\end{equation}`，多行用 `align/gather/aligned`、
   每行一个 `\tag`；无编号式用 `\[…\]` 或 `equation*`；引用公式写纯文本「式 (2.13)」。
6. **图表**：图用 `\includegraphics{figN.png}` + `\figtitle{N}{…}`（`\captionof*`，手工编号，
   不用 `\caption` 自动编号，以免与原文号冲突）；图注＝原文 `Figure N:` 那句的忠实中译。
7. **文献**：纯文本 `[12]`、`[45--54]`，不用 `\cite`。
8. **交叉校对**：6 位译者循环互校（tr-01↔tr-02↔…↔tr-06），只写报告不改他人文件，
   报告存 `work/review/`；Lead 用 exact-match patch 脚本落改，每条改动都有命中数校验。

## 5. 原文笔误登记表

> **原则**：正文照原文排印，**不做径改**；下表只登记「译者批注中指认过」的疑点。
> 判据一栏写明是怎么确认的。**「复核」列**：`Lead` = 本译本 Lead 亲自裁图复核过；
> `译校` = 译者裁图复核并经交叉校对复核，Lead 未再独立复核。

| # | 原文页 | 位置 | 原文（印作） | 说明 / 正确形式 | 复核 |
|---|---|---|---|---|---|
| 1 | p.3 | §1 | "countless pages … have been already **wasted** to describe…" | 措辞可疑（疑为 written），但文字层与页图一致，**不作为笔误**，仅批注说明 | Lead |
| 2 | p.5 | (2.9) 前 | 环面 `x¹∼x¹+L, x⁰∼x¹+T` | 第二个条件应为 `x⁰∼x⁰+T` | 译校 |
| 3 | p.6 | 正文 | `pionneered` | 应为 `pioneered`（中文无影响） | 译校 |
| 4 | p.7 | (2.14) | `χ_R(V^{-1})` | **不是笔误**：这是「传播子/热核」约定（第二个边界取相反定向），(2.16)(2.17) 用「同向」约定，二者差一个逆；$\SU(2)$ 特征标为实，两写法等价。仅登记为约定不一致 | Lead |
| 5 | p.7 | (2.15) | 右端 `ψ_A(U,V)` | 按该式自洽性应为 `ψ_{A+A'}(U,V)`（漏掉所缝圆盘面积 $A'$） | **Lead** |
| 6 | p.8 | (2.18) 下 | `integrates to β(2−2g)` | 按 Gauss–Bonnet 应为 `4πβ(2−2g)`；作者把 $4π$ 并入 $β$（属约定，非笔误） | 译校 |
| 7 | p.14 | (2.60) | `r_{\{\tilde n'\},Q-\alpha,\alpha_3,\alpha_4}` | 与 (2.58) 的配对关系看，疑应为 `r_{\{n'\},…}`（**存疑**，未定论） | 译校 |
| 8 | p.15 | (2.64) | 矩阵元 `4Δ_p+8Δ_0^{\,2}` | 应为 `8Δ_p^{\,2}`（其余各元均以 $Δ_p$ 表示，且与 (2.56) Gram 矩阵逐项计算一致） | **Lead** |
| 9 | p.16 | (3.2) 下 | "where $\mu$ is the mass term" | 式 (3.2) 通篇没有 $\mu$；疑为早期版本残留（质量项在 p.17 才由 $\underline\Phi$ 的 vev 引入） | 译校 |
| 10 | p.17 | 首行 | "give a vev to $\Phi$" | 同段另两处均为 $\underline\Phi$；能给 $(i,j)$ 指标供质量项的是 $\U(N_f)$ 伴随的 $\underline\Phi$，此处疑漏下划线 | 译校 |
| 11 | p.20 | §3.2.4 | "a torus with one puncture can be constructed from **two** three-punctured spheres in two ways" | 与 p.19「由**一个**三穿刺球面 + 一个圆柱面」冲突；亏格/穿刺计数也排除「两个三穿刺球面」（结果会是亏格 0、五穿刺），疑 `two`→`a`；同句另有脱字（considered … can be → considered how … can be） | 译校 |
| 12 | p.24 | (4.12) | `∏_{i,j}(1−z_i/z_j)^2`（分子首因子） | $i=j$ 时该因子为零、整式恒为零；应为 `∏_{i<j}` 或 `∏_{i≠j}`（同式另一个 `∏_{i,j}(1−q^{n+1}z_i/z_j)^2` 无此问题） | **Lead** |
| 13 | p.24 | 正文 | `th literature`、`through discussion` | 应为 `the literature`、`thorough discussion` | 译校 |
| 14 | p.25 | §4.3.1 | "invariant under the arbitrary shift of φ₁ and **φ₁**" | 应为 `φ₁` 与 `φ₂`（下一式 (4.14) 为 `φ_i→φ_i+ε_i`） | **Lead** |
| 15 | p.27 | (4.27) | `∏_{i,j}(a_i−a_j)` | 同 #12，$i=j$ 为零；应为 `∏_{i<j}`/`∏_{i≠j}`，即 $±∏_{i<j}(a_i−a_j)^2$ | 译校 |
| 16 | p.28 | 正文 | "when `|Y| ≥ 1`" | 应为 $|\vec Y|\ge1$（p.26 定义 $|\vec Y|=\sum|Y_i|$；原文漏箭头） | 译校 |
| 17 | p.28 | 正文 | `Hermitean` | 拼写应为 `Hermitian`。**同页的 "the the-ory" 不是笔误**：那是 "the theory" 在行末被连字断成 "the-"+"ory"，已 600 dpi 裁图复核；译者最初误判为「多一个 the」，经交叉校对指出后**已从登记表撤回** | **Lead** |
| 18 | p.29 | §5.1 | "introduced in Sec. **2.30**" | §2 无 2.30 小节，应为 §2.1.4（$q$-形变，pp.8–9，式 (2.30) 亦在该节） | 译校 |
| 19 | p.29 | §5.1 | `K(a_i)` 与 `K(0)` | 后者应为 `K_0`（(5.4) 定义；(5.2)(5.11) 均用 $K_0$；$K(a)$ 在 $a=0$ 发散） | 译校 |
| 20 | p.30 | (5.8)(5.9) | (5.8) 第二个求和的分子 `χ_m(z)χ_m(a_2)χ_n(a_3)`；(5.9) 的 `χ_m(a_3)` | 应为 `χ_m(z)χ_m(a_3)χ_m(a_4)`；`χ_m(a_3)` 应为 `χ_n(a_3)`（据 (5.7) 的指标约定） | 译校 |
| 21 | p.31 | §5.1 | `SU(2)×SU(2)_3×SU(3)_4` | 应为 `SU(2)_4`（同段下文与三基表示定义均为 SU(2)；参照点即式 (5.7)） | 译校 |
| 22 | p.32 | (5.19) | `±a+ε_1ε_2` | 应为 `±a+ε_1+ε_2`（与 §4.3.2 的 (4.18) `α·a+ε_1+ε_2` 对照） | 译校 |
| 23 | p.39 | §6.3 | "will **do** make such an epoch-making step" | 多一个 do，应为 will make | 译校 |
| 24 | p.26 | §4.3.3 | "a **non-decreasing** sequence of natural numbers $Y=(\lambda_1\ge\lambda_2\ge\cdots)$" | 词（non-decreasing，非降）与式子（$\lambda_1\ge\lambda_2\ge\cdots$，非增）自相矛盾；按 Young 图约定应为 non-increasing。正文译作「不增」并加批注 | 译校 |
| 25 | p.31 | (5.15) | $\alpha_i=m_i+(b+1/b)/2$ | 对照 (5.13)(5.14) 的 $(\pm m_1\pm m_2\pm m_3)/2$ 与 (2.48) 反推，应为 $\alpha_i=m_i/2+(b+1/b)/2$（原式差一个因子 2） | 译校 |
| 26 | p.10 | (2.34)(2.40) | 指数 $|z-w|^{-2a^2}$、$|z-w|^{-2a^2-Q^2/2}$ | 按同页明文约定（两点函数作 $(z-w)^{-2\Delta}$、$\ee^{2\ii a\phi}$ 的 $L_0=\Delta=a^2$）应为 $|z-w|^{-4a^2}$ 与 $|z-w|^{-4a^2-Q^2}$，即原文**漏因子 2**；同页 (2.55) 的 $|z|^{-2\Delta_p}$ 属同一写法。**存疑**，经两轮独立复核（编辑者与校对者各自 650–1100 dpi 裁图） | 译校 |

**另有两处「不是笔误但要知道」的读法提示**（已在批注里）：
① p.11 首句的 $T=\frac12∂φ∂φ$ 与 (2.37) 的 $T=∂φ∂φ+iQ∂²φ$ 第一项系数不一致——**是归一化约定不同**，不是笔误；
② p.20 的 $q'=1/q$、$q''=1-q$ 若与 $q=e^{2πiτ}$ 一起读会得 $τ'=-τ$，与 p.19 的 $τ→-1/τ$ 不同——这是
「四穿刺球面交比」的 anharmonic 群作用，属读法问题，未列为笔误。

## 6. 统计

| 指标 | 数值 |
|---|---|
| 底本页数 / 译本页数 | 46 / **39** |
| 编号公式 | **137**（1.1 + 2.1–2.72 + 3.1–3.11 + 4.1–4.27 + 5.1–5.26），`\tag` 集合与底本**完全一致**（脚本比对） |
| 图 / 表 | **13 / 0** |
| 参考文献 | **77** 条（0 缺号 0 重号） |
| Tutor Note 批注 | **128** 条（Lead 8 + tr-01 11 + tr-02 26 + tr-03 16 + tr-04 29 + tr-05 17 + tr-06 21） |
| 原文笔误登记 | **26** 项 + 2 项读法提示 |
| 参与者 | Lead + 6 位译者（tr-01 … tr-06），分块 19 个 `chunks/*.tex` |
| 编译 | LuaLaTeX 1.24 / TeX Live 2026，×3 遍；`file:line=0 fatal=0 undefined=0 missingchar=0 overfull=0` |
| 字体 | 37 种，**全部子集嵌入**（前缀 `XXXXXX+`） |

**三重 Gate 验收结果**（最后一轮，全部通过）：

| Gate | 内容 | 结果 |
|---|---|---|
| Gate 1 `check.py` | tag 集合 vs `tags.txt`；花括号/环境/`$` 配对；禁用命令；BOM/CRLF/U+FFFD；markdown 残留 | **PASS**（137/137，0 problem） |
| Gate 2 `build.ps1` | 真编译 ×3 | **PASS**（0 error / 0 undefined / 0 missing char / 0 overfull，PDF 1.48 MB） |
| Gate 3 `verify_pdf.py` | 成品 PDF 回读：137 条编号是否都在文本里；13 幅图注；结构关键词；字体嵌入；异常标记；抽页目视 | **PASS**（137/137，图 1–13 全在，字体全嵌入） |

## 7. 已知偏差与限制

1. **参考文献为脚本自动转录**（`work/tools/gen_refs.py` 从 PDF 文字层切分，按 `^[n]` 归并断行）。
   已保证 **77 条、0 缺号 0 重号**、版面统一；但**未逐条校对**，且文字层无上下标信息，
   数学符号被拍平：例如 $C^2\!\to$`C2`、$\mathbb{Z}_p\!\to$`Zp`、上标 $\frac12$ 变 `1/2`。
   **只宜检索，不宜引用**。
2. **图 13 内部夹带英文标注**（"6d theory on" / "4d N=2 SU(2) with 4 flavors on" / "2d Liouville theory on"）。
   这是从原文矢量图整体裁下来的，**保留了原图内的英文**；图注本身已译。若要零英文，需用 TikZ 重绘该图（本次未做）。
   图 12 内部只有 a–f 的穿孔点标签，图 1–11 的标签都是数学符号（$T,L,U,V,W,Q_{aiu},\tau,s$ 等），不涉及英文。
3. **两处公式为排版做了非内容性调整**（符号与顺序均未变）：
   (2.55) 由原文两行拆为三行以避免越界；(2.56) 用 `\resizebox{0.985\textwidth}` 收进版心。
   另有 (4.23)(4.25)(4.27)（译者）按同一规范加 `\resizebox`。
4. **脚注编号与原文不同**：原文 p.3 的脚注是 1、2，本译本由 LaTeX 统一编号，故号数可能与原文不完全对应；
   批注中已按「原文 p.N」定位。
5. **本译本页码 ≠ 底本页码**（39 vs 46），正文本身没有逐页对应关系；回查请用「原文 p.N」注释、公式号、图号。
6. **目录页码是本译本页码**，不是底本页码；底本目录（其 pp.1–2）的页码信息已记在上表。
7. **原文没有附录、表格、习题、要点框**——本译本相应地也没有；`preamble.tex` 里的
   `keybox`/`exercise`/`tabtitle` 等宏只是保留备用，未使用。
8. **未做**：TikZ 重绘图、参考文献逐条校对、英文原图内文字翻译、索引。
9. 底本 $A_1$ 型 6d 理论、class S、$T_N$ 等专业内容按作者原意直译；**译者未对物理内容作独立验证**，
   只保证「译得对、公式抄得准」。批注中的补充推导已尽力核对，但不排除有疏漏。
10. **连接号字形不统一**：部分块用 LaTeX 的 `--`/`---`，部分块直接用了 Unicode 的 en/em dash（U+2013/U+2014），
    在 ctex 下两者字形略长短不同。已检查成品 PDF：**没有出现「括号内外多空格」的排版事故**，只有长短的细微差别。
11. **(4.22)(4.25) 的指数**：原文印作 $q^{|Y|}$（p.26 的定义是 $|\vec Y|=\sum_i|Y_i|$，原文此处漏了箭头），
    译本在**公式里**按定义写作 $q^{|\vec Y|}$，并在批注中说明。这是有意的、已记录的偏离；
    逐字对照原文的读者会发现这一处差异。
12. **只有「摘要 + 译者说明」放在正文之前**；底本 p.1–p.2 的目录被替换为本译本自己的 `\tableofcontents`
    （因为两本页数不同，照抄底本目录的页码会指错），底本目录的原始页码信息见 §1 表格。

## 8. 版权声明

- 底本：© 2016 Yuji Tachikawa。原文以 arXiv 非排他许可（arXiv license）发布；
  本文为综述文集章节，正式出版版本见 *J. Phys. A: Math. Theor.*（DOI: 10.1088/1751-8121/aa5df8）。
- 本中译注本**仅供学习与研究使用**，不作商业用途，不替代原文；引用请务必引用**原文**。
- 译文与批注的著作权归译者；底本内容的著作权归原作者与出版方。
  如原作者或出版方要求，可随时移除本译本。

---

## 附：目录结构

```
deliverable/
├── 2d4d对应关系简述_中文译注本.pdf   成品（39 页，真编译）
├── src/
│   ├── main.tex                       汇总（\InputIfFileExists 逐块注入）
│   ├── preamble.tex                   导言区（宏、图注、页眉）
│   ├── build.ps1                      本机一键编译（镜像编译）
│   ├── chunks/                        19 个片段（c00/c01/tr01a…tr06b/c-refs）
│   └── figures/                       fig1.png … fig13.png（500 dpi）
├── build.ps1                          同上（根目录一份，方便直接用）
├── compile.log                        真实 lualatex 日志（0 error 凭证）
├── 译注汇总.md                        128 条 Tutor Note 全文 + 索引表
└── README.md                          本文件
```
