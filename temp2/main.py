def temperature_conversion():
    """摄氏、华氏、开尔文温度相互转换，校验开尔文温度非负"""
    print("===== 温度转换工具 =====")
    print("支持转换类型：")
    print("1. 摄氏温度(C) → 华氏温度(F)")
    print("2. 摄氏温度(C) → 开尔文温度(K)")
    print("3. 华氏温度(F) → 摄氏温度(C)")
    print("4. 华氏温度(F) → 开尔文温度(K)")
    print("5. 开尔文温度(K) → 摄氏温度(C)")
    print("6. 开尔文温度(K) → 华氏温度(F)")
    print("7. 退出程序")

    while True:
        # 获取用户选择的转换类型
        try:
            choice = int(input("\n请输入转换选项（1-7）："))
        except ValueError:
            print("错误：请输入有效的数字（1-7）！")
            continue

        # 退出程序
        if choice == 7:
            print("程序已退出！")
            break

        # 校验选项范围
        if choice not in range(1, 7):
            print("错误：请输入1-7之间的选项！")
            continue

        # 获取输入温度值（浮点数，对应double类型）
        try:
            input_temp = float(input("请输入需要转换的温度值："))
        except ValueError:
            print("错误：请输入有效的数字（整数/小数）！")
            continue

        # 定义温度转换公式 & 执行转换
        try:
            if choice == 1:
                # C → F
                result = input_temp * 9/5 + 32
                print(f"【结果】{input_temp:.2f} ℃ = {result:.2f} ℉")

            elif choice == 2:
                # C → K
                result = input_temp + 273.15
                # 校验开尔文温度不能为负
                if result < 0:
                    raise ValueError("转换后的开尔文温度不能小于0（绝对零度）！")
                print(f"【结果】{input_temp:.2f} ℃ = {result:.2f} K")

            elif choice == 3:
                # F → C
                result = (input_temp - 32) * 5/9
                print(f"【结果】{input_temp:.2f} ℉ = {result:.2f} ℃")

            elif choice == 4:
                # F → K
                result = (input_temp - 32) * 5/9 + 273.15
                # 校验开尔文温度不能为负
                if result < 0:
                    raise ValueError("转换后的开尔文温度不能小于0（绝对零度）！")
                print(f"【结果】{input_temp:.2f} ℉ = {result:.2f} K")

            elif choice == 5:
                # K → C
                # 先校验输入的开尔文温度
                if input_temp < 0:
                    raise ValueError("输入的开尔文温度不能小于0（绝对零度）！")
                result = input_temp - 273.15
                print(f"【结果】{input_temp:.2f} K = {result:.2f} ℃")

            elif choice == 6:
                # K → F
                # 先校验输入的开尔文温度
                if input_temp < 0:
                    raise ValueError("输入的开尔文温度不能小于0（绝对零度）！")
                result = (input_temp - 273.15) * 9/5 + 32
                print(f"【结果】{input_temp:.2f} K = {result:.2f} ℉")

        except ValueError as e:
            print(f"转换失败：{str(e)}")

# 启动程序
if __name__ == "__main__":
    temperature_conversion()