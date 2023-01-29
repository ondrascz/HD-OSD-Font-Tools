from math import floor
import sys
from os import environ, path
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

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
    ["btflminilogo" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_BTFL_MINILOGO , 0 ],

    ["inavlogo" , ["mcm", "bmp", "png"] , GLYPH_SUBSET_INAV_LOGO , 0 ],
]

# main program
def main():

    # init pygame
    pygame.init()
    clock = pygame.time.Clock() 

    # init a pygame screen (the default one for a built font)
    pygame.display.set_icon( pygame.image.load("resources/icon/icon.png") )
    pygame.display.set_caption("Font Builder Preview (click to close)")
    screen = pygame.display.set_mode((GLYPH_SIZE[0] * FONT_GRID_SIZE[0], GLYPH_SIZE[1] * FONT_GRID_SIZE[1]), pygame.SCALED)

    # parse CLI arguments
    cli_parsed_args = parse_cli_args()

    # validate the parsed arguments
    valid_args = validate_args( cli_parsed_args )
    
    # process the valid input files and create the input font surfaces
    source_font_surfaces = []
    for switch, values in valid_args:
        
        # the input file is .MCM analog OSD font
        if switch in SWITCHES_FILE and path.splitext(values[0])[1][1:].lower() == "mcm":
            source_font_surfaces.append( load_mcm( *values ) )

        # the input file is .TTF font
        if switch in SWITCHES_FILE and path.splitext(values[0])[1][1:].lower() == "ttf":
            source_font_surfaces.append( load_ttf( *values, chars_to_render=range(32,125) ) )

        # the input file is bitmap
        if switch in SWITCHES_FILE and path.splitext(values[0])[1][1:].lower() in FILE_INPUT_EXTENSIONS_BITMAP:
            source_font_surfaces.append( load_bitmap( *values ))

    # prepare target surface (for the built font)
    target_surf = pygame.Surface((GLYPH_SIZE[0] * FONT_GRID_SIZE[0], GLYPH_SIZE[1] * FONT_GRID_SIZE[1]))
    target_surf.fill(COLOR_TRANSPARENT)
    
    # compile the source surfaces
    if DEBUG: print("[DEBUG] Source surfaces compiler:")
    if DEBUG: print("[DEBUG] ")
    
    for source_nr, source_surf in enumerate( source_font_surfaces ):
        
        source_switch = str(valid_args[source_nr][0])
        source_ext = path.splitext(valid_args[source_nr][1][0])[1][1:].lower()
        
        if DEBUG: print("[DEBUG] Source nr. " + str(source_nr) + ": " + str(source_surf) + ", Switch: \"" + source_switch + "\", Source file extension: \"" + source_ext + "\"")

        # get the glyphs subset according to a switch and file extension
        for switch_matrix in SWITCH_EXT_SUBSET_OFFSET_MATRIX:
            
            # the source switch match the source file extension
            if switch_matrix[0] == source_switch and source_ext in switch_matrix[1]:
                 
                 if DEBUG: print("[DEBUG] Switch / extension combination is valid")

                 # copy the glyphs from the source to the target surface
                 for glyph in switch_matrix[2]:
                    copy_glyph( glyph, source_surf , target_surf , switch_matrix[3])
    
    if DEBUG: print("[DEBUG] ----")


    # process the valid output options
    if DEBUG: print("[DEBUG] Output handling:")
    if DEBUG: print("[DEBUG] ")
    
    show_preview = True
    show_demo = False
    demo_variant = "btfldemo"
    explode_output = False
    save_font = False

    for switch, values in valid_args:

        if switch in SWITCHES_NOFILE:

            # disable preview
            if switch == "nopreview" or switch == "btfldemo" or switch == "inavdemo":
                show_preview = False
                if DEBUG: print("[DEBUG]   Preview will not open...")

            # enable demo
            if switch == "btfldemo" or switch == "inavdemo":
                show_preview = False
                show_demo = True

                if switch == "inavdemo": demo_variant = "inavdemo"

                if DEBUG: print("[DEBUG]   Demo \"" + demo_variant + "\" will open instead of preview...")
                
            # enable exploded output
            if switch == "explode":
                explode_output = True
                if DEBUG: print("[DEBUG]   Saved font will be exploded...")

            # save built font
            if switch == "o":
                if values[0] != "":
                    
                    save_font = True
                    corrected_filename = path.splitext(values[0])[0] + ".bmp" 
                    
                    if DEBUG: print("[DEBUG]   Font will be saved...")
                    if DEBUG: print("[DEBUG]     entered file name: " + str(values[0]))
                    if DEBUG: print("[DEBUG]     corrected file name: " + corrected_filename)

    # handle font output to a file
    if save_font == True:
        
        if DEBUG: print("[DEBUG]   Saving the built font...")

        if explode_output == True:
            pygame.image.save( explode_font_surf( target_surf ) , corrected_filename )
        else:
            pygame.image.save( target_surf , corrected_filename )

    # handle windows
    if show_preview == True:
        
        # show preview
        if DEBUG: print("[DEBUG]   Showing preview of the font...")
        screen.blit( target_surf ,(0,0))
    
    elif show_preview == False and show_demo == False :

        # close preview, quit
        if DEBUG: print("[DEBUG]   Disabling preview window, quitting...")
        
        pygame.display.quit()
        pygame.quit()
        sys.exit()

    elif show_preview == False and show_demo == True :

        # close preview, open demo
        if DEBUG: print("[DEBUG]   Disabling preview window, Opening demo window...")
        
        pygame.display.quit()
        pygame.display.set_icon( pygame.image.load("resources/icon/icon.png") )
        pygame.display.set_caption("Font Builder Demo (click to close)")
        screen = pygame.display.set_mode((1280,720), pygame.SCALED)

        # demo background
        demo_surf = pygame.image.load("resources/demo/bkg_001.jpg")
        demo_surf = pygame.transform.smoothscale(demo_surf, (1280,720))
        screen.blit(demo_surf, (0,0))

        # print OSD elements
        
        # BTFL mini logo
        print_glyph( string_to_ord_list("[\]^_ AIR") , target_surf , screen , (1,1) )
        
        # BTFL logo
        # print_glyph( string_to_ord_list("BTFL LOGO:") , target_surf , screen , (22,4) )
        print_glyph( [*range(160,184)] , target_surf , screen , (15,5) )
        print_glyph( [*range(184,208)] , target_surf , screen , (15,6) )
        print_glyph( [*range(208,232)] , target_surf , screen , (15,7) )
        print_glyph( [*range(232,256)] , target_surf , screen , (15,8) )

        # INAV logo
        # print_glyph( string_to_ord_list("INAV6 LOGO:") , target_surf , screen , (22,9) )
        # print_glyph( [*range(257,267)] , target_surf , screen , (22,10) )
        # print_glyph( [*range(267,277)] , target_surf , screen , (22,11) )
        # print_glyph( [*range(277,287)] , target_surf , screen , (22,12) )
        # print_glyph( [*range(287,297)] , target_surf , screen , (22,13) )

        # compass
        print_glyph( (24, 29 , 28 , 29 , 26 , 29 , 28 ,  ) , target_surf , screen , (22,1) )

        # lon / lat
        print_glyph( [137,] , target_surf , screen , (40,1) )
        print_glyph( string_to_ord_list("52.2041699") , target_surf , screen , (41,1) )
        print_glyph( [152,] , target_surf , screen , (40,2) )
        print_glyph( string_to_ord_list("13.0169579") , target_surf , screen , (41,2) )

        # alt
        print_glyph( string_to_ord_list( chr(127) + "37.2" + chr(12)) , target_surf , screen , (3,4) )
        # home
        print_glyph( [98,32,17] , target_surf , screen , (22,4 ))
        print_glyph( string_to_ord_list("2.46" + chr(125)) , target_surf , screen , (25,4) )
        # sats
        print_glyph( string_to_ord_list( chr(30) + chr(31) + "13") , target_surf , screen , (45,4) )

        # odo
        print_glyph( string_to_ord_list(chr(113) + "876" + chr(12)) , target_surf , screen , (4,16) )
        # current
        print_glyph( string_to_ord_list("12.44" + chr(154)) , target_surf , screen , (3,17) )
        # capacity
        print_glyph( string_to_ord_list("965" + chr(7)) , target_surf , screen , (5,18) )
        # voltage
        print_glyph( string_to_ord_list(chr(149) + "3.81" + chr(6)) , target_surf , screen , (15,18) )
        # fly time
        print_glyph( string_to_ord_list(chr(156) + "12:35") , target_surf , screen , (25,18) )
        # speed
        print_glyph( string_to_ord_list(chr(112) + "94" + chr(158)) , target_surf , screen , (35,18) )
        # rssi
        print_glyph( string_to_ord_list(chr(1) + "-85") , target_surf , screen , (45,17) )
        # lq
        print_glyph( string_to_ord_list(chr(123) + "2:100") , target_surf , screen , (45,18) )

        # text
        print_glyph( string_to_ord_list("*** THAT IS FLYING PRETTY WELL ***") , target_surf , screen , (10,10) )

        

        
        




            



    
    
    # pygame loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pygame.quit()
                sys.exit()

            # if event.type == pygame.KEYUP:
            #     pygame.quit()
            #     sys.exit()


        pygame.display.update()
        clock.tick(60)

