# -*- coding: utf-8 -*-
"""Content-stream based extraction for BD Hitchin PDF (v2).

The embedded Type1 subsets were re-encoded by pdfTeX, so ordinary extractors
mis-decode symbols (\\sum -> "P").  We parse the content stream ourselves,
recover true character codes, map them through the ORIGINAL AMS fonts, and
rebuild spaces from advances while reconstructing ^/_ from size+baseline.
"""
import os, re, sys, json
from collections import Counter, defaultdict
import pymupdf
from fontTools.agl import toUnicode as agl

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = r"C:\Users\admin\Desktop\QuantizationHitchin(1).pdf"
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
WORK = os.path.join(ROOT, '工程文件', 'work')
FONTDIR = r"C:\Users\admin\AppData\Local\Programs\MiKTeX\fonts\type1\public\amsfonts"
DPI = 170

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
    'vextendsingle': '|', 'vextenddouble': '‖',
    'hatwide': '^', 'hatwider': '^', 'hatwidest': '^',
    'tildewide': '~', 'tildewider': '~', 'tildewidest': '~',
    'planckover2pi1': 'ℏ', 'multicloseleft': '≫',
    'braceex': '|', 'arrowvertex': '|', 'arrowvertexdbl': '‖',
    'dotlessi': 'ı', 'dotlessj': 'ȷ',
    'star': '⋆', 'sharp': '♯', 'triangleleft': '◁', 'triangleright': '▷',
    'vector': '⃗', 'tie': ' ', 'slurabove': '', 'slurbelow': '',
    'Gamma': 'Γ', 'Delta': 'Δ', 'Theta': 'Θ', 'Lambda': 'Λ', 'Xi': 'Ξ',
    'Pi': 'Π', 'Sigma': 'Σ', 'Upsilon': 'Υ', 'Phi': 'Φ', 'Psi': 'Ψ',
    'Omega': 'Ω',
}

BIGPREFIX = {
    'paren': '()', 'bracket': '[]', 'brace': '{}', 'angbracket': '⟨⟩',
    'floor': '⌊⌋', 'ceiling': '⌈⌉', 'slash': '/\\', 'backslash': '\\/',
}
BIGNAMES = {
    'summation': '∑', 'product': '∏', 'integral': '∫', 'union': '⋃',
    'intersection': '⋂', 'coproduct': '∐', 'coprod': '∐',
    'circleplus': '⊕', 'circlemultiply': '⊗', 'circledot': '⊙',
    'logicaland': '∧', 'logicalor': '∨', 'unionsq': '⊔', 'intersectionsq': '⊓',
    'contintegral': '∮', 'radical': '√',
}

PFB_CACHE = {}


def parse_pfb_encoding(path):
    txt = open(path, 'rb').read().decode('latin-1', 'replace')
    i = txt.find('/Encoding')
    if i < 0:
        return {}
    seg = txt[i:i + 16000]
    j = seg.find('readonly def')
    if j > 0:
        seg = seg[:j]
    return {int(a): b for a, b in re.findall(r'dup\s+(\d+)\s*/([^\s/]+)\s+put', seg)}


def font_family(basefont):
    return basefont.split('+')[-1].lower()


def pfb_path(family):
    for sub in ('cm', 'euler', 'symbols', 'cmextra'):
        p = os.path.join(FONTDIR, sub, family + '.pfb')
        if os.path.exists(p):
            return p
    return None


def big_glyph(name):
    for pre, br in BIGPREFIX.items():
        if name.startswith(pre):
            rest = name[len(pre):]
            if 'left' in rest or rest.endswith(('tp', 'bt', 'ex')):
                return br[0]
            if 'right' in rest:
                return br[1] if len(br) > 1 else br[0]
    for pre, ch in BIGNAMES.items():
        if name.startswith(pre):
            return ch
    return None


def glyph_to_unicode(name, family):
    if family.startswith('eufm'):
        if len(name) == 1 and name.isalpha():
            if name.islower():
                return chr(0x1D51E + ord(name) - ord('a'))
            return chr(0x1D504 + ord(name) - ord('A'))
    if family.startswith('msbm') and len(name) == 1 and name.isalpha():
        return chr(0x1D538 + ord(name) - ord('A')) if name.isupper() else chr(0x1D552 + ord(name) - ord('a'))
    if family.startswith('cmcsc') and len(name) == 1 and name.isalpha():
        return name.upper()
    if family.startswith('cmex'):
        b = big_glyph(name)
        if b:
            return b
    if name in MANUAL:
        return MANUAL[name]
    u = agl(name)
    if u:
        return u
    b = big_glyph(name)
    if b:
        return b
    return None


