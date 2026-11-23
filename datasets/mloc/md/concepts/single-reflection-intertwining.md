# 单反射的交织函子 $I_{s_\alpha}$：显式公式

> `mloc/concept/single-reflection-intertwining` · type=concept · track=E · status=draft · verification=source-only

**别名**：$I_{s_\alpha}$ 的显式公式、单反射交织函子、定理 8.3、three-term complex

## 摘要

整数点 $p=-\check{\alpha}(\lambda)$ 处，$I_{s_\alpha}$ 由 $Y_\alpha$ 上扭层 $L$ 的三项复形 $U^{-1},U^0,U^1$ 算出。

## 问题

对单反射 $s_\alpha$，$I_{s_\alpha}(V)$ 能写成什么样的三项复形；$V$ 不可约时它又只剩哪两种可能形态？

## 定义

取 $Y_\alpha=X\times_{X_\alpha}X$，$q_1,q_2$ 为两投影，$p_\alpha:X\to X_\alpha$ 为 $\alpha$ 型抛物子代数簇的投影（纤维 $\cong\mathbb{P}^1$，ch03c.tex:182-185）。$Y_\alpha=Z_1\cup Z_{s_\alpha}$，其中 $Z_1$ 是对角、闭，$Z_{s_\alpha}$ 稠密开且仿射嵌入 $Y_\alpha$（§3.8，ch03f.tex:146-154）。设 $p=-\check{\alpha}(\lambda)\in\mathbb{Z}$，则引理 8.2 给 $(D_{s_\alpha\lambda})_{q_1}=((D_\lambda)_{q_2})_L$，其中 $L=q_1^*(\mathcal{O}((-p+1)s_\alpha\rho+\alpha))\otimes_{\mathcal{O}_{Y_\alpha}}q_2^*(\mathcal{O}((-p+1)\rho))^{-1}$。令 $U^j(V)=R^jq_{1+}(q_2^+(V)\otimes_{\mathcal{O}_{Y_\alpha}}L)$；因 $q_1$ 的纤维是一维的，$j\notin\{-1,0,1\}$ 时 $U^j=0$（ch03f.tex:183-185）。定理 8.3：$U^{-1}(V)=L^{-1}I_{s_\alpha}(V)$，且有 $D_{s_\alpha\lambda}$-模的正合列 $0\to U^0(V)\to I_{s_\alpha}(V)\to V(p\alpha)\to U^1(V)\to0$。

记号：$\alpha\in\Pi$ 为单根，$s_\alpha$ 为对应的单反射（§3.8，ch03f.tex:131-134），$\check{\alpha}$ 为余根；$p=-\check{\alpha}(\lambda)$ 必须为整数，否则 $I_{s_\alpha}$ 已是范畴等价（推论 3.22）。$V(p\alpha)$ 是几何平移 $V\otimes\mathcal{O}(p\alpha)$（§2.2），其出现源于 $i_1^*(L)=\mathcal{O}(p\alpha)$（ch03f.tex:203）。$T_{s_\alpha}=p_1^*(\mathcal{O}(\alpha))$ 是 §3.3 的一般扭层（ch03f.tex:195），满足 $L|_{Z_{s_\alpha}}=T_{s_\alpha}$。$D_\lambda=D_{X,\lambda+\rho}$ 按 §2.1 约定。

## 要点

