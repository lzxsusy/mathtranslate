# raskin_glc：Raskin 射影曲线几何 Langlands 讲义资料卡

来源：Sam Raskin 讲授、Lin Chen 笔记《Notes for "Geometric Langlands for Projective Curves"》，
2025-07-07/11，18 页；底本与译注本见 `08_source_code/SY02-47_Raskin射影曲线上的几何Langlands讲义/`。

共 18 张卡。每张卡含原文页码、逐字引文、译注锚点与核验记录；
`verification.status = partial` 的卡含逐条外部核验；`source-only` 的卡只据原文与经典文献。

## 卡片

| id | 类型 | 标题 | 页码 |
| --- | --- | --- | --- |
| `raskin_glc/concept/deligne-gl1-construction` | concept | Deligne 的 $\mathbb{G}_m$ 几何类域论构造 | 3, 4 |
| `raskin_glc/concept/cuspidal-sheaf` | concept | 尖点层与常数项函子 | 6, 7 |
| `raskin_glc/derivation/cuspidal-vanishing` | derivation | 尖点层在 $d>2g-2$ 的 $!$-消没：命题 2.1.5 的拆解 | 6 |
| `raskin_glc/concept/coefficient-functor` | concept | $\operatorname{coeff}_D$：把层变成向量空间的系数函子 | 8, 9 |
| `raskin_glc/concept/fourier-deligne-transform` | concept | Fourier–Deligne 变换与 $\operatorname{coeff}_d$ 的改写 | 9, 10 |
| `raskin_glc/concept/pgl2-geometric-langlands` | concept | $\mathrm{PGL}_2$ 的几何 Langlands 对应 | 8, 9, 10, 11 |
| `raskin_glc/concept/whittaker-coefficient` | concept | Whittaker 系数与几何 Casselman–Shalika | 16, 17 |
| `raskin_glc/concept/hecke-eigensheaf` | concept | Hecke 特征层 | 14, 15 |
| `raskin_glc/concept/geometric-satake` | concept | 几何 Satake 等价 | 12, 13 |
| `raskin_glc/concept/categorical-geometric-langlands` | concept | 范畴化几何 Langlands | 17, 18 |
| `raskin_glc/correction/abel-jacobi-fiber` | correction | Abel–Jacobi 纤维被写成 $\Gamma(X,L)\setminus\{0\}$ | 4 |
| `raskin_glc/correction/perverse-lisse-swap` | correction | $\sigma^{(d)}$ 与 $\mathcal{F}_\sigma$ 的 perverse/lisse 性质被互换 | 9 |
| `raskin_glc/remark/generic-rank-convention` | remark | 通用秩公式中的指数 $d_i$ | 15 |
| `raskin_glc/correction/bh1-vs-bh0` | correction | 常数项证明中的 $BH^1$ 应为 $BH^0$ | 6 |
| `raskin_glc/correction/b-vs-e-borel-sequence` | correction | Borel 正合列中的 $B$ 应为 $\cE$ | 6 |
| `raskin_glc/correction/holonomic-vs-holomorphic` | correction | 「holonomic 模形式」应为「holomorphic 模形式」 | 7 |
| `raskin_glc/correction/rep-g-vs-rep-gdual` | correction | $\Gd$-局部系统的函子定义误写 $\Rep(G)$ | 12 |
| `raskin_glc/correction/vilonon-spelling` | correction | 作者名 Vilonen 被拼成 Vilonon | 16 |

## 校验

```bash
python tools/card_spec_check.py --set raskin_glc --strict
```

`related` 只指向本集内已存在的 id；`rights` 统一为 `rewritten`（中文重述，不复制原文）。
