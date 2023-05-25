import sys, os, subprocess

args = ["tmp.rst",
        "-o", "2.pdf",
        "--pdf-engine=xelatex",
        "-V", "monofont=Times New Roman",
        "-V", "mainfont=Times New Roman",
        "-V", "geometry= margin=2cm"
        ]
print(args)
p = subprocess.Popen(["pandoc"] + args)
p.wait()
