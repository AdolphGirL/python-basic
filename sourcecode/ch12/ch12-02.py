import pygame

pygame.init()

windowsize = [800, 600]
screen = pygame.display.set_mode(windowsize)

black = pygame.color.Color("#000000")

image1 = pygame.image.load('../imgs/cat.jpg')
image2 = pygame.image.load('../imgs/cat1.jpg')

screen.blit(pygame.transform.scale(image1, (500, 500)), (0, 0))
screen.blit(pygame.transform.scale(image2, (500, 500)), (100, 200))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

pygame.quit()
