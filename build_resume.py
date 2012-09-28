#!/usr/bin/env python

#
# see readme for more instructions.
#

import sys
import imp
import os.path

import jinja2

def add_ascii_data(resume):
    """takes a resume datastructure and add some data to the
    hashes for ascii formatting.

This function exists because the source file does not store 
whitespace information, but it's required for the ascii output.
It's easiest to put it in the data structure and let the
templates read and render it as necessary."""

    for hash in resume['TECHNICAL_SKILLS']:
        hash['ascii_whitespace'] = " " * (25 - len(hash['category']))

    for hash1 in resume['WORK_EXPERIENCE']:
        for hash2 in hash1['positions']:
            hash2['ascii_whitespace'] = " " * (26 - len(hash2['name']))

def main():
    """render templates using sourcefile.

takes the arg passed at the command line and saves output
there.  uses export type to determine the template name
and what filename to give the output."""

    # parse argument filepath
    SOURCE_FILE = sys.argv[1]
    name, ext = os.path.splitext(SOURCE_FILE)
    SAVE_AS = os.path.basename(name)

    # import the argument as a python module
    resume_module = imp.load_source('resume', SOURCE_FILE)

    add_ascii_data(resume_module.RESUME)

    # render templates
    template_types = ['html','tex','txt']

    for ttype in template_types:
        # open the template file, make it an object
        template_string = open('templates/' + ttype + '_template.' + ttype, 'r').read()
        template = jinja2.Template(template_string)

        # write the rendered template to file
        output = open(SAVE_AS + '.' + ttype, 'w')
        output.write(template.render(resume_module.RESUME, mode=ttype))
        output.close()

if __name__ == '__main__':
    main()
