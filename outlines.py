#!/usr/local/bin/fontforge -script

##############################################################################
#
# Muktamsiddham stroke to outline font conversion script
#
# This script only runs under FontForge with Python scripting support.
# font.stroke() in FontForge-20110222 causes a crash; do not use this version.
# On version 20100501 it works well.
#
# With Python 2.7 installed, FontForge may fail to be built. If you experience
# this issue, the following link may help you:
# http://old.nabble.com/Compiling-error-with-Python-td29226850.html
#
##############################################################################

import fontforge;

font = fontforge.open("Muktamsiddham.sfd");
font.strokedfont = False;
font.selection.all();
font.stroke("eliptical",100,40,-30.0/180.0*3.141592653589793238,"square","round");
font.addExtrema();font.round();
font.simplify();font.round();
font.removeOverlap();font.round();
font.simplify();font.round();
font.addExtrema();font.round();
font.autoHint();
font.mergeFonts("LatinGlyphs.sfd");
font.save("Outlines.sfd");
