# 几何量子化资料卡 · 总表

书名：李思《量子力学与几何》（中文译注本）第 5 章「几何量子化」。本表由卡片 JSON 自动汇总，与 `index.jsonl` 同步。

页码一律用**原书印刷页**（250–296）；PDF 页 = 印刷页 + 1（251–297）。源码行指底本 `chunks/ch05a.tex`（§5.1–§5.2）与 `chunks/ch05b.tex`（§5.3–§5.4）。

共 **48 张**：1 张总览 + 27 张概念卡 + 20 张例子卡。

## 总览卡

| id | 标题 | 印刷页 | 源码 |
|---|---|---|---|
| `geoq/concept/overview-geometric-quantization` | 几何量子化总览：从相空间到量子希尔伯特空间 | 全章 | `ch05a.tex:9-1221`、`ch05b.tex:6-1470` |

## 概念卡

### A 轨 · 相空间的辛几何（§5.1）（10 张）

| id | 标题 | 印刷页 | 源码行 |
|---|---|---|---|
| `geoq/concept/symplectic-vector-space` | 辛向量空间与辛基 | 250–251 | ch05a.tex:20-50、ch05a.tex:51-58 |
| `geoq/concept/compatible-complex-structure` | 相容复结构与可缩性 | 251–254 | ch05a.tex:106-176、ch05a.tex:233-278 |
| `geoq/concept/symplectic-group` | 辛群 $\operatorname{Sp}(V)$ | 251–253 | ch05a.tex:59-93、ch05a.tex:198-207 |
| `geoq/concept/lagrangian-grassmannian` | 拉格朗日子空间与格拉斯曼流形 | 254–256 | ch05a.tex:299-368、ch05a.tex:370-429 |
| `geoq/concept/maslov-index` | 马斯洛夫指标与 $\mathcal L(V)$ 的基本群 | 257–258 | ch05a.tex:435-490、ch05a.tex:491-531 |
| `geoq/concept/hamiltonian-vector-field` | 哈密顿向量场与泊松括号 | 259–261 | ch05a.tex:588-690 |
| `geoq/concept/symplectic-manifold` | 辛流形（symplectic manifold） | 259–260 | ch05a.tex:563-627 |
| `geoq/concept/cotangent-bundle` | 余切丛的典范辛结构与刘维尔形式 | 261 | ch05a.tex:691-703、ch05a.tex:725-728 |
| `geoq/concept/lagrangian-submanifold` | 拉格朗日子流形、可投影与相函数 | 261–262 | ch05a.tex:705-771 |
| `geoq/concept/symplectomorphism` | 辛同胚与哈密顿流 | 263 | ch05a.tex:772-812 |

### B 轨 · 几何半经典量子化（§5.2）（5 张）

| id | 标题 | 印刷页 | 源码行 |
|---|---|---|---|
| `geoq/concept/wkb-approximation` | WKB 半经典解与哈密顿–雅可比方程 | 263–266 | ch05a.tex:813-919、ch05a.tex:920-949 |
| `geoq/concept/half-density` | 密度、半密度与刘维尔测度 | 266–267 | ch05a.tex:950-1021、ch05a.tex:971-977 |
| `geoq/concept/geometric-semiclassical-state` | 几何半经典定态 | 267–269 | ch05a.tex:1000-1021、ch05a.tex:1062-1068、ch05a.tex:1072-1098 |
| `geoq/concept/bohr-sommerfeld` | 玻尔–索末菲量子化条件 | 268–269 | ch05a.tex:1024-1109 |
| `geoq/concept/maslov-correction` | 马斯洛夫修正与 EBK 条件 | 270–271 | ch05a.tex:1111-1199、ch05a.tex:1191-1199 |

### C 轨 · 海森堡群与表示（§5.3）（5 张）

