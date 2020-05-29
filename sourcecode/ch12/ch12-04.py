import pygame
import random
pygame.init()


def move(image1, image2):
    global count

    if count % 2 == 0:
        image = image1
    else:
        image = image2

    if count >= 10:
        count = 1
    else:
        count += 1
    return image

windowsize = [400, 300]
screen = pygame.display.set_mode(windowsize)
clock = pygame.time.Clock()

white = pygame.color.Color("#FFFFFF")

stand_img = pygame.image.load('../imgs/sprite1_standing.png')
walk1 = pygame.image.load('../imgs/sprite1_walking1.png')
walk2 = pygame.image.load('../imgs/sprite1_walking2.png')

count = 1
x = 0
y = 0

locked = False

done = False
while not done:
    screen.fill(white)
    keys = pygame.key.get_pressed()

    if not locked:
        if keys[pygame.K_s]:
            image = move(walk1, walk2)
            y += 1
        elif keys[pygame.K_SPACE]:
            locked = True
        else:
            image = stand_img
    else:
        image = stand_img
        x = random.randrange(0, windowsize[0])
        y = random.randrange(0, windowsize[1])
        locked = False

    screen.blit(image, (x, y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
    clock.tick(32)
    
pygame.quit()