# the load functions return a pygame Surface

# load and process MCM font file
def load_mcm(
    filename,
    mcm_glyph_color = COLOR_MCM_WHITE,
    mcm_outline_color = COLOR_MCM_BLACK,
):
    
    if DEBUG: print("[DEBUG] MCM font loader:")
    if DEBUG: print("[DEBUG]")
    
    # surfaces to operate glyphs and font
    glyph_mcm_surf = pygame.Surface(GLYPH_MCM_SIZE)
    font_surf = pygame.Surface(( GLYPH_SIZE[0] * FONT_GRID_SIZE[0] , GLYPH_SIZE[1] * FONT_GRID_SIZE[1] ))
    font_surf.fill( COLOR_TRANSPARENT )
    font_glyph_pos = [0,0]
    
    # open MCM file
    if DEBUG: print("[DEBUG] MCM font to load: " + filename)
    mcm_file = open(filename, "r")

    # read the mcm file into an array
    mcm_content = mcm_file.read().splitlines()
    mcm_file.close()

    # get rid of the first line in mcm_file
    if mcm_content[0] == "MAX7456":
        mcm_content.pop(0)

    # for each glyph in mcm file
    for glyph_mcm_start_byte in range(0, int(len(mcm_content)), 64):

        # clean the glyph surface
        glyph_mcm_surf.fill(COLOR_TRANSPARENT)
        # reset the glyph pixel position
        glyph_px_pos = [0,0]
        
        # for each glyph line
        for glyph_mcm_line_start_byte in range(0, 54 , 3):
            
            glyph_px_pos[0] = 0
            pixels = ""
            
            # for each glyph sub line
            for glyph_line_byte_num in range(0, 3):
                
                glyph_mcm_byte = mcm_content[glyph_mcm_start_byte + glyph_mcm_line_start_byte + glyph_line_byte_num]

                # decode byte to three pixels
                for i in range(0,8,2):
                    if glyph_mcm_byte[i:i+2] == "00":
                        # black pixel
                        glyph_mcm_surf.set_at(glyph_px_pos, mcm_outline_color)
                        pixels += ".."
                    elif glyph_mcm_byte[i:i+2] == "10":
                        # white pixel
                        glyph_mcm_surf.set_at(glyph_px_pos, mcm_glyph_color)
                        pixels += "XX"
                    else:
                        # transparent pixel
                        pixels += "  "
                    
                    glyph_px_pos[0] += 1        
            
            glyph_px_pos[1] += 1
        
        font_glyph_code = int(glyph_mcm_start_byte/64)
        font_glyph_pos[1] = int(font_glyph_code / FONT_GRID_SIZE[0])
        font_glyph_pos[0] = (font_glyph_code - font_glyph_pos[1] * FONT_GRID_SIZE[0])
        
        font_surf.blit( pygame.transform.scale(glyph_mcm_surf,GLYPH_SIZE), ( font_glyph_pos[0] * GLYPH_SIZE[0] , font_glyph_pos[1] * GLYPH_SIZE[1] ) )

    if DEBUG: print("[DEBUG] ----")
    
    return( font_surf )

