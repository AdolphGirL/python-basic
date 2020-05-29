import pygame

pygame.init()

windowsize = [800, 600]
screen = pygame.display.set_mode(windowsize)

black = pygame.color.Color("#000000")

image = pygame.image.load('../imgs/cat.jpg')
screen.blit(pygame.transform.scale(image, (500, 500)), (0, 0))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

pygame.quit()
