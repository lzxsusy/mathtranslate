# -*- coding: utf-8 -*-
"""Extract text (with script markers) + page images from BD Hitchin PDF.

- code->glyphname from the ORIGINAL AMS Type1 fonts in MiKTeX (the embedded
  subset fonts had their glyph names rewritten by pdfTeX, which is why the
  naive text layer renders \\sum as "P" etc.)
- glyphname -> unicode via fontTools.agl + a manual table for TeX names
- superscript/subscript reconstructed from font size + baseline shift
"""
import os, re, sys, json
import pymupdf
from fontTools.agl import toUnicode as agl

PDF = r"C:\Users\admin\Desktop\QuantizationHitchin(1).pdf"
ROOT = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-14_Hitchin可积系统的量子化与Hecke特征层"
WORK = os.path.join(ROOT, "工程文件", "work")
FONTDIR = r"C:\Users\admin\AppData\Local\Programs\MiKTeX\fonts\type1\public\amsfonts"
DPI = 170

# ---------------------------------------------------------------- glyph names
MANUAL = {
    'mapsto': '↦', 'angbracketleft': '⟨', 'angbracketright': '⟩',
    'negationslash': '≠', 'similarequal': '≃', 'wreathproduct': '≀',
    'lscript': 'ℓ', 'flat': '♭', 'natural': '♮', 'epsilon1': 'ε',
    'arrowhookleft': '↩', 'arrowhookright': '↪', 'openbullet': '◦',
    'circlemultiply': '⊗', 'circleplus': '⊕', 'circledot': '⊙',
    'circleminus': '⊖', 'circledivide': '⊘', 'circlecopyrt': '©',
    'equivasymptotic': '≍', 'reflexsubset': '⊆', 'reflexsuperset': '⊇',
    'precedesequal': '⪯', 'followsequal': '⪰', 'approxequal': '≈',
    'lessmuch': '≪', 'greatermuch': '≫', 'precedes': '≺', 'follows': '≻',
    'arrownortheast': '↗', 'arrowsoutheast': '↘', 'arrownorthwest': '↖',
    'arrowsouthwest': '↙', 'arrowboth': '↔', 'arrowbothv': '↕',
    'arrowdblleft': '⇐', 'arrowdblright': '⇒', 'arrowdblup': '⇑',
    'arrowdbldown': '⇓', 'arrowdblboth': '⇔', 'arrowdblbothv': '⇕',
    'proportional': '∝', 'prime': '′', 'infinity': '∞', 'element': '∈',
    'owner': '∋', 'triangle': '△', 'triangleinv': '▽', 'universal': '∀',
    'existential': '∃', 'logicalnot': '¬', 'emptyset': '∅',
    'Rfractur': 'ℜ', 'Ifractur': 'ℑ', 'latticetop': '⊤', 'perpendicular': '⊥',
    'aleph': 'ℵ', 'union': '∪', 'intersection': '∩', 'unionmulti': '⊎',
    'logicaland': '∧', 'logicalor': '∨', 'turnstileleft': '⊢', 'turnstileright': '⊣',
    'floorleft': '⌊', 'floorright': '⌋', 'ceilingleft': '⌈', 'ceilingright': '⌉',
    'bardbl': '‖', 'backslash': '\\', 'bar': '|', 'radical': '√',
    'coproduct': '∐', 'nabla': '∇', 'integral': '∫', 'unionsq': '⊔',
    'intersectionsq': '⊓', 'subsetsqequal': '⊆', 'supersetsqequal': '⊇',
    'section': '§', 'dagger': '†', 'daggerdbl': '‡', 'paragraph': '¶',
    'club': '♣', 'diamond': '♦', 'heart': '♥', 'spade': '♠',
    'summation': '∑', 'product': '∏', 'asteriskmath': '∗',
    'periodcentered': '·', 'minus': '−', 'multiply': '×', 'plusminus': '±',
    'minusplus': '∓', 'divide': '÷', 'diamondmath': '⋄', 'bullet': '•',
    'lessequal': '≤', 'greaterequal': '≥', 'propersubset': '⊂',
    'propersuperset': '⊃', 'similar': '∼', 'equivalence': '≡',
    'parenleftbig': '(', 'parenrightbig': ')', 'parenleftBig': '(',
    'parenrightBig': ')', 'parenleftBigg': '(', 'parenrightBigg': ')',
    'bracketleftbig': '[', 'bracketrightbig': ']', 'bracketleftBig': '[',
    'bracketrightBig': ']', 'braceleftbig': '{', 'bracerightbig': '}',
    'braceleftBig': '{', 'bracerightBig': '}', 'braceleftbt': '}',
    'braceleftmid': '{', 'bracelefttp': '{', 'bracerighttp': '}',
    'bracerightmid': '}', 'bracerightbt': '}',
    'summationdisplay': '∑', 'summationtext': '∑', 'productdisplay': '∏',
    'producttext': '∏', 'integraldisplay': '∫', 'integraltext': '∫',
    'uniondisplay': '⋃', 'uniontext': '⋃', 'unionbig': '⋃',
    'intersectiondisplay': '⋂', 'intersectiontext': '⋂',
    'coproddisplay': '∐', 'coprodtext': '∐',
    'vextendsingle': '|', 'vextenddouble': '‖',
    'hatwide': '^', 'hatwider': '^', 'hatwidest': '^',
    'tildewide': '~', 'tildewider': '~', 'tildewidest': '~',
    'planckover2pi1': 'ℏ', 'multicloseleft': '⟫', 'multicloseleft?': '≫',
    'circlemultiplytext': '⊗', 'circledottext': '⊙',
    'circleplusdisplay': '⊕', 'circleplustext': '⊕',
    'logicalandtext': '∧', 'logicalortext': '∨',
    'unionsqtext': '⊔', 'unionsqdisplay': '⊔',
    'arrowtp': '↗', 'arrowbt': '↘', 'arrowvertex': '|',
    'angbracketleftbig': '⟨', 'angbracketrightbig': '⟩',
    'angbracketleftBig': '⟨', 'angbracketrightBig': '⟩',
    'angbracketleftbigg': '⟨', 'angbracketrightbigg': '⟩',
    'slashbig': '/', 'backslashbig': '\\',
    'braceex': '|', 'parenlefttp': '(', 'parenleftbt': '(', 'parenleftex': '|',
    'parenrighttp': ')', 'parenrightbt': ')', 'parenrightex': '|',
    'bracketlefttp': '[', 'bracketleftbt': '[', 'bracketleftex': '|',
    'bracketrighttp': ']', 'bracketrightbt': ']', 'bracketrightex': '|',
    'radicalbig': '√', 'radicalBig': '√', 'radicalbigg': '√', 'radicalBigg': '√',
    'radicalbt': '√', 'radicaltp': '√', 'radicalvertex': '√',
    'dotlessi': 'ı', 'dotlessj': 'ȷ', 'Gamma': 'Γ', 'Delta': 'Δ',
    'Theta': 'Θ', 'Lambda': 'Λ', 'Xi': 'Ξ', 'Pi': 'Π', 'Sigma': 'Σ',
    'Upsilon': 'Υ', 'Phi': 'Φ', 'Psi': 'Ψ', 'Omega': 'Ω',
    'arrowvertexdbl': '‖',
}

