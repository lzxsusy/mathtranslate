# c08 交叉校对报告（reviewer：jp11-c07）

- 被校块：c08（p020–p021 / 原书 p.146–147，§8.4「镜像对称与单值性」续）
- 校对者：jp11-c07（独立复核，**未改动 c08.tex 及任何其他文件**；对照裁图存放在 `work/tmp_c07/rev_c08/`，只读证据）
- 依据：`work/pages/p020.png`、`p021.png`（150 dpi 原页全页目视 + 公式处 700–5000 dpi `work/tools/crop.py` 逐符号裁图）；`work/split/p020.txt`、`p021.txt`（仅用于定位正文，数学层不作数）；`work/BRIEF.md` §5；`work/glossary.tsv`；`work/STYLE_GUIDE.md`；`src/preamble.tex`；`src/figures/fig8_4.png`–`fig8_8.png`（与 p147 原图逐一比对）；独立重编译副本 `work/tmp_c08/test.pdf`。
- 自检复核：`python check.py c08` → `OK c08: tags=9 (8.24..8.32)`、`ALL CHECKS PASSED`；`compile_chunk.ps1 -Chunk c08` → `OK c08 : pages=3 Overfull=0 Undefined=0 MissingChar=0`；UTF-8 无 BOM、无 CR；文件末 `% CHUNK c08 DONE pages p020–p021` 在位。

## 0. 总评

9 条编号公式（(8.24)–(8.32)）逐条与图像核对：**条数、编号、左右两端、$\perp$ 位置、上下标、矩阵元、行末标点全部正确**；正文逐段对照 p020/p021，**无漏译、无增译**（nef 锥→$E_1,E_2$→$(q_1,q_2)$ 坐标→$\mathcal{N}(\check Y)\cong U\perp N$→$N$ 与 $O^+(N)$→回路单值性→扇 $\Sigma$→$C_1,C_2$→环与 $\mathbb{P}(1,2)$ 链→法丛，一段不缺一句不加）；5 幅图文件名、图注、顺序、图号（8.4→8.8）与 BRIEF §5 完全一致；术语全部符合 glossary。**只有 1 处「必须改」**（一个箭头的抄录：`, \to,` 应为 `\hookrightarrow`，见 §3），其余为措辞/版面层面的建议。

## 1. 编号公式逐条核对（9 条，全部相符）

| 编号 | 原图（p020） | c08 写法 | 判定 |
|---|---|---|---|
| (8.24) | $M_{\Delta_0}=\Pic Y_0=E_8\perp E_8\perp\bigl(\begin{smallmatrix}2&1\\1&-2\end{smallmatrix}\bigr),$ | `& M_{\Delta_0} = \Pic Y_0 = E_8\perp E_8\perp\begin{pmatrix}2&1\\1&-2\end{pmatrix},` | 相符（左端无 $\perp$，下标 $\Delta_0$ 正确） |
| (8.25) | $M_{\Delta_0}^{\perp}=U\perp\bigl(\begin{smallmatrix}2&1\\1&-2\end{smallmatrix}\bigr),$ | 同 | 相符（$\perp$ 在 $M_{\Delta_0}$ 右上） |
| (8.26) | $M_{\Delta_0}=\Pic\check Y_0=\bigl(\begin{smallmatrix}2&1\\1&-2\end{smallmatrix}\bigr),$ | 同 | 相符（**原图此处左端确实没有 $\perp$**，c08 照录并加 Note，处理正确） |
| (8.27) | $M_{\Delta_0}^{\perp}=U\perp E_8\perp E_8\perp\bigl(\begin{smallmatrix}2&1\\1&-2\end{smallmatrix}\bigr),$ | 同 | 相符 |
| (8.28) | $q_1=\lambda,$ | `& q_1=\lambda,` | 相符（尾逗号保留） |
| (8.29) | $q_2=\dfrac{\mu}{\lambda^{2}}$ | `& q_2=\frac{\mu}{\lambda^{2}}` | 相符（无尾标点） |
| (8.30) | $O^{+}(N)=\langle g_1,g_2\rangle,\ g_1=\bigl(\begin{smallmatrix}4&1\\-5&-1\end{smallmatrix}\bigr),\ g_2=\bigl(\begin{smallmatrix}1&1\\0&-1\end{smallmatrix}\bigr).$ | 同（display `pmatrix`） | 相符（末句点保留） |
| (8.31) | $T_1=\varphi_{e,e_1},$ | 同 | 相符（尾逗号保留） |
| (8.32) | $T_2=\varphi_{e,e_2},$ | 同 | 相符（尾逗号保留） |

