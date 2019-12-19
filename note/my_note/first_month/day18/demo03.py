"""
    Enclosing 外部嵌套作用域
"""

def fun01():
    a= 10 # 局部变量，外部嵌套变量
    def fun02():
        b=20
        # print(a)  # 可以读取外部嵌套变量
        nonlocal a # 声明外部嵌套变量
        a = 20
    fun02()
    print(a)

fun01()















