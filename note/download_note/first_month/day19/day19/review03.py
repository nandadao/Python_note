"""
    python 核心
        迭代器  -->  生成器
                   惰性/延迟

        def 函数名():
            yield

        生成器 = 函数名()
        for item in 生成器:

        函数式编程：
            函数作为参数：将核心逻辑传入函数。
            函数作为返回值：闭包 --> 装饰器

        装饰器：在不改变原有函数定义与调用情况下，为其增加新功能。
            核心思想：拦截
"""
import time

# 外层函数价值：拦 -->  拦截对旧功能的调用
# 内层函数价值：包 -->  将新旧功能包在一起
def print_execute_time(func):
    def wrapper(*args, **kwargs):# 合 --> 让调用旧功能的实参数量无限
        start_time = time.time()
        # func -- 旧功能
        re = func(*args, **kwargs)# 拆  --> 将实参拆分后与旧功能的形参对应
        stop_time = time.time()
        # 新功能 -- 打印执行时间
        print(stop_time - start_time)
        return re

    return wrapper

@print_execute_time# fun01 =  print_execute_time(fun01)
def fun01():
    time.sleep(2)  # 睡眠2秒，用于模拟计算2秒钟


def fun02(a):
    time.sleep(3)  # 睡眠3秒
    return "ok"

# fun01 指向的是内层函数 wrapper
# fun01 =  print_execute_time(fun01)# 调用外层函数，返回内层函数。

fun01()# 调用的是内层函数

# fun02 =  print_execute_time(fun02)# 调用外层函数，返回内层函数。
re = fun02(100)
print(re)



class Wife:
    def __init__(self, age=0):
        self.age = age

    @property# age = property(age,None)
    def age(self):
        return self.__age



w01 = Wife(20)
print(w01.age)
