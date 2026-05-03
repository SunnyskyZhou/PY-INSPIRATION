import random


def print_board(board):
    """按照要求的格式打印棋盘"""
    print("\n当前棋盘：")
    print("   (0) (1) (2)")

    # 从第2行开始打印（因为(0,0)是左下角）
    for i in range(2, -1, -1):  # 2,1,0
        row_str = f"({i}) "
        for j in range(3):
            row_str += f" {board[i][j]} "
            if j < 2:
                row_str += "|"
        print(row_str)
        if i > 0:  # 在第0行上面不打印分隔符
            print("    " + "___|___|___")


def check_winner(board, player):
    """检查指定玩家是否获胜"""
    # 检查行
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

    # 检查列
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True

    # 检查对角线
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    # 检查反对角线
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def is_board_full(board):
    """检查棋盘是否已满"""
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def get_empty_positions(board):
    """获取所有空位置"""
    empty_positions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_positions.append((i, j))
    return empty_positions


def get_player_move(board):
    """获取玩家A的移动位置"""
    while True:
        try:
            move = input("玩家A，请输入您要下棋的位置 (行 列)，例如：0 0：")
            coords = move.strip().split()

            if len(coords) != 2:
                print("请输入两个数字，用空格分隔！")
                continue

            row, col = int(coords[0]), int(coords[1])

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("坐标必须在0到2之间！")
                continue

            if board[row][col] != ' ':
                print("这个位置已经有棋子了，请选择其他位置！")
                continue

            return row, col

        except ValueError:
            print("请输入有效的数字！")
        except Exception as e:
            print(f"输入错误: {e}")


def computer_move(board):
    """电脑B随机选择一个空位置下棋"""
    empty_positions = get_empty_positions(board)
    if empty_positions:
        return random.choice(empty_positions)
    return None


def play_game():
    """主游戏函数"""
    print("=" * 40)
    print("      井字棋游戏 (玩家A vs 电脑B)")
    print("=" * 40)
    print("游戏说明：")
    print("1. 您是玩家A，电脑是玩家B")
    print("2. 坐标范围从(0,0)到(2,2)")
    print("3. (0,0)是左下角，(2,2)是右上角")
    print("4. 三个相同的棋子连成一条线获胜")
    print("5. 横、竖、斜线均可")
    print("=" * 40)
    print("棋盘坐标示意图：")
    print("    (0,2)  (1,2)  (2,2)")
    print("    (0,1)  (1,1)  (2,1)")
    print("    (0,0)  (1,0)  (2,0)")
    print("=" * 40)

    # 初始化棋盘
    board = [[' ' for _ in range(3)] for _ in range(3)]
    game_over = False

    while not game_over:
        # 玩家A的回合
        print_board(board)
        print("\n玩家A的回合 (您)")

        # 获取玩家A移动
        row_a, col_a = get_player_move(board)
        board[row_a][col_a] = 'A'

        # 检查玩家A是否获胜
        if check_winner(board, 'A'):
            print_board(board)
            print(f"\n{'=' * 40}")
            print(f"  恭喜！玩家A获胜！")
            print(f"{'=' * 40}")
            game_over = True
            break

        # 检查是否平局
        if is_board_full(board):
            print_board(board)
            print(f"\n{'=' * 40}")
            print(f"  游戏结束，平局！")
            print(f"{'=' * 40}")
            game_over = True
            break

        # 电脑B的回合
        print_board(board)
        print("\n电脑B的回合 (AI)")

        # 获取电脑B移动
        move = computer_move(board)
        if move:
            row_b, col_b = move
            board[row_b][col_b] = 'B'
            print(f"电脑B在位置 ({row_b}, {col_b}) 下棋")
        else:
            # 没有空位置了
            print_board(board)
            print(f"\n{'=' * 40}")
            print(f"  游戏结束，平局！")
            print(f"{'=' * 40}")
            game_over = True
            break

        # 检查电脑B是否获胜
        if check_winner(board, 'B'):
            print_board(board)
            print(f"\n{'=' * 40}")
            print(f"  电脑B获胜！")
            print(f"{'=' * 40}")
            game_over = True
            break

        # 检查是否平局
        if is_board_full(board):
            print_board(board)
            print(f"\n{'=' * 40}")
            print(f"  游戏结束，平局！")
            print(f"{'=' * 40}")
            game_over = True
            break

    # 询问是否再来一局
    while True:
        choice = input("\n是否再来一局？(y/n): ").lower()
        if choice in ['y', 'yes', '是']:
            print("\n" + "=" * 40)
            play_game()
            return
        elif choice in ['n', 'no', '否']:
            print("\n感谢游玩！再见！")
            return
        else:
            print("请输入y/n或是/否")


# 启动游戏
if __name__ == "__main__":
    play_game()