| id | 标题 | 印刷页 | 源码行 |
|---|---|---|---|
| `geoq/concept/heisenberg-lie-algebra` | 海森堡李代数 $h_V$ | 272 | ch05b.tex:29-64 |
| `geoq/concept/heisenberg-group` | 海森堡群 $H_V$ 与中心扩张 | 273 | ch05b.tex:69-100 |
| `geoq/concept/schrodinger-representation` | 薛定谔表示 $T_\hbar$ | 273–275 | ch05b.tex:102-205、ch05b.tex:153-173 |
| `geoq/concept/segal-bargmann-space` | Segal–Bargmann 空间 | 275–280 | ch05b.tex:220-554、ch05b.tex:389-554 |
| `geoq/concept/stone-von-neumann` | 斯通–冯·诺依曼定理 | 275 | ch05b.tex:204-214 |

### D 轨 · 几何量子化机器（§5.4）（7 张）

| id | 标题 | 印刷页 | 源码行 |
|---|---|---|---|
| `geoq/concept/dirac-quantization` | 狄拉克量子化原理 Q1–Q5 | 280–281 | ch05b.tex:559-611、ch05b.tex:612-661 |
| `geoq/concept/groenewold-van-hove` | 格罗嫩沃尔德–范霍夫定理（Groenewold–Van Hove） | 282–284 | ch05b.tex:686-760、ch05b.tex:761-816 |
| `geoq/concept/prequantization` | 预量子化线丛 | 284–286 | ch05b.tex:817-907、ch05b.tex:880-950 |
| `geoq/concept/quantization-condition` | 可量子化条件（陈类整性） | 286–287 | ch05b.tex:951-980、ch05b.tex:981-1007 |
| `geoq/concept/polarization` | 极化：实极化与凯勒极化 | 287–289 | ch05b.tex:1009-1045、ch05b.tex:1047-1075 |
| `geoq/concept/quantum-hilbert-space` | 量子希尔伯特空间与半形式修正 | 288–296 | ch05b.tex:1047-1075、ch05b.tex:1077-1265、ch05b.tex:1441-1465 |
| `geoq/concept/quantum-operator` | 量子算子与 P-保持条件 | 292–296 | ch05b.tex:1266-1321、ch05b.tex:1320-1465 |

## 例子卡

20 个编号例子各一张，均可用 `concept_refs` 指回概念卡。

