# 参考文献 校订日志（`源码/refs.tex`，原书 p.381–386）

## 1. 已核对范围

**p.381–p.386 全部 6 页、89 条，逐条核对完毕**（对照 `工程文件/work/pages/p381.png`–`p386.png`，文本层 `工程文件/work/en/p381.txt`–`p386.txt` 仅作定位辅助）。

| 页 | 条目 | 核对内容 |
|---|---|---|
| p.381 | [Ak]–[BR]（16 条） | 键名、作者、标题、刊名、卷、年、页码；`[Ak]` 人名后漏空格、`[BR]` 末尾无句号等底本特征已确认 |
| p.382 | [Bourb59]–[Fal94]（13 条） | 法文标题重音（Algèbre / algèbres / géométrie / Catégories tannakiennes / déterminant / dualité）、`chap. IV–VI` 用 en dash |
| p.383 | [F84]–[Gi97]（16 条） | 俄文原刊名（Uspekhi Mat. Nauk / Doklady Akademii Nauk SSSR）、`Adv. Ser. in Math. Phys.`、`SGA 4` |
| p.384 | [GK]–[KR]（11 条） | `Soviet Math. Doklady`、`$\mathfrak{p}$-adic`（底本确为 Fraktur p）、`Jantzen`、`To appear` |
| p.385 | [KT95]–[Pa76]（11 条） | `Kazhdan-Lusztig`、`Kostant` 三条、`vol 176`（底本无点）、`C-categories` 斜体 C |
| p.386 | [Phys]–[Yet]（13 条） | `Fehér`、`O'Raifertaigh`（底本误拼）、`algbras`（底本误拼）、`SGA 4½`、`Topology '90` |

另做两轮**机械比对**（脚本 `C:\Users\admin\Downloads\_refalnum.py`、`_refpunct.py`）：剥去 `\emph{}`/`$…$`/`\mathfrak{g}`→g/`--`→`-` 后，与文本层逐条比字母数字串，**89/89 完全一致**（仅 [T] 被底本并入 [Ve]、[Yet] 后接作者单位块两处需截断）；再比标点串，唯一实质差异为 [KS] 的 `vol 176`（见 §3）。→ 条目文字与底本逐字符相符，未发现抄录性错漏。

`p.386` 末尾的作者单位块（MASSACHUSETTS INSTITUTE OF TECHNOLOGY … / Current address … / E-mail address: sasha@mit.edu）不属于文献条目，未收入 `refs.tex`。

## 2. 问题清单

| 位置 | 原书（底本） | 原译 | 改为 | 理由 |
|---|---|---|---|---|
| refs.tex:23 | p.381–386 页眉为 “HITCHIN'S INTEGRABLE SYSTEM / 页码” | 参考文献 5 页页眉残留「10.1. Delta 函数」 | 加 `\markboth{参考文献}{参考文献}` | 版式（P2）。`\bdsec` 自带 `\markboth`，而 `\bdsection` 走 `\section*` 不改 marks；`chapters/fanli.tex` 也是显式 `\markboth`，照此例补 |
| refs.tex:31、131 | 底本排法式等距，句点后无附加空档 | LaTeX 默认在句末句点后加宽空档（`vectorielle.  In:`、`editors).  Adv.` 明显拉宽） | 用 `\frenchspacing … \nonfrenchspacing` 包住 description 环境 | 版式：书目为纯西文，句末附加空档与底本不符 |
| refs.tex:61 | `Mathematical Research Letters`（刊名） | 未加 `\emph` | 补 `\emph{…}` | 体例：89 条中唯一漏包刊名者，与全书「刊名/书名一律 `\emph`」不一致 |
| refs.tex:42 / 58 / 84 / 88 / 94 / 114 / 117 / 125 | 底本自身缺陷：[BD] 只作 “To appear”；[D71] “géometrie”；[IM] “decompositiopns”；[Kac97] “Amer.Math.Society”；[Kap97] “local systems Preprint”（漏句点）；[Phys] “O'Raifertaigh”；[R] “algbras” + “Trans.Amer.Math.Soc.”；[We83] “Expositiones Matematicae” | 无说明，读者会误以为译文排错 | 各加一行 `% [Tutor Note: …]`，正文**不改字** | 按校对须知「原书笔误照录」，加注备查 |

> 规范化与照录的分界（已写入 refs.tex 文件头注释）：**纯排印层的缺空格**（`Akman.A`、`I.Mirković`、`K.Vilonen`、`J.L. Verdier`、`Trans.Amer.Math.Soc.`、`Amer.Math.Society`、`vol 176`）按通行写法补齐分隔；**影响词句/书目信息层的缺陷**（误拼词、漏句点、`To appear`、缺卷期页码、键名年份与出版年不符）一律照录。

## 3. 未改动但存疑（需主译裁定）

