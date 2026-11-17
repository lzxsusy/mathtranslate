# -*- coding: utf-8 -*-
"""生成 RELEASE_REGISTER.csv：逐部登记底本类型、发布级别与权利依据。

用法：
    python tools/build_release_register.py            # 仅在台账不存在时生成
    python tools/build_release_register.py --force    # 覆盖重生成（会丢失人工修改）
    python tools/build_release_register.py --check    # 只检查覆盖，不写文件
"""
import csv
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "RELEASE_REGISTER.csv")

# 人工判定（证据见各工程 投稿信息.md）。auto 规则兜底，这里覆盖已知的图书/学位论文/讲义。
MANUAL = {
    # ---- arXiv 预印本（2026-11-16 校正：曾被 auto 规则误判为图书）----
    "SY02-06": ("arXiv 预印本", "arXiv:hep-th/0612073（Gukov–Witten）", "低", "Release 外链"),
    "SY05-19": ("arXiv 预印本", "arXiv:2609.21182", "低", "Release 外链"),
    # ---- 在版图书（Springer / AMS / CUP / OUP / 岩波 / 高教社 / 中国科大 / SGC …）----
    "SY01-08": ("图书", "Mirror Symmetry（Clay 专著，AMS/Clay 出版）", "高", "成品不公开"),
    "SY01-17": ("图书", "同调镜像对称性浅入门（出版本，365 页）", "高", "成品不公开"),
    "SY01-19": ("图书", "Guest, Quantum Cohomology，Oxford University Press 2008", "高", "成品不公开"),
    "SY02-08": ("图书", "Frenkel, Langlands Correspondence for Loop Groups，CUP 2007", "高", "成品不公开"),
    "SY03-09": ("图书", "Tachikawa, N=2 Supersymmetric Dynamics for Pedestrians（Springer LNP）", "高", "成品不公开"),
    "SY03-15": ("图书", "AMS, Quantum Fields and Strings: A Course for Mathematicians（pp.1119–1424）", "高", "成品不公开"),
    "SY03-18": ("图书", "Schottenloher, A Mathematical Introduction to CFT（Springer 2008）", "高", "成品不公开"),
    "SY03-19": ("图书", "AMS 出版专著（据原书全文翻译）", "高", "成品不公开"),
    "SY05-15": ("图书", "中国科学技术大学出版社 2025 年英文版（中科大一流规划教材）", "高", "成品不公开"),
    "SY05-20": ("图书", "代数群的几何表示论（第 I–II 卷）", "高", "成品不公开"),
    "SY05-21": ("图书", "复素几何 1–2", "高", "成品不公开"),
    "SY05-22": ("图书", "黎曼几何与几何分析（第七版）", "高", "成品不公开"),
    "SY07-01": ("图书", "深谷賢治《辛幾何》，岩波書店单行本 2008", "高", "成品不公开"),
    "SY07-02": ("图书", "AMS CBMS Regional Conference Series in Mathematics", "高", "成品不公开"),
    "SY07-04": ("图书", "场论与拓扑学（1998 年初版）", "高", "成品不公开"),
    "SY07-05": ("图书", "圏論（SGC ライブラリ 75，サイエンス社 2010 / Springer）", "高", "成品不公开"),
    "SY07-06": ("图书", "Atiyah, K-Theory（1967 年初版）", "高", "成品不公开"),
    "SY07-07": ("图书", "辛几何入门（SGC ライブラリ 118，サイエンス社 2015）", "高", "成品不公开"),
    "SY07-08": ("图书", "扶磊《代数几何（第二版）》，高等教育出版社", "高", "成品不公开"),
    "SY08-01": ("图书", "岩波講座 現代数学の展開 10（1998）", "高", "成品不公开"),
    "SY99-01": ("图书", "Springer《数学百科全书》第 12 卷（出版社影印本）", "高", "成品不公开"),
    # ---- 学位论文 ----
    "SY01-04": ("学位论文", "arXiv:2108.03931（学位论文，arXiv 托管）", "中", "Release 外链"),
    "SY01-06": ("学位论文", "arXiv:2306.13589（学位论文，arXiv 托管）", "中", "Release 外链"),
    "SY01-21": ("学位论文", "UC Berkeley 博士论文 2019（eScholarship）", "中", "成品不公开"),
    "SY01-22": ("学位论文", "Harvard 博士论文 2023（DASH）", "中", "成品不公开"),
    "SY02-11": ("学位论文", "Elliott 2016 学位论文", "中", "成品不公开"),
    "SY99-02": ("学位论文", "Setter 博士论文：TQFT 与几何 Langlands（2012/2013）", "中", "成品不公开"),
    # ---- 作者公开、未正式出版的讲义 ----
    "SY01-03": ("讲义", "驹场镜像对称讲义（2016）", "中", "成品不公开"),
    "SY01-13": ("讲义", "植田一石讲义（2015）", "中", "成品不公开"),
    "SY01-14": ("讲义", "植田一石《镜像对称入门》（2020）", "中", "成品不公开"),
    "SY01-15": ("讲义", "植田一石《镜像对称与 K3 曲面》", "中", "成品不公开"),
    "SY01-16": ("讲义", "植田一石《镜像对称与 Lagrange 环面纤维化》", "中", "成品不公开"),
    "SY02-05": ("讲义", "Between electric-magnetic duality and …（2021）", "中", "成品不公开"),
    "SY02-09": ("讲义", "袁瑶 2020 春季课程讲义（未正式出版）", "中", "成品不公开"),
    "SY02-10": ("讲义", "几何朗兰兹对偶是什么（科普/综述）", "中", "成品不公开"),
    "SY03-03": ("讲义", "arXiv:2006.14025", "低", "Release 外链"),
    "SY03-05": ("讲义", "广义对称性讲义（arXiv:2307.07547）", "低", "Release 外链"),
    "SY03-06": ("讲义", "量子场论的数学思想与概念（arXiv:2409.03117）", "低", "Release 外链"),
    "SY03-08": ("讲义", "Chern–Simons 理论导论（TASI 2019）", "中", "成品不公开"),
    "SY03-10": ("讲义", "量子场论讲义（2025）", "中", "成品不公开"),
    "SY03-13": ("讲义", "arXiv:2307.09215", "低", "Release 外链"),
    "SY03-20": ("讲义", "Witten 2015 规范理论与几何朗兰兹续谈", "中", "成品不公开"),
    "SY05-13": ("讲义", "Hines 拓扑 K 理论讲义（2016）", "中", "成品不公开"),
    "SY05-25": ("讲义", "Witten 0802.0999 镜像对称、Hitchin 方程与朗兰兹对偶", "低", "Release 外链"),
    "SY07-03": ("讲义", "李思《量子力学与几何》（2025）", "中", "成品不公开"),
    "SY07-09": ("讲义", "Lin Chen《Notes for Algebraic Geometry 1》2025 年秋课程讲义（未正式出版）", "中", "成品不公开"),
    "SY99-03": ("讲义", "SYZ 镜像对称讨论班讲义", "中", "成品不公开"),
}

