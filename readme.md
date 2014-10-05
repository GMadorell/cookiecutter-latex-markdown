
# cookiecutter-latex-markdown

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for writting latex documents with a markdown abstraction layer on top of it.

## Use me
    $ pip install cookiecutter
    $ cookiecutter https://github.com/Skabed/cookiecutter-latex-markdown.git

You will then be asked about the folder name (which is the same name as the markdown file to edit).

## Workflow

1. Setup metadata (such as the title, abstract, authors, etc).
2. Edit the markdown file. Add pure latex code where needed.
3. make build (or make debug, which will open the file) to create the pdf.

### What happens underneath?
The markdown file gets converted into the body of a .tex file using pandoc. Then, a template gets processed along with the metadata in order to add things such as the table of contents (if that option is enabled) or the tile and authors or the tex file. Afterwards, the tex file is processed with LaTeX and pdflatex.


## Features ##
### Code snippets ###
Simply use the line `#!language` wherever you need, inside of a indented block. For example, for writing some python code, just write the following in the .md file:

        #!python
        def this_is_a_function():
            print("Hello world!")
