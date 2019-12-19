"""
模拟僵尸进程产生
"""
import os,sys
from time import sleep
import signal

# 信号处理僵尸进场
signal.signal(signal.SIGCHLD,signal.SIG_IGN)


pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    sleep(4)
    print("Child PID:",os.getpid())
    sys.exit(2)
else:
    """
    os.wait() 处理僵尸进程
    """
    # pid,status = os.wait()
    # print("PID:",pid)
    # print("STATUS:",status) # 退出状态*256
    while True:
        pass
