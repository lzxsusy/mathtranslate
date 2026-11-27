# -*- coding: utf-8 -*-
import io,re,os
P=r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\datasets\encyclopedia\pages\geometric-langlands.md"
t=io.open(P,encoding='utf-8').read()
refs=re.findall(r"\{\{card:([^}]+)\}\}",t)
print("macro refs",len(refs),"unique",len(set(refs)))
start=t.index("## 附录 B"); end=t.index("## 附录 C")
b=t[start:end]
bids=re.findall(r"^\| `([^`]+)` \|",b,re.M)
print("B ids",len(bids))
print("in B not cited:",sorted(set(bids)-set(refs)))
print("cited not in B:",sorted(set(refs)-set(bids)))
# compiled_from ids
fm=t.split('---',2)[1]
cf=re.findall(r"- id: (\S+)",fm)
print("compiled",len(cf))
print("cited but not compiled:",sorted(set(refs)-set(cf)))
print("compiled but not cited:",sorted(set(cf)-set(refs)))
