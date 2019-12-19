from time import sleep
import os,sys


def fun1():
    for i in range(3):
        sleep(2)
        print("写代码")


def fun2():
    for i in range(2):
        sleep(4)
        print("测代码")

# 不希望产生僵尸

p1 = os.fork()

if p1 == 0:
    p2 = os.fork()
    if p2 == 0:
        fun2()# 二级子进程
    else:
        os._exit(0)   #　一级子进程退出

else:
    # print("Parent")
    p1, status = os.wait()  # 等待pid子进程退出
    fun1()



















