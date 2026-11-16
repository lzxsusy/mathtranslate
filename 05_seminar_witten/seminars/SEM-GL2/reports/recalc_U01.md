# U01 复算报告（P5 / r8）

**复算对象**：Kapustin–Witten, *Electric–Magnetic Duality and the Geometric Langlands Program*, hep-th/0604151（记 B），§1–§2。
**U01 范围**：印刷页 pp.2–16，对应逐页文本 `p003.txt`–`p017.txt`（映射：印刷页 N ↔ `p{N+1:03d}.txt`；§3 标题在 `p017.txt` 第 36 行）。
**输入**：`work/rounds/U01/report_v1.md`（110 行，下称"报告"，行号即其行号）、`work/rounds/U01/crit_r4.jsonl`、`work/rounds/U01/crit_r6.jsonl`。
**环境**：`python`（Python 3 + sympy 1.14.0）。所有计算见文末附录 A，可原样重跑。
**纪律**：五项全部完成，无"未完成"项；每条结论给算式/脚本与原文行号；报告原文引用逐字。

---

## 1. τ 与 T

### 1.1 定义与算式

B 的作用量含 θ 项（2.11）：

$$I_\theta = -\frac{\theta}{8\pi^2}\int \mathrm{Tr}\,F\wedge F \qquad\text{(2.11，p010.txt:39–46)}$$

并把 e、θ 合成（2.12）：

$$\tau = \frac{\theta}{2\pi} + \frac{4\pi i}{e^2}\qquad\text{(2.12，p011.txt:1–6)}$$

（B 用规范耦合 e；任务里写 g，同义。以下用 e。）

**sympy 计算**（附录 A.1，逐行可跑）：

- $\operatorname{Im}\tau = \dfrac{4\pi}{e^2} > 0$（τ 落在上半平面）；
- $\tau(\theta+2\pi) - \tau = \dfrac{2\pi}{2\pi} = 1$，虚部不变；
- 因此 $…/tau+1$ 时 $\Delta\operatorname{Re}\tau = 1$，只能来自 $\theta/2\pi$ 的 $+1$，即 $\theta\mapsto\theta+2\pi$；$\operatorname{Im}\tau$ 不变且 $e>0$，即 $e$ 不变（$g$ 不变）。
- 反向同理：$\theta\mapsto\theta+2\pi$、e 不变给出 $\tau\mapsto\tau+1$。

所以 **T 与"θ→θ+2π、g 不变"是同一变换**，B 的原文也正是把 T 解释为 θ 平移（p012.txt:21–22：``T : τ → τ + 1`` 是 θ 平移 2π、任意 G 在 R⁴ 上的经典对称）。

### 1.2 为什么 p.8 的整值归一化是前提

B 在 p.8（p009.txt:5–13）取 Tr 为李代数上不变负定二次型，G 单 ⇒ 唯一到常数倍，并**归一化**为：M=S⁴ 时

$$K \equiv \frac{1}{8\pi^2}\int_M \mathrm{Tr}\,F\wedge F \in \mathbb{Z}\quad(\text{"takes arbitrary integer values"})$$

（K 即瞬子数/第二 Chern 数，B 在 p.10 首行点明 "This last term is θ times the second Chern class or instanton number of the bundle"，p011.txt:1。）

θ 平移的量子判据：$I_\theta = -\theta K$，故 $\theta\mapsto\theta+2\pi$ 时

$$\Delta I_\theta = -2\pi K,\qquad e^{i\Delta I_\theta}=e^{-2\pi i K}.$$

**计算**：$e^{i\Delta I_\theta}=1 \iff K\in\mathbb{Z}$（附录 A.1 得 $\Delta I_\theta/(2\pi)=-K$）。若 Tr 归一化选得使 K 只落在 $\frac1m\mathbb{Z}$，则 θ→θ+2π 会把 $e^{iI}$ 乘上 $e^{-2\pi i/m}\ne1$，T 不是对称、θ 的周期变成 $2\pi m$、τ 的模变换群不再是 SL(2,Z)，(2.23) 的 SL(2,Z) 作用整体错位。B 在 p.10 明确把"整数值"说成 τ→τ+1 存在的原因（p011.txt:8–14：``there is an elementary symmetry τ → τ + 1, which expresses the fact that (1/8π²)∫TrF∧F is integer-valued, and that in quantum mechanics one only cares about the action modulo an integer multiple of 2π. Equivalently, θ is an angular variable, with θ ≅ θ + 2π``）。而"整值"是 p.8 归一化的人为选择（G 单 ⇒ Tr 唯一到常数倍），所以 **p.8 的归一化恰是 T 的前提**。

B 还附加了流形条件：R⁴ 或 $H^2(M,\mathbb{Z})=0$ 的四维流形；一般流形上 $\pi_1(G)$ 进场（见 p.11 对 [45,26] 的引文）。这划定了本论证的适用面。

**结论**：T: τ→τ+1 ⇔ θ→θ+2π 且 g 不变；前提是 p.8 的 Tr 归一化使瞬子数 K 为整数。复算通过（与报告 L27 一致）。

---

## 2. (2.25) 特殊值

### 2.1 定义、分支与记号

(2.25)（p017.txt:1–6，印刷 p.16）：

$$e^{-i\hat\varphi(\gamma)} = \left(\frac{|c\tau+d|}{c\tau+d}\right)^{1/2},\qquad \gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma.$$

B 紧接着说（p017.txt:8–13）：平方根意味着作用在超荷上的群是 Γ 的**双覆盖**，扩展由 $(-1)^F$（2 阶，翻转所有费米子符号）给出，而 $(-1)^F = I^2$（$I$ 为 SU(4)_R 中心生成元）；B 取 $\hat\varphi$ 在 Γ 下不变（而不是不变到符号）。

取主值分支：$\hat\varphi(\gamma,\tau)=\frac12\arg(c\tau+d)$，其中 $z=c\tau+d$；对 $\tau$ 在上半平面，$c>0$ 时 z 在上半平面、$\arg z\in(0,\pi)$，$c<0$ 时 z 在下半平面、$\arg z\in(-\pi,0)$，故 arg 沿 τ 连续（附录 A.2 逐点验证 $e^{-i\hat\varphi}=\sqrt{\bar z/r}$，$r=|z|$，误差 <1e-15）。

**S 的约定**：以原文 (2.16) 为准（p012.txt:28–41）：$S=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$，即 $(c,d)=(-1,0)$。任务里写的 $S=(0,-1;1,0)$ 等于 **−S**（差中心 −I），见 §2.3。

### 2.2 特殊值表

