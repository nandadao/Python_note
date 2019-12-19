# 3.在终端中录入月份，显示季度。

# month = int(input("请输入月份："))
# if month < 1 or month > 12:
#     print("您的输入有误！")
# elif month >= 10:
#     print("冬天")

# 4.在终端中获取年龄，显示婴儿，0-1   儿童2-13   青少年14-20  成年人21-65
#                             老年人66-150   那是不可能的（150以上）
# while 1:
#     age = input("请输入年龄：")
#     if age == "":
#         break
#     elif int(age) < 0:
#         print("您的输入有误！")
#     elif int(age) <= 1:
#         print("婴儿")
#     elif int(age) <= 13:
#         print("儿童")
#     elif int(age) <= 20:
#         print("青少年")
#     elif int(age) <= 65:
#         print("成年人")
#     elif int(age) <= 150:
#         print("老年人")
#     else:
#
#         print("那是不可能的")

# 5.BMI:用体重（千克）除以身高（米）的平方
#         根据BMI打印身体状况
#         小于18.5（不包含） --> 体重过低
#         18.5(包含) -- 24（不包含）  --> 正常
#         24（包含） -- 28（不包含）  -->  超重
#         28（包含） -- 30(不包含）  -- > 一度肥胖
#         30（包含） -- 40（不包含） ---> 二度肥胖
#         大于等于40   --->    重度肥胖

# while 1:
#     weight = float(input("请输入您的体重："))
#     height = float(input("请输入您的身高："))
#     BMI = weight / height ** 2
#     if BMI <= 0:
#         print("您的数据有误")
#     elif BMI < 18.5:
#         print("体重过低")
#     elif BMI < 24:
#         print("正常")
#     elif BMI < 28:
#         print("超重")
#     elif BMI < 30:
#         print("一度肥胖")
#     elif BMI < 40:
#         print("二度肥胖")
#     else:
#         print("重度肥胖")
