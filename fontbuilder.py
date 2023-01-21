import sys
from os import environ, path
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

# general settings
DEBUG = False

# HD OSD fonts settings
GLYPH_SIZE = (24, 36)
GLYPH_MCM_SIZE = (12, 18)
FONT_GRID_SIZE = (16, 32)

COLOR_TRANSPARENT = (127,127,127)
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_TTF_GLYPH = (255,255,255)
COLOR_TTF_OUTLINE = (0,0,0)

SWITCHES_FILE = ("", "base")
SWITCHES_NOFILE = ("o", "nopreview", "demo")

# main program
def main():
    pygame.init()
    
    # parse CLI arguments
    cli_parsed_args = parse_cli_args()

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
                    
                    if DEBUG: print("[DEBUG]   File: \"" + str(values[0]) + "\" exists")

                    # process the file
                
                # if file doesn't exist
                else:
                    
                    print("[Warning] File: \"" + str(values[0]) + "\" doesn't exists. Switch -" + switch + " is ignored...")
                    if DEBUG: print("[DEBUG]   File: \"" + str(values[0]) + "\" doesn't exists. Switch is ignored...")
            
            # if there are no switch values
            else:
                
                if DEBUG: print("[DEBUG]   Switch \"" + switch + "\" is known, no values are given, the switch is ignored...")

        
        # known switch that doesn't mean opening a file
        elif switch in SWITCHES_NOFILE:
            
            if DEBUG: print("[DEBUG]   Switch \"" + switch + "\" is known, no file is meant to be open for reading")

        # unknown switch
        else:
            
            print("[Warning] Switch -" + switch + " is unknown, ignoring...")
            if DEBUG: print("[DEBUG]   Switch \"" + switch + "\" is unknown, ignoring...")

    
    
    # guess what type of file it is
    
    # open file and render to source surface
    
    # prepare target surface
    
    # init a pygame screen
    screen = pygame.display.set_mode((GLYPH_SIZE[0] * FONT_GRID_SIZE[0], GLYPH_SIZE[1] * FONT_GRID_SIZE[1]), pygame.SCALED)
    pygame.display.set_caption("Font Builder Preview (click to close)")
    clock = pygame.time.Clock()

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
def load_image():
    # image can be a font bitmap of different dimmension
    # image can be a generoc bitmap to be used as a logo
    # [ ] format guesser
    pass

# load and process MCM font file
def load_mcm():
    # input is a MCM file
    pass

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

    return( cli_parsed_args )

# main program execution
if __name__ == "__main__": main()
        



