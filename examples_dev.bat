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

@REM py fontbuilder.py^
@REM  -base resources/fonts/BTFL_ondrascz.MCM #AAAAFF^
@REM  -btflspecials resources/ttf/robotomonoextraligh.ttf 30 1.3 0.8 #55FF88^
@REM  -btflnumbers resources/ttf/hemi.ttf 30 1.3 1.5 #FFFF77^
@REM  -btflletters "resources\ttf\Audiowide-Regular.ttf" 25 1.5 1 #FF8888^
@REM  -btflvalues resources/fonts/BTFL_analog_default.mcm #4444FF^
@REM  -btflunits resources/fonts/BTFL_analog_default.mcm #AA44FF^
@REM  -btflahi resources/fonts/BTFL_analog_default.mcm #555555 #88FF88^
@REM  -btflcompass resources/fonts/BTFL_analog_default.mcm #AA5A15^
@REM  -btflbattery resources/fonts/BTFL_analog_default.mcm #FF5A15^
@REM  -btflarrow resources/fonts/BTFL_analog_default.mcm #4F8A15 #FFFFFF^
@REM  -btflframe resources/fonts/BTFL_analog_default.mcm #aFaF95 #7A0303^
@REM  -btflprogress resources/fonts/BTFL_analog_default.mcm #7AD3D3^
@REM  -btfllogo resources/fonts/BTFL_analog_default.mcm #FFFF00 #0AAA05^
@REM  -btflminilogo resources/fonts/BTFL_analog_default.mcm #FFFF00 #FFFF00^
@REM  -inavlogo resources/fonts/INAV_analog_default.mcm #0AAA05 #FFFF00 

@REM py fontbuilder.py^
@REM  resources/fonts/BTFL_ondrascz_minimal_lowercase_color_ondras_V1.0.0.bmp^
@REM  -btflspecials resources\ttf\Audiowide-Regular.ttf 25 1.5 1 #FF8888^

@REM py fontbuilder.py^
@REM  resources/fonts/BTFL_gjs_visionplus_v1.0.0.bmp

@REM py fontbuilder.py^
@REM  resources/fonts/INAV6_gjs_visionplus_v1.0.0.bmp

@REM py fontbuilder.py^
@REM  resources/fonts/INAV_analog_default.png

@REM py fontbuilder.py^
@REM  resources/fonts/BTFL_analog_default.png

@REM py fontbuilder.py^
@REM  -base resources/fonts/INAV6_gjs_visionplus_v1.0.0.bmp^
@REM  -btflminilogo "resources/logos/BTFL_ondras.png"

@REM  py fontbuilder.py^
@REM   -base resources/fonts/INAV6_gjs_visionplus_v1.0.0.bmp^
@REM   -btflminilogo "resources/logos/BTFL_ondras.png"^
@REM   -btfllogo "resources/logos/BTFL_hdzero.png"^
@REM   -inavlogo "resources/logos/BTFL_hdzero.png"^
@REM   -o "out/compiled_font.bmp"^
@REM   -explode


@REM py fontbuilder.py^
@REM  -btflcharacters "resources/ttf/hemi.ttf" 28 1.2 1 #77AAFF
@REM  -o "out/compiled_font.bmp"^
@REM  -explode

@REM  py fontbuilder.py^
@REM  -btflcharacters "resources/ttf/DaysOne-Regular.ttf" 20 1.2 1 #77AAFF^
@REM  -o "out/compiled_font.bmp"^
@REM  -explode

@REM   py fontbuilder.py^
@REM  -btflcharacters "resources/ttf/RussoOne-Regular.ttf" 28 1.3 1 #77AAFF^
@REM  -o "out/compiled_font.bmp"^
@REM  -explode

@REM py fontbuilder.py^
@REM  -base "resources/fonts/BTFL_ondrascz_grey.png"^
@REM  -btflcharacters "resources/ttf/DaysOne-Regular.ttf" 20 1.2 1 ^
@REM  -btfllowletters "resources/ttf/DaysOne-Regular.ttf" 20 1.2 1 ^
@REM  -btflnumbers "resources/ttf/a4speed.ttf" 22 1.5 1.6 ^
@REM  -o "out/compiled_font.bmp"^
@REM  -explode

@REM  py fontbuilder.py^
@REM  -base "resources/fonts/BTFL_ondrascz_grey.png"^
@REM  -btflprogress "resources/fonts/BTFL_ondrascz_white.png"^
@REM  -o "docs/btfl_progress.bmp"^

@REM  py fontbuilder.py^
@REM  -base "resources/fonts/BTFL_ondrascz_grey.png"^
@REM  -btfllogo "resources/logos/BTFL_betaflight.png"^
@REM  -o "docs/btfl_btfllogo.bmp"^



 py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_color.bmp"^
 -btfllowletters "resources/ttf/DaysOne-Regular.ttf" 25 1.2 1 ^
 -btflnumbers "resources/ttf/a4speed.ttf" 22 1.4 1.7 -0.5 4.5 0.1 0.1 #FFFF44^
 -btfllogo "resources/logos/BTFL_hdzero.png"^
 -btflminilogo "resources/logos/BTFL_ondras.png"^
 -inavlogo "resources/logos/INAV6.png"^
 -btfldemo^
 -explode^
 -o "out/btfl_demo_font.bmp"^

@REM py fontbuilder.py^
@REM  -base "resources/fonts/BTFL_ondrascz_color.bmp"^
@REM  -btfldemo