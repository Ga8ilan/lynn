import pygame
from pygame.locals import *
pygame.init()
#pygame.font.init()
#pygame.sprite.init()

background = pygame.image.load("background.jpg")
player_image = pygame.image.load("player.png").convert_alpha()

size = width, height = background.get_width(), background.get_height()
#speed = [2, 2]
black = 0, 0, 0
green = 0, 255, 0

screen = pygame.display.set_mode(size)

#screen = [1, 1, 1, 1, 1]



class player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect(center=position)


my_player = player((100, 100))
all_sprites = pygame.sprite.Group()
all_sprites.add(my_player)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()



