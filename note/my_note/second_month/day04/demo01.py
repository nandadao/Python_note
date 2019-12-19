"""
    套接字属性
"""
from socket import *

s = socket()

# 设置端口立即重用
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)


s.bind(("127.0.0.1", 9999))
s.listen(3)
c, addr = s.accept()


print("套接字类型：", s.type)
print("套接字地址类型：", s.family)
print("绑定地址：", s.getsockname())
print("文件描述符：", s.fileno())
print("客户端地址：", c.getpeername())
print("设置")

c.recv(1024)