BOOK_HINTS = [
    "出版社", "Press", "Springer", "AMS", "American Mathematical", "Cambridge University",
    "Oxford University", "岩波", "高等教育", "中国科学技术大学", "SGC", "単行本",
    "Encyclopaedia", "Graduate Texts", "Lecture Notes in Mathematics", "CBMS",
    "Astérisque", "Bourbaki", "サイエンス社",
]
THESIS_HINTS = ["博士论文", "thesis", "Thesis", "eScholarship", "DASH URN", "学位论文"]


def load_catalog():
    p = os.path.join(ROOT, "site", "catalog.json")
    with open(p, encoding="utf-8") as f:
        return {x["id"]: x for x in json.load(f)}


def load_pdf_links():
    """_PDF清单.tsv: pid -> 成品直链"""
    out = {}
    p = os.path.join(ROOT, "03_translations_meta", "_PDF清单.tsv")
    if not os.path.exists(p):
        return out
    with open(p, encoding="utf-8-sig") as f:
        rd = csv.DictReader(f, delimiter="\t")
        for r in rd:
            out[r.get("pid", "")] = (r.get("成品直链（Release 附件）") or r.get("成品直链") or "").strip()
    return out


def classify(pid, cat, links):
    if pid in MANUAL:
        t, basis, risk, level = MANUAL[pid]
        return t, basis, risk, level, "人工"
    info = (cat.get("pubinfo") or "") + " " + (cat.get("first_text") or "")[:400]
    arxiv = re.search(r"arXiv:?\s*([0-9]{4}\.[0-9]{4,5}|hep-th/[0-9]{7}|math/[0-9]{6})", info)
    if any(h in info for h in THESIS_HINTS):
        return "学位论文", "学位论文（repository 版本）", "中", "成品不公开", "auto"
    if any(h in info for h in BOOK_HINTS):
        return "图书", "出版图书（见 site/catalog.json pubinfo）", "高", "成品不公开", "auto"
    if arxiv:
        return "arXiv 预印本", "arXiv:%s" % arxiv.group(1), "低", "Release 外链", "auto"
    if "讲义" in info or "课程" in info:
        return "讲义", "作者公开讲义/课程材料", "中", "成品不公开", "auto"
    return "待复核", "底本类型未判定（需读 投稿信息.md 后人工确认）", "中", "成品不公开", "auto"


