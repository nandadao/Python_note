"""
    模拟僵尸进程的产生
"""
import os, sys
from time import sleep
import signal

# 信号处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:", os.getpid())  # 获取进程的pid号
    sleep(4)
    # sys.exit(2)
else:
    """
        os.wait() 处理僵尸进程
    """
    # pid, status = os.wait()   # 这里阻塞父进程，等子进程执行完成再执行下面的程序
    print("PID:", pid)
    # print("STATUS:", os.WEXITSTATUS(status))  # 退出状态*256
    while True:  # 目的，让父进程挂起不退出
        pass

