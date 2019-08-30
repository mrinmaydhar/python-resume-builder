#!/usr/bin/env python
"""
Python Resume Builder

Usage:
  build_resume.py <source> <outdir>
  build_resume.py -h | --help
  build_resume.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
import sys
import importlib.util
import os.path

from docopt import docopt
import jinja2


def add_ascii_data(resume):
    """ 
    Takes a resume datastructure and adds some data to the
    hashes for ascii formatting.

    This function exists because the source file does not store 
    whitespace information, but it's required for the ascii output.
    It's easiest to put it in the data structure and let the
    templates read and render it as necessary.
    """
    for hash in resume['TECHNICAL_SKILLS']:
        hash['ascii_whitespace'] = " " * (30 - len(hash['category']))
    for hash in resume['EDUCATION']:
        hash['ascii_whitespace'] = " " * (120 - len(hash['degree']))
    for hash1 in resume['WORK_EXPERIENCE']:
        for hash2 in hash1['positions']:
            hash2['ascii_whitespace'] = " " * (120 - len(hash2['name']))

def checkAndReplaceAmpersandInTex(current):
    if isinstance(current, str):
        return current.replace('&', '\&')
    elif isinstance(current, dict):
        for key, value in current.items():
            current[key] = checkAndReplaceAmpersandInTex(value)
        return current
    elif isinstance(current, list):
        return [checkAndReplaceAmpersandInTex(item) for item in current]
    else:
        return current
        
def main(sourceFile, outdir):
    """
    Render the templates using the source file.
    Takes the arg passed at the commandline and saves output
    there.  Uses export type to determine the template name
    and what filename to give the output.
    """
    # parse argument filepath
    name, ext = os.path.splitext(sourceFile)
    SAVE_AS = os.path.join(os.path.relpath(outdir), os.path.basename(name))
    # import the argument as a python module
    spec = importlib.util.spec_from_file_location('resume', sourceFile)
    resume_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(resume_module)
    add_ascii_data(resume_module.RESUME)
    # render templates
    template_types = ['html','txt', 'tex']
    for ttype in template_types:
        # open the template file, make it an object
        template_string = open('templates/' + ttype + '_template.' + ttype, 'r').read()
        template = jinja2.Template(template_string)
        # write the rendered template to file
        filename = SAVE_AS + '.' + ttype
        with open(filename, 'w') as output:
            if ttype == 'tex':
                resume_module.RESUME = checkAndReplaceAmpersandInTex(resume_module.RESUME)
            output.write(template.render(resume_module.RESUME, mode=ttype))

if __name__ == '__main__':
    args = docopt(__doc__, help=True, version='1.0', options_first=False)
    main(args["<source>"], args["<outdir>"])
