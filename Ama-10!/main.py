print("我是Ama-10，跟我说说话吧！(输入'拜拜'以结束对话)")

while True:
    user_input = input("你: ")

    if user_input == "拜拜":
        print("Ama-10: 再见！记得想我哦！👋")
        break
    elif "名字" in user_input:
        print("Ama-10: 我叫#??#^5#2#2@呀！")
    else:
        print(f"Ama-10: 你刚才说的是 '{user_input}' 吗？")