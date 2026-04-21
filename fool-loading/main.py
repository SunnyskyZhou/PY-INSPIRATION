import tkinter as tk
import time

class AprilFoolsLoader:
    def __init__(self, root):
        self.root = root
        self.root.title("愚人节加载条")

        # 设置4:3背景，计算一个合适的尺寸
        self.canvas_width = 800
        self.canvas_height = 600  # 800:600 = 4:3
        self.bg_color = "#2F4F2F"  # 背景颜色
        self.bar_color = "white"   # 加载条颜色
        self.bar_unit = "▰"        # 加载条单位
        self.bar_count = 20        # 加载条最大显示的单位数

        # 动画阶段定义: (总时间(秒), 起始百分比, 结束百分比)
        self.animation_phases = [
            (40, 0, 100),      # 阶段1: 40秒 0% -> 100%
            (5, 100, 100),     # 阶段2: 5秒 暂停
            (10, 100, 999),    # 阶段3: 10秒 100% -> 999%
            (20, 999, -100)    # 阶段4: 20秒 999% -> -100%
        ]
        self.current_phase = 0
        self.start_time = time.time()
        self.phase_start_time = self.start_time
        self.current_percent = 0.0
        self.text_visible = False  # 控制顶部文字的显示

        # 创建画布
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg=self.bg_color, highlightthickness=0)
        self.canvas.pack()

        # 绘制加载条背景框
        self.bar_x = self.canvas_width * 0.1
        self.bar_y = self.canvas_height * 0.5
        self.bar_width = self.canvas_width * 0.8
        self.bar_height = 40
        self.bar_bg = self.canvas.create_rectangle(
            self.bar_x, self.bar_y,
            self.bar_x + self.bar_width, self.bar_y + self.bar_height,
            outline="gray", width=2
        )

        # 加载条文本（百分比显示）
        self.percent_text_id = self.canvas.create_text(
            self.canvas_width / 2,
            self.bar_y + self.bar_height + 30,
            text="0%",
            fill="white",
            font=("Arial", 20, "bold")
        )

        # 加载条主体（用文本来模拟方块条）
        self.bar_text_id = self.canvas.create_text(
            self.bar_x + 5,
            self.bar_y + self.bar_height / 2,
            text="",
            fill=self.bar_color,
            font=("Courier", 24),
            anchor="w"
        )

        # 顶部文字（愚人节祝福），初始隐藏
        self.top_text_id = self.canvas.create_text(
            self.canvas_width / 2,
            self.bar_y - 60,
            text="HAPPY  4.1  APRIL  FOOLS  DAY",
            fill="white",
            font=("Arial", 28, "bold"),
            state="hidden"  # 初始状态为隐藏
        )

        # 启动动画
        self.update_animation()

    def calculate_current_percent(self):
        """根据当前时间和动画阶段计算进度百分比"""
        now = time.time()
        phase_elapsed = now - self.phase_start_time
        phase_duration, start_pct, end_pct = self.animation_phases[self.current_phase]

        if phase_duration > 0:
            # 计算当前阶段的进度（0.0 到 1.0之间）
            phase_progress = min(phase_elapsed / phase_duration, 1.0)
            # 线性插值计算当前百分比
            self.current_percent = start_pct + (end_pct - start_pct) * phase_progress
        else:
            # 如果阶段持续时间为0，直接跳到结束值
            self.current_percent = end_pct

        # 检查当前阶段是否完成
        if phase_elapsed >= phase_duration:
            self.phase_start_time = now
            self.current_phase += 1
            # 如果所有阶段完成，则停留在最后阶段
            if self.current_phase >= len(self.animation_phases):
                self.current_phase = len(self.animation_phases) - 1
                # 最后一个阶段完成后，确保顶部文字显示
                self.text_visible = True

        # 在最后一个阶段（到-100%的阶段）开始时，显示顶部文字
        if self.current_phase == 3 and phase_elapsed > 0.1:
            self.text_visible = True

    def update_bar_display(self):
        """根据当前百分比更新加载条的显示"""
        # 将百分比映射到方块数量
        max_blocks = self.bar_count
        # 计算应显示的方块数量，确保不会超过最大值
        raw_blocks = (abs(self.current_percent) / 100.0) * max_blocks
        display_blocks = int(min(raw_blocks, max_blocks))

        # 生成加载条文本
        bar_string = self.bar_unit * display_blocks
        # 更新画布上的文本
        self.canvas.itemconfig(self.bar_text_id, text=bar_string)
        # 更新百分比文本，格式化为整数显示
        percent_display = f"{self.current_percent:.1f}%" if self.current_percent % 1 != 0 else f"{int(self.current_percent)}%"
        self.canvas.itemconfig(self.percent_text_id, text=percent_display)

        # 控制顶部文字的显示/隐藏
        if self.text_visible:
            self.canvas.itemconfig(self.top_text_id, state="normal")
        else:
            self.canvas.itemconfig(self.top_text_id, state="hidden")

    def update_animation(self):
        """主动画更新循环"""
        self.calculate_current_percent()
        self.update_bar_display()

        # 每隔50毫秒调用一次更新，形成动画
        self.root.after(50, self.update_animation)

def main():
    root = tk.Tk()
    app = AprilFoolsLoader(root)
    root.mainloop()

if __name__ == "__main__":
    main()