- 全部显式公式只在 $p=-\check{\alpha}(\lambda)\in\mathbb{Z}$ 时成立；若 $\check{\alpha}(\lambda)\notin\mathbb{Z}$，$I_{s_\alpha}$ 已是 $\mathcal{M}_{qc}(D_\lambda)\simeq\mathcal{M}_{qc}(D_{s_\alpha\lambda})$ 的等价（推论 3.22），既不需要也不存在这样的三项复形。
- 关键几何事实是 $Y_\alpha=Z_1\cup Z_{s_\alpha}$：取附着于 $Z_1$ 的特异三角，把 $I_{s_\alpha}$ 拆成「沿对角的部分」与「$\mathbb{P}^1$-纤维上的部分」，这两块分别给出 $V(p\alpha)[-1]$ 与 $LI_{s_\alpha}(D(V))$。
- 在开轨道上 $L|_{Z_{s_\alpha}}=p_1^*(\mathcal{O}(\alpha))=T_{s_\alpha}$，故该部分就是 §3.3 定义的一般交织函子按 $T_{s_\alpha}$ 作用的结果；这正是显式公式与一般定义相容的方式。
- 定理 8.4：$V$ 不可约时只有两型——(i) $U^{-1}(V)=U^1(V)=V(p\alpha)$ 且 $U^0(V)=0$，此时 $I_{s_\alpha}(V)=0$、$L^{-1}I_{s_\alpha}(V)=V(p\alpha)$；(ii) $U^{-1}(V)=U^1(V)=0$，此时 $L^{-1}I_{s_\alpha}(V)=0$ 且 $0\to U^0(V)\to I_{s_\alpha}(V)\to V(p\alpha)\to0$ 正合。
- 在两型中都出现 $V(p\alpha)$ 的平移：这说明单反射在「整数点」处不是等价，而带着一个确定的平移缺陷；缺陷由 $p=-\check{\alpha}(\lambda)$ 度量。
- 命题 8.6：$V$ 不可约时，$I_{s_\alpha}(V)=0$ 当且仅当 $V$ 是形如 $p_\alpha^+(U)$ 的模的几何平移；引理 8.5 给这个方向的具体计算：$I_{s_\alpha}(p_\alpha^+(U))=0$、$L^{-1}I_{s_\alpha}(p_\alpha^+(U))=V(\alpha)$。

## 公式

$$$Y_\alpha=X\times_{X_\alpha}X,\qquad Y_\alpha=Z_1\cup Z_{s_\alpha}$$$

$$$(D_{s_\alpha\lambda})_{q_1}=((D_\lambda)_{q_2})_L,\qquad L=q_1^*\bigl(\mathcal{O}((-p+1)s_\alpha\rho+\alpha)\bigr)\otimes_{\mathcal{O}_{Y_\alpha}}q_2^*\bigl(\mathcal{O}((-p+1)\rho)\bigr)^{-1}$$$

$$$U^j(V)=R^jq_{1+}\bigl(q_2^+(V)\otimes_{\mathcal{O}_{Y_\alpha}}L\bigr),\qquad U^j=0\ \ (j\notin\{-1,0,1\})$$$

$$$0\longrightarrow U^0(V)\longrightarrow I_{s_\alpha}(V)\longrightarrow V(p\alpha)\longrightarrow U^1(V)\longrightarrow0,\qquad U^{-1}(V)=L^{-1}I_{s_\alpha}(V)$$$

$$$L|_{Z_{s_\alpha}}=p_1^*(\mathcal{O}(\alpha))=T_{s_\alpha},\qquad i_1^*(L)=\mathcal{O}(p\alpha)$$$

## 相关定理

### 定理 8.3：单反射的三项复形

设 $p=-\check{\alpha}(\lambda)$ 为整数，$V\in\mathcal{M}_{qc}(D_\lambda)$。则 (i) $U^{-1}(V)=L^{-1}I_{s_\alpha}(V)$；(ii) 有 $D_{s_\alpha\lambda}$-模正合列 $0\to U^0(V)\to I_{s_\alpha}(V)\to V(p\alpha)\to U^1(V)\to0$。

证明状态：`complete`

1. 由引理 8.2 把 $(D_\lambda)_{q_2}$ 的 $L$-扭等同于 $(D_{s_\alpha\lambda})_{q_1}$，于是 $U^j(V)=R^jq_{1+}(q_2^+V\otimes L)$ 是 $D_{s_\alpha\lambda}$-模。
   - 为什么：$L$ 的选取使 $q_1$ 侧的 $D$-模结构正好是 $D_{s_\alpha\lambda}$，这一步是整个公式的合法性前提。
