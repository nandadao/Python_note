"""
    自定义线程类
"""
from threading import Thread
from time import sleep, ctime


class MyThread(Thread):
        def __init__(self, target=None, args=(), kwargs={}):
            # 此行不许动
            super().__init__()  # 用super调用父类的__init__
            self.target = target
            self.args = args
            self.kwargs = kwargs


        def run(self):
            # 函数传参，星号元组传参，双星号字典传参
            self.target(*self.args, **self.kwargs)



# ===================================
# 这个是一个测试函数
def player(sec, song):  # 这里可以随便，可能有参数，可能没有参数
    for i in range(3):
        print("Playing %s:%s"%(song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(2,),
             kwargs={"song":"凉凉"})
t.start()
t.join()