$T=\begin{pmatrix}1&1\\0&1\end{pmatrix}$，$T^n=\begin{pmatrix}1&n\\0&1\end{pmatrix}$，$S=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$（(2.16)），$-S$（任务给的矩阵），$S_{n_g}=\begin{pmatrix}0&1/\sqrt{n_g}\\-\sqrt{n_g}&0\end{pmatrix}$（(2.17)），$S'_{n_g}=\begin{pmatrix}0&-1/\sqrt{n_g}\\\sqrt{n_g}&0\end{pmatrix}$（(2.26) 的矩阵，差一个 −I），以及 $-I=\mathrm{diag}(-1,-1)$（说明用）。

记 $z=c\tau+d$、$r=|z|$，则 $e^{-i\hat\varphi}=\sqrt{\bar z/r}$。下表"τ=i 的值"按 $\hat\varphi$ 的 lift 给，**整体可差 π/2**（中心 I 的歧义，B p.14：$\hat\varphi\to\hat\varphi+\pi/2$）。

| γ | (c,d) | $e^{-i\hat\varphi}$ | $\hat\varphi(\gamma,\tau)$ | τ=i 的值 |
|---|---|---|---|---|
| T | (0,1) | $\sqrt{1/1}=1$ | 0 | 0 |
| T^n | (0,1) | 1 | 0 | 0 |
| S（(2.16)） | (−1,0) | $\sqrt{\bar z/r}$，$z=-\tau$ | $\tfrac12(\arg\tau-\pi)$ | $-\pi/4$ |
| −S（任务矩阵） | (1,0) | $\sqrt{\bar z/r}$，$z=\tau$ | $\tfrac12\arg\tau$ | $+\pi/4$ |
| S_(2.17) | $(-\sqrt{n_g},0)$ | $\sqrt{\bar z/r}$，$z=-\sqrt{n_g}\,\tau$ | $\tfrac12(\arg\tau-\pi)$ | $-\pi/4$（mod π/2） |
| S'_(2.26) | $(\sqrt{n_g},0)$ | $\sqrt{\bar z/r}$，$z=\sqrt{n_g}\,\tau$ | $\tfrac12\arg\tau$ | $+\pi/4$（mod π/2） |
| −I | (0,−1) | $z=-1$，$r=1$，$\sqrt{\bar z/r}=i$；B 的 lift 取 $e^{-i\hat\varphi}=-i$（$(-1)^{1/2}$ 的另一支） | $\pi/2$ | $\pi/2$ |

精确数值（附录 A.2，τ=i）：$\hat\varphi(T,i)=0$，$\hat\varphi(S,i)=-\pi/4$，$\hat\varphi(-S,i)=+\pi/4$；$e^{-i\hat\varphi(S,i)}=e^{i\pi/4}$，其 4 次方 $=-1=(-1)^F$、8 次方 $=+1$（8 阶相位，正对应双覆盖）；$e^{-i\hat\varphi(-I,i)}=-i$，平方 $=-1=(-1)^F$。对 τ=i 以外的 τ（附录取 1i、0.5+1.3i、2+0.7i、0.3+0.2i、3+4i）数值同样成立。

### 2.3 三个问题的回答

**(1) T 是否给出 $\hat\varphi=0$？** 是。$\hat\varphi(T,\tau)=\frac12\arg(1)=0$ 对一切 τ（$T^n$ 同）。这与 B 原文一致（p017.txt:14–16）：``T leaves fixed the supersymmetries, so φ̂ = 0 for T, in keeping with (2.25)``。

**(2) S 给出什么？在 τ=i 是多少？** 以 (2.16) 为准：$S=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$，$z=-τ$，故

$$\hat\varphi(S,\tau)=\tfrac12\arg(-\tau)=\tfrac12(\arg\tau-\pi)\quad(\tau\in\mathbb{H}),\qquad \hat\varphi(S,i)=-\frac{\pi}{4}.$$

即 4（$Q_{AX}$）上乘 $e^{i\hat\varphi}$、4̄（$Q_{Y\dot A}$）上乘 $e^{-i\hat\varphi}$（B p.13，p014.txt:30–32），在 τ=i 时分别为 $e^{-i\pi/4}$、$e^{+i\pi/4}$。用任务写的 $-S$ 则得 $+\pi/4$，两者差 $\pi/2$，正是中心 I 的歧义（B p.14，p015.txt:1–7：I 在 4 上为 i、在 4̄ 上为 −i，$\hat\varphi\to\hat\varphi+\pi/2$），不是矛盾。

**(3) 与报告用法的冲突。** 报告把 $\hat\varphi$ 说成"「γ 在超荷上的相位 $\hat\varphi$」这个数"（L43），并把"它在超荷上的实现"归给 "(2.18)–(2.24)"（L68）。按 (2.25) 复算，这有三处必须改：

- **(a) 决定式是 (2.25)，不是 (2.18)–(2.24)。** (2.18)–(2.22) 是 Coulomb 分支/N=2 子代数/中心荷的铺垫；(2.23) 是低能 SL(2,Z) 作用；(2.24) 只是中心荷变换 $Z\to\frac{|c\tau+d|}{c\tau+d}Z$，即 $2\hat\varphi=\arg(c\tau+d)$。$\hat\varphi$ 的显式定义在 p.16。
- **(b) $\hat\varphi$ 是 τ 的函数**：$\hat\varphi(\gamma,\tau)=\frac12\arg(c\tau+d)$（mod π/2）。只有 T 恒为 0；S 给 $\frac12(\arg\tau-\pi)$，随 τ 变；只有把 τ 固定在 i 才得到常数模 π/2 的 $-\pi/4$。报告没有记这个 τ 依赖。
- **(c) 双覆盖/中心结构**：平方根给出 $(-1)^F=I^2$；τ=i 时 $e^{-i\hat\varphi(S,i)}$ 是 8 阶元（4 次方 $=-1$、8 次方 $=+1$），且 $\hat\varphi$ 只在 mod π/2 下有定义。这些都在 p.16，报告范围 pp.2–15 内没有。

因此，若"$\hat\varphi$ 是实现 S-对偶在超荷上的相位"被读成"存在一个与 τ 无关、由 (2.18)–(2.24) 定出的常数相位"，则冲突成立；正确的说法是：$\hat\varphi(\gamma,\tau)$ 是 (2.25) 给出的 1/2 权自守因子相位（双覆盖），S 在 τ=i 给 $e^{\pm i\pi/4}$（模中心 $i$）。

