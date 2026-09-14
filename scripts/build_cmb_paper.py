#!/usr/bin/env python3
"""Generate the complete P004 LaTeX counterpart from canonical Markdown.

Requires Pandoc. PDF compilation is separate. No manuscript content is inferred.
"""
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
PAPER=ROOT/'papers/P004_cmb_trinity_audit'
HEADER=r'''
\usepackage{mathpazo}
\usepackage{microtype}
\usepackage{fancyhdr}
\usepackage{needspace}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small Atom 2.1: CMB and Trinity representations}
\fancyhead[R]{\small Working draft}
\fancyfoot[C]{\thepage}
\setlength{\headheight}{14pt}
\setlength{\emergencystretch}{3em}
\hypersetup{colorlinks=true,linkcolor=black,urlcolor=blue}
'''

def main():
    source=(PAPER/'paper.md').read_text()
    # The Markdown already includes the title and provenance; avoid a duplicate title page.
    result=subprocess.run(['pandoc','--from=markdown+tex_math_single_backslash','--to=latex','--standalone',
                           '--variable=fontsize:11pt','--variable=geometry:margin=0.85in',
                           '--variable=linestretch:1.08'],input=source,text=True,capture_output=True,check=True)
    latex=result.stdout.replace('\\begin{document}',HEADER+'\n\\begin{document}',1)
    latex=latex.replace('From the repository root:', r'\Needspace{15\baselineskip}'+'\nFrom the repository root:')
    (PAPER/'main.tex').write_text(latex)
    print('WROTE: papers/P004_cmb_trinity_audit/main.tex')

if __name__=='__main__':main()
