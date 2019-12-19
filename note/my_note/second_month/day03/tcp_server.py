"""
    tcp_server.py
    服务端
"""

import socket

# 创建套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(("0.0.0.0", 9997))

# 设置监听
sockfd.listen(3)   # 3这个值设置多少都无所谓，因为linux已经自动设置了

# 处理客户端连接
print("Waiting for connect ...")
connfd, addr = sockfd.accept()
print("Connect from", addr)

# 收发消息
data = connfd.recv(1024)
print("Recv:", data.decode())

n = connfd.send(b"OK\n")    # 一定要发送字节串

# 关闭套接字
connfd.close()
sockfd.close()


# 本地连接
# telnet 127.0.0.1 9999
