def font_table(family):
    if family in PFB_CACHE:
        return PFB_CACHE[family]
    p = pfb_path(family)
    tbl = {}
    if p:
        for code, name in parse_pfb_encoding(p).items():
            u = glyph_to_unicode(name, family)
            if u is None:
                u = ''
            tbl[code] = u
    PFB_CACHE[family] = tbl
    return tbl


WS = b' \t\r\n\x00\x0c'
DELIM = b'()<>[]{}/%'


def read_literal(data, i):
    """data[i] == '(' ; return (bytes, next_index)"""
    depth = 1
    i += 1
    n = len(data)
    buf = bytearray()
    while i < n and depth:
        ch = data[i:i + 1]
        if ch == b'\\':
            nx = data[i + 1:i + 2]
            esc = {b'n': b'\n', b'r': b'\r', b't': b'\t', b'b': b'\b',
                   b'f': b'\f', b'(': b'(', b')': b')', b'\\': b'\\'}.get(nx)
            if esc is not None:
                buf += esc
                i += 2
            elif nx.isdigit():
                m = re.match(rb'[0-7]{1,3}', data[i + 1:i + 4])
                buf.append(int(m.group(0), 8) & 0xFF)
                i += 1 + len(m.group(0))
            elif nx in (b'\n', b'\r'):
                i += 2
            else:
                buf += nx
                i += 2
        elif ch == b'(':
            depth += 1
            buf += ch
            i += 1
        elif ch == b')':
            depth -= 1
            if depth:
                buf += ch
            i += 1
        else:
            buf += ch
            i += 1
    return bytes(buf), i


def read_hex(data, i):
    j = data.find(b'>', i)
    hx = re.sub(rb'\s', b'', data[i + 1:j])
    if len(hx) % 2:
        hx += b'0'
    return bytes.fromhex(hx.decode('ascii')), j + 1


def tokenize(data):
    i, n = 0, len(data)
    out = []
    while i < n:
        c = data[i:i + 1]
        if c in WS:
            i += 1
            continue
        if c == b'%':
            j = data.find(b'\n', i)
            i = n if j < 0 else j + 1
            continue
        if c == b'(':
            s, i = read_literal(data, i)
            out.append(('str', s))
            continue
        if c == b'<':
            if data[i + 1:i + 2] == b'<':
                i += 2
                depth = 1
                while i < n and depth:
                    if data[i:i + 2] == b'<<':
                        depth += 1
                        i += 2
                    elif data[i:i + 2] == b'>>':
                        depth -= 1
                        i += 2
                    else:
                        i += 1
                continue
            s, i = read_hex(data, i)
            out.append(('str', s))
            continue
        if c == b'[':
            arr, i = parse_array(data, i + 1)
            out.append(('arr', arr))
            continue
        if c in b']>':
            i += 1
            continue
        if c == b'/':
            j = i + 1
            while j < n and data[j:j + 1] not in WS and data[j:j + 1] not in DELIM:
                j += 1
            out.append(('name', data[i + 1:j].decode('latin-1')))
            i = j
            continue
        j = i
        while j < n and data[j:j + 1] not in WS and data[j:j + 1] not in DELIM:
            j += 1
        word = data[i:j].decode('latin-1')
        if not word:
            i += 1
            continue
        try:
            out.append(('num', float(word)))
        except ValueError:
            out.append(('op', word))
        i = j
    return out


def parse_array(data, i):
    arr = []
    n = len(data)
    while i < n:
        c = data[i:i + 1]
        if c in WS:
            i += 1
            continue
        if c == b']':
            return arr, i + 1
        if c == b'(':
            s, i = read_literal(data, i)
            arr.append(('str', s))
            continue
        if c == b'<':
            s, i = read_hex(data, i)
            arr.append(('str', s))
            continue
        j = i
        while j < n and data[j:j + 1] not in WS and data[j:j + 1] not in DELIM:
            j += 1
        word = data[i:j].decode('latin-1')
        if not word:
            i += 1
            continue
        try:
            arr.append(('num', float(word)))
        except ValueError:
            arr.append(('op', word))
        i = j
    return arr, i


def num_list(raw):
    return [float(x) for x in re.findall(r'-?\d+(?:\.\d+)?', raw)]


