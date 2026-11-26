# 校对报告 rev-b：第 5、6、9 讲

- 对象：`源码/chapters/lecture05.tex`（568 行，p033–p045）、`lecture06.tex`（378 行，p046–p054）、`lecture09.tex`（476 行，p070–p078）。
- 依据：底本 `工程文件/work/pages/` 逐页文本、`glossary.tsv`（冻结）、`STYLE_GUIDE.md`。三篇均与底本逐句对读、公式逐条验算；**未修改任何 .tex**。

## 一、lecture05.tex

1. [严重] lecture05.tex:239,241 | $\Af^S$ 的定义与配套译注方向都反了。底本 p038 作 `A_f^S := Q ⊗_Z Ẑ^S`，这是对的：$\Q\otimes_\Z\prod_{p\notin S}\Z_p=\bigcup_n\prod_{p\notin S}\Z_p[1/n]$，恰为受限直积 $\sideset{}{'}\prod_{p\notin S}\Q_p$。现行写法取无限制直积，使 $\Af^S$ 非局部紧，第 250 行的 $T_S:=H(\GL_2(\Af^S),\GL_2(\widehat\Z^S))$ 随之失去意义，也与第 245 行已用的 $\sideset{}{'}\bigotimes$ 冲突；译注更把正确原文判为「错」，且其「正解」漏掉受限条件（与括注「几乎处处落在 $\Z_p$ 中」自相矛盾）。| 现在：`\Af^S:=\prod_{p\notin S}\Q_p`，外加 `\znote{原文把 $\Af^S$ 写成 $\Q\otimes_\Z\widehat\Z^S$；…张量积一般不保持无穷乘积，故此处按正解译。}` | 建议：恢复 `\Af^S:=\Q\otimes_\Z\widehat\Z^S`，删去该 \znote；若仍要解释，写作 `\Af^S=\sideset{}{'}\prod_{p\notin S}\Q_p`，并说明 $\Q\otimes_\Z\prod\Z_p\cong\sideset{}{'}\prod\Q_p$。

2. [中等] lecture05.tex:174 | $S$ 以 $m\ge0$ 取并：$m=0$ 时「$p\mid0$」对一切素数成立，且 $V^{K(0)}=V\neq0$，于是 $S$ 变成全体素数，与紧接的第 176 行「$p\in S$ 当且仅当 $V^{\GL_2(\Z_p)}=0$」及 177 行「非分歧」的定义直接冲突（底本 p036 同误，属底本缺陷）。| 现在：`S:=\bigcup_{m\ge0,\,V^{K(m)}\neq0}\{\,p\ \text{素数}:p\mid m\,\}` | 建议：条件改 `m\ge1`，并加 `\znoteplain{原文作 $m\ge0$；$m=0$ 时 $p\mid0$ 对一切 $p$ 成立，会把 $S$ 变成全体素数，故按 $m\ge1$ 读。[来源：原文 p.036 同式及其下一条 $p\in S\iff V^{\GL_2(\Z_p)}=0$]}`。

3. [中等] lecture05.tex:461 | 译注末句「同一笔误亦见于 p.032」不实：底本 p032 的 $\Gamma_0(m)$ 写作 `{… ∈ SL_2(Z) | c ≡ 0 mod m}`，本身正确，$c\equiv1$ 的笔误只在 p043。译注出错会给读者错误的「勘误史」。| 现在：`…；同一笔误亦见于 p.032。` | 建议：删去该分句，或改为「[来源：原文 p.043 的 $\Gamma_0(m)$ 定义与 p.042 的 $\Gamma_1(m)$ 定义]」。

4. [轻微] lecture05.tex:254 | 「维数可数，因此剩余域为 $\C$」推理不成立：可数维 $\C$-代数可有大于 $\C$ 的剩余域（如 $\C[t_1,t_2,\dots]$ 的极大理想）。正确理由是 $T_S$ 为诸 $T_{S,F}$（有限个 $p$ 的张量积，有限生成 $\C$-代数）之并，任一同态之像在 $\C$ 上有限生成，由 Zariski 引理像为 $\C$；结论本身为真，底本 p038 亦如此措辞。| 现在：`$T_S$ 的维数可数，因此每个 Hecke 特征系统的剩余域为 $\C$。` | 建议：改为「$T_S$ 是诸有限生成 $\C$-代数 $T_{S,F}$ 的并，故任一 $\C$-代数同态 $T_S\to K$ 的像由 Zariski 引理等于 $\C$，即每个 Hecke 特征系统的剩余域为 $\C$。」（可放进 \znoteplain 并注明底本措辞）

5. [轻微] lecture05.tex:309 | 底本 p039 末句误作 `Mat_{2,2}(Z_p)^{val=0}`（同页前两处均为 val=n），译文静默改为 `\mathrm{val}=n`——数学上正确，但读者对不上原文。| 现在：`…因为 $\mathrm{Mat}_{2,2}(\Z_p)^{\mathrm{val}=n}$ 中出现的其它双陪集…` | 建议：加半句 `\znoteplain{原文此处误作 $\mathrm{val}=0$，按定义应为 $\mathrm{val}=n$。[来源：原文 p.039 与前两处的用法]}`。

6. [轻微] lecture05.tex:511 | `\\pm` 中的 `pm` 紧贴换行符，极易被误读成 `\pm`；实际编译为「换行 + $pm$」，数学无误：$\begin{pmatrix}1&0\\0&p^{-1}\end{pmatrix}\begin{pmatrix}a&p^{-1}b\\pm&p\end{pmatrix}=\begin{pmatrix}a&p^{-1}b\\m&1\end{pmatrix}$ 与左侧相等。| 现在：`\begin{pmatrix}a&p^{-1}b\\pm&p\end{pmatrix}` | 建议：写作 `\\ pm` 或 `\\ p\,m`，渲染不变而歧义消除。

## 二、lecture06.tex

7. [中等] lecture06.tex:95 | 本句与下句、与 65–91 行的证明三者互相矛盾：先说「迹 $c_{i,p}$ 决定（半单）表示」是错的，紧接又说完整系统 $\{c_{1,p},\dots,c_{n,p}\}$ 由 Brauer–Nesbitt 仍唯一决定；而 65–91 行恰恰用 $\{c_{1,p}\}$ 证出决定性。真正要表达的是「单条迹不够，须整族」，底本 p048（`it is wrong that the traces c_{i,p} determine the (semisimple) representation`）把 $c_{1,p}$ 写成 $c_{i,p}$，又把「特征 0」与「是错的」硬接。| 现在：`重要的是我们考虑的是特征 $0$ 系数的表示；也就是说，「迹 $c_{i,p}$ 决定（半单）表示」这一说法是错误的。` | 建议：改为「重要的是系数域的特征为 $0$：此时由 Brauer–Nesbitt，单凭迹 $c_{1,p}$ 即可决定半单表示；特征为 $p>0$ 时则不然，必须知道全部外幂上的迹，即整族 $\{c_{1,p},\dots,c_{n,p}\}$。」95 行 \znoteplain 中对底本 $c_{i,p}$ 的说明可保留。

8. [轻微] lecture06.tex:335 | 语序照搬英文（construct (something close to) a GL_2(A_f)-equivariant embedding）。| 现在：`则我们将构造（接近）一个 $\GL_2(\Af)$-等变嵌入` | 建议：`则我们将构造一个（近乎）$\GL_2(\Af)$-等变的嵌入`。

## 三、lecture09.tex

9. [中等] lecture09.tex:398,409 | 术语与全书不一致：此处作「（标准化的）新形式」，而 lecture05.tex:552、lecture06.tex:11,23,149,180,189,238 一律作「归一化新形式」（`glossary.tsv` 无 normalized newform 条目，仅第 70 行 `normalization 正规化`）。| 现在：`对标准化的新形式 $f\in S_2(\Gamma_0(N),\chi)$…` / `把（标准化的）新形式…` | 建议：统一改为「（归一化的）新形式」。

10. [轻微] lecture09.tex:220 | 条件从句后置照搬英文（decays rapidly as Im z → ∞, n ≥ 1），中文是断的。| 现在：`利用 $|e^{2\pi inz}|=e^{-2\pi n\operatorname{Im}(z)}$ 当 $\operatorname{Im}(z)\to\infty$ 且 $n\ge1$ 时迅速衰减。` | 建议：`利用：当 $\operatorname{Im}(z)\to\infty$、$n\ge1$ 时，$|e^{2\pi inz}|=e^{-2\pi n\operatorname{Im}(z)}$ 迅速衰减。`

11. [轻微] lecture09.tex:455 | 「实现为一个……概形的平展上同调」搭配不成立（realize as the étale cohomology of…）；「proper、光滑概形」亦英文语序。| 现在：`由于 $\rho_f$ 实现为一个 $\Q$ 上 proper、光滑概形的平展上同调，…` | 建议：`由于 $\rho_f$ 可以实现在一个 $\Q$ 上 proper 光滑概形的平展上同调中，…`。

12. [轻微] lecture09.tex:472 | 「为……辩护」是 justify 的硬译。| 现在：`因此需要额外的论证，才能为基变换到 $\overline\F_p$ 辩护。` | 建议：`……才能使基变换到 $\overline\F_p$ 合法` 或 `才能为基变换到 $\overline\F_p$ 提供依据`。

13. [轻微] lecture09.tex:264 | 「完成……路线」动宾不搭。| 现在：`至此，我们完成了为新形式附着 Galois 表示的既定路线（至少在权 $2$ 的情形）。` | 建议：`至此，我们走完了「为新形式附着 Galois 表示」这一既定路线（至少在权 $2$ 的情形）。`

## 四、跨讲与结构核查

14. [轻微] 跨讲术语 | 「attach」在 lecture09.tex:1,7,68,264,266,332 及 lecture10、lecture12 中作「附着」，在 lecture05.tex:264、lecture06.tex:148,241,333 中作「相伴」。单讲内部自洽，但全书不统一；建议以「附着」为准（与第 9、10 讲标题一致）。

15. [通过] 页标记：lecture05 13 条（p033–p045，行 3/43/90/135/187/230/278/315/361/397/442/494/545）、lecture06 9 条（p046–p054）、lecture09 9 条（p070–p078）；逐页唯一、顺序与底本一致，无缺页重页。

16. [通过] 结构：`\begin`/`\end` 配对 56/56、18/18、29/29；编号 定义 5.1–5.4（33/44/224/250）、定理 5.5（375）、定理 5.6（548）、定理 9.1（190）、引理 9.2（359）、命题 9.3（392）均与底本一致；lecture09 的 `\tag{2}`(212)、`\tag{3}`(314) 接续第 8 讲的 `\tag{1}`（lecture08.tex:174），与底本印刷编号一致。

17. [通过] 译注：lecture05 八条（\znote 241/461，\znoteplain 23/48/378/379/402/542，已达体例上限 8 条）、lecture06 六条（64/95/222/223/313/372）、lecture09 七条（60/258/471，135/250/281/389）；`\znote` 均带 `[来源：…]`，原文脚注统一折为 `\znoteplain{原文脚注：…}`，与 lecture01/02/03/07 体例一致。

18. [已核无误] 高优先级数学点均正确：Hecke 卷积 $f*g(x)=\int_G f(xy)g(y^{-1})\,dy$、$\chi_{g_1K}*\chi_{g_2K}=\sum_j\mu(K)\chi_{h_jK}$、$e_K=\frac{1}{\mu(K)}\chi_K$、$H(G,K)=e_KH(G)e_K$、$V^K=e_K*V$ 及「不可约 ⇒ $V^K$ 不可约」的证明链；$H(\GL_2(\Q_p),\GL_2(\Z_p))\cong\C[X_1,X_2^{\pm1}]$（含 $KzK$ 的中心性、$f$ 满射的验证）；$\tilde T_p(f)=p^k\chi(p)f(pz)+\sum_{j=0}^{p-1}f((z-j)/p)$ 及其 Fourier 版、$\tilde a_p=pa_p$、$T_p=\frac1p\tilde T_p$；$\tilde S_p$ 的因子 $p^k\chi(p)$（$A\in\Gamma_0(m)$ 给 $\chi(p)$）；$X^2-\iota^{-1}(a_p)X+\iota^{-1}(b_p)$、Hodge–Tate 权 $0,\omega$（$\omega=k-1$）、Tate 定理、Grothendieck–Lefschetz 迹公式与 Chebotarev 段；Eichler–Shimura 同构、内上同调、$\tilde\rho_\pi$ 的二维性与 $X^2-a_pX+\chi(p)p$ 的完整推导链（$pa_p$、$\chi(p)p^2$ 与 $1/p^2$ 的扭）。

## 总体评价

这三讲整体质量高：底本的口语化推导被完整转成可读的书面语，几处底本笔误（p039 的 val=0、p043 的 $c\equiv1$、p047 用几何 Frobenius 的第二条注）都识别正确，$\tilde T_p$ 与 $X^2-a_pX+\chi(p)p$ 两条关键公式链逐项验算通过。
需要修的是两类问题：一是 lecture05.tex:239 的 $\Af^S$ 及配套译注（唯一会误导读者、且与本书其他表述冲突的硬错误），二是 lecture05.tex:461、lecture06.tex:95 这种「正文或译注关于底本的陈述本身有误/自相矛盾」的地方，其余多为行文与术语统一。
建议：改完第 1、2、3、7、9 条后即可定稿；其余轻微项与全书通稿时一并处理即可。
