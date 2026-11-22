import io, re, os
BASE = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论'
bbl = io.open(BASE + r'\工程文件\work\原文\samplez.bbl', encoding='utf-8').read()

# keep everything from \begin{thebibliography} to \end{thebibliography}
m = re.search(r'\\begin\{thebibliography\}.*?\\end\{thebibliography\}', bbl, re.S)
body = m.group(0)

# strip \MR{...} (amsalpha MR macros) since we do not load the MR link machinery
body = re.sub(r'\s*\\MR\{[^}]*\}', '', body)

header = ('\\clearpage\n'
          '\\phantomsection\n'
          '\\addcontentsline{toc}{section}{参考文献}\n'
          '\\renewcommand{\\refname}{参考文献}\n')
tail_notes = ('\n\\vspace{1em}\n\\noindent\\footnotesize 说明：文献条目照原文排印，未作翻译；'
              '方括号内为原文献表所用的 alpha 标号。\n')

io.open(BASE + r'\源码\chunks\ch26.tex', 'w', encoding='utf-8').write(header + body + tail_notes)
print('wrote ch26.tex', len(body), 'chars')
