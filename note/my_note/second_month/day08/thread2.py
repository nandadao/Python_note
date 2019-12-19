"""
    线程创建实力２
"""
from threading import Thread
from time import sleep


#　含有参数的线程函数
def fun(sec, name):
    print("线程函数参数")
    sleep(sec)  # sleep几秒钟，就让出了cpu核心
    print("%s执行完毕"%name)

# 同时创建五个线程
jobs = []
for i in range(5):
    t = Thread(target=fun, args=(2, ),
               kwargs={"name":"T%d"%i})
    jobs.append(t)  # 把每个线程放到jobs列表中
    t.start()

# 回收线程
for i in jobs:
    i.join()


























