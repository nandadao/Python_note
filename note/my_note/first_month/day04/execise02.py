"""
    随机加法考试提
        产生两个随机数
        在终端中获取结果，提示5 + 4 = ?
        如果回答正确加十分
        否则扣五分
        总共3道题，最后显示总分
"""

import random

score = 0
for i in range(3):
    random_number1 = random.randint(1, 10)
    random_number2 = random.randint(1, 10)
    # print(random_number1,random_number2)
    your = float(input("计算" + str(random_number1) + "+" + str(random_number2) + "="))
    if your == random_number1 + random_number2:
        score += 10
    else:
        score -= 5
print(score)
