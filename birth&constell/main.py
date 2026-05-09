# 6. 星座小查询
month = int(input("输入你的出生月份："))
day = int(input("输入你的出生日期："))

# 判断星座
if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    star = "白羊座"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    star = "金牛座"
elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
    star = "双子座"
else:
    star = "其他星座（可以自己补充哦）"

print(f"你的星座是：{star}")