# load and process TTF font file
def load_ttf(
    font_file,
    size = 15,
    outline_thickness = 1.5,
    glyph_vertical_stretch = 1,
    glyph_offset_x = 0,
    glyph_offset_y = 0,
    outline_offset_x = 0,
    outline_offset_y = 0,
    glyph_color = COLOR_TTF_GLYPH,
    outline_color = COLOR_TTF_OUTLINE,
    super_sampling = 8,
    chars_to_render = GLYPH_SUBSET_BTFL_CHARACTERS,
):
    
    if DEBUG: print("[DEBUG] TTF font loader:")
    if DEBUG: print("[DEBUG]")
    
    # repair the arguments types (might be originated from a command line and be strings)
    size = int(size)
    super_sampling = int(super_sampling)
    outline_thickness = float(outline_thickness)
    glyph_vertical_stretch = float(glyph_vertical_stretch)
    glyph_offset_x = float(glyph_offset_x)
    glyph_offset_y = float(glyph_offset_y)
    outline_offset_x = float(outline_offset_x)
    outline_offset_y = float(outline_offset_y)
    
    
    # load the font file
    if DEBUG: print("[DEBUG] TTF font to load: " + font_file)
    if DEBUG: print("[DEBUG] TTF font size to render: " + str(size))
    osd_font = pygame.font.Font(font_file, size * super_sampling)
    
    # surfaces to operate glyphs and font
    font_surf = pygame.Surface(( GLYPH_SIZE[0] * FONT_GRID_SIZE[0] , GLYPH_SIZE[1] * FONT_GRID_SIZE[1] ))
    font_surf.fill( COLOR_TRANSPARENT )
    glyph_ttf_surf = pygame.Surface((GLYPH_SIZE[0] * super_sampling, GLYPH_SIZE[1] * super_sampling  / glyph_vertical_stretch)).convert_alpha()
    
    for char in chars_to_render:

        glyph_y= floor( (char) / FONT_GRID_SIZE[0] )
        glyph_x=(char) - glyph_y * FONT_GRID_SIZE[0]
        
        # clean the surface for this glyph
        glyph_ttf_surf.fill( COLOR_TRANSPARENT )
        
        osd_character = chr(char)
        osd_glyph = osd_font.render(osd_character,True,glyph_color)
        osd_glyph_rect = osd_glyph.get_rect()
        osd_outline = osd_font.render(osd_character,False,outline_color)
        osd_outline_rect = osd_outline.get_rect()
        
        # blit not anti aliased outline to glyph surface
        for x in range(int(-outline_thickness * super_sampling) , int(outline_thickness * super_sampling) + 1):
            for y in range(int(-outline_thickness * super_sampling / glyph_vertical_stretch) ,int(outline_thickness * super_sampling / glyph_vertical_stretch) + 1):
                osd_outline_rect.centerx = x + ( GLYPH_SIZE[0]/2 + outline_offset_x + glyph_offset_x ) * super_sampling
                osd_outline_rect.centery = y + ( GLYPH_SIZE[1]/2 + outline_offset_y + glyph_offset_y ) * super_sampling / glyph_vertical_stretch
                glyph_ttf_surf.blit(osd_outline, osd_outline_rect)

        # scale down the outline, blit to font surface
        font_surf.blit(
            pygame.transform.scale(glyph_ttf_surf,(glyph_ttf_surf.get_size()[0]/super_sampling, glyph_ttf_surf.get_size()[1]/super_sampling * glyph_vertical_stretch)),
            (glyph_x*GLYPH_SIZE[0],glyph_y*GLYPH_SIZE[1])
        )
        
        # blit anti aliased glyph to glyph surface
        glyph_ttf_surf.fill((0,0,0,0))
        osd_glyph_rect.centerx = ( GLYPH_SIZE[0]/2 + glyph_offset_x ) * super_sampling
        osd_glyph_rect.centery = ( GLYPH_SIZE[1]/2 + glyph_offset_y ) * super_sampling / glyph_vertical_stretch
        glyph_ttf_surf.blit(osd_glyph, osd_glyph_rect)
        
        # scale down the glyph, blit to font surface
        font_surf.blit(
            pygame.transform.smoothscale(glyph_ttf_surf,(glyph_ttf_surf.get_size()[0]/super_sampling, glyph_ttf_surf.get_size()[1]/super_sampling * glyph_vertical_stretch)),
            (glyph_x*GLYPH_SIZE[0],glyph_y*GLYPH_SIZE[1])
        )

    if DEBUG: print("[DEBUG] ----")
    
    return(font_surf)

