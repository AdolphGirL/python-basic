import pygame
import random

pygame.init()

size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

black = pygame.color.Color("#000000")
white = pygame.color.Color("#FFFFFF")
btnColor = pygame.color.Color("#A45C8F")

btnWidth = 50
btnLength = 20
btnX = int((size[0] - btnWidth) / 2)
btnY = int((size[1] - btnLength) / 2)

toggled = False
pos = (0, 0)

points = 0

done = False
while not done:
    if toggled:
        screen.fill(black)
    else:
        screen.fill(white)

    pygame.draw.rect(screen, btnColor, (btnX, btnY, btnWidth, btnLength))

    if btnX <= pos[0] <= btnX + btnWidth and btnY <= pos[1] <= btnY + btnLength:
        toggled = not toggled
        pos = (0, 0)
        if toggled:
            screen.fill(black)
            pygame.draw.circle(screen, white, (btnX, btnY), 60)
        else:
            screen.fill(white)
            pygame.draw.circle(screen, black, (btnX, btnY), 60)
        

    btnX += random.randint(-1 - points, 1 + points)
    btnY += random.randint(-1 - points, 1 + points)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            points += 1
            
        if event.type == pygame.QUIT:
            done = True
            
    pygame.display.flip()
    clock.tick(10)

print(points)
pygame.quit()
