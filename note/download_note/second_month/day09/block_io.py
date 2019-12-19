"""
非阻塞IO演示
"""
from socket import *
from time import ctime,sleep

# 日志文件
f = open('run.log','a+')

# tcp套接字
sockfd = socket()
sockfd.bind(('127.0.0.1',8888))
sockfd.listen(3)

# 设置非阻塞
# sockfd.setblocking(False)

# 设置超时时间
sockfd.settimeout(2)

while True:
    sleep(3)
    print("Waiting for connect...")
    try:
        c,addr = sockfd.accept()
    except (BlockingIOError,timeout) as e:
        msg = "%s : %s\n"%(ctime(),e)
        f.write(msg)
        f.flush()
    else:
        data = c.recv(1024)
