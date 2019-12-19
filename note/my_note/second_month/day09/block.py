"""
    block.py 非阻塞IO
"""
from socket import *
from time import ctime, sleep

# 日志文件
f = open("run.log", "a+")



# tcp套接字
sockfd = socket()
sockfd.bind(("127.0.0.1", 8888))
sockfd.listen(3)

# 设置非阻塞
# sockfd.setblocking(False)


# 设置超时时间
sockfd.settimeout(2)



while True:
    sleep(5)
    print("Waiting for connect...")
    try:
        c, addr = sockfd.accept()
    except (BlockingIOError, TimeoutError) as e:
        msg = "%s : %s\n"%(ctime(), e)
        f.write(msg)
    else:
        data = c.recv(1024)






