附加数学校核（用于确认矩阵元没有互抄）：取 $N=\left(\begin{smallmatrix}10&5\\5&2\end{smallmatrix}\right)$，直接计算 $g_1^{T}Ng_1=N$、$g_2^{T}Ng_2=N$ 均成立，可见 $g_1,g_2$ 的 8 个矩阵元与 (8.30) 的 $O^{+}(N)$ 相符，**无抄错**。

## 2. 正文逐段核对（p020–p021，无漏译/增译）

- p020 首行「ここから」→「由此可得」✓；四条矩阵格公式后「となり，予想 3.1 がこの場合に成り立つことが分かる．」→「从而可知猜想 3.1 在此情形下成立。」✓。
- 「$\check X$ のネフ錐は $2D_1+D_4$ と $D_1$ で生成」→「$\check X$ 的 nef 锥由 $2D_1+D_4$ 与 $D_1$ 生成」✓；「$D_1,D_4$ 分别对应 $v_1,v_4$ 生成的一维锥（环面除子）」✓；「$2D_1+D_4$、$D_1$ 在 $\check Y$ 上的限制记作 $E_1,E_2$」✓。
- 「$H^{2}_{\mathrm{amb}}(\check Y,\mathbb C^{\times})$ 的坐标 $(q_1,q_2)$」与「二次栈的稠密环面 $\mathbb L^{\vee}_{\mathbb C^{\times}}\subset X_{\mathcal F(A_0)}$ 的坐标 $(\lambda,\mu)$」由 (8.28)(8.29) 等同 ✓（$H$ 的上标 2、下标 amb 的罗马体、$\mathbb L$ 的 $\vee$ 与 $\mathbb C^\times$ 位置均与原图一致）。
- 「$\check Y$ の代数格子は $\mathcal N(\check Y)\cong U\perp N$」→「$\check Y$ 的代数格写作 $\mathcal N(\check Y)\cong U\perp N$」✓；双曲平面 $U=\mathbb Z e\oplus\mathbb Z f$，$f=-[\mathcal O_{\check Y}]-[\mathcal O_{E_1}]+3[\mathcal O_{E_2}]$ ✓。
- **$e=[\mathcal O_p]$ 下标专核**：文字层作 `\mathcal{O}_{r}`，但 150 dpi 原页与 3000 dpi 裁图（`work/tmp_c07/rev_c08/p020_Op.png`）均显示下标为 **$p$**（有明显下伸部，非 $r$）；c08 作 `\mathcal{O}_p` **正确**，不应按文字层改成 $r$。
- $N\cong\left(\begin{smallmatrix}10&5\\5&2\end{smallmatrix}\right)$、$e_1=[\mathcal O_{E_1}]$、$e_2=[\mathcal O_{E_2}]$、「Picard 格子 $\NS(\check Y)$ と同型」✓；$\NS(\check Y)$ 的 $\check Y$ 已按图核对（见 §4(b)）。
- 「$N$ の直交群は 2 つの元で生成」→「$N$ 的正交群由两个元生成」+ (8.30) ✓。
- 两条回路的单值性：「$(q_1,q_2)\mapsto(e^{2\pi\sqrt{-1}}q_1,q_2)$」「$(q_1,q_2)\mapsto(q_1,e^{2\pi\sqrt{-1}}q_2)$」✓；「(6.4) によってそれぞれ $\mathcal O(-E_1)\otimes(-)$ と $\mathcal O(-E_2)\otimes(-)$」✓；$\varphi_{e,\bullet}$ 为 (4.25) 的嵌入 ✓；后接 (8.31)(8.32) 与「となることが直接計算によって容易に確かめられる」→「这容易由直接计算验证」✓。
- 「図8.4 にあるように…半直線を 1 次元錐とする…扇を $\Sigma$ とおく」✓；「対応するトーリック多様体 $X_\Sigma$ は，[p021] 図8.5 にある $(-1)$ 直線と $(-5)$ 直線が交互に並んだ長さが無限の鎖を $(\mathbb C^{\times})^{2}$ の境界に付け加えて得られる」✓（跨页断句处 `% ===== 原书 p.147 =====` 标在「是」与「在」之间，正确）。
- 「周期領域のトロイダルコンパクト化は尖点の近傍を $X_\Sigma$ の境界の近傍に取り替える」✓；「$X_\Sigma$ には $O^{+}(N)$ が自然に作用」✓；商 $X_\Sigma/O^{+}(N)$ 先模 $C_1\triangleleft O^{+}(N)$ 再模 $C_2=O^{+}(N)/C_1$ ✓（「位数 2」→「2 阶」正确）。
- $g_1$ 作用把一维锥移到「2 つ隣」→「与其相隔两个位置」（Tutor Note 解释为中间隔着一个一维锥，正确）；边界是由 $(-1)$、$(-5)$ 曲线如图 8.6 连成环状 ✓；$C_2$ 作用把这个环沿水平线如图 8.7 翻转 ✓；商为图 8.8 那样的加权射影直线 $\mathbb P(1,2)$ 的链 ✓；法丛 $\mathcal O_{\mathbb P(1,2)}(-1)$、$\mathcal O_{\mathbb P(1,2)}(-5)$ ✓。
- 块边界：p020 首「ここから」承接定理 8.2 之后，c08 未重复定理；结尾止于「……法丛为 $\mathcal O_{\mathbb P(1,2)}(-1)$ 与 $\mathcal O_{\mathbb P(1,2)}(-5)$。」，其后的「これらを順番に潰す」留给 c09 ✓。

