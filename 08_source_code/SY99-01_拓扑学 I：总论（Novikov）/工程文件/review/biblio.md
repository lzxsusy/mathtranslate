# review/biblio.md —— 参考文献核验（核验人：tr-wu）

核验对象：`src/chunks/biblio.tex`（原书 p.299–310，PDF p.306–317；467 行）
核验方式：逐页回页图抽核 p.299、p.302、p.310 三整页（覆盖卷首说明、IV 组开头、卷末 V.11–V.12），另核页标记与分组结构全量。
结论：**通过**（1 条建议，不涉正确性）。

## 一、结构核查

- 页标记 12 个（299–310）齐全、递增、独占一行；文件以 `% [原文 p.299]` 起、`% CHUNK biblio DONE` 收。
- 卷首：`\chapter*{参考文献}` + `\addcontentsline` + `\markboth`；说明段（"The items listed below have not been cited in the text…"）与脚注 1（Zbl./Jbuch. 说明）均已译出；星号说明（作者认为方法上最好的书文）保留 `\textsuperscript{*}`，条目内星号位置与原书一致。
- 分组：I（I.1–I.3）、II（II.1–II.4）、III（III.1–III.3）、IV（IV.1、IV.2、IV.4–IV.12）、V（V.1–V.12）。**IV.3 缺号是原书如此**：p.302 页图在 IV.2 纽结理论之后直接印 IV.4 同伦论，无 IV.3 标题；tex 已照录并在 `biblio.tex:171` 加 Tutor Note 说明。
- 条目体例：作者、题名、期刊、卷期年、页码、Zbl. 号一律保留英文原文（与 lead 要求一致），说明性文字译为中文；`\begin{itemize}` 手工条目（不用 `\bibitem`）；俄刊名（Usp. Mat. Nauk、Izv. Akad. Nauk、Tr. Mosk. Mat. O-va 等）照原书缩写不译。

## 二、逐页抽核记录

**p.299（PDF 306）**：标题 Bibliography^1；说明段与脚注 1 文意一致；I. 组标题「Popular Books and Articles on Geometry, Topology and Their Applications」→「几何、拓扑及其应用的普及读物与文章」；I.1 Aleksandrov–Efremovich 1936（ONTI, 94 pp.）、Hilbert–Cohn-Vossen 1932（Springer, 310 pp., Zbl. 5,112）；I.2 Boltyanskij–Efremovich 1982（Kvant No. 21, 149 pp.；德译 Braunschweig 1986；Zbl. 606.57001）、Chinn–Steenrod 1966（Random House, 115 pp., Zbl. 172,242）；I.3 *Volovik–Mineev 1980（Znanie, 63 pp.）、Mineev（Boltyanskij–Efremovich 书附录, 1982, 148–158, Zbl. 606.57001）、*Frank-Kamenetskij 1983（Kvant, 159 pp.）；II. 组标题；II.1 Lefschetz 1942（AMS Coll. Publ. 27, 389 pp., Zbl. 36,122）、*Seifert–Threlfall 1934（Teubner, 353 S., Zbl. 9,86）；II.2 Aleksandrov 1947（OGIZ-Gostekhizdat, 660 pp., Zbl. 37,97）。全部与 tex 条目逐字一致。

**p.302（PDF 309）**：Schwartz 1968（Gordon and Breach, 170 pp., Zbl. 187,450）、*Serre 1965（Benjamin, 252 pp., Zbl. 132,278）、Spivak 1965（Benjamin, 144 pp., Zbl. 141,54）、*Steenrod 1951（Princeton, 224 pp., Zbl. 54,71）；IV. 组标题「Surveys and Text-Books on Particular Aspects of Topology and Its Applications」；IV.1 Variational Calculus "in the Large"：Al'ber 1957、Dubrovin–Novikov–Fomenko 1984（Nauka 344 pp.；英译 Grad. Texts Math. 124, Springer 1990, 416 pp.）、Lyusternik–Shnirel'man 1947、Bott 1954（Ann. Math. 60, 375–382）、Klingenberg 1978（Grundlehren 230, 227 pp.）、*Milnor 1963（Ann. Math. Stud. 51, 153 pp.）；IV.2 Knot Theory：Crowell–Fox 1963、Bredon 1972、Conner–Floyd 1964；IV.4 Homotopy Theory. Cohomology Operations. Spectral Sequences：Boltyanskij 1966、*Dubrovin–Novikov–Fomenko 1984、Postnikov 1966、Fuks 1966×3、*Fuks–Fomenko–Gutenmakher 1969（MGU, 460 pp.；英译 Budapest 1986）、Adams 1969、Adams 1974。全部与 tex 一致（含卷期页码）。

**p.310（PDF 317）**：Kervaire 1960、Kervaire–Milnor 1963、Kirby–Siebenmann 1977、Madsen–Milgram 1979、Sullivan 1970、Wall 1970；V.11「Singularities of Smooth Functions and Maps」Arnol'd 1968/1974/1975/1978/1979、Mather 1971/1972、Thom 1971、Whitney 1948/1958；V.12「Foliations. Cohomology of Lie Algebras of Vector Fields」Bernshtejn–Rozenfel'd 1973、Novikov 1965、Fuks 1973、Fuks 1978、Godbillon 1974。与 tex 逐条一致。

## 三、原书笔误照排（已加批注，核验通过）

- p.310 Kervaire 1960 题名原书印 "A manifolds which does not admit any differentiable structure"（"A manifolds"）；tex 照录，`biblio.tex:464` 附 Tutor Note。
- p.310 Mather 条原书印卷期「29, No. 5 (167) (1972)」（年份疑误排为 167）；tex 照录并批注。
- 其余条目年份/页码未见异常。

## 四、建议（不涉正确性）

1. **脚注 1 的挂载位置**：原书脚注 1 挂在标题「Bibliography¹」上，tex 把它挂在说明段末句之后（脚注内容一致）。若追求版式一致可移到 `\chapter*` 标题处；不移也不影响语义。
2. 条目内的 `\textsuperscript{*}` 与原书星号位置一致，无需改动；但若排版上星号与作者之间空隙偏大，可在 preamble 统一调整（非本块问题）。

## 五、自检

- `python work/check_chunk.py src/chunks/biblio.tex`：页 299..310（12 页）、tag 0、陈述 0、Tutor Note 8、OK。
- 分组标题采用 `\subsection*`/`\subsubsection*`（不参与编号），与全书体例一致；未使用 `\bibitem` 与 `thebibliography`。
