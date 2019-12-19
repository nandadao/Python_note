"""
    自定义进程类
"""
from multiprocessing import Process
from time import sleep, ctime

class MyProcess(Process):
    def __init__(self, value):
        self.value = value
        super().__init__()   # 引用父类方法

    def fun1(self):
        # sleep(1)
        print("第一步")

    def fun2(self):
        # sleep(0.8)
        print("第二步")

    # 调用start会运行run
    def run(self):  # 这里的标记代表，重写
        for i in range(self.value):
            self.fun1()
            self.fun2()


p = MyProcess(2)
p.start()  # 调用start后，启动run()进程
p.join()






















