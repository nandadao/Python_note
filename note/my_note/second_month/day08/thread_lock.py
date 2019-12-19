"""
    线程锁 thread_lock
"""
from threading import Thread,Lock

a = b = 0  # 共享资源
lock = Lock()  # 创建锁对象

def value():
    while True:
        lock.acquire() #上锁
        if a == b:
            print("a = %d, b = %d"%(a, b))
        lock.release() # 解锁

# 创建线程
t = Thread(target=value)
t.start()
while True:
    with lock:  # 上锁，之后自动解锁，
        # 加锁后下面的程序不能执行，
        # 只有解锁后才可以执行
        a += 1
        b += 1
        print("a+1:", a+1)
        break


t.join()























