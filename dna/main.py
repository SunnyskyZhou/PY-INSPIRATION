import pygame
import math
import sys

WINDOW_WIDTH = 800  # 4:3比例 宽
WINDOW_HEIGHT = 600  # 4:3比例 高
BG_COLOR = (0, 0, 139)  # 背景色 #00008B（深蓝）
TEXT_COLOR = (255, 255, 255)  # 数字颜色 白色
ROTATE_CYCLE = 5000  # 旋转周期 5000ms = 5秒

# 初始化Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("DNA双螺旋旋转动画")
clock = pygame.time.Clock()

# 初始化字体（用于渲染数字0/1）
font = pygame.font.SysFont(None, 24)

# 双螺旋参数配置
SPIRAL_STEPS = 30  # 螺旋段数（密度）
SPIRAL_RADIUS = 100  # 螺旋半径
SPIRAL_HEIGHT = 450  # 螺旋总高度


def draw_dna_helix(angle_offset):
    """绘制旋转的DNA双螺旋：0=主体，1=连接，整体旋转"""
    center_x = WINDOW_WIDTH // 2
    center_y = WINDOW_HEIGHT // 2

    for i in range(SPIRAL_STEPS):
        # 计算螺旋垂直位置
        y = center_y - SPIRAL_HEIGHT // 2 + (i * SPIRAL_HEIGHT / SPIRAL_STEPS)
        # 基础角度 + 旋转偏移量（实现动画）
        angle = math.radians(i * 20 + angle_offset)

        # 左链坐标（数字0，DNA主体）
        left_x = center_x - SPIRAL_RADIUS * math.cos(angle)
        left_y = y
        # 右链坐标（数字0，DNA主体）
        right_x = center_x + SPIRAL_RADIUS * math.cos(angle)
        right_y = y

        # 渲染并绘制 主体数字0
        text0 = font.render("0", True, TEXT_COLOR)
        screen.blit(text0, (left_x - text0.get_width() // 2, left_y - text0.get_height() // 2))
        screen.blit(text0, (right_x - text0.get_width() // 2, right_y - text0.get_height() // 2))

        # 渲染并绘制 连接数字1（左右链中间）
        mid_x = (left_x + right_x) / 2
        mid_y = y
        text1 = font.render("1", True, TEXT_COLOR)
        screen.blit(text1, (mid_x - text1.get_width() // 2, mid_y - text1.get_height() // 2))


# 主循环
while True:
    # 退出事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 填充背景色
    screen.fill(BG_COLOR)

    # 计算旋转角度：5秒转360度，无限循环
    current_time = pygame.time.get_ticks()
    rotate_angle = (current_time % ROTATE_CYCLE) / ROTATE_CYCLE * 360

    # 绘制DNA双螺旋
    draw_dna_helix(rotate_angle)

    # 更新屏幕 + 控制帧率
    pygame.display.flip()
    clock.tick(60)