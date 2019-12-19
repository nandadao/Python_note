# 猜数字游戏
# 程序产生1--100之间的随机数，让用户不断猜猜，直到猜对为止。
# 提示：大了  小了  恭喜猜对了，总共猜了?次。
# 准备随机数工具
import random

random_number = random.randint(1, 100)  # 产生一个随机数
count = 0
while True:
    count += 1
    input_number = int(input("请输入："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("恭喜猜对了，总共猜了" + str(count) + "次。")
        break
