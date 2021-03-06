import pygame
import random
# 背景图片名称
image_name = "winter.jpg"
# 初始化
pygame.init()
screen_size = (1000, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("下雪啦!!!!")
# 加载位图
background = pygame.image.load(image_name)

# 定义一个雪花列表
snow = []
# 初始化雪花
for i in range(300):
    x = random.randrange(0, screen_size[0])
    y = random.randrange(0, screen_size[1])
    speedx = random.randint(-1, 2)
    speedy = random.randint(3, 8)
    snow.append([x, y, speedx, speedy])

done = False
while not done:
    # 消息事件循环, 判断退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # 绘制位图
    screen.blit(background, (0, 0))

    # 雪花列表循环
    for i in range(len(snow)):
        # 绘制雪花, 颜色, 位置, 大小
        pygame.draw.circle(screen, (255, 255, 255), snow[i][:2], snow[i][3])

        # 移动雪花位置(下一次循环起效)
        if snow[i][1] > screen_size[1]:
            snow[i][1] = random.randrange(-50, -10)
            snow[i][0] = random.randrange(0, screen_size[0])
    pygame.display.flip()


pygame.quit()


