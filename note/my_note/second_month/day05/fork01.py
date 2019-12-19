"""
    fork例子２
"""
import os
from time import sleep

# 这里只执行一遍，因为子进程执行从fork后面开始执行
print("======================")

a = 1
# 创建子进程
pid = os.fork()
if pid < 0:
    print("Create process failed")
elif pid == 0:
    # 这里是子进程执行部分
    print("Child process")
    print("a=", a)  # 从父进程拷贝了内存a的值
    a = 1000  # 只修改自己的内存空间a
else:
    sleep(1)
    # 父进程执行部分
    print("Parent process")
    print("a=", a)

print("All a=", a)  # 父子进程都执行一遍





















