# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.mixer.init()
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
# rectangle dimensions
rect_width = 50
rect_height = 50
# players score
player_score = 0
random_x = random.randint(0, 1280 - rect_width)
random_y = random.randint(0, 720 - rect_height)
# rectangle existence flag and timer
rect_exist = True
last_hit_time = 0
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# create score font and show_score once (outside the loop)
font = pygame.font.SysFont("Arial", 50)
fontX = 10
fontY = 10

def show_score(x, y):
    score_surface = font.render("Score : " + str(player_score), True, "white")
    screen.blit(score_surface, (x, y))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # generate random rectangle position and fill it
    random_pos_tuple = (random_x, random_y)
    rect_size_tuple = (rect_width, rect_height)

    # prepare rectangle rect object
    rectangle_def = pygame.Rect(random_x, random_y, rect_width, rect_height)

    if rect_exist:
        rect_item = pygame.draw.rect(screen, "blue", rectangle_def)

    # draw the player circle
    pygame.draw.circle(screen, "red", player_pos, 40)

    # check for collision between player and rectangle
    if rect_exist and rectangle_def.collidepoint(player_pos.x, player_pos.y):
        player_score += 1
        rect_exist = False
        last_hit_time = pygame.time.get_ticks()
    
    # respawn after delays
    if not rect_exist:
        current_time = pygame.time.get_ticks()
        if current_time - last_hit_time > 500:  # 500 milliseconds delay
            random_x = random.randint(0, 1280 - rect_width)
            random_y = random.randint(0, 720 - rect_height)
            rect_exist = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_ESCAPE]:
        running = False
    
    keysTwo = pygame.key.get_pressed()
    if keysTwo[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keysTwo[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keysTwo[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keysTwo[pygame.K_RIGHT]:
        player_pos.x += 300 * dt


    # display score
    show_score(fontX, fontY)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    # TODO: make it so that everytime you press wasd or the arrow keys, a noise is played

pygame.quit()