# parse CLI arguments
def parse_cli_args():
    
    # arguments parsing variables
    cli_parsed_args = []
    cli_switch_values = []
    cli_switch = ""

    if DEBUG: print("[DEBUG] Command line arguments parser:")
    if DEBUG: print("[DEBUG]")
    if DEBUG: print("[DEBUG] Argv: " + str(sys.argv[1:]))
    
    # iterate over a list of arguments except the first (program file name)
    for arg in sys.argv[1:]:
        # is the argument a switch?
        if arg[0:1] == "-" and not arg[1:2].isnumeric() :
            # append previous switch and its values to parsed arguments list
            cli_parsed_args.append([cli_switch, cli_switch_values])
            # set the name of the current switch
            cli_switch = (arg[1:])
            # clean the list of values for the current switch
            cli_switch_values = []

        # is the argument a switch value?
        else:
            # add argument to the current list of switch's values
            cli_switch_values.append(arg)

    # append the last swicth and its values to parsed arguments list
    cli_parsed_args.append([cli_switch, cli_switch_values])
    
    # if DEBUG print out the parsed arguments
    if DEBUG:
        print("[DEBUG] Parsed aruments list: " + str(cli_parsed_args))
        for cli_switch in cli_parsed_args:
            print("[DEBUG] For an argument \"" + cli_switch[0] + "\" there are following values:")
            for value in cli_switch[1]:
                print("[DEBUG]   " + value)
        print("[DEBUG] ----")

    return( cli_parsed_args )

