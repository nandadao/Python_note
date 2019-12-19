from threading import Thread
import time
from random import randint

# 仓库 规定列表中最多存入10个内容
ware = []

# 生产者函数
def produce(name):
    count = 0
    while True:
        print("%s正在生产中..."%name)
        time.sleep(2) # 2sec生产一个
        if len(ware) >= 10:
            print("仓库满了......")
            time.sleep(6)
        else:
            ware.append("good-%d"%count) # 将货物存入仓库
            print("Produce%s做好了一个商品"%name)
            count += 1

def consumer(name):
    while True:
        time.sleep(randint(1,8))
        if len(ware) <= 0:
            print("断货了...")
            time.sleep(4)
        else:
            print("Consumer %s 卖出了%s"%(name,ware.pop(0)))

p1 = Thread(target=produce,args=('呀买碟',))
c1 = Thread(target=consumer,args=('永辉超市',))
c2 = Thread(target=consumer,args=('家乐福超市',))
c3 = Thread(target=consumer,args=('沃尔玛超市',))

p1.start()
c1.start()
c2.start()
c3.start()

p1.join()
c1.join()
c2.join()
c3.join()









