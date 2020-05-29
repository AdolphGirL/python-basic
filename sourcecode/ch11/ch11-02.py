import pygame

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
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            
        if event.type == pygame.QUIT:
            done = True
            
    pygame.display.flip()
    clock.tick(100)
    
pygame.quit()
