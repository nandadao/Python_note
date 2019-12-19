"""
    最多猜五次，猜对了提示对了，超过五次提示“笨死”
"""
import random

random_number = random.randint(1, 100)
count = 0
while count < 5:
    count += 1
    input_number = int(input("请输入："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("恭喜猜对了，总共猜了" + str(count) + "次。")
        break
else:
    print("笨死")