# 《SYZ 猜想综述集》中文译注本 · 交付说明（README）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 为准：语料 / 轨迹 / 会话 CC BY 4.0，明确欢迎用于训练与蒸馏（译文与工程文档 CC BY-NC-SA 4.0）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

本交付包由《学术 PDF 翻译 · 标准作业手册 v2》流程制作：底本实测 → 素材制备 → 9 人分块翻译 → 合成与三重 Gate → 交叉校对 → Lead 落改 → 打包。全部数字均为实测值，未做任何"看起来完成"的静默降级。

---

## 一、底本信息与页码映射

| 章 | 英文原题 | 作者 / 出处 | 总页 | 正文 | 参考文献 | 编号公式 | 图 / 表 |
|---|---|---|---|---|---|---|---|
| 1 | The Strominger–Yau–Zaslow Conjecture and Its Impact | Kwokwai Chan，arXiv:1408.6062v2 [math.DG]，2014 | 22 | 1–15（止于 References 前） | 15–22（174 条） | 2 | 0 / 0 |
| 2 | A Glimpse of the SYZ Conjecture and Related Developments | Kwokwai Chan，ICCM 2016 会议报告 | 22 | 1–15 | 15–22（182 条） | 2 | 0 / 0 |
| 3 | The SYZ Conjecture: From Torus Fibrations to Degenerations | Mark Gross，Proc. Sympos. Pure Math.，arXiv:0802.3407v1 [math.AG] | 44 | 1–42 | 42–44（56 条） | 2 | **4 张无编号插图**（p13、p14、p17、p39）+ **1 张无编号表格**（p38） |
| 4 | Mirror Symmetry and the Strominger–Yau–Zaslow Conjecture | Mark Gross，Current Developments in Mathematics 2012，arXiv:1212.4220v2 [math.AG] | 68 | 1–64 | 65–68（78 条） | 3 | **11 张编号图**（图 4.1–4.11）+ 2 张无编号示意图（p38、p39，TikZ 重排） |
| 5 | Survey on the Metric SYZ Conjecture and Non-Archimedean Geometry | Yang Li，arXiv:2204.11363v1 [math.AG]，2022 | 48 | 1–43 | 43–48（80 条） | 21 | 0 / 0 |
| 6 | Recent Progress on SYZ Mirror Symmetry for Some Non-Compact Calabi–Yau Surfaces | Tristan C. Collins, Yu-Shen Lin，arXiv:2208.14485v1 [math.DG]，2022 | 29 | 1–26 | 26–29（64 条） | 11 | 0 / 0 |

**页码映射**：六篇均为 arXiv/会议预印本，**PDF 页号 = 印刷页号（偏移 0）**。译文严格按原文页码推进，每个原文页起始处在 LaTeX 源码中标注 `% [原文 p.N]`；正文中如出现"p.N"均指该篇自己的印刷页。

> 注：各篇正文最后一小段延伸进该篇「参考文献起始页」顶部（References 标题之前），已按页归属译出；第 4 章例外（正文止于 p64，p65 页首即 REFERENCES）。

---

## 二、结构清单

- 前置：书名页 / 目录 / **编者说明**（本集由来、六篇导读、体例、编译、版权）。
- **第一章**（Chan 2014）：1.1 SYZ 之前的镜像对称；1.2 SYZ 猜想的表述；1.3 半平坦 SYZ；1.4 构造 SYZ 纤维化；1.5 紧 Calabi–Yau 流形的 SYZ；1.6 非紧 Calabi–Yau 流形的 SYZ；1.7 非 Calabi–Yau 情形下的 SYZ；1.8 SYZ 之外。
- **第二章**（Chan 2016）：同第一章的八节结构（ICCM 报告版）。
- **第三章**（Gross 2008）：1 一个拓扑观察；2 特殊拉格朗日子流形的模空间；3 半平坦镜像对称；4 带奇点的仿射流形；5 SYZ 猜想的困难及其绕行；6 Gromov–Hausdorff 极限、代数退化与镜像；7 环面退化、相交复形及其对偶；8 对数结构；9 锥图与扇图；10 热带曲线。
- **第四章**（Gross 2013）：1 特殊拉格朗日子流形的模空间；2 半平坦镜像对称；3 带奇点的仿射流形；4 热带几何；5 SYZ 猜想的困难及其绕行；6 Gromov–Hausdorff 极限、代数退化与镜像；7 环面退化、相交复形及其对偶；8 对数结构；9 A-模型与热带几何；10 B-模型与热带几何；11 热带顶点；12 其他近期结果与未来。
- **第五章**（Yang Li 2022）：1 概述；2 度量 SYZ 猜想（2.1–2.5）；3 大复结构极限（3.1–3.3）；4 分析基础（4.1–4.6）；5 非阿基米德几何（5.1–5.6）；6 证明策略一瞥（6.1–6.3）。
- **第六章**（Collins–Lin 2022）：1 引言；2 del Pezzo 曲面上的特殊拉格朗日纤维化（2.1–2.4，含 2.3.1/2.3.2）；3 有理椭圆曲面上的特殊拉格朗日纤维化；4 非标准半平坦度量；5 超 Kähler 度量的唯一性定理；6 应用（6.1–6.3）。

