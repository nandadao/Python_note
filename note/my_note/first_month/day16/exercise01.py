"""
    练习
"""

def div_apple(apple_count):
    person_count = int(input("请输入人数："))
    result = apple_count / person_count
    print("每个人%f个苹果" % result)

# 1.统一处理所有异常
try:
    div_apple(10)
except:
    print("出错了")



# 2.针对不同戳无，作出相应的出路逻辑
# try:
#     div_apple(10)
# except ValueError:
#     print("输入的不是整数")
# except ZeroDivisionError:
#     print("0不能作为分母")
# else:
#     print(“否则”)
# print("后端逻辑")


# 3.出错但是解决不了可是具有必须执行的逻辑
# try:
#     div_apple(10)
# finally:
#     print("无论是否一场，都要执行的逻辑")

