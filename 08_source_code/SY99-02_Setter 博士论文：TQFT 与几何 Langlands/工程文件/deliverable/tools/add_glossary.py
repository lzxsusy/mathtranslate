import io, sys
sys.stdout.reconfigure(encoding="utf-8")
P = r"<本地路径>"
NEW = """electric source\t电性源
magnetic source\t磁性源
electric charge\t电荷
magnetic charge\t磁荷
coweight lattice\t余权格
character lattice\t特征标格
fundamental domain\t基本域
simply laced\t单链（simply laced）
lacing number\t链数（lacing number）
twisted rotation group\t扭转后的转动群
defining representation\t定义表示
trivializing neighborhood\t平凡化邻域
anti-Hermitian\t反厄米的
cohomological TQFT\t上同调型拓扑场论
ghost number\t鬼数
canonical parameter\t正则参数
localization equation\t局域化方程
localization submanifold\t局域化子流形
fixed point locus\t不动点轨迹
principal symbol\t主象征
self-dual 2-form\t自对偶 2-形式
normal coordinates\t法坐标
vertical bundle\t垂直丛
vertical projection\t垂直投影
gauge-covariant derivative\t规范协变导数
Cartan differential\tCartan 微分
symmetric algebra\t对称代数
moduli problem\t模问题
off-shell\t离壳
nonminimal term\t非极小项
flat variety\t平坦簇
screen distribution\t屏幕分布
transverse distribution\t横截分布
generalized metric\t广义度规
equivariant Maslov index\t等变 Maslov 指标
hyperkähler quotient\t超 Kähler 商
low-action configuration\t低作用量构形
truncated action\t截断作用量
neutral signature\t中性号差
generalized tangent bundle\t广义切丛
generalized complex structure\t广义复结构
allowed pair\t允许对（allowed pair）
coisotropic\t余迷向的
isotropic\t迷向的
Lagrangian subbundle\t拉格朗日子丛
"""
lines = [l for l in io.open(P, encoding="utf-8").read().splitlines() if l.strip()]
have = {l.split("\t")[0] for l in lines}
added = 0
for l in NEW.splitlines():
    if not l.strip():
        continue
    k = l.split("\t")[0]
    if k not in have:
        lines.append(l)
        have.add(k)
        added += 1
io.open(P, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print("glossary entries:", len(lines), "added:", added)
