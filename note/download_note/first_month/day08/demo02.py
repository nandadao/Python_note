"""
    作用域
    练习:exercise03
"""


def fun01():
    # 局部变量：只能在函数内部访问
    a = 10
    print(a)


# 全局变量：在整个文件中可以访问
g01 = 500


def fun02():
    # 在局部作用域中，可以读取全局变量
    # print(g01)
    # 声明全局变量
    global g01
    g01 = 600
    # 声明全局变量(创建全局变量)不建议
    # global g02
    # g02 = 700


fun02()
print(g01)
# print(g02)