# validate the arguments
def validate_args( cli_parsed_args ):

    if DEBUG: print("[DEBUG] Arguments validator:")
    if DEBUG: print("[DEBUG]")
    
    # prepare the list of valid arguments
    valid_args = []
    # iterate over parsed arguments
    for switch, values in cli_parsed_args:
        if DEBUG: print("[DEBUG] Checking switch \"" + switch + "\" with values: " + str(values))
        
        # known switch that means opening a file
        if switch in SWITCHES_FILE:
            
            # if there are switch values
            if len(values)>0:

                if DEBUG: print("[DEBUG]   Switch \"" + switch + "\" is known, \"" + str(values[0]) + "\" must be an existing file")

                # if file exists
                if path.isfile(values[0]):

                    # if the file extension is supported
                    if path.splitext(values[0])[1][1:].lower() in FILE_INPUT_EXTENSIONS:

                        if DEBUG: print("[DEBUG]   File: \"" + str(values[0]) + "\" exists and is of supported extension")
                        
                        # add the switch and its values to the list of valid arguments
                        valid_args.append([switch, values])
                    
                    # if the file extension is not supported
                    else:
                        print("[Warning] File: \"" + str(values[0]) + "\" is of not supported extension. Switch -" + switch + " is ignored...")
                        if DEBUG: print("[DEBUG]   File: \"" + str(values[0]) + "\" is of not supported extension. Switch is ignored...")
                
                # if file doesn't exist
                else:
                    
                    print("[Warning] File: \"" + str(values[0]) + "\" doesn't exists. Switch -" + switch + " is ignored...")
                    if DEBUG: print("[DEBUG]   File: \"" + str(values[0]) + "\" doesn't exists. Switch is ignored...")
            
            # if there are no switch values
            else:
                
                print("[Warning] No file name is provided. Switch -" + switch + " is ignored...")
                if DEBUG: print("[DEBUG]   Switch \"" + switch + "\" is known, no values are given, the switch is ignored...")

        
        # known switch that doesn't mean opening a file
        elif switch in SWITCHES_NOFILE:
            
            if DEBUG: print("[DEBUG]   Switch \"" + switch + "\" is known, no file is meant to be open for reading")

            # add the switch and its values to the list of valid arguments
            valid_args.append([switch, values])

        # unknown switch
        else:
            
            print("[Warning] Switch -" + switch + " is unknown, ignoring...")
            if DEBUG: print("[DEBUG]   Switch \"" + switch + "\" is unknown, ignoring...")

        if DEBUG: print("[DEBUG] --")
    
    if DEBUG:
        print("[DEBUG] Validated arguments list: " + str(valid_args))
        print("[DEBUG] ----")
    
    return( valid_args )

