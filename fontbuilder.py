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

# colors
COLOR_TRANSPARENT = (127,127,127)
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_TTF_GLYPH = (255,255,255)
COLOR_TTF_OUTLINE = (0,0,0)

# arguments parsing
SWITCHES_FILE = ("", "base")
SWITCHES_NOFILE = ("o", "nopreview", "demo")

# supported files extensions
FILE_INPUT_EXTENSIONS = ("ttf", "mcm", "bmp", "png")

# main program
def main():

    # parse CLI arguments
    cli_parsed_args = parse_cli_args()

    # validate the parsed arguments
    valid_args = validate_args( cli_parsed_args )
    
    # process the valid input files and create the input font surfaces
    input_font_surfaces = []
    for switch, values in valid_args:
        # the input file is .MCM font
        if switch in SWITCHES_FILE and path.splitext(values[0])[1][1:].lower() == "mcm":
            input_font_surfaces.append( load_mcm( values[0] ) )

    

    # process the file
    # guess what type of file it is
    # open file and render to source surface
    
    
    
    # prepare target surface
    
    # init a pygame screen
    pygame.init()
    pygame.display.set_icon( pygame.image.load("resources/icon/icon.png") )
    screen = pygame.display.set_mode((GLYPH_SIZE[0] * FONT_GRID_SIZE[0], GLYPH_SIZE[1] * FONT_GRID_SIZE[1]), pygame.SCALED)
    screen.fill( COLOR_TRANSPARENT )
    pygame.display.set_caption("Font Builder Preview (click to close)")
    clock = pygame.time.Clock()

    
    screen.blit(input_font_surfaces[0],(0,0))
    
    # pygame loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYUP:
                pygame.quit()
                sys.exit()


        pygame.display.update()
        clock.tick(60)

# the load functions return a pygame Surface
# load and process a bitmap image
def load_bitmap():
    # image can be a font bitmap of different dimmension
    # image can be a generoc bitmap to be used as a logo
    # [ ] format guesser
    pass

# load and process MCM font file
def load_mcm( filename ):
    
    # surfaces to operate glyphs and font
    glyph_mcm_surf = pygame.Surface(GLYPH_MCM_SIZE)
    font_surf = pygame.Surface(( GLYPH_SIZE[0] * FONT_GRID_SIZE[0] , GLYPH_SIZE[1] * FONT_GRID_SIZE[1] ))
    font_surf.fill( COLOR_TRANSPARENT )
    font_glyph_pos = [0,0]
    
    # open MCM file
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
                        glyph_mcm_surf.set_at(glyph_px_pos, COLOR_BLACK)
                        pixels += ".."
                    elif glyph_mcm_byte[i:i+2] == "10":
                        # black pixel
                        glyph_mcm_surf.set_at(glyph_px_pos, COLOR_WHITE)
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

    return( font_surf )

# load and process TTF font file
def load_ttf():
    # input is a TTF file
    pass

# parse CLI arguments
def parse_cli_args():
    
    # arguments parsing variables
    cli_parsed_args = []
    cli_switch_values = []
    cli_switch = ""

    if DEBUG: print("[DEBUG] Argv: " + str(sys.argv[1:]))
    
    # iterate over a list of arguments except the first (program file name)
    for arg in sys.argv[1:]:
        # is the argument a switch?
        if arg[0:1] == "-":
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

# guess file type from a filename
def guess_file_type():
    pass

# main program execution
if __name__ == "__main__": main()
        