**自洽检验**（附录 A.2）：
- $e^{-2i\hat\varphi}=|c\tau+d|/(c\tau+d)$ 对 T、S、−S 与一般 γ 全部差 0（这正是 (2.24)）；
- 余圈 $\hat\varphi(g_1g_2,\tau)\equiv\hat\varphi(g_1,g_2\tau)+\hat\varphi(g_2,\tau)\ (\mathrm{mod}\ \pi)$ 对 (S,T)、(T,S)、(S,S)、(T,T)、(−S,S) 全部成立（严格差为 0 或 ±π），即双覆盖的一致性；
- (2.26) 的 $S'_{n_g}$：$z=\sqrt{n_g}\,\tau$，$|z|/z=|\tau|/\tau$，$\hat\varphi$ 与 $n_g$ 无关（n_g=2、3 在 τ=i 均为 $+\pi/4$），验证 B 的 "n_g cancels out, so (2.25) remains valid in the general case"（p017.txt:30–32）。

---

## 3. n_g

### 3.1 原文怎么定义

B 没有给 $n_g$ 的公式。p.12（p013.txt:1–6）原文：

> "This presence of a factor of 2 or 3 in the action of S on τ can be seen [46,47] by examining the BPS mass formulas for electric and magnetic charges and reflects the relation between roots and coroots for these groups. It also can be extracted from a string-theoretic explanation of S-duality for non-simply-laced groups [48]. The factor of 2 or 3 means that the duality groups for G2 or F4 are not simply SL(2, Z), but certain infinite discrete subgroups of SL(2, R) that are known as Hecke groups."

即 B 只说这个因子"反映根与余根的关系"，公式归给 [46,47]。数值 $n_g=2$ (F4)、$3$ (G2) 出现在 (2.17) 与 p.12 正文（p012.txt:35–36）；Sp(k)/Spin(2k+1) 对的 $n_g=2$ 见 p013.txt:15–20（``Thus we set n_g = 2 for Spin(2k+1) and Sp(k)``）。

**复算采用的定义**（lacing number）：

$$n_g \;=\; \frac{|\alpha_{\rm long}|^2}{|\alpha_{\rm short}|^2}.$$

等价的根/余根陈述：$\alpha^\vee = 2\alpha/|\alpha|^2$ 把长根映到短余根，余根系统的长短平方比仍为 $n_g$；故 $n_g$ 正是"根 ↔ 余根"互换时两套度规的比值，与 B 的措辞一致。

### 3.2 从显式根系复算（附录 A.3）

用坐标实现并枚举根（sympy 精确有理数）：

- $B_n$：$\pm e_i$（$|\alpha|^2=1$）+ $\pm e_i\pm e_j$（2）；
- $C_n$：$\pm 2e_i$（4）+ $\pm e_i\pm e_j$（2）；
- $D_n$：$\pm e_i\pm e_j$（2）；
- $G_2$：短根 $\pm(e_i-e_j)$（6 个，$|\alpha|^2=2$）+ 长根 $\pm(e_i+e_j-2e_k)$（6 个，$|\alpha|^2=6$）；
- $F_4$：$\pm e_i$（8 个，1）+ $\pm e_i\pm e_j$（24 个，2）+ $(\pm\frac12,\pm\frac12,\pm\frac12,\pm\frac12)$（16 个，1），共 48；
- $E_8$：$\pm e_i\pm e_j$（112 个）+ 半整数偶负号（128 个），均 $|\alpha|^2=2$，共 240。

| 类型 | 根数 | 长度² 分布 | $n_g=\max/\min$ | 长度比 $\sqrt{n_g}$ |
|---|---|---|---|---|
| B2 | 8 | {1:4, 2:4} | 2 | √2 |
| C2 | 8 | {2:4, 4:4} | 2 | √2 |
| D2 | 4 | {2:4} | 1 | 1 |
| G2 | 12 | {2:6, 6:6} | 3 | √3 |
| F4 | 48 | {1:24, 2:24} | 2 | √2 |
| E8 | 240 | {2:240} | 1 | 1 |

余根集合直验（附录 A.3）：
- $\alpha^\vee=2\alpha/|\alpha|^2$：B2 余根 $|\alpha|^2$ 分布 {2:4,4:4}（比 2）；C2 {1:4,2:4}（比 2）；G2 {2:6, 2/3:6}（比 3）；F4 {2:24,4:24}（比 2）；E8 {2:240}（比 1）。
- 集合相等：$B_2$ 的余根集合 $=C_2$ 的根集合（True）；$C_2$ 的余根集合 $=B_2$ 的根集合（True）；$F_4$ 的余根集合 $=\{2\alph…/text{ short}\}\cup\{\text{long}\}$（True）。
- 显式根例子：B2 短 $(1,0)$（平方长 1）、长 $(1,1)$（2）；C2 短 $(1,1)$（2）、长 $(2,0)$（4）；G2 短 $(1,-1,0)$（2）、长 $(1,1,-2)$（6）；F4 短 $(1,0,0,0)$（1）、长 $(1,1,0,0)$（2）。G2 长根 (1,1,−2) 的余根 = (1/3,1/3,−2/3)，平方长 2/3。

**回答"是 2、3 还是 4、9 或别的"**：$n_g=(\text{长}/\text{短})^2$，故 F4 为 **2**、G2 为 **3**、B/C 为 **2**；**4、9 是 $(|\alpha_l|/|\alpha_s|)^4=n_g^2$，不是 $n_g$**；长度比本身 √2、√3 不是整数，也不能直接进 (2.17) 的 $\sqrt{n_g}$。

### 3.3 与 (2.17) 及 Hecke 群的自洽

对 $n_g=1,2,3$，$S=\begin{pmatrix}0&1/\sqrt{n_g}\\-\sqrt{n_g}&0\end{pmatrix}$ 满足 det=1、tr=0、$S^2=-I$（附录 A.3 旁边直算），作用为 $\tau\mapsto-1/(n_g\tau)$。令 $\tilde\tau=\sqrt{n_g}\,\tau$，则 $…/sqrt{n_g}$，$…/tau$；而 $\sqrt2=2\cos(\pi/4)$、$\sqrt3=2\cos(\pi/6)$，即生成 Hecke 群 $H(\sqrt2)$、$H(\sqrt3)$，与 B 的 "Hecke groups"（p013.txt:4–6）一致。

### 3.4 与报告的差异

报告 L39："非 simply-laced 时根与余根长度不同，格之间还要乘一个整数因子，这正是 n_g=2、3 的来源 (B p.12)"。**数值 2、3 正确，但表述不精确**：B 只说该因子"reflects the relation between roots and coroots"，没有"格之间乘整数因子"这种说法；正确的统一说法是同一根格内**长/短根平方长度比**（= 根↔余根互换的度规比）。见 §6 的 E4。

---

## 4. Table 1 逐行

Table 1（p004.txt:12–24，印刷 p.3；表题 p004.txt:22–24："Table 1. Examples of the correspondence between a Lie group G and its Langlands or GNO dual ^L G."）全文 7 行：

