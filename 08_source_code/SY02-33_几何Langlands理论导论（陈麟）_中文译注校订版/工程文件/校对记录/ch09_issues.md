# ch09.tex 审读意见（第 9 章，原 PDF p48–p53）

## ch09.tex:20（原 PDF p48）
- 原文：D-mod(Bun_G)^{temp} ≃ QCoh(LocSys_Ǧ)（temp 为上标）；同页一条为 D-mod(Bun_G) ≃ IndCoh_Nilp(LocSys_Ǧ)
- 原译：\[\DMod(\Bun_G)_{\mathrm{temp}}\simeq\QCoh(\LocSys_{\checkG}),\qquad\DMod(\Bun_G)\simeq\IndCoh_{\mathrm{Nilp}}(\LocSys_{\checkG}).\]
- 类型：公式
- 改法：\[\DMod(\Bun_G)^{\mathrm{temp}}\simeq\QCoh(\LocSys_{\checkG}),\qquad\DMod(\Bun_G)\simeq\IndCoh_{\mathrm{Nilp}}(\LocSys_{\checkG}).\] 即把 `_{\mathrm{temp}}` 改为 `^{\mathrm{temp}}`；第 147 行、ch10.tex:99、ch10.tex:118 同改。
- 理由：原文 temp 一律作上标（p48 与 p53 的 $\widetilde D(\Bun_G)=D(\Bun_G)^{\mathrm{temp}}$ 均已对照 PNG 核实），译稿一律作下标；该记号全书共 12 处，若确为既定约定可不动，否则应统一为上标。

## ch09.tex:75（原 PDF p50）
- 原文：Under geometric Satake, S_μ(St_m) corresponds to the IC sheaf of the Schubert stratum indexed by μ
- 原译：在几何 Satake 下，$S_\mu(\mathrm{St}_m)$ 对应于由 $\mu$ 标记的 Schubert 层的 IC 层
- 类型：术语
- 改法：在几何 Satake 下，$S_\mu(\mathrm{St}_m)$ 对应于由 $\mu$ 标记的 Schubert 子簇的 IC 层
- 理由：stratum 是子簇/胞腔而非 sheaf（层），“Schubert 层”与紧随的“IC 层”叠成“层的 IC 层”，读者无法分辨 stratum 与 sheaf；同类译法见 ch02.tex:138、ch02.tex:155、ch04.tex:143，建议全书统一为“Schubert 子簇”。

## ch09.tex:130（原 PDF p52）
- 原文：This also gives a quick proof of a fact used above. If F ∈ D(Bun_m) is an E-Hecke eigensheaf, then
- 原译：这也迅速证明了上文用到的一个事实。现在设 $E$ 为秩 $m$ 的不可约局部系统，且 $\cF\in D(\Bun_m)$ 是 $E$-Hecke 特征层，则如谱作用所预言，
- 类型：增译
- 改法：这也迅速证明了上文用到的一个事实。若 $\cF\in D(\Bun_m)$ 是 $E$-Hecke 特征层，则如谱作用所预言，
- 理由：原文没有“设 E 为秩 m 的不可约局部系统”这一限定；本章的 E 自 §9.1 起就是 rank(E)=r>m 的不可约局部系统（ch09.tex:7、ch09.tex:126），此处凭空改成秩 m，与上文矛盾并扰乱了 E-Hecke 特征层的含义。
