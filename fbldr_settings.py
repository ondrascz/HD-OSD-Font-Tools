# general settings
DEBUG = True

# HD OSD fonts settings
GLYPH_SIZE = (24, 36)
GLYPH_MCM_SIZE = (12, 18)
FONT_GRID_SIZE = (16, 32)
DEMO_GRID_SIZE = (53,20)

# colors
COLOR_TRANSPARENT = (127,127,127)
COLOR_MCM_WHITE = (255,255,255)
COLOR_MCM_BLACK = (0,0,0)
COLOR_TTF_GLYPH = (255,255,255)
COLOR_TTF_OUTLINE = (0,0,0)

# logo dimensions
LOGO_SIZE_BTFL = ( 576, 144 )
LOGO_SIZE_INAV = ( 240, 144 )
LOGO_SIZE_MINI = ( 120, 36 )

# glyphs sets definitions
# all glyphs
GLYPH_SUBSET_ALL = [*range(0,512)]

# all characters (letters, numbers, special characters)
GLYPH_SUBSET_BTFL_CHARACTERS = [*range(32,36)]
GLYPH_SUBSET_BTFL_CHARACTERS.extend( [*range(37,96)] )
GLYPH_SUBSET_BTFL_CHARACTERS.append( 124 )

# letters
GLYPH_SUBSET_BTFL_LETTERS = [*range(65,91)]

# numbers
GLYPH_SUBSET_BTFLNUMBERS = [*range(48,58)]

# lower case letters
GLYPH_SUBSET_BTFL_LOWLETTERS = [*range(97,123)]
GLYPH_SUBSET_BTFL_LOWLETTERS_OFFSET = -32

# special characters
GLYPH_SUBSET_BTFL_SPECIALS = [*range(32,36)]
GLYPH_SUBSET_BTFL_SPECIALS.extend( [*range(37,48)] )
GLYPH_SUBSET_BTFL_SPECIALS.extend( [*range(58,65)] )
GLYPH_SUBSET_BTFL_SPECIALS.extend( [*range(91,96)] )
GLYPH_SUBSET_BTFL_SPECIALS.append( 124 )

# BTFL values icons
GLYPH_SUBSET_BTFL_VALUES = (1, 4, 5, 16, 17, 18, 20, 21, 30, 31, 36, 112, 113, 122, 123, 127, 137, 152, 155, 156)

# BTFL units symbols
GLYPH_SUBSET_BTFL_UNITS = (6, 7, 12, 13, 14, 15, 125, 126, 153, 154, 157, 158, 159)

# BTFL AHI glyphs
GLYPH_SUBSET_BTFL_AHI = (2,3, 19, 114, 115, 116, 117, 118, 119, 120, 128, 129, 130, 131, 132, 133, 134, 135, 136)

# BTFL compass glyphs
GLYPH_SUBSET_BTFL_COMPASS = [*range(24,30)]

# BTFL battery glyphs
GLYPH_SUBSET_BTFL_BATTERY = [*range(144,152)]

# BTFL arrow glyphs
GLYPH_SUBSET_BTFL_ARROW = [*range(96,112)]

# BTFL frame glyphs
GLYPH_SUBSET_BTFL_FRAME = (8,9,10,11,22,23)

# BTFL progress glyphs
GLYPH_SUBSET_BTFL_PROGRESS = [*range(138,144)]

# BTFL logo glyphs
GLYPH_SUBSET_BTFL_LOGO = [*range(160,256)]

# BTFL minilogo glyphs
GLYPH_SUBSET_BTFL_MINILOGO = ( [*range(91,96)] )

# INAV logo glyphs
GLYPH_SUBSET_INAV_LOGO = [*range(257,297)]

# arguments parsing
SWITCHES_FILE = ("", "base", "btflcharacters", "btflnumbers", "btflletters", "btfllowletters" , "btflspecials" , "btflvalues", "btflunits", "btflahi", "btflcompass", "btflbattery", "btflarrow", "btflframe", "btflprogress", "btfllogo", "btflminilogo", "inavlogo" )
SWITCHES_NOFILE = ("o", "explode", "nopreview", "btfldemo", "inavdemo")

# supported files extensions
FILE_INPUT_EXTENSIONS = ("ttf", "mcm", "bmp", "png")
FILE_INPUT_EXTENSIONS_BITMAP = ("bmp", "png")

# switch - extension - subset matrix
SWITCH_EXT_SUBSET_OFFSET_MATRIX = [
    ["base" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_ALL , 0 ],
    ["base" , ["ttf"] , GLYPH_SUBSET_BTFL_CHARACTERS , 0 ],
    ["" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_ALL , 0 ],
    ["" , ["ttf"] , GLYPH_SUBSET_BTFL_CHARACTERS , 0 ],

    ["btflcharacters" , ["ttf", "mcm", "bmp", "png"] , GLYPH_SUBSET_BTFL_CHARACTERS , 0 ],
    ["btflspecials" , ["ttf", "mcm", "bmp", "png"] , GLYPH_SUBSET_BTFL_SPECIALS , 0 ],
    ["btflnumbers" , ["ttf", "mcm", "bmp", "png"] , GLYPH_SUBSET_BTFLNUMBERS , 0 ],
    ["btflletters" , ["ttf", "mcm", "bmp", "png"]  , GLYPH_SUBSET_BTFL_LETTERS , 0 ],
    ["btfllowletters" , ["ttf"] , GLYPH_SUBSET_BTFL_LOWLETTERS , GLYPH_SUBSET_BTFL_LOWLETTERS_OFFSET ],

    ["btflvalues" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_BTFL_VALUES , 0 ],
    ["btflunits" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_BTFL_UNITS , 0 ],
    ["btflahi" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_BTFL_AHI , 0 ],
    ["btflcompass" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_BTFL_COMPASS , 0 ],
    ["btflbattery" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_BTFL_BATTERY , 0 ],
    ["btflarrow" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_BTFL_ARROW , 0 ],
    ["btflframe" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_BTFL_FRAME , 0 ],
    ["btflprogress" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_BTFL_PROGRESS , 0 ],
    ["btfllogo" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_BTFL_LOGO , 0 ],
    ["btflminilogo" , [ "bmp", "png"] , GLYPH_SUBSET_BTFL_MINILOGO , 0 ],

    ["inavlogo" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_INAV_LOGO , 0 ],
]