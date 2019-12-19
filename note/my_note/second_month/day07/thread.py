"""
    创建多线程基础使用
    thread1.py
"""
import threading
from time import sleep
import os

a = 1

# 线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放黄河大合唱")
    global a
    print("a=", a)
    a = 10000

# 创建线程对象
t = threading.Thread(target=music)
t.start() # 启动线程,start之后才是真正创建线程
for i in range(4):
    sleep(1)
    print(os.getpid(),"播放葫芦娃")
t.join()
print("a:", a)





