# explode font surface by inserting given gap
def explode_font_surf(
    font_surf: pygame.Surface,
    glyph_size = GLYPH_SIZE,
    gap_size = 6,
    outline = True,
):
    if DEBUG: print("[DEBUG] Font bitmap exploder:")
    if DEBUG: print("[DEBUG]")
    
    # calculate font grid size
    font_grid_size = (int(font_surf.get_width() / glyph_size[0]) , int(font_surf.get_height() / glyph_size[1]))
    if DEBUG: print("[DEBUG]   Grid size: " + str(font_grid_size))

    # prepare target surface
    exploded_font_surf = pygame.Surface(
        (
            gap_size * (font_grid_size[0] + 1) + font_surf.get_width(),
            gap_size * (font_grid_size[1] + 1) + font_surf.get_height(),
        )
    )
    if DEBUG: print("[DEBUG]   Exploded surface size: " + str(exploded_font_surf.get_size()))
    exploded_font_surf.fill((0,0,0))

    # iterate over glyphs and copy them to target surface
    for x in range(0,font_grid_size[0]):
        for y in range(0,font_grid_size[1]):
            exploded_font_surf.blit(
                font_surf,
                ( x * (glyph_size[0] + gap_size) + gap_size, y * (glyph_size[1] + gap_size) + gap_size ),
                pygame.Rect(x * glyph_size[0] , y * glyph_size[1], glyph_size[0], glyph_size[1])

            )

    if DEBUG: print("[DEBUG] ----")
    # return exploded surface
    return exploded_font_surf

# implode font surface by removing given gap
def implode_font_surf(
    font_surf: pygame.Surface,
    glyph_size = GLYPH_SIZE,
    gap_size = 6,
    outline = True,
    double = False,
):
    if DEBUG: print("[DEBUG] Font bitmap imploder:")
    if DEBUG: print("[DEBUG]")
    
    # calculate font grid size
    if outline:
        font_grid_size = (int((font_surf.get_width() - gap_size) / (glyph_size[0] + gap_size)), int((font_surf.get_height() - gap_size) / (glyph_size[1] + gap_size)))
    else:
        font_grid_size = (int((font_surf.get_width() + 1) / (glyph_size[0] + gap_size)), int( (font_surf.get_height() + 1) / (glyph_size[1] + gap_size)))

    if DEBUG: print("[DEBUG]   Grid size: " + str(font_grid_size))

    # prepare target surface
    imploded_font_surf = pygame.Surface(
        (
            font_grid_size[0] * glyph_size[0],
            font_grid_size[1] * glyph_size[1],
        )
    )
    if DEBUG: print("[DEBUG]   Imploded surface size: " + str(imploded_font_surf.get_size()))
    imploded_font_surf.fill((0,0,0))

    # iterate over glyphs and copy them to target surface
    if outline:
        outer_gap = gap_size
    else:
        outer_gap = 0
    for x in range(0,font_grid_size[0]):
        for y in range(0,font_grid_size[1]):
            imploded_font_surf.blit(
                font_surf,
                ( x * glyph_size[0], y * glyph_size[1]),
                pygame.Rect(x * (glyph_size[0] + gap_size) + outer_gap , y * (glyph_size[1] + gap_size) + outer_gap, glyph_size[0], glyph_size[1])
            )

    # double scale, typically for analog font sources
    if double:
        if DEBUG: print("[DEBUG]   Doubling surface size...")
        imploded_font_surf = pygame.transform.scale(imploded_font_surf, (imploded_font_surf.get_width()*2,imploded_font_surf.get_height()*2))
    
    if DEBUG: print("[DEBUG] ----")
    # return exploded surface
    return imploded_font_surf

# copy glyph from source surface to target surface
def copy_glyph(
    glyph,
    source_surf :pygame.Surface,
    target_surf :pygame.Surface,
    glyph_offset = 0
):
    
    # calculate source glyph coordinates
    source_glyph_y= floor( (glyph) / FONT_GRID_SIZE[0] )
    source_glyph_x=(glyph) - source_glyph_y * FONT_GRID_SIZE[0]
    
    # calculate target glyph coordinates
    target_glyph_y= floor( (glyph+glyph_offset) / FONT_GRID_SIZE[0] )
    target_glyph_x=(glyph+glyph_offset) - target_glyph_y * FONT_GRID_SIZE[0]

    if DEBUG: print("[DEBUG]   Copying glyph " + str(glyph) + " from position (" + str (source_glyph_x) + ", " + str (source_glyph_y) + ") to position (" + str (target_glyph_x) + ", " + str (target_glyph_y) + ")")
    
    # blit a source glyph to target surface
    target_surf.blit( source_surf , ( target_glyph_x * GLYPH_SIZE[0] , target_glyph_y * GLYPH_SIZE[1] ) , pygame.Rect( source_glyph_x * GLYPH_SIZE[0], source_glyph_y * GLYPH_SIZE[1] , GLYPH_SIZE[0] , GLYPH_SIZE[1] ) )

