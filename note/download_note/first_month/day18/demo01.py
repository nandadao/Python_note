"""
    lambda 匿名函数：
        语法：lambda 参数:函数体
        价值：作为实参传递给函数
"""
# 有参数 有返回值
# def fun01(a):
#     return a == "ok"
#
#
# re = fun01("ok")
# print(re)

# 形参 = 实参
fun01 = lambda a: a == "ok"
# 函数体
re = fun01("ok")
print(re)


# 有多参数 有返回值
# def fun02(a, b, c):
#     return a == b == c


fun02 = lambda a, b, c: a == b == c
re = fun02(1, 2, 3)
print(re)


# 没参数 有返回值
# def fun03():
#     return "ok"

fun03 = lambda :"ok"
re = fun03()
print(re)


# 没参数 没返回值
# def fun04(a):
#     print(a)


fun04 = lambda a:print(a)
fun04("ok")

# def fun05(a):
#     a[0] = 10
#
# list01 = [1]
# fun05(list01)
# print(list01)#?

# lambda 表达式不能赋值
# fun05 = lambda a:a[0] = 10

def fun06(a):
    print("a")
    return a == "ok"

# lambda 表达式只支持一行语句
# fun06 =lambda a:(
#     print("a")
#     a == "ok"
# )

















