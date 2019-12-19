"""
    函数：功能
    参数：用功能 --> 做功能
    返回值：做功能 --> 用功能
    16：45
"""


def fun01():
    print("fun01执行了")
    return 300  # 返回 数据 --> 结束（退出函数）
    print("fun01又执行了")  # return 后面的代码不执行


re = fun01()
print(re)


def fun02():
    print("fun02执行了")
    # return # return 后面如果没有数据，默认为None


re = fun02()
print(re)  # None
