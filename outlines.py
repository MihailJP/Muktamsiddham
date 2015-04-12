#!/usr/local/bin/fontforge -script

##############################################################################
#
# Muktamsiddham stroke to outline font conversion script
#
# This script only runs under FontForge with Python scripting support.
# With Python 2.7 installed, FontForge may fail to be built. If you experience
# this issue, the following link may help you:
# http://old.nabble.com/Compiling-error-with-Python-td29226850.html
#
##############################################################################

import fontforge
from math import radians

font = fontforge.open("Muktamsiddham.sfd")
font.strokedfont = False

font.selection.all()
font.selection.select(("less","ranges"),"section01","section12")
font.selection.select(("more",),"section10")
font.stroke("eliptical",100,40,radians(-30.0),"square","round")
font.selection.invert()
font.selection.select(("less",),"section09")
font.stroke("circular",40,"square","round")
font.selection.select("section09")
font.stroke("circular",30,"square","round")

font.selection.all()
font.addExtrema();font.round()
font.simplify();font.round()
font.removeOverlap();font.round()
font.simplify();font.round()
font.addExtrema();font.round()

latinFont = fontforge.open("LatinGlyphs.sfd")
font.encoding = "UnicodeBmp"
for glyph in latinFont.glyphs():
	if glyph.isWorthOutputting():
		assert glyph.unicode >= 0
		latinFont.selection.select(glyph.glyphname)
		latinFont.copy()
		font.selection.select(("unicode",),glyph.unicode)
		try:
			font[glyph.unicode] # Check if the glyph already exists
			# Already exists: do nothing
		except TypeError: # No such glyph yet
			font.paste()
			font[glyph.unicode].glyphname = glyph.glyphname
font.encoding = "Original"

font.importLookups(latinFont, latinFont.gsub_lookups)
font.importLookups(latinFont, latinFont.gpos_lookups)

font.autoHint()

font.save("Outlines.sfd")
