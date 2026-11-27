"""Deterministic glossary cleanup for the Whisper output of this talk.

Whisper (small.en) transcribes the mathematics phonetically: "brains" for "branes",
"homomorphic" for "holomorphic", "modular space" for "moduli space", "au pair" for
"oper".  This pass applies a hand-written, auditable glossary so the narration is
readable next to the slides.  The raw transcript is never modified.

usage: python clean_asr.py asr_p04.json asr_p04_clean.json
"""
import json, re, sys

RULES = [
    # people
    (r'\b(?:Edinkov|Edinger|Edinger|Edicard|Eddinger|Edinghoff|Eddinghoff|Edinghoff)\b', 'Etingof'),
    (r'\bEtinghof\b', 'Etingof'),
    (r'\b(?:Frankel|Frankl|Franklin|Frankel)\b', 'Frenkel'),
    (r'\b(?:Kajdan|Kajan|Karsten|Karshan|Kachen|cajun|Kadzjdan|Kasdan)\b', 'Kazhdan'),
    (r'\b(?:Iguayato|Gaiato|Guyato|Guayato|Gaiotto|Guyatto)\b', 'Gaiotto'),
    (r'\b(?:Gukav|Gucov|Gookov|Gukoff)\b', 'Gukov'),
    (r'\b(?:Kapostin|Kuposten|Copustin|Kaposteen|Kopustin)\b', 'Kapustin'),
    (r'\b(?:Bhelensen|Balinson|Valinson|Balenkson|Beilinson)\b', 'Beilinson'),
    (r'\b(?:Hitchen|Hitchens|Hichin|Hichen|Hitchin)\b', 'Hitchin'),
    (r'\b(?:Teschner|Teshner)\b', 'Teschner'),
    (r'\bDennis Gayskory\b', 'Dennis Gaitsgory'),
    (r'\bDennis Gidgoria\b', 'Dennis Gaitsgory'),
    (r'\bInstitute for Advanced Studies\b', 'Institute for Advanced Study'),
    # subjects / objects
    (r'\bgeometric (?:language|linelands|landlands|Landlands|London|landlands)\b', 'geometric Langlands'),
    (r'\bgeometric landlands\b', 'geometric Langlands'),
    (r'\b(?:A|B)-brains\b', lambda m: m.group(0).replace('brains', 'branes')),
    (r'\b(?:coisotropic|co-osotopic|co-acetropic|quasitropic|quatropic|quiescentropic|quisotropic|claustrophobic|coisotropic)\b', 'coisotropic'),
    (r'\bbrains\b', 'branes'),
    (r'\bbrain quantization\b', 'brane quantization'),
    (r'\bhomomorphic\b', 'holomorphic'),
    (r'\bhomomorphically\b', 'holomorphically'),
    (r'\banti-homomorphic\b', 'anti-holomorphic'),
    (r'\bmodular space\b', 'moduli space'),
    (r'\bmodular spaces\b', 'moduli spaces'),
    (r'\bhexagonal modulus space\b', 'Higgs bundle moduli space'),
    (r'\bHiggs-Bundell\b', 'Higgs bundle'),
    (r'\bHiggs-Wunzel\b', 'Higgs bundle'),
    (r'\bHiggs-Ponsil\b', 'Higgs bundle'),
    (r'\bHitchens vibration\b', 'Hitchin fibration'),
    (r'\bHitchens Hamiltonian(s?)\b', r'Hitchin Hamiltonian\1'),
    (r'\bHitchens\b', "Hitchin's"),
    (r'\bau pair\b', 'oper'),
    (r'\bau pairs\b', 'opers'),
    (r'\bAU pair\b', 'oper'),
    (r'\bO pair\b', 'oper'),
    (r'\bO pairs\b', 'opers'),
    (r'\bOperes\b', 'opers'),
    (r'\b(?:fakaya|F-chaya|Fukaya|fukaya)\b', 'Fukaya'),
    (r'\bBCCZ\b', 'Bcc'),
    (r'\bBCC1\b', 'Bcc_1'),
    (r'\bBCC2\b', 'Bcc_2'),
    (r'\bD modules\b', 'D-modules'),
    (r'\bD module\b', 'D-module'),
    (r'\bquattrople\b', 'quintuple'),
    (r'\bN equals four\b', 'N=4'),
    (r'\bsuper Yang-Mills\b', 'super Yang–Mills'),
    (r'\bEfK\b', 'EFK'),
    (r'\bEF and K\b', 'EFK'),
    (r'\bST2 to the algebra\b', 'su(2) algebra'),
    (r'\bG-vee\b', 'G-vee'),
    (r'\bgeometric linelands\b', 'geometric Langlands'),
    (r'\bgeometric Langland\b', 'geometric Langlands'),
]


def clean(text):
    for pat, rep in RULES:
        flags = re.IGNORECASE if not pat[0].isupper() else 0
        text = re.sub(pat, rep, text, flags=flags)
    return text


def main():
    src, dst = sys.argv[1], sys.argv[2]
    rows = json.load(open(src, encoding='utf-8'))
    n = 0
    for r in rows:
        t = clean(r['text'])
        if t != r['text']:
            n += 1
        r['text'] = t
    json.dump(rows, open(dst, 'w', encoding='utf-8'), ensure_ascii=False)
    print(f'{len(rows)} segments, {n} changed -> {dst}')


if __name__ == '__main__':
    main()
