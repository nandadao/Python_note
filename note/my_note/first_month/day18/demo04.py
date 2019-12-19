"""
    闭包
        调用函数，在内存中开辟栈帧
        函数执行过后，栈帧释放，局部变量销毁。

        外部函数执行过后，不释放栈帧(留给内部函数使用)
"""


def fun01():
    a= 100
    def fun02():
        print(a)

    return fun02

re = fun01()
re()













