#!/bin/bash

name=$1

sed "s/<<<CONTENT>>>/$name/" template.tex > tmp.tex
xelatex tmp.tex
inkscape --export-area-page --export-type=svg -o $(basename -s .tex $name).svg tmp.pdf
rm tmp.tex tmp.aux tmp.log tmp.pdf
