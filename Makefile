# Makefile for Muktamsiddham font

.PHONY: all
all: sfd4otf

sfd4otf: Muktamsiddham.sfd LatinGlyphs.sfd
	fontforge -script ./outlines.py

.PHONY: clean
clean:
	rm Outlines.sfd
