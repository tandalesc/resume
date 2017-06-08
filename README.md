# Resume
### Shishir Tandale

LaTeX, Python, and YaML required to build `out/resume.pdf`.

Requires the following technologies:
- TeXLive
- Makefile
- Python 3.6
- PyYAML

Uses Python to interpret a resume YaML file and produce LaTeX which is compiled
into a PDF for an easy content vs. style-separable editing workflow. Document
sections are first specified in the YaML file and their styles and inclusion in the
final document are specified in the Python script.

#### Usage
`make latex` generates a .tex file from the provided .yaml specification document. Using this file, `make resume` uses `pdflatex` to generate a publishable resume. Calling just `make` with no arguments transforms .yaml specifications directly into .pdf resumes.
