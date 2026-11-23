# 分工表（Lead 维护）

底本：Frenkel, *Langlands Correspondence for Loop Groups*（2007, 406 PDF 页）。
印刷页 = PDF 页 − 14。每单元输出一个 `.tex` 片段 + 一份 `reports/UXX.md`。

| 单元 | PDF 页 | 印刷页 | 内容 | 输出文件 | 负责人 |
|---|---|---|---|---|---|
| U01 | 15–22 | 1–8 | 第 1 章 + 1.1 经典理论 | ch01-1.tex | 待定 |
| U02 | 23–44 | 9–30 | 1.2–1.3 | ch01-2.tex | 待定 |
| U03 | 45–74 | 31–60 | 第 2 章 顶点代数 | ch02.tex | 待定 |
| U04 | 75–94 | 61–80 | 第 3 章 + 3.1–3.3 | ch03-1.tex | 待定 |
| U05 | 95–114 | 81–100 | 3.4–3.5 | ch03-2.tex | 待定 |
| U06 | 115–139 | 101–125 | 第 4 章 oper | ch04.tex | 待定 |
| U07 | 140–153 | 126–139 | 第 5 章 + 5.1–5.3 | ch05-1.tex | 待定 |
| U08 | 154–176 | 140–162 | 5.4–5.6 | ch05-2.tex | 待定 |
| U09 | 177–208 | 163–194 | 第 6 章 Wakimoto 模 | ch06.tex | 待定 |
| U10 | 209–231 | 195–217 | 第 7 章 交织算子 | ch07.tex | 待定 |
| U11 | 232–260 | 218–246 | 第 8 章 中心=opers | ch08.tex | 待定 |
| U12 | 261–283 | 247–269 | 第 9 章 + 9.1–9.3 | ch09-1.tex | 待定 |
| U13 | 284–314 | 270–300 | 9.4–9.6 | ch09-2.tex | 待定 |
| U14 | 315–325 | 301–311 | 第 10 章 + 10.1–10.2 | ch10-1.tex | 待定 |
| U15 | 326–346 | 312–332 | 10.3 无分歧情形 | ch10-2.tex | 待定 |
| U16 | 347–374 | 333–360 | 10.4 温和分歧情形 | ch10-3.tex | 待定 |
| U17 | 375–388 | 361–374 | 10.5 从局部到整体 | ch10-4.tex | 待定 |
| U18 | 389–401 | 375–387 | 附录 A + 参考文献 | appendix.tex, bibliography.tex | 待定 |
| — | 9–14 | v–x | 序言 + 译校说明 + 标题页 | preface.tex 等 | Lead（已完成） |

## 纪律
1. 每个单元只写自己的文件，禁止改 `preamble.tex`、`main.tex`、`GLOSSARY.md`、`units/` 与别人的章节。
2. 公式必须对照 `pages/pNNN.png` 核对；`text/pNNN.txt` 只用于定位（数学符号不可信）。
3. 编号公式用 `\tag{x.y-n}` 保留原编号；定理/引理用环境自动编号。
4. 每节开头 `keypoints`；批注 `% [Tutor Note: ...]` 每 2–3 页至少一条、每节至少 3 条。
5. 自检：`pwsh -File tools\check.ps1 -Chunk tex\chapters\<file>` 必须 `CHECK OK`。


## 实际执行记录（终稿）

| 单元 | 负责人 | 文件 | 状态 |
|---|---|---|---|
| U01 | ch01a | ch01-1.tex | ✔ |
| U02 | ch01b | ch01-2.tex | ✔ |
| U03 | ch02 | ch02.tex | ✔ |
| U04 | ch03a | ch03-1.tex | ✔ |
| U05 | ch03b | ch03-2.tex | ✔ |
| U06 | ch04 | ch04.tex | ✔ |
| U07 | ch05a | ch05-1.tex | ✔ |
| U08 | ch05b | ch05-2.tex | ✔ |
| U09 | ch02 | ch06.tex | ✔ |
| U10 | ch04 | ch07.tex | ✔ |
| U11 | subagent U11 | ch08.tex | ✔ |
| U12 | ch05b | ch09-1.tex | ✔ |
| U13 | ch03b | ch09-2.tex | ✔ |
| U14 | ch01b | ch10-1.tex | ✔ |
| U15 | ch05a | ch10-2.tex（含 p.347 上半补译） | ✔ |
| U16 | ch01b | ch10-3.tex | ✔ |
| U17 | ch03a | ch10-4.tex | ✔ |
| U18 | ch01a | appendix.tex + bibliography.tex | ✔ |
| 前置 | Lead | titlepage/preface/translator-note | ✔ |

专项审计：QC-front（ch01a）、visual-qa（ch01a）、structure-audit（ch05b）、seam-audit（ch01b）、formula-audit（ch05a）、citation-audit（ch05a）、terms-audit（ch04）、numeric-spotcheck（ch03b）、审校报告（ch03a）。
终审与合成：Lead。最终编译 327 页，0 error / 0 overfull / 0 missing character。
