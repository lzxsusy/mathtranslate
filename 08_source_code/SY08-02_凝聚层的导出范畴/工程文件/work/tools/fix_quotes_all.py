import io, glob, os
tot=0
for p in sorted(glob.glob('src/chunks/*.tex')):
    if os.path.basename(p).startswith('_'): continue
    s=io.open(p,encoding='utf-8').read()
    a,b=s.count('\u300c'), s.count('\u300d')
    if a or b:
        n=min(a,b)
        s=s.replace('\u300c','\u201c').replace('\u300d','\u201d')
        io.open(p,'w',encoding='utf-8').write(s)
        print(os.path.basename(p), a, b, '-> replaced')
        tot+=1
print('files touched', tot)
