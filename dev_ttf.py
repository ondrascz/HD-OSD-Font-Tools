import pygame
import sys
from sys import exit

def main():
    pygame.init()
    screen = pygame.display.set_mode((384,400),pygame.SCALED)
    clock = pygame.time.Clock()

    screen.fill((127,127,127))

    bkg = pygame.image.load("resources/demo/bkg_001.jpg")
    screen.blit(pygame.transform.smoothscale(bkg,(1280,720)),(-400,-300))
    
    # osd_font = pygame.font.Font("resources/ttf/A4SPEED.ttf", 47)
    # osd_font = pygame.font.Font("resources/ttf/robotomonoextraligh.ttf", 52)
    # osd_font = pygame.font.Font("resources/ttf/hemi.ttf", 54)
    # osd_font = pygame.font.Font("resources/ttf/AlfaSlabOne-Regular.ttf", 42)
    # osd_font = pygame.font.Font("resources/ttf/Audiowide-Regular.ttf", 46)
    # osd_font = pygame.font.Font("", 40)
    osd_font = pygame.font.Font("resources/ttf/DaysOne-Regular.ttf", 44)
    # osd_font = pygame.font.Font("resources/ttf/Orbitron-ExtraBold.ttf", 42)
    # osd_font = pygame.font.Font("resources/ttf/RussoOne-Regular.ttf", 56)
    # osd_font = pygame.font.SysFont("Consolas", 60)
    # osd_font = pygame.font.Font(None, 70)

    glyph_x=0
    glyph_y=0
    
    for char in range(32,126):
        
    
        glyph = pygame.Surface((48,72)).convert_alpha()
        glyph.fill((0,0,0,0))
        # glyph.fill((glyph_x*16,glyph_y*16+glyph_x*2,255-glyph_x*16,128))
        
        osd_str = chr(char)
        osd_text = osd_font.render(osd_str,True,(200,200,255))
        osd_text_rect = osd_text.get_rect()
        osd_outline = osd_font.render(osd_str,False,(64,64,128))
        osd_outline_rect = osd_outline.get_rect()
        
        # blit not anti aliased outline to glyph
        for x in range(-3,4):
            for y in range(-3,4):
                osd_outline_rect.centerx = 24 + x
                osd_outline_rect.centery = 36 + y
                glyph.blit(osd_outline, osd_outline_rect)

        # scale down the outline, blit to screen
        screen.blit(
            pygame.transform.scale(glyph,(glyph.get_size()[0]/2, glyph.get_size()[1]/2)),
            (glyph_x*24,glyph_y*36)
        )
        
        # blit anti aliased text to glyph
        glyph.fill((0,0,0,0))
        osd_text_rect.centerx = 24
        osd_text_rect.centery = 36
        glyph.blit(osd_text, osd_text_rect)
        
        # scale down the text, blit to screen
        screen.blit(
            pygame.transform.smoothscale(glyph,(glyph.get_size()[0]/2, glyph.get_size()[1]/2)),
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


