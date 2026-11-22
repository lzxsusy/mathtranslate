# -*- coding: utf-8 -*-
"""追加 §2 翻译中新发现的疑点/勘误条目，并补录术语。"""
import io, os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 工程文件
work = os.path.join(base, "work")
yi = os.path.join(work, "疑点清单.tsv")

rows = [
 ("Q21", "372", "Ng\\^o's proof the the fundamental lemma",
  "重复 the，且缺介词 of",
  "照译「Ngô 对基本引理的证明」，登记 errata E01",
  "语法", "已解"),
 ("Q22", "392", "non-archimidean local field",
  "拼写错误，应为 non-archimedean",
  "照译作「非阿基米德」，登记 errata E02", "拼写", "已解"),
 ("Q23", "434", "for the the classification; and that and the set",
  "两处重复词（the the；that and the set 中 that 为衍字）",
  "照译并顺句，登记 errata E03", "语法", "已解"),
 ("Q24", "527", "p^{-1}(\\La_0)",
  "上下文定义的紧合映射是 m: \\Gr\\tilde\\times\\Gr\\to\\Gr，此处写法应为 m^{-1}",
  "照原文写 p^{-1}，加译者按，登记 errata E04", "记号", "已解"),
 ("Q25", "564", "correction definition; we do not loss; topologically problems",
  "三处笔误：correction→correct、loss→lose、topologically→topological",
  "按原意译出，登记 errata E05", "拼写", "已解"),
 ("Q26", "674", "(\\mE_r,\\beta_1\\cdots\\beta_r)",
  "修正链 E:chain mod 的最后一段箭头记作 \\beta_0，复合应写 \\beta_0\\cdots\\beta_{r-1}",
  "照译并按原式保留，加译者按，登记 errata E06", "下标", "已解"),
 ("Q27", "813", "h(\\Gr_{\\mmu})(n)\\otimes h(\\Gr_{\\nu_\\bullet})(n)",
  "左因子应为 h(\\Gr_{\\mmu})(m)，原文两处都写 n",
  "照译，登记 errata E07", "下标", "已解"),
 ("Q28", "848", "\\La_0=\\mO_2",
  "第二条链的基应为 \\mO^2，原文写作 \\mO_2",
  "照译并加译者按，登记 errata E08", "记号", "已解"),
 ("Q29", "862", "\\Gr_{\\omega_1,\\omega_1*}^0, \\Gr_{\\omega_1^*,\\omega_2}^0",
  "前者星号位置错，后者下标应为 \\omega_1",
  "译文按上下文写作 \\Gr_{\\omega_1,\\omega_1^*}^0 与 \\Gr_{\\omega_1^*,\\omega_1}^0，加译者按，登记 errata E09", "下标", "已解"),
]

with io.open(yi, "a", encoding="utf-8", newline="") as f:
    for r in rows:
        f.write("\t".join(r) + "\n")

gl = os.path.join(work, "glossary.tsv")
terms = [
 ("cocharacter", "余特征标", "A", "§2.1"),
 ("uniformizer", "一致化元", "A", "§2.1"),
 ("spherical Hecke algebra", "球面 Hecke 代数", "A", "§2.1"),
 ("modification", "修正", "A", "§2.1"),
 ("perfection", "完全化", "A", "§2.1"),
 ("perfect $k$-algebra", "完全 $k$-代数", "A", "§2.1"),
 ("jet group", "射流群", "B", "§2.1"),
 ("loop group", "环路群", "B", "§2.1"),
 ("relative position", "相对位置", "A", "§2.1"),
 ("Schubert cell", "Schubert 胞腔", "A", "§2.1"),
 ("Bruhat order", "Bruhat 序", "A", "§2.1"),
 ("twisted product", "扭积", "A", "§2.1"),
 ("semismall", "半小", "A", "§2.1"),
 ("Künneth", "Künneth", "I", "§2.1"),
 ("motivic", "动机的", "A", "§2.2"),
 ("pure motive", "纯动机", "A", "§2.2"),
 ("idempotent completion", "幂等完备化", "A", "§2.2"),
 ("pseudo-abelian", "伪 Abel", "A", "§2.2"),
 ("Chow group", "Chow 群", "A", "§2.2"),
 ("commutativity constraint", "交换性约束", "A", "§2.2"),
 ("Tannakian group", "Tannakian 群", "I", "§2.2"),
 ("quasi-minuscule", "拟极小", "A", "§2.2"),
 ("resolution of singularities", "奇点消解", "A", "§2.2"),
 ("deperfection", "去完全化", "I", "§2.2"),
 ("intersection cohomology sheaf", "相交上同调层", "A", "§2.2"),
]

with io.open(gl, "a", encoding="utf-8", newline="") as f:
    for r in terms:
        f.write("\t".join(r) + "\n")

print("ok", len(rows), len(terms))