1. **底本对刊名/书名的斜体极不统一，本译文未逐条追摹。** 例：`Duke Math. Jour.` 在 [Hit87] 斜体、在 [La87][La88] 正体；`Annals of Math.` 在 [Ar] 斜体、在 [Ko61] 正体；`Publications Mathématiques IHES`（[IM][Gr64][Gr67]）、`Inventiones Math.`（[Ha88][Ko78][RG]）、`Amer.Math.Society`、`Collected papers by J.-P. Serre`（[Se]）、`Champs Algébriques`（[LMB93]）底本均**正体**；而 `[BD]` `Chiral algebras`、`[DSim]` 等底本又是斜体。现统一按「刊名/书名一律 `\emph`」处理——请确认接受此归一，或改为逐条追摹底本（则需再动约 20 条）。
2. **`-` 与 `--` 未强行统一。** [Lu83] `Astérisque, vol. 101-102 (1983), 208-229`、[Se] `vol. I, 531-543` 底本用的是**连字符**，与其余条目的 en dash 不一致；现照录底本，未改。若要求全书统一为 `--`，请裁定。
3. **`D`-模的花体写法。** [Sa89][Sa91] 底本印作花体 𝒟（`𝒟-modules`），[Kas] 同位置却是斜体 `D`；译文两条均用 `$D$`。正文层记号多用 `$\mathcal{D}_X$`（ch02/ch05 共 198 处，`$D$` 59 处），是否把这三条书目改为 `$\mathcal{D}$`，请裁定。
4. **[Kap97] 的漏句点未代补。** 底本作 `… local systems Preprint alg-geom/9710027.`（`systems` 后无句点），译文照录。若认为这属于排印层、应与上条空格同等对待，可补为 `systems. Preprint`。
5. **键名年份与出版年不符，键名未动。** [LMB93] 正文作 1992、[Ma96] 正文作 `vol. 27 (1995)`；键名按底本保留（正文按这些键引用）。
6. **底本末尾无句号的条目**：[BR] 以 `…, 103--138)` 收、[F84] 以 `…, 195--196)` 收，底本即无句点，照录。
7. **[W] 的 `W-symmetry`**：底本仅 `W` 为斜体、`-symmetry` 正体；译文整条 `\emph{$W$-symmetry}` 全斜。属第 1 条的同一问题。

## 4. 术语与记号一致性

- 键名 89 个与正文 `[键]` 引用一一对应，**未改动任何一个键名**（含 `[Ma96]`/`[LMB93]` 这类年份与出版年不符者）。
- 数学记号与正文一致：`$\mathfrak{g}$`（[BB81][BL]）、`$(\mathfrak{g},K)$`（[BL]）、`$\mathfrak{p}$-adic`（[IM]，底本确为 Fraktur p）、`$BG$`（[Kap97]）、`$C$-categories`（[Pa]）、`$W$-algebra`（[Phys]、[W]）、`$G$-bundles`、`$K$-theory`。
- 刊名缩写一律照底本：`J. of Math.`（[Ba63][J]）、`Jour. of Algebra`（[J]）、`Annals of Math.`、`Inventiones Math.`、`Comptes Rendus Acad. Sci. Paris`、`Uspekhi Mat. Nauk`、`Soviet Math. Doklady` 等，未按 ISO 缩写改写。
- 法/德/俄语标题、丛书名一律照原文（`Algèbre`、`Groupes et algèbres de Lie`、`Éléments de géométrie algébrique`、`Catégories cofibrées additives et complexe cotangent relatif`、`Champs Algébriques`、`Critères de platitude et de projectivité`、`Doklady Akademii Nauk SSSR`），未作任何翻译。
- 本文件不涉及 oper/gerbe/torsor 等术语的译法。

## 5. 自检

- **编译**：`C:\Users\admin\Downloads\_rev_refs\` 内 `xelatex -interaction=nonstopmode main.tex` 两遍，退出码 0，`grep -c "^!" main.log` = **0**，`Output written on main.pdf (194 pages)`。
- **Overfull**：`Overfull \hbox` 2 处（`ch07` 第 649–650 行 9.02pt、`ch08` 第 43–47 行 3.20pt）、`Overfull \vbox` 3 处（页高微溢 0.44/1.55/0.50pt，全书普遍现象），**本文件无任何 Overfull**；缺字 0。
- **结构**：`\item[{[键]}]` 89 个、键名 89 个且互不重复；`$` 总数 42（偶数，配对正常）；`\begin`/`\end` 各 1；花括号收支平衡；`` `` `` 与 `''` 各 2（引号成对）。
- **改动行数**：原 106 行 → 现 131 行（新增 25 行、修改 1 行），全部在 `源码/refs.tex` 内；`main.tex`、`chapters/*`、`units/*` 未动。
- 其中影响输出的实质改动 3 处：页眉 `\markboth`、`\frenchspacing` 包夹、[DSim] 补 `\emph`；其余为文件头说明 10 行、Tutor Note 8 行、代码旁注 5 行。
- **条目文字改动：1 条（[DSim]，仅加 `\emph`）；其余 88 条正文一字未改。**
