grafik.pdf: grafik.latex Makefile
	latex -output-format pdf grafik.latex
grafik.latex: grafik.rst Makefile
	rst2latex grafik.rst > grafik.latex
