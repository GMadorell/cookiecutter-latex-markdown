
initialize:
	python scripts/initialize.py

build:
	pandoc -f markdown -t latex "{{cookiecutter.name}}.md" > "{{cookiecutter.name}}.tex"
	# Use listings.
	# sed -i -e 's/\\begin{verbatim}/\\begin{minipage}\{0\.95\\textwidth}\\begin{lstlisting}/g' "{{cookiecutter.name}}"}}.tex
	# sed -i -e 's/\\end{verbatim}/\\end{lstlisting}\\end{minipage}/g' "{{cookiecutter.name}}"}}.tex

	python scripts/apply_template.py -i "{{cookiecutter.name}}.tex" -o "{{cookiecutter.name}}.tex" -t latex.template

	python scripts/transform_img_eps.py

	latex -shell-escape "{{cookiecutter.name}}".tex
	bibtex "{{cookiecutter.name}}"
	latex -shell-escape "{{cookiecutter.name}}".tex
	latex -shell-escape "{{cookiecutter.name}}".tex
	pdflatex -shell-escape "{{cookiecutter.name}}".tex

debug:
	$(MAKE) clean
	$(MAKE) build
	xdg-open "{{cookiecutter.name}}.pdf" &
	$(MAKE) clean

publish:
	$(MAKE) build
	$(MAKE) clean   

clean:
	rm -f *.out *.aux *.dvi *.log *.blg *.bbl *.tex-e *.toc *.pyc