import io, re, glob, os
BASE = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论'

files = sorted(glob.glob(BASE + r'\源码\chunks\ch*.tex'))
banned = ['被', '进行', '对于', '使得']
patterns = {
    '被…所': r'被[^。，；]{0,12}所',
    '进行…的': r'进行[^。，；]{0,8}的',
    '对于…而言': r'对于[^。，；]{0,15}而言',
    '使得…得以': r'使得[^。，；]{0,15}得以',
    'ASCII 引号': r'(?<![0-9a-zA-Z])"|"(?![0-9a-zA-Z])',
    '半角括号包中文': r'\([^)]*[\u4e00-\u9fff][^)]*\)',
    '连续空格': r'  +',
}
totals = {k: 0 for k in patterns}
for f in files:
    s = io.open(f, encoding='utf-8').read()
    # 去掉注释行与数学环境内的内容，粗略处理
    for k, p in patterns.items():
        hits = re.findall(p, s)
        if hits:
            totals[k] += len(hits)
            if k in ('被…所', '对于…而言', '使得…得以'):
                for m in re.finditer(p, s):
                    ln = s[:m.start()].count('\n') + 1
                    print('%s:%d %s | %s' % (os.path.basename(f), ln, k, m.group(0).replace('\n', ' ')))
print(totals)
