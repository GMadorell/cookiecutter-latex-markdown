import requests
import encoding

LATEX_TEMPLATE_URL = "https://raw.githubusercontent.com/Skabed/cookiecutter-latex-markdown/master/%7B%7Bcookiecutter.name%7D%7D/templates/latex.template"
APPLY_TEMPLATE_URL = "https://raw.githubusercontent.com/Skabed/cookiecutter-latex-markdown/master/%7B%7Bcookiecutter.name%7D%7D/scripts/apply_template.py"


def main():
    # Reload latex template because cookiecutter removes tags from it.
    reload_latex_template()
    reload_apply_template()


def reload_latex_template():
    print("Reloading latex template.")
    latex_template = requests.get(LATEX_TEMPLATE_URL).text
    with open("./templates/latex.template", "w") as latex_template_file:
        latex_template_file.write(latex_template)
    print("Done.")


def reload_apply_template():
    print("Reloading apply template.")
    apply_template = requests.get(APPLY_TEMPLATE_URL).text
    with open("./scripts/apply_template.py", "w") as apply_template_file:
        apply_template_file.write(apply_template)
    print("Done.")


if __name__ == "__main__":
    encoding.set_system_encoding_utf8()
    main()
