@REM Create the fonts set for the readme.md documentation

 py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflprogress "resources/fonts/BTFL_ondrascz_white.png"^
 -o "docs/btfl_progress.bmp"

 py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btfllogo "resources/logos/BTFL_betaflight.png"^
 -o "docs/btfl_btfllogo.bmp"





py fontbuilder.py^
 -base resources/fonts/BTFL_ondrascz.MCM #FFFF00 #0000FF^
 -o "docs/values_mcm.bmp"


py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflcharacters "resources/ttf/DaysOne-Regular.ttf" 25 1.2 1^
 -btfllowletters "resources/ttf/DaysOne-Regular.ttf" 25 1.2 1 0 0 0 0 #8899EE^
 -btflnumbers "resources/ttf/a4speed.ttf" 22 1.4 1.7 -0.5 4.5 0.1 0.1 #FFFF44^
 -o "docs/values_ttf.bmp"^