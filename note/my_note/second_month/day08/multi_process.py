"""
多进程
"""
"""
    多线程
"""
from test import *
import multiprocessing as mp
import time

jobs = []
tm = time.time()
for i in range(10):
    t = mp.Process(target=count, args=(1,1))
    jobs.append(t)
    t.start()

[i.join() for i in jobs]

print("Process cpu", time.time()-tm)
# Process cpu 2.108125925064087   计算
# Process cpu 1.322871208190918　　io


















