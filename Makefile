# Makefile for Muktamsiddham font

FONTS=Muktamsiddham.otf MuktamsiddhamT.ttf MuktamsiddhamG.ttf
DOCUMENTS=license.txt README ChangeLog NEWS
SOURCE=Muktamsiddham.sfd LatinGlyphs.sfd outlines.py truetype.py smp.py Muktamsiddham.gdl Makefile
PKGS=Muktamsiddham.tar.xz Muktamsiddham-source.tar.xz
FFCMD=for i in $?;do fontforge -lang=ff -c "Open(\"$$i\");Generate(\"$@\");Close()";done
PKGCMD=rm -rf $*; mkdir $*; cp $^ $*

# Path to Graphite compiler

# On Windows (Cygwin) uncomment:
#GRCOMPILER=/cygdrive/c/Program\ Files/Graphite\ Compiler/GrCompiler
# For systems other than Windows:
GRCOMPILER=wine ~/.wine/drive_c/Program\ Files/Graphite\ Compiler/GrCompiler.exe


.PHONY: all
all: ${FONTS}

Outlines.sfd: Muktamsiddham.sfd LatinGlyphs.sfd
	fontforge -script ./outlines.py

OutlinesTT.sfd: Outlines.sfd
	fontforge -script ./truetype.py

Muktamsiddham.otf: Outlines.sfd
	${FFCMD}
MuktamsiddhamT.ttf: OutlinesTT.sfd
	${FFCMD}

MuktamsiddhamG.ttf: MuktamsiddhamT.ttf Muktamsiddham.gdl
	${GRCOMPILER} $^ $@ "MuktamsiddhamG"


.SUFFIXES: .tar.xz .tar.gz .tar.bz2 .zip
.PHONY: dist
dist: ${PKGS}

Muktamsiddham.tar.xz: ${FONTS} ${DOCUMENTS}
	${PKGCMD}; tar cfvJ $@ $*
Muktamsiddham.tar.gz: ${FONTS} ${DOCUMENTS}
	${PKGCMD}; tar cfvz $@ $*
Muktamsiddham.tar.bz2: ${FONTS} ${DOCUMENTS}
	${PKGCMD}; tar cfvj $@ $*
Muktamsiddham.zip: ${FONTS} ${DOCUMENTS}
	${PKGCMD}; zip -9r $@ $*

Muktamsiddham-source.tar.xz: ${SOURCE} ${DOCUMENTS}
	${PKGCMD}; tar cfvJ $@ $*
Muktamsiddham-source.tar.gz: ${SOURCE} ${DOCUMENTS}
	${PKGCMD}; tar cfvz $@ $*
Muktamsiddham-source.tar.bz2: ${SOURCE} ${DOCUMENTS}
	${PKGCMD}; tar cfvj $@ $*
Muktamsiddham-source.zip: ${SOURCE} ${DOCUMENTS}
	${PKGCMD}; zip -9r $@ $*

ChangeLog: .git # GIT
	./mkchglog.rb > $@ # GIT

.PHONY: clean
clean:
	-rm -f Outlines.sfd OutlinesTT.sfd \
	gdlerr.txt '$$_temp.gdl' ${FONTS} ChangeLog
	-rm -rf ${PKGS} ${PKGS:.tar.xz=} ${PKGS:.tar.xz=.tar.bz2} \
	${PKGS:.tar.xz=.tar.gz} ${PKGS:.tar.xz=.zip}
