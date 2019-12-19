"""
fork_server  基于fork的多进程网络并发
    重点代码
"""
from socket import *
import os

# 定义全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 创建套接字TCP
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # 设置套接字的端口重用
s.bind(ADDR)
s.listen(3)

print("Listen the port 8888...")


def handle(c):
    pass


while True:
    # 循环接收客户端的连接
    try:
        c, addr = s.accept()
        print("Connect from ", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 客户端连接处理
    pid = os.fork()
    if pid == 0:
        # 处理请求
        handle(c)  # 处理具体请求,用套接字与客户端连接
        os._exit(0) # 子进程退出
        # 处理完请求子进程结束
    else:
        continue # 父进程循环回去继续等待其他客户端




















