# -*- coding: utf-8 -*-
"""把 资料卡/_核验/MS-*.json 汇总成 资料卡/_核验记录.md"""
import json
import os
import sys

BASE = sys.argv[1] if len(sys.argv) > 1 else "."
VDIR = os.path.join(BASE, "_核验")
OUT = os.path.join(BASE, "_核验记录.md")

NAME = {
    "MS-01": "镜像对称", "MS-02": "镜像映射", "MS-03": "五次三维簇",
    "MS-04": "量子上同调", "MS-05": "GW 不变量", "MS-06": "Picard–Fuchs 方程",
    "MS-07": "环面簇", "MS-08": "扇与多胞形", "MS-09": "自反多胞形",
    "MS-10": "Hodge 结构", "MS-11": "Hodge 结构变分", "MS-12": "单值性与最大幺幂",
    "MS-13": "单值性定理与 LIM", "MS-14": "消失圈", "MS-15": "稳定映射与虚基本类",
    "MS-16": "预稳定曲线", "MS-17": "局部化与等变上同调", "MS-18": "Frobenius 流形",
    "MS-19": "量子超平面截面原理", "MS-20": "非线性 σ 模型与 SCFT", "MS-21": "GLσM 与相",
    "MS-22": "极端与锥形奇点跃迁", "MS-23": "nef 分拆与 Batyrev", "MS-24": "Berglund–Hübsch 转置",
}

MARK = {"ok": "✓", "wrong": "✗", "unverified": "△"}

rows, wrongs, unvers, total = [], [], [], [0, 0, 0]
for fn in sorted(os.listdir(VDIR)):
    if not fn.endswith(".json"):
        continue
    d = json.load(open(os.path.join(VDIR, fn), encoding="utf-8"))
    cid = d.get("id", fn[:-5])
    claims = d.get("claims", [])
    n_ok = sum(1 for c in claims if c.get("verdict") == "ok")
    n_w = sum(1 for c in claims if c.get("verdict") == "wrong")
    n_u = sum(1 for c in claims if c.get("verdict") == "unverified")
    total[0] += n_ok
    total[1] += n_w
    total[2] += n_u
    rows.append((cid, NAME.get(cid, ""), len(claims), n_ok, n_w, n_u, fn))
    for c in claims:
        if c.get("verdict") == "wrong":
            wrongs.append((cid, c))
        elif c.get("verdict") == "unverified":
            unvers.append((cid, c))

L = []
L.append("# SY01-26 资料卡核验记录\n")
L.append("本记录回答一个问题：**卡里的话，有多少经得起外部文献与自算的检验。**\n")
L.append("核验分三路，优先级由高到低：\n")
L.append("1. **外部权威文献**（A/B 级）：arXiv、AMS、nLab、Springer、原始论文，逐条给 URL；")
L.append("2. **自算**：能用算术或最小例子验证的数值/恒等式，直接算并写出算式；")
L.append("3. **库内对照**：与 `SY01-24_术语表`、`SY01-25_资料卡` 的用法比对（冲突已记入 `_冲突表.md`，此处不重复）。\n")
L.append("判定只有三种：✓ 与来源一致；✗ 与来源矛盾（需改卡）；△ 现有材料无法判定（记待核，不猜）。\n")
L.append(f"## 统计（{len(rows)}/{24} 张卡已核验）\n")
L.append("| 卡 | 名称 | 断言 | ✓ | ✗ | △ |")
L.append("|---|---|---|---|---|---|")
for cid, name, n, a, b, c, _ in rows:
    L.append(f"| {cid} | {name} | {n} | {a} | {b} | {c} |")
L.append(f"| **合计** | | **{total[0]+total[1]+total[2]}** | **{total[0]}** | **{total[1]}** | **{total[2]}** |\n")

if wrongs:
    L.append("## 一、与外部来源矛盾的断言（必须改卡）\n")
    for cid, c in wrongs:
        L.append(f"- **{cid}**：{c.get('claim','')}\n  - 证据：{c.get('evidence','')}\n  - 来源：{c.get('source','')}")
    L.append("")
if unvers:
    L.append("## 二、现有材料无法判定的断言（记待核，照卡保留）\n")
    for cid, c in unvers:
        L.append(f"- **{cid}**：{c.get('claim','')}\n  - 说明：{c.get('evidence','')}")
    L.append("")

L.append("## 三、本机复算（不依赖任何外部结论）\n")
L.append("脚本：`_mirror_review/verify_arith.py`、`verify_quintic.py`、`verify_instanton.py`。\n")
L.append("| 对象 | 复算结果 | 书中出处 | 结论 |")
L.append("|---|---|---|---|")
L.append("| 基础周期 ω₀(q) | 1, 120, 113400, 168168000, 305540235000 | (5.45) 分子 (5d)!/(d!)⁵；(2.11) 的 120 | ✓ 逐项一致 |")
L.append("| 镜像映射一次项 | 由 PF 算子 D = q d/dq(ω₁/ω₀) 得 D = 1 + 770q + 1435650q² + … | (2.9) 的 770 | ✓ 一致 |")
L.append("| Kähler 模曲线 | Σ n_d d³ q^d/(1−q^d) 用文献 n_d 复算 = 5, 2875, 4876875, 8564575000 | (2.32)/(5.45) | ✓ 前四项一致 |")
L.append("| Betti/Euler 数 | b₃ = 2+2h^{2,1} = 204，χ = 4−b₃ = −200 | MS-03 卡、§1.4 | ✓ |")
L.append("| n_d 全序列独立提取 | 需第三个周期（log² 解）的正确归一；当前尝试得 1+2115q…，与 1+575q 不符 | — | △ 待核（见下） |\n")
L.append("**关于 n_d 独立提取的说明**：`verify_instanton.py` 已用 Frobenius 方法从 PF 算子造出 0 阶、1 阶、2 阶解，"
         "y₀ 与 120 一致、镜像映射 770 一致；但用 θ²(y₂/y₀) 或 −ω₀²(θ/D)³(ω₂/ω₀) 得到的常数项/一次项归一仍与 5+2875q 相差一个"
         "与 q 有关的多项式因子，说明第三个周期的归一化约定尚未对齐。此项**如实记为待核**，不以文献值倒推。\n")
L.append("## 四、维护方式\n")
L.append("- 新核验：把 `MS-xx.json` 放进 `_核验/`，重跑 `scripts/make_verify_report.py 资料卡目录`；")
L.append("- 卡内 §11 的待核条目与本记录第二节互补：§11 是「我怀疑但没查」，本记录是「查过、结论如此」；")
L.append("- 标 ✗ 的条目改卡后，在卡内 §11 记一行「已按核验记录修正（日期）」并保留原断言。\n")

open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(L))
print(f"wrote {OUT}: {len(rows)} cards, ok={total[0]}, wrong={total[1]}, unverified={total[2]}")
