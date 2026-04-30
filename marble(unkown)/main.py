import curses
from curses import KEY_LEFT, KEY_RIGHT

# ===================== 游戏常量配置（严格按你的要求） =====================
TOTAL_ROWS = 12  # 窗口总行数
TOTAL_COLS = 7  # 窗口总列数
BRICK_ROWS = 7  # 砖块行数
BRICK_COLS = 7  # 砖块列数
PADDLE_ROW = 10  # 挡板固定在第10行
PADDLE_LEN = 4  # 挡板长度：----
SCORE_PER_BRICK = 10  # 每个砖块10分

# 游戏字符
BALL_CHAR = "●"
BRICK_CHAR = "▬"
PADDLE_CHAR = "-"


def reset_game(stdscr):
    """重置游戏状态（用于重新开始）"""
    # 初始化砖块：7行7列，True=存在，False=消除
    bricks = [[True for _ in range(BRICK_COLS)] for _ in range(BRICK_ROWS)]
    # 弹球初始位置（第8行，第3列）+ 移动速度
    ball_row, ball_col = 8, 3
    ball_dx, ball_dy = 1, 1  # dx=行方向，dy=列方向
    # 挡板初始位置（第10行，列2开始，长度4）
    paddle_col = 2
    # 得分
    score = 0
    # 剩余砖块数量
    remaining_bricks = BRICK_ROWS * BRICK_COLS
    return bricks, ball_row, ball_col, ball_dx, ball_dy, paddle_col, score, remaining_bricks


def main(stdscr):
    # ===================== curses 初始化 =====================
    curses.curs_set(0)  # 隐藏光标
    stdscr.nodelay(True)  # 非阻塞按键监听
    stdscr.timeout(50)  # 游戏刷新速度（数值越小越快）

    # 颜色配置：黑字白底（边框/砖块/球）、红字白底（挡板）
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    BLACK_ON_WHITE = curses.color_pair(1)
    RED_ON_WHITE = curses.color_pair(2)

    # 初始化第一局游戏
    bricks, ball_row, ball_col, ball_dx, ball_dy, paddle_col, score, remaining_bricks = reset_game(stdscr)

    # ===================== 主游戏循环 =====================
    while True:
        stdscr.clear()  # 清屏
        key = stdscr.getch()  # 获取按键

        # ===================== 按键控制 =====================
        if key == ord('0'):  # 按0直接退出
            break
        if key == KEY_LEFT and paddle_col > 0:  # 左移挡板（不越界）
            paddle_col -= 1
        if key == KEY_RIGHT and paddle_col < TOTAL_COLS - PADDLE_LEN:  # 右移挡板
            paddle_col += 1

        # ===================== 绘制边框（黑色，背景白色） =====================
        stdscr.border('|', '|', '-', '-', '+', '+', '+', '+', BLACK_ON_WHITE)

        # ===================== 绘制砖块（黑色▬，7×7） =====================
        for r in range(BRICK_ROWS):
            for c in range(BRICK_COLS):
                if bricks[r][c]:
                    stdscr.addch(r, c, BRICK_CHAR, BLACK_ON_WHITE)

        # ===================== 绘制弹球（黑色●） =====================
        stdscr.addch(ball_row, ball_col, BALL_CHAR, BLACK_ON_WHITE)

        # ===================== 绘制挡板（红色----，固定第10行） =====================
        for i in range(PADDLE_LEN):
            stdscr.addch(PADDLE_ROW, paddle_col + i, PADDLE_CHAR, RED_ON_WHITE)

        # ===================== 显示得分 =====================
        stdscr.addstr(11, 0, f"得分:{score}", BLACK_ON_WHITE)

        # ===================== 弹球移动逻辑 =====================
        ball_row += ball_dx
        ball_col += ball_dy

        # ===================== 碰撞检测 =====================
        # 1. 左右边框碰撞 → 列方向反弹
        if ball_col <= 0 or ball_col >= TOTAL_COLS - 1:
            ball_dy *= -1

        # 2. 上边框碰撞 → 行方向反弹
        if ball_row <= 0:
            ball_dx *= -1

        # 3. 挡板碰撞 → 行方向反弹
        if (ball_row == PADDLE_ROW and
                paddle_col <= ball_col <= paddle_col + PADDLE_LEN - 1):
            ball_dx *= -1

        # 4. 砖块碰撞 → 消除砖块+得分+反弹
        if 0 <= ball_row < BRICK_ROWS and 0 <= ball_col < BRICK_COLS:
            if bricks[ball_row][ball_col]:
                bricks[ball_row][ball_col] = False
                remaining_bricks -= 1
                score += SCORE_PER_BRICK
                ball_dx *= -1  # 反弹

        # ===================== 游戏结束判断 =====================
        # 1. 弹球落到第12行（最底部）→ 游戏失败
        if ball_row >= TOTAL_ROWS - 1:
            stdscr.nodelay(False)
            stdscr.clear()
            stdscr.addstr(4, 0, "游戏结束!", BLACK_ON_WHITE)
            stdscr.addstr(5, 0, f"最终得分:{score}", BLACK_ON_WHITE)
            stdscr.addstr(6, 0, "按任意键退出", BLACK_ON_WHITE)
            stdscr.getch()
            break

        # 2. 所有砖块消除 → 通关
        if remaining_bricks == 0:
            stdscr.nodelay(False)
            stdscr.clear()
            stdscr.addstr(3, 0, "恭喜通关!", BLACK_ON_WHITE)
            stdscr.addstr(4, 0, f"得分:{score}", BLACK_ON_WHITE)
            stdscr.addstr(5, 0, "是否再来一局?", BLACK_ON_WHITE)
            stdscr.addstr(6, 0, "0退出 1继续", BLACK_ON_WHITE)

            # 等待玩家选择0/1
            while True:
                choice = stdscr.getch()
                if choice == ord('0'):
                    return  # 退出游戏
                if choice == ord('1'):
                    # 重置游戏，重新开始
                    bricks, ball_row, ball_col, ball_dx, ball_dy, paddle_col, score, remaining_bricks = reset_game(
                        stdscr)
                    stdscr.nodelay(True)
                    break


# 运行游戏（curses自动处理终端初始化/清理）
if __name__ == "__main__":
    curses.wrapper(main)