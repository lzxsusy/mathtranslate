# r-bung —— §2「叠 Bun_G」译校报告

- 译手：bung　｜　底本：Fargues, *Geometrization of the local Langlands correspondence: an overview*（2016-02-02），p.16–p.23（p.23 §3 之前止）
- 交付：`源码/sections/s04-bung.tex`（新建，27.7 KB，538 行，正文汉字约 3 250）
- 自检：`cd 源码 && cmd /c "build.bat check sections/s04-bung.tex c"` → **[OK]，10 页，0 error**；log 中 Overfull 0、Underfull 0、Missing character 0、Undefined control 0；`_check_c.pagemarks` = 16 17 18 19 20 21 22 23（八行齐全）。
- 说明：check 版单独编译本文时节号为 1，故显示 1.x；整书 `main.tex` 中 s02-curve-a 为 §1、本文件紧随其后为 §2，即自动印成 2.1–2.27，与原文逐条对齐。

## 1. 编号对齐表（原文 ↔ 译文，逐条）

| 原文 | 类型 | 源页 | 译文环境 | 备注 |
|---|---|---|---|---|
| 2 | 节标题 | p.16 | `\section` | “叠 Bun_G”；标题用 `\texorpdfstring` 避免书签里出现数学 |
| 2.1 | Def | p.16 | `definition` `def:2.1` | ⊗-正合函子，记 Bun_G |
| 2.2 | Prop | p.16 | `proposition` `prop:2.2` | “技术性结果，读者可直接接受” |
| 2.3 | **Hope** | p.16 | `hope` `hope:2.3` | preamble 已定名「期望」；语气弱于猜想，见疑点 1 |
| 2.4 | Prop | p.16 | `proposition` `prop:2.4` | Isom 层是菱形 |
| 2.5 | Prop | p.16 | `proposition` `prop:2.5` | f_*ℰ 可表；证明中 Kedlaya–Liu 部分消解 |
| 2.6 | Cor | p.17 | `corollary` `cor:2.6` | 对角线可表 |
| 2.7 | Ex | p.17 | `example` `ex:2.7` | 展开乘积公式与 𝒱₁×𝒱₁→𝒱₂ 逐符号复原 |
| 2.8 | Def | p.18 | `definition` `def:2.8` | 代数菱形 = 𝕍ⁿ_{d/S} 的子层 |
| 2.9 | Prop | p.18 | `proposition` `prop:2.9` | Pres_𝒟 可表；𝕍ᵐ¹ᵐ²_{d₁−d₂}=M_{m₁,m₂} |
| 2.10 | Prop | p.18 | `proposition` `prop:2.10` | Bun_G=∪U_n，datum 𝒟_n |
| 2.11 | Thm | p.19 | `theorem` `thm:2.11` | （[10]）本质满 |
| 2.12 | Thm | p.20 | `theorem` `thm:2.12` | (1)(2) 两条 |
| 2.13 | Thm | p.20 | `theorem` `thm:2.13` | B(G) ≃ H¹_ét(X^sch,G)，带点集 |
| 2.14 | Conj | p.20 | `conjecture` `conj:2.14` | |
| 2.15 | Thm | p.21 | `theorem` `thm:2.15` | κ 在 Bun_{G,F̄_q} 上局部常值 |
| 2.16 | Conj | p.21 | `conjecture` `conj:2.16` | 每个 α-分支连通 |
| 2.17 | Thm | p.21 | `theorem` `thm:2.17` | HN 映射半连续；HN 用 `\HN`（正体），见疑点 8 |
| 2.18 | Cor | p.22 | `corollary` `cor:2.18` | 半稳定轨迹开 |
| 2.19 | Def | p.22 | `definition` `def:2.19` | J̃_b(S)=Aut(ℰ_b|_{X_S}) |
| 2.20 | Prop | p.22 | `proposition` `prop:2.20` | basic 时 J̄_b(E)=J̃_b（下划线照原文） |
| 2.21 | Ex | p.22 | `example` `ex:2.21` | 平凡丛自同构 = 𝒞(|S|,G(E)) |
| 2.22 | Rmk | p.22 | `remark` `rem:2.22` | 与经典情形相反 |
| 2.23 | Prop | p.22 | `proposition` `prop:2.23` | π₀(J̃_b)=J_b(E)、J̃_b=J̃_b⁰⋊J̄_b(E) |
| 2.24 | Ex | p.22 | `example` `ex:2.24` | GL₂ 矩阵，两对角元 E^× 照原文加下划线 |
| (7) | 公式 | p.22 | `equation` `eq:2.7` | κ: B(G)_{basic} ≃→ π₁(G)_Γ |
| 2.25 | Prop | p.22 | `proposition` `prop:2.25` | 基本轨迹只是一个点 |
| (8) | 公式 | p.23 | `equation` `eq:2.8` | x_b: [Spa(F̄_q)/J̄_b(E)] → Bun^{α,ss} |
| 2.26 | Thm | p.23 | `theorem` `thm:2.26` | (8) 是同构 |
| 2.27 | Prop | p.23 | `proposition` `prop:2.27` | 分层空或一点 |

