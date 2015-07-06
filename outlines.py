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

strokeType = {
	'section01': ('circular', 40),
	'section02': ('circular', 40),
	'section03': ('circular', 40),
	'section04': ('circular', 40),
	'section05': ('circular', 40),
	'section06': ('circular', 40),
	'section07': ('circular', 40),
	'section08': ('circular', 40),
	'section09': ('circular', 30),
	'section11': ('circular', 40),
	'section12': ('circular', 40),
	'section13': ('circular', 40),
	'section14': ('circular', 40),
	'section15': ('circular', 35),
}

for glyph in font.glyphs():
	if glyph.isWorthOutputting():
		if glyph.glyphname not in strokeType:
			glyph.stroke("eliptical",100,40,radians(-30.0),"square","round")
		elif strokeType[glyph.glyphname][0] == 'circular':
			glyph.stroke("circular",strokeType[glyph.glyphname][1],"square","round")
		else: # this should not occur
			raise ValueError, "unsupported stroke type"

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