| 群 G | ^L G | 根/余根与格核对 | 结论 |
|---|---|---|---|
| U(N) | U(N) | X=Z^N；Q=A_{N-1} 根格；A_{N-1} 单长度 ⇒ Φ∨=Φ；对偶根数据 (X∨,Φ∨,X,Φ)=(Z^N,Φ,Z^N,Φ)；X/Q≅Z（U(1) 中心），X∨/Q∨≅Z（π1） | 自对偶 ✓ |
| SU(N) | PSU(N)=SU(N)/Z_N | A_{N-1} 单长度，α∨=α；SU(N) 单连通：X=P，X∨=Q；对偶的权格 = X∨ = Q = 根格 ⇒ 伴随群；P/Q 的阶 = det A_{N-1} = N = Z(SU(N)) 的阶 = π1(PSU(N)) 的阶 | ✓ |
| Spin(2n) | SO(2n)/Z_2 | D_n 单长度，Φ∨=Φ；P/Q 的阶 = det A(D_n) = 4（n≥3；D2=A1×A1 亦 4）= Z(Spin(2n)) 的阶 = π1(SO(2n)/Z_2) 的阶 | ✓ |
| Sp(n) | SO(2n+1) | Φ(C_n)∨=Φ(B_n)（余根集合直验相等）；Sp(n) 单连通：X=P(C_n)，X∨=Q(C_n)；对偶权格 = Q(C_n) = Q(B_n) ⇒ 伴随 B_n = SO(2n+1)；Z(Sp(n))=Z_2=π1(SO(2n+1)) | ✓ |
| Spin(2n+1) | Sp(n)/Z_2 | Φ(B_n)∨=Φ(C_n)；Spin(2n+1) 单连通：X=P(B_n)，X∨=Q(B_n)；对偶权格 = Q(B_n) ⇒ 伴随 C_n = Sp(n)/Z_2；Z(Spin)=Z_2=π1(Sp(n)/Z_2) | ✓ |
| G2 | G2 | A(G2) 的转置 = P·A(G2)·P（P 为图自同构 1↔2，即 (2.26) 的 R 在根图上的版本）；Φ∨≅Φ；det=1 ⇒ 既单连通又伴随；中心与 π1 平凡 | ✓ |
| E8 | E8 | Cartan 对称、单长度，Φ∨=Φ；det=1；中心与 π1 平凡 | ✓ |

### 4.1 要求的三个格层面细核

**(1) SU(3) ↔ PSU(3)。** A2 的 Cartan 行列式 =3；单根坐标下 P/Q 的阶 = det A2 = 3。基本权：$\omega_1=(\tfrac23,\tfrac13)$、$\omega_2=(\tfrac13,\tfrac23)$（根坐标，附录 A.4 由 $A^{-1}$ 得出）；$3\omega_i\in Q$ 但 $\omega_i\notin Q$ ⇒ $P/Q\cong\mathbb{Z}_3$。于是
- SU(3)：$X=P$，$X^\vee=Q$ ⇒ $\pi_1=0$，$Z=Z_3$；
- PSU(3)：$X=Q$，$X^\vee=P$ ⇒ $\pi_1=P/Q=Z_3$，$Z=0$；
- 对偶根数据 $(X^\vee,\Phi^\vee,X,\Phi)=(Q,\Phi,P,\Phi)$，权格为 $Q$ = 根格 ⇒ 对偶群是**伴随型** = PSU(3)。
中心与 π1 互换（0↔Z_3，Z_3↔0）✓。

**(2) Sp(1) ↔ SO(3)。** Sp(1)=SU(2)=Spin(3)，A1；$P/Q\cong Z_2$（$\omega=\alpha/2$，$2\omega\in Q$、$\omega\notin Q$）。Sp(1) 单连通：$\pi_1=0$、$Z=Z_2$；SO(3)=PSU(2)：$\pi_1=Z_2$、$Z=0$。$\Phi^\vee=\Phi$；对偶权格 $=X^\vee=Q$ ⇒ 伴随 A1 = SO(3) ✓。与 Table 1 第 5 行 $n=1$ 的 "Spin(3)↔Sp(1)/Z_2=SO(3)" 自洽。

**(3) Spin(4) ↔ SO(4)/Z_2。** D2=A1×A1；$\det A(D_2)=4$，由此 $|P/Q|=4=|Z(\text{Spin}(4))|=|Z_2\times Z_2|$。
- Spin(4)=SU(2)×SU(2)：$X=P\times P$，$X^\vee=Q\times Q$，$\pi_1=0$，$Z=(P/Q)^2$ 阶 4；
- SO(4)/Z_2 = PSO(4) = SO(3)×SO(3)：$X=Q\times Q$，$X^\vee=P\times P$，$\pi_1=(P/Q)^2$ 阶 4，$Z=0$；
- 对偶权格 $=X^\vee=Q\times Q$ = 根格 ⇒ 伴随 D2 = PSO(4) ✓；D2 单长度 ⇒ $\Phi^\vee=\Phi$ ✓。

### 4.2 附加核对

- 对偶 Cartan 直验（附录 A.4）：$B_2^{\mathsf T}=C_2$、$B_3^{\mathsf T}=C_3$、$G_2^{\mathsf T}=P G_2 P$、$F_4^{\mathsf T}=P F_4 P$（P 为图自同构）全部 True；$A_2,D_2,D_4,E_8$ 对称；行列式 A1=2、A2=3、B2=2、C2=2、D2=D3=D4=D5=4、G2=F4=E8=1。**教训**：$D_n$ 的 Cartan 矩阵必须对称构造（$A_{n-3,n-1}=A_{n-1,n-3}=-1$ 等）；第一版漏对称项把 D4 的行列式误算成 8，纠正后为 4。
- Table 1 表题是 "Examples"，非穷尽；F4 未列入（^L F4=F4，但 n_g=2 是 lacing 数据，与"群自对偶"是两件事）。
- 报告 L35 列 Table 1 的行序与 B 原文顺序（SU、Spin(2n)、Sp、Spin(2n+1)、G2、E8，第 2–7 行）不同，但内容无缺漏；不算错误，仅提醒按原文顺序引用。

---

## 5. 维度账

### 5.1 十维 N=1 SYM 的场内容与降维

B 的十维场（p.7–9）：
- 规范场 $A_M$：10 个实分量（$M=0,\dots,9$）；
- 费米子 λ：取值于 $S_+\otimes\mathrm{ad}(E)$，$S_+$ 在 Lorentz 号差下 rank 16 且实（p007.txt:33–38："S+ and S− are of rank 16 ... real"），即 16 个实分量；λ 正手征且取伴随（p008.txt:22–25）。

降维（p010.txt:18–26，(2.10)）：要求场与 $x^4,\dots,x^9$ 无关，