# helper to convert a string to a list of ascii codes of the string's characters
def string_to_ord_list( string ):
    return [ ord(x) for x in list(string) ]

# prints a set of given glyphs to a target surface
def print_glyph(
    chars,
    font_surf :pygame.Surface,
    target_surf :pygame.Surface,
    print_at = (0,0),
    glyph_size = GLYPH_SIZE,
    font_grid_size = FONT_GRID_SIZE,
    color_transparent = COLOR_TRANSPARENT,
):
    if DEBUG: print("[DEBUG] Glyph Printer:")
    if DEBUG: print("[DEBUG]")
    
    font_surf.set_colorkey(color_transparent)

    for char in enumerate( chars ):
        # calculate source glyph coordinates
        source_glyph_y= floor( (char[1]) / font_grid_size[0] )
        source_glyph_x=(char[1]) - source_glyph_y * font_grid_size[0]

        # calculate target glyph coordinates
        screen_glyph_x = print_at[0] + char[0]
        screen_glyph_y = print_at[1]

        if DEBUG: print("[DEBUG]   Printing glyph code (" + str(char[1]) + ") from a font position " + str( (source_glyph_x, source_glyph_y) )  + " to demo screen position " + str( ( screen_glyph_x , screen_glyph_y ) ))

        # blit a font glyph to the target surface
        target_surf.blit( font_surf , ( screen_glyph_x * glyph_size[0] , screen_glyph_y * glyph_size[1] ) , pygame.Rect( source_glyph_x * glyph_size[0], source_glyph_y * glyph_size[1] , glyph_size[0] , glyph_size[1] )   )


# load a bitmap and convert it to a font surface
def load_bitmap(
    filename
):
    if DEBUG: print("[DEBUG] Bitmap loader:")
    if DEBUG: print("[DEBUG]")
    
    # load the bitmap file
    if DEBUG: print("[DEBUG]   Bitmap to load: " + filename)
    input_surf_file = pygame.image.load(filename).convert_alpha()
    input_surf = input_surf_file.copy()

    # check the bitmap size
    input_size = input_surf.get_size()
    if DEBUG: print("[DEBUG]   Bitmap size: " + str(input_size))

    # HDZERO HD OSD not exploded
    if input_size == (384, 1152):
        if DEBUG: print("[DEBUG]   Assuming HDZERO HD OSD font file, not exploded...")
        font_surf = input_surf

    # HDZERO HD OSD exploded
    elif input_size == (486, 1350):
        if DEBUG: print("[DEBUG]   Assuming HDZERO HD OSD font file, exploded...")
        font_surf = implode_font_surf(input_surf)

    # Analog INAV OSD exploded
    elif input_size == (209, 609):
        if DEBUG: print("[DEBUG]   Assuming Analog INAV OSD font file, exploded...")
        font_surf = implode_font_surf(input_surf, glyph_size=GLYPH_MCM_SIZE, gap_size=1, double=True )

    # Analog BTFL OSD exploded
    elif input_size == (207, 303):
        if DEBUG: print("[DEBUG]   Assuming Analog BTFL OSD font file, exploded...")
        font_surf = implode_font_surf(input_surf, glyph_size=GLYPH_MCM_SIZE, gap_size=1, outline=False,  double=True )

    # Not known font set, assuming logo
    else:
        if DEBUG: print("[DEBUG]   Not font set related bitmap size. Assuming it's a logo...")
        
        # complicated way to ensure the correct transparency even though the input surface is scalled in next steps
        if input_size == (288, 72):
            # Source for BTFL analog logo with green background
            input_surf_file.set_colorkey( (0,255,0) )
            input_surf.fill((127,127,127,0))
            input_surf.blit(input_surf_file, (0,0))
            input_surf = pygame.transform.scale(input_surf , (576,144) )
        else:
            input_surf_file.set_colorkey(COLOR_TRANSPARENT)
            input_surf.fill((127,127,127,0))
            input_surf.blit(input_surf_file, (0,0))

        # resize and slice to three logo variants
        # BTFL logo - 576x144
        # INAV logo - 240x144
        # BTFL minilogo - 120x36

        font_surf = pygame.Surface(( GLYPH_SIZE[0] * FONT_GRID_SIZE[0] , GLYPH_SIZE[1] * FONT_GRID_SIZE[1] ))
        font_surf.fill( COLOR_TRANSPARENT )

        # BTFL mini logo
        scaled_logo_surf = fit_surf_into( input_surf , (120,36) ).convert_alpha()
        font_surf.blit(scaled_logo_surf, ( 264 ,180))

        # BTFL logo
        scaled_logo_surf = fit_surf_into( input_surf , (576,144) ).convert_alpha()
        font_surf.blit(scaled_logo_surf, (0 ,360), pygame.Rect(0,0,384,36))
        font_surf.blit(scaled_logo_surf, (0 ,396), pygame.Rect(384,0,192,36))
        font_surf.blit(scaled_logo_surf, (192 ,396), pygame.Rect(0,36,192,36))
        font_surf.blit(scaled_logo_surf, (0 ,432), pygame.Rect(192,36,384,36))
        font_surf.blit(scaled_logo_surf, (0 ,468), pygame.Rect(0,72,384,36))
        font_surf.blit(scaled_logo_surf, (0 ,504), pygame.Rect(384,72,192,36))
        font_surf.blit(scaled_logo_surf, (192 ,504), pygame.Rect(0,108,192,36))
        font_surf.blit(scaled_logo_surf, (0 ,540), pygame.Rect(192,108,384,36))

        # INAV logo
        scaled_logo_surf = fit_surf_into( input_surf , (240,144) ).convert_alpha()
        font_surf.blit(scaled_logo_surf, (24 ,576) , pygame.Rect(0,0,240,36) )
        font_surf.blit(scaled_logo_surf, (264 ,576) , pygame.Rect(0,36,120,36) )
        font_surf.blit(scaled_logo_surf, (0 ,612) , pygame.Rect(120,36,120,36) )
        font_surf.blit(scaled_logo_surf, (120 ,612) , pygame.Rect(0,72,240,36) )
        font_surf.blit(scaled_logo_surf, (360 ,612) , pygame.Rect(0,108,24,36) )
        font_surf.blit(scaled_logo_surf, (0 ,648) , pygame.Rect(24,108,216,36) )

        
    
    if DEBUG: print("[DEBUG] ----")
    return(font_surf)

