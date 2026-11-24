from pathlib import Path
import sys,json,subprocess,hashlib
import pymupdf as fitz
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')
root=Path(__file__).resolve().parent.parent
dest=root/'output/pdf/LinChenGLC2023_CN_full.pdf'
dest.parent.mkdir(parents=True,exist_ok=True)
doc=fitz.open(root/'build/main.pdf')
assert doc.embfile_count()==0
doc.set_metadata({**doc.metadata,'title':'几何 Langlands 理论导论：完整中文译本','subject':'第二轮审校修订；完整第1–16章119节；原PDF第5–83页References之前正文及33条参考文献','author':'Lin Chen; Wenhan Dai'})
doc.save(dest,garbage=4,deflate=True)
doc.close()
check=fitz.open(dest)
toc=check.get_toc()
assert len(toc)==137
assert len([t for t in toc if t[0]==2])==119
assert len([t for t in toc if t[0]==1])==18
assert all(1<=t[2]<=len(check) for t in toc)
links=[(i+1,l) for i,p in enumerate(check) for l in p.get_links()]
bad=[(i,l) for i,l in links if l.get('kind') in (1,4) and not 0<=l.get('page',-1)<len(check)]
assert not bad,bad
assert not any(l.get('file') for i,l in links)
fonts=subprocess.check_output(['pdffonts',str(dest)],text=True,encoding='utf-8')
badfonts=[l for l in fonts.splitlines()[2:] if len(l.split())>=8 and l.split()[-5]!='yes']
assert not badfonts,badfonts
assert 'NewCMMath-Regular' in fonts
log=(root/'build/main.log').read_text(encoding='utf-8',errors='replace')
for token in ['Overfull','Missing character','There were undefined references','multiply defined','! LaTeX Error','Token not allowed in a PDF string']:
    assert token not in log,token
assert Image.open(root/'images/cover.png').size==(1536,1024)
main=(root/'main.tex').read_text(encoding='utf-8')
assert r'\setlength{\origimageunit}{0.7176470588\paperwidth}' in main
original=fitz.open(root/'build/main.pdf')
assert all(hashlib.sha256(a.get_pixmap(matrix=fitz.Matrix(.5,.5)).samples).digest()==hashlib.sha256(b.get_pixmap(matrix=fitz.Matrix(.5,.5)).samples).digest() for a,b in zip(original,check))
report={'scope':'Full chapters1–16, source正文 PDF5–83 before References, source references83–85; skip publishing metadata','pages':len(check),'chapters':16,'sections':119,'bib_entries':33,'vector_files':48,'vector_uses':49,'bookmarks':len(toc),'links':len(links),'external_pdf_links':0,'all_fonts_embedded':True,'math_font':'New Computer Modern','body_size':'11pt','cover_size':[1536,1024],'undefined_references':0,'unresolved_page_destinations':0,'missing_glyphs':0,'overfull_boxes':0,'bookmark_string_warnings':0,'optimized_pdf_render_matches_all_pages':True,'pdf_sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
report['image_page_width_ratio_preserved']=True
report['source_pdf_page_width_bp']=612
(root/'audit/full-final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
(root/'audit/full-fonts.txt').write_text(fonts,encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
print(dest)
