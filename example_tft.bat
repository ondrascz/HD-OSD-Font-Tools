@REM py fontbuilder.py resources/ttf/hemi.ttf 20 1.3 1.5 #FFFF88
@REM py fontbuilder.py "resources\ttf\Audiowide-Regular.ttf" 25 1.5 1

@REM py fontbuilder.py -base resources/fonts/BTFL_analog_default.MCM -btflcharacters "resources\ttf\Audiowide-Regular.ttf" 25 1.5 1

@REM py fontbuilder.py -base resources/fonts/BTFL_analog_default.MCM -base "resources\ttf\Audiowide-Regular.ttf" 25 1.5 1 red -btflspecials resources/fonts/BTFL_analog_default.MCM #22FF22

@REM py fontbuilder.py -base resources/fonts/BTFL_ondrascz.MCM #AAAAFF -base "resources\ttf\Audiowide-Regular.ttf" 25 1.2 1 red -btflspecials resources/fonts/BTFL_analog_default.MCM #22FF22 -btflnumbers resources/ttf/hemi.ttf 26 1.3 0.7 #FFFF77

@REM py fontbuilder.py^
@REM  -base resources/fonts/BTFL_ondrascz.MCM #AAAAFF^
@REM  -btflspecials resources/fonts/BTFL_analog_default.MCM #22FF22^
@REM  -btflnumbers resources/ttf/hemi.ttf 26 1.3 0.7 #FFFF77^
@REM  -btfllowletters "resources\ttf\Audiowide-Regular.ttf" 25 1.5 1

 py fontbuilder.py^
 -base resources/fonts/BTFL_ondrascz.MCM #AAAAFF^
 -btflspecials resources/ttf/robotomonoextraligh.ttf 30 1.3 0.8 #55FF88^
 -btflnumbers resources/ttf/hemi.ttf 30 1.3 1.5 #FFFF77^
 -btflletters "resources\ttf\Audiowide-Regular.ttf" 25 1.5 1 #FF8888^
 -btflvalues resources/fonts/BTFL_analog_default.mcm #4444FF^
 -btflunits resources/fonts/BTFL_analog_default.mcm #AA44FF^
 -btflahi resources/fonts/BTFL_analog_default.mcm #555555 #88FF88^
 -btflcompass resources/fonts/BTFL_analog_default.mcm #AA5A15^
 -btflbattery resources/fonts/BTFL_analog_default.mcm #FF5A15^
 -btflarrow resources/fonts/BTFL_analog_default.mcm #4F8A15 #FFFFFF^
 -btflframe resources/fonts/BTFL_analog_default.mcm #aFaF95 #7A0303^
 -btflprogress resources/fonts/BTFL_analog_default.mcm #7AD3D3^
 -btfllogo resources/fonts/BTFL_analog_default.mcm #FFFF00 #0AAA05^