PFB_ENCODING_CACHE = {}


def parse_pfb_encoding(path):
    raw = open(path, 'rb').read()
    txt = raw.decode('latin-1', 'replace')
    i = txt.find('/Encoding')
    if i < 0:
        return {}
    seg = txt[i:i + 12000]
    j = seg.find('readonly def')
    if j > 0:
        seg = seg[:j]
    enc = {}
    for code, name in re.findall(r'dup\s+(\d+)\s*/([^\s/]+)\s+put', seg):
        enc[int(code)] = name
    return enc


def font_family(basefont):
    return basefont.split('+')[-1].lower()


def pfb_path(family):
    for sub in ('cm', 'euler', 'symbols', 'cmextra'):
        p = os.path.join(FONTDIR, sub, family + '.pfb')
        if os.path.exists(p):
            return p
    return None


def glyph_to_unicode(name, family):
    if family.startswith('eufm'):
        if len(name) == 1 and name.isalpha():
            if name.islower():
                return chr(0x1D51E + ord(name) - ord('a'))   # fraktur small
            return chr(0x1D504 + ord(name) - ord('A'))       # fraktur cap
    if family.startswith('msbm'):
        if len(name) == 1 and name.isalpha():
            if name.isupper():
                return chr(0x1D538 + ord(name) - ord('A'))
            return chr(0x1D552 + ord(name) - ord('a'))
    if family.startswith('cmcsc'):
        if len(name) == 1 and name.isalpha():
            return name.upper()
    if name in MANUAL:
        return MANUAL[name]
    u = agl(name)
    if u:
        return u
    # big-delimiter variants
    m = re.match(r'(paren|bracket|brace|angbracket)(left|right)', name)
    if m:
        return {'paren': '(', 'bracket': '[', 'brace': '{', 'angbracket': '⟨'}[m.group(1)] if m.group(2) == 'left' else \
               {'paren': ')', 'bracket': ']', 'brace': '}', 'angbracket': '⟩'}[m.group(1)]
    if name.endswith('display') or name.endswith('text') or name.endswith('big') or name.endswith('Big'):
        stem = re.sub(r'(display|text|big|Big|bigg|Bigg|bt|tp|mid|ex|vertex)$', '', name)
        if stem in MANUAL:
            return MANUAL[stem]
    return None


