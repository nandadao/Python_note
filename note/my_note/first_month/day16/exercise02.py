"""
    定义函数：获取成绩0-100
"""

def get_score():
    while True:
        try:
            score_input = int(input("请输入成绩："))
            if 0 <= score_input <= 100:
                return score_input
            else:
                print("超过有效范围")
        except:
            print("输入的不是整数")




score = get_score()
print(score)
