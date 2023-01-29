@REM Create the fonts set for the readme.md documentation

 py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflprogress "resources/fonts/BTFL_ondrascz_white.png"^
 -o "docs/btfl_progress.bmp"

 py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btfllogo "resources/logos/BTFL_betaflight.png"^
 -o "docs/btfl_btfllogo.bmp"