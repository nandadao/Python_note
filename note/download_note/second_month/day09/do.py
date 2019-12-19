
"""
基于threading 多线程并发
"""
from socket import *
from threading import Thread
import sys

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"OK")
    c.close()



# 创建tcp套接字
s = socket()
# 设置端口复用
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

print("Listen the port 8888...")

# 循环接收客户端连接
while True:
    try:
        c, addr = s.accept()
        print("Connect from ", addr)
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    # 创建线程处理
    t = Thread(target=handle, args=(c, ))
    # setDaemon(True)设置主线程退出其他线程也退出
    t.setDaemon(True)
    t.start()


































