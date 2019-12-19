from threading import Thread,Lock
from time import sleep,ctime

ticket = [] # 存储车票
lock = Lock()

for i in range(1,51):
    ticket.append("T%d"%i)

def sell(w):
    while True:
        sleep(0.1)
        with lock:
            if ticket:
                print("%3s窗口%s出售：%3s"%(w,ctime(),ticket.pop(0)))
            else:
                return

jobs = []
for i in range(1,11):
    t = Thread(target=sell,args=('w%d'%i,))
    jobs.append(t)
    t.start()

[i.join() for i in jobs]
