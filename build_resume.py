#!/usr/bin/env python

#
# see readme for more instructions.
#

import sys
import imp
import os.path

from jinja2 import Template

def add_ascii_data(resume):
    "takes a resume datastructure and add some data to the hashes for ascii formatting."

    for hash in resume['TECHNICAL_SKILLS']:
        hash['ascii_whitespace'] = " " * (25 - len(hash['category']))

    for hash1 in resume['WORK_EXPERIENCE']:
        for hash2 in hash1['positions']:
            hash2['ascii_whitespace'] = " " * (26 - len(hash2['name']))

def main():
    "render templates using sourcefile"

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
        template_string = open('templates/' + ttype + '_template.' + ttype, 'r').read()
        template = Template(template_string)
        output = open(SAVE_AS + '.' + ttype, 'w')
        output.write(template.render(resume_module.RESUME, mode=ttype))
        output.close()

if __name__ == '__main__':
    main()
