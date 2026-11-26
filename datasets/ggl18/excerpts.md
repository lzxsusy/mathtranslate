# 关键段落精译

说明：页码为 PDF 页序（本篇 PDF 页序 = 印刷页序）。译文按原文段落逐句对应，术语依 `terms.tsv`；方括号内为译者补注，非原文。

---

[p.1]（摘要）

我们研究复光滑旗流形 $G/B$ 上的二维扭化 (0,2) sigma 模型，并探讨它与几何 Langlands 纲领的关系。我们发现：在 $G/B$ 上的玻色弦与它在 $G$ 上的 $B$-规范版本之间，存在一个全纯手征代数层面的等价；这一等价将蕴含使 $G=\mathrm{SL}(N,\mathbb C)$ 的几何 Langlands 对应得以成立的经典 W 代数同构与一个水平关系。这为 $G=\mathrm{SL}(N,\mathbb C)$ 的几何 Langlands 对应提供了另一种物理解释，不同于 Kapustin 与 Witten 先前通过四维规范理论电磁对偶所给出的解释。同样地，Hecke 算子与 Hecke 特征层也将获得另一种物理解释：它们是无边界的准拓扑 sigma 模型的局域算符关联函数。一篇后续论文将在类似框架下研究 $G=\mathrm{SL}(N,\mathbb C)$ 的「量子」几何 Langlands 对应的解释，不过要打开 sigma 模型模空间上的 flux，使相应的经典代数发生「量子」形变。

---

[p.67]（(3.61)–(3.63) 附近的论证）

由 $S^{(s_i)}_n$ 生成的经典 W 代数与由 $L^{(s_i)}_n$ 生成的经典 W 代数之间的同构，必然蕴含 (3.58) 与 (3.59) 中分别由 $S^{(2)}_n$ 与 $L^{(2)}_n$ 生成的经典子代数之间的同构。这又意味着必须有 $c(k,k')|_{k\to-h^{\vee},\,k'\to\infty}=-h^{\vee}\dim\mathfrak{sl}_N$，即 (3.61)。在 §2 讨论的 $N=2,3$ 诸例中我们看到，上式成立当且仅当 $(k+h^{\vee})(k'+h^{\vee})=1$。稍加验证可知对任意 $N$ 亦然：注意 $c(k,k')$ 在该极限下的存活项恰为 $-N(N^2-1)(k+h^{\vee})(k'+h^{\vee})$，而 $N=h^{\vee}$、$N^2-1=\dim\mathfrak{sl}_N$，故该极限等于 $-h^{\vee}\dim\mathfrak{sl}_N$ 当且仅当 $(k+h^{\vee})(k'+h^{\vee})=1$。由于 $\mathcal W_N(-h^{\vee}\dim\mathfrak{sl}_N)\simeq z(\widehat{\mathfrak{sl}}_N)$，且 $\mathfrak{sl}_N$ 为自对偶（$h^{\vee}={}^Lh^{\vee}$、$r^{\vee}=1$），于是：$SL(N)/B$ 上扭化 sigma 模型中与 $\bar\psi^j$ 无关的扇区，与 $SL(N)$ 上 $B$-规范 WZW 模型在手征代数层面的等价，将蕴含 Poisson 代数同构 $z(\widehat{\mathfrak g})\simeq\mathcal W_\infty({}^L\widehat{\mathfrak g})$ 与水平关系 $(k+h^{\vee})r^{\vee}=1/(k'+{}^Lh^{\vee})$。

---

[p.79]（Hecke 特征层 ↔ 平坦全纯丛，含脚注 14 的限制）

最后回忆：$\Delta(V_\chi)$、从而是 $\mathrm{Bun}_{SL(N)}$ 上的余不变量层，具有 $\mathrm{Bun}_{SL(N)}$ 上扭化 D-模的结构。所寻的 Hecke 特征层 [6] 是 $\mathrm{Bun}_{SL(N)}$ 上的非扭化全纯 D-模 $\Delta(V_\chi)\otimes K^{-1/2}$，本征值为 $E_\chi$；其中 $K$ 是 $\mathrm{Bun}_{SL(N)}$ 上的典范线丛，$E_\chi$ 是对应于某一组 $S^{(s_i)}(z)$ 场之选取的唯一 ${}^LSL(N)$-丛。由于与整体定义的 $K$ 作张量积只是把 $\Delta(V_\chi)$ 一一地送到 $\Delta(V_\chi)\otimes K^{-1/2}$，我们得到 $\mathrm{Bun}_{SL(N)}$ 上 Hecke 特征层与 $\Sigma$ 上平坦全纯 ${}^LSL(N)$-丛（${}^LSL(N)=PSL(N)$）之间的一一对应，即 $G=SL(N)$ 的几何 Langlands 对应。脚注 14 补充：上述平坦全纯丛限于那些具有 $\Sigma$ 上 ${}^L\mathfrak g$-oper 结构的丛；这类丛的连接空间只是全部平坦丛的连接模叠 $\mathrm{Loc}_{{}^LG}$ 中的半维子空间。因此本构造只部分地建立了几何 Langlands 对应；但把关联函数中考虑的手征算符推广为带 $\mathfrak g$ 的有限维表示标签的更一般算符（在数学上等价于显式化任意平坦丛的 singular oper 结构 [6]），即可囊括全部平坦丛。

---

[p.80]（Hecke 算子的作用与 KW06 的对比）

由 $F(J(z))$ 描述的这组局域算符，可以等同于临界层 $k=-h^{\vee}$ 处与 $\widehat{\mathfrak g}$ 相伴的、数学上定义的手征顶点代数 $V_{-h^{\vee}}(\mathfrak g)$（本篇中 $\mathfrak g=\mathfrak{sl}_N$）。按公理化 CFT 意义定义的 Hecke 算子对 Hecke 特征层的作用，等价于插入一个位于 $m$ 份 $V_{-h^{\vee}}(\mathfrak g)$ 之拷贝所给手征顶点代数（即 $\oplus_mV_{-h^{\vee}}(\mathfrak g)$）中的算符；这样的算符仍是 $F(J(z))$ 形式的多项式算符。简言之，Hecke 算子的作用等价于在 $SL(N)/B$ 上扭化 (0,2) sigma 模型的局域初级场算符关联函数中，插入同样位于该模型全纯手征代数内的其他局域算符——如前强调，这是一个无边界准拓扑 sigma 模型。这与几何 Langlands 纲领的规范理论进路中对 Hecke 算子（及 Hecke 特征层）的描述形成对照：在那里它们被解释为有边界拓扑 sigma 模型中的 't Hooft 线算子（及 D-膜）。因此我们的结果为 $G=SL(N)$ 几何 Langlands 对应的这些抽象对象提供了另一种物理解释，不同于 Kapustin 与 Witten 在 [1] 中给出的规范理论解释。
