import pygame
import sys
from sys import exit

def main():
    pygame.init()
    screen = pygame.display.set_mode((384,400), pygame.SCALED)
    clock = pygame.time.Clock()

    screen.fill((127,127,127))

    bkg = pygame.image.load("resources/demo/bkg_001.jpg")
    screen.blit(pygame.transform.smoothscale(bkg,(1280,720)),(-400,-300))
    
    ttf_super_sampling = 6
    ttf_outline_thickness = 1.2
    ttf_vertical_stretch = 0.8

    # osd_font = pygame.font.Font("resources/ttf/A4SPEED.ttf", 45)
    osd_font = pygame.font.Font("resources/ttf/robotomonoextraligh.ttf", 45 * ttf_super_sampling)
    # osd_font = pygame.font.Font("resources/ttf/hemi.ttf", 27 * ttf_super_sampling)
    # osd_font = pygame.font.Font("resources/ttf/AlfaSlabOne-Regular.ttf", 21 * ttf_super_sampling)
    # osd_font = pygame.font.Font("resources/ttf/Audiowide-Regular.ttf", 26  * ttf_super_sampling)
    # osd_font = pygame.font.Font("", 40)
    # osd_font = pygame.font.Font("resources/ttf/DaysOne-Regular.ttf", 23 * ttf_super_sampling)
    # osd_font = pygame.font.Font("resources/ttf/Orbitron-ExtraBold.ttf", 24 * ttf_super_sampling)
    # osd_font = pygame.font.Font("resources/ttf/RussoOne-Regular.ttf", 28 * ttf_super_sampling)
    # osd_font = pygame.font.SysFont("Consolas", 30 * ttf_super_sampling)
    # osd_font = pygame.font.Font(None, 55 * ttf_super_sampling)

    glyph_x=0
    glyph_y=0
    
    for char in range(32,126):
        
    
        glyph = pygame.Surface((24 * ttf_super_sampling, 36 * ttf_super_sampling  / ttf_vertical_stretch)).convert_alpha()
        glyph.fill((0,0,0,0))
        # glyph.fill((glyph_x*16,glyph_y*16+glyph_x*2,255-glyph_x*16,128))
        
        osd_str = chr(char)
        osd_text = osd_font.render(osd_str,True,(255,255,255))
        osd_text_rect = osd_text.get_rect()
        osd_outline = osd_font.render(osd_str,False,(0,0,0))
        osd_outline_rect = osd_outline.get_rect()
        
        # blit not anti aliased outline to glyph
        for x in range(int(-ttf_outline_thickness * ttf_super_sampling) , int(ttf_outline_thickness * ttf_super_sampling) + 1):
            for y in range(int(-ttf_outline_thickness * ttf_super_sampling / ttf_vertical_stretch) ,int(ttf_outline_thickness * ttf_super_sampling / ttf_vertical_stretch) + 1):
                osd_outline_rect.centerx = 12 * ttf_super_sampling + x
                osd_outline_rect.centery = 18 * ttf_super_sampling + y
                glyph.blit(osd_outline, osd_outline_rect)

        # scale down the outline, blit to screen
        screen.blit(
            pygame.transform.scale(glyph,(glyph.get_size()[0]/ttf_super_sampling, glyph.get_size()[1]/ttf_super_sampling * ttf_vertical_stretch)),
            (glyph_x*24,glyph_y*36)
        )
        
        # blit anti aliased text to glyph
        glyph.fill((0,0,0,0))
        osd_text_rect.centerx = 12 * ttf_super_sampling
        osd_text_rect.centery = 18 * ttf_super_sampling
        glyph.blit(osd_text, osd_text_rect)
        
        # scale down the text, blit to screen
        screen.blit(
            pygame.transform.smoothscale(glyph,(glyph.get_size()[0]/ttf_super_sampling, glyph.get_size()[1]/ttf_super_sampling * ttf_vertical_stretch)),
            (glyph_x*24,glyph_y*36)
        )



        glyph_x += 1
        if glyph_x > 15:
            glyph_x = 0
            glyph_y += 1

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        #game code


        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__": main()