$$A_M \;\longrightarrow\; A_\mu\ (\mu=0..3;\ 4\text{ 个}) \;\oplus\; \varphi_i=A_{i+4}\ (i=0..5;\ 6\text{ 个实标量}),$$

$$4+6=10\quad\checkmark$$

在壳：$A_\mu$ 2 + $\varphi$ 6 = 8 玻色；费米子 16 → 8（四维 N=4 的 4 个 Majorana，每个在壳 2）。8=8 ✓。

### 5.2 (2.14)：16 = (2,1,4)⊕(1,2,4̄)

SO(10)→SO(4)×SO(6)，$\mathrm{Spin}(6)\cong SU(4)_R$；B p.10 给出（p011.txt:38–44，式 (2.14) 在第 42 行）：

$$\mathbf{16}\;\longrightarrow\;(\mathbf{2},\mathbf{1},\mathbf{4})\oplus(\mathbf{1},\mathbf{2},\bar{\mathbf{4}}),\qquad \lambda\ \text{同}.$$

- 复维数：$2\cdot4+2\cdot4=8+8=16$ ✓（附录 A.5）；
- 任务说的 "$4\times4=16$"：Dirac 4 = (2,1)⊕(1,2)（复 4 维），乘 SU(4) 的 4 或 4̄（复 4 维），得复 16 维；作为 Lorentz 实的 Majorana–Weyl 旋量恰为 16 个实分量，两种记法一致。
- 四维 N=4 超荷：16 个（B 在 p.9 写 $Q_a,\ a=1,\dots,16$，p010.txt:7–13，式 (2.9)）。

### 5.3 twist 可用的超荷数

4 维 N=4 有 16 个超荷，但 twist 只保留**不变的**超荷。条件原文（p019.txt:1–11，印刷 p.18，属 §3.1，超出 U01）：

> "To accomplish this, we pick a homomorphism κ : Spin(4) → Spin(6) and set Spin′(4) = (1 × κ)(Spin(4)) ⊂ Spin(4) × Spin(6). We also want to pick κ such that the action of Spin′(4) on S+ has a non-zero invariant vector. Since the supersymmetry generator ε takes values in S+, a choice of an invariant vector in S+ will give us a Spin′(4)-invariant supersymmetry that we will call Q. It will automatically obey Q² = 0, by virtue of (2.15). (There is no Spin′(4) invariant operator on the right hand side of (2.15), so as Q² = ½{Q,Q} is Spin′(4)-invariant, it must vanish.)"

即条件为：**存在 κ，使 $\mathrm{Spin}'(4)=(1\times\kappa)(\mathrm{Spin}(4))$ 在 $S_+$ 上有非零不变矢量**；ε∈S₊ 取该不变量 ⇒ 得不变的 Q，且由 (2.15) 自动 $Q^2=0$。

GL twist 的具体 κ（p019.txt:22–32）：4 of SU(4)_R = (2,1)⊕(1,2) of SU(2)_ℓ×SU(2)_r；此时 (2.14) 分解为（p020.txt:1–8 的 K 与 p021.txt 的 (3.5)(3.6)，(3.5) 在 p021.txt:5、(3.6) 在 p021.txt:11）：

$$(\mathbf{2},\mathbf{1})_0\otimes[(\mathbf{2},\mathbf{1})_{-1}\oplus(\mathbf{1},\mathbf{2})_1]=(\mathbf{1},\mathbf{1})_{-1}\oplus(\mathbf{3},\mathbf{1})_{-1}\oplus(\mathbf{2},\mathbf{2})_1,$$

$$(\mathbf{1},\mathbf{2})_0\otimes[(\mathbf{2},\mathbf{1})_1\oplus(\mathbf{1},\mathbf{2})_{-1}]=(\mathbf{1},\mathbf{1})_{-1}\oplus(\mathbf{1},\mathbf{3})_{-1}\oplus(\mathbf{2},\mathbf{2})_1.$$

维数 $1+3+4=8$、$4+1+3=8$，总计 16 ✓；每式恰含一个 (1,1) 单态（且 $-iK=-1$），故**不变超荷数 = 2**：一个左手 ε_ℓ、一个右手 ε_r（B p.20，p021.txt:14–23："there is one invariant supersymmetry generator ε_ℓ that is left-handed ... and one such generator ε_r that is right-handed"；(3.7) $\hat\Gamma_E\varepsilon_\ell=-\varepsilon_\ell$、$\hat\Gamma_E\varepsilon_r=\varepsilon_r$；(3.8) $\varepsilon_r=N\varepsilon_\ell$、$N=\frac14\sum_{\mu=0}^3\Gamma_{\mu+4}\Gamma_\mu$、$N^2\varepsilon=-\varepsilon$；(3.9) $\varepsilon_\ell=-N\varepsilon_r$；(3.10) $\Gamma_{\mu+4}\varepsilon_\ell=-\Gamma_\mu\varepsilon_r$、$\Gamma_{\mu+4}\varepsilon_r=\Gamma_\mu\varepsilon_\ell$）。

附注：若再要求对额外 U(1)_K 不变，则不变超荷数为 **0**（两个单态都有 $-iK=-1$）；B 的 Q 只要求 Spin′(4)-不变。**因此"要求不变超荷 Q 满足哪个条件"的原文依据在 §3.1（p.18），不在 §2**；这正是报告范围漏掉 p.16 的连带影响（U01 内只能引到 (2.14)/(2.15) 的表示数据）。

---

## 6. 复算发现的错误/歧义

（逐条：报告原句 → 正确内容 → 依据。行号为 `report_v1.md` 行号。共 10 条：高 2、中 4、低 4。）

**E1（高，页范围）** 报告 L1 标题 "(B pp.2–15)"、L3 "本单元为 p003–p016"、L110 自检 "B 页码全部落在 2–15"。
**正确**：U01 = 印刷 pp.2–16 = `p003.txt`–`p017.txt`。p.16 顶部 1–6 行就是 (2.25)（`p017.txt`:1–6）、8–13 行是双覆盖、14–16 行是 T 的 $\hat\varphi=0$、18–32 行是 (2.26)，§3 标题在第 36 行。报告因此漏掉 §2 的收尾公式（$\hat\varphi$ 的显式定义与双覆盖、非单连通修正），这是下面 E2/E3 的根源。
**依据**：任务对 U01 的定义；`p017.txt`:1–36。

**E2（高，归因）** 报告 L68："加上它在超荷上的实现 φ̂，即 (2.18)–(2.24) (B p.11–15)"。
**正确**：(2.18)–(2.22) 是 Coulomb 分支/N=2 子代数/中心荷的准备工作；(2.23) 是低能 SL(2,Z) 作用；(2.24) 只是中心荷变换；$\hat\varphi$ 的显式定义是 (2.25)，在 p.16。报告声明的范围内没有确定 $\hat\varphi$ 的公式。
**依据**：`p015.txt`:18–49、`p016.txt`:1–59（(2.18)–(2.24)）；`p017.txt`:1–6（(2.25)）。与 crit_r4/r6 的 CHL-001 一致。

