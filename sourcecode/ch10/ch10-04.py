import pygame
import random

pygame.init()

size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# 角色起始位置
x = int(size[0] / 2)
y = int(size[1] / 2)

ballX = random.randrange(0, size[0])
ballY = random.randrange(0, size[1])

# 設定顏色
red = pygame.color.Color('#FF8080')
blue = pygame.color.Color('#8080FF')
white = pygame.color.Color('#FFFFFF')
black = pygame.color.Color('#000000')

def checkOffScreenX(x):
    if x > size[0]:
        x = 0
    elif x < 0:
        x = size[0]
    return x

def checkOffScreenY(y):
    if y > size[1]:
        y = 0
    elif y < 0:
        y = size[1]
    return y

done = False
while not done:
    # 每次更新前會重新填充頁面
    screen.fill(black)

    # 處理輸入鍵盤，當按下w時，表示往前進，則y的距離減1
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y -= 1
    if keys[pygame.K_s]:
        y += 1
    if keys[pygame.K_a]:
        x -= 1
    if keys[pygame.K_d]:
        x += 1

    pygame.draw.circle(screen, red, [x, y], 6)
    pygame.display.flip()

    x = checkOffScreenX(x)
    y = checkOffScreenY(y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    clock.tick(100)
pygame.quit()
