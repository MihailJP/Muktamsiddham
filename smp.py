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

font = fontforge.open("OutlinesTT.sfd")

codepoints = {
	'akAra':       0x11580,
	'AkAra':       0x11581,
	'it':          0x11582,
	'It':          0x11583,
	'ut':          0x11584,
	'Ut':          0x11585,
	'Rt':          0x11586,
	'RRt':         0x11587,
	'Lt':          0x11588,
	'LLt':         0x11589,
	'et':          0x1158a,
	'ait':         0x1158b,
	'ot':          0x1158c,
	'aut':         0x1158d,
	'ka':          0x1158e,
	'kha':         0x1158f,
	'ga':          0x11590,
	'gha':         0x11591,
	'Ga':          0x11592,
	'ca':          0x11593,
	'cha':         0x11594,
	'ja':          0x11595,
	'jha':         0x11596,
	'Ja':          0x11597,
	'Ta':          0x11598,
	'Tha':         0x11599,
	'Da':          0x1159a,
	'Dha':         0x1159b,
	'Na':          0x1159c,
	'ta':          0x1159d,
	'tha':         0x1159e,
	'da':          0x1159f,
	'dha':         0x115a0,
	'na':          0x115a1,
	'pa':          0x115a2,
	'pha':         0x115a3,
	'ba':          0x115a4,
	'bha':         0x115a5,
	'ma':          0x115a6,
	'ya':          0x115a7,
	'ra':          0x115a8,
	'la':          0x115a9,
	'va':          0x115aa,
	'za':          0x115ab,
	'Sa':          0x115ac,
	'sa':          0x115ad,
	'ha':          0x115ae,
	'AT':          0x115af,
	'iT':          0x115b0,
	'IT':          0x115b1,
	'uT':          0x115b2,
	'UT':          0x115b3,
	'RT':          0x115b4,
	'RRT':         0x115b5,
	'eT':          0x115b8,
	'aiT':         0x115b9,
	'oT':          0x115ba,
	'auT':         0x115bb,
	'candrabindu': 0x115bc,
	'anusvAra':    0x115bd,
	'visarga':     0x115be,
	'virAma':      0x115bf,
	'nukta':       0x115c0,
	'begin':       0x115c1,
	'daNDa':       0x115c2,
	'dvidaNDa':    0x115c3,
	'separator1':  0x115c4,
	'separator2':  0x115c5,
	'ditto1':      0x115c6,
	'ditto2':      0x115c7,
	'ditto3':      0x115c8,
	'terminus':    0x115c9,
	'section01':   0x115ca,
	'section02':   0x115cb,
	'section03':   0x115cc,
	'section13':   0x115cd,
	'section04':   0x115ce,
	'section06':   0x115cf,
	'section07':   0x115d0,
	'section14':   0x115d1,
	'section08':   0x115d2,
	'section15':   0x115d3,
	'section09':   0x115d4,
	'section05':   0x115d5,
	'section12':   0x115d6,
	'section11':   0x115d7,
	'it3':         0x115d8,
	'it2':         0x115d9,
	'It2':         0x115da,
	'ut2':         0x115db,
}

for glyph in font.glyphs():
	if glyph.isWorthOutputting():
		if glyph.glyphname in codepoints:
			glyph.unicode = codepoints[glyph.glyphname]
		elif 0x0900 <= glyph.unicode <= 0x097f:
			glyph.unicode = 0xe000 | (glyph.unicode & 0x0fff)

font.encoding = "UnicodeFull"

latinFont = fontforge.open("LatinGlyphs.sfd")
latinFont.em = font.em
latinFont.selection.select("paragraph")
latinFont.copy()
font.selection.select("paragraph")
font.paste()
latinFont.close()

font.familyname = font.fullname = font.fontname = "MuktamsiddhamG"

for lookup in (font.gsub_lookups + font.gpos_lookups):
	removalFlag = False
	for tag in font.getLookupInfo(lookup)[2]:
		for lang in tag[1]:
			if lang[0] == 'deva':
				removalFlag = True
	if removalFlag:
		font.removeLookup(lookup)

sfnt = []
for sfntName in font.sfnt_names:
	if sfntName[0] == "English (US)":
		if sfntName[1] != "Sample Text":
			sfnt += [sfntName]
		elif sfntName[1] == "Descriptor":
			sfnt += [(sfntName[0], sfntName[1], 'A free Siddham font using Graphite.')]
font.sfnt_names = sfnt

font.save("OutlinesG.sfd")
