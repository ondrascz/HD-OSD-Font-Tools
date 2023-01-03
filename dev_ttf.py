import pygame
import sys
from sys import exit

def main():
    pygame.init()
    screen = pygame.display.set_mode((384,1152), pygame.SCALED)
    clock = pygame.time.Clock()

    screen.fill((127,127,127))
    bkg = pygame.image.load("resources/demo/bkg_001.jpg")
    
    screen.blit(pygame.transform.smoothscale(bkg,(1280,720)),(-400,-200))
    
    # osd_font = pygame.font.Font("resources/ttf/A4SPEED.ttf", 25)
    # osd_font = pygame.font.Font("resources/ttf/robotomonoextraligh.ttf", 26)
    osd_font = pygame.font.Font("resources/ttf/hemi.ttf", 27)
    # osd_font = pygame.font.Font("resources/ttf/AlfaSlabOne-Regular.ttf", 21)
    # osd_font = pygame.font.Font("resources/ttf/Audiowide-Regular.ttf", 24)
    # osd_font = pygame.font.Font("", 40)
    # osd_font = pygame.font.Font("resources/ttf/DaysOne-Regular.ttf", 22)
    # osd_font = pygame.font.Font("resources/ttf/Orbitron-ExtraBold.ttf", 21)
    # osd_font = pygame.font.Font("resources/ttf/RussoOne-Regular.ttf", 28)
    # osd_font = pygame.font.SysFont("Consolas", 30, True, True)
    # osd_font = pygame.font.Font(None, 25)

    glyph_x=0
    glyph_y=0
    
    for char in range(32,126):
        
    
        glyph = pygame.Surface((24,36)).convert_alpha()
        glyph.fill((0,0,0,0))
        # glyph.fill((glyph_x*16,glyph_y*16+glyph_x*2,255-glyph_x*16))
        
        osd_str = chr(char)
        osd_text = osd_font.render(osd_str,True,(180,220,255))
        osd_text_rect = osd_text.get_rect()
        osd_outline = osd_font.render(osd_str,False,(0,0,0))
        osd_outline_rect = osd_outline.get_rect()
        
        osd_text_rect.centerx = 12
        osd_text_rect.centery = 18
        
        # blit not anti aliased outline
        for x in range(-1,3):
            for y in range(-1,3):
                osd_outline_rect.centerx = 12 + x
                osd_outline_rect.centery = 18 + y
                glyph.blit(osd_outline, osd_outline_rect)

        # blit anti aliased character
        glyph.blit(osd_text, osd_text_rect)

        # blit of complete glyph to screen
        screen.blit(glyph,(glyph_x*24,glyph_y*36))

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


