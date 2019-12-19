"""
    随机加法考试题
        产生两个随机数
        在终端中获取结果，提示：5 + 4 = ?
        如果回答正确加10分，否则扣5分。
        总共3道题，最后显示总分。
"""
import random

score = 0
for item in range(3):
    random_number01 = random.randint(1, 10)
    random_number02 = random.randint(1, 10)
    message = str(random_number01) + " + " + str(random_number02) + " = ?"
    input_result = float(input(message))
    if input_result == random_number01 + random_number02:
        score += 10
    else:
        score -= 5

print(score)
