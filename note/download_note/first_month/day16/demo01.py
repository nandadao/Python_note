"""
    异常处理
    10:10
"""
# 常见错误类型
# print(qtx)
# print("结果是："+10)
# print([1,2,3][10])

# class MyClass:
#     pass
# c01 = MyClass()
# print(c01.qtx)

# print({"a":1}["b"])


def div_apple(apple_count):
    person_count = int(input("请输入人数："))  # ValueError
    result = apple_count / person_count  # ZeroDivisionError
    print("每个人%f个苹果" % result)


# 1. 统一处理所有异常
try:
    div_apple(10)
except:
    print("出错啦")

# 2.针对不同错误，做出相应的处理逻辑
# try:
#     div_apple(10)
# except ValueError:
#     print("输入的不是整数")
# except ZeroDivisionError:
#     print("0不能作为分母")

# 3. 没有错误的逻辑 + 出错的逻辑
# try:
#     div_apple(10)
# except ValueError:
#     print("输入的不是整数")
# except ZeroDivisionError:
#     print("0不能作为分母")
# else:
#     print("没有错误的逻辑")

# 4.出错但是解决不了，可是具有必须执行的逻辑。
# try:
#     div_apple(10)
# finally:
#     print("无论是否异常，都要执行的逻辑")

print("后续逻辑")
