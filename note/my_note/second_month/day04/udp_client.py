"""
    服务端
"""
from socket import *

# 服务端地址
ADDR = ("0.0.0.0", 9999)

#　创建udp套机字
sockfd = socket(AF_INET, SOCK_DGRAM)


while True:
    data = input(">>")
    if not data:
        break
    # 向服务器发送
    n = sockfd.sendto(data.encode(), ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print("From Server:", msg.decode())


sockfd.close()






















