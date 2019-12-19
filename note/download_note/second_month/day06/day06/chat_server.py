"""
chat room  AID 1910
env: python3.6
author: Levi
socket udp  & fork
"""
from socket import *
import os,sys

# 服务地址
ADDR = ('0.0.0.0',8888)

# 存储用户  {name:address}
user = {}

# 进入处理
def do_login(s,name,addr):
    if name in user:
        s.sendto(b'FAIL',addr)
        return
    s.sendto(b'OK',addr)

    # 通知其他人
    msg = "欢迎%s进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    # 将其添加到用户字典
    user[name] = addr

# 功能分发函数
def do_request(s):
    while True:
        # 循环接受请求
        data,addr = s.recvfrom(1024)
        tmp = data.decode().split(' ')
        # 根据请求类型，选择功能模块去处理
        # L   C   Q
        if tmp[0] == 'L':
            do_login(s,tmp[1],addr) # 具体函数处理具体功能


# 启动函数
def main():
    # udp网络服务
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    do_request(s)


if __name__ == '__main__':
    main()