def font_info(doc, page):
    info = {}
    for f in page.get_fonts(full=False):
        xref, ext, typ, basefont, resname, enc = f
        fam = font_family(basefont)
        widths, first = {}, 0
        k = doc.xref_get_key(xref, 'FirstChar')
        if k[0] == 'int':
            first = int(k[1])
        k = doc.xref_get_key(xref, 'Widths')
        raw = None
        if k[0] == 'xref':
            raw = doc.xref_object(int(k[1].split()[0]))
        elif k[0] == 'array':
            raw = k[1]
        if raw:
            for idx, w in enumerate(num_list(raw)):
                widths[first + idx] = w
        info[resname] = {'family': fam, 'basefont': basefont,
                         'widths': widths, 'tbl': font_table(fam)}
    return info


def page_glyphs(doc, page):
    data = page.read_contents()
    toks = tokenize(data)
    finfo = font_info(doc, page)
    glyphs = []
    st = {'font': None, 'size': 10.9, 'x': 0.0, 'y': 0.0, 'lead': 0.0}
    tm = [1, 0, 0, 1, 0.0, 0.0]
    stack = []
    pend = []
    for kind, val in toks:
        if kind == 'op':
            op = val
            args = pend
            pend = []
            if op == 'q':
                st = dict(st)
                stack.append((id(st), st['font'], st['size'], st['x'], st['y'], st['lead'], list(tm)))
            elif op == 'Q':
                if stack:
                    _, fn, sz, x, y, ld, t = stack.pop()
                    st.update(font=fn, size=sz, x=x, y=y, lead=ld)
                    tm = t
            elif op == 'BT':
                tm = [1, 0, 0, 1, 0.0, 0.0]
                st['x'], st['y'] = 0.0, 0.0
            elif op == 'Tf' and len(args) >= 2:
                st['font'] = args[-2][1]
                st['size'] = args[-1][1]
            elif op == 'Td' and len(args) >= 2:
                st['x'] += args[-2][1] * tm[0]
                st['y'] += args[-1][1] * tm[3]
            elif op == 'TD' and len(args) >= 2:
                st['lead'] = -args[-1][1]
                st['x'] += args[-2][1] * tm[0]
                st['y'] += args[-1][1] * tm[3]
            elif op == 'Tm' and len(args) >= 6:
                tm = [a[1] for a in args[-6:]]
                st['x'], st['y'] = tm[4], tm[5]
            elif op == 'TL' and args:
                st['lead'] = args[-1][1]
            elif op == 'T*':
                st['y'] -= st['lead']
            elif op in ('Tj', 'TJ', "'", '"'):
                if op in ("'", '"'):
                    st['y'] -= st['lead']
                fi = finfo.get(st['font'])

                def emit(s):
                    for code in s:
                        u = ''
                        w = 500.0
                        if fi:
                            u = fi['tbl'].get(code, '')
                            w = fi['widths'].get(code, 500.0)
                        if code == 32 and u in ('', '\ufffd'):
                            u = ' '
                        if not u:
                            continue
                        adv = w / 1000.0 * st['size'] * tm[0]
                        glyphs.append({'c': u, 'code': code, 'x': st['x'], 'y': st['y'],
                                       'size': st['size'],
                                       'font': fi['basefont'] if fi else '?',
                                       'w': adv})
                        st['x'] += adv

                if op == 'TJ':
                    for k2, v2 in args[-1][1]:
                        if k2 == 'str':
                            emit(v2)
                        elif k2 == 'num':
                            st['x'] -= v2 / 1000.0 * st['size'] * tm[0]
                else:
                    emit(args[-1][1])
        else:
            pend.append((kind, val))
            if len(pend) > 12:
                pend = pend[-12:]
    return glyphs


LIG = {'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬀ': 'ff', 'ﬃ': 'ffi', 'ﬄ': 'ffl',
       'ﬅ': 'ft', 'ﬆ': 'st', '\u00a0': ' '}


def normalize(s):
    for k, v in LIG.items():
        s = s.replace(k, v)
    return s


