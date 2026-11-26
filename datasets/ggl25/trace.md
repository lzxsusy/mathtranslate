# trace · ggl25（Teschner, arXiv:1405.0359）

记录本篇实际做过的判断。每条四栏：判断点 / 依据 / 结论与理由 / 事后确认。标「弯路」的是真正写错—发现—改正的过程，不是预设的示例。

| # | 判断点 | 依据 | 结论与理由 | 事后确认 |
|---|---|---|---|---|
| 1 | 式号体系：§4 首式为什么是 (4.19) 而不是 (4.1)？ | 通读 p011–p022 的式号：§2 用 (2.1)–(2.13)、§3 用 (3.1)–(3.18)，§4 起为 (4.19)、(5.33)、(6.38)、(7.43) | 判定「第一位是节号、第二位是全文累计计数器，§4 起不再按节重置」。所有 locator 一律照抄印刷式号，不自行换算 | 用 `grep -o "(4\.[0-9]*)"` 逐页核对 p011–p016，式号连续无缺；audit_locators 全过，说明照抄策略正确 |
| 2 | **（弯路）** 式 (3.9)（$C_{1,1}$ 的二次关系）相位 $e^{\pi ib^2/2}$ 是否为笔误？ | 我先按 (3.7) 的展开套路推：若相位是 $e^{\pi ib^2}$，$b\to0$ 应给 $\{L_s,L_t\}=2L_u-L_sL_t$；用 $b^2/2$ 展开只给 $\tfrac12(2L_u-L_sL_t)$，差因子 2 | 初判「疑为笔误、拟记 errata」；随后下载 Teschner–Vartanov arXiv:1302.3778，其 (6.5) 与本篇 (3.9) **逐字相同**（含 $b^2/2$），故改判为约定问题，**不写 errata**，只在卡片 pitfalls 说明 | 回看 BRIEF §9.2：只有一处冲突才记 low，此处与独立出处一致 ⇒ 不该记。errata.tsv 最终无此条，正确 |
| 3 | **（弯路）** (3.15) 的 $\Delta_l=(1+b^2)/(4b)+(l/4\pi b)^2$ 常数项是否应为 $Q^2/4$？ | 我按 $\Delta(\alpha)=\alpha(Q-\alpha)$ 在 $l=0$ 处应得 $Q^2/4$，而 $(1+b^2)/(4b)=Q/4$，疑为笔误 | 核 TV13 (6.15b)：$\Delta(l):=(1+b^2)/(4b)+l^2/(4\pi b)^2$ 全同 ⇒ 原文正确；差值 $\Delta_l-\Delta(\alpha)=-Q(Q-1)/4$ 是常数，因 B 算符只定义到相位而不矛盾。改为卡片 pitfall | 该条写进 `moore-seiberg-groupoid` 的 pitfalls 与 notes §5；若当时直接改，会在卡片里写出与原文不符的公式 |
| 4 | 式 (5.34) 的 $(L_{-1}^2+b^{\pm2}L_{-2})$ 与 $\alpha=-b^{\pm1}/2$ 是否配对错？ | 直接算 level-2 零向量：$L_1N=0\Rightarrow(4\Delta+2)+3\kappa=0\Rightarrow\kappa=-(4\Delta+2)/3$；代 $\Delta(-b/2)=-1/2-3b^2/4$ 得 $\kappa=b^2$，代 $\Delta(-1/(2b))$ 得 $\kappa=1/b^2$ | $b^{\pm2}\leftrightarrow\alpha=-b^{\pm1}/2$ 完全配对，**不是笔误**；这个计算还顺带给出旁证（Ising 的 $c=1/2,h=1/16$ 给 $\kappa=-3/4$） | 写成 `verlinde-line-operators` 里唯一一条 `complete` 的 theorem，steps 逐条可查 |
| 5 | 式 (3.4) 的求和范围 $\nu\in\mathbb{Z}^{3g-3+2n}$ 与「with components $\nu_e$（$e$ 跑遍三角剖分边）」是否冲突？ | 数边：理想三角剖分有 $6g-6+3n$ 条内部边（Euler 计数），而裤子分解只有 $3g-3+n$ 条曲线；FG1 §1.2 的 $X^{P+}_{GL_2,S}=\mathbb{R}^{6g-6+3n}$ 也指向边数 | 判为原文笔误候选，但只有 FG1 这一条硬出处 + TV13 §6.2 的间接支持 ⇒ 记 **medium**（不是 high：本篇内部只有「$3g-3+2n$ vs 边」这一处不自洽，够不上两处独立冲突 + 内部矛盾的 high 标准） | errata E1；卡片里一律不写这个范围（`quantum-teichmuller-algebra` 只在 pitfalls 提到 E1） |
| 6 | p011 的 $c=1+6Q^2$ 先用 $Q$、而 $Q=b+b^{-1}$ 到 p016 (5.33) 才定义，是否记笔误？ | AGT 0906.3219 与 TV13 都是「$c=1+6Q^2$ 与 $Q=b+1/b$ 并列给出」；本篇只是顺序倒置 | 记 **low**（记号顺序问题，非数值错误），写进 errata E2；`liouville-conformal-blocks` 加 `corrections:[E2]` 并在 definition/pitfalls 补注 | lint 对 corrections.id 与 errata 的交叉校验通过；E2 的影响卡片字段填了该卡 id |
| 7 | **（弯路）** 外部文献的页码能不能进 `sources.pages`？ | 先按「如实标注」把 TV13 的 (6.3) 写成 `pages: [39,39]`，lint 立刻报 pages 超出 `--max-pages 25` | 改为：外部 PDF 页码一律不进 sources，交叉核对写进卡片 `provenance_note` 与 notes.md（并给出 PDF 页号供回查） | 重跑 lint 通过；`verify_pages` 只核 A 类 quote，说明该策略与工具设计一致 |
| 8 | **（弯路）** 推导卡里 C 类步骤的 locator 怎么写？ | 写成 `C §6.3（Teschner–Vartanov 1302.3778，式 (6.3) 与经典极限说明）`，lint 报「locator 格式错」（ANCHOR_RE 要求 `^[A-D] p\.\d+`） | 第一次想补成 `C p.39 …`，但 audit_locators 会把 p.39 当本篇页号去 `pages[39]` 查、越界；最终把该步改成 A 类内部一致性检查（三次关系给 (2.9)），TV13 的对照移入 provenance_note | 四道检查同时通过；教训：locator 是**本篇页码**语义，外部文献只能进 note |
| 9 | **（弯路）** anchor `A p.10 eq (3.12)` 与 `A p.6 eq (2.13)` 页码 | 两处 anchor/locator 都是凭「式子在正文出现的位置」写的；audit_locators 报 (3.12) 实际在 p9、(2.13) 在 p7 | 原文这一页是页间断式：(3.12) 的编号落在 p009 末行、(2.13) 在 p007；改 anchor 为 `A p.10 §3.3`（不带式号，因 quote 确在 p10）、locator 改 `A p.7 eq (2.13)` | 重跑 audit 输出 `OK: all locators with eq numbers match their pages`；教训：跨页公式的「式号页」与「引文页」可以不同 |
| 10 | 8 张概念卡怎么切？是否把剪切坐标与簇变换拆开、把 Fricke 与 Poisson 拆开？ | 读者要能迁移：剪切坐标与簇变换是同一套坐标的两面（(2.3)+(2.5) 共用一个定义域），Fricke 关系 (2.9)–(2.11) 与 Poisson (2.12)–(2.13) 共用同一个多项式 $P_e$ | 合并为 `shear-coordinates` 与 `trace-function-algebra`；把省下的卡位给 `verlinde-line-operators`（track D）与 `quantum-teichmuller-liouville-dictionary`（track O）——后者是全篇结论，不能没有 | 最终 8 卡覆盖 §2/§3/§4/§5/§6，无一张是为凑数拆出来的；track 分布 C×5、D×1、O×1、C×1 |
| 11 | 推导卡 D1 的第三、四步（迹恒等式展开）能不能标 `complete`？ | 原文把 (2.13) 的推导推给 [NRS]，正文没有展开；我只能确认 $\partial P_e/\partial L_u$ 的显式形式与 (3.7) 经典极限一致 | 标 `sketch` 并写两条 gaps（迹恒等式未展开、$\nu_\gamma$ 符号未追踪）；「complete」只留给真正逐项算过的 (5.34) 配对 | 复读卡片时确认：三张推导卡里只有 D1/D2 的部分步骤是自算，(5.34) 那条才是 complete |
| 12 | **（弯路）** §2.3.1 的标题是 "Skein algebra" 还是 "skeleton algebra"？ | 初读 p004 时把 "Skein" 记成了 "skeleton"（笔记里写成「骨架代数」） | 回看原文 p004 的节标题与 p009「quantum analogs of the skein relations」⇒ 是 **skein**；中文定名改为「skein 代数/skein 关系」，并在 notes 里注明本篇不用 Fricke 之名 | `terms.tsv` 已改；若沿用「骨架代数」，术语表会与原文对不上 |
| 13 | 主结论该给 `sketch` 还是 `gap`？ | 原文 p016 把主结论写成本篇的定理，但证明推给 [TV13]（F 核 vs 6j、B 相位 vs R-矩阵）与 [HJS]（S-move⇒模核） | 给 `sketch` + `gap_note`（说明我没有复算 F 核与 6j 的相等）；`gap` 只留给 (4.31)⇒(4.32) 那条完全依赖 [HJS] 的论证 | 复核 lint 对 sketch/gap 的 gap_note 要求：两者都必须有，已都有 |
| 14 | 撞名怎么处理？ | `term_index.py check` 先报 alias「平坦联络模空间」撞 `csw/concept/flat-connection-moduli`，改后又报「character variety」撞同一张旧卡 | 按「保留旧卡术语、本卡加限定词」：改成「平坦 PSL(2,C)-联络模空间」与「character variety M^C_char(C)」 | 重跑 `check` 输出「撞名 0 处」；没有删卡、没有改旧卡 |

## 弯路小结（真实写错—发现—改正）

1. **(3.9) 的半相位**：先判笔误，核 TV13 (6.5) 后撤回。
2. **$\Delta_l$ 的常数项**：先按 $\alpha(Q-\alpha)$ 判笔误，核 TV13 (6.15b) 后撤回，改为 pitfall。
3. **外部页码进 sources**：lint 报越界，改为写进 provenance_note。
4. **C 类 locator 格式**：lint + audit 双重约束下改写，并把 TV13 对照移到 note。
5. **anchor 页码**：两处跨页公式的页码写错，由 audit 抓出后改正。
6. **Skein vs skeleton**：术语读错，回原文改正。