# helper function to scale down a surface while maintaining the aspect ratio
def fit_surf_into(
    input_surf: pygame.Surface,
    output_size = (320, 240),
):
    
    if DEBUG: print("[DEBUG] Surface resize to fit into given space:")
    if DEBUG: print("[DEBUG]")
    
    input_size = input_surf.get_size()
    input_rect = input_surf.get_rect()
    input_ar = input_size[0] / input_size[1]
    output_ar = output_size[0] / output_size[1]

    if DEBUG: print("[DEBUG]   Input size: " + str(input_size))
    if DEBUG: print("[DEBUG]   Fit to size: " + str(output_size))

    # prepare the ouput surface
    output_surf = pygame.Surface( output_size ).convert_alpha()
    output_surf.fill((0,0,0,0))
    output_rect = output_surf.get_rect()

    # is the input larger that the output?
    if input_size[0] > output_size[0] or input_size[0] > output_size[0]:
        
        # at least one input dimmension is larger that the output one
        # scale down while maintaining the AR
        if input_ar > output_ar:
            scaled_logo_surf = pygame.transform.smoothscale(input_surf , ( output_size[0] , input_size[1] * output_size[0] / input_size[0] ))
            
        else:
            scaled_logo_surf = pygame.transform.smoothscale(input_surf , ( input_size[0] * output_size[1] / input_size[1] , output_size[1] ) )

        
        # blit scaled surface to the center of the output surface
        scaled_logo_rect = scaled_logo_surf.get_rect()
        scaled_logo_rect.center = output_rect.center
        output_surf.blit(scaled_logo_surf , scaled_logo_rect )

        if DEBUG: print("[DEBUG]   Output size: " + str(scaled_logo_surf.get_size()))
    
    else:

        # the input size is smaller or equal to output size 
        # blit input surface to the center of the output surface
        input_rect.center = output_rect.center
        output_surf.blit(input_surf , input_rect )

        if DEBUG: print("[DEBUG]   Output size (not touched): " + str(input_size))
    
    if DEBUG: print("[DEBUG] ----")
    return( output_surf )

# main program execution
if __name__ == "__main__": main()
        



