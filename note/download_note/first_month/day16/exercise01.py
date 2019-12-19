"""
    定义函数，获取成绩。
            0--100
"""

def get_score():
    while True:
        try:
            score = int(input("请输入成绩："))
            if 0 <= score <= 100:
                return score
            else:
                print("超过有效范围")
        except:
            print("输入的不是整数")

score = get_score()
print(score)

# 练习:修改信息管理系统代码，不要发生异常。
#     异常处理原则：就近处理，保障程序可以按照既定流程执行。