**全书编号体系**：章号 = 论文序（1–6）；节号 = 章.节（自动编号，与原文节号一致）；编号公式 = 章.原编号（如第 1 章原式 (6.1) 记作 (1.6.1)）；定理类对象 = 章.节.原编号（如定理 4.5.2；原文按全章连续编号的 Question/Remark 用章.原编号，如问题 5.1）；图 = 章.图号（如图 4.3）；交叉引用一律纯文本。

---

## 三、编译方法（含字体与路径注意事项）

1. **引擎**：LuaLaTeX（TeX Live 2026），文档类 `ctexbook`，A4，11pt，编译 3 次（目录/交叉引用收敛）。
2. **命令**（本机实测）：
   ```powershell
   powershell -ExecutionPolicy Bypass -File build.ps1
   ```
3. **本机两条硬约束**（换机器时若遇到 `I can't write on file main.log` 即此因）：
   - `lualatex` 在**非 ASCII 路径**下无法写 `.log`；
   - 子进程**不能写 Desktop**。
   因此 `build.ps1` 把 `src/` 与 `figures/` 镜像到 ASCII 可写目录
   `<本地路径>`，在那里编译，再把 `main.pdf` 拷回 `src/` 与 `deliverable/`。
4. **字体**：ctex 自动选取系统字体，无需 fontconfig；跨机器若缺字体可加 `fontset=fandol`（fandol 为 TeX Live 自带中文 OpenType 字体集）。
5. **临时目录**：编译前脚本已设 `TMP`/`TEMP` 到镜像目录下的 `tmp/`。
6. **日志**：不得把日志重定向到 `<jobname>.out`（TeX 会把它当输入文件读，满屏 `Text line contains an invalid character`）；本脚本用 `Out-Null`。
7. `src/` 可独立重编译（不依赖 `work/` 中的中间素材）；`compile.log` 是真实 `main.log` 的拷贝。

---

## 四、译校体例

- **忠实**：不增删、不概括、不合并段落；原文一句对应译文一句（长句可断句但不丢信息）；公式逐符号对照 200 dpi 页图抄写。
- **批注**：译者补充说明写作 `% [Tutor Note: ...]`（LaTeX 注释，**不进入排版**），全部批注汇总于本交付包的《译注汇总.md》（**396 条**）。批注只写可验证的易错符号、被省略的论证步骤、术语辨析与原文笔误；不添加与原文无关的内容。
- **术语**：统一术语表（`src/glossary.tsv`，225 条随包交付）；人名、模型名、通行缩写（SYZ、CY、K3、ALH、CFT 等）保留原文写法；首次出现可括注英文。
- **参考文献**：按学术惯例不翻译，保留英文原貌，由脚本从底本文字层自动转录（已知限制见第七节）。
- **图**：第 4 章 11 张矢量图按 400 dpi 从 PDF 紧裁（`src/figures/p4_fig01..11.png`），未重画；第 3 章 4 张无编号插图按 500–600 dpi 裁出；第 4 章 p38/p39 两处无编号示意图用 TikZ 原样重排。原文图注只有编号的（图 4.1–4.4、4.7、4.8、4.11），译文图注留空（不自造）。
- **校对**：全部交稿后按轮次交叉校对（每人校别人一块：tag 完整性、≥8 条逐符号、结构、漏译、术语、边界接缝），Lead 以 exact-match patch 脚本落改并重编译；共 9 份校对报告、落改记录见交付源码 `PATCH_LOG.md`。

