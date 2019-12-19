"""
    process_server.py  基于proces多进程
    重点代码
"""
import sys
from socket import *
import os
import signal
from threading import Thread
from multiprocessing import Process


ADDR = ("0.0.0.0", 8888)



# 处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("收到消息：", data.decode())
        c.send("服务端发给客户端的消息".encode())
    c.close()



# 创建tcp套接字
s = socket()
# 复用端口
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

signal.signal(signal.SIGCHLD, signal.SIG_IGN)


print("Listen the port 8888...")
n = 0
# 循环接收客户端连接
while True:
    try:
        c, addr = s.accept()
        print("Connect from ", addr )
        n += 1
        print("已连接数量:", n)
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    # 创建多进程
    p = Process(target=handle, args=(c, ))
    p.daemon = True
    p.start()
















