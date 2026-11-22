# -*- coding: utf-8 -*-
"""生成 工程文件/reports/chNN.md（25 块施工记录）与 验收记录.md。"""
import io, os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports")
os.makedirs(OUT, exist_ok=True)

ROWS = [
 ("ch01", "§1 引言", "368–384", "无编号对象",
  "六段正文 + 致谢段；人名保留拉丁写法，肖梁、刘一峰在括号内附拉丁；术语用「层-函数字典」「去范畴化」「上同调与轮」。",
  "首块编译只有 5 页，确认版式与定理样式。"),
 ("ch02", "§2 节首 + §2.1 经典 Satake 同构", "385–481",
  "例 2.1.1、公式 (2.1.1)–(2.1.4)",
  "`S: GSat`、`S: affGrass`、`E:conv prod alge`、`cartan1`（原文在 equation* 内且从未被引用）、`cartan2`、`coweightGLn`、`E:twist conj`、`Sat isom`、`upper tr`；对偶群对照表用 tabular 原样。",
  "「单参数子群群」改为「单参数子群构成的群」；`\\section` 定名「$p$ 进群的几何 Satake」。"),
 ("ch03", "§2.1 格论例子、Witt 向量、完全 $k$-代数", "482–547",
  "注 2.1.4、例 2.1.5、2.1.6、引理 2.1.7 前的准备",
  "`R: norm Sat`、`minu Sch`、`coset vs lattice`、`quasiminuSch`、`Gr2`、`Gr2latt`、`wGr2latt`、`ramified Witt vector`、`discs`。",
  "「完全 $k$-代数」首次出现处加了术语说明；Witt 向量的函数性按原文直译。"),
 ("ch04", "§2.1 仿射 Grassmann 簇的定义", "548–604",
  "定理 2.1.7、注 2.1.8、例 2.1.9",
  "`E:affGrass def`、`affGrass`、`R:scholzediamond`、`E:jet and loop`、`E:rjet`、`E:gr as quotient`、`invbetaGLn`。",
  "定理 2.1.7 的证明梗概提到 Beauville–Laszlo、Faltings、Bhatt–Scholze，照译不补。"),
 ("ch05", "§2.1 Schubert 簇与 Satake 范畴", "607–676",
  "例 2.1.10–2.1.13、公式 (2.1.11)–(2.1.17)",
  "`mathring\\Gr_\\mu`、Bruhat 序、`I:conv` 扭积、`conv m0`、`E:chain mod`、`conv m`。",
  "极小余权与 $\\Gr_{\\omega_i}\\cong\\Gr(n-i,n)$ 的例按原文顺序排。"),
 ("ch06", "§2.1 卷积积与几何 Satake 定理", "677–742",
  "定理 2.1.15、注 2.1.16、引理 2.1.14",
  "`E-conv Sch`、`conv m2`、`E:dim est`、`\\tilde\\boxtimes`、`Lus conv`、Künneth、`intro:geomSat`、`R: birth of the dual group`。",
  "等特征与混合特征的证明差异是本块最需要小心的段落，逐句核对了 Lusztig–Vogan 公式的写法。"),
 ("ch07", "§2.2 动机 Satake（前）", "743–810",
  "引理 2.2.1、注 2.2.2",
  "`SS: MotSat`、`\\on{Mot}^*_k`、`\\Sat_G^0`、`L:faithful realization` 及交换方块。",
  "交换方块原为 amscd 五列，溢出 98pt，改 tikz-cd 2×2，并从 footnotesize 降回 scriptsize 才 0 Overfull。"),
 ("ch08", "§2.2 动机 Satake（后）", "810–944",
  "引理 2.2.3、例 2.2.5、注 2.2.4",
  "幺半结构、$\\Sat^T_G$ 与 $\\hat G^T$、Koszul 符号、`R:Tate twist`、`intersection by geom Sat`。",
  "补了两条勘误（`h(\\Gr_\\mmu)(n)` 应为 `(m)`；`\\La_0=\\mO_2` 应为 `\\mO^2`）。"),
 ("ch09", "§3 节首 + §3.1 范畴迹的定义", "945–1009",
  "命题 3.1.1、注 3.1.2–3.1.3",
  "`E:HH` bar 复形、`E:cond trace`、`E:cond trace cor`、`\\on{Func}^{\\tr_\\sigma}`、`L:trace cat`。",
  "加了「范畴迹」译名注（不取「范畴化迹」）。"),
 ("ch10", "§3.1 命题 3.1.1 的证明", "1010–1131",
  "注 3.1.4、例 3.1.5",
  "`E:trace hom`、$S_{u,v}$、`E:frac`、`E: comp in tr`、`E: trace of rep`。",
  "`E: comp in tr` 小图用 `@C=0.8em@R=0.9em` 消掉 34pt Overfull。"),
 ("ch11", "§3.1 $S_V$ 与 $K$-环", "1132–1184",
  "命题 3.1.7、注 3.1.6、3.1.8–3.1.10",
  "`E:abs S`、`E: K to End`、`E: K to End2`、`E: K to End3`、`L: K iso End`、`R: cat center`。",
  "原文 1185–1190 的 `\\quash` 段（∞-范畴版）不译，记录在 `资料卡/04`。"),
 ("ch12", "§3.2 节首与两例", "1192–1305",
  "例 3.2.1–3.2.3、注 3.2.4、引理 3.2.5",
  "`\\Ad_\\sigma`、$X=\\frac{G}{\\Ad_\\sigma K}$、$C=X\\times_YX$、`Ex:springer`、`Ex:DL`、`E:Hk for unit`、`E:endo for unit`、`E:endo for reg`、`L: decom of C`。",
  "Deligne–Lusztig 簇与 $\\End(\\widetilde{\\delta_e})\\cong H_W^{\\on{op}}$ 的对应按原文逐步核。"),
 ("ch13", "§3.2 $S$-算子", "1310–1419",
  "构造 3.2.5、推论 3.2.6",
  "`Con: S`、`Lus conv2`、`E: creation corr`、`E: ann corr`、`on{sw}(\\id\\times\\sigma)`、`E: Frob corr`、$S_{u,v}$、`C:trace str on tilde`。",
  "$S_{u,v}$ 那一行过长，改 `aligned` 拆两行；极限圆变换的译名沿用 SY02-17。"),
 ("ch14", "§3.2 有限版 $S=T$", "1420–1494",
  "注 3.2.8、命题 3.2.9",
  "$\\mathbb H_W$、$v=1$ 与 $v=\\sqrt q$ 特化、$f_\\mF$、$S'_\\mF$、`P:S=T finite`、`E: cal coh corr to local` 的 (A)–(D)。",
  "四个交换图逐行核对 $\\sw$ 与 $\\px\\sigma$ 的位置；Braverman–Varshavsky 迹公式只引不证。"),
 ("ch15", "§4 节首 + §4.1 局部 Shtuka", "1495–1600",
  "例 4.1.1–4.1.2、注 4.1.3–4.1.4",
  "`S: cattrSat`、$\\on{D}^\\Hk(X)$、`R:pre of Sht`、`no singularity`、`loc Sht and pdiv`、`hpf`、`E;Hk Shtuka`、`R:fiber of hloc`。",
  "Shtuka 不译，加术语注；与 Fargues–Scholze 的对比照译。"),
 ("ch16", "§4.1 有限维逼近", "1601–1740",
  "例 4.1.9、注 4.1.10、若干公式",
  "$\\mmu$-大、`torsor1`/`torsor2`、`E:ex and q compatibility`、`E:mS restricted as a Cartesian product`、`trunc`、`E:Sht-Zip`。",
  "$F$-zip 的四元组 $(M,C^\\bullet M,D_\\bullet M,\\phi_0,\\phi_1)$ 逐符号抄录。"),
 ("ch17", "§4.1 命题 + §4.2 开头", "1741–1830",
  "命题 4.1.11、注 4.1.12",
  "`deompf1`、`E:cycle construction diagram full`、`E:projection localization truncated`、`R: grp theoretical Sht`、`E:definition of P(Sloc)`。",
  "`E:projection localization truncated` 原 `@C=20pt` 溢出 70pt，降为 `\\footnotesize` + `@C=5pt`。"),
 ("ch18", "§4.2 对应范畴", "1830–1931",
  "注 4.2.2–4.2.3、命题 4.2.4",
  "反常 $t$-结构、`\\Phi^{\\loc(m,n)}`、`E:functor P(Hk) to P(S)`、`R: more object`、`E: hom space of PcorrSht`、`P: endo of unit`。",
  "`E: hom space` 前的 `align*` 过长，包 `\\footnotesize` 消 32.9pt Overfull。"),
 ("ch19", "§4.3 + §5.1 前段", "1932–2044",
  "定理 4.3.1、注 4.3.2–4.3.3、命题 5.1.1",
  "`T: trace of geom Sat`、$S(\\mO)=\\widetilde{\\delta_e}$、$\\mathbf J$、`R:affine springer`、`S:app to Sh`、Kisin–Vasiu 整模型、`smoothness`。",
  "初版漏了 §4.3 的标题与开头两段（编号因此错 3 处），已补；1936 行的 $G$ 按勘误作 $\\hat G$ 并加译注。"),
 ("ch20", "§5.1 定理与猜想", "2045–2120",
  "定理 5.1.3、注 5.1.4、定理 5.1.5、猜想 5.1.6、注 5.1.7",
  "`T: corr. Shimura`、`E: pHecke corr`、`E: exotic p`、`introT: spectral action`、`introconj: S=T`、`R: coh of Shimura`。",
  "猜想表述里补回原文的 `\\eqref{Sat isom}`（初版漏）；一条 Underfull 属文献排版，无害。"),
 ("ch21", "§5.2 Tate 轮", "2121–2210",
  "定理 5.2.1、注 5.2.2、例 5.2.3",
  "$\\Lambda^\\Tate_p$、$V^\\Tate$、${\\rm H}^{\\rm BM}_{2d}$、`on{cl}`、Newton 分层、`T:main theorem`、`GU(1,2r)`、`E:Hecke operator in Tpj`。",
  "Tate 轮译名加注并注明沿用 SY02-17；奇酉群的 $v$-二项式系数按原文式子抄。"),
 ("ch22", "§6 节首 + §6.1 前段", "2211–2380",
  "定义 6.1.2、引理 6.1.3、引理 6.1.5、定义 6.1.6、例 6.1.7",
  "`Sec:cohomological correspondence`、`E: VD counit`、`E: VD unit`、`D: basechangeable`、`L: criterion basechangeable`、`L:proper base change`、`AD:correspondences`、`Ex:examples of correspondences`。",
  "`\\ev_\\mF`/`\\coev_\\mF` 的 `$$...$$` 改 `aligned` 消 5.06pt Overfull；「可基变换」加译名注。"),
 ("ch23", "§6.1 前推与拉回", "2386–2478",
  "引理 6.1.9、引理 6.1.11",
  "`AL:pushforward compatible with composition`、三种拉回（`ASS:smooth pullback correspondence` 等，标签里的空格逐字保留）、`AL:pullback compatible with composition`。",
  "标签名里的空格原样照抄，否则 label 对账会报 extra。"),
 ("ch24", "§6.2 对应范畴", "2479–2554",
  "引理 6.2.1、注 6.2.2",
  "`SS: cat of corr`、`E: diagram`、`E:HomDC`、$\\on{D}^C(X)$、$\\on{P}^C(X)$、`L: fully faithful`、`R: DC enh`。",
  "`E: diagram` 的 5×3 xymatrix 用 `@C=` 调窄；`\\substack` 的余极限图照原文排版。"),
 ("ch25", "参考文献", "2555–2671", "48 条 `\\bibitem`",
  "`thebibliography{9999}`，显示标签与 key 原样保留（17 条不同，见 `资料卡/04`），`{\\it}` 改 `\\emph`，`\\url` 保留。",
  "书目错字（`101?228`、`Alegbra`、`alg\\`ebres`、`Hautes tudes`）照抄并登记 E19–E22。"),
]

