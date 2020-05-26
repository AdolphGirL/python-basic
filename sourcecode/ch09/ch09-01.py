import pygame as pg

# 初始化
pg.init()

# 設定視窗
width, height = 640, 480

# 或者
# windowSize = [640, 480]

# 依設定顯示視窗
screen = pg.display.set_mode((width, height))

# 設定視窗標題
pg.display.set_caption("first pygame")

# 建立一個顏色
color = pg.color.Color('#FFFFFF')

running = True
while running:
    pg.draw.circle(screen, color, [200, 150], 50)
    pg.display.flip()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()
