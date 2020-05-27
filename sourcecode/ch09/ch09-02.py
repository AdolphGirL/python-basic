import pygame

pygame.init()

windowsize = [400, 300]
screen = pygame.display.set_mode(windowsize)
color = pygame.color.Color('#0A32F4')

done = False
while not done:
    # 10, 20-- x,y位置；30、40--矩形的寬和長
    pygame.draw.rect(screen, color, [10, 20, 30, 40])
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
