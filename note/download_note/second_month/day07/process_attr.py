"""
进程对象属性
"""
from multiprocessing import Process
import time

def tm():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)

p = Process(target=tm,name='show_time')

# 设置daemon属性 在start之前
p.daemon = True

p.start()
print("Name:",p.name)
print("PID:",p.pid)
print("is alive:",p.is_alive())
time.sleep(1)