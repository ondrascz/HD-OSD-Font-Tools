from math import floor
import sys
from os import environ, path
import pygame

from fbldr_settings import *

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
