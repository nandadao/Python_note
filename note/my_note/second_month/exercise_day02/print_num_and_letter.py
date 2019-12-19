"""
### 练习一
写两个线程，一个线程打印1-52，另一个线程打印A-Z, 要求打印顺序：
12A34B56C...5152Z,不能使用sleep进行时间控制。
        提示：
        顺序，要按照同步互斥方法控制
"""

from threading import Thread, Event, Lock
import os

lock1 = Lock()
lock2 = Lock()



def print_num():
    for i in range(1, 53, 2):
        lock1.acquire()
        print(i)
        print(i+1)
        lock2.release()
def print_char():
    chars = [chr(x) for x in range(65, 91)]  # ASCII值
    for i in chars:
        lock2.acquire()
        print(i)
        lock1.release()

t1 = Thread(target=print_num)
t2 = Thread(target=print_char)

lock2.acquire()  # 先让print_char执行

t1.start()
t2.start()
t1.join()
t2.join()
























# 创建事件对象
# e = Event()
# 创建锁对象
# lock = Lock()
#
#
#
# # 设置线程函数
# def print_letter():
#     global s
#     while True:
#         lock.acquire() #上锁
#         if s == "":
#             s += "12"
#             lock.release()  # 解锁
#
#         # elif s[-2] <=50:
#         else:
#             lock.acquire() #上锁
#             s += "%s%s"%(str(s[-2]+1), str(s[-2]+2))
#             lock.release()  # 解锁
#         # elif s[-2] == 52:
#         #     break
#
#
# t = Thread(target=print_letter)
# t.start()
#
#
# count = 65
# while True:
#     if count <= 90:
#         lock.acquire()
#         # 字母转换chr()  ord()
#         # ord("A")= 65, chr(65) = A  ord("Z")=90
#         s += chr(count)
#         print(s)
#         lock.release()
#         count += 1
#         print(s)
#
# # e.wait()  # 阻塞，知道set()解除阻塞
# # t.join()  # 回收线程
# print(s)




# lock = Lock()  # 创建锁对象
#
# def value():
#     global s
#     while True:
#
#         if s == "":
#             lock.acquire() #上锁
#             s += "12"
#             print(s)
#             lock.release() # 解锁
#         else:
#             lock.acquire()
#             # print(s)
#             s += "1"
#             # s += "%s%s"%(str(s[-2]+1), str(s[-2]+2))
#             lock.release()
#             # os._exit(0)
# # 创建线程
# t = Thread(target=value)
# t.start()
# count = 65
# while True:
#     # with lock:  # 上锁，之后自动解锁，
#         # 加锁后下面的程序不能执行，
#         # 只有解锁后才可以执行
#     lock.acquire()
#     s += chr(count)
#     count += 1
#     print(s)
#     lock.release()
#     os._exit(0)
#
#
#
# t.join()
























