import re, io
BASE = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论'
t = io.open(BASE + r'\工程文件\work\条款索引_raw.md', encoding='utf-8').read()
cur = None
ks = {}
for line in t.split('\n'):
    m = re.match(r'### (§|附录 )(\S+)', line)
    if m:
        cur = m.group(2); ks.setdefault(cur, [])
    m2 = re.search(r'(?:段|注|例|定理|定义|引理) [A]?(\d+)\.(\d+)\.(\d+)', line)
    if m2 and cur:
        ks[cur].append(int(m2.group(3)))
for sec in ks:
    v = sorted(ks[sec])
    gaps = [i for i in range(1, (max(v) if v else 0) + 1) if i not in v]
    print(sec, 'n=%d max=%s gaps=%s' % (len(v), max(v) if v else '-', gaps))
