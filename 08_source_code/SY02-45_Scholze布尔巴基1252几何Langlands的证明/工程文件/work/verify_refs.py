# -*- coding: utf-8 -*-
"""核验参考文献的外部标识（arXiv 标题、Crossref DOI/期刊），输出 JSON。"""
import json, time, urllib.parse, urllib.request, re, sys

ARXIV = {
 "2405.03648": "Proof of the geometric Langlands conjecture II: Kac-Moody localization and the FLE",
 "2409.08670": "Proof of the geometric Langlands conjecture IV: ambidexterity",
 "2012.07665": "Duality for automorphic sheaves with nilpotent singular support",
 "2010.01906": "The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support",
 "2102.07906": "Automorphic functions as the trace of Frobenius",
 "1801.00655": "Contractibility of the space of generic opers for classical groups",
 "2409.07051": "Proof of the geometric Langlands conjecture III: compatibility with parabolic induction",
 "2405.12169": "K-theory and localizing invariants of large categories",
 "2210.01404": "An introduction to the categorical p-adic Langlands program",
 "2102.13459": "Geometrization of the local Langlands correspondence",
 "2508.02237": "Geometric Langlands in positive characteristic from characteristic zero",
 "2405.03599": "Proof of the geometric Langlands conjecture I: construction of the functor",
 "2409.09856": "Proof of the geometric Langlands conjecture V: the multiplicity one theorem",
 "2211.17247": "Exponentiation of coefficient systems and exponential motives",
 "2409.07363": "Geometric Eisenstein series I: finiteness theorems",
 "2410.13038": "6-Functor Formalisms and Smooth Representations",
 "1811.07976": "Decomposition au-dessus des parametres de Langlands elliptiques",
 "alg-geom/9603004": "Transformation de Fourier generalisee",
 "1211.5948": "Enhanced six operations and base change theorem for higher Artin stacks",
 "2206.02022": "A p-Adic 6-Functor Formalism in Rigid-Analytic Geometry",
 "2404.15694": "The integral motivic Satake equivalence for ramified groups",
}

CROSSREF = {
 "aizenbud_avni": "Representation growth and rational singularities of the moduli space of local systems",
 "arinkin_gaitsgory_2015": "Singular support of coherent sheaves and the geometric Langlands conjecture",
 "beilinson_2016": "Constructible sheaves are holonomic",
 "benzvi_nadler_2013": "Loop spaces and representations",
 "drinfeld_1983": "Two-dimensional l-adic representations of the fundamental group of a curve over a finite field and automorphic forms on GL(2)",
 "drinfeld_gaitsgory_2016": "Geometric constant term functor(s)",
 "faergeman_raskin_2025": "Non-vanishing of geometric Whittaker coefficients for reductive groups",
 "fargues_2025": "Geometrization of the local Langlands correspondence: an overview",
 "hansen_scholze_2023": "Relative perversity",
 "lafforgue_2018": "Chtoucas pour les groupes reductifs et parametrisation de Langlands globale",
 "laumon_1987": "Correspondance de Langlands geometrique pour les corps de fonctions",
 "mirkovic_vilonen_2007": "Geometric Langlands duality and representations of algebraic groups over commutative rings",
 "nadler_taylor_2025": "The Whittaker functional is a shifted microstalk",
 "nadler_yun_2019": "Spectral action in Betti geometric Langlands",
 "richarz_scholbach_2021": "The motivic Satake equivalence",
 "tamarkin_2018": "Microlocal condition for non-displaceability",
}

out = {"arxiv": {}, "crossref": {}}
ids = ",".join(ARXIV.keys())
url = "https://export.arxiv.org/api/query?id_list=%s&max_results=40" % urllib.parse.quote(ids)
raw = urllib.request.urlopen(url, timeout=40).read().decode("utf-8", "replace")
entries = re.findall(r"<entry>(.*?)</entry>", raw, re.S)
found = {}
for e in entries:
    aid = re.search(r"<id>https?://arxiv.org/abs/([^<]+)</id>", e)
    title = re.search(r"<title>(.*?)</title>", e, re.S)
    if aid and title:
        found[aid.group(1)] = " ".join(title.group(1).split())
for k, v in ARXIV.items():
    hit = None
    for a, t in found.items():
        if a.replace("v", "") .startswith(k.split("v")[0]) or k.startswith(a.split("v")[0]):
            hit = t
            break
    out["arxiv"][k] = {"expected": v, "got": hit, "ok": bool(hit) and v.split(":")[0].split()[0].lower() in hit.lower()}

for key, title in CROSSREF.items():
    q = urllib.parse.quote(title)
    u = "https://api.crossref.org/works?rows=1&query.bibliographic=%s" % q
    try:
        data = json.loads(urllib.request.urlopen(u, timeout=40).read().decode("utf-8", "replace"))
        it = data["message"]["items"][0]
        out["crossref"][key] = {
            "expected": title,
            "got": it.get("title", [""])[0],
            "doi": it.get("DOI"),
            "container": (it.get("container-title") or [""])[0],
            "volume": it.get("volume"), "page": it.get("page"),
            "year": (it.get("issued", {}).get("date-parts") or [[None]])[0][0],
        }
    except Exception as ex:
        out["crossref"][key] = {"expected": title, "error": str(ex)}
    time.sleep(0.4)

with open("refs_verify.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(json.dumps({k: (v.get("ok"), v.get("got", "")[:60]) for k, v in out["arxiv"].items()}, ensure_ascii=False, indent=1))
print("---")
for k, v in out["crossref"].items():
    print(k, "|", (v.get("got") or v.get("error"))[:70], "|", v.get("doi"), "|", v.get("container"), v.get("volume"), v.get("page"), v.get("year"))
