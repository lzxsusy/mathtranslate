# -*- coding: utf-8 -*-
"""把 产出/汇总/cards-chNN.tsv 合并成卡片施工计划 tmp/cards-plan.tsv。

  python tools/plan_cards.py            # 写计划表并打印统计
  python tools/plan_cards.py --check    # 只检查 id 冲突/重复

规则：
- id = grassmann/<type>/<slug>，slug 默认由 title_en 转 kebab-case，个别要手改的进 OVERRIDE。
- 与 _cards_grassmann/cards 里已有种子卡同标题的候选跳过（先看 id 末段、再看 title_zh 精确匹配）。
- 分组：ch1/ch3/A→甲，ch2/ch7→乙，ch5/ch8→丙，ch4/ch6/ch9→丁。
"""
import os
import re
import sys
import io
import glob
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUMMARY = os.path.join(ROOT, "产出", "汇总")
SEED = os.path.join(os.path.dirname(ROOT), "_cards_grassmann", "cards")
OUT = os.path.join(ROOT, "tmp", "cards-plan.tsv")

GROUP = {"1": "甲", "3": "甲", "A": "甲", "2": "乙", "7": "乙",
         "5": "丙", "8": "丙", "4": "丁", "6": "丁", "9": "丁"}

# 只有真正跨章的基础概念才挂 A 轨道；其余一律按所在章。读者 TSV 的 track 列口径不一，不采信。
A_SET = {
    "grassmann/concept/koszul-cohomology",
    "grassmann/concept/affine-grassmannian",
    "grassmann/concept/gv-sheaf",
    "grassmann/concept/coherent-system",
}
# 与种子卡或其它候选重复、不单独建卡的 id
DROP = {
    "grassmann/concept/alpha-stability": "并入 seed grassmann/concept/alpha-stable-coherent-system",
}

# title_en -> slug（只列自动转换会难看或会撞车的）
OVERRIDE = {
    "Berezin–Toeplitz deformation quantization": "berezin-toeplitz-quantization",
    "rigid family of Kähler structures": "rigid-kahler-family",
    "factorization along a curve": "factorization-along-a-curve",
    "star product on holonomy functions": "holonomy-star-product",
    "graded minimal resolution and Betti number": "graded-minimal-resolution",
    "property (N_p)": "property-np",
    "Koszul duality on projective varieties": "koszul-duality",
    "Green's dimension formula": "greens-dimension-formula",
    "Koszul cycle as a degeneracy locus": "koszul-cycle",
    "slope of an effective divisor": "slope-of-effective-divisor",
    "Green's conjecture on canonical syzygies": "greens-conjecture",
    "Maximal Rank Conjecture": "maximal-rank-conjecture",
    "Minimal Syzygy Conjecture": "minimal-syzygy-conjecture",
    "Max Noether's theorem as K_{0,2}=0": "max-noether-theorem",
    "Enriques–Babbage–Petri as K_{1,2}=0": "enriques-babbage-petri",
    "degree 6 genus 3 curves on a quadric": "degree-6-genus-3-quadric",
    "Reider's theorem": "reiders-theorem",
    "torsion pair and tilt": "torsion-pair-and-tilt",
    "central charge and phase": "central-charge-and-phase",
    "wall and wall-crossing": "wall-and-wall-crossing",
    "s = 1/2 dichotomy": "s-half-dichotomy",
    "slope comparison in a semicircle": "slope-comparison-semicircle",
    "Kirwan map and the class D": "kirwan-map-and-class-d",
    "intersection pairing via V_M": "intersection-pairing-via-vm",
    "residue formula for pairings": "residue-formula-for-pairings",
    "wall-crossing term for M(2,0)": "wall-crossing-term-m20",
    "Hecke modification and Hecke type": "hecke-modification",
    "Partial Grothendieck resolution and nilpotent cone": "partial-grothendieck-resolution",
    "gerbe banded by mu_n": "gerbe-banded-by-mu-n",
    "twisted sheaf on a mu_n-gerbe": "twisted-sheaf",
    "isotrivial family / form of a variety": "isotrivial-family",
    "period and index of a Brauer class": "period-and-index",
    "parabolic bundle and parabolic degree": "parabolic-bundle",
    "root stack (n-th root of a divisor)": "root-stack",
    "ramification exact sequence": "ramification-sequence",
    "isotrivial (non-abelian) Torelli theorem": "isotrivial-torelli",
    "bicyclic algebra with Faddeev index 4": "bicyclic-algebra-faddeev-4",
    "Brill–Noether number beta": "brill-noether-number",
    "d_0(n,k) and U(n,d,k)": "existence-region-d0",
    "M-regular sheaf": "m-regular-sheaf",
    "torsion-freeness criterion": "torsion-freeness-criterion",
    "continuously globally generated": "continuously-globally-generated",
    "nefness of GV-sheaves": "nefness-of-gv-sheaves",
    "M-regularity index": "m-regularity-index",
    "$m$-" + chr(92) + "Theta$-regular": "m-theta-regular",
    "elliptic curve example": "elliptic-curve-regularity",
    "Brill–Noether locus and number": "brill-noether-locus-on-reducible-curves",
    "Example 5.3": "example-non-stability-large-alpha",
    "Example 7.5": "example-genus-10-d0",
    "Verlinde bundles": "verlinde-bundle-regularity",
}


