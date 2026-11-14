# 分章报告：chapters/sec02d.tex（§2.7 与第 3 节，原书 p.14–20）

## 一、完成情况
§2.7 旁注与第 3 节（3.1、3.2）全文逐句译出，无删节：编号式 16 个（32–47），未编号行间式 5 个（$V$ 的分解、$\mathbb M$ 的分解、$\mu(X_1,X_2,X_3)$ 树形示例、$A/B$ 的对角/非对角分解、$A'/B'$ 分解），图 8、9、10 各一，脚注 9–14 六条；批注 19 条（易错预警 11、含糊点拨 4、背景直觉 4），每页约 2.7 条；takeaway 4 段（2.7、§3、3.1、3.2）。文件止于式 (47)，§4（式 48 起）归 translator-d，无重叠。

## 二、公式核对
所有公式回 work/pages/p14–p20.png 及 350 dpi 裁剪图逐符号核对。重点：式 (32) 用 `\curvearrowright` 与 `\overset/\underset` 复现 $K\curvearrowright V\overset{\mathrm i}{\underset{\mathrm p}{\rightleftarrows}}\mathbb M$；式 (42) 的四个系数 1/2、1/2、1/2、1/8 逐项核对（(42) 末项「哑铃」树自同构群阶为 8，故 1/8）；式 (43) 的 (a)–(f) 六项小标与 (e)=$\langle B_Z,\tfrac12[A_Z,A_Z]\rangle$、(f)=$\langle B_Z,\tfrac12[A_W,A_W]\rangle$ 核对无误。引用按 `work/citations.md` 改为 `\cite`：`kontsevichsoibelman`（含 `\cite[第 6 章]{}`）、`cattaneo`（脚注 12）、`mnev`（[15]）；批注中另引 `crainic`、`gugenheim`、`lambe`。

## 三、术语裁定请求
1. **范畴记号**：已随 Lead 全局替换改为 $\mathbb F$；复形用 $\mathbb M$，以区别于模空间 $\mathcal M$。
2. **coboundary operator**：术语表只有 boundary operator（边界算子），暂译「余边界算子」，请裁定是否统一为「上边缘算子」。
3. **新术语登记**：fast fields→快场；half-edge→半边；loose (external) half-edge→自由的（外部的）半边；integral structure→整结构；enumerative flavor→计数味道；arity 保留英文；1-loop→单圈图；loop enhancement→圈增强。

## 四、原文疑似笔误（照录 + 批注，未擅改）
1. p.17「Kontsevich–Soibleman」：应为 Soibelman。正文照录并同处批注；建议 Lead 裁定是否全书统一改正（我只此一处）。
2. 式 (33) 下方的树形示例图是原书内嵌手绘图，纯 LaTeX 无法复现（导言区无 tikz，且不得新增图片文件）。中译保留求值式 $\mu(X_1,X_2,X_3)=\mathrm p(K(\mathrm i(X_1)\cdot\mathrm i(X_2))\cdot\mathrm i(X_3))$ 并加批注说明树的装饰；请 Lead 裁定是否需补图或改用 fig 裁剪。

## 五、存疑
- 脚注由 LaTeX 全局自动编号，与原文 9–14 号不对应；批注中用「那条脚注」指代，未硬编码编号。
- 式 (43) 的 (a)–(f) 用 `\underset` 置于各项正下方，贴合原书版式但行距偏紧，请编译后看效果。
- 图号依赖前七图按序出现（已确认为 fig01–fig07），合并后图 8–10 应自动对上。

## 六、自检
`work/lint.py chapters/sec02d.tex` → **PASS，FAIL=0**（18 条 warn 全为跨文件 `\ref`：eq:3/4/7/12/18/20/29/31、thm:1、sec:2.1，按约定忽略）。另核：`\begin/\end` 与花括号平衡、`$` 成对、`\tag` 32–47 连续、`\endinput` 在文末；无英文整句、无「被……所」「进行……的」「对于……而言」；最长句 55 汉字；未触碰 main.tex、figures/、glossary 与他人文件。
