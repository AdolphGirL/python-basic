import pygame

pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()

pygame.time.delay(1000)

pygame.mixer.music.load("../music/music.mp3")
pygame.mixer.music.play()

done = False
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
    clock.tick(32)
    
pygame.quit()
