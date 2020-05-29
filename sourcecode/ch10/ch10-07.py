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

goalX = int(size[0] / 4 ) - 10
goalY = int(size[1] / 4 ) - 10

goalW = 20
goalH = 20

points = 0

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

def checkTouching():
    # 宣告此函示內會使用到全局變量
    global x
    global ballX
    global y
    global ballY

    if -10 < y - ballY < 10 and -10 < x - ballX < 10:
        # 畫出一個爆炸的圈圈
        pygame.draw.circle(screen, white, [x, y], 15)

        xDiff = x - ballX
        yDiff = y - ballY

        # 將兩者反向離開
        if ballX == 0:
            xDiff -= 5
        elif ballX == size[0]:
            xDiff += 5

        if ballY == 0:
            yDiff -= 5
        elif ballY == size[1]:
            yDiff += 5
    
        x += xDiff * 3
        ballX -= xDiff * 3

        y += yDiff * 3
        ballY -= yDiff * 3


done = False
start_time = pygame.time.get_ticks()
while not done:
    # 每次更新前會重新填充頁面
    screen.fill(black)

    # 球門
    pygame.draw.rect(screen, white, (goalX, goalY, goalW, goalH))

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

    x = checkOffScreenX(x)
    y = checkOffScreenY(y)
    ballX = checkOffScreenX(ballX)
    ballY = checkOffScreenY(ballY)

    # 是否碰撞
    checkTouching()

    # 畫出得分
    for point in range(points):
        pointX = 0 + point * 6
        pygame.draw.rect(screen, white, (pointX, 3, 4, 10))
    
    # 人
    pygame.draw.circle(screen, red, [x, y], 6)

    # 球
    pygame.draw.circle(screen, blue, [ballX, ballY], 6)

    # 碰撞後的球，看看有沒有在球門內，有的話將球產生一個新的位置
    if goalX <= ballX <= goalX + goalW and goalY <= ballY <= goalY + goalH:
        points += 1
        ballX = random.randrange(0, size[0])
        ballY = random.randrange(0, size[1])

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    clock.tick(72)
    start_now = pygame.time.get_ticks()

    print(start_time, start_now)
    if start_now - start_time >= 60000:
        done = True
    
pygame.quit()
