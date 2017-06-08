# Shishir Tandale
# yaml->tex->pdf

PYTHON=python.exe
SOURCE=in/spec.yaml
MAKETEX=scripts/make_tex.py
MAKEYAML=scripts/make_yaml.py
OUT=resume
CLEAN=*.log *.aux *.bcf *.xml *.bbl *.blg *.tex out/*

resume: latex
	pdflatex $(OUT).tex
	mv $(OUT).pdf out
latex:
	$(PYTHON) $(MAKETEX) -input out/test-spec.yaml -out $(OUT).tex
yaml:
	$(PYTHON) $(MAKEYAML) -out $(SOURCE) #out/test-spec.yaml
clean:
	ls $(CLEAN) | xargs rm
