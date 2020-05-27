import pygame

pygame.init()

windowsize = [400, 300]
screen = pygame.display.set_mode(windowsize)
color = pygame.color.Color(255, 153, 153)
# print(color)


row = 0
done = False
while not done:
    increment = int(255 / 100)
    # print(increment)
    while row <= windowsize[0]:
        pygame.draw.rect(screen, color, [0, row, windowsize[0], row + increment])
        pygame.display.flip()

        if color[2] + increment < 255:
            color = pygame.color.Color(255, 153, color[2] + increment)

        row += increment

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()

