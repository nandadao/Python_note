"""
    在不改变fun01和fun02函数定义和调用的情况下
        为增加新功能(打印函数执行时间)  开始时间-结束时间
            如何记录开始与结束时间
"""
import time


# def print_func_name(func):
#     def wrapper(*args, **kwargs):  # 合
#         print(func.__name__)
#         return func(*args, **kwargs)   # 拆
#     return wrapper

# 使用装饰器，拦截对旧功能的调用
# 将新功能与旧功能包装在一起
def print_execute_tiem(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # func -- 旧功能
        re = func(*args, **kwargs)
        stop_time = time.time()
        # 新功能 -- 打印执行时间
        print(stop_time - start_time)
        return re
    return wrapper



@print_execute_tiem  # print_execute_tiem(func01)
def fun01():
    time.sleep(2)  # 睡2秒, 用于模拟计算2秒钟

@print_execute_tiem
def fun02(a):
    time.sleep(3)

fun01()
fun02(10)