小节：2.1 / 2.2 / 2.3 / 2.4 / 2.5 / 2.6（`\subsection`），2.2.1 / 2.2.2 / 2.2.3 / 2.6.1 / 2.6.2（`\subsubsection*`，标题内保留原文号）。
合计：**27 个编号环境 + 2 个编号公式**，与原文 2.1–2.27、(7)(8) 一一对应，无跳号、无重号（编译后正文实际印出 1.1–1.27 连排，逐条核过）。

## 2. 页锚（`\srcpage`）

| 锚 | 源码行 | 语义位置 | 说明 |
|---|---|---|---|
| 16 | 7 | `\section` 之后、2.1 标题前 | p.16 起点即 §2 标题 |
| 17 | 60 | “更确切地说，对 E=F_q((π)) 的情形：”之后、itemize 前 | 原文页界正落在此句冒号后（句子跨页，锚置于段落末） |
| 18 | 129 | 例 2.7 收尾句之后、⊕𝕍_{d/S} 斜体段之前 | 见疑点 11 |
| 19 | 188 | 命题 2.10 段末“这给了我们 Bun_G 的一个‘表示’。”后 | p.19 首件为 2.2 标题 |
| 20 | 265 | 展开覆盖译注之后、λ 段之前 | p.20 首件为“对 λ∈Q…” |
| 21 | 338 | “b basic ⟺ ℰ_b semi-stable”之后 | p.21 首件为 w/B^w 那句 |
| 22 | 402 | 定理 2.17 之后 | p.22 首件为推论 2.18 |
| 23 | 482 | 命题 2.25 之后 | p.23 首件为“固定 b∈G(L)…” |

八个锚全部落在环境之外（`\srcpage` 不得进 example/itemize/proof 内部）。

## 3. 疑点表

| # | 位置 | 原文 | 类型 | 判断与处理 | 依据 | 状态 |
|---|---|---|---|---|---|---|
| 1 | p.16 Hope 2.3 后 | There is no precise definition of this notion up to now. | 语气 | 作者自认概念未定；译文「迄今为止，这个概念还没有精确的定义」+ 同段「试图说服读者」，**保留不确定语气，未强化为定义** | 页面图 p.16 | 已解 |
| 2 | p.16 命题 2.4 证明 | To this **this** let u : ℰ₁|_{X_T}→ℰ₂|_{X_T} | 重复词 | 依 “to this end” 读，译作「为此，设 u：…」 | 页面图 p.16 | 已录 |
| 3 | p.16 命题 2.5 证明 | …this is 0 if d<0, **E is d = 0** and represented… | 笔误（is/if） | 应为 if；译作「若 d=0 它是 E」 | 页面图 p.16；p016.txt:56 | 已录 |
| 4 | p.17 | Then, taking the **the** generic fiber over S | 重复词 | 译作「于是，取 S 上的一般纤维」 | p017.txt | 已录 |
| 5 | p.17 | Note f : (X_S)_{pro-ét} → S_{pro-ét} | 疑为 Let | 译作「记 f：…」（按“记”处理，不另注） | 页面图 p.17 | 已录 |
| 6 | p.18 | This gives us **a a** “presentation” | 重复词 | 译作「一个“表示”」 | p018.txt | 已录 |
| 7 | p.18 命题 2.10 | whose **Galois group E^h** | 疑误（当为 E_h 或 Gal(E_h/E)） | 照原文译「其 Galois 群为 E^h」，加 `\yizhuw`（源码 182 行） | 页面图 p.18；p018.txt | 已注 |
| 8 | p.21 定理 2.17 | HN : B(G) → X_*(A)⁺_ℚ | 正体/斜体 | 放大核图确认 HN 为**正体**，用 `\HN`（`\DeclareMathOperator`） | 裁图 p021 裁 0.62–0.66 | 已改 |
| 9 | p.19 双射 | 箭头写 $G$-等晶体 → B(G)，而下行元素写 $[b]\mapsto[\mathcal F_b]$ | 方向不符 | 照原文排，加 `\yizhuw`（源码 217 行） | 页面图 p.19；p019.txt | 已注 |
| 10 | p.19 | X_E ⊗_E E_h = X_{E_h} | 记号 | 疑为 X_E ×_{Spec E} Spec E_h 的简写；照译未改 | 页面图 p.19 | 已录 |
| 11 | p.17–p.18 例 2.7 | B⁺_cris 公式上方残留无标签大括号；页界落在例 2.7 内部 | 排版 | 大括号为原文 PDF 排版残留，未复现；页界：把例 2.7 收在“给出。”，其后斜体段独立成段，`\srcpage{18}` 置于该段前（不在环境内） | 页面图 p.17、p.18 | 已解 |
| 12 | p.20 | We will admit this conjecture and do as if it **where** true | 笔误（where/were） | 译作「就当它为真」 | 页面图 p.20；p020.txt:59 | 已录 |
| 13 | p.21 | …an **G**-equivariant first Chern class | 笔误（a/an） | 译作「G-等变第一 Chern 类」 | 页面图 p.21；p021.txt:40 | 已录 |
| 14 | p.21 | 定义 x₁∼x₂ 时写 α_*x ≃ β_*y，与前文 x₁,x₂ 不一致 | 记号 | 照原文保留 x,y，加 `\yizhuw`（源码 368 行） | 页面图 p.21 | 已注 |
| 15 | p.22 | J̃_b→J_b(E) 与 π₀(J̃_b)=J_b(E) 两处 J_b(E) **无下划线**；而同页命题 2.20、命题 2.23 后半写作 J̄_b(E) | 记号不一致 | 三处各按原样排（有/无下划线），未统一 | 裁图 p022 三处 | 待裁 |
| 16 | p.23 | **This theorems** means… | 笔误 | 译作「这个定理的意思只是……」 | 页面图 p.23 | 已录 |
| 17 | p.22–p.23 | 2.2「叠的点」与 2.2.3「叠的点」同名 | 原文如此 | 照原文同题，不改 | 页面图 p.21、p.22 | 已录 |

