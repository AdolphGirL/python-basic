import pygame

pygame.init()

size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            
        if event.type == pygame.QUIT:
            done = True

    clock.tick(100)
    
pygame.quit()
