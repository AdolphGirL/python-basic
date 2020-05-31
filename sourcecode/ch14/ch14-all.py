import pygame
import random

pygame.init()


# 判斷行走時，需要產生的圖像
def moveAnimation(image1, image2, count):
    if 10 < count % 20 <= 20:
        return image2
    else:
        return image1

# 判斷是否可以穿越牆(往上)
def upClear(x, y):
    canMove = True

    if verticalDoorLeft <= x <= verticalDoorRight and y - 1 < topWall:
        canMove = True
    elif y - 1 < topWall:
        canMove = False
    elif (x < leftWall or x > rightWall) and y - 1 < middleDoorsTop:
        canMove = False

    if canMove:
        return 1
    else:
        return 0

def randomPosition():
    x = random.randrange(32, windowSize[0] - 52)
    y = random.randrange(32, windowSize[1] - 52)
    return x, y
    

windowSize = [640, 384]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

# 分數的字體大小
pointFont = pygame.font.SysFont("Monospace", 15)

pOneX = int(windowSize[0] / 4)
pOneY = int(windowSize[1] / 2)

pTwoX = int(windowSize[0] / 4) * 3
pTwoY = int(windowSize[1] / 2)

coinPos = randomPosition()

pOnePoints = 0
pTwoPoints = 0

pOneCount = 0
pTwoCount = 0

pOneMoving = False
pTwoMoving = False

# 牆的相關變數
leftWall = 28
topWall = 16
rightWall = windowSize[0] - 60
bottomWall = 312

middleDoorsTop = 144
middleDoorsBottom = 182
verticalDoorLeft = 284
verticalDoorRight = verticalDoorLeft + 40

# Game loop
done = False
while not done:

    pygame.display.flip()
     
    # exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(60)
pygame.quit()
    
