
# 函数式编程的理论支柱

# 1.理论支柱一：把函数赋值给变量
def fun01():
    print("fun01执行了")

a = fun01
a()

def fun02():
    print("fun02执行了")

# 2.允许将函数作为参数传入另一个函数
def fun03(func):
    print("fun03执行了")
    func()

fun03(fun01)