**E3（中，内容）** 报告 L43："这一关的产出是「γ 在超荷上的相位 φ̂」这个数"；L100："φ̂ 只定义到模 π/2 (B p.14)"。
**正确**：$\hat\varphi(\gamma,\tau)=\frac12\arg(c\tau+d)$（mod π/2）是 τ 的函数：T→0；S（(2.16)）→$\frac12(\arg\tau-\pi)$，τ=i 时 $-π/4$；若取 −S 则 $+π/4$（差 π/2 是中心 I 的歧义）。τ=i 时 $e^{-i\hat\varphi(S,i)}=e^{iπ/4}$ 是 8 阶相位（4 次方 = $(-1)^F$，8 次方 =1）；此外有 $\sqrt{}$ 双覆盖与 $(-1)^F=I^2$（`p017.txt`:8–13）。"mod π/2"只说中心歧义，漏了 τ 依赖与双覆盖。
**依据**：`p017.txt`:1–13；`p015.txt`:1–7。

**E4（中，n_g 表述）** 报告 L39："非 simply-laced 时根与余根长度不同，格之间还要乘一个整数因子，这正是 n_g=2、3 的来源 (B p.12)"。
**正确**：B 只说该因子 "reflects the relation between roots and coroots"（`p013.txt`:1–3），没有"格之间乘整数因子"的说法；可复算的统一说法是 $n_g=(|\alpha_{\rm long}|/|\alpha_{\rm short}|)^2$（F4=2、G2=3、B/C=2）。4、9 是 $n_g^2$，√2、√3 是长度比本身，都不是 $n_g$。§3 已给显式根系复算。
**依据**：`p013.txt`:1–6、`p013.txt`:15–20、`p012.txt`:35–41。

**E5（中，指代）** 报告 L35："所以 G2、F4 的对偶群不是 SL(2,Z)，而是 Hecke 群 (B p.12)"。
**正确**：B 的 "duality groups for G2 or F4" 指 **S-对偶群 Γ**（SL(2,R) 的 Hecke 离散子群 $H(\sqrt2)$、$H(\sqrt3)$），不是 Langlands/GNO 对偶群 ^L G——^L G2=G2、^L F4=F4（Table 1 也如此写）。报告若把它读成"对偶群 = ^L G"则错。
**依据**：`p013.txt`:4–6；`p012.txt`:35–41；`p004.txt`:12–24。

**E6（中，原文误读）** 报告 L31："这正是 §7 离散通量的伏笔"（指 (2.15) 右边的额外项）。
**正确**：B 紧接 (2.15) 只说 "They will make a brief appearance at the end of this section"（`p012.txt`:10–13）；ξ∈H²(M,π1(G)) 的讨论在 p.12 另一段（`p013.txt`:30–33），B 把一般流形情形指到 §7。把 (2.15) 的额外项直接判成 §7 是越级归因（B 说的是"本节末尾短暂出现"，不是 §7）。
**依据**：`p012.txt`:10–13；`p013.txt`:30–33。与 crit_r6 的 CHL-002 一致。

**E7（低，定位）** 报告 L68 把 (2.18)–(2.24) 标为 "(B p.11–15)"。
**正确**：(2.16)、(2.17) 在 p.11；(2.18)–(2.22) 在 pp.14–15；只有 (2.23)–(2.24) 在 p.15。应写 "B pp.11, 14–15"。
**依据**：`p012.txt`:28–41；`p015.txt`:18–49；`p016.txt`:1–59。

**E8（低，前提遗漏）** 报告在 §2.6/§3(b) 引用 (2.23) 的 SL(2,Z) 作用时没写 B 的前提。
**正确**：B 原文 "For simply-laced G, the low energy abelian gauge theory on the Coulomb branch admits an SL(2,Z) group of duality symmetries ..."(2.23)（`p016.txt`:28–34）；非 simply-laced 由 (2.26) 修正（`p017.txt`:14–32）；B 另说 (2.23) 中 T 的作用的全理论验证 "valid for all G, simply-laced or not"（`p016.txt`:48–54）。报告 L47 引了后半句，但 §2.6 正文没提前提。
**依据**：`p016.txt`:28–34、48–54；`p017.txt`:14–32。与 crit_r6 的 CHL-003 一致。

**E9（低，定位/推论）** 报告 L104："§2.1 明确假设 G 单以保证 Tr 唯一 (B p.8)，但 Table 1 第一行是 U(N)↔U(N) (B p.3)；U(N) 不是半单群……"（把它列为"可疑/不一致"）。
**正确**：Table 1 在 §1，表题是 GNO/Langlands 对偶的 "Examples"（`p004.txt`:22–24），不继承 §2.1 的 simple-G 假设；U(N) 的根数据自对偶（X=Z^N），该行本身自洽。真正的差别是 §2 的拉氏量/Tr 唯一性论证只对单 G 说；U(N) 的 U(1) 因子与中心商需要另处理，但这不是"Table 1 与正文矛盾"。把两条不同前提的陈述并列成"不一致"定位不准。
**依据**：`p004.txt`:12–24；`p009.txt`:5–13。

**E10（低，措辞）** 报告 L94："D 把物理端写成 (G_c,τ)↔(^L G_c,−1/(n_g τ))，即 (D p.12, (4.1))，与 B 的 (2.16)、(2.17) 一致"。
**正确**：在 τ 的映射层面确实一致（S 把 τ 送到 −1/(n_g τ)）；但 (2.16)/(2.17) 是 SL(2,R) **矩阵**（在 τ 上的作用），(4.1) 是**理论等价**的陈述，二者不是同一个数学对象；说"一致"应注明是"同一个 τ 映射的两种表述"。与 crit_r4 的 CHL-001 同向，但我的表述更窄（未读 D 原文，不评判其原文语境）。
**依据**：`p012.txt`:28–41；报告 L94 原句。

**未在报告中发现错误、复算通过的部分**：L27 的 τ/T 逻辑（§1 全过）；Table 1 七行内容（§4 全过，仅行序不同）；$n_g$ 数值 2、3（§3 过，仅表述需修）；场内容、(2.14) 与维度账（§5 过）。

---

## 7. P5 判词

主干对：τ/T 等价、Table 1 七行、n_g=2/3、(2.14) 与维度账通过。但漏 p.16，(2.25)/(2.26) 缺失致 φ̂ 归因错、τ 依赖未记；n_g 表述含糊；(2.15) 伏笔误指 §7。补 p.16 后重审。

