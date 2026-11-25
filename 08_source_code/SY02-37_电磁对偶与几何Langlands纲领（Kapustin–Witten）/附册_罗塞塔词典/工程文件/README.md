# 数学 ↔ 物理 罗塞塔词典（KW06 配套）

为 Kapustin–Witten《Electric–Magnetic Duality and the Geometric Langlands Program》(arXiv:hep-th/0604151, 231 页) 中译注本编写的**双向对照词典**：111 条术语，每条给出数学侧定义与例子、物理侧定义与例子、对应规则、直觉与常见误解，另附 KW06 逻辑流程图一张。

## 目录

```
rosetta/
├── main.tex              主文件（\input preamble → front → 六条轨道 → 附录）
├── preamble.tex          导言：ctex + amsmath + 词条环境 word + 侧标签宏
├── front.tex             扉页与「怎么用这本词典」
├── SCHEMA.md             写作规范（模板 / 质量标尺 / 分配表 / 禁用项）
├── REF-TERMS.tsv         111 条术语底稿（从解经本术语表抽取，含首现与易混点）
├── TEST-QUESTIONS.md     盲测题（10 题）
├── tools/
│   ├── check_track.py    单轨道自检：xelatex 冒烟编译 + 规范 lint
│   ├── make_table.py     从 entries/*.tex 生成附录 A 对照总表
│   └── test_key.md       盲测评分要点（内部）
├── entries/
│   ├── t1-duality.tex    T1 对偶、群论与耦合常数（14 条）
│   ├── t2-twist.tex      T2 超对称、扭化与拓扑场论（14 条）
│   ├── t3-hitchin.tex    T3 Hitchin 模空间与超凯勒几何（15 条）
│   ├── t4-branes.tex     T4 广义复几何、sigma 模型与膜（18 条）
│   ├── t5-operators.tex  T5 线算子、特征膜、单极子与 Hecke（21 条）
│   └── t6-langlands.tex  T6 Langlands 对应、D-模与几何背景（21 条）
├── flow/                 逻辑流程图（TikZ 源 + PDF）
├── appendix-table.tex    附录 A 对照总表（脚本生成）
├── appendix-flow.tex     附录 B 逻辑流程图说明
└── 交付/                 组装结果（成品 PDF / 工程文件 / 盲测报告）
```

## 构建

```bash
export PATH="/c/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64:$PATH"
cd C:\Users\admin\Downloads\KW06_work\rosetta
python tools/make_table.py            # 生成附录 A
for i in 1 2 3; do xelatex -interaction=nonstopmode -file-line-error main.tex; done
```

单轨道自检（写作时用）：

```bash
python tools/check_track.py entries/t3-hitchin.tex
```

## 质量约定

- 每条词条四段固定：两侧定义、两侧例子、对应规则、直觉与易错；每条 250–520 汉字。
- 术语与译本 `brief/GLOSSARY.tsv`、`brief/SPEC.md` 完全一致（如 canonical coisotropic brane = 典范余各向同性膜，eigenbrane = 特征膜）。
- 原文锚点写「§节号 + 印刷页码」，可翻回 KW06 核对。
- 参考了 Witten 2008 短综述（arXiv:0802.0999）、Frenkel 2009 综述（arXiv:0906.2747）与本地解经本 SEM-0604151 的判断，但正文均为重写，不搬运整段。

## 验收

1. `python tools/check_track.py` 对六个轨道全部 `errors: 0`；
2. `main.tex` 三遍 xelatex 0 error，PDF 页数与目录正常；
3. **盲测**：把词典 PDF 单独交给一个不知情的新智能体，答 `TEST-QUESTIONS.md` 的 10 题，≥8/10 且无反向错误为通过；未通过则按缺项补写后重测。盲测记录见 `交付/报告/盲测报告.md`。
