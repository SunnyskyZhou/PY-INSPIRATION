# 5. 动态文字进度条
import time  # 延时库

print("加载中...")
# 循环打印进度条
for i in range(1, 21):
    # end="" 不换行
    print(f"[{'■' * i}{' ' * (20-i)}] {i*5}%", end="\r")
    time.sleep(0.5)  # 暂停0.5秒
print("\n加载完成！")