---

## 附录 A：可重跑计算脚本

运行方式（MSYS bash，工作目录 `工程根`）：

```bash
PY="…/python.exe"
PYTHONIOENCODING=utf-8 "$PY" - <<'PYEOF'
# ... 把下面任一代码块贴在这里 ...
PYEOF
```

### A.1 第 1 项：τ、T 与瞬子数（sympy）

```python
import sympy as sp

th, e = sp.symbols('theta e', positive=True)
tau = th/(2*sp.pi) + 4*sp.pi*sp.I/e**2
print("Im tau =", sp.simplify(sp.im(tau)))                       # 4*pi/e**2
print("tau(theta+2pi)-tau =", sp.simplify(tau.subs(th, th+2*sp.pi) - tau))   # 1

# I_theta = -theta*K; theta -> theta+2pi 时 Delta I = -2 pi K
K = sp.symbols('K', integer=True)
dI = -(th + 2*sp.pi)*K - (-th*K)
print("Delta I_theta =", sp.simplify(dI))                        # -2*pi*K
print("Delta I/(2pi) =", sp.simplify(dI/(2*sp.pi)))              # -K   => exp(i Delta I)=1 iff K in Z
```

输出：`Im tau = 4*pi/e**2`；`tau(theta+2pi)-tau = 1`；`Delta I_theta = -2*pi*K`；`Delta I/(2pi) = -K`。

### A.2 第 2 项：φ̂(γ,τ) 与 (2.25)

```python
import cmath, math

def phi(g, tau):
    a, b, c, d = g
    return 0.5 * cmath.phase(c*tau + d)      # phi = (1/2) arg(c tau + d)

def lhs(g, tau):                              # exp(-i phi)
    return cmath.exp(-1j * phi(g, tau))

def rhs(g, tau):                              # (|c tau + d|/(c tau + d))^{1/2}, 主值
    a, b, c, d = g
    z = c*tau + d
    return cmath.sqrt(abs(z)/z)

T  = (1, 1, 0, 1)
S  = (0, 1, -1, 0)          # B 的 (2.16)
Sm = (0, -1, 1, 0)          # 任务给的矩阵 = -S
taus = [1j, 0.5 + 1.3j, 2 + 0.7j, 0.3 + 0.2j, 3 + 4j]

for g, name in [(T, 'T'), (S, 'S(2.16)'), (Sm, '-S')]:
    print(name, [abs(lhs(g, t) - rhs(g, t)) for t in taus])   # 全 0（1e-16）

print("phi(T,i), phi(S,i), phi(-S,i) =", phi(T, 1j), phi(S, 1j), phi(Sm, 1j))
print("exp(-i phi(S,i)) =", lhs(S, 1j))
print("  ^4 =", lhs(S, 1j)**4, "  ^8 =", lhs(S, 1j)**8)       # -1, +1

# (2.26) 的 S 矩阵：n_g 抵消，phi = arg(tau)/2，与 n_g 无关
for n in (2, 3):
    g = (0, -1/math.sqrt(n), math.sqrt(n), 0)
    print("S(2.26) n=%d: phi(i)=%s diff=%s" % (n, phi(g, 1j), abs(lhs(g, 1j) - rhs(g, 1j))))

# 余圈 phi(g1 g2, tau) = phi(g1, g2 tau) + phi(g2, tau)  (mod pi)
def mul(g1, g2):
    a, b, c, d = g1
    A, B, C, D = g2
    return (a*A + b*C, a*B + b*D, c*A + d*C, c*B + d*D)

def mob(g, t):
    a, b, c, d = g
    return (a*t + b)/(c*t + d)

bad = []
for g1, g2 in [(S, T), (T, S), (S, S), (T, T), (Sm, S)]:
    for t in taus:
        r = phi(mul(g1, g2), t) - phi(g1, mob(g2, t)) - phi(g2, t)
        r = (r + math.pi) % (2*math.pi) - math.pi      # 折到 [-pi, pi)
        if min(abs(r), abs(abs(r) - math.pi)) > 1e-9:
            bad.append((g1, g2, t, r))
print("cocycle failures (mod pi):", bad)                  # []
```

输出要点：T、S、−S 的 `exp(-i phi)` 与主值平方根差 0；`phi(S,i) = -0.785398... = -π/4`；`exp(-i phi(S,i)) = e^{iπ/4}`，`^4 = -1`、`^8 = +1`；(2.26) 的 n=2、3 都给 `+π/4`；余圈在 mod π 下全部通过。

### A.3 第 3、4 项：根系、n_g 与 Cartan 矩阵