| id | 标题 | 对应概念 | 印刷页 | 源码行 |
|---|---|---|---|---|
| `geoq/example/sp2-equals-sl2` | $n=1$ 时 $\operatorname{Sp}(2)=\operatorname{SL}(2)$ | `geoq/concept/symplectic-group`、`geoq/concept/symplectic-vector-space` | 251 | ch05a.tex:94-105 |
| `geoq/example/standard-compatible-complex-structure` | 标准辛基下的相容复结构 | `geoq/concept/compatible-complex-structure`、`geoq/concept/symplectic-vector-space` | 252 | ch05a.tex:131-151、ch05a.tex:153-176 |
| `geoq/example/unitary-symplectic-intersection` | $\operatorname{Sp}(2n)\cap\operatorname{O}(2n)=\operatorname{U}(n)$ 的显式实现 | `geoq/concept/symplectic-group`、`geoq/concept/compatible-complex-structure` | 253 | ch05a.tex:208-231 |
| `geoq/example/compatible-complex-structures-on-r2` | $\mathbb R^2$ 上相容复结构的参数化 | `geoq/concept/compatible-complex-structure`、`geoq/concept/symplectic-group` | 254 | ch05a.tex:280-295 |
| `geoq/example/standard-lagrangian-subspaces` | 标准辛基给出的两张拉格朗日子空间 | `geoq/concept/lagrangian-grassmannian`、`geoq/concept/symplectic-vector-space` | 255 | ch05a.tex:335-345 |
| `geoq/example/maslov-index-rp1` | $\mathcal L(\mathbb R^2)=\mathbb{RP}^1$ 上的马斯洛夫指标 | `geoq/concept/maslov-index`、`geoq/concept/lagrangian-grassmannian` | 258–259 | ch05a.tex:533-543、ch05a.tex:550-559 |
| `geoq/example/cotangent-bundle-symplectic` | 余切丛 $T^*X$ 的典范辛形式（$X=\mathbb{R}^2$） | `geoq/concept/cotangent-bundle`、`geoq/concept/symplectic-manifold` | 261 | ch05a.tex:691-703 |
| `geoq/example/circle-lagrangian-in-r2` | $\mathbb{R}^2=T^*\mathbb{R}$ 中的圆是拉格朗日子流形 | `geoq/concept/lagrangian-submanifold`、`geoq/concept/cotangent-bundle` | 262 | ch05a.tex:754-771 |
| `geoq/example/exact-lagrangian-phase-function` | 恰当拉格朗日 $L_{df}$ 与相函数（$f=q^1q^2$） | `geoq/concept/lagrangian-submanifold`、`geoq/concept/cotangent-bundle` | 262 | ch05a.tex:746-753 |
| `geoq/example/hamiltonian-flow-symplectomorphism` | 哈密顿流是辛同胚（$f=\tfrac12q^2$ 与 $f=q^1q^2$） | `geoq/concept/symplectomorphism`、`geoq/concept/hamiltonian-vector-field` | 263 | ch05a.tex:785-812 |
| `geoq/example/harmonic-oscillator-level-set` | 一维谐振子的水平集与焦散 | `geoq/concept/geometric-semiclassical-state`、`geoq/concept/wkb-approximation`、`geoq/concept/half-density` | 268 | ch05a.tex:1032-1059 |
| `geoq/example/oscillator-ebk-spectrum` | 谐振子的凯勒–马斯洛夫条件给出精确谱 | `geoq/concept/maslov-correction`、`geoq/concept/bohr-sommerfeld`、`geoq/concept/geometric-semiclassical-state` | 271–272 | ch05a.tex:1201-1211、ch05b.tex:6-23 |
| `geoq/example/s2-quantization-condition` | $S^2$ 的可量子化条件 $A\in\frac{\hbar}{2}\mathbb{Z}$ | `geoq/concept/quantization-condition`、`geoq/concept/prequantization` | 287 | ch05b.tex:996-1007 |
| `geoq/example/cotangent-bundle-quantizable` | 余切丛总可量子化 | `geoq/concept/prequantization`、`geoq/concept/quantization-condition` | 287 | ch05b.tex:981-995 |
| `geoq/example/kahler-polarization-cn` | $\mathbb{C}^n$ 的凯勒极化与全纯截面 | `geoq/concept/polarization`、`geoq/concept/prequantization` | 289–290 | ch05b.tex:1125-1163 |
| `geoq/example/real-polarization-r2n` | $\mathbb{R}^{2n}$ 的实极化与位置波函数 | `geoq/concept/polarization`、`geoq/concept/prequantization` | 289 | ch05b.tex:1077-1124 |
| `geoq/example/holomorphic-line-bundle-polarization` | 全纯线丛上的凯勒极化 | `geoq/concept/polarization`、`geoq/concept/quantization-condition` | 290–291 | ch05b.tex:1164-1219 |
| `geoq/example/tensor-power-line-bundle` | 线丛张量幂与 $\hbar$ 的重新标定 | `geoq/concept/prequantization`、`geoq/concept/quantization-condition` | 291–292 | ch05b.tex:1220-1265 |
| `geoq/example/quantum-operators-real-polarization` | 实极化下 P-保持函数的量子化 | `geoq/concept/quantum-operator`、`geoq/concept/polarization`、`geoq/concept/quantum-hilbert-space` | 293–294 | ch05b.tex:1323-1361 |
| `geoq/example/oscillator-half-form-spectrum` | 凯勒极化、半形式与 $(n+\frac12)\hbar$ 谱 | `geoq/concept/quantum-hilbert-space`、`geoq/concept/quantum-operator`、`geoq/concept/polarization` | 294–296 | ch05b.tex:1363-1439、ch05b.tex:1441-1465 |

## 统计

- 总览：1 张
- A 轨 · 相空间的辛几何（§5.1）：20 张
- B 轨 · 几何半经典量子化（§5.2）：7 张
- C 轨 · 海森堡群与表示（§5.3）：5 张
- D 轨 · 几何量子化机器（§5.4）：15 张
- 定理陈述 55 条；证明步骤 214 步；例子计算 97 步；易错点 163 条。

> 读法：先看 `MAP.md` / `map.png` 建立四轨与一条流水线的位置感，再按总表挑卡；概念卡正面是 `question`，例子卡按 `setup → computation → result → check` 使用。
