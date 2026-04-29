# 初始化3x3棋盘，用'-'表示空位置
board = [['-' for _ in range(3)] for _ in range(3)]


def print_board():
    """打印当前棋盘状态"""
    print("\n当前棋盘：")
    for row in board:
        print(" ".join(row))
    print()


def check_win(player):
    """检查当前玩家是否获胜（行、列、对角线）"""
    # 检查横向三连
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    # 检查纵向三连
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # 检查两条对角线
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def is_board_full():
    """检查棋盘是否下满（平局）"""
    for row in board:
        if '-' in row:
            return False
    return True


def get_valid_pos():
    """获取合法的坐标输入（0-2，且位置为空）"""
    while True:
        try:
            # 输入行和列
            row = int(input("请输入行坐标(0-2)："))
            col = int(input("请输入列坐标(0-2)："))
            # 校验坐标范围
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("错误！坐标必须是0、1、2中的数字，请重新输入！")
                continue
            # 校验位置是否为空
            if board[row][col] != '-':
                print("错误！该位置已被占用，请重新输入！")
                continue
            return row, col
        # 处理非数字输入
        except ValueError:
            print("错误！请输入整数数字！")


def main():
    """主游戏逻辑"""
    print("欢迎来到3x3井字棋游戏！")
    print("我方：A，对方：B，坐标范围：(0,0) ~ (2,2)")
    print_board()

    while True:
        # 1. 我方A落子
        print("===== 我方A回合 =====")
        a_row, a_col = get_valid_pos()
        board[a_row][a_col] = 'A'
        print_board()

        # 检查A是否获胜
        if check_win('A'):
            print("游戏结束！我方A获胜！")
            break

        # 检查平局
        if is_board_full():
            print("游戏结束！棋盘已满，平局！")
            break

        # 2. 对方B落子
        print("===== 对方B回合 =====")
        b_row, b_col = get_valid_pos()
        board[b_row][b_col] = 'B'
        print_board()

        # 检查B是否获胜
        if check_win('B'):
            print("游戏结束！对方B获胜！")
            break

        # 检查平局
        if is_board_full():
            print("游戏结束！棋盘已满，平局！")
            break


if __name__ == "__main__":
    main()