TITLE = {
    "grassmann/concept/gerbe-banded-by-mu-n": "$\\mu_n$-带化的 gerbe",
    "grassmann/concept/brill-noether-locus-on-reducible-curves": "可约曲线上的 Brill–Noether 簇",
    "grassmann/concept/existence-region-d0": "$d_0$ 与存在域 $U(n,d,k)$",
    "grassmann/concept/torsion-freeness-criterion": "$M$-正则性的无挠判别",
    "grassmann/concept/nefness-of-gv-sheaves": "GV-层的 nef 性",
    "grassmann/example/example-non-stability-large-alpha": "大 $\\alpha$ 下不半稳定的例子（例 5.3）",
    "grassmann/example/example-genus-10-d0": "$g=10$、$(2,12,4)$ 的 $d_0$ 例子（例 7.5）",
}


def slugify(s):
    if s in OVERRIDE:
        return OVERRIDE[s]
    s = (s.replace("&", " and ").replace("–", "-").replace("—", "-")
         .replace("'", "").replace("’", "").replace("$", "").replace("\\", ""))
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return re.sub(r"-+", "-", s)


def load_seeds():
    ids, titles = set(), set()
    for p in glob.glob(os.path.join(SEED, "*", "*.json")):
        with open(p, encoding="utf-8") as f:
            c = json.load(f)
        ids.add(c["id"])
        titles.add(c.get("title", ""))
        for a in c.get("aliases", []):
            titles.add(a)
    return ids, titles


def main():
    check_only = "--check" in sys.argv
    seed_ids, seed_titles = load_seeds()
    rows, seen, dup, skipped = [], {}, [], []
    for p in sorted(glob.glob(os.path.join(SUMMARY, "cards-ch*.tsv"))):
        ch = re.search(r"cards-ch(\d\d)\.tsv", os.path.basename(p)).group(1)
        lines = open(p, encoding="utf-8-sig").read().splitlines()
        for ln in lines[1:]:
            f = ln.split("\t")
            if len(f) < 7:
                dup.append(("BADROW", os.path.basename(p), ln[:60]))
                continue
            kind, ten, tzh, track, anchor = f[1], f[2], f[3], f[4], f[6]
            typ = "example" if ("例" in kind or kind.strip() == "example") else "concept"
            slug = slugify(ten)
            cid = "grassmann/%s/%s" % (typ, slug)
            if cid in seed_ids or tzh in seed_titles:
                skipped.append((cid, ch, tzh, "seed"))
                continue
            tr = track.strip()
            if tr.lower().startswith("ch"):
                tr = str(int(tr[2:]))
            tr = "A" if cid in A_SET else ch.lstrip("0")
            if cid in DROP:
                skipped.append((cid, ch, tzh, DROP[cid]))
                continue
            key = (cid,)
            if key in seen:
                dup.append((cid, ch, "dup with %s" % seen[key]))
                continue
            seen[key] = ch
            rows.append([cid, typ, TITLE.get(cid, tzh), ten, tr, GROUP.get(tr, "?"), ch, anchor])

    rows.sort(key=lambda r: ("甲乙丙丁?".index(r[5]), r[6], r[0]))
    if not check_only:
        with open(OUT, "w", encoding="utf-8", newline="\n") as f:
            f.write("id\ttype\ttitle_zh\ttitle_en\ttrack\tgroup\tchapter\tanchor\n")
            for r in rows:
                f.write("\t".join(r) + "\n")
    from collections import Counter
    print("合并 %d 行（跳过种子重复 %d，冲突/坏行 %d）" % (len(rows), len(skipped), len(dup)))
    print("按组：", dict(Counter(r[5] for r in rows)))
    print("按类型：", dict(Counter(r[1] for r in rows)))
    print("按 track：", dict(sorted(Counter(r[4] for r in rows).items())))
    for s in skipped:
        print("  SKIP", s)
    for d in dup:
        print("  DUP ", d)
    if not check_only:
        print("写出", OUT)


if __name__ == "__main__":
    main()
