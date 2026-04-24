import tkinter as tk
from tkinter import messagebox
import re


# 核心功能：验证输入并切换背景颜色
def change_color():
    # 获取输入框的十六进制码
    hex_code = entry_hex.get().strip()

    # 正则表达式：严格匹配6位十六进制字符（0-9, a-f, A-F）
    pattern = r'^[0-9a-fA-F]{6}$'
    if re.match(pattern, hex_code):
        # 验证通过：拼接#号，设置窗口背景色
        root.config(bg=f'#{hex_code}')
    else:
        # 验证失败：弹出错误提示
        messagebox.showerror("输入错误", "请输入**6位十六进制颜色码**！\n（合法字符：0-9、a-f、A-F）")
        # 清空输入框，方便重新输入
        entry_hex.delete(0, tk.END)


#1:1正方形窗口
root = tk.Tk()
root.title("色卡参考")
# 设置窗口为400x400正方形，固定大小（禁止缩放，保持1:1比例）
window_size = 400
root.geometry(f"{window_size}x{window_size}")
root.resizable(False, False)
# 初始背景色-白色
root.config(bg="#FFFFFF")

# 输入验证规则：仅允许输入6个字符
def limit_input(char):
    return len(char) <= 6

# 注册验证函数
validate_input = root.register(limit_input)
# 创建输入框：居中、宽度适配、限制输入长度
entry_hex = tk.Entry(
    root,
    font=("微软雅黑", 16),  # 字体大小
    justify="center",  # 文字居中
    validate="key",  # 实时验证输入
    validatecommand=(validate_input, "%P")  # 限制输入长度
)
# 将输入框放置在窗口正中央
entry_hex.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=200, height=40)

#绑定事件
# 1. 点击回车触发颜色切换
entry_hex.bind("<Return>", lambda event: change_color())
# 2. 可选：添加按钮，点击也能触发
btn_confirm = tk.Button(
    root,
    text="确认切换颜色",
    font=("微软雅黑", 12),
    command=change_color
)
btn_confirm.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

# 启动窗口主循环
root.mainloop()