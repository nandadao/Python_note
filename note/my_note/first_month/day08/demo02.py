""
"""
    # 局部变量 ，在函数内部的变量，只能在函数内部访问的
"""

# print = 100
def fun01():
    a = 10  # 局部变量
    print(10)

fun01()
g01 = 500  # 全局变量


def fun02():
    # 再局部作用域中，可以访问全局变量
    # print(g01)
    # 声明全局变量
    global g01
    g01 = 600

    # global g02        :不建议这样定义
    # g02 = 60


fun02()
print(g01)
print(g02)

print()