## 4. 术语与新增术语建议

按 `glossary.tsv` 用工：Bun_G（保留记号，不译）、v-层、完满（完满空间/完满开球）、菱形、Kottwitz 集、Newton 点、Newton 多边形、Harder–Narasimhan 分层、HN 过滤、σ-中心化子、纯内形式、单值化、基本的、余特征、支配的、半稳定、斜率、G-丛、向量丛、内形式、约化群、伪一致化元、非分歧扩张、等晶体、展开覆盖、分类叠、代数空间、形式概形、仿射 Grassmann 簇（§2 未出现，留待 §3）。
不译保留：pro-étale、affinoid、torsor（加译注）、shtuka（本块未出现）、Quot 概形（Quot scheme，半译）。

建议补入 glossary 的新译（本块首次出现）：
`diamond stack` 菱形叠｜`diamond group` 菱形群｜`perfectoid open ball` 完满开球｜`pseudo-uniformizing element` 伪一致化元｜`isocrystal` 等晶体｜`slope morphism` 斜率态射｜`unramified extension` 非分歧扩域｜`groupoid` 群胚｜`fibered category` 纤维范畴｜`cokernel` 余核｜`locally free` 局部自由｜`ample` 丰沛｜`presentation` 表示｜`projective system` 投影系统｜`universal covering` 万有覆盖｜`formal group` 形式群｜`stacky quotient` 叠商（未出现，留待后文）。

## 5. 译注（9 条：6 条 A/B 级 + 3 条无据提示）

1. 命题 2.1 后：⊗-正合函子（A：原文 §2.1 p.16）
2. 命题 2.2 后：原文用 Hope（期望）而非 Conjecture，且承认“光滑”当时无定义（A：原文 p.16）
3. 命题 2.5 后：d 维完满开球 + 例 2.7 的 d=1 情形（A：原文 §2.1 p.16–18 及例 2.7）
4. 命题 2.10 内：Galois 群 E^h 存疑（`\yizhuw`，源码 182 行）
5. 2.2 开头：B(G) 即 Kottwitz 集（A：原文 §2.2 p.19；Kottwitz [18]）
6. 双射处：$[b]\mapsto[\mathcal F_b]$ 方向存疑（`\yizhuw`，源码 217 行）
7. 展开覆盖的含义（A：原文 §2.2.1 p.19）
8. 点集定义处：x₁,x₂ 与 x,y 不一致（`\yizhuw`，源码 368 行）
9. 公式 (8) 后：torsor 即主齐性空间（B：Stacks Project，“Torsors”）

## 6. 遗留与建议

1. **p.19「X_E ⊗_E E_h」**（疑点 10）若整书别处出现 X_E ×_{Spec E} Spec E_h 的写法，建议 Lead 统一；本块照原文未动。
2. **J_b(E) 的下划线**（疑点 15）：原文自身在三处不一致，本书若要统一，建议统一为带下划线（离散群 J_b(E) 嵌入 pro-étale 层 J̃_b 的语义更清楚），需 Lead 裁定全书写法。
3. **`\marginnote` 可见性**：`_check_c.pagemarks` 八条齐全，但 check 版 PDF 中部分锚（如 p.21、p.22）在页边可见性不稳定（与 s02/s05 同现象）；preamble 已注明以 pagemarks 为准，本文件只保证源码位置正确。
4. **公式编号**：原文 (7)(8) 用 `\tag` 硬排，不占 equation 计数器（与原文一致，后续公式若续编号须注意从 (9) 起）。
5. **引文编号**：[4][6][10][16][18][22] 以字面 [] 排入正文（与 s02、s05、s06 一致），未用 `\cite`；`s99-bibliography` 编号须与之对应。
6. **p.23 之后**：p.23 下半页起为 §3，本文件止于命题 2.27 后的两条 bullet，未越界。
