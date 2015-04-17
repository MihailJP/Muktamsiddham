# Makefile for Muktamsiddham font

FONTS=Muktamsiddham.otf MuktamsiddhamT.ttf MuktamsiddhamG.ttf
DOCUMENTS=license.txt README ChangeLog NEWS
SOURCE=Muktamsiddham.sfd LatinGlyphs.sfd outlines.py truetype.py smp.py Muktamsiddham.gdl Makefile
PKGS=Muktamsiddham.tar.xz Muktamsiddham-source.tar.xz
FFCMD=for i in $?;do fontforge -lang=ff -c "Open(\"$$i\");Generate(\"$@\");Close()";done

# Path to Graphite compiler
GRCOMPILER=grcompiler


.PHONY: all
all: ${FONTS}

Outlines.sfd: Muktamsiddham.sfd LatinGlyphs.sfd
	fontforge -script ./outlines.py

OutlinesTT.sfd: Outlines.sfd
	fontforge -script ./truetype.py
OutlinesG.sfd: smp.py OutlinesTT.sfd
	fontforge -script ./smp.py OutlinesTT.sfd

Muktamsiddham.otf: Outlines.sfd
	$(FFCMD)
MuktamsiddhamT.ttf: OutlinesTT.sfd
	$(FFCMD)
MuktamsiddhamG-raw.ttf: OutlinesG.sfd
	$(FFCMD)

MuktamsiddhamG.ttf: MuktamsiddhamG-raw.ttf Muktamsiddham.gdl
	$(GRCOMPILER) $^ $@ "MuktamsiddhamG"


.SUFFIXES: .tar.xz
.PHONY: dist
dist: ${PKGS}

Muktamsiddham.tar.xz: ${FONTS} ${DOCUMENTS}
	-rm -rf $*
	mkdir $*
	cp ${FONTS} ${DOCUMENTS} $*
	tar cfvJ $@ $*

Muktamsiddham-source.tar.xz: ${SOURCE} ${DOCUMENTS}
	-rm -rf $*
	mkdir $*
	cp ${SOURCE} ${DOCUMENTS} $*
	sed -ie '/# GIT/d' $*/Makefile
	tar cfvJ $@ $*

ChangeLog: .git # GIT
	./mkchglog.rb > $@ # GIT

.PHONY: clean
clean:
	-rm -f Outlines.sfd OutlinesTT.sfd OutlinesG.sfd MuktamsiddhamG-raw.ttf \
	gdlerr.txt '$$_temp.gdl' ${FONTS} ChangeLog
	-rm -rf ${PKGS} ${PKGS:.tar.xz=}
