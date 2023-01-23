@REM py fontbuilder.py resources/ttf/hemi.ttf 20 1.3 1.5 #FFFF88
@REM py fontbuilder.py "resources\ttf\Audiowide-Regular.ttf" 25 1.5 1

@REM py fontbuilder.py -base resources/fonts/BTFL_analog_default.MCM -btfllowletters "resources\ttf\Audiowide-Regular.ttf" 25 1.5 1

@REM py fontbuilder.py -base resources/fonts/BTFL_analog_default.MCM -base "resources\ttf\Audiowide-Regular.ttf" 25 1.5 1 red -btflspecials resources/fonts/BTFL_analog_default.MCM #22FF22

@REM py fontbuilder.py -base resources/fonts/BTFL_ondrascz.MCM #AAAAFF -base "resources\ttf\Audiowide-Regular.ttf" 25 1.2 1 red -btflspecials resources/fonts/BTFL_analog_default.MCM #22FF22 -btflnumbers resources/ttf/hemi.ttf 26 1.3 0.7 #FFFF77

py fontbuilder.py -base resources/fonts/BTFL_ondrascz.MCM #AAAAFF  -btflspecials resources/fonts/BTFL_analog_default.MCM #22FF22 -btflnumbers resources/ttf/hemi.ttf 26 1.3 0.7 #FFFF77 -btfllowletters "resources\ttf\Audiowide-Regular.ttf" 25 1.5 1