for ch, sec, lines, objs, pts, notes in ROWS:
    p = os.path.join(OUT, ch + ".md")
    body = (
        "# %s · %s\n\n" % (ch, sec) +
        "| 项 | 内容 |\n| --- | --- |\n" % () +
        "| 原文行 | %s |\n" % lines +
        "| 编号对象 | %s |\n" % objs +
        "| 目标文件 | `源码/chunks/%s.tex` |\n" % ch +
        "| 状态 | 完成 |\n\n" % () +
        "## 覆盖内容\n\n%s\n\n" % pts +
        "## 施工备注\n\n%s\n" % notes
    )
    io.open(p, "w", encoding="utf-8").write(body)

acc = """# 验收记录 · SY02-20

验收日期：2026-11-22。判据以 `04_playbook/01_数学文献翻译纪律.md` 的交付清单为准。

| 项 | 判据 | 实测 | 结论 |
| --- | --- | --- | --- |
| 编译 | 0 error | `main.log` 无 `!` 开头 | 通过 |
| 版面 | 0 Overfull | `grep -c "Overfull \\\\hbox"` = 0 | 通过 |
| 缺字 | 0 Missing character | 同上 = 0 | 通过 |
| 引用 | 0 未定义 | `build.sh` 统计 = 0 | 通过 |
| 页数 | — | 59 页（原文 50 页） | 通过 |
| 编号对账 | mismatch 0 | `sim_numbering.py`：orig 140 / mine 140 | 通过 |
| 标签对账 | 差集可解释 | 原文 151 / 译文 150，仅差 `\\quash` 段 | 通过 |
| 引用键对账 | 不一致小节 0 | `refs_check.py` | 通过 |
| 文献 | 48 条全在 | `ch25.tex` 48 个 `\\bibitem` | 通过 |
| 译注 | 均带来源或推断标注 | 9 条 `\\zy`，逐条检查 | 通过 |
| 术语 | 冻结且一致 | `glossary.tsv` 179 条 | 通过 |
| 疑点 | 未解 0 | `疑点清单.tsv` 32 条全「已解」 | 通过 |
| 勘误 | 全登记不改原文 | `资料卡/04` E01–E22 | 通过 |
| 七件套 | 齐全 | 源码、成品 PDF、投稿信息、资料卡五件、精选片段、工程文件、编译说明 | 通过 |
"""
io.open(os.path.join(OUT, "验收记录.md"), "w", encoding="utf-8").write(acc)
print("reports:", len(ROWS) + 1)
