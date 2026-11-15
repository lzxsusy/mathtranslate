import re, pathlib

def fix_url(u):
    disp = u
    disp = disp.replace('https://', 'https://\\allowbreak{}')
    disp = disp.replace('/show/', '/show/\\allowbreak{}')
    disp = disp.replace('+', '+\\allowbreak{}')
    disp = disp.replace('_', '\\_')
    href = u.replace('_', '\\_').replace('%', '\\%').replace('#', '\\#')
    return '\\href{%s}{\\texttt{%s}}' % (href, disp)

pat = re.compile(r'\\url\{(https://ncatlab\.org/nlab/show/[^}]+)\}')

for p in sorted(pathlib.Path(r'<HOME>\Downloads\GL_work\源码\chunks').glob('*.tex')):
    t = p.read_text(encoding='utf-8')
    n = pat.sub(lambda m: fix_url(m.group(1)), t)
    if n != t:
        p.write_text(n, encoding='utf-8')
        print('fixed', p.name, len(pat.findall(t)))
