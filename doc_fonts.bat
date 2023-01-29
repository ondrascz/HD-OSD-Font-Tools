@REM Create the fonts set for the readme.md documentation

py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflcharacters "resources/fonts/BTFL_ondrascz_white.png"^
 -nopreview^
 -o "docs/btfl_characters.bmp"

py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflspecials "resources/fonts/BTFL_ondrascz_white.png"^
 -nopreview^
 -o "docs/btfl_specials.bmp"
 
py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflnumbers "resources/fonts/BTFL_ondrascz_white.png"^
 -nopreview^
 -o "docs/btfl_numbers.bmp"
 
py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflletters "resources/fonts/BTFL_ondrascz_white.png"^
 -nopreview^
 -o "docs/btfl_letters.bmp"
 
py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btfllowletters "resources/ttf/DaysOne-Regular.ttf" 25 1.2 1 ^
 -nopreview^
 -o "docs/btfl_lowletters.bmp"
 
py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflvalues "resources/fonts/BTFL_ondrascz_white.png"^
 -nopreview^
 -o "docs/btfl_values.bmp" 

py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflunits "resources/fonts/BTFL_ondrascz_white.png"^
 -nopreview^
 -o "docs/btfl_units.bmp"  
 
py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflahi "resources/fonts/BTFL_ondrascz_white.png"^
 -nopreview^
 -o "docs/btfl_ahi.bmp"  

py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflcompass "resources/fonts/BTFL_ondrascz_white.png"^
 -nopreview^
 -o "docs/btfl_compass.bmp"  

py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflframe "resources/fonts/BTFL_ondrascz_white.png"^
 -nopreview^
 -o "docs/btfl_frame.bmp"  

py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflbattery "resources/fonts/BTFL_ondrascz_white.png"^
 -nopreview^
 -o "docs/btfl_battery.bmp"  

py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflarrow "resources/fonts/BTFL_ondrascz_white.png"^
 -nopreview^
 -o "docs/btfl_arrow.bmp"  

py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -inavlogo "resources/logos/INAV6.png"^
 -nopreview^
 -o "docs/inav_logo.bmp"  

py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflminilogo "resources/logos/BTFL_hdzero.png"^
 -nopreview^
 -o "docs/btfl_minilogo.bmp"  





 
 py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflprogress "resources/fonts/BTFL_ondrascz_white.png"^
 -nopreview^
 -o "docs/btfl_progress.bmp"

 py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btfllogo "resources/logos/BTFL_betaflight.png"^
 -nopreview^
 -o "docs/btfl_btfllogo.bmp"





py fontbuilder.py^
 -base resources/fonts/BTFL_ondrascz.MCM #FFFF00 #0000FF^
 -nopreview^
 -o "docs/values_mcm.bmp"


py fontbuilder.py^
 -base "resources/fonts/BTFL_ondrascz_grey.png"^
 -btflcharacters "resources/ttf/DaysOne-Regular.ttf" 25 1.2 1^
 -btfllowletters "resources/ttf/DaysOne-Regular.ttf" 25 1.2 1 0 0 0 0 #8899EE^
 -btflnumbers "resources/ttf/a4speed.ttf" 22 1.4 1.7 -0.5 4.5 0.1 0.1 #FFFF44^
 -nopreview^
 -o "docs/values_ttf.bmp"^