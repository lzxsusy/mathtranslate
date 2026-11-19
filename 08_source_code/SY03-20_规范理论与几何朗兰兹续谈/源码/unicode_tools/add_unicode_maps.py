"""Embed missing PDF text mappings without changing page content or font programs.

The output retains the entire original PDF as an unchanged byte prefix and adds
only an incremental revision containing ToUnicode streams and updated font
dictionaries. No visible text, glyph outline, geometry, link, bookmark, metadata,
or original embedded object stream is intentionally changed.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import shutil
import unicodedata

import fitz
from fontTools import agl
from fontTools.cffLib import CFFFontSet
from fontTools.encodings.StandardEncoding import StandardEncoding
from fontTools.encodings.MacRoman import MacRoman
from fontTools.ttLib import TTFont
from pypdf import PdfReader


RESOURCE_ROOT = Path(__file__).resolve().parent
ADOBE_GB1 = RESOURCE_ROOT / 'resources/cmaps/Adobe-GB1-UCS2'
GLYPHLIST_ROOT = RESOURCE_ROOT / 'resources/glyphlist'


def obj(value):
    return value.get_object() if hasattr(value, 'get_object') else value


def unicode_from_hex(value):
    data = bytes.fromhex(value)
    if len(data) % 2:
        data = b'\x00' + data
    return data.decode('utf-16-be')


def parse_cmap(data):
    text = re.sub(r'%[^\n]*', '', data.decode('ascii', errors='ignore'))
    result = {}
    for block in re.findall(r'\bbeginbfchar\b(.*?)\bendbfchar\b', text, re.S):
        for source, dest in re.findall(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]*)>', block):
            result[int(source, 16)] = unicode_from_hex(dest)
    for block in re.findall(r'\bbeginbfrange\b(.*?)\bendbfrange\b', text, re.S):
        tokens = re.findall(r'<[0-9A-Fa-f]+>|\[|\]', block)
        index = 0
        while index < len(tokens):
            start = int(tokens[index][1:-1], 16)
            end = int(tokens[index + 1][1:-1], 16)
            destination = tokens[index + 2]
            index += 3
            if destination == '[':
                for code in range(start, end + 1):
                    result[code] = unicode_from_hex(tokens[index][1:-1])
                    index += 1
                if tokens[index] != ']':
                    raise ValueError('Invalid bfrange array')
                index += 1
            else:
                hex_value = destination[1:-1]
                base = int(hex_value, 16)
                width = len(hex_value)
                for code in range(start, end + 1):
                    result[code] = unicode_from_hex(f'{base + code - start:0{width}X}')
    return result


def load_glyph_map():
    mapping = dict(agl.AGL2UV)
    mapping = {name: chr(value) for name, value in mapping.items()}
    for name in ['glyphlist.txt', 'pdfglyphlist.txt', 'texglyphlist.txt']:
        for line in (GLYPHLIST_ROOT / name).read_text().splitlines():
            if not line or line.startswith('#') or ';' not in line:
                continue
            glyph, values = line.split(';', 1)
            # A comma separates alternatives; spaces join Unicode sequences.
            values = values.split(',')[0]
            try:
                value = ''.join(chr(int(v, 16)) for v in values.split())
            except ValueError:
                continue
            if not invalid_unicode(value):
                mapping[glyph] = value
    # Standard Unicode representations for components of extensible delimiters.
    names = {
        'parenlefttp': 'LEFT PARENTHESIS UPPER HOOK',
        'parenleftex': 'LEFT PARENTHESIS EXTENSION',
        'parenleftbt': 'LEFT PARENTHESIS LOWER HOOK',
        'parenrighttp': 'RIGHT PARENTHESIS UPPER HOOK',
        'parenrightex': 'RIGHT PARENTHESIS EXTENSION',
        'parenrightbt': 'RIGHT PARENTHESIS LOWER HOOK',
        'bracketlefttp': 'LEFT SQUARE BRACKET UPPER CORNER',
        'bracketleftex': 'LEFT SQUARE BRACKET EXTENSION',
        'bracketleftbt': 'LEFT SQUARE BRACKET LOWER CORNER',
        'bracketrighttp': 'RIGHT SQUARE BRACKET UPPER CORNER',
        'bracketrightex': 'RIGHT SQUARE BRACKET EXTENSION',
        'bracketrightbt': 'RIGHT SQUARE BRACKET LOWER CORNER',
        'bracelefttp': 'LEFT CURLY BRACKET UPPER HOOK',
        'braceleftmid': 'LEFT CURLY BRACKET MIDDLE PIECE',
        'braceleftbt': 'LEFT CURLY BRACKET LOWER HOOK',
        'braceex': 'CURLY BRACKET EXTENSION',
        'bracerighttp': 'RIGHT CURLY BRACKET UPPER HOOK',
        'bracerightmid': 'RIGHT CURLY BRACKET MIDDLE PIECE',
        'bracerightbt': 'RIGHT CURLY BRACKET LOWER HOOK',
        'radicalbt': 'RADICAL SYMBOL BOTTOM',
        'radicalvertex': 'VERTICAL LINE EXTENSION',
        'radicalex': 'HORIZONTAL LINE EXTENSION',
        'arrowvertex': 'VERTICAL LINE EXTENSION',
        'vextendsingle': 'DIVIDES',
        'vextenddouble': 'PARALLEL TO',
        'arrowvertexdbl': 'DOUBLE VERTICAL LINE',
        'hatwide': 'COMBINING CIRCUMFLEX ACCENT',
        'hatwider': 'COMBINING CIRCUMFLEX ACCENT',
        'hatwidest': 'COMBINING CIRCUMFLEX ACCENT',
        'tildewide': 'COMBINING TILDE',
        'tildewider': 'COMBINING TILDE',
        'tildewidest': 'COMBINING TILDE',
        'contintegral': 'CONTOUR INTEGRAL',
    }
    mapping.update({glyph: unicodedata.lookup(name) for glyph, name in names.items()})
    return mapping


def invalid_unicode(value):
    return not value or any(
        ord(char) < 0x20 or 0x7F <= ord(char) <= 0x9F
        or 0xD800 <= ord(char) <= 0xDFFF or char == '\uFFFD'
        for char in value
    )


def glyph_unicode(name, mapping):
    if name in mapping:
        return mapping[name]
    plain = name.split('.')[0]
    if plain in mapping:
        return mapping[plain]
    # These suffixes indicate the optical size of the same mathematical sign.
    plain = re.sub(r'(?:display|text|Bigg|bigg|Big|big)$', '', plain)
    if plain in mapping:
        return mapping[plain]
    value = agl.toUnicode(plain)
    return value if value and not invalid_unicode(value) else None


def collect_fonts(reader):
    found = {}
    visited = set()

    def resources(value):
        if value is None:
            return
        reference = getattr(value, 'idnum', None)
        if reference is not None:
            if reference in visited:
                return
            visited.add(reference)
        resource = obj(value)
        for ref in obj(resource.get('/Font', {})).values():
            font = obj(ref)
            xref = getattr(ref, 'idnum', None)
            if xref is None:
                xref = getattr(getattr(font, 'indirect_reference', None), 'idnum', None)
            if xref is None:
                raise ValueError('Direct font dictionary cannot be updated safely')
            found[xref] = font
        for ref in obj(resource.get('/XObject', {})).values():
            form = obj(ref)
            if form.get('/Subtype') == '/Form':
                resources(form.get('/Resources'))

    for page in reader.pages:
        resources(page.get('/Resources'))
    return found


def cff_encoding(font):
    descriptor = obj(font.get('/FontDescriptor', {}))
    stream = descriptor.get('/FontFile3')
    if stream is None:
        raise ValueError(f'Expected embedded CFF program for {font.get("/BaseFont")}')
    data = obj(stream).get_data()
    cff = CFFFontSet()
    cff.decompile(io.BytesIO(data), TTFont())
    top = cff[cff.fontNames[0]]
    embedded = top.Encoding
    if embedded == 'StandardEncoding':
        names = list(StandardEncoding)
    elif isinstance(embedded, list):
        names = list(embedded)
    else:
        raise ValueError(f'Unknown embedded encoding: {embedded}')
    specified = obj(font.get('/Encoding'))
    differences = []
    if isinstance(specified, dict):
        differences = specified.get('/Differences', [])
        specified = specified.get('/BaseEncoding')
    if specified == '/StandardEncoding':
        names = list(StandardEncoding)
    elif specified == '/MacRomanEncoding':
        names = list(MacRoman)
    elif specified == '/WinAnsiEncoding':
        names = []
        for code in range(256):
            try:
                character = bytes([code]).decode('cp1252')
            except UnicodeDecodeError:
                names.append('.notdef')
                continue
            names.append(agl.UV2AGL.get(ord(character), f'uni{ord(character):04X}'))
    elif specified is not None and specified != '/Identity-H':
        raise ValueError(f'Unknown explicit encoding: {specified}')
    code = 0
    for value in differences:
        if isinstance(value, int):
            code = value
        else:
            names[code] = str(value).lstrip('/')
            code += 1
    # A PDF subset may declare a broader range; only embedded glyphs are real.
    charset = set(top.charset)
    return {i: glyph for i, glyph in enumerate(names)
            if glyph != '.notdef' and glyph in charset}


def make_cmap(mapping, name, code_bytes=1):
    header = f'''/CIDInit /ProcSet findresource begin
12 dict begin
begincmap
/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def
/CMapName /{name} def
/CMapType 2 def
1 begincodespacerange
<{'00' * code_bytes}> <{'FF' * code_bytes}>
endcodespacerange
'''
    rows = [(code, value) for code, value in sorted(mapping.items()) if value]
    chunks = [header]
    for offset in range(0, len(rows), 100):
        block = rows[offset:offset + 100]
        chunks.append(f'{len(block)} beginbfchar\n')
        for code, value in block:
            chunks.append(f'<{code:0{code_bytes * 2}X}> <{value.encode("utf-16-be").hex().upper()}>\n')
        chunks.append('endbfchar\n')
    chunks.append('endcmap\nCMapName currentdict /CMap defineresource pop\nend\nend\n')
    return ''.join(chunks).encode('ascii')


def embedded_programs(reader):
    result = {}
    for xref, font in collect_fonts(reader).items():
        descendants = font.get('/DescendantFonts')
        subfonts = [obj(v) for v in descendants] if descendants else [font]
        for subfont in subfonts:
            desc = obj(subfont.get('/FontDescriptor', {}))
            streams = [key for key in ['/FontFile', '/FontFile2', '/FontFile3'] if key in desc]
            if not streams:
                raise ValueError(f'Unembedded font {subfont.get("/BaseFont")}')
            for key in streams:
                stream = obj(desc[key])
                result[(xref, key)] = hashlib.sha256(stream.get_data()).hexdigest()
    return result


def structural_snapshot(path, render):
    document = fitz.open(path)
    result = {
        'pages': len(document),
        'metadata': document.metadata,
        'xml': document.get_xml_metadata(),
        'toc': repr(document.get_toc(simple=False)),
        'page_boxes': [tuple(page.rect) for page in document],
        'links': [repr(page.get_links()) for page in document],
        'content': [[hashlib.sha256(document.xref_stream(xref)).hexdigest()
                     for xref in page.get_contents()] for page in document],
        'attachments': document.embfile_names(),
    }
    if render:
        result['pixels_72dpi'] = [hashlib.sha256(page.get_pixmap(alpha=False).samples).hexdigest()
                                  for page in document]
    document.close()
    return result


def add_maps(source, output, verify_render=False):
    source = source.resolve()
    output = output.resolve()
    if source == output:
        raise ValueError('Use a separate output file to retain the original compilation')
    original = source.read_bytes()
    reader = PdfReader(io.BytesIO(original))
    fonts = collect_fonts(reader)
    glyph_map = load_glyph_map()
    plans = []
    unresolved = []
    for xref, font in sorted(fonts.items()):
        name = str(font.get('/BaseFont'))
        current = obj(font.get('/ToUnicode'))
        if font.get('/Subtype') == '/Type0':
            if current is not None:
                continue
            child = obj(font['/DescendantFonts'][0])
            info = obj(child.get('/CIDSystemInfo', {}))
            if info.get('/Registry') == 'Adobe' and info.get('/Ordering') == 'GB1' and font.get('/Encoding') == '/Identity-H':
                plans.append((xref, ADOBE_GB1.read_bytes(), name, 'embedded Adobe-GB1 UCS2 map'))
            else:
                unresolved.append({'font': name, 'reason': f'Unsupported CID collection {info}'})
            continue
        try:
            encoding = cff_encoding(font)
        except ValueError as error:
            if current is None:
                unresolved.append({'font': name, 'reason': str(error)})
            continue
        current_map = parse_cmap(current.get_data()) if current is not None else {}
        revised = dict(current_map)
        changed = current is None
        for code, glyph in encoding.items():
            existing = current_map.get(code)
            if existing is not None and not invalid_unicode(existing):
                continue
            replacement = glyph_unicode(glyph, glyph_map)
            if replacement is None:
                unresolved.append({'font': name, 'code': code, 'glyph': glyph})
            else:
                revised[code] = replacement
                changed = True
        if changed:
            cmap_name = re.sub('[^A-Za-z0-9]', '', name) + 'EmbeddedUnicode'
            plans.append((xref, make_cmap(revised, cmap_name), name,
                          'embedded or completed simple-font mapping'))
    if unresolved:
        raise ValueError('Unresolved mappings: ' + json.dumps(unresolved, ensure_ascii=False))

    before = structural_snapshot(source, verify_render)
    programs_before = embedded_programs(reader)
    shutil.copyfile(source, output)
    if plans:
        document = fitz.open(output)
        stream_ids = {}
        for xref, data, name, reason in plans:
            digest = hashlib.sha256(data).hexdigest()
            if digest not in stream_ids:
                stream_xref = document.get_new_xref()
                document.update_object(stream_xref, '<<>>')
                document.update_stream(stream_xref, data)
                stream_ids[digest] = stream_xref
            document.xref_set_key(xref, 'ToUnicode', f'{stream_ids[digest]} 0 R')
        document.save(output, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP,
                      no_new_id=True, preserve_metadata=True)
        document.close()

    if output.read_bytes()[:len(original)] != original:
        raise RuntimeError('Original PDF byte prefix was changed')
    after = structural_snapshot(output, verify_render)
    if before != after:
        raise RuntimeError('Unexpected structural or visual change: ' +
                           ', '.join(key for key in before if before[key] != after[key]))
    output_reader = PdfReader(output)
    if programs_before != embedded_programs(output_reader):
        raise RuntimeError('An embedded font program changed')
    remaining = [str(font.get('/BaseFont')) for font in collect_fonts(output_reader).values()
                 if '/ToUnicode' not in font]
    if remaining:
        raise RuntimeError('Fonts remain without explicit Unicode maps: ' + repr(remaining))
    report = {
        'source': str(source), 'output': str(output), 'font_count': len(fonts),
        'mapped_fonts': [{'xref': xref, 'font': name, 'operation': reason}
                         for xref, _, name, reason in plans],
        'original_pdf_prefix_preserved': True,
        'page_content_streams_unchanged': True,
        'font_programs_unchanged': True,
        'links_bookmarks_metadata_unchanged': True,
        'pixel_comparison_72dpi': 'identical' if verify_render else 'not requested',
        'missing_tounicode': remaining,
    }
    report_path = output.with_suffix('.unicode-audit.json')
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--verify-render', action='store_true')
    arguments = parser.parse_args()
    add_maps(arguments.source, arguments.output, arguments.verify_render)
