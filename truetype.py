#!/usr/local/bin/fontforge

##############################################################################
#
# Muktamsiddham OTF source to TTF source conversion script
#
# This script only runs under FontForge with Python scripting support.
#
##############################################################################

import fontforge;

font = fontforge.open("Outlines.sfd");
font.em = 2048;
font.is_quadratic = True;
font.selection.all();
font.addExtrema();font.round();
font.simplify();font.round();
font.addExtrema();font.round();
font.autoHint();
font.fontname = "MuktamsiddhamT";
font.fullname = font.fontname;
font.familyname = font.fontname;
font.save("OutlinesTT.sfd");
