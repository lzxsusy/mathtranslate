import io, subprocess, sys
f=sys.argv[1]
lines=io.open(f,encoding='utf-8').read().split('\n')
XEL=r"C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"
def test(n):
    body='\n'.join(lines[:n])
    io.open('t_b.tex','w',encoding='utf-8').write('\\documentclass{article}\\usepackage{amsmath}\\usepackage{amssymb}\\input{preamble}\n\\begin{document}\n'+body+'\n\\end{document}\n')
    subprocess.run([XEL,'-interaction=batchmode','-file-line-error','t_b.tex'],capture_output=True)
    log=io.open('t_b.log',encoding='utf-8',errors='replace').read()
    return '! ' in log
lo,hi=1,len(lines)
print('full errors?',test(len(lines)))
while lo<hi:
    mid=(lo+hi)//2
    if test(mid): hi=mid
    else: lo=mid+1
print('first error at line:',lo)
for i in range(max(0,lo-8),min(len(lines),lo+2)): print(i+1, lines[i][:120])
