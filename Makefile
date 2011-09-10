# Makefile for Muktamsiddham font

.PHONY: all
all: Muktamsiddham.otf MuktamsiddhamT.ttf

Outlines.sfd: Muktamsiddham.sfd LatinGlyphs.sfd
	fontforge -script ./outlines.py

OutlinesTT.sfd: Outlines.sfd
	fontforge -script ./truetype.py

Muktamsiddham.otf: Outlines.sfd
	fontforge -lang=ff -c "Open(\"$<\");Generate(\"$@\");Close()"
MuktamsiddhamT.ttf: OutlinesTT.sfd
	fontforge -lang=ff -c "Open(\"$<\");Generate(\"$@\");Close()"

.PHONY: clean
clean:
	rm Outlines.sfd OutlinesTT.sfd Muktamsiddham.otf MuktamsiddhamT.ttf
