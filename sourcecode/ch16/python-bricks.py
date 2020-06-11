# -*- coding: utf-8 -*-

import random
import pygame


class Box:
    def __init__(self, py_game, box_canvas, name, rect, box_color):
        self.py_game = py_game
        self.box_canvas = box_canvas
        self.name = name
        self.rect = rect
        self.box_color = box_color
        self.visible = True

    def update(self):
        if self.visible:
            self.py_game.draw.rect(self.box_canvas, self.box_color, self.rect)


class Circle:
    def __init__(self, py_game, circle_canvas, name, pos, radius, circle_color):
        self.py_game = py_game
        self.circle_canvas = circle_canvas
        self.name = name
        self.pos = pos
        self.radius = radius
        self.circle_color = circle_color
        self.visible = True

    def update(self):
        if self.visible:
            self.py_game.draw.circle(self.circle_canvas, self.circle_color, self.pos, self.radius)


def reset_game():
    global game_mode, brick_num, bricks_list, dx, dy

    # 磚塊
    for bricks in bricks_list:
        # 亂數磚塊顏色
        r = random.randint(100, 200)
        g = random.randint(100, 200)
        b = random.randint(100, 200)
        bricks.color = [r, g, b]
        bricks.visible = True

    # 等待開球
    game_mode = 0
    # 磚塊起始數量
    brick_num = 99
    dx = 8
    dy = -8


# 球是否碰撞到磚塊
def is_collision(x, y, box_rect):
    if box_rect[0] <= x <= box_rect[0] + box_rect[2] and box_rect[1] <= y <= box_rect[1] + box_rect[3]:
        return True

    return False


def show_font(text, x, y):
    global canvas

    text = font.render(text, 1, (255, 0, 0))
    canvas.blit(text, (x, y))


canvas_width = 800
canvas_height = 600
block = (0, 0, 0)

# 磚塊數量串列
bricks_list = []

# 移動速度
dx = 8
dy = -8

# 遊戲狀態
game_mode = 0

pygame.init()
pygame.display.set_caption("打磚塊遊戲")

canvas = pygame.display.set_mode((canvas_width, canvas_height))
clock = pygame.time.Clock()
font = pygame.font.SysFont('simhei', 18)

paddle_x = 0
paddle_y = (canvas_height - 48)
paddle = Box(pygame, canvas, "paddle", [paddle_x, paddle_y, 100, 24], (255, 255, 255))

ball_x = paddle_x
ball_y = paddle_y
ball = Circle(pygame, canvas, "ball", [ball_x, ball_x], 8, (255, 255, 255))

# 建立磚塊
brick_num = 0

# 第一塊起始位置(磚塊寬58, 高16)
brick_x = 70
brick_y = 60
brick_w = 0
brick_h = 0
for i in range(0, 99):
    if i % 11 == 0:
        brick_w = 0
        brick_h = brick_h + 18

    bricks_list.append(Box(pygame, canvas, "brick_" + str(i), [brick_w + brick_x, brick_h + brick_y, 58, 16], [255, 255, 255]))
    brick_w = brick_w + 60

reset_game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # 判斷滑鼠位置，移動底板
        if event.type == pygame.MOUSEMOTION:
            paddle_x = pygame.mouse.get_pos()[0] - 50

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_mode == 0:
                game_mode = 1

    # 清除畫面
    canvas.fill(block)

    for bricks in bricks_list:
        if is_collision(ball.pos[0], ball.pos[1], bricks.rect):
            if bricks.visible:
                brick_num = brick_num - 1

                if brick_num <= 0:
                    reset_game()
                    break

                # 球反彈
                dy = -dy

            bricks.visible = False

        # 更新磚塊
        bricks.update()

    show_font("磚塊數量:" + str(brick_num), 8, 20)

    paddle.rect[0] = paddle_x
    paddle.update()

    # 球碰板子
    if is_collision(ball.pos[0], ball.pos[1], paddle.rect):
        dy = -dy

    if game_mode == 0:
        ball.pos[0] = ball_x = paddle.rect[0] + ((paddle.rect[2] - ball.radius) >> 1)
        ball.pos[1] = ball_y = paddle.rect[1] - ball.radius
    elif game_mode == 1:
        ball_x += dx
        ball_y += dy

        # 判斷死亡
        if ball_y + dy > canvas_height - ball.radius:
            game_mode = 0

        # 右牆或左牆碰撞
        if ball_x + dx > canvas_width - ball.radius or ball_x + dx < ball.radius:
            dx = -dx

        # 下牆或上牆碰撞
        if ball_y + dy > canvas_height - ball.radius or ball_y + dy < ball.radius:
            dy = -dy

        ball.pos[0] = ball_x
        ball.pos[1] = ball_y

    ball.update()

    show_font("FPS:" + str(clock.get_fps()), 8, 2)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
