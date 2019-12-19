""
"""
    函数：功能
    参数：用功能  -->  做功能
    返回值：做功能 -- > 用功能
"""

def fun01():
    print("fun01执行了")
    return 100 #  返回数据，结束函数（return 后面的代码不会执行，退出方法）
    print("fun01又执行了")

def fun02():
    print("fun02")


re = fun01()
print(re)

re1 = fun02()
print(re1)









