from math import floor
import sys
from os import environ, path

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from fbldr_settings import *
from fbldr_functions import *

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


# main program execution
if __name__ == "__main__": main()
        



