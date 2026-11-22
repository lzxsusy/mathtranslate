import re, io
p = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论\工程文件\work\原文\samplez.tex'
src = io.open(p, encoding='utf-8').read()
lines = src.split('\n')
# region from line 6912 to 7937 (1-based inclusive)
region = '\n'.join(lines[6911:7937])
region = re.sub(r'\\iffalse.*?\\fi', '', region, flags=re.S)
out = []
sec = sub = sss = 0
for ln in region.split('\n'):
    if re.search(r'\\section\{', ln):
        sec += 1; sub = 0; sss = 0
        out.append('SEC %d' % sec)
    elif re.search(r'\\subsection\{', ln):
        sub += 1; sss = 0
        out.append('  SUB %d.%d' % (sec, sub))
    elif re.search(r'\\subsubsection\{', ln):
        sss += 1
        out.append('    %d.%d.%d  %s' % (sec, sub, sss, ln.strip()[:45]))
    elif re.match(r'\s*\\begin\{(ex|re|defn|theo|lemma|remark|example|pro|cor|conj)\}', ln):
        sss += 1
        out.append('    %d.%d.%d  %s' % (sec, sub, sss, ln.strip()[:45]))
print('\n'.join(out))
