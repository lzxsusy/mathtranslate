import io
p = 'src/preamble.tex'
s = io.open(p, encoding='utf-8').read()
if 'cleardoublepage' not in s:
    s = s.rstrip('\n') + '''
% ---------- 分页 ----------
% openany 应让章首接排，但 ctexbook 仍会因 \\cleardoublepage 产生空白页；
% 直接把它降级为 \\clearpage，避免书里出现只带页眉的空白页。
\\let\\cleardoublepage\\clearpage
'''
    io.open(p, 'w', encoding='utf-8').write(s)
    print('appended')
else:
    print('exists')
