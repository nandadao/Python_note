"""
    多线程
"""
from test import *
import threading
import time

jobs = []
tm = time.time()
for i in range(10):
    t = threading.Thread(target=count, args=(1,1))
    jobs.append(t)
    t.start()

[i.join() for i in jobs]

print("Thread cpu", time.time()-tm)
# Thread cpu 11.624666452407837   计算
# Thread cpu 7.001250743865967   io

















