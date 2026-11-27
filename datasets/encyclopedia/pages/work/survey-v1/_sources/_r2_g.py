# -*- coding: utf-8 -*-
import io,re,sys
src=sys.argv[1]; keys=sys.argv[2].split('|'); C=int(sys.argv[3]) if len(sys.argv)>3 else 3
t=io.open(src,encoding='utf-8').read().splitlines(); page=0
for i,l in enumerate(t):
    m=re.match(r'===== PAGE (\d+) =====',l.strip())
    if m: page=int(m.group(1)); continue
    if any(k in l for k in keys):
        print("--- p%d L%d"%(page,i+1))
        for j in range(max(0,i-C),min(len(t),i+C+1)): print("  ",t[j])
