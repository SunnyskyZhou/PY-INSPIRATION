def celsius_to_fahrenheit(c):
    """摄氏温度转华氏温度"""
    return c * 9 / 5 + 32


def celsius_to_kelvin(c):
    """摄氏温度转开尔文温度"""
    return c + 273.15


def fahrenheit_to_celsius(f):
    """华氏温度转摄氏温度"""
    return (f - 32) * 5 / 9


def fahrenheit_to_kelvin(f):
    """华氏温度转开尔文温度"""
    c = fahrenheit_to_celsius(f)
    return celsius_to_kelvin(c)


def kelvin_to_celsius(k):
    """开尔文温度转摄氏温度"""
    if k < 0:
        raise ValueError("开尔文温度不能小于0")
    return k - 273.15


def kelvin_to_fahrenheit(k):
    """开尔文温度转华氏温度"""
    c = kelvin_to_celsius(k)
    return celsius_to_fahrenheit(c)


def temperature_converter():
    """主转换函数"""
    print("温度转换器")
    print("支持的温度单位：")
    print("C - 摄氏温度")
    print("F - 华氏温度")
    print("K - 开尔文温度")
    print("-" * 30)

    # 获取输入
    while True:
        try:
            original_unit = input("请输入原始温度单位(C/F/K): ").upper()
            if original_unit not in ['C', 'F', 'K']:
                print("错误：请输入C、F或K")
                continue

            original_value = float(input("请输入温度值: "))
            target_unit = input("请输入目标温度单位(C/F/K): ").upper()
            if target_unit not in ['C', 'F', 'K']:
                print("错误：请输入C、F或K")
                continue

            if original_unit == target_unit:
                print(f"{original_value}{original_unit} 就是 {original_value}{target_unit}")
                continue

            # 进行转换
            result = None

            if original_unit == 'C' and target_unit == 'F':
                result = celsius_to_fahrenheit(original_value)
            elif original_unit == 'C' and target_unit == 'K':
                result = celsius_to_kelvin(original_value)
            elif original_unit == 'F' and target_unit == 'C':
                result = fahrenheit_to_celsius(original_value)
            elif original_unit == 'F' and target_unit == 'K':
                result = fahrenheit_to_kelvin(original_value)
            elif original_unit == 'K' and target_unit == 'C':
                result = kelvin_to_celsius(original_value)
            elif original_unit == 'K' and target_unit == 'F':
                result = kelvin_to_fahrenheit(original_value)

            if result is not None:
                # 检查开尔文温度是否为负数
                if target_unit == 'K' and result < 0:
                    print("错误：开尔文温度不能为负数！")
                else:
                    print(f"{original_value:.2f}{original_unit} = {result:.2f}{target_unit}")

        except ValueError as e:
            if "开尔文温度不能小于0" in str(e):
                print("错误：开尔文温度不能小于0！")
            else:
                print("错误：请输入有效的数字！")
        except Exception as e:
            print(f"发生错误: {e}")

        # 询问是否继续
        choice = input("\n是否继续转换？(y/n): ").lower()
        if choice != 'y':
            print("感谢使用温度转换器！")
            break
        print("-" * 30)