2. 对 $W^\bullet=D(q_2^+V\otimes L)$ 取附着于闭子簇 $Z_1$ 的特异三角 $\Gamma_{[Z_1]}(W^\bullet)\to W^\bullet\to i_{\alpha*}(W^\bullet|_{Z_{s_\alpha}})\to\Gamma_{[Z_1]}(W^\bullet)[1]$。
   - 为什么：开闭分解 $Y_\alpha=Z_1\sqcup Z_{s_\alpha}$ 给出的标准特异三角，是分离两块贡献的唯一工具。
3. 由 $L|_{Z_{s_\alpha}}=T_{s_\alpha}$ 得 $Rq_{1+}(i_{\alpha*}(W^\bullet|_{Z_{s_\alpha}}))=LI_{s_\alpha}(D(V))$；由 $R\Gamma_{[Z_1]}(W^\bullet)=Ri_{1+}(Li_1^+(W^\bullet)[-1])$ 与 $i_1^*(L)=\mathcal{O}(p\alpha)$ 得 $Rq_{1+}(\Gamma_{[Z_1]}(W^\bullet))=D(V(p\alpha)[-1])$。
   - 为什么：两块分别落在开轨道（回到 §3.3 的 $T_{s_\alpha}$）与对角（沿 $i_1$ 的逆像，权为 $p\alpha$）上。
4. 对特异三角取上同调长正合列，逐项读出 $U^{-1},U^0,U^1$ 与 $V(p\alpha)$ 的位置，得 (i) 与 (ii)。
   - 为什么：长正合列中只有三个相邻次数可能非零（$q_1$ 纤维一维），故读出的正是那条四项正合列。

### 定理 8.4：不可约模的两型

设 $p=-\check{\alpha}(\lambda)$ 为整数，$V$ 是不可约 $D_\lambda$-模。则或 (i) $U^{-1}(V)=U^1(V)=V(p\alpha)$ 且 $U^0(V)=0$，此时 $I_{s_\alpha}(V)=0$、$L^{-1}I_{s_\alpha}(V)=V(p\alpha)$；或 (ii) $U^{-1}(V)=U^1(V)=0$，此时 $L^{-1}I_{s_\alpha}(V)=0$ 且 $0\to U^0(V)\to I_{s_\alpha}(V)\to V(p\alpha)\to0$ 正合。并且 $U^0(V)$ 是 $I_{s_\alpha}(V)$ 的最大真拟凝聚子模。

证明状态：`sketch`

1. 若 $U^{-1}(V)\ne0$，由定理 8.3 得 $L^{-1}I_{s_\alpha}(V)\ne0$；再由引理 5.6，$I_{s_\alpha}(V)=0$ 且 $L^{-1}I_{s_\alpha}(V)=V(p\alpha)$。再用 8.3 得 $U^0(V)=0$、$U^1(V)=V(p\alpha)$，即情形 (i)。
   - 为什么：5.6 断言不可约模在单反射下的两种可能，其中一种正是「$L^{-1}$ 非零则整体消没」。
2. 若 $U^{-1}(V)=0$，由 8.3 得 $L^{-1}I_{s_\alpha}(V)=0$；再由 5.6 知 $I_{s_\alpha}(V)\ne0$。
   - 为什么：此时落在 5.6 的另一型上，交织函子非零。
3. 反设 $U^1(V)\ne0$，则 $U^1(V)=V(p\alpha)$（$V$ 不可约）。用引理 8.5 与基变换证明这迫使 $I_{s_\alpha}(V)=0$，矛盾。
   - 为什么：8.5 说「$p_\alpha^+(U)$ 型」的模在单反射下整体消没；$\mathbb{P}^1$-纤维上的非零 $U^1$ 恰好把 $V$ 逼成这种型。
4. 故 $U^1(V)=0$，得情形 (ii)；$U^0(V)$ 的最大性由 5.7 与基变换给出。
   - 为什么：5.7 已把「无截面最大子模」刻画为核，与 8.3 的 $U^0$ 一致。

