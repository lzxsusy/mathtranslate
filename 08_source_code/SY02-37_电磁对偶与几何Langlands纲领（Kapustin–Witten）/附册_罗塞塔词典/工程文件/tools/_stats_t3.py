import re, sys
p = r"C:\Users\admin\Downloads\KW06_work\rosetta\entries\t3-hitchin.tex"
s = open(p, encoding='utf-8').read()
words = re.findall(r'\\begin\{word\}\{(.*?)\}\{(.*?)\}\{(.*?)\}\{(.*?)\}(.*?)\\end\{word\}', s, re.S)
req = ['mathdef','mathex','physdef','physex','bridge','intuit','pitfall']
uni = '−×≤≥≠∈∀∃∑∫∞∂∇√±⊗⊕⟨⟩⊂⊃→⇒↦≅≈∖'
print('entries:', len(words))
for i, (cn, en, tag, anchor, body) in enumerate(words, 1):
    n = len(re.findall(r'[\u4e00-\u9fff]', body))
    missing = [r for r in req if ('\\%s{' % r) not in body]
    dup = [r for r in req if body.count('\\%s{' % r) > 1]
    bad = [c for c in set(body) if c in uni]
    print(i, cn.strip(), '| hans=%d' % n, '| anchor=%s' % anchor.strip(), '| missing=%s' % missing, '| dup=%s' % dup, '| uni=%s' % bad)
print('unicode-all:', [c for c in set(s) if c in uni])
