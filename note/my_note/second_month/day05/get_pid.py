"""

"""
import os
from time import sleep


pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    sleep(1)
    print("Child PID:", os.getpid())  # 获取子进程pid
    print("Get Parent PID:", os.getppid())  # 子进程获取父进程的PID
else:
    print("Get child PID:", pid)  # 这里的pid=os.getpid()
    print("Parent PID:", os.getpid())  # 父进程获取自己的pid
