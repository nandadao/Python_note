"""
    exercise_thread_server.py  基于threading多线程并发
    重点代码
"""
import sys
from socket import *
import os
import signal
from threading import Thread

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

print("Listen the port 8888...")
# 循环接收客户端连接
while True:
    try:
        c, addr = s.accept()
        print("Connect from ", addr )
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    # 创建线程
    t = Thread(target=handle, args=(c, ))
    t.setDaemon(True)
    t.start()
















