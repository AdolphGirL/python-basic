import pygame

pygame.init()

size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False
while not done:
    keys = pygame.key.get_pressed()
    # w，對應英文字母的w
    if keys[pygame.K_w]:
        print('hello W')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    clock.tick(40)

pygame.quit()
