all: lekcja1/lekcja1.pdf lekcja2/lekcja2.pdf

lekcja1/lekcja1.pdf: lekcja1/lekcja1.latex Makefile
	cd lekcja1 && latex -output-format pdf -shell-escape lekcja1.latex

lekcja2/lekcja2.pdf: lekcja2/lekcja2.latex Makefile
	cd lekcja2 && latex -output-format pdf -shell-escape lekcja2.latex