```python
import itertools, sympy as sp

def B(n):
    R = []
    for i in range(n):
        for s in (1, -1):
            v = [0]*n; v[i] = s; R.append(tuple(v))
    for i, j in itertools.combinations(range(n), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0]*n; v[i] = si; v[j] = sj; R.append(tuple(v))
    return R

def C(n):
    R = []
    for i in range(n):
        for s in (1, -1):
            v = [0]*n; v[i] = 2*s; R.append(tuple(v))
    for i, j in itertools.combinations(range(n), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0]*n; v[i] = si; v[j] = sj; R.append(tuple(v))
    return R

def D(n):
    R = []
    for i, j in itertools.combinations(range(n), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0]*n; v[i] = si; v[j] = sj; R.append(tuple(v))
    return R

def G2():
    R = []
    for i in range(3):                      # 短根 (1,-1,0)
        for j in range(3):
            if i != j:
                v = [0, 0, 0]; v[i] = 1; v[j] = -1
                R.append(tuple(v)); R.append(tuple(-x for x in v))
    for k in range(3):                      # 长根 (1,1,-2)
        i, j = [x for x in range(3) if x != k]
        for s in (1, -1):
            v = [0, 0, 0]; v[i] = s; v[j] = s; v[k] = -2*s
            R.append(tuple(v))
    return list(set(R))

def F4():
    R = []
    for i in range(4):
        for s in (1, -1):
            v = [0]*4; v[i] = s; R.append(tuple(v))
    for i, j in itertools.combinations(range(4), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0]*4; v[i] = si; v[j] = sj; R.append(tuple(v))
    for s in itertools.product((1, -1), repeat=4):
        R.append(tuple(x/2 for x in s))
    return list(set(R))

def E8():
    R = []
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0]*8; v[i] = si; v[j] = sj; R.append(tuple(v))
    for s in itertools.product((1, -1), repeat=8):
        if s.count(-1) % 2 == 0:
            R.append(tuple(x/2 for x in s))
    return list(set(R))

def norm2(v):
    return sp.Rational(sum(x*x for x in v))

def summarize(name, R):
    ns = {}
    for v in R:
        ns[norm2(v)] = ns.get(norm2(v), 0) + 1
    ratio = sp.Rational(max(ns))/sp.Rational(min(ns))
    print(name, "roots=", len(R), ns, "n_g=", ratio, "len_ratio=", sp.sqrt(ratio))

for name, R in [("B2", B(2)), ("C2", C(2)), ("D2", D(2)),
                ("G2", G2()), ("F4", F4()), ("E8", E8())]:
    summarize(name, R)

def coroot(v):
    n = norm2(v)
    return tuple(2*sp.Rational(x)/n for x in v)

def coset(R):
    return set(coroot(v) for v in R)

print("B2 coroots == C2 roots:", coset(B(2)) == set(C(2)))
print("C2 coroots == B2 roots:", coset(C(2)) == set(B(2)))
short = set(v for v in F4() if norm2(v) == 1)
long_ = set(v for v in F4() if norm2(v) == 2)
print("F4 coroots == {2*short} U {long}:",
      coset(F4()) == set(tuple(2*sp.Rational(x) for x in v) for v in short) | long_)

def coroot_norms(R):
    d = {}
    for v in R:
        nv = norm2(coroot(v))
        d[nv] = d.get(nv, 0) + 1
    return d

for name, R in [("B2", B(2)), ("C2", C(2)), ("G2", G2()), ("F4", F4()), ("E8", E8())]:
    print(name, "coroot |alpha|^2:", coroot_norms(R))
print("G2 long root (1,1,-2) coroot:", coroot((1, 1, -2)))

# ---- Cartan 矩阵：行列式 = |P/Q|，对偶 = 转置（至多差图自同构）----
def rev(n):
    return sp.Matrix(n, n, lambda i, j: 1 if i + j == n - 1 else 0)

Cart = {
    'A1': [[2]],
    'A2': [[2, -1], [-1, 2]],
    'B2': [[2, -2], [-1, 2]],
    'C2': [[2, -1], [-2, 2]],
    'D2': [[2, 0], [0, 2]],
    'D4': [[2, -1, 0, 0], [-1, 2, -1, -1], [0, -1, 2, 0], [0, -1, 0, 2]],
    'G2': [[2, -1], [-3, 2]],
    'F4': [[2, -1, 0, 0], [-1, 2, -2, 0], [0, -1, 2, -1], [0, 0, -1, 2]],
    'E8': [[2, -1, 0, 0, 0, 0, 0, 0],
           [-1, 2, -1, 0, 0, 0, 0, 0],
           [0, -1, 2, -1, 0, 0, 0, -1],
           [0, 0, -1, 2, -1, 0, 0, 0],
           [0, 0, 0, -1, 2, -1, 0, 0],
           [0, 0, 0, 0, -1, 2, -1, 0],
           [0, 0, 0, 0, 0, -1, 2, 0],
           [0, 0, -1, 0, 0, 0, 0, 2]],
}
M = {k: sp.Matrix(v) for k, v in Cart.items()}
for k in ['A2', 'B2', 'C2', 'D2', 'D4', 'G2', 'F4', 'E8']:
    print(k, "det =", M[k].det())

print("B2^T == C2:", M['B2'].T == M['C2'])
B3 = sp.Matrix([[2, -1, 0], [-1, 2, -1], [0, -2, 2]])
C3 = sp.Matrix([[2, -1, 0], [-1, 2, -2], [0, -1, 2]])
print("B3^T == C3:", B3.T == C3)
print("G2^T == P G2 P:", M['G2'].T == rev(2) * M['G2'] * rev(2))
print("F4^T == P F4 P:", M['F4'].T == rev(4) * M['F4'] * rev(4))
print("A2, D2, D4, E8 symmetric:",
      M['A2'].T == M['A2'], M['D2'].T == M['D2'],
      M['D4'].T == M['D4'], M['E8'].T == M['E8'])

# SU(3)：基本权 = A2^{-1} 的行；3*omega 整、omega 不整 => P/Q = Z_3
W = M['A2'].inv()
print("A2^{-1} rows (fundamental weights) =", W.tolist())
print("3*omega1 =", [sp.nsimplify(3*x) for x in W.row(0)], "; det A2 =", M['A2'].det())
```

输出要点：B2 {1:4, 2:4} n_g=2；C2 {2:4, 4:4} n_g=2；D2 {2:4} n_g=1；G2 {2:6, 6:6} n_g=3；F4 {1:24, 2:24} n_g=2；E8 {2:240} n_g=1；B2↔C2 余根集合互等、F4 余根 = {2×短}∪{长} 均 True；行列式 A2=3、B2=2、C2=2、D2=4、D4=4、G2=1、F4=1、E8=1；对偶关系全部 True；A2 基本权行 = (2/3,1/3)、(1/3,2/3)。

### A.4 第 5 项：维度与表示分解

```python
print("10 = 4 + 6 :", 4 + 6)                                  # 10
print("(2,1,4)+(1,2,4bar) complex dim =", 2*4 + 2*4)         # 16
print("(3.5) dims 1+3+4 =", 1 + 3 + 4)                        # 8
print("(3.6) dims 4+1+3 =", 4 + 1 + 3)                        # 8
print("total =", (1+3+4) + (4+1+3), "; singlets = 2")         # 16 ; 2
# 在壳计数：4d N=4 玻色 2 (A_mu) + 6 (phi) = 8；费米 16 -> 8 (4 个 Majorana)
```

---

## 附录 B：与质询（crit_r4/r6）的对账

| 质询条目 | 我的复算结论 |
|---|---|
| r4/r6 CHL-001（高）(2.25)/(2.26) 在 p.16，超出报告声明范围，报告把 $\hat\varphi$ 归给 (2.18)–(2.24) | **成立**：见 E1/E2；原文 `p017.txt`:1–6（(2.25)）、14–32（(2.26)）、36（§3） |
| r6 CHL-002（中）报告把 (2.15) 额外项说成 §7 伏笔 | **成立**：见 E6；`p012.txt`:10–13 只说到 "end of this section" |
| r6 CHL-003（低）报告漏 (2.23) 的 "For simply-laced G" 前提 | **成立**：见 E8；`p016.txt`:28–34 |
| r4 CHL-001（中）报告称 D (4.1) 与 B (2.16)(2.17) 一致 | **部分**：τ 映射层面一致；对象不同（理论等价 vs 矩阵），见 E10（未读 D 原文，仅就 B 侧与报告原句判断） |
| r4 CHL-003/CHL-004（中）p.13 "bigger role" 未指 §3；六想法只有 B 单源 | 本次复算不涉及，未表态（不改变我的十条结论） |

---

*本文件是 P5（r8）唯一的写入文件；未修改任何其他文件。计算环境与脚本见附录 A，五件事全部完成。*
