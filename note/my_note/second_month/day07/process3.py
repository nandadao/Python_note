"""
    process
    给进程函数传参
"""
from multiprocessing import *
from time import sleep


# 带有参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

# args里面按照位置传参
# p = Process(target=worker, args=(2, "Levi"))
# 关键字字典传参
# p = Process(target=worker, kwargs={"sec":2, "name":"Levi"})
# 混合使用args和kwargs传参
p = Process(target=worker, args=(2,), kwargs={"name":"Levi"})


p.start()
p.join()











