"""
    ### 练习三
模拟窗口卖票，有十个窗口，(w1...w10)，同时开放售票，一共有50张票
(T1--T50)，需要按照顺序出售(先到先得)
要求：
１．输出每一张票的出售时间和窗口，不能出现票未出售或者出现出售多次的情况
２．窗口开放之前，票存储在一个容器中（容器自己定）
提示：
１．使用多线程的同步互斥方法解决问题，输出结果
２．每个线程模拟售票情景(用函数还是用类自己思考)
３．将票的存储提前定一个合理的结构(类或者容器)
"""
from threading import Thread, Lock
from time import ctime,sleep
from random import randint
lock = Lock()

ticket = []  # 存储车票

for i in range(1, 51):
    ticket.append("T%d"%i)


# 卖票线程
def sell(w):
    while True:
        sleep(0.1)
        with lock:
            if ticket:
                print("%3s窗口%s出售：%3s"%(w, ctime(), ticket.pop(0)))
                continue
            return # 结束线程

# 创建线程
jobs = []
for i in range(1, 11):
    t = Thread(target=sell, args=("w%d"%i,))
    jobs.append(t)
    t.start()



# 回收线程
[i.join() for i in jobs]



































# 自己写的
# lock1 = Lock()
# lock2 = Lock()
#
# # 车票存在一个列表中
# tickets = ["T%d"%i for i in range(1, 51)]
# windows = ["w%d"%i for i in range(1, 11)]
#
# # 还剩多少票
# # def tick():
# #     tickets.remove(tickets[0])
#
# # 模拟窗口
#
# def sale_ticks():
#     for i in tickets:
#         lock1.acquire()
#         print("%s时间 出售一张票%s"%(ctime(), i))
#
# # 创建线程  创建10个窗口
# jobs = []
# for i in range(10):
#     t = Thread(target=sale_ticks)
#     jobs.append(t)
#     t.start()
#
# # while True:
# #     sale_ticks()
#
# # 回收线程
# [i.join() for i in jobs]












































