PYTHON-RESUME-BUILDER
=====================
This project uses a python template system to produce many output formats of the same resume.  The resume is stored directly in python source code and pushed through the jinja template system (similar to Django) to plain text, html and tex source. The tex source can then be compiled to PDF using rubber.  

REQUIREMENTS
------------
- nix                        (tested with Ubuntu 20.04 Focal Fossa)  
- Python                      (tested with 3.8.2)  
- Jinja                       (tested with 2.10.1-2, via ubuntu package python-jinja2)  
- rubber                    (tested with ubuntu package rubber)  

INSTRUCTIONS
------------
From the project directory, run:  

~$ ./build_resume.py [source_file.py] [out_directory]  
~$ rubber [source_file.tex]  

TO-DO
-----
- Update main script to validate arguments  
- Add usage statement to main script
- change resume source_file format to a friendlier format than .py.
- add octocat icon next to github url!
- Create a .deb installation file for offline use
- Create a web app using flask, deploy it to Heroku, and host on static GitHub Pages
