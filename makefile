

build:
	pandoc -f markdown -t latex "name.md" > name.tex
	# Use listings.
	# sed -i -e 's/\\begin{verbatim}/\\begin{minipage}\{0\.95\\textwidth}\\begin{lstlisting}/g' name.tex
	# sed -i -e 's/\\end{verbatim}/\\end{lstlisting}\\end{minipage}/g' name.tex
	python apply_template.py -i name.tex -o name.tex -t latex.template
	latex name.tex
	latex name.tex
	pdflatex name.tex

debug:
	$(MAKE) build
	xdg-open name.pdf &
	@sleep 1
	$(MAKE) clean

clean:
	rm -f *.out *.pdf *.aux *.dvi *.log *.blg *.bbl *.tex-e *.toc

