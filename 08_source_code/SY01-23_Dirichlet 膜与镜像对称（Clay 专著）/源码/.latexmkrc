$pdf_mode = 5;
$xelatex = 'xelatex -interaction=nonstopmode -halt-on-error %O %S';
# biber runs from the project root (latexmk passes build/main.bcf). Point its
# input directory at the root so references.bib is found, not a system copy.
$biber = 'biber --input-directory=. --output-directory=build %O %S';
$out_dir = 'build';
