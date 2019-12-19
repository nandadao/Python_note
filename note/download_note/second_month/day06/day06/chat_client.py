"""
chat room client
"""
from socket import *
import os

# 服务器地址
ADDR = ('127.0.0.1',8888)

# 客户端启动函数
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    # 进入聊天室部分
    while True:
        name = input("请输入姓名:")
        msg = "L "+name
        s.sendto(msg.encode(),ADDR)
        # 得到结果
        data,addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break
        else:
            print('进入聊天室失败')

if __name__ == '__main__':
    main()