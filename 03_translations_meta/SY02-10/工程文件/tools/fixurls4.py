import re, pathlib

def disp_of(u):
    out = []
    for ch in u:
        out.append(ch)
        if ch in '/+.':
            out.append('\\allowbreak{}')
    return ''.join(out)

pat = re.compile(r'\\href\{(https://ncatlab\.org/nlab/show/[^}]+)\}\{\\texttt\{.*?\}\}', re.S)

for p in sorted(pathlib.Path(r'<HOME>\Downloads\GL_work\源码\chunks').glob('*.tex')):
    t = p.read_text(encoding='utf-8')
    n = pat.sub(lambda m: '\\href{%s}{\\texttt{%s}}' % (m.group(1), disp_of(m.group(1).replace('\\_', '_'))), t)
    if n != t:
        p.write_text(n, encoding='utf-8')
        print('fixed', p.name, len(pat.findall(t)))
