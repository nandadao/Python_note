"""
udp_client.py udp客户端流程
"""
from socket import *

# 服务端地址
ADDR = ('127.0.0.1',8888)

# 创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 循环发送消息
while True:
    data = input("Msg>>")
    if not data:
        break
    # 向服务器发送
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("From Server:",msg.decode())
sockfd.close()


