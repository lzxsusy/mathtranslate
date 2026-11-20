# SY05-28 工程说明（README）

## 一、这是什么

Denis Auroux 两份公开讲义的中译注本：

- **底本一**：《Mirrors of curves and their Fukaya categories》，2020 年 1 月 27–29 日迈阿密 Conference on Homological Mirror Symmetry 三场报告的手写笔记，17 页，无文字层 → 正文第一至三讲。
- **底本二**：《An invitation to homological mirror symmetry》，2019 年 9 月 6 日 IMSA 成立大会报告幻灯片，14 页，beamer → 附录 A。

成品：`成品/SY05-28_曲线的镜像及其Fukaya范畴_中译注本.pdf`，32 页。

## 二、目录结构

```
源码/
  main.tex            主文件（preamble → ch0_front → 三讲 → 参考文献 → 附录 A/B）
  preamble.tex        版式与宏（ctexart + fontset=windows + amsthm + TikZ）
  ch0_front.tex       封面、译者说明（翻译原则/符号约定/批注说明）、目录
  ch1_talk1.tex       第一讲：曲线的镜像与 wrapped Fukaya 范畴
  ch2_talk2.tex       第二讲：函子、Knörrer 周期性与热带拉格朗日
  ch3_talk3.tex       第三讲：三价构形上的拉格朗日 Floer 理论
  app_invitation.tex  附录 A：同调镜像对称导引（按幻灯片逐页译）
  app_terms.tex       附录 B：术语对照表（longtable，90 行）
  refs.tex            参考文献（12 条）
  original/           底本 PDF 与 300 dpi 页面 PNG（只读；按 L4 规则不入库，
                     本地保留以备复核，见 `源码/.gitignore`）
工程文件/
  BRIEF.md            任务书
  README.md           本文件
  reports/01_通读笔记.md
  reports/02_疑点清单.tsv（17 条，已解 12 / 待核 5 / 未解 0）
  reports/03_术语表.md（冻结 v1.0）
  reports/04_交付核对.md
  精选片段.md          4 段中英对照与判定链
  work/               读图阶段的逐页速记（transcript_t1/t2/t3/t3b.md）
  tools/              读图辅助：crop.py（相对坐标裁剪）、lines.py（行带检测）
成品/
  SY05-28_曲线的镜像及其Fukaya范畴_中译注本.pdf
投稿信息.md
```

## 三、编译方法

MiKTeX 在 `C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\`：

```bash
export PATH="C:/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64:$PATH"
cd 源码
xelatex -interaction=nonstopmode main.tex   # 三遍，目录与交叉引用才稳定
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

单章自检可临时建一个只 `\input{preamble}` + 单章的 `_test.tex`（本次已用过，交付时删除）。

## 四、实测记录

最后一轮编译（2026-11-20，XeLaTeX，MiKTeX）：

| 项目 | 结果 |
|---|---|
| 编译遍数 / 退出码 | 3 遍，均 exit=0 |
| 页数 | 32 |
| `!` 错误 | 0 |
| Overfull \hbox | 0 |
| Overfull \vbox | 0 |
| Undefined control sequence | 0 |
| undefined reference / citation | 0 |
| Missing character | 0 |
| hyperref 书签警告 | 0 |
| Underfull \hbox | 5（纯排版松紧，不影响验收线） |
| 目录条目 | 46 行 .toc，正文显示到 subsection 层（`tocdepth=2`） |
| 图 | 17 幅，全为 Ti*k*Z 代码 |
| 批注 | 14 条（另有 1 条为封面上的条数声明） |
| 参考文献 | 12 条 |
| 术语表 | 90 行 |

## 五、翻译与校订说明

1. **手写页逐页读图**。全部 17 页手写笔记按 300 dpi PNG 逐页读，先用 `read_image` 看整页，再对难辨处用 `tools/crop.py` 按相对坐标裁剪放大（最多放大到 5 倍），必要时用 `tools/lines.py` 的行投影定位。幻灯片用 pymupdf 文字层作索引，但公式与图形回页面图像核对。
2. **不臆造**。难辨处一律进 `02_疑点清单.tsv`；原稿的笔误（例如第 7 页把合作者写成 "A.-Efimov-Orlov"、第 10 页把摩天楼层写成 $\OO_H$）照原样保留，另加批注说明。
3. **图的处理**。手写稿的示意图按几何内容用 Ti*k*Z 重画（裤子、带洞三角形、三面板、U 形弧、柱面、三价构形、传播圆盘），图注末尾标「原稿第 N 页」。
4. **附录照片**。幻灯片第 13 页有一幅 Jeff Koons 的雕塑《Balloon Dog》（摄影：Librado Romero，The New York Times）。版权所限不予复制，正文以文字说明其位置与用途。
5. **术语**。与 SY05-27 已冻结译名一致（Fukaya 范畴、拉格朗日、同调镜像对称、热带化、Novikov 域等）；wrapped、stop、Lefschetz thimble、framing、sectors、plabic、contact fusion、sacred rays 保留英文。

## 六、已知取舍

- **底本是手写笔记，不是作者审定的成文文献**。译文严格照录，不补证、不改写数学内容；因此某些句子在中文里显得"跳"，这是原稿的性质，不是翻译失误。凡补出之处均加方括号。
- **第 13 页的 "$A^1$ components"** 字迹与含义均无法确认，保留原记号并在批注中说明（疑点清单第 14 条，状态"待核"）。
- **第 3 页的一个修饰词**（写作近似 "Flwrix"）反复放大仍不可辨，据同页 "plabic sheaves / sectors"（层论一侧）判为与之对立的 "Floer-theoretic"，正文按此译，疑点清单记为"待核"。
- **参考文献不臆补**。原稿常按姓氏提到他人的工作（Hanlon、Hicks、Jeffs、Cannizzo、Lee、Gammage–Shende、Lekili–Polishchuk、Ganatra 等），未给出可核验书目信息，文献表不收录这些条目，另在表末附识说明。
- **定理编号按节**。原稿的"定理"多为口头断言且无编号，本译本按节编号，并在题注中保留原作者署名（如"（Abouzaid–A.）"）。
