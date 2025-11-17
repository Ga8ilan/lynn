import sys, pygame
pygame.init()

size = width, height = 500, 500
speed = [2, 2]
black = 0, 0, 0
green = 0, 255, 0

screen = pygame.display.set_mode(size)
ball_screen = pygame.draw.rect(screen, green, (size, size))

BLUE = (0, 0, 255)
center = [50, 50]

ball = pygame.image.load("ball.webp")
new_ball = pygame.transform.scale(ball, (50, 50))
print(ball.get_width(), " ", ball.get_height())

#pygame.draw.circle(screen, BLUE, center, 10)
#ballrect = ball_screen.get_rect()
#ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(new_ball, ball_screen) #draws the ball on top of the rectangle 
    pygame.display.flip()