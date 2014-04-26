# coding=utf-8

# Global settings.
document_class = "ext" + "article"  # Ext is for extsizes package.
font_size = "10pt"  # Allowed: 8pt, 9pt, 10pt, 11pt, 12pt, 14pt, 17pt, 20pt

# Front page.
## Setting title to None also ignores authors and date.
title = {{cookiecutter.name}}
authors = ["Authòr1", "Author2"]
date = r"\today"

abstract = open("abstract.txt", "r").read()

table_contents = True

bibliography_style = "plain"




