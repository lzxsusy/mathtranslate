# ch05a 译注报告

## 1. 块名与页段

- 块名：ch05a（第 5 章章首块）
- 页段：PDF 251–272（原书 p.250–271），共 21 个原书页
- 输出文件：`src/chunks/ch05a.tex`（1216 行，汉字约 2.76 万）
- 章首标记：文件开头写 `\chapter{几何量子化}`，全块只出现一次；本块无 `\chapterreview`（第 5 章尚未结束）

## 2. 节清单

- §5.1 相空间的辛几何
  - 5.1.1 辛向量空间
  - 5.1.2 拉格朗日 Grassmann 流形
  - 5.1.3 马斯洛夫指标
  - 5.1.4 辛流形
- §5.2 几何半经典量子化
  - 5.2.1 半经典解
  - 5.2.2 半密度
  - 5.2.3 马斯洛夫修正（本块写到玻尔–索末菲条件与例 5.2.4 开头，§5.2 未在本块收尾）

## 3. 陈述编号清单（共 36 条，编号全部照抄原文）

- 定义 13 条：5.1.1、5.1.3、5.1.5、5.1.11、5.1.13、5.1.15、5.1.18、5.1.19、5.1.20、5.1.25、5.1.27、5.1.30、5.2.3
- 命题 10 条：5.1.2、5.1.7、5.1.9、5.1.12、5.1.16、5.1.21、5.1.22、5.1.23、5.1.26、5.1.31
- 例 12 条：5.1.4、5.1.6、5.1.8、5.1.10、5.1.14、5.1.17、5.1.24、5.1.28、5.1.29、5.1.32、5.2.2、5.2.4
- 注 1 条：5.2.1

其中带证明的有 6 条（命题 5.1.12、5.1.16、5.1.21、5.1.22、5.1.23、5.1.9），均用 `proof` 环境。

## 4. 图清单

| 文件 | 来源页 | 处理方式 |
| --- | --- | --- |
| `figures/fig_p259_a.png` | 原书 p.258（例 5.1.17） | 裁切 PNG，`width=0.40\textwidth`，图后注释「原书 p.258，图内文字照原样保留」 |
| `figures/fig_p263_a.png` | 原书 p.262（可投影拉格朗日子流形示意图） | 裁切 PNG |
| `figures/fig_p263_b.png` | 原书 p.262（例 5.1.29 圆周图） | 裁切 PNG |
| `figures/fig_p266_a.png` | 原书 p.265（$L_{dS}$ 与 $V_{\mathcal{H}}$ 相切示意图） | 裁切 PNG |
| `figures/fig_p269_a.png` | 原书 p.268（例 5.2.2 谐振子水平集圆） | 裁切 PNG |
| `figures/fig_p270_c.png` | 原书 p.269（$z_0$、$z$、闭链 $\gamma$ 示意图） | 裁切 PNG（重裁版；`fig_p270_a.png`、`fig_p270_b.png` 因裁切不全已弃用，文件仍留在 `src/figures/` 与 `work/review/`，未嵌入正文） |

另有 TikZ 重绘 5 张（均为「几何线条＋数学符号」的简单示意图，按 ch01a 体例重绘）：

- 命题 5.1.16 证明中的 $\tilde\varphi$ 交换图（$L_1\oplus JL_1\to L_2\oplus JL_2$，两侧下接 $V$）
- 纤维化 $\operatorname{SU}(n)/\operatorname{SO}(n)\to\mathcal{L}(V)\xrightarrow{\det^2}S^1$
- 纤维化 $\operatorname{SU}(n-1)\to\operatorname{SU}(n)\to S^{2n-1}$（$n\ge3$）
- 纤维化 $\operatorname{SO}(n)\to\operatorname{SU}(n)\to\operatorname{SU}(n)/\operatorname{SO}(n)$
- 回到 $\operatorname{SU}(n)/\operatorname{SO}(n)\to\mathcal{L}(V)\xrightarrow{\det^2}S^1$ 的纤维化

以上 TikZ 图只含数学符号，无英文单词标签，故不涉及图内标注翻译。

## 5. 术语与宏

- 未收术语 28 条，已登记 `work/term_requests_ch05a.md`（symplectic vector space 辛向量空间、Lagrangian Grassmannian 拉格朗日 Grassmann 流形、Maslov correction 马斯洛夫修正、Keller–Maslov 凯勒–马斯洛夫、EBK 爱因斯坦–布里渊–凯勒 等）。
- 群符号一律用 `\operatorname{Sp}`、`\operatorname{GL}`、`\operatorname{SL}`、`\operatorname{SO}`、`\operatorname{SU}`、`\operatorname{U}`、`\operatorname{O}`（preamble 无 `\Sp` 等宏；未改 preamble）。
- 拉格朗日 Grassmann 流形记 $\mathcal{L}(V)$（原书即用花体 L，未新建宏）。
- `\Span` 用 preamble 已有宏（排为小写 span，与原书大写 Span 排版略异，全工程统一，未自行改动）。
- 编译期修正：`\longhookrightarrow` 未定义，改 `\hookrightarrow`；两处超长公式拆行（厄米性推导、命题 5.1.22 的嘉当公式链）。

## 6. Tutor Note

本块未加 Tutor Note（原文无影响数学内容的明显笔误；个别纯排版不一致见第 8 节）。

## 7. 自检

```
LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0
DRAFT PDF -> work\tmp_ch05a.pdf
```

- 草稿 24 页；预览 `work/preview/ch05a_1.png`–`ch05a_24.png`（105 dpi）逐页目检：公式与原书一致、无溢出页边、图清晰、中文全角标点。
- `python tools\lint.py ch05a` → `合计：问题 0 条`，1 条提示「`\section`=2 而 `\takeaway`=1」——§5.2 跨块（收尾在 ch05b），属预期的跨块现象。

## 8. 存疑与交接

1. **块界半句**：原书 p.271 末句「The level set $C=\{\mathcal{H}(x,p)=E\}$」的谓语在 p.272 首「is a Lagrangian submanifold.」。本块按 Lead 规则译到完整句「……是一张拉格朗日子流形。」并闭合例 5.2.4，文件末尾已写块界注释。
2. **与 ch05b 重复**：`src/chunks/ch05b.tex` 已由 tr07 写出，其第 7–8 行也补全了同一句（「水平集 $C=\{H(x,p)=E\}$ 是拉格朗日子流形。」），合书时会重复。建议 Lead 定夺：删去 ch05b 第 8 行前半句、保留「我们有 …」，或删去本块末句（但本块例 5.2.4 需保留 `\end{example}`，故不宜删）。另注意 ch05b 未重新打开 `example` 环境，其续文作为普通段落，依赖本块闭合例 5.2.4。
3. **原文记号不一致**：原书 p.268 定义投影时写 $\pi_P:L\to\R$，紧接着正文又写 $\pi_p$ 是 $u_\pm$ 附近的局部微分同胚。本块统一取 $\pi_P$，未加 Tutor Note（纯下标大小写，不影响数学内容）。
4. **§5.2 的 `\takeaway`**：§5.2 在本块起头、未收尾，其 `\takeaway` 应由 ch05b 在节末补（与本块 §5.1 的 `\takeaway` 配对）。
