"""
    ### 练习二
模拟生产，入库，销售场景
假定企业，自产，自存，自销。将工厂生产的产品不定时的运到仓库，
与此同时，仓库货物需要运到商场销售。请编一个程序模拟这个过程。
(主要是对仓库的存取过程)。
要求：
１．仓库的可存量，可以设置为一个常量，比如　max = 10
２．仓库满的时候不能向仓库存入东西
３．仓库空的时候则不能向商场提供货物
４．写多线程分别表达货物的存储和提取，而这两个操作是同时进行的
５．不能出现，先存满再取完，或者先取完再存满的情况
"""

from threading import Thread, Lock, Event
import time
from random import  randint

# 仓库  规定列表中最多存入10个内容
ware = []

# 生产者函数
def produce(name):
    count = 0
    while True:
        print("%s正在生产中..."%name)
        time.sleep(2)  # 2秒生产一个
        if len(ware) >= 10:
            print("仓库满了......")
            time.sleep(5)
        else:
            ware.append("good-%d"%count)  # 将货物存入仓库
            print(ware)
            print("Produce%s做好了一个商品"%name)
            count += 1

# 消费者函数
def consumer(name):
        while True:
            time.sleep(randint(1, 8))
            if len(ware) <= 0:
                print("断货了...")
                time.sleep(4)
            else:
                print("Consumer %s 卖出了%s"%(name, ware.pop(0)))

p1 = Thread(target=produce, args=("牙买碟", ))
c1 = Thread(target=consumer, args=("永辉超市", ))
c2 = Thread(target=consumer, args=("家乐福超市", ))
c3 = Thread(target=consumer, args=("沃尔玛超市", ))

p1.start()
c1.start()
c2.start()
c3.start()

p1.join()
c1.join()
c2.join()
c3.join()








































