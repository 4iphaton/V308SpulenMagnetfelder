ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/main.pdf

# hier Python-Skripte:
build/plot1.pdf: content/python/lang_07.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python content/python/lang_07.py
build/plot2.pdf: content/python/lang_14.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python content/python/lang_14.py
build/plot3.pdf: content/python/kurz_07.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python content/python/kurz_07.py
build/plot4.pdf: content/python/kurz_14.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python content/python/kurz_14.py
build/plot5.pdf: content/python/hh_25i.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python content/python/hh_25i.py
build/plot6.pdf: content/python/hh_25a.py matplotlibrc header-matplotlib.tex | build
		TEXINPUTS="$(call translate,$(pwd):)" python content/python/hh_25a.py
build/plot7.pdf: content/python/hh_50i.py matplotlibrc header-matplotlib.tex | build
		TEXINPUTS="$(call translate,$(pwd):)" python content/python/hh_50i.py
build/plot8.pdf: content/python/hh_50a.py matplotlibrc header-matplotlib.tex | build
	  TEXINPUTS="$(call translate,$(pwd):)" python content/python/hh_50a.py
build/plot9.pdf: content/python/hysterese.py matplotlibrc header-matplotlib.tex | build
		TEXINPUTS="$(call translate,$(pwd):)" python content/python/hysterese.py
build/plot10.pdf: content/python/hysterese2.py matplotlibrc header-matplotlib.tex | build
		TEXINPUTS="$(call translate,$(pwd):)" python content/python/hysterese2.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot1.pdf build/plot2.pdf build/plot3.pdf build/plot4.pdf build/plot5.pdf build/plot6.pdf build/plot7.pdf build/plot8.pdf build/plot9.pdf build/plot10.pdf
build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
