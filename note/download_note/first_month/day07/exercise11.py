# 练习：day03/exercise05
# def get_score_level(score):
#     if score < 0 or score > 100:
#         return "成绩有误"
#     elif score >= 90:
#         return "优秀"
#     elif score >= 80:
#         return "良好"
#     elif score >= 60:
#         return "及格"
#     else:
#         return "不及格"

def get_score_level(score):
    if score < 0 or score > 100:
        return "成绩有误"
    if score >= 90:
        return "优秀"
    if score >= 80:
        return "良好"
    if score >= 60:
        return "及格"
    return "不及格"


print(get_score_level(90))
