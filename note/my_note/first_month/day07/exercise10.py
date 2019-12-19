""
"""
# 练习：在终端中录入一个成绩，打印等级。
#  优秀  良好  及格   不及格   成绩有误
score = float(input("请输入成绩："))

    if score < 0 or score > 100:
    print("成绩有误")
elif score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
"""


def get_score_level(score):
    if score < 0 or score > 100:
        return "成绩有误"
    elif score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"




# ----------------------

score = float(input("请输入成绩："))
re = get_score_level(score)
print(re)
