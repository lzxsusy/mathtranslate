from pathlib import Path
import csv, hashlib, json, re, subprocess, sys, unicodedata
from pypdf import PdfReader
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('<本地路径>  Lecture 1~23.pdf')

def groups(text):
    result = []
    depth = 0
    start = 0
    for i, char in enumerate(text):
        if char == '{':
            if depth == 0:
                start = i + 1
            depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0:
                result.append(text[start:i])
    return result

labels = {}
for line in (ROOT/'build/main.aux').read_text(encoding='utf-8').splitlines():
    if line.startswith(r'\newlabel{'):
        fields = groups(line)
        if len(fields) >= 2:
            values = groups(fields[1])
            if len(values) >= 2:
                labels[fields[0]] = values

objects = []
lecture = 0
source_reader = PdfReader(SOURCE)
for number, page in enumerate(source_reader.pages, 1):
    text = unicodedata.normalize('NFKC', page.extract_text() or '')
    head = re.match(r'\s*Lecture\s*(\d+)\.', text)
    if head:
        lecture = int(head[1])
    for match in re.finditer(r'(?m)^\s*(Theorem|Lemma|Corollary|Proposition|Conjecture|Definition|Example|Remark|Question|Problem)\s*(\d+)\.(\d+)(?:\.|\s*\()', text):
        kind, section, ordinal = match.groups()
        label = f'L{lecture}S{section}O{ordinal}'
        objects.append({'source_page':number, 'lecture':lecture, 'type':kind,
                        'original_number':section+'.'+ordinal, 'label':label})
assert len(objects) == 299, len(objects)
numbering_errors = [x for x in objects if x['label'] not in labels or labels[x['label']][0] != x['original_number']]
assert not numbering_errors, numbering_errors
assert {int(x[4:]) for x in labels if x.startswith('src:')} == set(range(1,199))
source_review = json.loads((ROOT/'audit/source-review.json').read_text(encoding='utf-8'))
assert set(map(int, source_review)) == set(range(1,199))
assert all(all(x[k] for k in ['source_png_seen','paragraphs_compared','formulas_compared']) for x in source_review.values())

chapters = sorted((ROOT/'chapters').glob('lecture*.tex'))
assert len(chapters) == 23
tex = '\n'.join(p.read_text(encoding='utf-8') for p in chapters)
assert tex.count(r'\begin{exercise*}') == 10
assert tex.count(r'\includegraphics') == 61
assert '\ufffd' not in tex
assert not re.search('译者注|勘误说明|补充说明|原书.*笔误', tex)

formulas = []
for path in chapters:
    content = path.read_text(encoding='utf-8')
    lecture = int(path.stem[-2:])
    for match in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}', content, re.S):
        tag = re.search(r'\\tag\{([^}]+)\}',match[0])
        label = re.search(r'\\label\{([^}]+)\}',match[0])
        if tag:
            assert label, (path,tag[1])
            assert label[1] in labels, label[1]
            actual = labels[label[1]][0].strip('{}')
            assert actual == tag[1], (label[1],actual,tag[1])
            formulas.append({'lecture':lecture,'original_tag':tag[1],'label':label[1],'compiled_tag':actual})
assert len(formulas) == 80

pdf_path = ROOT/'build/main.pdf'
pdf = PdfReader(pdf_path)
destinations = pdf.named_destinations
page_refs = {(p.indirect_reference.idnum,p.indirect_reference.generation) for p in pdf.pages}
broken = []
links = index_links = 0
for number,page in enumerate(pdf.pages,1):
    for ref in page.get('/Annots',[]):
        annot = ref.get_object()
        if annot.get('/Subtype') != '/Link':
            continue
        links += 1
        target = annot.get('/Dest')
        action = annot.get('/A')
        if action:
            action = action.get_object()
            if action.get('/S') != '/GoTo':
                continue
            target = action.get('/D')
        if isinstance(target,str):
            index_links += target.startswith('page.')
            if target not in destinations:
                broken.append([number,str(target)])
        elif isinstance(target,list) and target:
            ref = target[0]
            if hasattr(ref,'idnum'):
                if (ref.idnum,ref.generation) not in page_refs:
                    broken.append([number,str(target)])
            elif isinstance(ref,int) and not (0 <= ref < len(pdf.pages)):
                broken.append([number,str(target)])
        else:
            broken.append([number,str(target)])
assert not broken, broken

