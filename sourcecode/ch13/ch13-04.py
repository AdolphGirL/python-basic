import pygame

pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()

pygame.time.delay(1000)

pygame.mixer.music.load('../music/music.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.delay(200)
