# TIMELINE —— 边界裁决记录（Lead 独占）

## 底本坐标
- PDF 页号 = 印刷页码 + 10；正文印刷 pp.1–154，参考文献 pp.155–159（不译）。
- 编号公式 57 条；`tags.txt` / `tags_bypage.txt` 为唯一验收依据。
- 图 10 张，已裁好：`src/figures/fig11.png, fig21.png, fig41–47.png, fig61.png`。

## 分块边界（裁决即生效）
| 边界 | 裁决 |
|---|---|
| p.8 / p.9 | lead 写到第 1 章末（p.8）；tr-01 从第 2 章章首（p.9）开始写 `\chapter{…}` |
| p.19 / p.20 | tr-01 写到 §2.5.2 结束（p.19）；tr-02 从第 3 章章首（p.20）开始 |
| p.32 / p.33 | tr-02 写到第 3 章末（p.32）；tr-03 从第 4 章章首（p.33）开始 |
| p.41 / p.42 | tr-03 写到第 4 章末（p.41）；tr-04 从第 5 章章首（p.42）开始 |
| p.58 / p.59 | tr-04 写到第 5 章末（p.58）；tr-05 从第 6 章章首（p.59）开始 |
| p.70 / p.71 | **tr-05 写到 §6.4.1.2（Neumann 条件）结束（印刷 p.70）为止**；tr-06 从 §6.4.2 标题（印刷 p.71）开始，**不写 `\chapter`**，写 `\subsection{Boundary conditions in the matter sector}` |
| p.83 / p.84 | tr-06 写到第 6 章末（p.83）；tr-07 从第 7 章章首（p.84）开始 |
| p.99 / p.100 | tr-07 写到第 7 章末（p.99）；tr-08 从第 8 章章首（p.100）开始 |
| p.106 / p.107 | tr-08 在 ch08 写到第 8 章末（p.106），随后 ch09 从第 9 章章首（p.107）开始 |
| p.121 / p.122 | ch09 写到第 9 章末（p.121）；附录 A（p.122）由 tr-01 写（独立块，从 `\chapter` 开始，**不要写 `\appendix`**，Lead 在 main.tex 里统一给） |
| 附录 B | tr-02，p.132–141 |
| 附录 C | tr-03，p.142–149 |
| 附录 D | tr-06，p.150–154 |
| 参考文献 | Lead 统一生成 `c-refs.tex`（英文原貌） |

## 专属物件
- 图：fig11→lead；fig21→tr-01；fig41–fig47→tr-03；fig61→tr-06。其他人**不插图**。
- 表：无（原文 0 张表）。
- `\appendix`：**只有 Lead 在 main.tex 里写**，译者不写。
- 定理/定义/命题编号：ch09 的定义 1–7、命题 1–10；appD 证的是命题 (1)(3)(6)(7)(8)；appC 有 4 处**不编号**的 Theorem 块（印刷 p.145/146/146/148）。全部手工照抄原文。
- ch07 印刷 p.97 的 “Theorem 3.3.8” 是文献 [21] 的编号（外部定理），**不是本章定理**；不建 theorem 环境。
- appD 印刷 p.151 原文 “Theorem 1 tells us…” 是**原文悬空引用**（全文无 Theorem 1），照译 + 批注。

## 合成顺序
main.tex：preamble → c00 → c00b → 目录/图目录 → _order.tex（c01 → ch02 → ch03 → ch04 → ch05 → ch06a → ch06b → ch07 → ch08 → ch09 → appA → appB → appC → appD）→ c-refs
