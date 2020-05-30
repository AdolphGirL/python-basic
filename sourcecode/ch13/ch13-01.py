import pygame

pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()

pygame.time.delay(1000)

sound = pygame.mixer.Sound('../music/hit.wav')

done = False
while not done:
    
    sound.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
    clock.tick(32)
    
pygame.quit()
