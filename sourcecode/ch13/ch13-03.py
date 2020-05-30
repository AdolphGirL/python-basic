import pygame

pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()

pygame.time.delay(1000)

hit = pygame.mixer.Sound('../music/hit.wav')
crash = pygame.mixer.Sound('../music/crash.wav')


done = False
while not done:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        hit.play()
    
    if keys[pygame.K_s]:
        crash.play()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    clock.tick(32)
    
pygame.quit()