## 3. 必须改（1 条）

1. **c08.tex 第 48 行：箭头抄录错。** 现文
   `$\varphi_{e,\bullet}\colon N\to O(\mathcal{N}(\check{Y}))$ 为 (4.25) 给出的嵌入，则`
   原图为 $\varphi_{e,\bullet}\colon N\hookrightarrow O(\mathcal N(\check Y))$，**箭头带钩**（$\hookrightarrow$），不是 $\to$。
   证据：p020 原页该行 $x\approx145$–$178$ pt、$y\approx572$–$588$ pt，按 5000 dpi 裁图（`work/tmp_c07/rev_c08/p020_phiarrow2.png`），箭头尾部有明显的向上弯钩；且同句下文作「埋め込み（嵌入）」，与 (4.25)（c03 块）的 `N\hookrightarrow O(T)` 一致。
   改法：`N\to O(...)` → `N\hookrightarrow O(...)`（1 个命令，不影响其余）。

## 4. 建议改（不影响正确性，建议 Lead 统一润色时一并处理）

1. **第 22–23 行**「$D_1$ 与 $D_4$ 分别是与由 $v_1$ 与 $v_4$ 生成的一维锥对应的环面除子」：一句里三个「与」，读者需停顿判断。可改「$D_1$、$D_4$ 分别是对应于由 $v_1$、$v_4$ 生成的一维锥的环面除子」。
2. **第 45–47 行**「……的单值性 $T_1$ 与 $T_2$，由 (6.4) 分别给出为 $\mathcal O(-E_1)\otimes(-)$ 与 $\mathcal O(-E_2)\otimes(-)$」：「分别给出为」略生硬，可改「由 (6.4) 分别给出」或「分别由 (6.4) 给出为」。
3. **第 74–102 行 5 个 figure**：`fig8_4`/`fig8_5` 用 `height=6.2cm`（STYLE 建议 6.5cm，属建议值，不违规；但单独编译时 5 图占 2 页，原书 5 图仅占 p147 上半页）。如希望版面更贴近原书，可把二者降到约 5.0–5.2cm、`fig8_6`–`fig8_8` 的 `width` 由 0.34 降到 0.30，或两两并排；**纯排版偏好，非必须**。
4. **第 57–58 行**「把由 $e_1$ 与 $e_2$ 经 $O^{+}(N)$ 作用移动所得的向量生成的射线取作一维锥，把以这些射线为一维锥的 $N_{\mathbb{R}}$ 中的扇记作 $\Sigma$」：两句连用「一维锥」，可压缩为「把由……所得的元所生成的射线取作一维锥，并把 $N_{\mathbb{R}}$ 中以这些射线为一维锥的扇记作 $\Sigma$」。现译不误。

## 5. 需裁定（请 Lead 定，均非错误）

