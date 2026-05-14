#pip install colorama
import time
from colorama import init, Fore

init(autoreset=True)
# 彩虹颜色列表
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
text = "Python太有趣啦！！！"

print("\n 彩虹文字如下：")
for i, char in enumerate(text):
    # 循环切换颜色
    color = colors[i % len(colors)]
    print(color + char, end="", flush=True)
    time.sleep(0.1)  # 打字机延迟