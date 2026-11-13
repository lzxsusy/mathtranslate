# append_glossary.py — 只追加新术语，不改动已有行（Lead 统稿用）
import io, os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'glossary.tsv')
new = [
    ("rigid geometry", "刚性几何", "ST11 术语，区别于 rigid object"),
    ("worldsheet", "世界面", ""),
    ("spacetime", "时空", ""),
    ("background field", "背景场", ""),
    ("invertible", "可逆的", "invertible twist 可逆扭"),
    ("collar", "领", "collar neighbourhood 领邻域"),
    ("delooping", "去环", "deloop 去环"),
    ("anomaly", "反常", "'t Hooft anomaly 保留人名"),
    ("anomalous field theory", "反常场论", ""),
    ("projective representation", "射影表示", ""),
    ("level", "级别", "H^4(BG;Z) 中的 [l]"),
    ("derived scheme", "导出概形", ""),
    ("nonabelian theta function", "非 Abel theta 函数", ""),
    ("free loop space", "自由环路空间", "LR^n"),
    ("concordance", "concordance（协调）", "保留英文，附中文"),
    ("2-category", "2-范畴", ""),
    ("complexification", "复化", ""),
    ("super vector space", "超向量空间", ""),
    ("symmetric monoidal functor", "对称幺半函子", ""),
    ("Euclidean bordism category", "欧几里得配边范畴", "EBord_d"),
    ("super Euclidean", "超欧几里得", "EBord_{d|delta}"),
    ("topological index", "拓扑指标", ""),
    ("analytic index", "解析指标", ""),
    ("spin geometry", "spin 几何", ""),
    ("flat metric", "平坦度量", ""),
    ("moduli space", "模空间", ""),
    ("landscape", "景观", "string landscape"),
    ("topological phase", "拓扑相", ""),
    ("monstrous moonshine", "魔群月光", ""),
    ("conformal net", "共形网", ""),
    ("factorization algebra", "因子化代数", ""),
    ("loop group", "环路群", ""),
    ("positive energy representation", "正能表示", ""),
    ("WZW model", "WZW 模型", "Wess-Zumino-Witten"),
    ("elliptic power operation", "椭圆幂运算", ""),
    ("twisted sector", "扭扇区", ""),
    ("mirror symmetry", "镜像对称", ""),
    ("topological twist", "拓扑扭", "与本文 twist（扭）不同"),
    ("'t Hooft anomaly", "'t Hooft 反常", ""),
    ("section", "截面", ""),
    ("sheaf", "层", ""),
    ("compact Lie group", "紧 Lie 群", ""),
    ("incoming/outgoing", "入射／出射", ""),
    ("double cover", "二重覆盖", ""),
]

with io.open(path, 'r', encoding='utf-8') as f:
    existing = f.read()
lines = [ln for ln in existing.split('\n') if ln.strip()]
have = set(ln.split('\t')[0] for ln in lines)
added = 0
for en, zh, note in new:
    if en in have:
        continue
    lines.append('\t'.join([en, zh, note]))
    added += 1
with io.open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(lines) + '\n')
print('total lines =', len(lines), '| added =', added)
