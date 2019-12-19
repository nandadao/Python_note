"""
    求１０００００以内质数之和
    分别使用４个进程和１０个进程做这件事，
    并且分别统计执行时间，进行对比
    提示：
        １－－－２５０００
        ２５００１－－５０００

        １－－１００００
        １０００１－－２００００
"""
from multiprocessing import Process
import time
import os

# 装饰器
def timeis(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print("%s运行时间%.6f"%(f.__name__, end_time-start_time))
        print("res:", res)   # None
        return res
    return wrapper


# 判断一个数是否为质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



# 求质数和，　一个进程
# @timeis
# def no_multi_process():
#     prime = []
#     for i in range(1, 100001):
#         if isPrime(i):
#             prime.append(i)
#     sum(prime)



class Prime(Process):
    def __init__(self, prime, begin, end):
        super().__init__()
        self.prime = prime # 装质数的列表
        self.begin = begin # 开始数值
        self.end = end # 结束数值
    def run(self):
        for i in range(self.begin, self.end):
            if isPrime(i):
                self.prime.append(i)
            sum(self.prime)

# 四个进程　　　use_4_process运行时间11.910304
# 因为，机器是双核的，所以时间只是一个进程的一半
# @timeis
# def use_4_process():
#     prime = []
#     jobs = []
#     for i in range(1, 100001, 25000):   # 1, 25001, 50001, 75001　　一共是个值
#         p = Prime(prime, i, i+25000)
#         jobs.append(p)
#         p.start()
#
#     [i.join() for i in jobs]  # 列表推到式

# 十个进程，　use_10_process运行时间8.093432，　为什么会少３秒
@timeis
def use_10_process():
    prime = []
    jobs = []
    for i in range(1, 100001, 10000):   # 1, 25001, 50001, 75001　　一共是个值
        p = Prime(prime, i, i+10000)
        jobs.append(p)
        p.start()

    [i.join() for i in jobs]  # 列表推到式


if __name__ == '__main__':
    # no_multi_process()
    # use_4_process()
    use_10_process()
# no_multi_process运行时间26.439729
# 一个进程时间








# def prime(start , stop):
#     num = []
#     for i in range(start, stop):
#         for j in range(2, i):
#             if (i % j) == 0:
#                 break
#         else:
#             num.append(i)
#             # yield i
#
#     return num
#
# def fun1():
#     print(stop)
# def fun2():
#     print(stop)
# def fun3():
#     print(stop)
# def fun4():
#     print(stop)
#
#
# fun = [fun1, fun2, fun3, fun4]
#
# p_list = []
# for i in fun:
#     p = Process(target=i)
#     p_list.append(p)
#     p.start()
#
# for i in p_list:
#     i.join()






















