import glob,re
n=0
for f in glob.glob('src/chunks/*.tex')+glob.glob('src/*.tex')+glob.glob('src/frontmatter/*.tex'):
    s=open(f,encoding='utf-8').read()
    t=re.sub(r'\\ot(?![A-Za-z])', r'\\otimes', s)
    if t!=s:
        open(f,'w',encoding='utf-8').write(t); n+=1; print('fixed',f)
print('files',n)