def main():
    force = "--force" in sys.argv
    check = "--check" in sys.argv
    cat = load_catalog()
    links = load_pdf_links()

    rows = []
    base = os.path.join(ROOT, "08_source_code")
    for d in sorted(os.listdir(base)):
        full = os.path.join(base, d)
        if not os.path.isdir(full):
            continue
        pid = d.split("_", 1)[0]
        c = cat.get(pid, {})
        t, basis, risk, plevel, how = classify(pid, c, links)
        # 实际成品文件是否在仓内
        chengpin = os.path.join(full, "成品")
        pdfs = []
        if os.path.isdir(chengpin):
            pdfs = [f for f in os.listdir(chengpin) if f.lower().endswith(".pdf")]
        yuanben = os.path.join(full, "原本")
        has_yuanben = os.path.isdir(yuanben) and any(
            f.lower().endswith(".pdf") for f in os.listdir(yuanben)
        )
        link = links.get(pid, "")
        rows.append({
            "id": pid,
            "中文题名": c.get("cn") or d.split("_", 1)[-1],
            "工程目录": "08_source_code/" + d,
            "底本类型": t,
            "底本标识": basis,
            "权利状态": "演绎作品；底本权利归原作者/出版方" if t != "待复核" else "待核",
            "风险": risk,
            "源码级别": "L2 公开·受限（可撤下）",
            "成品级别": plevel if not (plevel == "Release 外链" and not link.startswith("http")) else "申请获取（暂无外链）",
            "成品在仓": "是（违规待清）" if pdfs else "否",
            "成品直链": link if link.startswith("http") else "",
            "原文级别": "L4 禁入（原本 PDF 待清）" if has_yuanben else "L4 禁入",
            "判定方式": how,
            "状态": "待整改" if (pdfs or has_yuanben) else "合规",
            "复核日期": "2026-11-16",
            "备注": "",
        })

    if check:
        print("projects:", len(rows))
        from collections import Counter
        print(Counter(r["底本类型"] for r in rows))
        print(Counter(r["判定方式"] for r in rows))
        print("待整改:", sum(1 for r in rows if r["状态"] == "待整改"))
        return

    if os.path.exists(OUT) and not force:
        print("台账已存在，未覆盖：", OUT, "（加 --force 重生成）")
        return

    cols = ["id", "中文题名", "工程目录", "底本类型", "底本标识", "权利状态", "风险",
            "源码级别", "成品级别", "成品在仓", "成品直链", "原文级别",
            "判定方式", "状态", "复核日期", "备注"]
    with open(OUT, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print("written", OUT, len(rows), "rows")


if __name__ == "__main__":
    main()
