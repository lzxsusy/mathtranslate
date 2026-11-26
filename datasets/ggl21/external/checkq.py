import re,sys,glob,os
LIG={"\ufb00":"ff","\ufb01":"fi","\ufb02":"fl","\ufb03":"ffi","\ufb04":"ffl","\ufb05":"ft","\ufb06":"st"}
def norm(s):
    s="".join(LIG.get(c,c) for c in s).lower()
    return re.sub(r"[^a-z0-9]+","",s)
pages={}
for p in sorted(glob.glob("txt/21/p*.txt")):
    n=int(re.search(r"p(\d+)",os.path.basename(p)).group(1))
    pages[n]=norm(open(p,encoding="utf-8",errors="replace").read())
qs=open(sys.argv[1],encoding="utf-8").read().splitlines()
for q in qs:
    q=q.strip()
    if not q: continue
    hits=[p for p,t in pages.items() if norm(q) and norm(q) in t]
    print(f"{len(q):3d} {hits}  {q}")
