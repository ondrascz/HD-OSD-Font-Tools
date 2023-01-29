@REM fontbuilder usage examples

fontbuilder.exe^
 -base "resources/fonts/BTFL_ondrascz_color.bmp"^
 -btfllowletters "resources/ttf/DaysOne-Regular.ttf" 25 1.2 1 ^
 -btflnumbers "resources/ttf/a4speed.ttf" 22 1.4 1.7 -0.5 4.5 0.1 0.1 #FFFF44^
 -btfllogo "resources/logos/BTFL_hdzero.png"^
 -btflminilogo "resources/logos/BTFL_ondras.png"^
 -inavlogo "resources/logos/INAV6.png"^
 -btfldemo^
 -explode^
 -o "out/btfl_demo_font.bmp"

@REM py fontbuilder.py^
@REM  -base "resources/fonts/BTFL_ondrascz_color.bmp"^
@REM  -btflminilogo "resources/logos/BTFL_ondras.png"^
@REM  -btfldemo