def build_tables(doc):
    """basefont family -> {code: unicode or None}"""
    fams = set()
    for i in range(doc.page_count):
        for f in doc.get_page_fonts(i):
            fams.add(font_family(f[3]))
    tables = {}
    missing = {}
    for fam in sorted(fams):
        p = pfb_path(fam)
        if not p:
            missing[fam] = 'no pfb'
            continue
        if fam not in PFB_ENCODING_CACHE:
            PFB_ENCODING_CACHE[fam] = parse_pfb_encoding(p)
        enc = PFB_ENCODING_CACHE[fam]
        tbl = {}
        for code, name in enc.items():
            u = glyph_to_unicode(name, fam)
            if u is None:
                missing.setdefault(fam, []).append(name)
                u = '\uFFFD'
            if len(u) != 1:
                # keep unique placeholder for multi-char results
                u = u[0]
            tbl[code] = u
        tables[fam] = tbl
    return tables, missing


# ---------------------------------------------------------------- page text
HEADER_RE = re.compile(r'^(HITCHIN.S INTEGRABLE SYSTEM|A\. BEILINSON AND V\. DRINFELD)$')
LIG = {'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬀ': 'ff', 'ﬃ': 'ffi', 'ﬄ': 'ffl', 'ﬅ': 'ft', 'ﬆ': 'st'}


def is_bold(font):
    f = font_family(font)
    return f.startswith('cmbx') or 'bold' in f


def decode_chars(span, tables):
    fam = font_family(span['font'])
    tbl = tables.get(fam, {})
    out = []
    for ch in span['text']:
        c = ch
        if c in LIG:
            out.append(LIG[c]); continue
        code = ord(c)
        if code < len(tbl) and tbl[code] != '\uFFFD':
            out.append(tbl[code])
        else:
            out.append(c)
    return ''.join(out)


def page_lines(page, tables):
    d = page.get_text('dict')
    lines = []
    for b in d['blocks']:
        if b['type'] != 0:
            continue
        for ln in b['lines']:
            spans = []
            for s in ln['spans']:
                if not s['text']:
                    continue
                spans.append({
                    'text': decode_chars(s, tables),
                    'size': s['size'],
                    'y': s['origin'][1],
                    'x': s['bbox'][0],
                    'x1': s['bbox'][2],
                    'font': s['font'],
                    'bold': is_bold(s['font']),
                })
            if spans:
                spans.sort(key=lambda t: t['x'])
                lines.append({'y': min(s['y'] for s in spans), 'spans': spans,
                              'bbox': ln['bbox']})
    lines.sort(key=lambda l: (round(l['y'], 1), l['bbox'][0]))
    return lines


