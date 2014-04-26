import requests
import encoding

LATEX_TEMPLATE_URL = "https://raw.githubusercontent.com/Skabed/cookiecutter-latex-markdown/master/%7B%7Bcookiecutter.name%7D%7D/templates/latex.template"


def main():
    # Reload latex template because cookiecutter removes tags from it.
    reload_latex_template()


def reload_latex_template():
    latex_template = requests.get(LATEX_TEMPLATE_URL).text
    with open("./templates/latex.template", "w") as latex_template_file:
        latex_template_file.write(latex_template)


if __name__ == "__main__":
    encoding.set_system_encoding_utf8()
    main()