1. **图 8.4–8.8 的版面**：c08 把 5 幅图集中放在块末（c09 之前），与 BRIEF/STYLE「图放在首次引用它的段落之后」不冲突（8.4 的首次引用在其前一段，8.5–8.8 的引用在同一段内），但原书是排在 p147 页首。若 Lead 要求「图随文（p020 末句之后、即跨页断句处）」可移动 figure 环境；因是 `[htbp]` 浮动体，实际位置由 LaTeX 决定，**建议维持现状**。请裁定是否需要在全书层面统一图的排版策略。
2. **c08 第 20 行 Tutor Note 的表述**：note 说「(8.24) 与 (8.26) 的左端同为 $M_{\Delta_0}$」——已复核属实（(8.26) 原图确无 $\perp$，疑为原书笔误）。是否要把该 Note 升级为「疑为原书笔误：与 (8.25)(8.27) 对照，(8.26) 左端可能漏了 $\perp$」这样的措辞，属批注尺度问题，请 Lead 定（现 Note 只陈述事实，安全）。

## 6. 图与图注核对（5 幅，全部相符）

| 文件 | 原书图号/图题（p147） | c08 图注 | 顺序/图号 | 判定 |
|---|---|---|---|---|
| fig8_4.png | 図8.4 扇 $\Sigma$ | `扇 $\Sigma$（原书 p.147）` | 8.4（首） | 相符（图为带 $(0,1),(1,0),(1,-1)$ 三点的扇形图） |
| fig8_5.png | 図8.5 トーリック多様体 $X_\Sigma$ | `环面簇 $X_\Sigma$（原书 p.147）` | 8.5 | 相符（$(-5),(-1),(-5)$ 交替无限链） |
| fig8_6.png | 図8.6 商多様体 $X_\Sigma/C_1$ | `商簇 $X_\Sigma/C_1$（原书 p.147）` | 8.6 | 相符（标 $-1$、$-5$ 的环） |
| fig8_7.png | 図8.7 $C_2$ の作用 | `$C_2$ 的作用（原书 p.147）` | 8.7 | 相符（水平虚线 + 翻转箭头） |
| fig8_8.png | 図8.8 商多様体 $X_\Sigma/O^{+}(N)$ | `商簇 $X_\Sigma/O^{+}(N)$（原书 p.147）` | 8.8 | 相符（两个标 2 的交点） |

图号顺序 8.4→8.8 与原文一致（并入 main.tex 后 c06 的图 8.1、8.2 + c07 的图 8.3 之后正好接续）；文件名拼写、`\caption` 用法（未手写编号）、`（原书 p.147）` 后缀均合规。

## 7. 术语核查（对照 glossary.tsv，全部相符）

ネフ錐→nef 锥；トーリック因子→环面除子；1 次元錐→一维锥；巨大体積極限→大体积极限；双曲平面→双曲平面；直交補空間→正交补空间；直交群→正交群；代数格子→代数格；Picard 格子→Picard 格；無限巡回群→无限循环群；巡回群→循环群；位数→阶；法束→法丛；重み付き射影直線→加权射影直线；半直線→射线；周期領域→周期区域；トロイダルコンパクト化→环面紧化；尖点→尖点；モノドロミー→单值性；埋め込み→嵌入；ループ→回路；扇→扇；トーリック多様体→环面簇；商多様体→商簇；2 次スタック→二次栈；稠密トーラス→稠密环面；輪→环。专有名词 Noether–Lefschetz、Picard、Fano 等按体例保留原文；`\Pic`、`\NS`、`\mathcal O`、`\check` 等宏使用与 preamble 相符。

## 8. 结论

**c08 通过交叉校对，无需返工。** 9 条编号公式（(8.24)–(8.32)）与 p020 原图逐项相符（含 (8.24)–(8.27) 的 $\perp$ 位置、(8.26) 无 $\perp$ 的原样照录、(8.28)(8.29) 的 $q_1=\lambda$、$q_2=\mu/\lambda^2$、(8.30) 的 $g_1,g_2$ 矩阵元、(8.31)(8.32) 的 $\varphi_{e,e_1},\varphi_{e,e_2}$）；5 幅图文件名/图注/顺序/图号全对；无漏译、无增译；术语合规。**唯一必须改**是第 48 行 `\to` → `\hookrightarrow`（1 处 1 命令），建议由 c08 译者或 Lead 顺手改；§4 的 4 条与 §5 的 2 条均为措辞/批注尺度层面的可选优化。
