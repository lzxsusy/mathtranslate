% Overfull 清理报告（tr-ch5a，2026-11-11）
% 编译环境：xelatex（MiKTeX），`-output-directory=tmp/ovf`，TMP/TEMP=tmp/。
% 所有验证编译都在 tmp/ovf 下进行，未触碰工程根目录的 main.pdf / aux。

## 结论

- 修前：全本 19 处 Overfull（Lead 清单），最大 34.9pt。
- 修后：**全本 Overfull 总数 = 0**（`main.tex` 编译 156 页，0 error）。
- 每块单编（wrapper = 同款 documentclass + `\input{src/preamble.tex}` + 单块）均 0 Overfull、0 error。
- 未改字号、未删内容、未动 b16；b15 已改但见下方并发说明。

## 逐条明细（文件:行 → 原 pt → 修法 → 复验 pt）

| # | 文件:行 | 原 Overfull | 类型 | 修法 | 复验 |
|---|---------|------------|------|------|------|
| 1 | b00_preface.tex:7–13 | 2.01pt | paragraph | 该段外包 `\begin{sloppypar}…\end{sloppypar}` | 0 |
| 2 | b01.tex:617–619 | 6.82pt | paragraph | 同上 | 0 |
| 3 | b01.tex:887–888 | 5.88pt | paragraph | 同上 | 0 |
| 4 | b02.tex:301 | 34.87pt | detected（显示式） | 该式分子改用 `\splitfrac{…}{…}` 断成两行（`\operatorname{Ker}` 后一行、`H^0(C,\cD^{(0,2)}…)` 一行），分母不动 | 0 |
| 5 | b02.tex:308–309 | 29.29pt | paragraph | `\begin{sloppypar}` 包裹 | 0 |
| 6 | b03.tex:23–30 | 4.38pt | paragraph | 同上 | 0 |
| 7 | b03.tex:237–241 | 1.81pt | paragraph | 同上 | 0 |
| 8 | b04.tex:10–13 | 25.69pt | paragraph | 同上 | 0 |
| 9 | b07.tex:85–86 | 0.98pt | paragraph | 同上 | 0 |
| 10 | b07.tex:523–528 | 24.03pt | paragraph | 同上 | 0 |
| 11 | b07.tex:678–681 | 27.59pt | paragraph | 同上 | 0 |
| 12 | b08.tex:86 | 33.02pt | detected（显示式） | 该式改用 `\[\begin{aligned}…\end{aligned}\]`，在 `=` 前断行，第二行 `\qquad` 缩进对齐 | 0 |
| 13 | b08.tex:154–156 | 18.06pt | paragraph | `\begin{sloppypar}` 包裹 | 0 |
| 14 | b08.tex:452–457 | 11.53pt | paragraph | 同上 | 0 |
| 15 | b09.tex:6–9 | 0.70pt | paragraph | 段首插 `{\emergencystretch=2.8pt `、段末 `\par}` | 0 |
| 16 | b10.tex:159–160 | 22.84pt | paragraph | 段首插 `{\emergencystretch=28.3pt `、段末 `\par}` | 0 |
| 17 | b11.tex:559–561 | 19.32pt | paragraph | 段首插 `{\emergencystretch=24.2pt `、段末 `\par}`（修后该段在 561–563 行） | 0 |
| 18 | b13.tex:407–408 | 17.64pt | paragraph | 段首插 `{\emergencystretch=22.3pt `、段末 `\par}` | 0 |
| 19 | b15.tex:491–494 | 2.77pt | paragraph | 段首插 `{\emergencystretch=5.2pt `、段末 `\par}`（修后该段在 458–461 行） | 0 |

另有本块（B12）此前已修的 41.56pt（b12.tex p.103「注意…」段，逗号后插 `\allowbreak`），本次复验仍为 0。

## 修法说明（为什么分两种）

- 这批 Overfull 全部落在**段内**（`paragraph at lines`），根因是中文行内公式构成的长不可断块：CJK 字间 glue 的伸缩量极小，一旦某行落在一段很长的行内数学之间，就没有可行的断点，TeX 只能给出 Overfull。
- 小溢出的段（< 25pt、且断行只需少量额外伸缩）用**局部 `\emergencystretch` 组**：只影响该段的伸缩量，不动 `\tolerance`，视觉最保守。
- 大溢出段改用 **`sloppypar`**（局部 `\tolerance=9999` + 3em 紧急伸缩）：这是 LaTeX 标准的"该段允许较松断行"手段，只改断行参数，不改字号、不删内容、不动公式。
- 「detected at line」两处是显示公式超宽，按 Lead 要求改成 `aligned` / `\splitfrac` 断行，编号 tag 位置不变（这两处本身无编号）。

## c_v 统一

`c_V` → `c_v` 单向替换（含译注注释，保持文件内一致）：
- `src/b08.tex`：7 处
- `src/b09.tex`：3 处
- `src/b11.tex`：27 处
替换后三文件内 `c_V` 残留 0 处；b00/b05/b06/b12 未动（本就是 `c_v`）。

c_v unified: b08 7 / b09 3 / b11 27

## 并发说明（b15）

- b15.tex 在我动手前后被 tr-ch5b 改动过（mtime 23:11:13，晚于我插入 wrap 的时刻）。当前 b15.tex 内我的 `\emergencystretch` 组仍在（grep 计数 1），单编 b15 与全本编译均 0 Overfull；但若 tr-ch5b 后续重写该段，此行可能被覆盖，届时需重跑一次全本确认。
- b16.tex 全程未动。

## 复验命令

```
# 单块
python tmp/ovf/ovf.py b02.tex ...   # 逐块 0 Overfull / 0 error
# 全本（输出全在 tmp/ovf，不写工程根）
$env:TMP="...\cft_gauge\tmp"; $env:TEMP=$env:TMP
xelatex -interaction=nonstopmode -output-directory=tmp\ovf main.tex
```

修后全本：**156 页 / 0 error / Overfull 总数 0**。
