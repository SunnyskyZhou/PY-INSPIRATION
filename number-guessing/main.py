import random
# 生成1-10的随机数
secret_num = random.randint(1, 10)
print("我想到了一个1-10的数字，来猜猜看！")

# 循环猜数字，直到猜对
while True:
    guess = int(input("请输入你的猜测："))
    if guess > secret_num:
        print("太大啦！再小一点~")
    elif guess < secret_num:
        print("太小啦！再大一点~")
    else:
        print("恭喜你猜对了！🎉")
        break  