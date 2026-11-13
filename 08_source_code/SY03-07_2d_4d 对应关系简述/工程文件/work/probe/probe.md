```
=== METADATA ===
format: 'PDF 1.5'
title: ''
author: ''
subject: ''
keywords: ''
creator: 'LaTeX with hyperref package'
producer: 'pdfTeX-1.40.12'
creationDate: 'D:20161018003045Z'
modDate: 'D:20161018003045Z'
trapped: ''
encryption: None
pages: 46
page size: Rect(0.0, 0.0, 612.0, 792.0)
printed page numbers on page 1..3: see per-page section
toc entries: 37
  TOC L1 p2: 1 Introduction
  TOC L1 p4: 2 Two two-dimensional theories
  TOC L2 p4: 2.1 Two-dimensional Yang-Mills theories
  TOC L3 p4: 2.1.1 Action
  TOC L3 p4: 2.1.2 On the cylinder
  TOC L3 p5: 2.1.3 On a general surface
  TOC L3 p8: 2.1.4 q-deformation
  TOC L2 p10: 2.2 The Liouville theory
  TOC L3 p10: 2.2.1 Free boson theory
  TOC L3 p11: 2.2.2 Interacting theory
  TOC L3 p13: 2.2.3 Four-point function: general structure
  TOC L3 p15: 2.2.4 Four-point function: explicit expressions
  TOC L1 p16: 3 A class of four-dimensional theories
  TOC L2 p16: 3.1 N=2 supersymmetric gauge theories
  TOC L2 p17: 3.2 Class S theories of type SU(2)
  TOC L3 p17: 3.2.1 Construction from three-punctured spheres and cylinders
  TOC L3 p18: 3.2.2 One-punctured torus
  TOC L3 p19: 3.2.3 Four-punctured sphere
  TOC L3 p20: 3.2.4 General consideration
  TOC L1 p21: 4 Two supersymmetric backgrounds
  TOC L2 p21: 4.1 General yoga of supersymmetric localization
  TOC L2 p23: 4.2 S1S3
  TOC L2 p24: 4.3 S4
  TOC L3 p25: 4.3.1 General structure
  TOC L3 p25: 4.3.2 Classical and one-loop factors
  TOC L3 p26: 4.3.3 Instanton contributions
  TOC L1 p28: 5 Two correspondences and an interpretation
  TOC L2 p28: 5.1 S1S3 and the two-dimensional Yang-Mills
  TOC L2 p31: 5.2 S4 and the Liouville theory
  TOC L2 p33: 5.3 Six-dimensional interpretation
  TOC L3 p33: 5.3.1 6d N=(2,0) theory and 4d class S theories
  TOC L3 p35: 5.3.2 Alternative derivations of the correspondences
  TOC L1 p36: 6 Future directions
  TOC L2 p36: 6.1 Two unsolved problems in the SU(2) case
  TOC L2 p37: 6.2 More objects in the SU(2) case
  TOC L2 p38: 6.3 Using 6d N=(2,0) theories of other types
  TOC L2 p39: 6.4 Other spacetimes, other theories

=== PAGE 1 TEXT ===
IPMU-16-0048
A brief review of the 2d/4d correspondences
Yuji Tachikawa
Kavli Institute for the Physics and Mathematics of the Universe,
University of Tokyo, Kashiwa, Chiba 277-8583, Japan
[邮箱隐去]
Abstract
An elementary introduction to the 2d/4d correspondences is given. After quickly reviewing
the 2d q-deformed Yang-Mills theory and the Liouville theory, we will introduce 4d theories
obtained by coupling trifundamentals to SU(2) gauge ﬁelds. We will then see concretely
that the supersymmetric partition function of these theories on S3 × S1 and on S4 is given
respectively by the q-deformed Yang-Mills theory and the Liouville theory. After giving a
short discussion on how this correspondence may be understood from the viewpoint of the
6d N = (2, 0) theory, we conclude the review by enumerating future directions. Most of the
technical points will be referred to more detailed review articles.
This is a contribution to the review volume “Localization techniques in quantum ﬁeld
theories” (eds. V. Pestun and M. Zabzine) which contains 17 Chapters available at [1]
Contents
1
Introduction
2
2
Two two-dimensional theories
4
2.1
Two-dimensional Yang-Mills theories . . . . . . . . . . . . . . . . . . . . . .
4
2.1.1
Action . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2.1.2
On the cylinder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2.1.3
On a general surface
. . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2.1.4
q-deformation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2
The Liouville theory
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
2.2.1
Free boson theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
2.2.2
Interacting theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
2.2.3
Four-point function: general structure
. . . . . . . . . . . . . . . . .
13
2.2.4
Four-point function: explicit expressions . . . . . . . . . . . . . . . .
15
arXiv:1608.02964v5  [hep-th]  15 Oct 2016


=== PAGE 2 TEXT (head) ===
3
A class of four-dimensional theories
16
3.1
N=2 supersymmetric gauge theories
. . . . . . . . . . . . . . . . . . . . . .
16
3.2
Class S theories of type SU(2) . . . . . . . . . . . . . . . . . . . . . . . . . .
17
3.2.1
Construction from three-punctured spheres and cylinders . . . . . . .
17
3.2.2
One-punctured torus . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
3.2.3
Four-punctured sphere . . . . . . . . . . . . . . . . . . . . . . . . . .
19
3.2.4
General consideration . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
4
Two supersymmetric backgrounds
21
4.1
General yoga of supersymmetric localization . . . . . . . . . . . . . . . . . .
21
4.2
S1 × S3
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
4.3
S4
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
4.3.1
General structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
4.3.2
Classical and one-loop factors . . . . . . . . . . . . . . . . . . . . . .
25
4.3.3
Instanton contributions . . . . . . . . . . . . . . . . . . . . . . . . . .
26
5
Two correspondences and an interpretation
28
5.1
S1 × S3 and the two-dimensional Yang-Mills

=== FIGURE STATS ===
TOTAL images=0 drawings=404

=== EQUATION-LIKE NUMBERED PARTICLES IN TEXT LAYER ===
raw occurrences: 186
distinct numbers: 137
per-page raw counts: {"3": 1, "4": 4, "5": 7, "6": 5, "7": 8, "8": 8, "9": 11, "10": 6, "11": 12, "12": 8, "13": 6, "14": 9, "15": 11, "16": 3, "17": 2, "18": 2, "19": 1, "20": 4, "22": 5, "23": 4, "24": 5, "25": 5, "26": 5, "27": 3, "28": 3, "29": 12, "30": 8, "31": 11, "32": 11, "33": 2, "35": 2, "36": 2}

=== KEYWORDS ===
'Appendix': 0 occurrences
'References': 1 occurrences
'Bibliography': 0 occurrences
'Acknowledg': 1 occurrences
'Contents': 1 occurrences

=== CAPTION SCAN (Figure N: / Table N:) ===
  p5 Figure 1: ...T | L | Figure 1: A cylinder with circumference L | considered up to the adjoint G-action U 7→gUg−1. | Then the...
  p6 Figure 2: ...U | U | V | W | Figure 2: A disk and a three-holed sphere, with holonomies around the boundaries speciﬁed | ψA(U) = Z...
  p6 Figure 3: ...tle-Hawking wavefunction. | U | A | A! | A+A! | U | Figure 3: The area of a disk can be changed by gluing a cylinder | So, what is this wavefunction ψA(U...
  p7 Figure 4: ...U, V, W)ψA′(W −1)dW = ψA(U, V ). | (2.15) | Figure 4: Sewing a disk to a hole makes a three-holed sphere into a cylinder | Using (2.13) and (2.14...
  p8 Figure 5: ...1 | 2 | 3 | 4 | 1 | 3 | 4 | 2 | Figure 5: The amplitude does not depend on how one cuts a four-holed sphere into two | three-holed sp...
  p13 Figure 6: ...,¯q), see Fig. 6. | 1 | q | 0 | ∞ | ∞ | 1 | 0 | ∞ | 1 | 0 | q | Figure 6: A four-punctured sphere is composed from two three-punctured sphere by gluing | At the leve...
  p17 Figure 7: ...tured sphere or a cylinder. | i | a | u | Q aiu | Figure 7: A three punctured sphere corresponds to Qaiu, with SU(2)3 symmetry. | 17 | ...
  p18 Figure 8: ... multiplet | with complexified coupling τ | Figure 8: A cylinder with parameter τ corresponds to an SU(2) vector multiplet. | Now, given a collec...
  p19 Figure 9: ...τ | 0 | τ | 1 | Figure 9: A punctured torus can be obtained from gluing two points of a three-punctured | sphere. | sym...
  p20 Figure 10: ...ﬂavor symmetry. | a | i | s | x | a | s | i | x | a | x | s | i | Figure 10: A four-punctured sphere can be decomposed in three diﬀerent ways. | Now, a four-punctured s...
  p27 Figure 11: ...s • • • | ◦ | ◦ | Figure 11: Young diagram Y = (5, 4, 3, 2, 2, 1) and a box s = (2, 2), and its arm and leg | length. | No...
  p35 Figure 12: ...a | d | b | c | e | f | a | d | b | c | e | f | Figure 12: A sphere with six punctures under two diﬀerent decompositions | is SU(2)3 and there are fou...
  p35 Figure 13: ...ry on | S4 | 4d N=2  SU(2) | with 4 ﬂavors on | Figure 13: 6d theory on S4× a Riemann surface, and its dimensional reduction | These two equalities ar...

=== FONTS ===
  ('ALICUN+Times-Italic', 'TT6')
  ('BJGAPW+MSBM10', 'F36')
  ('CANJJO+Times-Roman', 'TT5')
  ('CRPSRL+CMEX8', 'F31')
  ('DJEWCJ+TimesNewRomanPSMT', 'TT5')
  ('EHVFZM+TimesNewRomanPS-ItalicMT', 'TT1')
  ('FWBSAB+Times-Italic', 'TT1')
  ('GWJQAP+MSAM10', 'F33')
  ('GYCOYH+CMTT12', 'F69')
  ('HDIGVY+CMR12', 'F15')
  ('HWZVOK+TimesNewRomanPS-ItalicMT', 'TT4')
  ('IKKZMJ+CMR10', 'F16')
  ('IPYCAX+CMMI10', 'F11')
  ('JESOXW+Times-Italic', 'TT1')
  ('JVCMBX+Times-Italic', 'TT1')
  ('JVPOHN+CMSS12', 'F51')
  ('KVJXHX+CMTT10', 'F20')
  ('LPYQIU+TimesNewRomanPSMT', 'TT2')
  ('MFVUAC+TimesNewRomanPSMT', 'TT1')
  ('NFISZS+CMMI7', 'F10')
  ('NUETUR+CMMI6', 'F26')
  ('OBUTKO+CMR8', 'F22')
  ('PEXIYL+Times-BoldItalic', 'TT1')
  ('PPWXSQ+TimesNewRomanPSMT', 'TT3')
  ('PUKWVQ+CMEX10', 'F30')
  ('QXCTRJ+TimesNewRomanPS-ItalicMT', 'TT2')
  ('QZKRDM+CMBX10', 'F21')
  ('RTUZNT+Symbol', 'TT3')
  ('SACEHT+CMSY6', 'F29')
  ('SCZSFI+TimesNewRomanPS-ItalicMT', 'TT2')
  ('SHRWCP+TimesNewRomanPS-ItalicMT', 'TT1')
  ('TFWCLZ+TimesNewRomanPSMT', 'TT4')
  ('THGOAZ+CMR5', 'F6')
  ('TOGDQC+Times-Italic', 'TT1')
  ('Times-Roman', 'arXivStAmP')
  ('UARRPW+CMR6', 'F23')
  ('UESNFY+TimesNewRomanPS-ItalicMT', 'TT2')
  ('ULIPOG+CMSS8', 'F52')
  ('UQKRXX+TimesNewRomanPSMT', 'TT5')
  ('UQOZNR+CMTI12', 'F48')
  ('VCTIYZ+Times-BoldItalic', 'TT1')
  ('WNFLST+TimesNewRomanPS-ItalicMT', 'TT2')
  ('WNRYSD+CMBX12', 'F18')
  ('WVCKRN+CMMI12', 'F24')
  ('WVSKGQ+Times-Roman', 'TT1')
  ('XCGBWB+CMR7', 'F7')
  ('YJQZYY+TimesNewRomanPS-ItalicMT', 'TT1')
  ('ZAWXVP+EUFM10', 'F63')
  ('ZENVVU+TimesNewRomanPSMT', 'TT3')
  ('ZPZBAK+CMTI10', 'F19')
  ('ZRCHLG+CMSY8', 'F28')
  ('ZRKKWG+CMSY10', 'F27')
  ('ZYUIGY+CMMI8', 'F25')

=== PER PAGE: char count, first line, last line ===
p01 chars= 2038 FIRST='IPMU-16-0048' LAST='arXiv:1608.02964v5  [hep-th]  15 Oct 2016'
p02 chars= 2792 FIRST='3' LAST='2'
p03 chars= 3349 FIRST='X4 very small, we ﬁrst have a two-dimensional theory S(X4), and then we can cons' LAST='3'
p04 chars= 2117 FIRST='supersymmetric localization, and describe how the partition functions on S1 × S3' LAST='4'
p05 chars= 1468 FIRST='T' LAST='5'
p06 chars= 1261 FIRST='U' LAST='6'
p07 chars= 1522 FIRST='Second, it is useful at this point to rewrite the Hamiltonian on the cylinder we' LAST='7'
p08 chars= 1538 FIRST='1' LAST='8'
p09 chars= 1634 FIRST='and' LAST='9'
p10 chars= 1876 FIRST='2.2' LAST='10'
p11 chars= 1958 FIRST='In a free-boson theory, the energy-momentum tensor T(z) is given by T(z) = (1/2)' LAST='11'
p12 chars= 2337 FIRST='that the Lagrangian density (2.43) determines an interacting conformal ﬁeld theo' LAST='12'
p13 chars= 2293 FIRST='continuation, we have' LAST='13'
p14 chars= 1815 FIRST='where p ≥0 is real and positive, and the positive integers' LAST='14'
p15 chars= 1518 FIRST='2.2.4' LAST='15'
p16 chars= 2180 FIRST='Combining the results, we ﬁnd' LAST='16'
p17 chars= 2336 FIRST='The Lagrangian above describes a massless hypermultiplet. To give a mass term, w' LAST='17'
p18 chars= 2442 FIRST='First, take a three-punctured sphere, see Fig. 7. We associate an SU(2) ﬂavor sy' LAST='18'
p19 chars= 2361 FIRST='τ' LAST='19'
p20 chars= 2108 FIRST='subgroups of this SO(8):' LAST='20'
p21 chars= 3078 FIRST='Yang-Mills with gauge group SU(2) with a decoupled hypermultiplet, but with diﬀe' LAST='21'
p22 chars= 2352 FIRST='speciﬁed. This point of view was emphasized ﬁrst in [21] and reviewed in more de' LAST='22'
p23 chars= 2833 FIRST='and ﬂuctuations around them. For this reason we often call δϵO as the localizing' LAST='23'
p24 chars= 2118 FIRST='Correspondingly, the computation of Z(q, g) for an N=2 Lagrangian ﬁeld theory ca' LAST='24'
p25 chars= 2208 FIRST='4.3.1' LAST='25'
p26 chars= 2534 FIRST='over various gauge multiplets, where τ is the complexiﬁed gauge coupling. The se' LAST='26'
p27 chars= 1702 FIRST='s • • •' LAST='27'
p28 chars= 1984 FIRST='the partition function of SU(N) gauge theory with an adjoint hypermultiplet of m' LAST='28'
p29 chars= 1702 FIRST='partition function Z(a1, a2, a3) on S1×S3, when the holonomy of SU(2)i is (ai, 1' LAST='29'
p30 chars= 2135 FIRST='Plugging in the inﬁnite-sum form (5.2) instead, one ﬁnds' LAST='30'
p31 chars= 2189 FIRST='5.2' LAST='31'
p32 chars= 2559 FIRST='Here, mi are the mass parameters for SU(2)i, Zinstanton' LAST='32'
p33 chars= 3239 FIRST='where the equality is again up to multiplication by a function independent of mi' LAST='33'
p34 chars= 3532 FIRST='G. This deﬁnes the Wilson line on L in the representation R. This introduces an ' LAST='34'
p35 chars= 1485 FIRST='a' LAST='35'
p36 chars= 3055 FIRST='We have arrived at the two equations (5.25), (5.26) on S(X4) in a rather roundab' LAST='36'
p37 chars= 3230 FIRST='hypermultiplet in the trifundamental of SU(2)3, see e.g. [38]. Due to this probl' LAST='37'
p38 chars= 2932 FIRST='• The operator sits at a point in X4, and covers the entire C2. This just gives ' LAST='38'
p39 chars= 3496 FIRST='TN theory when G = SU(N). The T2 theory is then the free theory of a half-hyperm' LAST='39'
p40 chars= 3542 FIRST='provided by diﬀerent authors in [55]. The corresponding two-dimensional theories' LAST='40'
p41 chars= 1935 FIRST='since there is only one two-cycle in C2. That said, having an explicit Lagrangia' LAST='41'
p42 chars= 2072 FIRST='[9] A. Gadde, L. Rastelli, S. S. Razamat, and W. Yan, “Gauge Theories and Macdon' LAST='42'
p43 chars= 2204 FIRST='[22] T. Dumitrescu, “An Introduction to Supersymmetric Field Theories in Curved ' LAST='43'
p44 chars= 2276 FIRST='[37] C. Cordova and D. L. Jaﬀeris, “Toda Theory From Six Dimensions,”' LAST='44'
p45 chars= 2270 FIRST='[52] D. Maulik and A. Okounkov, “Quantum Groups and Quantum Cohomology,”' LAST='45'
p46 chars= 1865 FIRST='[67] A. Belavin, M. Bershtein, B. Feigin, A. Litvinov, and G. Tarnopolsky, “Inst' LAST='46'
```
