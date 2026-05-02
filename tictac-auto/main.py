import random

# 初始化3x3棋盘，坐标(x,y)：x=0(左)~2(右)，y=0(下)~2(上)
board = [[None for _ in range(3)] for _ in range(3)]


def print_board():
    """打印棋盘，竖向|，横向___"""
    # 棋盘从y=2（最上方）打印到y=0（最下方）
    for y in range(2, -1, -1):
        row = []
        for x in range(3):
            # 空位置显示空格，有棋子显示A/B
            row.append(board[x][y] if board[x][y] is not None else " ")
        # 拼接行：| 内容 | 内容 | 内容 |
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
        # 横向分隔符
        print("___ ___ ___")


def get_empty_positions():
    """获取所有空位置，用于AI随机落子"""
    empty = []
    for x in range(3):
        for y in range(3):
            if board[x][y] is None:
                empty.append((x, y))
    return empty


def check_win(player):
    """判断指定玩家是否获胜"""
    # 检查横向（同一y，x不同）
    for y in range(3):
        if board[0][y] == board[1][y] == board[2][y] == player:
            return True
    # 检查纵向（同一x，y不同）
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2] == player:
            return True
    # 检查对角线
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def main():
    print("===== 3x3井字棋游戏 =====")
    print("坐标规则：左下角(0,0) → 右上角(2,2)")
    print("你是玩家A，电脑是玩家B")
    print("========================\n")

    while True:
        # 1. 玩家A落子
        empty_pos = get_empty_positions()
        if not empty_pos:
            print("棋盘已满，平局！")
            break

        while True:
            try:
                # 输入坐标
                x = int(input("请输入你的x坐标(0-2)："))
                y = int(input("请输入你的y坐标(0-2)："))
                # 判断坐标是否合法且为空
                if 0 <= x <= 2 and 0 <= y <= 2 and board[x][y] is None:
                    board[x][y] = "A"
                    break
                else:
                    print("坐标不合法或已被占用，请重新输入！")
            except ValueError:
                print("请输入数字！")

        # 打印当前棋盘
        print("\n===== 当前棋盘 =====")
        print_board()

        # 判断A是否获胜
        if check_win("A"):
            print("\n恭喜！玩家A获胜！游戏结束")
            break

        # 2. 电脑B随机落子
        empty_pos = get_empty_positions()
        if not empty_pos:
            print("棋盘已满，平局！")
            break

        bx, by = random.choice(empty_pos)
        board[bx][by] = "B"
        print(f"\n电脑B落子在坐标({bx}, {by})")

        # 打印当前棋盘
        print("===== 当前棋盘 =====")
        print_board()

        # 判断B是否获胜
        if check_win("B"):
            print("\n很遗憾！玩家B获胜！游戏结束")
            break


if __name__ == "__main__":
    main()