> 缺口：第 3 步依赖引理 8.5 与图表 (ch03f.tex:249-263) 上的基变换计算；底本此处把 §5 条目误引作 4.6/4.7（annote ch03f.tex:259-261 已改为 5.6/5.7），本卡未逐行复核基变换。

### 命题 8.6：$I_{s_\alpha}(V)=0$ 的刻画

设 $p=-\check{\alpha}(\lambda)\in\mathbb{Z}$，$V$ 不可约。则以下等价：(i) $I_{s_\alpha}(V)=0$；(ii) $V$ 是形如 $p_\alpha^+(U)$ 的模的几何平移。

证明状态：`sketch`

1. (ii)$\Rightarrow$(i)：设 $V=p_\alpha^+(U)(\nu)$；由引理 8.5，$I_{s_\alpha}(p_\alpha^+(U))=0$，再由几何平移与引理 3.5 得 $I_{s_\alpha}(V)=0$。
   - 为什么：平移只把权按 $w$ 搬运，不改变消没性。
2. (i)$\Rightarrow$(ii)：由定理 8.4，$I_{s_\alpha}(V)=0$ 落在情形 (i)，故 $U^{-1}(V)=V(p\alpha)$ 非零；沿着 $\mathbb{P}^1$-纤维把 $V$ 沿 $p_\alpha$ 下降，得 $U$ 使 $V=p_\alpha^+(U)$ 的平移。
   - 为什么：8.4(i) 中 $U^{-1}$ 与 $U^1$ 同时等于 $V(p\alpha)$，这种「两端相等」正是沿 $\mathbb{P}^1$-纤维常值、可下降到 $X_\alpha$ 的判据。

> 缺口：第 2 步的「沿纤维下降」用的是 $p_\alpha$ 的 $\mathbb{P}^1$-纤维化与 Kashiwara 等价（ch03f.tex:249-263 的图表），本卡未复核该下降的完整论证。

## 易错点

- 扭层 $L$ 里出现的是 $(-p+1)$，不是 $(p+1)$：底本此处下标与参数印错，译本 annote（ch03f.tex:170-172，底本 p.72）已改；照抄底本会得到错误的 $D_{s_\alpha\lambda}$-结构。
- 定理 8.3 的 $U^1(V)$ 一般不消失：$I_{s_\alpha}$ 有 $U^{-1},U^0,U^1$ 三段，只有 $V$ 不可约（8.4）时才塌成两型；把 8.3 当成短正合列是常见错误。
- $I_{s_\alpha}$ 的显式公式与 §3.3 的一般定义（$R^0p_{1+}(T_w\otimes p_2^+)$）不是同一个复形：前者用 $X_\alpha$-纤维化上的 $L$，后者用 $Z_{s_\alpha}$ 上的 $T_{s_\alpha}$；两者只在 $0$ 次上同调一致，高阶项由 8.3 给出。
- 前提 $p=-\check{\alpha}(\lambda)\in\mathbb{Z}$ 不能漏：$\check{\alpha}(\lambda)\notin\mathbb{Z}$ 时 $I_{s_\alpha}$ 是等价（推论 3.22），套用三项复形会得到错误的消没结论。

## 相关卡

- `mloc/concept/intertwining-functor-i-w`
- `mloc/concept/iw-exactness`
- `mloc/concept/irreducible-d-lambda-sections`
- `mloc/concept/support-and-n-homology`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.8 $Y_\alpha$、扭层 $L$ 与 $U^j$ · p.[72]（PDF [76]） · `源码/chapters/ch03f.tex:146-204（$Y_\alpha$、引理 8.2、$U^j$、特异三角与 $i_1^*(L)=\mathcal{O}(p\alpha)$）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.8 三项复形与不可约情形（定理 8.3、8.4） · p.[72, 73]（PDF [76, 77]） · `源码/chapters/ch03f.tex:208-243（定理 8.3、8.4、引理 8.5）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.8 $I_{s_\alpha}=0$ 的刻画（命题 8.6、定理 8.7） · p.[74]（PDF [78]） · `源码/chapters/ch03f.tex:265-281（命题 8.6、定理 8.7）`
