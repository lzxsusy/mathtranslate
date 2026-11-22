import io, re, glob, os
BASE = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论'
src = io.open(BASE + r'\工程文件\work\原文\samplez.tex', encoding='utf-8').read()

# drop \iffalse ... \fi blocks (they are commented-out text in the original)
def strip_iffalse(s):
    out, i = [], 0
    while True:
        j = s.find(r'\iffalse', i)
        if j < 0:
            out.append(s[i:]); break
        out.append(s[i:j])
        k = s.find(r'\fi', j)
        i = k + 3
    return ''.join(out)

src2 = strip_iffalse(src)
orig = set(re.findall(r'\\label\{([^}]*)\}', src2))

mine = set()
for f in glob.glob(BASE + r'\源码\chunks\ch*.tex'):
    mine |= set(re.findall(r'\\label\{([^}]*)\}', io.open(f, encoding='utf-8').read()))

print('orig labels:', len(orig), ' mine labels:', len(mine))
print('missing in mine:', sorted(orig - mine))
print('extra in mine:', sorted(mine - orig))

# also: every \ref/\eqref in chunks must be in mine
bad = set()
for f in glob.glob(BASE + r'\源码\chunks\ch*.tex'):
    s = io.open(f, encoding='utf-8').read()
    for k in re.findall(r'\\(?:eq)?ref\{([^}]*)\}', s):
        if k not in mine:
            bad.add((os.path.basename(f), k))
print('dangling refs:', sorted(bad))
