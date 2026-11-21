# 19 · 关键段落精译（4 段）

> 说明：页码用 PDF 页序（`p.3` = `txt/19/p003.txt`），与卡片 `sources.pages` 一致；括注里的印刷页码见 `notes.md §0`。
> 译文按原意重写，公式照抄；仅对原文的口语化表达做了必要的书面化。

[p.3] 在量子几何朗兰兹对偶中，人们比较的是曲线 $C$ 上主 $G$-丛模空间与主 ${}^LG$-丛模空间上的扭化 D-模范畴：当扭化参数 $q$ 与 ${}^Lq$ 满足
$${}^Lq=-\frac{1}{n_g q}$$
时，两者的导出范畴等价；其中 $n_g$ 取 $1,2,3$，由 $G$ 的 Dynkin 图最大边的重数决定。这里有一处参数化的平移要当心：$q=0$ 并不对应未扭化的 D-模，而是对应全纯微分算子层作用在 $L_0^{-h^\vee}$ 上的模，作者把这一扭化称为临界扭化。若把 $q$ 读作普朗克常数的倒数，则一侧的经典极限 $q\to\infty$ 与另一侧的超量子极限 ${}^Lq\to0$ 互相对偶；在该极限下量子几何朗兰兹退化为经典几何朗兰兹：$M_{\mathrm{flat}}(G_{\mathbb C},C)$ 上凝聚层的导出范畴，等价于 $\mathrm{Bun}_{{}^LG}(C)$ 上临界扭化 D-模的导出范畴。（印刷页 2）

[p.8] 在 $t=0$、$\theta=0$ 时，可以在 Higgs 丛模空间上造出这样一张膜：取 $M_H(G,C)$ 上的秩一线丛，令其曲率正比于 $\omega_K$，比例系数正是 $\mathrm{Im}\,\tau$。由于 $\omega_K$ 在 $M_H$ 上恰当，该曲率的上同调类为零，联络可以在平凡线丛上实现，膜因此存在，而且不依赖 $C$ 的复结构——它是一个拓扑对象。这张膜在复结构 $I$ 与 $J$ 下都是 A-膜、在 $K$ 下是 B-膜。把它放在圆盘边界上，二维 A-模型的作用量化为 $i\,\mathrm{Im}\,\tau\int\varphi^*\Omega_J$，于是 $\mathrm{Im}\,\tau$ 恰好扮演 $1/\hbar$ 的角色：边界可观测量的代数，就是复结构 $J$ 下 $M_{\mathrm{flat}}(G_{\mathbb C},C)$ 上全纯函数代数在 $\hbar=(\mathrm{Im}\,\tau)^{-1}$ 处的量子化，其一阶交换子为
$$[f,g]=-i(\mathrm{Im}\,\tau)^{-1}\Omega_J^{-1}(df,dg)+O((\mathrm{Im}\,\tau)^{-2}).$$
（印刷页 7）

[p.13] 设 $M$ 是复流形、$L$ 是其上的全纯线丛、$\lambda\neq0$。扭化余切丛 $\mathcal A_{L^\lambda}(M)$ 上的辛形式在典范坐标下写作 $(1/\hbar)\,dp_j\,dq_j$，量子化条件为 $[p_k,q_j]=-i\hbar\,\delta^j_k$ 与 $[p_k,p_j]=0$。取 $p_j=-i\hbar\nabla_j$，即得可观测量层是某个线丛上的全纯微分算子层，而该线丛由仿射丛的转移律定出，为 $L^{i\lambda/\hbar}$。此外还有一处 $\hbar^0$ 阶的修正：当 $L$ 平凡时，最自然的配方取 $K^{1/2}$，以保证扭化微分算子代数与其反代数同构。若假定没有更高阶修正，量子化就是 $K^{1/2}\otimes L^{i\lambda/\hbar}$ 上的全纯微分算子。代入 $M=\mathrm{Bun}_G$、$L=L_0$、$\lambda=-1$、$\hbar=(\mathrm{Im}\,\tau)^{-1}$，并用 $K^{1/2}=L_0^{-h^\vee}$，得到 $L_0^{-h^\vee-i\,\mathrm{Im}\,\tau}$，于是 $q=-i\,\mathrm{Im}\,\tau$，纯虚。（印刷页 12）

[p.16] 在 $C$ 上插入曲面算子之后，$t=0$ 的二维有效理论变成靶为抛物稳定 Higgs 丛模空间的 A-模型。$\omega_I$ 的周期线性依赖于 $\mathrm{Im}\,\tau$ 与各个 $\alpha_k$，B-场的周期线性依赖于 $\mathrm{Re}\,\tau$ 与各个 $\eta_k$：具体地，
$$\left[\frac{\omega_I}{2\pi}\right]=e\oplus\Big(-\bigoplus_{k=1}^{s}\alpha_k^*\Big),\qquad \left[\frac{B}{2\pi}\right]=(-\mathrm{Re}\,\tau)\oplus\bigoplus_{k=1}^{s}\eta_k .$$
取 $\mathrm{Re}\,\tau=0$ 时仍可构造特异余各向同性膜，只须把条件改成 $F+B=\mathrm{Im}\,\tau\,\omega_K$；此时由 $[\omega_K/2\pi]$ 的分解得到 $\gamma_k=-(\mathrm{Im}\,\tau)^{-1}\eta_k^*$，而 A-膜范畴并不依赖 $\gamma$，故这个限制无关紧要。对偶把 $(\alpha,\eta)$ 送到 $(\eta,-\alpha)$，于是两侧扭化 D-模范畴等价，条件是 ${}^L\alpha_k=\eta_k$、${}^L\eta_k=-\alpha_k$，以及
$$\mathrm{Im}\,{}^L\tau=\frac{1}{n_g\,\mathrm{Im}\,\tau}.$$
（印刷页 15）
