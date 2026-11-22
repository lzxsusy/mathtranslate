import io, re, glob, os
BASE = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论'
files = sorted(glob.glob(BASE + r'\源码\chunks\ch*.tex'))
for f in files:
    if f.endswith('ch26.tex'):
        continue
    s = io.open(f, encoding='utf-8').read()
    # strip comments and math
    lines = s.split('\n')
    for i, ln in enumerate(lines, 1):
        t = re.sub(r'(?<!\\)%.*', '', ln)
        t = re.sub(r'\$[^$]*\$', '', t)
        t = re.sub(r'\\[a-zA-Z]+', '', t)
        if re.search(r'[\u4e00-\u9fff]', t):
            continue
        words = re.findall(r'[A-Za-z]{3,}', t)
        if len(words) >= 6:
            print('%s:%d  %s' % (os.path.basename(f), i, ln.strip()[:110]))
