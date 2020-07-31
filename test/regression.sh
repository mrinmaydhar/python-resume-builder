#!/bin/sh

# Run from root directory.  Check output with 'echo $?'

python3 build_resume.py source_files/example_resume.py ./examples/
exit $(git status -u no --short -- examples | wc -l)
