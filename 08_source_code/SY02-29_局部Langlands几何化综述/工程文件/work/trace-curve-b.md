# trace-curve-b —— §1.5–§1.6（p.10–p.16）决策流水

tag：curve-b　底本：Fargues, *Geometrization of the local Langlands correspondence: an overview*（2016-02-02）
逐条格式：**原文 → 我的处理 → 依据**。凡「图上核」= `工程文件/work/pages/pNNN.png` 的放大裁片（用 150–600 dpi 重渲染后裁切比对）。

## A. 版式与宏

1. **承接 s02，不写 `\section`**
   原文 → §1.5、§1.6 仍属第 1 节。处理 → 只写 `\subsection{概形曲线}`、`\subsection{untilt 作为概形曲线上的 Cartier 除子}`。
   依据 → s02 已有 `\section{曲线}`；若本文件再写 `\section`，全书会多出一节并把编号推到 2.x。

2. **小标题保留原号**
   原文 → `1.5.1. Definition.` 一类。处理 → `\subsubsection*{1.5.1.\ 定义}`（星号版，号写在标题里）。
   依据 → SPEC 体例；与 s02 的 `1.1.1.` 等写法一致。

3. **草稿编号守卫**
   原文 → 本块定理号从 **1.24** 起、公式号 **（6）**。处理 → 文件头
   `\ifnum\value{section}=0\relax \setcounter{section}{1}\setcounter{theorem}{23}\setcounter{equation}{5}\fi`
   依据 → preamble 的 definition/proposition/… 共用 `[section]` 计数器；s02 收在 `prop:1.23`（23 个环境）与 equation=5。单章 `build.bat check` 时 `section=0`，守卫生效；全书里 `section=1`，整块跳过。实测 aux：1.24–1.33 与 (6) 全部正确。

4. **公式 (6) 不用 `\tag`**
   原文 → p.14 的编号 (6) 排在公式左侧。处理 → `\begin{equation}\label{eq:1.6}…\end{equation}`，编号依计数器自然得到 (6)。
   依据 → 这样全书里 s04 的下一个编号公式会自动接 (7)；若用 `\tag{6}`，计数器停在第 5，后续会重号。（最初用过 `\tag{6}`，后弃。）

5. **页锚**
   - p.10：`\subsection{概形曲线}` 之后一行 `\srcpage{10}`——原文 p.10 末行就是 §1.5 标题。
   - p.11 / p.14：`\subsubsection*{…}` 之后成行放 `\srcpage{N}`（其后紧跟标题或定理环境，垂直模式下实测不产生空段落）。
   - p.12 / p.13 / p.16：`\leavevmode\srcpage{N}` 紧贴下一段正文行首（`\leavevmode\srcpage{12}定义`、`\leavevmode\srcpage{13}由此推出…`、`\leavevmode\srcpage{16}这给出典范同构`）。
     依据 → 先试过「成行 `\leavevmode\srcpage{13}` + 空行」，渲染出一个空段落（`\marginnote` 独占一行，p.3 与「由此推出」之间多出约一行空白，见 `chk-3.png` 初版）；改成贴行首后空白消失（`v3-3.png`）。
   - p.15：页界落在 “Let us form **|** the convergent Weierstrass product” 句中 → `\srcpageinl{15}`，渲染为行内小号 `〔p.15〕`。
   - 7 个锚全部在正文，不在任何环境内部（脚本核过 `\begin…\end` 区间）。

6. **p.15 交换图**
   原文 → `B⁺_dR(R♯) --θ--> R♯`（θ 双箭头），`R` 用斜箭头指 `B⁺_dR`，`R` 与 `R♯` 之间等号双线。处理 →
   `\begin{tikzcd} \mathrm{B}^{+}_{dR}(R^\sharp)\arrow[r,two heads,"\theta"] & R^\sharp \\ & R\arrow[ul]\arrow[u,equal] \end{tikzcd}`
   依据 → 600 dpi 裁片核过：θ 的箭头是双箭头；`R→R♯` 是双线等号；斜箭头无标号。

7. **marginnote 出界（全书问题，未改 preamble）**
   实测 → `_check_b.log` 报 `\marginparwidth=116.0pt`，而 geometry `margin=2.6cm`≈73.7pt；`p.N` 画在版心外、贴纸缘（v3-3.png 里 `p.13` 在 x≈1130/1241px）。
   依据 → 与 s02 报告 §4 同一结论；任务禁止改 preamble，故校验口径取 `.pagemarks`（7 个锚齐全有序）。**建议 Lead 在 preamble 加 `\setlength{\marginparwidth}{2cm}`。**

