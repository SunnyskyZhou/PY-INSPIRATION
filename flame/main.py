import random, string, time

pwd = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
print(f"快输入这个密码（你有 3 秒）：{pwd}")

start = time.time()
user_input = input("> ")
if time.time() - start > 3:
    print("太慢了！密码跑路了！新密码是：", ''.join(random.choices(string.ascii_letters, k=12)))
elif user_input == pwd:
    print("正确！")
else:
    print("错了！系统自毁程序启动... 💣")