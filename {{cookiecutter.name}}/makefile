

build:
	pandoc -f markdown -t latex "{{cookiecutter.name}}.md" > {{cookiecutter.name}}.tex
	# Use listings.
	# sed -i -e 's/\\begin{verbatim}/\\begin{minipage}\{0\.95\\textwidth}\\begin{lstlisting}/g' {{cookiecutter.name}}.tex
	# sed -i -e 's/\\end{verbatim}/\\end{lstlisting}\\end{minipage}/g' {{cookiecutter.name}}.tex
	python apply_template.py -i {{cookiecutter.name}}.tex -o {{cookiecutter.name}}.tex -t latex.template
	latex {{cookiecutter.name}}.tex
	latex {{cookiecutter.name}}.tex
	pdflatex {{cookiecutter.name}}.tex

debug:
	$(MAKE) build
	xdg-open {{cookiecutter.name}}.pdf &
	@sleep 1
	$(MAKE) clean

clean:
	rm -f *.out *.pdf *.aux *.dvi *.log *.blg *.bbl *.tex-e *.toc

