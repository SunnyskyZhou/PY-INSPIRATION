import tkinter as tk
from tkinter import ttk

# 创建主窗口
root = tk.Tk()
root.title("🎨 简易涂鸦画板")
root.geometry("800x600")

# 创建画布
canvas = tk.Canvas(root, bg="white", width=700, height=500)
canvas.pack(pady=20)

# 画画功能：鼠标拖动绘制
def paint(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    canvas.create_oval(x1, y1, x2, y2, fill=color_var.get(), width=5)

# 颜色选择
color_var = tk.StringVar(value="black")
colors = ["black", "red", "blue", "green", "pink", "purple"]
ttk.Combobox(root, textvariable=color_var, values=colors).pack()

# 绑定鼠标事件
canvas.bind("<B1-Motion>", paint)

# 清空画布
def clear():
    canvas.delete("all")
ttk.Button(root, text="清空画布", command=clear).pack(pady=5)

root.mainloop()