8. **`⟦ ⟧` 兜底**
   原文 → `R°⟦π⟧`、`E⟦T⟧`、`O_E⟦T⟧`、`R⟦T⟧`。处理 → 文件头 `\providecommand{\llbracket}{[\![}` / `\rrbracket`，正文一律 `\llbracket…\rrbracket`。
   依据 → preamble 未载 stmaryrd；与 s02 同一兜底。600 dpi 下呈双竖笔，可辨为双括号；若 Lead 统一加 stmaryrd，`\providecommand` 自动让位。

## B. 公式逐符号核对（图上核）

9. **$(R^{\circ\circ})^d$ 的同构**
   图上核 → `(x_0,…,x_{d-1}) ↦ Σ_{i=0}^{d-1} Σ_{n∈Z} x_i^{q^{-n}} π^{nd+i}`。指数是 **$q^{-n}$（负指数）**，不是 $q^n$；内层对 $n∈\ZZ$ 双向求和，外层 `i=0…d-1`，幂次 `nd+i`。→ 照排（`\sum_{i=0}^{d-1}\sum_{n\in\ZZ}x_i^{q^{-n}}\pi^{nd+i}`）。

10. **形式群 $\mathscr{G}_d$**
    图上核 → 花体 `𝒢_d`（script），右端 `Ĝ_a^d` 是**双线体** $\mathbb{G}$ 带帽。→ `\mathscr{G}_d=\widehat{\mathbb{G}}_a^d`。
    $\pi$ 的作用 `(X_0,…,X_{d-1})↦(X_{d-1}^q,X_0,…,X_{d-2})` 逐符号核过。

11. **$f^{-1}(\pi f)$ 的余项**
    图上核 → `f^{-1}(\pi f) ≡ πT + αT^q mod T^{q^2}O_E⟦T⟧`，`α ∈ 1+πO_E`。注意余项模的是 $T^{q^2}$（不是 $T^{q}$）。→ 照排 `\mathrm{mod}\ T^{q^2}\oo_E\llbracket T\rrbracket`。

12. **$\mathscr{G}$ 与它的提升**
    原文三处：p.11 “Note 𝒢 for 𝒢₁”、“a lift 𝒢̃ of 𝒢”、“$[π]_{𝒢̃}=f^{-1}(πf)$”、p.12 “$f=\log_{𝒢̃}$”。
    图上核 → 三处都是**同一花体** 𝒢，提升只多一道波浪号；`Note G for G1` 的文本抽取丢了下标。→ 群律 `\mathscr{G}`、提升 `\widetilde{\mathscr{G}}`，`[\pi]_{\widetilde{\mathscr{G}}}`、`\log_{\widetilde{\mathscr{G}}}`。

13. **$\eta$ 与 $u_\varepsilon$**
    图上核 → `η = lim_{k→+∞}[π^k]_{𝒢̃}(ε^{q^{-k}}) ∈ R^{∘∘}⟦π⟧`；`u_ε = η/φ^{-1}(η) = [π]_{𝒢̃}(φ^{-1}(η))/φ^{-1}(η) ∈ 𝐀`（两行，第二行分母同）。→ 照排；`𝐀=R^∘⟦π⟧` 用 `\mathbf{A}`（原文黑体）。

14. **$u_\varepsilon=\varepsilon^{(q-1)/q}+\pi(1+\beta)$**
    文本抽取得 `ε^{q−1 q}`，符号层不可信。600 dpi 裁片核 → 指数是 $\frac{q-1}{q}$，`β∈R^{∘∘}⟦π⟧`。→ `\varepsilon^{\frac{q-1}{q}}+\pi(1+\beta)`。

15. **$\Pi^\pm$ 与部分分解**
    图上核 → `Π^+(u_ε)=∏_{k≥0} φ^k(u_ε)/π ∈ O(Y_{R,R+})`；`Π^-(u_ε)=φ^{-1}(η)`；想象成 “∏_{k<0}φ^k(u_ε)”（加引号，原文即加引号）；`η=φ^{i-1}(η)·∏_{i≤k<0}φ^k(u_ε)`（乘积下界 `i≤k<0`，顿号点是原文的 `.`）。→ 照排，引号用中文「」包裹数学。