toc = (ROOT/'build/main.toc').read_text(encoding='utf-8')
sections = len(re.findall(r'\\contentsline \{section\}',toc))
expected_sections = len(re.findall(r'\\section\{',tex))
assert sections == expected_sections
assert len(re.findall(r'\\contentsline \{chapter\}',toc)) == 25
def outline_entries(items,level=0):
    result=[]
    for item in items:
        if isinstance(item,list):
            result.extend(outline_entries(item,level+1))
        else:
            result.append({'title':str(item.title),'level':level,'pdf_page':pdf.get_destination_page_number(item)+1})
    return result
outlines = outline_entries(pdf.outline)
assert len(outlines) == 25 + sections
assert all(x['level'] in [0,1] for x in outlines)
assert all(1 <= x['pdf_page'] <= len(pdf.pages) for x in outlines)

log = (ROOT/'build/main.log').read_text(encoding='utf-8',errors='replace')
log_counts = {'overfull':len(re.findall(r'Overfull \\[hv]box',log)),
              'missing_glyphs':log.count('Missing character:'),
              'undefined_references':len(re.findall(r'(?:Reference|Hyper reference).*undefined',log)),
              'font_substitution_warnings':log.count('LaTeX Font Warning'),
              'duplicate_destination_warnings':len(re.findall(r'destination.*(?:same identifier|duplicate)',log,re.I))}
assert not any(log_counts.values()), log_counts
fonts = subprocess.run(['pdffonts',str(pdf_path)],check=True,capture_output=True).stdout.decode('utf-8',errors='replace')
(ROOT/'audit/font-embedding.txt').write_text(fonts,encoding='utf-8')
font_checks=[]
for line in fonts.splitlines()[2:]:
    match=re.search(r'\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$',line)
    if match:
        font_checks.append((line.split()[0],match[1]=='yes'))
assert font_checks and all(x[1] for x in font_checks)
assert any('NewCMMath' in x[0] for x in font_checks)
assert Image.open(ROOT/'images/cover.png').size == (1536,1024)

figure_review=json.loads((ROOT/'audit/figure-review-final.json').read_text(encoding='utf-8'))
assert len(figure_review) == 61
assert all(x.get('visually_checked') and x['raster_images']==0 for x in figure_review)
for figure in figure_review:
    assert hashlib.sha256((ROOT/'images'/figure['file']).read_bytes()).hexdigest() == figure['sha256']
    match=re.search(r'\\includegraphics\[width=([.\d]+)\\paperwidth\]\{images/'+re.escape(figure['file'])+r'\}',tex)
    assert match, figure['file']
    assert abs(float(match[1])-figure['width_fraction']) < 0.00011, (figure['file'],match[1],figure['width_fraction'])

visual=json.loads((ROOT/'audit/visual-reviewed.json').read_text(encoding='utf-8'))
digest=hashlib.sha256(pdf_path.read_bytes()).hexdigest()
assert visual['pdf_sha256']==digest
assert visual['reviewed_pdf_pages']==list(range(1,len(pdf.pages)+1))
assert visual['unresolved_visual_issues']==[]

with (ROOT/'reference-map.tsv').open('w',encoding='utf-8',newline='') as stream:
    writer=csv.writer(stream,delimiter='\t')
    writer.writerow(['原PDF页','讲','对象类型','原编号','译本编号','译本正文页','标签'])
    for obj in objects:
        writer.writerow([obj['source_page'],obj['lecture'],obj['type'],obj['original_number'],*labels[obj['label']][:2],obj['label']])
with (ROOT/'page-map.tsv').open('w',encoding='utf-8',newline='') as stream:
    writer=csv.writer(stream,delimiter='\t')
    writer.writerow(['原PDF页','译本页标记','源页阅读','逐段翻译','逐页对照复核'])
    for number in range(1,199):
        writer.writerow([number,labels[f'src:{number}'][1],'完成','完成','完成'])

result={'edition':'全书复核修订版','source_pages_reviewed':198,'lectures':23,
        'pdf_pages':len(pdf.pages),'numbered_original_objects':299,'numbering_errors':numbering_errors,
        'unnumbered_original_exercises':10,'numbered_formulas':80,'sections':sections,
        'bookmarks':len(outlines),'links':links,'index_page_links':index_links,'broken_links':broken,
        'vector_diagrams':61,'restored_boxed_diagrams':5,'crop_boundaries_revised':34,
        'font_resources_checked':len(font_checks),'fonts_not_embedded':[],
        'cover_size':[1536,1024],'visual_reviewed_pdf_pages':len(pdf.pages),
        'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'pdf_sha256':digest,**log_counts}
(ROOT/'audit/validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'audit/object-map.json').write_text(json.dumps(objects,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'audit/formula-map.json').write_text(json.dumps(formulas,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'audit/bookmark-map.json').write_text(json.dumps(outlines,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