def row_text(row, base):
    glyphs = sorted(row, key=lambda g: g['x'])
    if not glyphs:
        return ''
    cnt = Counter(round(g['size'], 1) for g in glyphs)
    base_size = max(cnt.items(), key=lambda kv: (kv[1], kv[0]))[0]
    base_y = None
    for g in glyphs:
        if abs(g['size'] - base_size) < 0.5:
            base_y = g['y'] if base_y is None else min(base_y, g['y'])
    if base_y is None:
        base_y = glyphs[0]['y']
    out, cur, buf = [], None, []
    prev_end = None
    for g in glyphs:
        if prev_end is not None:
            gap = g['x'] - prev_end
            if gap > 0.15 * base_size and (not out or not out[-1].endswith(' ')):
                if cur:
                    out.append(cur + '{' + ''.join(buf) + '}')
                    cur, buf = None, []
                out.append(' ')
        kind = ''
        if g['size'] < base_size * 0.92:
            dy = g['y'] - base_y
            if dy > 1.0:
                kind = '^'
            elif dy < -1.0:
                kind = '_'
        if kind:
            if cur != kind:
                if cur:
                    out.append(cur + '{' + ''.join(buf) + '}')
                cur, buf = kind, []
            buf.append(g['c'])
        else:
            if cur:
                out.append(cur + '{' + ''.join(buf) + '}')
                cur, buf = None, []
            out.append(g['c'])
        prev_end = g['x'] + g['w']
    if cur:
        out.append(cur + '{' + ''.join(buf) + '}')
    s = ''.join(out)
    s = re.sub(r'[ \t]+', ' ', s).strip()
    return normalize(s)


def page_rows(doc, page):
    glyphs = page_glyphs(doc, page)
    glyphs = [g for g in glyphs if g['y'] < 680]      # drop running head
    if not glyphs:
        return []
    rows = []
    for g in sorted(glyphs, key=lambda g: (-g['y'], g['x'])):
        for r in rows:
            if abs(r['y'] - g['y']) < 3.2:
                r['glyphs'].append(g)
                break
        else:
            rows.append({'y': g['y'], 'glyphs': [g]})
    big = Counter(round(g['size'], 1) for g in glyphs)
    body_size = max(big.items(), key=lambda kv: kv[1])[0]
    # merge script-only rows into nearest body row
    body = [r for r in rows if max(g['size'] for g in r['glyphs']) >= body_size * 0.92]
    small = [r for r in rows if r not in body]
    for r in small:
        best, bd = None, 9.0
        tall = all(('CMEX' in g['font'].upper()) for g in r['glyphs'])
        if tall:
            bd = 14.0
        for b in body:
            d = abs(b['y'] - r['y'])
            if d < bd:
                best, bd = b, d
        if best is not None:
            best['glyphs'].extend(r['glyphs'])
        else:
            body.append(r)
    for r in body:
        r['glyphs'].sort(key=lambda g: g['x'])
    body.sort(key=lambda r: -r['y'])
    return body


def page_to_text(doc, page):
    rows = page_rows(doc, page)
    out = []
    for r in rows:
        t = row_text(r['glyphs'], None)
        if not t:
            continue
        gl = r['glyphs']
        bold = sum(1 for g in gl if 'CMBX' in g['font'].upper())
        ratio = bold / max(1, len(gl))
        if ratio > 0.6 and len(gl) > 1 and (re.match(r'^\d+(\.\d+)*\.? ', t) or re.match(r'^(Chapter|CHAPTER)\b', t)):
            mx = max(g['size'] for g in gl)
            mark = '## ' if mx > 12 else '# '
            out.append(mark + t)
        elif ratio > 0.9 and len(gl) > 1 and max(g['size'] for g in gl) > 12:
            out.append('## ' + t)
        else:
            out.append(t)
    return '\n'.join(out)


def main():
    doc = pymupdf.open(PDF)
    os.makedirs(os.path.join(WORK, 'en'), exist_ok=True)
    render = (len(sys.argv) > 1 and sys.argv[1] == 'render')
    pages = [int(x) for x in sys.argv[2:]] if len(sys.argv) > 2 else list(range(1, doc.page_count + 1))
    if render:
        os.makedirs(os.path.join(WORK, 'pages'), exist_ok=True)
    for pno in pages:
        page = doc[pno - 1]
        txt = page_to_text(doc, page)
        with open(os.path.join(WORK, 'en', 'p%03d.txt' % pno), 'w', encoding='utf-8') as f:
            f.write(txt + '\n')
        if render:
            page.get_pixmap(dpi=DPI).save(os.path.join(WORK, 'pages', 'p%03d.png' % pno))
        if pno % 25 == 0:
            print('done', pno, flush=True)
    print('ok', len(pages))


if __name__ == '__main__':
    main()