def render_line(line):
    spans = line['spans']
    # dominant size by char count
    from collections import Counter
    cnt = Counter()
    for s in spans:
        cnt[round(s['size'], 1)] += len(s['text'])
    base_size = max(cnt.items(), key=lambda kv: (kv[1], kv[0]))[0]
    base_y = None
    for s in spans:
        if abs(s['size'] - base_size) < 0.6:
            base_y = s['y'] if base_y is None else min(base_y, s['y'])
    if base_y is None:
        base_y = spans[0]['y']
    out = []
    mode = None
    buf = []

    def flush():
        nonlocal mode, buf
        if mode and buf:
            out.append(mode + '\u2063' + ''.join(buf) + '\u2063')
        elif buf:
            out.append(''.join(buf))
        mode, buf = None, []

    for s in spans:
        script = s['size'] < base_size * 0.9
        kind = None
        if script:
            dy = s['y'] - base_y
            if dy < -1.2:
                kind = '^'
            elif dy > 1.2:
                kind = '_'
        if kind is None:
            flush()
            out.append(s['text'])
        else:
            if kind != mode:
                flush()
                mode = kind
            buf.append(s['text'])
    flush()
    return ''.join(out).replace('\u2063', '{', 1) if '\u2063' in ''.join(out) else ''.join(out)


def render_line2(line):
    """cleaner brace insertion"""
    spans = line['spans']
    from collections import Counter
    cnt = Counter()
    for s in spans:
        cnt[round(s['size'], 1)] += len(s['text'])
    base_size = max(cnt.items(), key=lambda kv: (kv[1], kv[0]))[0]
    base_y = min((s['y'] for s in spans if abs(s['size'] - base_size) < 0.6), default=spans[0]['y'])
    out = []
    cur = None
    buf = []
    for s in spans:
        kind = None
        if s['size'] < base_size * 0.9:
            dy = s['y'] - base_y
            if dy < -1.2:
                kind = '^'
            elif dy > 1.2:
                kind = '_'
        if kind is None:
            if cur is not None:
                out.append(cur + '{' + ''.join(buf) + '}')
                cur, buf = None, []
            out.append(s['text'])
        else:
            if cur != kind:
                if cur is not None:
                    out.append(cur + '{' + ''.join(buf) + '}')
                cur, buf = kind, []
            buf.append(s['text'])
    if cur is not None:
        out.append(cur + '{' + ''.join(buf) + '}')
    return ''.join(out)


def main():
    doc = pymupdf.open(PDF)
    tables, missing = build_tables(doc)
    os.makedirs(os.path.join(WORK, 'en'), exist_ok=True)
    os.makedirs(os.path.join(WORK, 'pages'), exist_ok=True)
    print('missing glyph names:', json.dumps(missing, ensure_ascii=False)[:2000])
    for i in range(doc.page_count):
        pno = i + 1
        page = doc[i]
        lines = page_lines(page, tables)
        txt = []
        for ln in lines:
            y0 = ln['bbox'][1]
            content = render_line2(ln).strip()
            if not content:
                continue
            if y0 < 110 and (HEADER_RE.match(content.strip()) or content.strip().isdigit()):
                continue
            if y0 > 745 and content.strip().isdigit():
                continue
            txt.append(content)
        with open(os.path.join(WORK, 'en', 'p%03d.txt' % pno), 'w', encoding='utf-8') as f:
            f.write('\n'.join(txt) + '\n')
        pix = page.get_pixmap(dpi=DPI)
        pix.save(os.path.join(WORK, 'pages', 'p%03d.png' % pno))
        if pno % 50 == 0:
            print('done', pno, flush=True)
    print('all done', doc.page_count)


if __name__ == '__main__':
    main()