# 增强版：提供更多功能和选择
def enhanced_temperature_converter():
    """增强版温度转换器"""
    print("=" * 40)
    print("增强版温度转换器")
    print("=" * 40)

    conversion_map = {
        'CF': (celsius_to_fahrenheit, "摄氏 → 华氏"),
        'CK': (celsius_to_kelvin, "摄氏 → 开尔文"),
        'FC': (fahrenheit_to_celsius, "华氏 → 摄氏"),
        'FK': (fahrenheit_to_kelvin, "华氏 → 开尔文"),
        'KC': (kelvin_to_celsius, "开尔文 → 摄氏"),
        'KF': (kelvin_to_fahrenheit, "开尔文 → 华氏")
    }

    while True:
        print("\n请选择转换类型:")
        for i, (key, (_, desc)) in enumerate(conversion_map.items(), 1):
            print(f"{i}. {desc} ({key[0]}→{key[1]})")
        print("7. 退出程序")

        try:
            choice = int(input("请输入选项(1-7): "))

            if choice == 7:
                print("感谢使用温度转换器！")
                break

            if choice < 1 or choice > 6:
                print("错误：请输入1-7之间的数字")
                continue

            # 获取对应的转换键
            conv_key = list(conversion_map.keys())[choice - 1]
            func, desc = conversion_map[conv_key]
            from_unit, to_unit = conv_key[0], conv_key[1]

            # 获取温度值
            value = float(input(f"请输入{from_unit}温度值: "))

            # 执行转换
            result = func(value)

            # 检查开尔文温度是否为负数
            if to_unit == 'K' and result < 0:
                print("错误：转换结果开尔文温度为负数，这是不可能的！")
            else:
                print(f"{value:.2f}°{from_unit} = {result:.2f}°{to_unit}")

                # 额外信息
                if to_unit == 'K' and result >= 0:
                    if result < 2.7:
                        print("提示：这个温度比宇宙微波背景辐射(2.7K)还要低！")
                    elif result < 77:
                        print("提示：这是液氮的温度范围")
                    elif result < 273.15:
                        print("提示：温度低于冰点")
                    elif result == 273.15:
                        print("提示：这是水的冰点")
                    elif result == 373.15:
                        print("提示：这是水的沸点")

        except ValueError as e:
            if "开尔文温度不能小于0" in str(e):
                print("错误：开尔文温度不能小于0！")
            else:
                print("错误：请输入有效的数字！")
        except Exception as e:
            print(f"发生错误: {e}")


def batch_conversion():
    """批量转换功能"""
    print("\n批量温度转换")
    print("支持一次性转换多个温度")

    temps = input("请输入多个温度值，用空格分隔: ").split()
    from_unit = input("请输入原始单位(C/F/K): ").upper()
    to_unit = input("请输入目标单位(C/F/K): ").upper()

    if from_unit not in ['C', 'F', 'K'] or to_unit not in ['C', 'F', 'K']:
        print("错误：单位必须是C、F或K")
        return

    results = []
    for temp_str in temps:
        try:
            temp = float(temp_str)
            # 根据单位选择转换函数
            if from_unit == 'C' and to_unit == 'F':
                result = celsius_to_fahrenheit(temp)
            elif from_unit == 'C' and to_unit == 'K':
                result = celsius_to_kelvin(temp)
            elif from_unit == 'F' and to_unit == 'C':
                result = fahrenheit_to_celsius(temp)
            elif from_unit == 'F' and to_unit == 'K':
                result = fahrenheit_to_kelvin(temp)
            elif from_unit == 'K' and to_unit == 'C':
                result = kelvin_to_celsius(temp)
            elif from_unit == 'K' and to_unit == 'F':
                result = kelvin_to_fahrenheit(temp)
            else:
                result = temp

            # 检查开尔文温度
            if to_unit == 'K' and result < 0:
                results.append(f"{temp}{from_unit} -> 错误: K<0")
            else:
                results.append(f"{temp}{from_unit} -> {result:.2f}{to_unit}")
        except:
            results.append(f"{temp_str} -> 输入错误")

    print("\n转换结果:")
    for r in results:
        print(r)


if __name__ == "__main__":
    print("请选择转换器模式:")
    print("1. 基础交互式转换器")
    print("2. 增强版转换器（更多功能）")
    print("3. 批量转换")

    mode = input("请输入模式(1/2/3): ")

    if mode == '1':
        temperature_converter()
    elif mode == '2':
        enhanced_temperature_converter()
    elif mode == '3':
        batch_conversion()
    else:
        print("无效选择，使用基础模式")
        temperature_converter()