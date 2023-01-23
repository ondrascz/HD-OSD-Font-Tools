import pygame
from sys import exit

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()

    screen.fill((190,50,190))
    
    # test of surface loding from a file
    # surface_from_file = pygame.image.load("dev resources/image_open_tests/sharp_transparency_small_portion.png")
    # surface_from_file = pygame.image.load("dev resources/image_open_tests/no_transparency_plus_grey.png")
    surface_from_file = pygame.image.load("dev resources/image_open_tests/outxx.bmp")
    # surface_from_file = pygame.image.load("dev resources/image_open_tests/gradual_transparency.png")
    # surface_from_file = pygame.image.load("dev resources/image_open_tests/sharp_transparency.png")

    print(surface_from_file)
    print(surface_from_file.get_size())

    print("color key: " + str(surface_from_file.get_colorkey()))
    print("flags: " + str(surface_from_file.get_flags()))
    

    screen.blit(surface_from_file,(16,16))
    
    surface_from_file.set_colorkey((229,255,0))
    # surface_from_file.convert_alpha()
    # surface_from_file.set_alpha(127)

    print("color key: " + str(surface_from_file.get_colorkey()))
    print("flags: " + str(surface_from_file.get_flags()))
    print(surface_from_file.get_flags() >> 16)

    screen.blit(surface_from_file,(16,320))

    pygame.image.save(surface_from_file, "dev resources/image_open_tests/out.jpg")



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        #game code


        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__": main()

