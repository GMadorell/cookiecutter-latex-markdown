
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

### Pandoc Markdown Dialect ###
Pandoc is used to transform Markdown to Tex. This means that we get access to the Pandoc Markdown dialect, which has a lot more things than the basic one created by John Gruber’s. We have access to:

* Tables
* Headers with identifiers.
* Fenced blocks.
* Line blocks.
* Horitzontal rules.

And more things. Check [the pandoc docs](http://johnmacfarlane.net/pandoc/demo/example9/pandocs-markdown.html) for more information.

### Code snippets ###
Simply use the line `#!language` wherever you need, inside of a indented block. For example, for writing some python code, just write the following in the .md file:

        #!python
        def this_is_a_function():
            print("Hello world!")

### Images ###
A shortcut can be used whenever we want to insert an image as a **figure**:

    \stdfig{width}{image_name}{Image title}

A image with name `image_name.extension` (currently the only supported extension is *.png*) will be searched inside the *img* directory and will be automatically converted to *.eps* and inserted with the given width.  
A label will be created for the image with value *fig:image_name*.

#### In Place Images ####
If we want to add an uncaptioned image at the exact same location as the code, we can use the syntax:

    \inplacefig{width}{image_name}

Works the same way as \stdfig except that the image isn't floating.

### Latex commands ###
#### Math ####

* Absolute value: \abs{smth} -> |smth|
* Norm: \norm{smth} -> ||smth||


