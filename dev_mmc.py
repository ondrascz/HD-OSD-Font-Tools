import pygame
from sys import exit

def main():
    pygame.init()

    # basic dimensions
    GLYPH_SIZE = (24, 36)
    GLYPH_MCM_SIZE = (12, 18)
    FONT_GRID_SIZE = (16, 32)
    COLOR_TRANSPARENT = (127,127,127)
    COLOR_BLACK = (0,0,0)
    COLOR_WHITE = (255,255,255)

    # surfaces to operate glyphs and font
    glyph_mcm_surf = pygame.Surface(GLYPH_MCM_SIZE)
    font_surf = pygame.Surface(( GLYPH_SIZE[0] * FONT_GRID_SIZE[0] , GLYPH_SIZE[1] * FONT_GRID_SIZE[1] ))
    font_surf.fill( COLOR_TRANSPARENT )
    font_glyph_pos = [0,0]
    
    # open MCM file
    mcm_file = open("resources/fonts/BTFL_analog_default.mcm", "r")

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
            # print(pixels)
        
        font_glyph_code = int(glyph_mcm_start_byte/64)
        font_glyph_pos[1] = int(font_glyph_code / FONT_GRID_SIZE[0])
        font_glyph_pos[0] = (font_glyph_code - font_glyph_pos[1] * FONT_GRID_SIZE[0])
        
        font_surf.blit( pygame.transform.scale(glyph_mcm_surf,GLYPH_SIZE), ( font_glyph_pos[0] * GLYPH_SIZE[0] , font_glyph_pos[1] * GLYPH_SIZE[1] ) )
        # print("code: " + str(font_glyph_code) + " -> col: " + str(font_glyph_pos[0]) + " -> row: " + str(font_glyph_pos[1]) )
        # print( font_glyph_pos[0] * GLYPH_SIZE[0] , font_glyph_pos[1] * GLYPH_SIZE[1] )

    
    
    screen = pygame.display.set_mode(( GLYPH_SIZE[0] * FONT_GRID_SIZE[0] , GLYPH_SIZE[1] * FONT_GRID_SIZE[1] ), pygame.SCALED)
    clock = pygame.time.Clock()
    
    screen.fill((255,0,255))
    screen.blit(font_surf, (0,0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        #game code


        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__": main()