16. **$R_\varepsilon$、$\theta_\varepsilon$ 与 Tate 模**
    图上核（600 dpi）→ `R_ε=𝐀[1/π]/u_ε`（斜杠形式，不是分式）；`θ_ε:𝐀[1/π]→R_ε`；`(θ_ε(φ^{-n}(η)))_{n≥0}` 是 `T_π(𝒢̃⊗_{O_E}R_ε^∘)` 的一组基——**波浪号只在 𝒢 上**，⊗ 无帽（一度疑心是 `\widehat{\widetilde{\mathscr{G}}}`，放大后否掉）。→ `T_\pi(\widetilde{\mathscr{G}}\otimes_{\oo_E}R_\varepsilon^\circ)`。

17. **区间与范数**
    图上核 → `I ⊂ ]0,1[` 端点落在 $p^{\mathbb{Q}}$；`δ:|Y_{R,R+}|→]0,1[`；`‖\varpi_R‖=1/p`。→ 照排（`\,]0,1[` 保留原文的半开区间写法）。

18. **定义 1.25 与两条 bullet**
    图上核 → `‖ξ‖=‖a_0‖`；第一条 `A={k∈\ZZ \mid ‖u_{\varepsilon^{q^k}}‖∈I}`——下标是 **$u_{\varepsilon^{q^k}}$**（对 $\varepsilon$ 取 $q^k$ 次幂），不是 $u_\varepsilon^{q^k}$；`t_ε=∏_{k∈A}φ^k(u_ε)×u`，`u∈O(D^*_I)^×`；第二条 `O(D^*)u_ε+O(D^*)u_{\varepsilon^n}=O(D^*)`。→ 照排。

19. **1.5.3 的群律互相同构**
    图上核 → `𝒢(R^∘) ≅ O(Y_{R,R+})^{φ=π}`，`ε ↦ t_ε:=Σ_{n∈Z}[ε^{q^{-n}}]π^n`（方括号是群律 $[\;]$ 记号）。对数 `log_𝒢=Σ_{n≥0}T^{q^n}/π^n`。→ 照排。

20. **$O(1)=\widetilde{P}[1]$**
    图上核 → p.14 `O(1)=P̃[1]`，P 上有波浪号、后接 `[1]`。→ `\oo(1)=\widetilde{P}[1]`。

21. **$T_\pi(\widetilde{\mathscr{G}}\otimes_{\oo_E}R^{\sharp,\circ})=\oo_E$**
    图上核 → 波浪号只在 𝒢 上；$R^{\sharp,\circ}$ 上标为 $\sharp,\circ$。原文该 $\oo_E$ 下有一道短横（疑残留），按无排。→ 照排。

22. **公式 (6)**
    图上核 → `(6)  Γ(X^{ad},ℒ_ξ(d)) ⊂ O(Y)[1/ξ]^{φ=π^d}`，编号 (6) 在**左侧**。→ `\begin{equation}` 的编号默认在右，需注意：本机 book 类 `\theequation` 在右侧，原文在左属该刊（Astérisque）版式，**未强行复刻左置**，只保证号码为 (6)。若 Lead 要求左右一致，可在 preamble 统一用 `leqno`。

23. **$\times\Pi^+(\xi)$ 的上标**
    图上核 → `×Π^+(ξ):Γ(X^{ad},ℒ_ξ^{ad}(d)) \xrightarrow{\sim} O(Y)^{ξφ=π^{d-1}}`。上标确是 **$\xi\varphi=\pi^{d-1}$**（无逗号、$\xi$ 与 $\varphi$ 连写），已加 `\yizhuw` 释义为「先在 ξ 处局部化，再取 φ(x)=π^{d-1}x 的元素」。→ 照排。

24. **$N_\xi$ 与命题 1.30**
    图上核 → `N_ξ=⊕_{d≥0}O(Y)^{ξφ=π^{d-1}}`；命题写 `ℒ_ξ=Ñ_ξ`（N 上宽波浪号）。→ `\widetilde{N_\xi}`。

25. **1.6.2 的归约**
    图上核 → `R̃=R^∘/R^{∘∘}`，`ξ̃` 是 ξ 在 `W_{O_E}(R̃)` 中的归约；结论 `ξ̃=π` ⇔ `ξ∈π+W_{O_E}(R^{∘∘})`。→ 照排（`\widetilde{R}`、`\widetilde{\xi}`）。

26. **定义 1.32 的字体**
    图上核 → `B` 是正体、`dR` 是斜体下标、`+` 在上。→ `\mathrm{B}^{+}_{dR}(R^\sharp)`，`\mathrm{B}_{dR}(R^\sharp)=\mathrm{B}^{+}_{dR}(R^\sharp)[1/\xi]`。

27. **p.16 的 $E$-代数结构**
    图上核 → `R⟦T⟧ ≅ B⁺_{dR}(R♯), T↦ξ`；下面另起一行 `F_q((π))→R⟦T⟧, π↦T+a`（原文是两行居中，不是交换图）。→ 用 `aligned` 两行。

