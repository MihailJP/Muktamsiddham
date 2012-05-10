# Makefile for Muktamsiddham font

FONTS=Muktamsiddham.otf MuktamsiddhamT.ttf MuktamsiddhamG.ttf
DOCUMENTS=license.txt README ChangeLog
SOURCE=Muktamsiddham.sfd LatinGlyphs.sfd outlines.py truetype.py Makefile
PKGS=Muktamsiddham.7z Muktamsiddham-source.7z
7ZOPT=-mx9
FFCMD=for i in $?;do fontforge -lang=ff -c "Open(\"$$i\");Generate(\"$@\");Close()";done

# Path to Graphite compiler
GRCOMPILER=/cygdrive/c/Apps/graphite/Graphite\ Compiler/GrCompiler -w4517


.PHONY: all
all: ${FONTS}

Outlines.sfd: Muktamsiddham.sfd LatinGlyphs.sfd
	fontforge -script ./outlines.py

OutlinesTT.sfd: Outlines.sfd
	fontforge -script ./truetype.py

Muktamsiddham.otf: Outlines.sfd
	$(FFCMD)
MuktamsiddhamT.ttf: OutlinesTT.sfd
	$(FFCMD)

MuktamsiddhamG.ttf: MuktamsiddhamT.ttf Muktamsiddham.gdl
	$(GRCOMPILER) $^ $@ "MuktamsiddhamG"


.SUFFIXES: .7z
.PHONY: dist
dist: ${PKGS}

Muktamsiddham.7z: ${FONTS} ${DOCUMENTS}
	-rm -rf $*
	mkdir $*
	cp ${FONTS} ${DOCUMENTS} $*
	7z a ${7ZOPT} $@ $*

Muktamsiddham-source.7z: ${SOURCE} ${DOCUMENTS}
	-rm -rf $*
	mkdir $*
	cp ${SOURCE} ${DOCUMENTS} $*
	7z a ${7ZOPT} $@ $*

.PHONY: clean
clean:
	-rm Outlines.sfd OutlinesTT.sfd gdlerr.txt '$$_temp.gdl' ${FONTS}
	-rm -rf ${PKGS} ${PKGS:.7z=}
