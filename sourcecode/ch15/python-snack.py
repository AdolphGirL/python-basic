import pygame, sys, time, random
from pygame.locals import *

# 定義顏色變數
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)


def draw_score(play_surface, score):
    draw_score_font = pygame.font.SysFont("SIMYOU.TTF", 40)
    draw_score_surf = draw_score_font.render('%s' %(score), True, greyColour)
    draw_score_rect = draw_score_surf.get_rect()
    draw_score_rect .midtop = (20, 10)
    play_surface.blit(draw_score_surf, draw_score_rect)


# 定義gameOver函數
def game_over(play_surface):
    game_over_font = pygame.font.SysFont("SIMYOU.TTF", 80)
    game_over_surf = game_over_font.render('Game Over', True, greyColour)
    game_over_rect = game_over_surf.get_rect()
    game_over_rect.midtop = (320, 10)

    play_surface.blit(game_over_surf, game_over_rect)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()


def main():
    pygame.init()
    fps_clock = pygame.time.Clock()

    play_sur_face = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Raspberry Snake')

    # 初始化變數
    snake_position = [100, 100]
    snake_segments = [[100, 100], [80, 100], [60, 100]]
    raspberry_position = [300, 300]
    raspberry_spawned = 1
    direction = 'right'
    change_direction = direction

    while True:
        # 檢測例如按鍵等pygame事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # 判斷鍵盤事件
                if event.key == K_RIGHT or event.key == ord('d'):
                    change_direction = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    change_direction = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    change_direction = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    change_direction = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        # 判斷是否輸入了反方向
        if change_direction == 'right' and not direction == 'left':
            direction = change_direction
        if change_direction == 'left' and not direction == 'right':
            direction = change_direction
        if change_direction == 'up' and not direction == 'down':
            direction = change_direction
        if change_direction == 'down' and not direction == 'up':
            direction = change_direction

        # 根據方向移動蛇頭的坐標
        if direction == 'right':
            snake_position[0] += 20
        if direction == 'left':
            snake_position[0] -= 20
        if direction == 'up':
            snake_position[1] -= 20
        if direction == 'down':
            snake_position[1] += 20

        # 增加蛇的長度
        snake_segments.insert(0, list(snake_position))

        # 判斷是否吃掉了樹莓
        if snake_position[0] == raspberry_position[0] and snake_position[1] == raspberry_position[1]:
            raspberry_spawned = 0
        else:
            snake_segments.pop()

        # 如果吃掉樹莓，則重新生成樹莓
        if raspberry_spawned == 0:
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            raspberry_position = [int(x*20), int(y*20)]
            raspberry_spawned = 1

        # 繪製pygame顯示層
        play_sur_face.fill(blackColour)
        for position in snake_segments:
            pygame.draw.rect(play_sur_face, whiteColour, Rect(position[0], position[1], 20, 20))
            
        pygame.draw.rect(play_sur_face, redColour, Rect(raspberry_position[0], raspberry_position[1], 20, 20))
        draw_score(play_sur_face, len(snake_segments) - 3)

        # 刷新pygame顯示層
        pygame.display.flip()
        
        # 判斷是否死亡
        if snake_position[0] > 620 or snake_position[0] < 0:
            game_over(play_sur_face)
        if snake_position[1] > 460 or snake_position[1] < 0:
            game_over(play_sur_face)
            
        for snakeBody in snake_segments[1:]:
            if snake_position[0] == snakeBody[0] and snake_position[1] == snakeBody[1]:
                game_over(play_sur_face)
                
        # 控制游戲速度
        fps_clock.tick(7)


if __name__ == "__main__":
     main()
    #print(pygame.font.get_fonts())
    
