# -- coding: utf-8 --
"""
Usage:
    apply_template.py -i input_file -o output_file -t template -m metadata

Options:
    -i input_file   Input tex file to use as the templates body.
    -o output_file  Output tex file.
    -t template     Template filename to use (shall be inside templates folder).
    -m metadata     Metadata to use.
    -h, --help      Show this screen and exit.
"""
import json

from jinja2 import Environment, FileSystemLoader
from docopt import docopt


def process_tex_file(input_path, template_name, metadata_path):
    with open(input_path, "r") as tex_file:
        body = tex_file.read()

    with open(metadata_path) as metadata_file:
        metadata = json.load(metadata_file)

    env = Environment(loader=FileSystemLoader("./templates"))
    template = env.get_template(template_name)
    return template.render(body=body, **metadata)

if __name__ == "__main__":
    arguments = docopt(__doc__)

    processed_tex_file = process_tex_file(arguments["-i"], arguments["-t"], arguments["-m"])

    with open(arguments["-o"], "w") as output_file:
        output_file.write(processed_tex_file.encode("utf-8"))