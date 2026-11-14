import fitz, sys

doc = fitz.open(r'C:\Users\admin\Downloads\GL_work\源码\main.pdf')
for i, page in enumerate(doc, 1):
    h = page.rect.height
    blocks = [b for b in page.get_text('blocks') if b[4].strip()]
    if not blocks:
        print(f'p{i}: EMPTY'); continue
    # 排除页脚（页码）与页眉：h=842, 页脚在 y>790, 页眉 y<70
    body = [b for b in blocks if 70 < b[1] < 790 and not b[4].strip().isdigit()]
    bottom = max((b[3] for b in body), default=0)
    gap = 790 - bottom
    if gap > 120:
        print(f'p{i}: 正文底部 y={bottom:.0f}, 距页脚带 {gap:.0f}pt')
