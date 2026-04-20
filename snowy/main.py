import pygame
import random

# 初始化pygame
pygame.init()

# 背景比例 4:3，即宽度800，高度600（标准4:3）
WIDTH, HEIGHT = 800, 600
# 背景颜色为#00008B
BG_COLOR = (0, 0, 139)
# 雪花颜色 白色
SNOW_COLOR = (255, 255, 255)
# 雪花字符：0和1
SNOW_CHARS = ['0', '1']

# 创建窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("01数字雪花飘落")

# 字体设置（系统默认字体，大小随机）
font = pygame.font.SysFont(None, 30)


# 雪花类
class Snowflake:
    def __init__(self):
        # 随机初始位置
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-50, -10)
        # 随机下落速度
        self.speed = random.uniform(1, 4)
        # 随机雪花字符（0或1）
        self.char = random.choice(SNOW_CHARS)
        # 随机大小（让雪花更自然）
        self.size = random.randint(20, 36)
        self.font = pygame.font.SysFont(None, self.size)

    def fall(self):
        # 向下飘落
        self.y += self.speed
        # 飘出屏幕底部后重置到顶部
        if self.y > HEIGHT:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, WIDTH)
            self.speed = random.uniform(1, 4)

    def draw(self):
        # 渲染雪花字符
        text_surface = self.font.render(self.char, True, SNOW_COLOR)
        screen.blit(text_surface, (self.x, self.y))


# 创建大量雪花
snowflakes = [Snowflake() for _ in range(150)]

# 主循环
clock = pygame.time.Clock()
running = True

while running:
    # 控制帧率
    clock.tick(60)

    # 退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景色
    screen.fill(BG_COLOR)

    # 更新并绘制所有雪花
    for snow in snowflakes:
        snow.fall()
        snow.draw()

    # 刷新屏幕
    pygame.display.flip()

# 退出程序
pygame.quit()