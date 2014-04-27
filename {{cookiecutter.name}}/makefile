
initialize:
	python scripts/initialize.py

build:
	pandoc -f markdown -t latex "06.01 - Advice for Applying Machine Learning.md" > "06.01 - Advice for Applying Machine Learning.tex"
	# Use listings.
	# sed -i -e 's/\\begin{verbatim}/\\begin{minipage}\{0\.95\\textwidth}\\begin{lstlisting}/g' 06.01 - Advice for Applying Machine Learning}}.tex
	# sed -i -e 's/\\end{verbatim}/\\end{lstlisting}\\end{minipage}/g' 06.01 - Advice for Applying Machine Learning}}.tex

	python scripts/apply_template.py -i "06.01 - Advice for Applying Machine Learning.tex" -o "06.01 - Advice for Applying Machine Learning.tex" -t latex.template

	python scripts/transform_img_eps.py

	latex "06.01 - Advice for Applying Machine Learning".tex
	bibtex "06.01 - Advice for Applying Machine Learning"
	latex "06.01 - Advice for Applying Machine Learning".tex
	latex "06.01 - Advice for Applying Machine Learning".tex
	pdflatex "06.01 - Advice for Applying Machine Learning".tex

debug:
	$(MAKE) build
	xdg-open "06.01 - Advice for Applying Machine Learning.pdf" &
	$(MAKE) clean

publish:
	$(MAKE) build
	$(MAKE) clean	

clean:
	rm -f *.out *.aux *.dvi *.log *.blg *.bbl *.tex-e *.toc *.pyc