---

## 五、原文笔误登记表

> 规则：正文一律照原文排印；只有经 500+ dpi 裁图复核确认的问题才登记。状态列：**已确认**（裁图复核）/ **疑似**（未定）/ **体例不一致**（照原文，非笔误）。

| # | 章 / 页 | 原文（形式） | 说明 / 正确形式 | 状态 |
|---|---|---|---|---|
| 1 | 3 / p5 | Leray 谱序列图 d₁/d₂ 标注 | 按标准双度约定 $d_r:E^{p,q}\to E^{p+r,q-r+1}$，(0,3)→(2,2) 的箭头应为 $d_2$，原文标作 $d_1$ | 疑似 |
| 2 | 3 / p24 | "refinement $\tilde\Sigma'$ of $\Sigma'$" | 被加细者应为 p.24 定义的 $\tilde\Sigma$；$\Sigma'$ 已在 §4/p.12 定义、属另一侧 | 已确认（照原文+批注） |
| 3 | 3 / p27 | "a fan $\Sigma_\sigma$ in $\mathbb{R}^p$" | 同段前文明确 $\Sigma_\sigma\subset\mathbb{R}^{n-p}$，应为 $\mathbb{R}^{n-p}$ | 已确认 |
| 4 | 3 / p29 | $\tilde\Sigma'$ 与 $\tilde{\check\Sigma}'$、$\tilde{\check\Sigma}$ | 两套重音记号并存，属不同对象，非笔误；按原文分别照排 | 体例不一致 |
| 5 | 3 / p31 | "away from $X$" | 前两句刚说 away from $Z$，此处应为 $Z$ | 已确认 |
| 6 | 3 / p38 | 花体 $\mathcal{P}$（cones over elements of） | 按上下文疑为幺半群 $P$；页图为花体 | 已确认（字形） |
| 7 | 3 / p4, p10, p15, p25, p29, p30, p42 | Mihkalkin / affine stucture / an real / symetrically / as simply possible / torseur | 拼写笔误（Mikhalkin / affine structure / a real / symmetrically / as simply as possible / torsor） | 已确认 |
| 8 | 4 / p10 | "$g_{ij}=\partial^2K/\partial y_j\partial y_k$" | 左右指标不一致，应为 $g_{jk}=\partial^2K/\partial y_j\partial y_k$ | 已确认 |
| 9 | 4 / p15 | $\prod_j q_j^{c_{ij}}=e^{-2\pi d_j}$ | 方程按 $1\le i\le p$ 编号，右端应为 $e^{-2\pi d_i}$ | 已确认 |
| 10 | 4 / p12 | "the vertices of $\Gamma$ on the edges of $\Xi$" | $\Xi$ 在本章此前未定义，疑为 $\Delta$ | 疑似 |
| 11 | 4 / p25 | "(i.e., $\tilde V_i\cap\mathcal{X}_\varepsilon$)" | 同句后半作 $\mathcal{X}_t$，疑下标应为 $t$（原文前后本不一致） | 已确认（照原文） |
| 12 | 4 / p29 | $C(\sigma_x)=\{(rm,r)\mid m\in\sigma,r\ge0\}$ | 按 p22/§定义应为 $m\in\sigma_x$ | 已确认 |
| 13 | 4 / p61 | $f_{\mathfrak d}=(1+t^2xy)^4/(1-t^4x^{-2}y^{-2})^4=(1-t^2x^{-1}y^{-1})^{-4}$ | 分子按对 $f_{\mathfrak d}$ 取指数应为 $(1+t^2x^{-1}y^{-1})^4$ | 已确认 |
| 14 | 5 / p1 | "Stominger–Yau–Zaslow" | 漏 r（Strominger） | 已确认 |
| 15 | 5 / p3 | "skyscrapper sheaves" | 应为 skyscraper | 已确认 |
| 16 | 5 / p15 | "Kontsevich and Tscinkel" | 应为 Tschinkel（人名保留原文拼写+批注） | 已确认 |
| 17 | 5 / p10 | Example 3.1 "union of $n+2$ projective planes" | 一般 $n$ 应为射影超平面 $\PP^n$（仅 $n=2$ 是"平面"） | 已确认 |
| 18 | 5 / p29 | 式 (15) 分母「$\{\{\sum_j\cdots\}$」 | 两个左花括号仅配一个右花括号，外层未闭合；译文视觉复现+批注 | 已确认 |
| 19 | 5 / p32 | 式 (17) 的 "MA" 排正体，而 (16) 排斜体 | 同一缩写前后字形不一致；按页图分别照排 | 体例不一致 |
| 20 | 5 / p32 | "Kolodziej's" | 通行拼法 Kołodziej；原文无 ł，照原文 | 已确认（照原文） |
| 21 | 5 / p39 | "…从而验证了命题 6.5 的假设" | 按逻辑第二处应为命题 6.3 | 已确认 |
| 22 | 6 / p1 | 资助脚注 "is supported in by" | 英文笔误（应为 supported in part by）；中译照原意 | 已确认 |
| 23 | 6 / p2 | $\check D\in|-K_Y|$ | 同段下一行作 $\check Y$，应为 $|-K_{\check Y}|$ | 已确认 |
| 24 | 6 / p4 | $L_\varepsilon=\cdots\subseteq X$ | 按上下文应为 $\subseteq X_{\mathbb C}$ | 已确认 |
| 25 | 6 / p9 | $\widetilde\Gamma(v,u,b_0)$ 与 $(u,v,b_0)$ | 两括号内变量次序不同；原文如此，照排 | 体例不一致 |
| 26 | 6 / p11 | "$T_\sigma^*\check\omega_{sf}=\check\omega_{sf,b_0,sf}$" | 末下标按定义为 $\varepsilon$ | 已确认 |
| 27 | 6 / p11–12 | 定理 4.2/4.5 中 "$\check\omega_0$ 是 $X$ 上的 Kähler 形式" 与 $[\check\omega_0]_{BC}\in H^{1,1}(X)$ | 应为 $\check X$ | 已确认 |
| 28 | 6 / p12 | 定理条件(2) "$T_h^*\check\omega$" | 缺下标，按同定理末尾应为 $T_h^*\check\omega_{sf,b_0,\varepsilon}$ | 已确认 |
| 29 | 6 / p12 | 定理 4.5 的 Re/Im 排作数学斜体 | 与原书 p6 正体不同；照原样并加注 | 体例不一致 |
| 30 | 6 / p17 | 定理 6.1 结论 "$(\check Y',\check D)\cong(\check Y,\check D)$" | 第二个配对缺 $'$ | 已确认 |
| 31 | 6 / p24 | ① 两处均印 $\check X$（后者应为 $\check X'$）；② "$(\omega'-\operatorname{Im}\Omega')$" 少于虚数单位 | 已确认 | 已确认 |
| 32 | 6 / p16, p25 | "Fukaya-Siedel" / "Sympectomorphisms" | 拼写笔误（Seidel / Symplectomorphisms） | 已确认 |
| 33 | 2 / p4 | 全纯体积形式句 "…$X$ is equipped with … $\check\Omega$" | 按上下文应为 $\check X$ | 已确认 |
| 34 | 2 / p1, p5 | "predictions … is" / "is a special Lagrangian fibrations" | 英文语法笔误（不影响数学） | 已确认 |
| 35 | 1 / p3 | 脚注 1 的 "integral affine structure" 定义 | 与正文一致（非笔误），保留 | — |

---

## 六、统计

| 指标 | 数值 |
|---|---|
| 底本 | 6 篇英文综述，共 233 页（正文 200 + 参考文献 33） |
| 成品 PDF | **189 页**（A4，`SYZ猜想综述集_中文译注本.pdf`） |
| 章 / 节 | 6 章 / 约 60 节（含子节、子子节） |
| 编号公式 | 41 条（1.6.1–1.6.2；2.6.1–2.6.2；3.1–3.2；4.10.1–4.10.3；5.1–5.21；6.2.1–6.6.4） |
| 图 / 表 | 第 4 章 11 张编号图 + 2 张无编号示意图（TikZ）；第 3 章 4 张无编号插图 + 1 张无编号表格 |
| 参考文献 | 634 条（自动转录，**0 缺号 0 重号**） |
| Tutor Note | **396 条**（见《译注汇总.md》） |
| 分工 | 9 人：Lead 1 块 + 8 位译者各 2 块 = 17 块（每块 9–15 原页） |
| 交叉校对 | 9 份报告（每块至少 1 人独立校对），必须改全部落改，可选改取舍记录于 `PATCH_LOG.md` |
| 编译 | LuaLaTeX ×3：**file:line 错误 0 / Undefined 0 / Missing character 0 / Overfull hbox 3（均 < 13pt）** |
| 制作日期 | 2026-11-04 |

---

## 七、已知偏差与限制

1. **参考文献为自动转录**：从底本文字层解析（`gen_refs.py`），已做连字、重音、希腊字母、常见数学符号的映射与"缺号/重号"检查（634 条，0 缺号 0 重号），但**数学公式被拍平**（如 $C^2/\mathbb{Z}_p$ 可能显示为 C2/Zp），个别特殊字符被丢弃或近似。未逐条人工校对——这是本交付最明确的已知偏差。
2. **图未重画**：第 4 章 11 张图为 400 dpi 紧裁（保留原文图内文字与线条），第 3 章 4 张为 500–600 dpi 裁图；放大后略见位图边缘。第 4 章 p38/p39 两处无编号示意图为 TikZ 重排（非裁图）。
3. **原文图注只有编号的图**（图 4.1–4.4、4.7、4.8、4.11）：译文图注留空（只印"图 4.N."），未自行补写图注；说明见源码批注。
4. **无编号图/表**（第 3 章 p13/p14/p17/p39 插图、p38 表格）：按原文不加图号/表号（不伪造编号），无 `\figtitle`/`\tabtitle`。
5. **编号公式仅 41 条**：六篇底本本身只对少数公式编号（大量公式无编号），译文严格跟随，不自行加号。
6. **公式抄写**：底本文字层数学不可信（分式/上下标/花体常错），全部公式按 200 dpi 页图逐符号抄写；仍可能存在个别误读，欢迎指正。
7. **原文笔误**：只登记经裁图复核确认者；未确认者记为"疑似"（见第五节）。
8. **记号约定**：第 4 章中 $\mathcal{P}$ 与 $\mathscr{P}$ 依原文页图分别保留（同一章中两种字体并存，系原文如此）；原文按全章连续编号的 Question/Remark 采用"章.原编号"（如问题 5.1），与按节编号对象（如定理 4.5.2）并存。
9. **3 处 Overfull hbox**（最大 12.9pt）：均为个别宽公式/长行，未影响版面与内容；已在编译日志中如实保留。
10. **底本版本**：以第一节所列 arXiv/会议版本为准；若读者使用其他版本，页码可能不同。
11. **个别章节无摘要/致谢**：第 2 章原文无 Abstract；第 4、6 章原文无致谢（按原文，不补写）。

---

## 八、版权声明

六篇底本的版权归原作者与出版方所有（arXiv 预印本按 arXiv 许可；ICCM 报告按会议出版方许可）。本译本为**学习与研究用途的非商业性译注**，不替代原文；引用原文内容请以原文为准。译文、批注与编排的疏漏由译者负责，欢迎读者指正。

---

## 附：交付包清单

```
deliverable/
├── SYZ猜想综述集_中文译注本.pdf     成品（189 页，真编译）
├── src/                             全部 LaTeX 源码（main.tex, preamble.tex, chunks/, figures/, glossary.tsv）
├── build.ps1                        一键编译（镜像目录 + lualatex ×3）
├── compile.log                      真实编译日志（0 error 凭证）
├── 译注汇总.md                       396 条 Tutor Note（脚本生成）
├── 校对报告/                          9 份交叉校对报告（每块至少 1 人独立校对）
├── PATCH_LOG.md                      Lead 落改记录（exact-match，逐条可审计）
└── README.md                        本文件
```