## C. 术语与译法

28. **schematical curve → 概形曲线**；与之相对的 adic 曲线保留 adic 不译（glossary「adic 空间」）。定义 1.24(2) 首现处加 `\yizhu`。

29. **untilt / GAGA / affinoid / ind- / pro-étale 不译**（glossary）。untilt 全篇作名词：「$S$ 的任一 untilt $S^\sharp$」「与 $S^\sharp$ 相联系的本原元」。

30. **perfectoid → 完满**；formal completion → 形式完备化；Cartier divisor → Cartier 除子；primitive of degree 1 → 次数 1 的本原元；pseudo-uniformising element → 伪一致化元；Lubin–Tate group law → Lubin–Tate 群律；Tate module → Tate 模。

31. **综述体口语保真**（未雅化）：
    - “Maybe it is a good idea to explain in more details the characteristic $p$ case.” → 「也许值得更详细地解释特征 $p$ 的情形。」
    - “Let's come back to the preceding situation.” → 「让我们回到前面的情形。」
    - “The almost here is due to the fact that…” → 「这里的『几乎』是因为……」
    - “Even if this product has no meaning let us remark that…” → 「即使这个乘积没有意义，我们仍要指出……」
    - “But one has to be a little bit careful” → 「但这里要小心一点」。
    - “We're seeking for a Weierstrass product expansion of” → 「我们要找……的 Weierstrass 乘积展开。」

32. **斜体断言照排**：p.11 “In this case $X_F$ is a Dedekind scheme.”、p.14 “the curve exists in itself without a fixed line bundle $O(1)$ on it” → `\emph{}`。

## D. 疑误处理（照原样或按文意 + 说明）

33. **§1.5.3 标题 equal → 疑为 unequal**（重点，报告 §4 已单列）
    图上核 → 标题确为 “The analog computation in **equal** characteristic.”。但本节内容全是不等特征（`[E:\QQ_p]<+\infty`、Lubin–Tate 群律、$W_{\oo_E}(R^\circ)$），且 §1.5.2 才是等特征、§1.6.2 明写 “The unequal characteristic case”。
    处理 → **标题照译「等特征下的类似计算」，正文照原文译，未改一个词**；源文件在标题上方留了三行注释说明。请 Lead 决定是否在标题加译者注或径改「不等特征」。

34. **p.15 “A usual”** → 按 “As usual” 理解，译「照例」，加 `\yizhuw` 说明原文拼写。
    依据 → 600 dpi 裁片确认原文确为 “A usual,”（不是抽取错误）。

35. **p.14 推论 1.28 “is the the categorical quotient”** → 冠词重复，中译无对应，只译一次，未加注（报告 §4 记一笔）。

36. **p.15 “Weirstrass”** → 原文拼写，译名用正字「Weierstrass」，未加注。

37. **p.14 $\oo_E$ 下的短横** → 放大核过，确有一道短横压在 $\oo_E$ 下，疑排版残留（同页其他 $\oo_E$ 无此横）。→ 按无排，报告 §4 记录。

38. **p.13 “with reduction 𝒢”** → 与群律同一花体字形（原文未用黑体 $\mathbb{G}$）。逻辑上归约应是 $\mathbb{G}$，但图上核两处字形一致。→ 照排两处 `\mathscr{G}`，报告 §4 记录，请 Lead 定夺是否统一改黑体。

39. **p.14 “this cartier divisor”**（小写 c）→ 译名照「Cartier 除子」，不保留大小写错误。

## E. 自查

40. **页锚 7 个**：`grep -c srcpage` = 7；`.pagemarks` = 10 11 12 13 14 15 16（各一次）。注意全书里 p.10 会与 s02 的 `\srcpage{10}` 重复（报告 §4 已提请 Lead 择一）。
41. 无 `??`；无空段落（`_check_b.log` 无 `Underfull \hbox (badness 10000) in paragraph`）；`\srcpage` 不在脚注、不在任何环境内部。
42. 定理号 aux 实测 1.24–1.33 连续无缺；公式 (6)。
43. 编译：`./build.bat check sections/s03-curve-b.tex b` → `[OK] _check_b.pdf`，7 页，0 error，无 Overfull/Underfull，无 undefined control sequence。
44. 注意：路径必须正斜杠（`sections\s03-…` 会被 TeX 当控制序列）；MSYS bash 下 `cmd //c "build.bat …"` 只开交互 cmd，直接 `./build.bat …`。
