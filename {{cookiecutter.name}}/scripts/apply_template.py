# -- coding: utf-8 --
"""
Usage:
    apply_template.py -i input_file -o output_file -t template

Options:
    -i input_file   Input tex file to use as the templates body.
    -o output_file  Output tex file.
    -t template     Template filename to use (shall be inside templates folder).
    -h, --help      Show this screen and exit.
"""
import re

from jinja2 import Environment, FileSystemLoader
from docopt import docopt
import os
import sys
import encoding

# Add parent directory to the path.
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(PARENT_DIR)
from metadata import *

SPACE_AFTER_FIRST_BRACKET_REG = re.compile(r"({ [\d\D]*?})")
SPACE_BEFORE_LAST_BRACKET_REG = re.compile(r"({[\d\D]*? })")
SPACE_AROUND_BRACKETS_REG = re.compile(r"({ [\d\D]*? })")


def process_tex_file(input_path, template_name):
    with open(input_path, "r") as tex_file:
        body = tex_file.read()

    citations_found = "\cite{" in body
    g_layout = "top={0}, bottom={1}, left={2}, right={3}".format(top_margin, bot_margin, left_margin, right_margin)

    env = Environment(loader=FileSystemLoader("./templates"))
    template = env.get_template(template_name)
    templated_text = template.render(body=body, citations_found=citations_found,
                                     geometry_layout=g_layout, **globals())

    return post_process_templated_text(templated_text)


def post_process_templated_text(templated_text):
    return remove_spaces_around_brackets(templated_text)


def remove_spaces_around_brackets(text):
    text = remove_spaces_at_positions(text, SPACE_AFTER_FIRST_BRACKET_REG, [1])
    text = remove_spaces_at_positions(text, SPACE_BEFORE_LAST_BRACKET_REG, [-2])
    text = remove_spaces_at_positions(text, SPACE_AROUND_BRACKETS_REG, [1, -2])
    return text


def remove_spaces_at_positions(text, regex, positions):
    for group in regex.findall(text):
        new_group = group
        for displacement, position in enumerate(positions):
            new_group = new_group[:position] + new_group[position + 1:]
        text = text.replace(group, new_group)
    return text


if __name__ == "__main__":
    arguments = docopt(__doc__)

    # Solve a problem with the encoding of the metadata.
    encoding.set_system_encoding_utf8()

    processed_tex_file = process_tex_file(arguments["-i"], arguments["-t"])

    with open(arguments["-o"], "w") as output_file:
        output_file.write(processed_tex_file.encode("utf-8"))