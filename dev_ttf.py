from math import floor
import pygame
from sys import exit

DEBUG = True

GLYPH_SIZE = (24, 36)

FONT_GRID_SIZE = (16, 32)

COLOR_TTF_GLYPH = (255,255,0)
COLOR_TTF_OUTLINE = (0,0,0)


def explode_font_surf(
    font_surf: pygame.Surface,
    glyph_size = GLYPH_SIZE,
    gap_size = 6,
    outline = True,
):
    # calculate font grid size
    font_grid_size = (int(font_surf.get_width() / glyph_size[0]) , int(font_surf.get_height() / glyph_size[1]))

    if DEBUG:
        print("Grid size: " + str(font_grid_size))

    # prepare target surface
    exploded_font_surf = pygame.Surface(
        (
            gap_size * (font_grid_size[0] + 1) + font_surf.get_width(),
            gap_size * (font_grid_size[1] + 1) + font_surf.get_height(),
        )
    )
    if DEBUG:
        print("Exploded grid size: " + str(exploded_font_surf.get_size()))
    exploded_font_surf.fill((0,0,0))

    # iterate over glyphs and copy them to target surface
    for x in range(0,font_grid_size[0]):
        for y in range(0,font_grid_size[1]):
            exploded_font_surf.blit(
                font_surf,
                ( x * (glyph_size[0] + gap_size) + gap_size, y * (glyph_size[1] + gap_size) + gap_size ),
                pygame.Rect(x * glyph_size[0] , y * glyph_size[1], glyph_size[0], glyph_size[1])

            )

    # return exploded surface
    return exploded_font_surf



def main():
    pygame.init()
    screen = pygame.display.set_mode((384,1152), pygame.SCALED)
    clock = pygame.time.Clock()

    screen.fill((127,127,127))

    bkg = pygame.image.load("resources/demo/bkg_001.jpg")
    # screen.blit(pygame.transform.smoothscale(bkg,(1280,720)),(-400,-300))
    
    ttf_super_sampling = 8
    ttf_outline_thickness = 1.5
    ttf_vertical_stretch = 1

    # osd_font = pygame.font.Font("resources/ttf/A4SPEED.ttf", 45)
    # osd_font = pygame.font.Font("resources/ttf/robotomonoextraligh.ttf", 30 * ttf_super_sampling)
    # osd_font = pygame.font.Font("resources/ttf/hemi.ttf", 21 * ttf_super_sampling)
    # osd_font = pygame.font.Font("resources/ttf/AlfaSlabOne-Regular.ttf", 21 * ttf_super_sampling)
    osd_font = pygame.font.Font("resources/ttf/Audiowide-Regular.ttf", 26  * ttf_super_sampling)
    # osd_font = pygame.font.Font("", 40)
    # osd_font = pygame.font.Font("resources/ttf/DaysOne-Regular.ttf", 23 * ttf_super_sampling)
    # osd_font = pygame.font.Font("resources/ttf/Orbitron-ExtraBold.ttf", 24 * ttf_super_sampling)
    # osd_font = pygame.font.Font("resources/ttf/RussoOne-Regular.ttf", 28 * ttf_super_sampling)
    # osd_font = pygame.font.SysFont("Consolas", 45 * ttf_super_sampling)
    # osd_font = pygame.font.Font(None, 55 * ttf_super_sampling)

    GLYPH_SUBSET_BTFL_CHARACTERS = [*range(32,36)]
    GLYPH_SUBSET_BTFL_CHARACTERS.extend( [*range(37,96)] )
    GLYPH_SUBSET_BTFL_CHARACTERS.append( 124 )

    GLYPH_SUBSET_BTFL_LETTERS = [*range(65,91)]
    
    GLYPH_SUBSET_BTFLNUMBERS = [*range(48,58)]

    GLYPH_SUBSET_BTFL_LOWLETTERS = [*range(97,123)]
    # GLYPH_SUBSET_BTFL_LOWLETTERS_OFFSET = -32

    GLYPH_SUBSET_BTFL_SPECIALS = [*range(32,36)]
    GLYPH_SUBSET_BTFL_SPECIALS.extend( [*range(37,48)] )
    GLYPH_SUBSET_BTFL_SPECIALS.extend( [*range(58,65)] )
    GLYPH_SUBSET_BTFL_SPECIALS.extend( [*range(91,96)] )
    GLYPH_SUBSET_BTFL_SPECIALS.append( 124 )    

    glyph_x=0
    glyph_y=2
    glyph_offset = 0

    ttf_chars_to_render = GLYPH_SUBSET_BTFL_CHARACTERS

    for char in ttf_chars_to_render:

        glyph_y= floor( (char+glyph_offset) / FONT_GRID_SIZE[0] )
        glyph_x=(char+glyph_offset) - glyph_y * FONT_GRID_SIZE[0]
        
        glyph = pygame.Surface((GLYPH_SIZE[0] * ttf_super_sampling, GLYPH_SIZE[1] * ttf_super_sampling  / ttf_vertical_stretch)).convert_alpha()
        glyph.fill((127,127,127,255))
        # glyph.fill((glyph_x*16,glyph_y*16+glyph_x*2,255-glyph_x*16,128))
        
        osd_character = chr(char)
        osd_glyph = osd_font.render(osd_character,True,COLOR_TTF_GLYPH)
        osd_glyph_rect = osd_glyph.get_rect()
        osd_outline = osd_font.render(osd_character,False,COLOR_TTF_OUTLINE)
        osd_outline_rect = osd_outline.get_rect()
        
        # blit not anti aliased outline to glyph surface
        for x in range(int(-ttf_outline_thickness * ttf_super_sampling) , int(ttf_outline_thickness * ttf_super_sampling) + 1):
            for y in range(int(-ttf_outline_thickness * ttf_super_sampling / ttf_vertical_stretch) ,int(ttf_outline_thickness * ttf_super_sampling / ttf_vertical_stretch) + 1):
                osd_outline_rect.centerx = GLYPH_SIZE[0]/2 * ttf_super_sampling + x
                osd_outline_rect.centery = GLYPH_SIZE[1]/2 * ttf_super_sampling / ttf_vertical_stretch + y
                glyph.blit(osd_outline, osd_outline_rect)

        # scale down the outline, blit to screen
        screen.blit(
            pygame.transform.scale(glyph,(glyph.get_size()[0]/ttf_super_sampling, glyph.get_size()[1]/ttf_super_sampling * ttf_vertical_stretch)),
            (glyph_x*GLYPH_SIZE[0],glyph_y*GLYPH_SIZE[1])
        )
        
        # blit anti aliased glyph to glyph surface
        glyph.fill((0,0,0,0))
        osd_glyph_rect.centerx = GLYPH_SIZE[0]/2 * ttf_super_sampling
        osd_glyph_rect.centery = GLYPH_SIZE[1]/2 * ttf_super_sampling / ttf_vertical_stretch
        glyph.blit(osd_glyph, osd_glyph_rect)
        
        # scale down the glyph, blit to screen
        screen.blit(
            pygame.transform.smoothscale(glyph,(glyph.get_size()[0]/ttf_super_sampling, glyph.get_size()[1]/ttf_super_sampling * ttf_vertical_stretch)),
            (glyph_x*GLYPH_SIZE[0],glyph_y*GLYPH_SIZE[1])
        )



    
    
    
    pygame.image.save(explode_font_surf(screen), "out/out.bmp")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        #game code


        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__": main()


